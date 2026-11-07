# Ecosystem metrics

Verified November 7, 2026. Public repositories only. GitHub counts: 2026-11-07T13:06:48+00:00.

| Metric | Count |
| --- | ---: |
| Public owned repositories | 232 |
| Original repositories | 205 |
| Public fork repositories | 27 |
| Stars across all owned repos | 201,156 |
| Stars across originals | 200,891 |
| Forks across all owned repos | 26,562 |
| Followers | 12,297 |
| Repository subscriptions | 1,807 |
| Published releases | 2,466 |
| Current release asset downloads | 115,686 |
| Retained observed release asset downloads | 115,689 |
| Rust crates | 492 |
| crates.io cumulative downloads | 2,128,681 |

## Repository cohorts

| Cohort | Public repositories | Stars | Forks | Subscribers | Open issues + PRs |
| --- | ---: | ---: | ---: | ---: | ---: |
| All owned | 232 | 201,156 | 26,562 | 1,807 | 2,628 |
| Nonfork | 205 | 200,891 | 26,482 | 1,804 | 2,621 |

## Activity: October 24 through November 6, UTC

| Metric | Count |
| --- | ---: |
| Issues opened | 227 |
| Issues closed | 511 |
| PRs opened | 682 |
| PRs merged | 487 |
| Releases published | 57 |
| Workflow runs | Unknown |

Workflow run counts are unknown. GitHub limits complete run enumeration to 1,000 results per query; this snapshot does not have complete workflow coverage.

## GitHub traffic

Across the complete 14-day UTC window, GitHub reported 636,476 clone events and 245,294 view events for 232 repositories. Unique cloners and visitors are retained per repository only and are not summed.

## npm downloads

Confirmed daily-event sum: 10,241,357 across 405 of 405 packages for October 24 through November 6. All inventory packages have download-range evidence. Dates with incomplete package coverage: none. Missing package observations remain unknown (null); the sum includes only observed events. This is not a lifetime or rolling-24-hour count. The separate rolling 365 day total is 112,631,504, through 2026-11-06.

## Coverage and gaps

All 232 public repositories were enumerated, including 27 forks and 0 archived repositories. Repository subscriptions and release pagination are complete. Open public issues and PRs are 1,260 and 1,366. Indexed search can differ from repository metadata because sources are not an atomic snapshot. Open issues and PR counts are separate search estimates; the cohort row reports GitHub's combined open_issues_count.

GitHub traffic was available through the owner-authorized ruOS interface. Across all repositories, clone events were 636,476 and view events were 245,294 from 2026-10-24 through 2026-11-06 UTC. Per-repository unique counts are retained in the dated snapshot; they are not summed across repositories. Commits and contributors were not refreshed.

## Running totals and verification

[Running totals](../data/ecosystem-running-totals.json), [daily npm ledger](../data/ecosystem-daily-ledger.json), and [release asset ledger](../data/release-asset-ledger.json) keep providers and metrics separate. Revised daily cells replace earlier observations; overlapping windows are never added. 8 release assets are absent from the complete current inventory; their last observed counts and deletion provenance are retained.

Validation passed: 35,506 unique daily keys, idempotent replay, total reconciliation, complete repository and release pagination, and explicit missing data. [Dated evidence](../data/snapshots/2026-11-07/).

## Progress toward 100 million

Observed combined registry downloads: 115,098,753; remaining: 0. Basis: npm since October 1, 2025 plus cumulative crates.io. npm contributes 112,970,072 through 2026-11-06; crates.io contributes 2,128,681. This is an observed lower bound. Clones and release assets are excluded. [Full npm evidence](../data/snapshots/2026-11-07/npm-downloads.json).
