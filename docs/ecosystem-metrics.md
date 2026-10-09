# Ecosystem metrics

Verified October 9, 2026. Public repositories only. GitHub counts: 2026-10-09T12:14:43.561449+00:00.

| Metric | Count |
| --- | ---: |
| Public owned repositories | 222 |
| Original repositories | 196 |
| Stars across all owned repos | 187,952 |
| Stars across originals | 187,692 |
| Forks across all owned repos | 25,162 |
| Followers | 11,721 |
| Repository subscriptions | 1,759 |
| Published releases | 2,333 |
| Current release asset downloads | 108,022 |
| Rust crates | 480 |
| crates.io cumulative downloads | 1,803,303 |

## Activity: September 25 through October 8, UTC

| Metric | Count |
| --- | ---: |
| Issues opened | 206 |
| Issues closed | 156 |
| PRs opened | 685 |
| PRs merged | 461 |
| Releases published | 47 |
| Workflow runs enumerated (partial) | 6,230 |
| Successful workflow runs | 4,284 |
| Failed workflow runs | 706 |

Workflow coverage is incomplete for Ruflo; the JSON report records expected and collected counts. Workflow outcomes below are current conclusions of unique runs, not all retry attempts or measures of product reliability. Cancelled, skipped and unfinished runs are recorded separately in the JSON report.

## npm downloads

Observed 9,854,546 downloads across 398 of 398 packages for September 25 through October 8. Status: complete API responses, provider latency may remain. Recent zero days can reflect provider reporting delay. This window is not a lifetime count. Previous complete rolling-year figures retain their original verification dates in data/registry-stats.json.

## Coverage and gaps

All 222 public repositories were enumerated. Repository subscriptions and releases have complete pagination. Workflow queries were partitioned by UTC date where necessary; 221 of 222 repository queries are complete. Ruflo remains partial because of API result limits. Open public issues and PRs are 1,467 and 1,047; indexed search sum can differ from repository metadata (2,516 combined) because the sources are not an atomic snapshot.

Clones and page views remain unavailable: the connected GitHub interface lacks Administration read permission and a traffic endpoint. Historical traffic is retained separately and never reported as current. Commits and contributors were not refreshed.

## Running totals and verification

[Running totals](../data/ecosystem-running-totals.json), [daily npm ledger](../data/ecosystem-daily-ledger.json), and [release asset ledger](../data/release-asset-ledger.json) keep sources separate. Daily npm keys combine provider, package, metric and UTC date. Revised cells replace prior observations; overlapping windows are never added. Missing release assets retain their last observed values and are flagged.

Validation passed: 5,572 unique daily keys, unchanged totals after replay, daily sum reconciliation, all repository and release pages accounted for; Actions coverage gaps explicitly recorded. [Dated evidence](../data/snapshots/2026-10-09/).

## Progress toward 100 million

Observed combined registry downloads: 95,790,408; remaining: 4,209,592. Basis: npm since October 1, 2025 plus cumulative crates.io. New npm observations after October 5 are added once to the preserved baseline. This is an observed lower bound, with provider reporting latency and package coverage disclosed above. Clones and release assets are excluded from this milestone.
