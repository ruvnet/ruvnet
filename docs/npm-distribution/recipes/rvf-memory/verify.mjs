import assert from 'node:assert/strict';
import { createHash } from 'node:crypto';
import { spawnSync } from 'node:child_process';
import { mkdtemp, readdir, readFile, rm } from 'node:fs/promises';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { fileURLToPath } from 'node:url';
import { createRvfBackend } from '@metaharness/kernel/memory-rvf';

const namespace = 'example';
const pins = { '@metaharness/kernel': '0.1.8', '@ruvector/rvf': '0.4.12' };
const input = [1, 0, 0, 0];
const wanted = 'release-notes';

async function stage(action, dir) {
  const store = await createRvfBackend({ dimensions: 4, dir, metric: 'cosine' });
  assert.ok(store?.persistent, 'RVF did not open a persistent backend');
  try {
    if (action === 'write') {
      await store.insertBatch([
        { id: 'distractor', embedding: input, metadata: { kind: 'draft' } },
        { id: wanted, embedding: [0.8, 0.2, 0, 0], metadata: { kind: 'verified' } },
      ], namespace);
      assert.equal(await store.size(namespace), 2);
      assert.ok(store.metadataSupported, 'RVF did not store metadata');
    } else {
      assert.equal(await store.size(namespace), 2, 'entries did not survive restart');
      const unfiltered = await store.search(input, 2, namespace, { exact: true });
      assert.deepEqual(unfiltered.map(hit => hit.id), ['distractor', wanted]);
      const hits = await store.search(input, 2, namespace, {
        exact: true, filter: { op: 'eq', field: 'kind', value: 'verified' },
      });
      assert.deepEqual(hits.map(hit => hit.id), [wanted], 'filter must exclude the closer draft');
      assert.equal(hits[0].metadata?.kind, 'verified');
    }
  } finally {
    await store.close();
  }
}

if (process.argv.length === 4 && ['write', 'read'].includes(process.argv[2])) {
  await stage(process.argv[2], process.argv[3]);
} else {
  assert.equal(process.argv.length, 2, 'run the recipe without arguments');
  for (const [name, expected] of Object.entries(pins)) {
    const manifest = new URL(`./node_modules/${name}/package.json`, import.meta.url);
    assert.equal(JSON.parse(await readFile(manifest, 'utf8')).version, expected);
  }

  const dir = await mkdtemp(join(tmpdir(), 'ruvnet-rvf-memory-'));
  try {
    for (const action of ['write', 'read']) {
      const result = spawnSync(process.execPath, [fileURLToPath(import.meta.url), action, dir], {
        encoding: 'utf8', timeout: 30_000,
      });
      if (result.error) throw result.error;
      assert.equal(result.status, 0, `${action} failed: ${result.stderr}`);
      assert.ok((await readdir(dir)).includes(`${namespace}.rvf`), 'no RVF file was created');
    }

    const lock = await readFile(new URL('./package-lock.json', import.meta.url));
    console.log(JSON.stringify({
      candidate: 'rvf-memory-v1', pins,
      platform: `${process.platform}/${process.arch}`, node: process.version,
      lock_sha256: createHash('sha256').update(lock).digest('hex'),
      recipe_sha256: createHash('sha256').update(await readFile(new URL(import.meta.url))).digest('hex'),
      checks: { 'rvf-active': true, 'restart-persistence': true, 'metadata-filter': true },
      result: { persisted: 2, retrieved: wanted, excluded: 'distractor' },
    }, null, 2));
  } finally {
    await rm(dir, { force: true, recursive: true });
  }
}
