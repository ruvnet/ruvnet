# Ecosystem metrics

Verified October 26, 2026. Public repositories only. GitHub counts: 2026-10-26T12:45:14+00:00.

| Metric | Count |
| --- | ---: |
| Public owned repositories | 229 |
| Original repositories | 202 |
| Public fork repositories | 27 |
| Stars across all owned repos | 196,126 |
| Stars across originals | 195,863 |
| Forks across all owned repos | 25,992 |
| Followers | 12,081 |
| Repository subscriptions | 1,785 |
| Published releases | 2,414 |
| Current release asset downloads | 111,617 |
| Retained observed release asset downloads | 111,620 |
| Rust crates | 481 |
| crates.io cumulative downloads | 1,972,634 |

## Repository cohorts

| Cohort | Public repositories | Stars | Forks | Subscribers | Open issues + PRs |
| --- | ---: | ---: | ---: | ---: | ---: |
| All owned | 229 | 196,126 | 25,992 | 1,785 | 2,830 |
| Nonfork | 202 | 195,863 | 25,913 | 1,782 | 2,820 |

## Activity: October 12 through October 25, UTC

| Metric | Count |
| --- | ---: |
| Issues opened | 215 |
| Issues closed | 159 |
| PRs opened | 560 |
| PRs merged | 414 |
| Releases published | 64 |
| Workflow runs | Unknown |

Workflow run counts are unknown. GitHub limits complete run enumeration to 1,000 results per query; this snapshot does not have complete workflow coverage.

## GitHub traffic

Across the complete 14-day UTC window, GitHub reported 687,581 clone events and 157,075 view events for 229 repositories. Unique cloners and visitors are retained per repository only and are not summed.

## npm downloads

Confirmed daily-event sum: 2,733,103 across 401 of 401 packages for October 12 through October 25. All inventory packages have download-range evidence. All-package-zero days 2026-10-13, 2026-10-14, 2026-10-15, 2026-10-19, 2026-10-20, 2026-10-21, 2026-10-23, 2026-10-24, 2026-10-25 are unknown (null), not zero, and excluded from the sum. This is not a lifetime or rolling-24-hour count. The separate rolling 365 day total is 98,900,691, through 2026-10-22.

## Coverage and gaps

All 229 public repositories were enumerated, including 27 forks and 0 archived repositories. Repository subscriptions and release pagination are complete. Open public issues and PRs are 1,550 and 1,279. Indexed search can differ from repository metadata because sources are not an atomic snapshot. Open issues and PR counts are separate search estimates; the cohort row reports GitHub's combined open_issues_count.

GitHub traffic was available through the owner-authorized ruOS interface. Across all repositories, clone events were 687,581 and view events were 157,075 from 2026-10-12 through 2026-10-25 UTC. Per-repository unique counts are retained in the dated snapshot; they are not summed across repositories. Commits and contributors were not refreshed.

## Running totals and verification

[Running totals](../data/ecosystem-running-totals.json), [daily npm ledger](../data/ecosystem-daily-ledger.json), and [release asset ledger](../data/release-asset-ledger.json) keep providers and metrics separate. Revised daily cells replace earlier observations; overlapping windows are never added. 8 release assets are absent from the complete current inventory; their last observed counts and deletion provenance are retained.

Validation passed: 25,022 unique daily keys, idempotent replay, total reconciliation, complete repository and release pagination, and explicit missing data. [Dated evidence](../data/snapshots/2026-10-26/).

## Progress toward 100 million

Observed combined registry downloads: 101,083,786; remaining: 0. Basis: npm since October 1, 2025 plus cumulative crates.io. npm contributes 99,111,152 through 2026-10-22; crates.io contributes 1,972,634. This is an observed lower bound. Clones and release assets are excluded. [Full npm evidence](../data/snapshots/2026-10-26/npm-downloads.json).
