import assert from 'node:assert/strict';
import { createHash } from 'node:crypto';
import { spawnSync } from 'node:child_process';
import { cp, mkdir, mkdtemp, readFile, rm, writeFile } from 'node:fs/promises';
import { tmpdir } from 'node:os';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';
import { NativeRouter, Router, resolveRouterBackend, trainNativeRouter } from '@metaharness/router';

const pins = { '@metaharness/router': '0.4.1', '@ruvector/tiny-dancer': '0.1.26' };
const modelA = [1, 0, 0, 0, 0];
const modelB = [0, 1, 0, 0, 0];
const prices = { small: 1, large: 15 };
const tasks = [
  { embedding: [0.9, 0.1, 0, 0, 0], expected: 'small' },
  { embedding: [0.1, 0.9, 0, 0, 0], expected: 'large' },
];
const candidates = [{ id: 'small', embedding: modelA }, { id: 'large', embedding: modelB }];
const rows = Array.from({ length: 64 }, (_, i) => {
  const a = i % 2 === 0;
  const drift = i / 1000;
  return {
    embedding: a ? [1, drift, 0, 0, 0] : [drift, 1, 0, 0, 0],
    scores: { small: a ? 0.95 : 0.35, large: 0.96 },
  };
});

if (process.argv.length === 4 && process.argv[2] === '--train') {
  const result = await trainNativeRouter(rows, prices, {
    outputPath: process.argv[3], hiddenDim: 8, epochs: 20,
  });
  assert.ok(result.modelBytes > 0);
} else {
  assert.equal(process.argv.length, 2, 'run the recipe without arguments');
  await verify();
}

async function verify() {
  for (const [name, version] of Object.entries(pins)) {
    const manifest = new URL(`./node_modules/${name}/package.json`, import.meta.url);
    assert.equal(JSON.parse(await readFile(manifest, 'utf8')).version, version);
  }
  const dir = await mkdtemp(join(tmpdir(), 'ruvnet-native-routing-'));
  try {
    assert.equal(await resolveRouterBackend('auto'), 'native');
    const model = join(dir, 'router.safetensors');
    const trained = spawnSync(process.execPath, [fileURLToPath(import.meta.url), '--train', model], {
      encoding: 'utf8', timeout: 30_000,
    });
    if (trained.error) throw trained.error;
    assert.equal(trained.status, 0, trained.stderr || trained.stdout);
    const native = await NativeRouter.load({ modelPath: model, enableCircuitBreaker: false });
    const js = new Router({
      k: 1, qualityBar: 0.8,
      candidates: [
        { id: 'small', costPerMTok: prices.small, examples: [
          { embedding: modelA, quality: 0.95 }, { embedding: modelB, quality: 0.35 },
        ] },
        { id: 'large', costPerMTok: prices.large, examples: [
          { embedding: modelA, quality: 0.96 }, { embedding: modelB, quality: 0.96 },
        ] },
      ],
    });

    // Exercise backend auto-detection in a separate process with the same published
    // router files, outside the native dependency tree.
    const isolatedRouter = join(dir, 'node_modules', '@metaharness', 'router');
    await mkdir(dirname(isolatedRouter), { recursive: true });
    await cp(new URL('./node_modules/@metaharness/router/', import.meta.url), isolatedRouter, { recursive: true });
    const probe = join(dir, 'fallback.mjs');
    await writeFile(probe, "import { resolveRouterBackend } from '@metaharness/router'; console.log(await resolveRouterBackend('auto'));\n");
    const fallback = spawnSync(process.execPath, [probe], { encoding: 'utf8', timeout: 30_000 });
    if (fallback.error) throw fallback.error;
    assert.equal(fallback.status, 0, fallback.stderr);
    assert.equal(fallback.stdout.trim(), 'js');

    const comparisons = [];
    for (const task of tasks) {
      const scored = await native.route(task.embedding, candidates);
      assert.equal(scored.id, task.expected);
      assert.ok(Number.isFinite(scored.confidence));
      const routed = js.route(task.embedding);
      assert.equal(routed.id, task.expected);
      comparisons.push({ expected: task.expected, native: scored.id, js: routed.id });
    }

    const sha = async (url) => createHash('sha256').update(await readFile(url)).digest('hex');
    console.log(JSON.stringify({
      candidate: 'native-routing-v1', pins, platform: `${process.platform}/${process.arch}`, node: process.version,
      lock_sha256: await sha(new URL('./package-lock.json', import.meta.url)),
      recipe_sha256: await sha(new URL(import.meta.url)),
      checks: { 'native-path': true, 'typescript-fallback': true, 'fixed-task-comparison': true },
      result: { comparisons, fixture_only: true },
    }, null, 2));
  } finally {
    await rm(dir, { force: true, recursive: true });
  }
}
