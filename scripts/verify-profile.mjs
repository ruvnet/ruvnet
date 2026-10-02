// Cross-check the public claims against their captured inputs. No network or dependencies.
import fs from 'node:fs';
import path from 'node:path';
import assert from 'node:assert/strict';
import { createHash } from 'node:crypto';
import { fileURLToPath } from 'node:url';
const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const read = p => fs.readFileSync(path.join(root, p), 'utf8');
const json = p => JSON.parse(read(p));
const format = n => new Intl.NumberFormat('en-US').format(n);
const github = json('data/github-stats.json');
const inventory = json(github.inventory);
const owned = inventory.repositories.filter(r => !r.fork);
assert.equal(new Set(inventory.repositories.map(r => r.full_name)).size, inventory.repositories.length);
const expected = {
  followers: inventory.user.followers,
  public_repositories: inventory.repositories.length,
  owned_public_nonfork_repositories: owned.length,
  public_forks: inventory.repositories.length - owned.length,
  stars_across_owned_nonfork: owned.reduce((n, r) => n + r.stargazers_count, 0),
  aggregate_downstream_forks_of_owned_nonfork: owned.reduce((n, r) => n + r.forks_count, 0)
};
assert.deepEqual(github.account, expected);
assert.equal(inventory.user.public_repos, expected.public_repositories);
const readme = read('README.md');
const githubBlock = readme.split('<!-- github-public-metrics:start -->')[1].split('<!-- github-public-metrics:end -->')[0];
for (const value of Object.values(expected)) assert.ok(githubBlock.includes(`| ${format(value)} |`), `README GitHub value ${value}`);
const metrics = json('data/metrics.json');
const registry = json('data/registry-stats.json');
const npm = registry.npm, crates = registry.crates_io;
assert.equal(metrics.counts.github_public_repositories, expected.public_repositories);
assert.equal(metrics.counts.github_stars_owned_nonfork, expected.stars_across_owned_nonfork);
assert.equal(metrics.counts.npm_packages, npm.package_count);
assert.equal(metrics.counts.rust_crates, crates.crate_count);
assert.equal(metrics.counts.rust_crate_downloads_cumulative, crates.cumulative_downloads);
assert.equal(metrics.counts.published_registry_and_huggingface_artifacts_minimum, npm.package_count + crates.crate_count + metrics.counts.pypi_packages + metrics.counts.huggingface_models_and_spaces);
assert.equal(metrics.current_windows.npm_downloads_rolling_365_days, npm.downloads);
assert.equal(metrics.current_windows.npm_download_package_count, npm.download_package_count);
assert.equal((Date.parse(npm.period_end) - Date.parse(npm.period_start)) / 86400000 + 1, 365);
assert.equal(npm.monthly_downloads.length, 12);
assert.equal(npm.monthly_downloads[0].month, npm.monthly_period_start.slice(0, 7));
assert.equal(npm.monthly_downloads.at(-1).month, npm.monthly_period_end.slice(0, 7));
if (npm.inventory_path) assert.equal(json(npm.inventory_path).packages.length, npm.package_count);
if (crates.inventory_path) {
  const list = json(crates.inventory_path).crates;
  assert.equal(list.length, crates.crate_count);
  assert.equal(list.reduce((n, c) => n + c.downloads, 0), crates.cumulative_downloads);
}
const packageBlock = readme.split('<!-- package-public-metrics:start -->')[1].split('<!-- package-public-metrics:end -->')[0];
for (const value of [npm.package_count, npm.downloads, crates.crate_count, crates.cumulative_downloads]) assert.ok(packageBlock.includes(format(value)), `README registry value ${value}`);
assert.ok(packageBlock.includes(npm.downloads_verified_at.slice(0, 10)));
const newProjects = json('data/snapshots/2026-10-02/new-projects.json').repositories;
assert.equal(newProjects.length, 6);
const projects = json('data/projects.json').projects;
for (const item of newProjects) {
  assert.ok(item.roots.length > 0);
  assert.match(item.head_sha, /^[0-9a-f]{40}$/);
  assert.ok(projects.some(p => p.source_commit === item.head_sha));
  assert.ok(readme.includes(item.readme_source));
}
const proof = json('data/proof-2026-10-02.json');
assert.ok(proof.files.length >= 6);
for (const file of proof.files) {
  assert.equal(createHash('sha256').update(fs.readFileSync(path.join(root, file.path))).digest('hex'), file.sha256, `Snapshot hash: ${file.path}`);
}
for (const source of proof.sources) {
  assert.match(source.commit, /^[0-9a-f]{40}$/);
  assert.ok(source.url.includes('/blob/' + source.commit + '/'));
  assert.match(source.sha256, /^[0-9a-f]{64}$/);
}
// Only local Markdown links: historical external availability is not inferred.
const docs = ['README.md', 'docs/proof/2026-10-02.md', 'docs/ruvnet-prior-art.md', 'docs/ruvnet-packages.md'];
let links = 0;
for (const doc of docs) {
  for (const match of read(doc).matchAll(/\]\(([^\s)]+)(?:\s+"[^"]*")?\)/g)) {
    const href = match[1];
    if (/^(?:[a-z]+:|#|\/\/)/i.test(href)) continue;
    const target = href.split('#')[0];
    if (!target) continue;
    assert.ok(fs.existsSync(path.resolve(root, path.dirname(doc), target)), `Broken local link in ${doc}: ${target}`);
    links++;
  }
}
console.log(JSON.stringify({ status: 'PASS', publicRepositories: expected.public_repositories, npmPackages: npm.package_count, crates: crates.crate_count, newProjects: newProjects.length, frozenSnapshots: proof.files.length, sourceReceipts: proof.sources.length, localLinks: links }));
