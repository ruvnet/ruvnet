# Ecosystem metrics

Verified October 13, 2026. Public repositories only. GitHub counts: 2026-10-13T12:14:00.353362Z.

| Metric | Count |
| --- | ---: |
| Public owned repositories | 225 |
| Original repositories | 198 |
| Public fork repositories | 27 |
| Stars across all owned repos | 189,046 |
| Stars across originals | 188,784 |
| Forks across all owned repos | 25,287 |
| Followers | 11,766 |
| Repository subscriptions | 1,761 |
| Published releases | 2,370 |
| Current release asset downloads | 108,782 |
| Retained observed release asset downloads | 108,782 |
| Rust crates | 481 |
| crates.io cumulative downloads | 1,861,096 |

## Activity: September 29 through October 12, UTC

| Metric | Count |
| --- | ---: |
| Issues opened | 252 |
| Issues closed | 172 |
| PRs opened | 873 |
| PRs merged | 511 |
| Releases published | 66 |
| Workflow runs enumerated, partial | 17,665 |
| Successful workflow runs | 13,936 |
| Failed workflow runs | 1,794 |

Workflow enumeration is complete for 224 of 225 repositories. Ruflo remains partial because GitHub limits pagination to 1,000 results per query. Outcomes are current conclusions of unique run IDs, not all retry attempts or a reliability measure.

## npm downloads

Observed 8,365,172 downloads across 399 of 400 packages for September 29 through October 12. Range responses are complete for the collected cohort. 1 newly indexed package is explicitly missing because its range endpoint returned HTTP 404 after bounded retries. Recent zero days can reflect provider delay. This window is not a lifetime count. The separate rolling 365 day total is 96,332,647, through 2026-10-11.

## Coverage and gaps

All 225 public repositories were enumerated, including 27 forks and 0 archived repositories. Repository subscriptions and release pagination are complete. Open public issues and PRs are 1,525 and 1,163. Indexed search can differ from repository metadata because sources are not an atomic snapshot.

Clones and page views are unavailable: the connected GitHub interface rejects `/traffic/clones` and `/traffic/views` as non-public endpoints, and the managed app lacks the required Administration-read permission. Historical traffic remains preserved and is never substituted for current data. Commits and contributors were not refreshed.

## Running totals and verification

[Running totals](../data/ecosystem-running-totals.json), [daily npm ledger](../data/ecosystem-daily-ledger.json), and [release asset ledger](../data/release-asset-ledger.json) keep providers and metrics separate. Revised daily cells replace earlier observations; overlapping windows are never added. Missing assets retain their last observed counts and are flagged.

Validation passed: 7,179 unique daily keys, idempotent replay, total reconciliation, complete repository and release pagination, and explicit missing data. [Dated evidence](../data/snapshots/2026-10-13/).

## Progress toward 100 million

Observed combined registry downloads: 98,239,145; remaining: 1,760,855. Basis: npm since October 1, 2025 plus cumulative crates.io. npm contributes 96,378,049 through 2026-10-11; crates.io contributes 1,861,096. This is an observed lower bound. Clones and release assets are excluded. [Full npm evidence](../data/snapshots/2026-10-13/npm-downloads.json).
