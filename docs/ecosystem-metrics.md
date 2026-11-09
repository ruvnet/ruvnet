# Ecosystem metrics

Verified November 9, 2026. Public repositories only. GitHub counts: 2026-11-09T13:32:01+00:00.

| Metric | Count |
| --- | ---: |
| Public owned repositories | 233 |
| Original repositories | 206 |
| Public fork repositories | 27 |
| Stars across all owned repos | 201,788 |
| Stars across originals | 201,523 |
| Forks across all owned repos | 26,635 |
| Followers | 12,333 |
| Repository subscriptions | 1,814 |
| Published releases | 2,504 |
| Current release asset downloads | 116,594 |
| Retained observed release asset downloads | 116,597 |
| Rust crates | 492 |
| crates.io cumulative downloads | 2,136,887 |

## Repository cohorts

| Cohort | Public repositories | Stars | Forks | Subscribers | Open issues + PRs |
| --- | ---: | ---: | ---: | ---: | ---: |
| All owned | 233 | 201,788 | 26,635 | 1,814 | 2,578 |
| Nonfork | 206 | 201,523 | 26,555 | 1,811 | 2,571 |

## Activity: October 26 through November 8, UTC

| Metric | Count |
| --- | ---: |
| Issues opened | 217 |
| Issues closed | 495 |
| PRs opened | 669 |
| PRs merged | 448 |
| Releases published | 57 |
| Workflow runs | Unknown |

Workflow run counts are unknown. GitHub limits complete run enumeration to 1,000 results per query; this snapshot does not have complete workflow coverage.

## GitHub traffic

Across the complete 14-day UTC window, GitHub reported 678,617 clone events and 229,165 view events for 233 repositories. Unique cloners and visitors are retained per repository only and are not summed.

## npm downloads

Confirmed daily-event sum: 10,125,521 across 405 of 408 packages for October 26 through November 8. 3 npm packages are missing download-range evidence. See [npm source evidence](../data/snapshots/2026-11-09/npm-downloads.json) for provider errors. Dates with incomplete package coverage: 2026-10-26, 2026-10-27, 2026-10-28, 2026-10-29, 2026-10-30, 2026-10-31, 2026-11-01, 2026-11-02, 2026-11-03, 2026-11-04, 2026-11-05, 2026-11-06, 2026-11-07, 2026-11-08. Missing package observations remain unknown (null); the sum includes only observed events. This is not a lifetime or rolling-24-hour count. The separate rolling 365 day total is 113,531,070, through 2026-11-08.

## Coverage and gaps

All 233 public repositories were enumerated, including 27 forks and 0 archived repositories. Repository subscriptions and release pagination are complete. Open public issues and PRs are 1,270 and 1,306. Indexed search can differ from repository metadata because sources are not an atomic snapshot. Open issues and PR counts are separate search estimates; the cohort row reports GitHub's combined open_issues_count.

GitHub traffic was available through the owner-authorized ruOS interface. Across all repositories, clone events were 678,617 and view events were 229,165 from 2026-10-26 through 2026-11-08 UTC. Per-repository unique counts are retained in the dated snapshot; they are not summed across repositories. Commits and contributors were not refreshed.

## Running totals and verification

[Running totals](../data/ecosystem-running-totals.json), [daily npm ledger](../data/ecosystem-daily-ledger.json), and [release asset ledger](../data/release-asset-ledger.json) keep providers and metrics separate. Revised daily cells replace earlier observations; overlapping windows are never added. 8 release assets are absent from the complete current inventory; their last observed counts and deletion provenance are retained.

Validation passed: 37,316 unique daily keys, idempotent replay, total reconciliation, complete repository and release pagination, and explicit missing data. [Dated evidence](../data/snapshots/2026-11-09/).

## Progress toward 100 million

Observed combined registry downloads: 116,027,455; remaining: 0. Basis: npm since October 1, 2025 plus cumulative crates.io. npm contributes 113,890,568 through 2026-11-08; crates.io contributes 2,136,887. This is an observed lower bound. Clones and release assets are excluded. [Full npm evidence](../data/snapshots/2026-11-09/npm-downloads.json).
