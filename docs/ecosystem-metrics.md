# Ecosystem metrics

Verified October 11, 2026. Public repositories only. GitHub counts: 2026-10-11T12:40:24.116Z.

| Metric | Count |
| --- | ---: |
| Public owned repositories | 222 |
| Original repositories | 196 |
| Public fork repositories | 26 |
| Stars across all owned repos | 188,358 |
| Stars across originals | 188,096 |
| Forks across all owned repos | 25,224 |
| Followers | 11,729 |
| Repository subscriptions | 1,759 |
| Published releases | 2,342 |
| Current release asset downloads | 108,323 |
| Retained observed release asset downloads | 108,323 |
| Rust crates | 480 |
| crates.io cumulative downloads | 1,823,072 |

## Activity: September 27 through October 10, UTC

| Metric | Count |
| --- | ---: |
| Issues opened | 227 |
| Issues closed | 145 |
| PRs opened | 788 |
| PRs merged | 432 |
| Releases published | 45 |
| Workflow runs enumerated, partial | 16,232 |
| Successful workflow runs | 12,804 |
| Failed workflow runs | 1,419 |

Workflow enumeration is complete for 221 of 222 repositories. Ruflo remains partial because GitHub limits pagination to 1,000 results per query. Outcomes are current conclusions of unique run IDs, not all retry attempts or a reliability measure.

## npm downloads

Observed 9,800,319 downloads across 398 of 398 packages for September 27 through October 10. Official range responses are complete; recent zero days can reflect provider delay. This window is not a lifetime count. The separate rolling 365 day total is 95,712,793, through 2026-10-10.

## Coverage and gaps

All 222 public repositories were enumerated, including 26 forks and zero archived repositories. Repository subscriptions and release pagination are complete. Open public issues and PRs are 1,482 and 1,205. Indexed search can differ from repository metadata because sources are not an atomic snapshot.

Clones and page views are unavailable because the connected GitHub interface lacks Administration read permission and does not expose repository traffic endpoints. Historical traffic remains preserved and is never substituted for current data. Commits and contributors were not refreshed.

## Running totals and verification

[Running totals](../data/ecosystem-running-totals.json), [daily npm ledger](../data/ecosystem-daily-ledger.json), and [release asset ledger](../data/release-asset-ledger.json) keep providers and metrics separate. Revised daily cells replace earlier observations; overlapping windows are never added. Missing assets retain their last observed counts and are flagged.

Validation passed: 6,368 unique daily keys, idempotent replay, total reconciliation, complete repository and release pagination, and explicit missing data. [Dated evidence](../data/snapshots/2026-10-11/).

## Progress toward 100 million

Observed combined registry downloads: 97,577,018; remaining: 2,422,982. Basis: npm since October 1, 2025 plus cumulative crates.io. npm contributes 95,753,946 through 2026-10-10; crates.io contributes 1,823,072. This is an observed lower bound. Clones and release assets are excluded. [Full npm evidence](../data/snapshots/2026-10-11/npm-downloads.json).
