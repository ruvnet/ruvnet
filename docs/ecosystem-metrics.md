# Ecosystem metrics

Verified November 3, 2026. Public repositories only. GitHub counts: 2026-11-03T13:29:00+00:00.

| Metric | Count |
| --- | ---: |
| Public owned repositories | 231 |
| Original repositories | 204 |
| Public fork repositories | 27 |
| Stars across all owned repos | 200,095 |
| Stars across originals | 199,831 |
| Forks across all owned repos | 26,573 |
| Followers | 12,247 |
| Repository subscriptions | 1,805 |
| Published releases | 2,445 |
| Current release asset downloads | 114,207 |
| Retained observed release asset downloads | 114,210 |
| Rust crates | 489 |
| crates.io cumulative downloads | 2,039,972 |

## Repository cohorts

| Cohort | Public repositories | Stars | Forks | Subscribers | Open issues + PRs |
| --- | ---: | ---: | ---: | ---: | ---: |
| All owned | 231 | 200,095 | 26,573 | 1,805 | 2,978 |
| Nonfork | 204 | 199,831 | 26,480 | 1,802 | 2,968 |

## Activity: October 20 through November 2, UTC

| Metric | Count |
| --- | ---: |
| Issues opened | 169 |
| Issues closed | 114 |
| PRs opened | 561 |
| PRs merged | 377 |
| Releases published | 63 |
| Workflow runs | Unknown |

Workflow run counts are unknown. GitHub limits complete run enumeration to 1,000 results per query; this snapshot does not have complete workflow coverage.

## GitHub traffic

Across the complete 14-day UTC window, GitHub reported 656,199 clone events and 218,302 view events for 231 repositories. Unique cloners and visitors are retained per repository only and are not summed.

## npm downloads

Confirmed daily-event sum: 8,084,428 across 401 of 401 packages for October 20 through November 2. All inventory packages have download-range evidence. All-package-zero days 2026-10-20, 2026-10-21 are unknown (null), not zero, and excluded from the sum. This is not a lifetime or rolling-24-hour count. The separate rolling 365 day total is 107,551,099, through 2026-11-02.

## Coverage and gaps

All 231 public repositories were enumerated, including 27 forks and 0 archived repositories. Repository subscriptions and release pagination are complete. Open public issues and PRs are 1,593 and 1,383. Indexed search can differ from repository metadata because sources are not an atomic snapshot. Open issues and PR counts are separate search estimates; the cohort row reports GitHub's combined open_issues_count.

GitHub traffic was available through the owner-authorized ruOS interface. Across all repositories, clone events were 656,199 and view events were 218,302 from 2026-10-20 through 2026-11-02 UTC. Per-repository unique counts are retained in the dated snapshot; they are not summed across repositories. Commits and contributors were not refreshed.

## Running totals and verification

[Running totals](../data/ecosystem-running-totals.json), [daily npm ledger](../data/ecosystem-daily-ledger.json), and [release asset ledger](../data/release-asset-ledger.json) keep providers and metrics separate. Revised daily cells replace earlier observations; overlapping windows are never added. 8 release assets are absent from the complete current inventory; their last observed counts and deletion provenance are retained.

Validation passed: 31,964 unique daily keys, idempotent replay, total reconciliation, complete repository and release pagination, and explicit missing data. [Dated evidence](../data/snapshots/2026-11-03/).

## Progress toward 100 million

Observed combined registry downloads: 109,901,735; remaining: 0. Basis: npm since October 1, 2025 plus cumulative crates.io. npm contributes 107,861,763 through 2026-11-02; crates.io contributes 2,039,972. This is an observed lower bound. Clones and release assets are excluded. [Full npm evidence](../data/snapshots/2026-11-03/npm-downloads.json).
