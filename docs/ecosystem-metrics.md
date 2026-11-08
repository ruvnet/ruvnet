# Ecosystem metrics

Verified November 8, 2026. Public repositories only. GitHub counts: 2026-11-08T13:13:10+00:00.

| Metric | Count |
| --- | ---: |
| Public owned repositories | 233 |
| Original repositories | 206 |
| Public fork repositories | 27 |
| Stars across all owned repos | 201,462 |
| Stars across originals | 201,197 |
| Forks across all owned repos | 26,604 |
| Followers | 12,322 |
| Repository subscriptions | 1,810 |
| Published releases | 2,466 |
| Current release asset downloads | 116,031 |
| Retained observed release asset downloads | 116,034 |
| Rust crates | 492 |
| crates.io cumulative downloads | 2,133,369 |

## Repository cohorts

| Cohort | Public repositories | Stars | Forks | Subscribers | Open issues + PRs |
| --- | ---: | ---: | ---: | ---: | ---: |
| All owned | 233 | 201,462 | 26,604 | 1,810 | 2,644 |
| Nonfork | 206 | 201,197 | 26,524 | 1,807 | 2,637 |

## Activity: October 25 through November 7, UTC

| Metric | Count |
| --- | ---: |
| Issues opened | 224 |
| Issues closed | 500 |
| PRs opened | 664 |
| PRs merged | 445 |
| Releases published | 54 |
| Workflow runs | Unknown |

Workflow run counts are unknown. GitHub limits complete run enumeration to 1,000 results per query; this snapshot does not have complete workflow coverage.

## GitHub traffic

Across the complete 14-day UTC window, GitHub reported 650,872 clone events and 236,102 view events for 233 repositories. Unique cloners and visitors are retained per repository only and are not summed.

## npm downloads

Confirmed daily-event sum: 10,263,568 across 405 of 405 packages for October 25 through November 7. All inventory packages have download-range evidence. Dates with incomplete package coverage: none. Missing package observations remain unknown (null); the sum includes only observed events. This is not a lifetime or rolling-24-hour count. The separate rolling 365 day total is 113,153,515, through 2026-11-07.

## Coverage and gaps

All 233 public repositories were enumerated, including 27 forks and 0 archived repositories. Repository subscriptions and release pagination are complete. Open public issues and PRs are 1,263 and 1,379. Indexed search can differ from repository metadata because sources are not an atomic snapshot. Open issues and PR counts are separate search estimates; the cohort row reports GitHub's combined open_issues_count.

GitHub traffic was available through the owner-authorized ruOS interface. Across all repositories, clone events were 650,872 and view events were 236,102 from 2026-10-25 through 2026-11-07 UTC. Per-repository unique counts are retained in the dated snapshot; they are not summed across repositories. Commits and contributors were not refreshed.

## Running totals and verification

[Running totals](../data/ecosystem-running-totals.json), [daily npm ledger](../data/ecosystem-daily-ledger.json), and [release asset ledger](../data/release-asset-ledger.json) keep providers and metrics separate. Revised daily cells replace earlier observations; overlapping windows are never added. 8 release assets are absent from the complete current inventory; their last observed counts and deletion provenance are retained.

Validation passed: 36,403 unique daily keys, idempotent replay, total reconciliation, complete repository and release pagination, and explicit missing data. [Dated evidence](../data/snapshots/2026-11-08/).

## Progress toward 100 million

Observed combined registry downloads: 115,635,647; remaining: 0. Basis: npm since October 1, 2025 plus cumulative crates.io. npm contributes 113,502,278 through 2026-11-07; crates.io contributes 2,133,369. This is an observed lower bound. Clones and release assets are excluded. [Full npm evidence](../data/snapshots/2026-11-08/npm-downloads.json).
