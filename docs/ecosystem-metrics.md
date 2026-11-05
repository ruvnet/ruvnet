# Ecosystem metrics

Verified November 5, 2026. Public repositories only. GitHub counts: 2026-11-05T13:25:06+00:00.

| Metric | Count |
| --- | ---: |
| Public owned repositories | 231 |
| Original repositories | 204 |
| Public fork repositories | 27 |
| Stars across all owned repos | 200,670 |
| Stars across originals | 200,406 |
| Forks across all owned repos | 26,644 |
| Followers | 12,280 |
| Repository subscriptions | 1,814 |
| Published releases | 2,450 |
| Current release asset downloads | 114,860 |
| Retained observed release asset downloads | 114,863 |
| Rust crates | 492 |
| crates.io cumulative downloads | 2,080,867 |

## Repository cohorts

| Cohort | Public repositories | Stars | Forks | Subscribers | Open issues + PRs |
| --- | ---: | ---: | ---: | ---: | ---: |
| All owned | 231 | 200,670 | 26,644 | 1,814 | 3,096 |
| Nonfork | 204 | 200,406 | 26,551 | 1,811 | 3,086 |

## Activity: October 22 through November 4, UTC

| Metric | Count |
| --- | ---: |
| Issues opened | 155 |
| Issues closed | 98 |
| PRs opened | 564 |
| PRs merged | 371 |
| Releases published | 50 |
| Workflow runs | Unknown |

Workflow run counts are unknown. GitHub limits complete run enumeration to 1,000 results per query; this snapshot does not have complete workflow coverage.

## GitHub traffic

Across the complete 14-day UTC window, GitHub reported 626,654 clone events and 229,931 view events for 231 repositories. Unique cloners and visitors are retained per repository only and are not summed.

## npm downloads

Confirmed daily-event sum: 9,605,835 across 402 of 402 packages for October 22 through November 4. All inventory packages have download-range evidence. All-package-zero days none are unknown (null), not zero, and excluded from the sum. This is not a lifetime or rolling-24-hour count. The separate rolling 365 day total is 109,592,875, through 2026-11-04.

## Coverage and gaps

All 231 public repositories were enumerated, including 27 forks and 0 archived repositories. Repository subscriptions and release pagination are complete. Open public issues and PRs are 1,661 and 1,433. Indexed search can differ from repository metadata because sources are not an atomic snapshot. Open issues and PR counts are separate search estimates; the cohort row reports GitHub's combined open_issues_count.

GitHub traffic was available through the owner-authorized ruOS interface. Across all repositories, clone events were 626,654 and view events were 229,931 from 2026-10-22 through 2026-11-04 UTC. Per-repository unique counts are retained in the dated snapshot; they are not summed across repositories. Commits and contributors were not refreshed.

## Running totals and verification

[Running totals](../data/ecosystem-running-totals.json), [daily npm ledger](../data/ecosystem-daily-ledger.json), and [release asset ledger](../data/release-asset-ledger.json) keep providers and metrics separate. Revised daily cells replace earlier observations; overlapping windows are never added. 8 release assets are absent from the complete current inventory; their last observed counts and deletion provenance are retained.

Validation passed: 33,704 unique daily keys, idempotent replay, total reconciliation, complete repository and release pagination, and explicit missing data. [Dated evidence](../data/snapshots/2026-11-05/).

## Progress toward 100 million

Observed combined registry downloads: 111,998,948; remaining: 0. Basis: npm since October 1, 2025 plus cumulative crates.io. npm contributes 109,918,081 through 2026-11-04; crates.io contributes 2,080,867. This is an observed lower bound. Clones and release assets are excluded. [Full npm evidence](../data/snapshots/2026-11-05/npm-downloads.json).
