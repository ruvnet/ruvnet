# Ecosystem metrics

Verified October 31, 2026. Public repositories only. GitHub counts: 2026-10-31T12:29:54+00:00.

| Metric | Count |
| --- | ---: |
| Public owned repositories | 230 |
| Original repositories | 203 |
| Public fork repositories | 27 |
| Stars across all owned repos | 199,316 |
| Stars across originals | 199,052 |
| Forks across all owned repos | 26,455 |
| Followers | 12,208 |
| Repository subscriptions | 1,801 |
| Published releases | 2,436 |
| Current release asset downloads | 113,327 |
| Retained observed release asset downloads | 113,330 |
| Rust crates | 489 |
| crates.io cumulative downloads | 2,018,240 |

## Repository cohorts

| Cohort | Public repositories | Stars | Forks | Subscribers | Open issues + PRs |
| --- | ---: | ---: | ---: | ---: | ---: |
| All owned | 230 | 199,316 | 26,455 | 1,801 | 2,937 |
| Nonfork | 203 | 199,052 | 26,362 | 1,798 | 2,927 |

## Activity: October 17 through October 30, UTC

| Metric | Count |
| --- | ---: |
| Issues opened | 161 |
| Issues closed | 125 |
| PRs opened | 546 |
| PRs merged | 400 |
| Releases published | 59 |
| Workflow runs | Unknown |

Workflow run counts are unknown. GitHub limits complete run enumeration to 1,000 results per query; this snapshot does not have complete workflow coverage.

## GitHub traffic

Across the complete 14-day UTC window, GitHub reported 651,193 clone events and 213,377 view events for 230 repositories. Unique cloners and visitors are retained per repository only and are not summed.

## npm downloads

Confirmed daily-event sum: 6,100,146 across 401 of 401 packages for October 17 through October 30. All inventory packages have download-range evidence. All-package-zero days 2026-10-19, 2026-10-20, 2026-10-21, 2026-10-30 are unknown (null), not zero, and excluded from the sum. This is not a lifetime or rolling-24-hour count. The separate rolling 365 day total is 104,141,514, through 2026-10-29.

## Coverage and gaps

All 230 public repositories were enumerated, including 27 forks and 0 archived repositories. Repository subscriptions and release pagination are complete. Open public issues and PRs are 1,585 and 1,350. Indexed search can differ from repository metadata because sources are not an atomic snapshot. Open issues and PR counts are separate search estimates; the cohort row reports GitHub's combined open_issues_count.

GitHub traffic was available through the owner-authorized ruOS interface. Across all repositories, clone events were 651,193 and view events were 213,377 from 2026-10-17 through 2026-10-30 UTC. Per-repository unique counts are retained in the dated snapshot; they are not summed across repositories. Commits and contributors were not refreshed.

## Running totals and verification

[Running totals](../data/ecosystem-running-totals.json), [daily npm ledger](../data/ecosystem-daily-ledger.json), and [release asset ledger](../data/release-asset-ledger.json) keep providers and metrics separate. Revised daily cells replace earlier observations; overlapping windows are never added. 8 release assets are absent from the complete current inventory; their last observed counts and deletion provenance are retained.

Validation passed: 29,353 unique daily keys, idempotent replay, total reconciliation, complete repository and release pagination, and explicit missing data. [Dated evidence](../data/snapshots/2026-10-31/).

## Progress toward 100 million

Observed combined registry downloads: 106,448,551; remaining: 0. Basis: npm since October 1, 2025 plus cumulative crates.io. npm contributes 104,430,311 through 2026-10-29; crates.io contributes 2,018,240. This is an observed lower bound. Clones and release assets are excluded. [Full npm evidence](../data/snapshots/2026-10-31/npm-downloads.json).
