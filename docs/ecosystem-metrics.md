# Ecosystem metrics

Verified November 4, 2026. Public repositories only. GitHub counts: 2026-11-04T13:57:41+00:00.

| Metric | Count |
| --- | ---: |
| Public owned repositories | 231 |
| Original repositories | 204 |
| Public fork repositories | 27 |
| Stars across all owned repos | 200,379 |
| Stars across originals | 200,115 |
| Forks across all owned repos | 26,598 |
| Followers | 12,252 |
| Repository subscriptions | 1,808 |
| Published releases | 2,446 |
| Current release asset downloads | 114,538 |
| Retained observed release asset downloads | 114,541 |
| Rust crates | 489 |
| crates.io cumulative downloads | 2,057,423 |

## Repository cohorts

| Cohort | Public repositories | Stars | Forks | Subscribers | Open issues + PRs |
| --- | ---: | ---: | ---: | ---: | ---: |
| All owned | 231 | 200,379 | 26,598 | 1,808 | 2,995 |
| Nonfork | 204 | 200,115 | 26,505 | 1,805 | 2,985 |

## Activity: October 21 through November 3, UTC

| Metric | Count |
| --- | ---: |
| Issues opened | 165 |
| Issues closed | 93 |
| PRs opened | 542 |
| PRs merged | 335 |
| Releases published | 59 |
| Workflow runs | Unknown |

Workflow run counts are unknown. GitHub limits complete run enumeration to 1,000 results per query; this snapshot does not have complete workflow coverage.

## GitHub traffic

Across the complete 14-day UTC window, GitHub reported 634,285 clone events and 221,724 view events for 231 repositories. Unique cloners and visitors are retained per repository only and are not summed.

## npm downloads

Confirmed daily-event sum: 8,779,893 across 401 of 401 packages for October 21 through November 3. All inventory packages have download-range evidence. All-package-zero days 2026-10-21 are unknown (null), not zero, and excluded from the sum. This is not a lifetime or rolling-24-hour count. The separate rolling 365 day total is 108,774,376, through 2026-11-03.

## Coverage and gaps

All 231 public repositories were enumerated, including 27 forks and 0 archived repositories. Repository subscriptions and release pagination are complete. Open public issues and PRs are 1,591 and 1,402. Indexed search can differ from repository metadata because sources are not an atomic snapshot. Open issues and PR counts are separate search estimates; the cohort row reports GitHub's combined open_issues_count.

GitHub traffic was available through the owner-authorized ruOS interface. Across all repositories, clone events were 634,285 and view events were 221,724 from 2026-10-21 through 2026-11-03 UTC. Per-repository unique counts are retained in the dated snapshot; they are not summed across repositories. Commits and contributors were not refreshed.

## Running totals and verification

[Running totals](../data/ecosystem-running-totals.json), [daily npm ledger](../data/ecosystem-daily-ledger.json), and [release asset ledger](../data/release-asset-ledger.json) keep providers and metrics separate. Revised daily cells replace earlier observations; overlapping windows are never added. 8 release assets are absent from the complete current inventory; their last observed counts and deletion provenance are retained.

Validation passed: 32,827 unique daily keys, idempotent replay, total reconciliation, complete repository and release pagination, and explicit missing data. [Dated evidence](../data/snapshots/2026-11-04/).

## Progress toward 100 million

Observed combined registry downloads: 111,149,562; remaining: 0. Basis: npm since October 1, 2025 plus cumulative crates.io. npm contributes 109,092,139 through 2026-11-03; crates.io contributes 2,057,423. This is an observed lower bound. Clones and release assets are excluded. [Full npm evidence](../data/snapshots/2026-11-04/npm-downloads.json).
