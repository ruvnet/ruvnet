# Ecosystem metrics

Verified October 25, 2026. Public repositories only. GitHub counts: 2026-10-25T12:51:17+00:00.

| Metric | Count |
| --- | ---: |
| Public owned repositories | 229 |
| Original repositories | 202 |
| Public fork repositories | 27 |
| Stars across all owned repos | 195,696 |
| Stars across originals | 195,432 |
| Forks across all owned repos | 25,947 |
| Followers | 12,072 |
| Repository subscriptions | 1,781 |
| Published releases | 2,413 |
| Current release asset downloads | 111,299 |
| Retained observed release asset downloads | 111,302 |
| Rust crates | 481 |
| crates.io cumulative downloads | 1,970,876 |

## Repository cohorts

| Cohort | Public repositories | Stars | Forks | Subscribers | Open issues + PRs |
| --- | ---: | ---: | ---: | ---: | ---: |
| All owned | 229 | 195,696 | 25,947 | 1,781 | 2,815 |
| Nonfork | 202 | 195,432 | 25,868 | 1,778 | 2,805 |

## Activity: October 11 through October 24, UTC

| Metric | Count |
| --- | ---: |
| Issues opened | 223 |
| Issues closed | 169 |
| PRs opened | 670 |
| PRs merged | 477 |
| Releases published | 75 |
| Workflow runs | Unknown |

Workflow run counts are unknown. GitHub limits complete run enumeration to 1,000 results per query; this snapshot does not have complete workflow coverage.

## GitHub traffic

Across the complete 14-day UTC window, GitHub reported 717,310 clone events and 149,757 view events for 229 repositories. Unique cloners and visitors are retained per repository only and are not summed.

## npm downloads

Confirmed daily-event sum: 3,357,206 across 401 of 401 packages for October 11 through October 24. All inventory packages have download-range evidence. All-package-zero days 2026-10-13, 2026-10-14, 2026-10-15, 2026-10-19, 2026-10-20, 2026-10-21, 2026-10-23, 2026-10-24 are unknown (null), not zero, and excluded from the sum. This is not a lifetime or rolling-24-hour count. The separate rolling 365 day total is 98,900,691, through 2026-10-22.

## Coverage and gaps

All 229 public repositories were enumerated, including 27 forks and 0 archived repositories. Repository subscriptions and release pagination are complete. Open public issues and PRs are 1,543 and 1,270. Indexed search can differ from repository metadata because sources are not an atomic snapshot. Open issues and PR counts are separate search estimates; the cohort row reports GitHub's combined open_issues_count.

GitHub traffic was available through the owner-authorized ruOS interface. Across all repositories, clone events were 717,310 and view events were 149,757 from 2026-10-11 through 2026-10-24 UTC. Per-repository unique counts are retained in the dated snapshot; they are not summed across repositories. Commits and contributors were not refreshed.

## Running totals and verification

[Running totals](../data/ecosystem-running-totals.json), [daily npm ledger](../data/ecosystem-daily-ledger.json), and [release asset ledger](../data/release-asset-ledger.json) keep providers and metrics separate. Revised daily cells replace earlier observations; overlapping windows are never added. 8 release assets are absent from the complete current inventory; their last observed counts and deletion provenance are retained.

Validation passed: 24,163 unique daily keys, idempotent replay, total reconciliation, complete repository and release pagination, and explicit missing data. [Dated evidence](../data/snapshots/2026-10-25/).

## Progress toward 100 million

Observed combined registry downloads: 101,082,028; remaining: 0. Basis: npm since October 1, 2025 plus cumulative crates.io. npm contributes 99,111,152 through 2026-10-22; crates.io contributes 1,970,876. This is an observed lower bound. Clones and release assets are excluded. [Full npm evidence](../data/snapshots/2026-10-25/npm-downloads.json).
