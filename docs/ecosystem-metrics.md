# Ecosystem metrics

Verified October 30, 2026. Public repositories only. GitHub counts: 2026-10-30T12:03:25+00:00.

| Metric | Count |
| --- | ---: |
| Public owned repositories | 230 |
| Original repositories | 203 |
| Public fork repositories | 27 |
| Stars across all owned repos | 199,016 |
| Stars across originals | 198,753 |
| Forks across all owned repos | 26,422 |
| Followers | 12,189 |
| Repository subscriptions | 1,798 |
| Published releases | 2,434 |
| Current release asset downloads | 113,059 |
| Retained observed release asset downloads | 113,062 |
| Rust crates | 489 |
| crates.io cumulative downloads | 2,011,358 |

## Repository cohorts

| Cohort | Public repositories | Stars | Forks | Subscribers | Open issues + PRs |
| --- | ---: | ---: | ---: | ---: | ---: |
| All owned | 230 | 199,016 | 26,422 | 1,798 | 2,907 |
| Nonfork | 203 | 198,753 | 26,330 | 1,795 | 2,897 |

## Activity: October 16 through October 29, UTC

| Metric | Count |
| --- | ---: |
| Issues opened | 160 |
| Issues closed | 126 |
| PRs opened | 534 |
| PRs merged | 391 |
| Releases published | 61 |
| Workflow runs | Unknown |

Workflow run counts are unknown. GitHub limits complete run enumeration to 1,000 results per query; this snapshot does not have complete workflow coverage.

## GitHub traffic

Across the complete 14-day UTC window, GitHub reported 649,434 clone events and 207,570 view events for 230 repositories. Unique cloners and visitors are retained per repository only and are not summed.

## npm downloads

Confirmed daily-event sum: 5,839,661 across 401 of 401 packages for October 16 through October 29. All inventory packages have download-range evidence. All-package-zero days 2026-10-19, 2026-10-20, 2026-10-21, 2026-10-29 are unknown (null), not zero, and excluded from the sum. This is not a lifetime or rolling-24-hour count. The separate rolling 365 day total is 103,473,800, through 2026-10-28.

## Coverage and gaps

All 230 public repositories were enumerated, including 27 forks and 0 archived repositories. Repository subscriptions and release pagination are complete. Open public issues and PRs are 1,576 and 1,329. Indexed search can differ from repository metadata because sources are not an atomic snapshot. Open issues and PR counts are separate search estimates; the cohort row reports GitHub's combined open_issues_count.

GitHub traffic was available through the owner-authorized ruOS interface. Across all repositories, clone events were 649,434 and view events were 207,570 from 2026-10-16 through 2026-10-29 UTC. Per-repository unique counts are retained in the dated snapshot; they are not summed across repositories. Commits and contributors were not refreshed.

## Running totals and verification

[Running totals](../data/ecosystem-running-totals.json), [daily npm ledger](../data/ecosystem-daily-ledger.json), and [release asset ledger](../data/release-asset-ledger.json) keep providers and metrics separate. Revised daily cells replace earlier observations; overlapping windows are never added. 8 release assets are absent from the complete current inventory; their last observed counts and deletion provenance are retained.

Validation passed: 28,492 unique daily keys, idempotent replay, total reconciliation, complete repository and release pagination, and explicit missing data. [Dated evidence](../data/snapshots/2026-10-30/).

## Progress toward 100 million

Observed combined registry downloads: 105,769,464; remaining: 0. Basis: npm since October 1, 2025 plus cumulative crates.io. npm contributes 103,758,106 through 2026-10-28; crates.io contributes 2,011,358. This is an observed lower bound. Clones and release assets are excluded. [Full npm evidence](../data/snapshots/2026-10-30/npm-downloads.json).
