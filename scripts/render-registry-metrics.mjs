// Render all current registry summaries from one dated record.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const read = p => fs.readFileSync(path.join(root, p), 'utf8');
const save = (p, s) => fs.writeFileSync(path.join(root, p), s);
const data = JSON.parse(read('data/registry-stats.json'));
const metrics = JSON.parse(read('data/metrics.json'));
const npm = data.npm, crates = data.crates_io;
const format = n => new Intl.NumberFormat('en-US').format(n);
const date = value => value.slice(0, 10);
const inventoryDate = date(npm.inventory_verified_at || data.generated_at);
const downloadDate = date(npm.downloads_verified_at || data.generated_at);
const crateDate = date(crates.verified_at || data.generated_at);
const cohort = npm.download_package_count ?? npm.package_count;
const total = npm.package_count + crates.crate_count + metrics.counts.pypi_packages + metrics.counts.huggingface_models_and_spaces;
const retained = downloadDate !== inventoryDate || cohort !== npm.package_count;
const period = `${npm.period_start} through ${npm.period_end}`;
function replaceBlock(text, name, body) {
  const expression = new RegExp(`<!-- ${name}:start -->[\\s\\S]*?<!-- ${name}:end -->`);
  if (!expression.test(text)) throw new Error(`Missing ${name} markers`);
  return text.replace(expression, `<!-- ${name}:start -->\n${body}\n<!-- ${name}:end -->`);
}
const explanation = retained
  ? `The current npm inventory contains **${format(npm.package_count)} packages**. Download evidence retains its **${downloadDate}** verification date and **${format(cohort)} package cohort**. The newer download refresh was unavailable; no extrapolation is applied.`
  : `The npm inventory and download recount cover the same **${format(cohort)} package cohort**, verified **${downloadDate} UTC**.`;
let readme = read('README.md');
readme = replaceBlock(readme, 'package-public-metrics', `## Package distribution

| Measure | Verified value | Evidence date |
| --- | ---: | --- |
| Published registry and Hugging Face artifacts | at least ${format(total)} | Mixed dates below |
| Known npm packages listing \`ruvnet\` as maintainer | at least ${format(npm.package_count)} | ${inventoryDate} UTC |
| npm downloads, rolling 365 days (${period}) | ${format(npm.downloads)} | ${downloadDate}; ${format(cohort)} package cohort |
| Rust crates owned by \`ruvnet\` | ${format(crates.crate_count)} | ${crateDate} UTC |
| Cumulative Rust crate downloads (verified ${crateDate}) | ${format(crates.cumulative_downloads)} | ${crateDate} UTC |
| Ownership verified PyPI packages | ${metrics.counts.pypi_packages} | July 12, 2026; historical |
| Hugging Face models, spaces, and datasets | ${metrics.counts.huggingface_models_and_spaces} | July 12, 2026; historical |

${explanation} [Registry evidence](data/registry-stats.json) records both populations. The artifact total combines current npm and crates counts with the 30 historically verified PyPI and Hugging Face artifacts.

Package downloads include CI, reinstallations and platform packages. They do not establish unique users. The [weekly refresh](.github/workflows/refresh-registry-metrics.yml) updates these measurements from official APIs.`);
const monthly = npm.monthly_downloads;
const labels = monthly.map(row => JSON.stringify(new Date(`${row.month}-01T00:00:00Z`).toLocaleString('en-US', { month: 'short', year: 'numeric', timeZone: 'UTC' }))).join(', ');
const values = monthly.map(row => Number((row.downloads / 1e6).toFixed(3)));
readme = replaceBlock(readme, 'registry-download-chart', `## npm download growth

Monthly downloads across the ${format(cohort)} package cohort verified ${downloadDate}. This dated series covers ${npm.monthly_period_start} through ${npm.monthly_period_end}; it is not extended beyond the measured window.

\`\`\`mermaid
xychart-beta
    title "rUv npm ecosystem: monthly downloads"
    x-axis [${labels}]
    y-axis "Downloads (millions)" 0 --> ${Math.max(1, Math.ceil(Math.max(...values)))}
    line [${values.join(', ')}]
\`\`\`

**Source:** official npm daily range API. Figures are millions of download events, including scoped, unscoped, and platform packages. Download events are not unique users.`);
save('README.md', readme);
let doc = read('docs/ruvnet-packages.md');
doc = doc.replace(/Current inventory observed [^.]+\./, `Current inventory observed ${inventoryDate} UTC.`);
doc = doc.replace(/\*\*At least [\s\S]*?separate inventions\./, `**At least ${format(total)} published artifacts** across the known distribution surface: **${format(crates.crate_count)} Rust crates**, **${format(npm.package_count)} known npm packages**, plus **8 PyPI packages** and **22 Hugging Face artifacts** retained from their July ownership checks. Packages, native target binaries, adapters, and examples are grouped under products; they are not ${format(total)} separate inventions.`);
doc = replaceBlock(doc, 'registry-summary', `## Registry totals

| Registry | Packages | Downloads | Verified |
| --- | ---: | --- | --- |
| [crates.io](https://crates.io/users/ruvnet) | ${format(crates.crate_count)} | ${format(crates.cumulative_downloads)} cumulative | ${crateDate} UTC |
| [npm](https://www.npmjs.com/~ruvnet) | at least ${format(npm.package_count)} | ${format(npm.downloads)} during ${period}; ${format(cohort)} package cohort | Inventory ${inventoryDate}; downloads ${downloadDate} |
| [PyPI](https://pypi.org/user/ruvnet/) | 8 | Not aggregated | Historical ownership check, July 12, 2026 |
| [Hugging Face](https://huggingface.co/ruvnet) | 22 | Not recounted | Historical inventory, July 12, 2026 |

${explanation} [Registry data](../data/registry-stats.json) retains exact windows and dates.`);
save('docs/ruvnet-packages.md', doc);
metrics.counts.rust_crates = crates.crate_count;
metrics.counts.npm_packages = npm.package_count;
metrics.counts.rust_crate_downloads_cumulative = crates.cumulative_downloads;
metrics.counts.published_registry_and_huggingface_artifacts_minimum = total;
metrics.verification_dates = { ...metrics.verification_dates, npm_inventory: npm.inventory_verified_at || data.generated_at, npm_downloads: npm.downloads_verified_at || data.generated_at, crates_io: crates.verified_at || data.generated_at };
metrics.current_windows = { npm_downloads_rolling_365_days: npm.downloads, npm_period_start: npm.period_start, npm_period_end: npm.period_end, npm_download_package_count: cohort };
metrics.notes = metrics.notes.filter(note => !note.startsWith('The npm download cohort is'));
metrics.notes.push(`The npm download cohort is ${cohort} packages; the current inventory contains ${npm.package_count}.`);
save('data/metrics.json', JSON.stringify(metrics, null, 2) + '\n');
console.log(`Rendered ${npm.package_count} npm packages, ${crates.crate_count} crates; downloads dated ${downloadDate}.`);
