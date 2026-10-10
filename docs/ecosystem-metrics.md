# Ecosystem metrics

Verified October 10, 2026. Public repositories only. GitHub counts: 2026-10-10T12:37:17.982Z.

| Metric | Count |
| --- | ---: |
| Public owned repositories | 222 |
| Original repositories | 196 |
| Public fork repositories | 26 |
| Stars across all owned repos | 188,130 |
| Stars across originals | 187,869 |
| Forks across all owned repos | 25,201 |
| Followers | 11,726 |
| Repository subscriptions | 1,759 |
| Published releases | 2,339 |
| Current release asset downloads | 108,131 |
| Retained observed release asset downloads | 108,131 |
| Rust crates | 480 |
| crates.io cumulative downloads | 1,815,085 |

## Activity: September 26 through October 9, UTC

| Metric | Count |
| --- | ---: |
| Issues opened | 219 |
| Issues closed | 166 |
| PRs opened | 715 |
| PRs merged | 491 |
| Releases published | 50 |
| Workflow runs enumerated, partial | 15,991 |
| Successful workflow runs | 12,663 |
| Failed workflow runs | 1,323 |

Workflow enumeration is complete for 221 of 222 repositories. Ruflo remains partial on five high volume UTC days because GitHub limits search pagination to 1,000 results per query. Outcomes are current conclusions of unique run IDs, not all retry attempts or a product reliability measure.

## npm downloads

Observed 9,262,643 downloads across 398 of 398 packages for September 26 through October 9. The official range responses are complete; recent zero days can reflect provider reporting delay. This window is not a lifetime count. The separate rolling 365 day total is 94,500,218, through 2026-10-08.

## Coverage and gaps

All 222 public repositories were enumerated across four connector pages, including 26 forks and zero archived repositories. Repository subscriptions and releases have complete pagination. Open public issues and PRs are 1,484 and 1,104; indexed search can differ from repository metadata because the sources are not an atomic snapshot.

Clones and page views are unavailable because the connected GitHub interface lacks Administration read permission and does not expose repository traffic endpoints. Historical September traffic remains preserved and is never substituted for current data. Commits and contributors were not refreshed.

## Running totals and verification

[Running totals](../data/ecosystem-running-totals.json), [daily npm ledger](../data/ecosystem-daily-ledger.json), and [release asset ledger](../data/release-asset-ledger.json) keep providers and metrics separate. Daily npm keys combine provider, package, metric and UTC date. Revised cells replace prior observations; overlapping windows are never added. Missing assets retain their last observed counts and are flagged.

Validation passed: 5,572 unique daily keys, idempotent replay, daily and milestone reconciliation, complete repository and release pagination, and explicit missing data. [Dated evidence](../data/snapshots/2026-10-10/).

## Progress toward 100 million

Observed combined registry downloads: 96,349,820; remaining: 3,650,180. Basis: npm since October 1, 2025 plus cumulative crates.io. The npm component is 94,534,735, reconciled from all 398 official per package range responses through the latest positive cohort day, 2026-10-08; the Rust component is 1,815,085. This is an observed lower bound: 7 internal all zero cohort days may be provider reporting gaps, and trailing all zero days do not advance the npm window. Clones and release assets are excluded. [Full npm evidence](../data/snapshots/2026-10-10/npm-downloads.json).
