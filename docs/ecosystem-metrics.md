# Ecosystem metrics

Verified November 1, 2026. Public repositories only. GitHub counts: 2026-11-01T13:57:51+00:00.

| Metric | Count |
| --- | ---: |
| Public owned repositories | 230 |
| Original repositories | 203 |
| Public fork repositories | 27 |
| Stars across all owned repos | 199,558 |
| Stars across originals | 199,294 |
| Forks across all owned repos | 26,496 |
| Followers | 12,221 |
| Repository subscriptions | 1,806 |
| Published releases | 2,440 |
| Current release asset downloads | 113,623 |
| Retained observed release asset downloads | 113,626 |
| Rust crates | 489 |
| crates.io cumulative downloads | 2,024,997 |

## Repository cohorts

| Cohort | Public repositories | Stars | Forks | Subscribers | Open issues + PRs |
| --- | ---: | ---: | ---: | ---: | ---: |
| All owned | 230 | 199,558 | 26,496 | 1,806 | 2,951 |
| Nonfork | 203 | 199,294 | 26,403 | 1,803 | 2,941 |

## Activity: October 18 through October 31, UTC

| Metric | Count |
| --- | ---: |
| Issues opened | 164 |
| Issues closed | 116 |
| PRs opened | 556 |
| PRs merged | 391 |
| Releases published | 61 |
| Workflow runs | Unknown |

Workflow run counts are unknown. GitHub limits complete run enumeration to 1,000 results per query; this snapshot does not have complete workflow coverage.

## GitHub traffic

Across the complete 14-day UTC window, GitHub reported 651,418 clone events and 215,680 view events for 230 repositories. Unique cloners and visitors are retained per repository only and are not summed.

## npm downloads

Confirmed daily-event sum: 5,684,609 across 401 of 401 packages for October 18 through October 31. All inventory packages have download-range evidence. All-package-zero days 2026-10-19, 2026-10-20, 2026-10-21, 2026-10-30, 2026-10-31 are unknown (null), not zero, and excluded from the sum. This is not a lifetime or rolling-24-hour count. The separate rolling 365 day total is 104,141,514, through 2026-10-29.

## Coverage and gaps

All 230 public repositories were enumerated, including 27 forks and 0 archived repositories. Repository subscriptions and release pagination are complete. Open public issues and PRs are 1,589 and 1,360. Indexed search can differ from repository metadata because sources are not an atomic snapshot. Open issues and PR counts are separate search estimates; the cohort row reports GitHub's combined open_issues_count.

GitHub traffic was available through the owner-authorized ruOS interface. Across all repositories, clone events were 651,418 and view events were 215,680 from 2026-10-18 through 2026-10-31 UTC. Per-repository unique counts are retained in the dated snapshot; they are not summed across repositories. Commits and contributors were not refreshed.

## Running totals and verification

[Running totals](../data/ecosystem-running-totals.json), [daily npm ledger](../data/ecosystem-daily-ledger.json), and [release asset ledger](../data/release-asset-ledger.json) keep providers and metrics separate. Revised daily cells replace earlier observations; overlapping windows are never added. 8 release assets are absent from the complete current inventory; their last observed counts and deletion provenance are retained.

Validation passed: 30,214 unique daily keys, idempotent replay, total reconciliation, complete repository and release pagination, and explicit missing data. [Dated evidence](../data/snapshots/2026-11-01/).

## Progress toward 100 million

Observed combined registry downloads: 106,455,308; remaining: 0. Basis: npm since October 1, 2025 plus cumulative crates.io. npm contributes 104,430,311 through 2026-10-29; crates.io contributes 2,024,997. This is an observed lower bound. Clones and release assets are excluded. [Full npm evidence](../data/snapshots/2026-11-01/npm-downloads.json).
