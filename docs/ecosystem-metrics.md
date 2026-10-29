# Ecosystem metrics

Verified October 29, 2026. Public repositories only. GitHub counts: 2026-10-29T12:41:38+00:00.

| Metric | Count |
| --- | ---: |
| Public owned repositories | 230 |
| Original repositories | 203 |
| Public fork repositories | 27 |
| Stars across all owned repos | 198,619 |
| Stars across originals | 198,356 |
| Forks across all owned repos | 26,381 |
| Followers | 12,177 |
| Repository subscriptions | 1,798 |
| Published releases | 2,429 |
| Current release asset downloads | 112,568 |
| Retained observed release asset downloads | 112,571 |
| Rust crates | 489 |
| crates.io cumulative downloads | 2,004,915 |

## Repository cohorts

| Cohort | Public repositories | Stars | Forks | Subscribers | Open issues + PRs |
| --- | ---: | ---: | ---: | ---: | ---: |
| All owned | 230 | 198,619 | 26,381 | 1,798 | 2,883 |
| Nonfork | 203 | 198,356 | 26,289 | 1,795 | 2,873 |

## Activity: October 15 through October 28, UTC

| Metric | Count |
| --- | ---: |
| Issues opened | 163 |
| Issues closed | 127 |
| PRs opened | 525 |
| PRs merged | 373 |
| Releases published | 58 |
| Workflow runs | Unknown |

Workflow run counts are unknown. GitHub limits complete run enumeration to 1,000 results per query; this snapshot does not have complete workflow coverage.

## GitHub traffic

Across the complete 14-day UTC window, GitHub reported 653,319 clone events and 191,463 view events for 230 repositories. Unique cloners and visitors are retained per repository only and are not summed.

## npm downloads

Confirmed daily-event sum: 5,129,746 across 401 of 401 packages for October 15 through October 28. All inventory packages have download-range evidence. All-package-zero days 2026-10-15, 2026-10-19, 2026-10-20, 2026-10-21, 2026-10-28 are unknown (null), not zero, and excluded from the sum. This is not a lifetime or rolling-24-hour count. The separate rolling 365 day total is 102,770,896, through 2026-10-27.

## Coverage and gaps

All 230 public repositories were enumerated, including 27 forks and 0 archived repositories. Repository subscriptions and release pagination are complete. Open public issues and PRs are 1,565 and 1,316. Indexed search can differ from repository metadata because sources are not an atomic snapshot. Open issues and PR counts are separate search estimates; the cohort row reports GitHub's combined open_issues_count.

GitHub traffic was available through the owner-authorized ruOS interface. Across all repositories, clone events were 653,319 and view events were 191,463 from 2026-10-15 through 2026-10-28 UTC. Per-repository unique counts are retained in the dated snapshot; they are not summed across repositories. Commits and contributors were not refreshed.

## Running totals and verification

[Running totals](../data/ecosystem-running-totals.json), [daily npm ledger](../data/ecosystem-daily-ledger.json), and [release asset ledger](../data/release-asset-ledger.json) keep providers and metrics separate. Revised daily cells replace earlier observations; overlapping windows are never added. 8 release assets are absent from the complete current inventory; their last observed counts and deletion provenance are retained.

Validation passed: 27,631 unique daily keys, idempotent replay, total reconciliation, complete repository and release pagination, and explicit missing data. [Dated evidence](../data/snapshots/2026-10-29/).

## Progress toward 100 million

Observed combined registry downloads: 105,053,106; remaining: 0. Basis: npm since October 1, 2025 plus cumulative crates.io. npm contributes 103,048,191 through 2026-10-27; crates.io contributes 2,004,915. This is an observed lower bound. Clones and release assets are excluded. [Full npm evidence](../data/snapshots/2026-10-29/npm-downloads.json).
