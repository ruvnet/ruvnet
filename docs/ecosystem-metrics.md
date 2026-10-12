# Ecosystem metrics

Verified October 12, 2026. Public repositories only. GitHub counts: 2026-10-12T12:58:30.859845Z.

| Metric | Count |
| --- | ---: |
| Public owned repositories | 224 |
| Original repositories | 197 |
| Public fork repositories | 27 |
| Stars across all owned repos | 188,709 |
| Stars across originals | 188,447 |
| Forks across all owned repos | 25,249 |
| Followers | 11,736 |
| Repository subscriptions | 1,762 |
| Published releases | 2,354 |
| Current release asset downloads | 108,523 |
| Retained observed release asset downloads | 108,523 |
| Rust crates | 480 |
| crates.io cumulative downloads | 1,848,105 |

## Activity: September 28 through October 11, UTC

| Metric | Count |
| --- | ---: |
| Issues opened | 236 |
| Issues closed | 151 |
| PRs opened | 842 |
| PRs merged | 468 |
| Releases published | 55 |
| Workflow runs enumerated, partial | 16,996 |
| Successful workflow runs | 13,165 |
| Failed workflow runs | 1,488 |

Workflow enumeration is complete for 223 of 224 repositories. Ruflo remains partial because GitHub limits pagination to 1,000 results per query. Outcomes are current conclusions of unique run IDs, not all retry attempts or a reliability measure.

## npm downloads

Observed 9,695,288 downloads across 399 of 399 packages for September 28 through October 11. Official range responses are complete; recent zero days can reflect provider delay. This window is not a lifetime count. The separate rolling 365 day total is 96,332,647, through 2026-10-11.

## Coverage and gaps

All 224 public repositories were enumerated, including 27 forks and 0 archived repositories. Repository subscriptions and release pagination are complete. Open public issues and PRs are 1,501 and 1,210. Indexed search can differ from repository metadata because sources are not an atomic snapshot.

Clones and page views are unavailable because the connected GitHub interface lacks Administration read permission and does not expose repository traffic endpoints. Historical traffic remains preserved and is never substituted for current data. Commits and contributors were not refreshed.

## Running totals and verification

[Running totals](../data/ecosystem-running-totals.json), [daily npm ledger](../data/ecosystem-daily-ledger.json), and [release asset ledger](../data/release-asset-ledger.json) keep providers and metrics separate. Revised daily cells replace earlier observations; overlapping windows are never added. Missing assets retain their last observed counts and are flagged.

Validation passed: 6,780 unique daily keys, idempotent replay, total reconciliation, complete repository and release pagination, and explicit missing data. [Dated evidence](../data/snapshots/2026-10-12/).

## Progress toward 100 million

Observed combined registry downloads: 98,226,154; remaining: 1,773,846. Basis: npm since October 1, 2025 plus cumulative crates.io. npm contributes 96,378,049 through 2026-10-11; crates.io contributes 1,848,105. This is an observed lower bound. Clones and release assets are excluded. [Full npm evidence](../data/snapshots/2026-10-12/npm-downloads.json).
