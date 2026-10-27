# Ecosystem metrics

Verified October 27, 2026. Public repositories only. GitHub counts: 2026-10-27T12:24:19+00:00.

| Metric | Count |
| --- | ---: |
| Public owned repositories | 230 |
| Original repositories | 203 |
| Public fork repositories | 27 |
| Stars across all owned repos | 196,741 |
| Stars across originals | 196,478 |
| Forks across all owned repos | 26,077 |
| Followers | 12,109 |
| Repository subscriptions | 1,787 |
| Published releases | 2,423 |
| Current release asset downloads | 111,867 |
| Retained observed release asset downloads | 111,870 |
| Rust crates | 489 |
| crates.io cumulative downloads | 1,985,542 |

## Repository cohorts

| Cohort | Public repositories | Stars | Forks | Subscribers | Open issues + PRs |
| --- | ---: | ---: | ---: | ---: | ---: |
| All owned | 230 | 196,741 | 26,077 | 1,787 | 2,844 |
| Nonfork | 203 | 196,478 | 25,998 | 1,784 | 2,834 |

## Activity: October 13 through October 26, UTC

| Metric | Count |
| --- | ---: |
| Issues opened | 206 |
| Issues closed | 152 |
| PRs opened | 548 |
| PRs merged | 380 |
| Releases published | 61 |
| Workflow runs | Unknown |

Workflow run counts are unknown. GitHub limits complete run enumeration to 1,000 results per query; this snapshot does not have complete workflow coverage.

## GitHub traffic

Across the complete 14-day UTC window, GitHub reported 670,176 clone events and 164,504 view events for 230 repositories. Unique cloners and visitors are retained per repository only and are not summed.

## npm downloads

Confirmed daily-event sum: 3,742,362 across 401 of 401 packages for October 13 through October 26. All inventory packages have download-range evidence. All-package-zero days 2026-10-13, 2026-10-14, 2026-10-15, 2026-10-19, 2026-10-20, 2026-10-21, 2026-10-26 are unknown (null), not zero, and excluded from the sum. This is not a lifetime or rolling-24-hour count. The separate rolling 365 day total is 101,398,888, through 2026-10-25.

## Coverage and gaps

All 230 public repositories were enumerated, including 27 forks and 0 archived repositories. Repository subscriptions and release pagination are complete. Open public issues and PRs are 1,551 and 1,292. Indexed search can differ from repository metadata because sources are not an atomic snapshot. Open issues and PR counts are separate search estimates; the cohort row reports GitHub's combined open_issues_count.

GitHub traffic was available through the owner-authorized ruOS interface. Across all repositories, clone events were 670,176 and view events were 164,504 from 2026-10-13 through 2026-10-26 UTC. Per-repository unique counts are retained in the dated snapshot; they are not summed across repositories. Commits and contributors were not refreshed.

## Running totals and verification

[Running totals](../data/ecosystem-running-totals.json), [daily npm ledger](../data/ecosystem-daily-ledger.json), and [release asset ledger](../data/release-asset-ledger.json) keep providers and metrics separate. Revised daily cells replace earlier observations; overlapping windows are never added. 8 release assets are absent from the complete current inventory; their last observed counts and deletion provenance are retained.

Validation passed: 25,909 unique daily keys, idempotent replay, total reconciliation, complete repository and release pagination, and explicit missing data. [Dated evidence](../data/snapshots/2026-10-27/).

## Progress toward 100 million

Observed combined registry downloads: 103,646,349; remaining: 0. Basis: npm since October 1, 2025 plus cumulative crates.io. npm contributes 101,660,807 through 2026-10-25; crates.io contributes 1,985,542. This is an observed lower bound. Clones and release assets are excluded. [Full npm evidence](../data/snapshots/2026-10-27/npm-downloads.json).
