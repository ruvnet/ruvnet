# Ecosystem metrics

Verified November 10, 2026. Public repositories only. GitHub counts: 2026-11-10T13:59:12+00:00.

| Metric | Count |
| --- | ---: |
| Public owned repositories | 233 |
| Original repositories | 206 |
| Public fork repositories | 27 |
| Stars across all owned repos | 202,506 |
| Stars across originals | 202,241 |
| Forks across all owned repos | 26,754 |
| Followers | 12,350 |
| Repository subscriptions | 1,812 |
| Published releases | 2,521 |
| Current release asset downloads | 117,144 |
| Retained observed release asset downloads | 117,147 |
| Rust crates | 498 |
| crates.io cumulative downloads | 2,196,355 |

## Repository cohorts

| Cohort | Public repositories | Stars | Forks | Subscribers | Open issues + PRs |
| --- | ---: | ---: | ---: | ---: | ---: |
| All owned | 233 | 202,506 | 26,754 | 1,812 | 2,439 |
| Nonfork | 206 | 202,241 | 26,674 | 1,809 | 2,432 |

## Activity: October 27 through November 9, UTC

| Metric | Count |
| --- | ---: |
| Issues opened | 204 |
| Issues closed | 523 |
| PRs opened | 754 |
| PRs merged | 533 |
| Releases published | 87 |
| Workflow runs | Unknown |

Workflow run counts are unknown. GitHub limits complete run enumeration to 1,000 results per query; this snapshot does not have complete workflow coverage.

## GitHub traffic

Across the complete 14-day UTC window, GitHub reported 696,719 clone events and 221,670 view events for 233 repositories. Unique cloners and visitors are retained per repository only and are not summed.

## npm downloads

The full npm download refresh hit HTTP 429. November 9 UTC is unknown for the ecosystem cohort. The inventory and crates.io totals were refreshed November 10; npm download ranges remain dated November 9 and cover through November 8.

Latest reported complete UTC date: **2026-11-08**, with **388,290 observed npm download events** across 405 of 410 packages. This is a calendar day, and missing package observations are excluded.

Confirmed daily-event sum: 9,358,390 across 405 of 410 packages for October 27 through November 9. 3 npm packages are missing download-range evidence. See [npm source evidence](../data/snapshots/2026-11-09/npm-downloads.json) for provider errors. Dates with incomplete package coverage: 2026-10-27, 2026-10-28, 2026-10-29, 2026-10-30, 2026-10-31, 2026-11-01, 2026-11-02, 2026-11-03, 2026-11-04, 2026-11-05, 2026-11-06, 2026-11-07, 2026-11-08, 2026-11-09. Missing package observations remain unknown (null); the sum includes only observed events. This is not a lifetime or rolling-24-hour count. The separate rolling 365 day total is 113,531,070, through 2026-11-08.

## Coverage and gaps

All 233 public repositories were enumerated, including 27 forks and 0 archived repositories. Repository subscriptions and release pagination are complete. Open public issues and PRs are 1,232 and 1,205. Indexed search can differ from repository metadata because sources are not an atomic snapshot. Open issues and PR counts are separate search estimates; the cohort row reports GitHub's combined open_issues_count.

GitHub traffic was available through the owner-authorized ruOS interface. Across all repositories, clone events were 696,719 and view events were 221,670 from 2026-10-27 through 2026-11-09 UTC. Per-repository unique counts are retained in the dated snapshot; they are not summed across repositories. Commits and contributors were not refreshed.

## Running totals and verification

[Running totals](../data/ecosystem-running-totals.json), [daily npm ledger](../data/ecosystem-daily-ledger.json), and [release asset ledger](../data/release-asset-ledger.json) keep providers and metrics separate. Revised daily cells replace earlier observations; overlapping windows are never added. 8 release assets are absent from the complete current inventory; their last observed counts and deletion provenance are retained.

Validation passed: 38,218 unique daily keys, idempotent replay, total reconciliation, complete repository and release pagination, and explicit missing data. [Dated evidence](../data/snapshots/2026-11-10/).

## Progress toward 100 million

Observed combined registry downloads: 116,086,923; remaining: 0. Basis: npm since October 1, 2025 plus cumulative crates.io. npm contributes 113,890,568 through 2026-11-08; crates.io contributes 2,196,355. This is an observed lower bound. Clones and release assets are excluded. [Full npm evidence](../data/snapshots/2026-11-09/npm-downloads.json).
