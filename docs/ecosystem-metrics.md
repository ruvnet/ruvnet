# Ecosystem metrics

Verified November 6, 2026. Public repositories only. GitHub counts: 2026-11-06T13:28:33+00:00.

| Metric | Count |
| --- | ---: |
| Public owned repositories | 232 |
| Original repositories | 205 |
| Public fork repositories | 27 |
| Stars across all owned repos | 200,933 |
| Stars across originals | 200,669 |
| Forks across all owned repos | 26,682 |
| Followers | 12,289 |
| Repository subscriptions | 1,809 |
| Published releases | 2,455 |
| Current release asset downloads | 115,176 |
| Retained observed release asset downloads | 115,179 |
| Rust crates | 492 |
| crates.io cumulative downloads | 2,110,392 |

## Repository cohorts

| Cohort | Public repositories | Stars | Forks | Subscribers | Open issues + PRs |
| --- | ---: | ---: | ---: | ---: | ---: |
| All owned | 232 | 200,933 | 26,682 | 1,809 | 2,676 |
| Nonfork | 205 | 200,669 | 26,589 | 1,806 | 2,666 |

## Activity: October 23 through November 5, UTC

| Metric | Count |
| --- | ---: |
| Issues opened | 219 |
| Issues closed | 501 |
| PRs opened | 614 |
| PRs merged | 392 |
| Releases published | 46 |
| Workflow runs | Unknown |

Workflow run counts are unknown. GitHub limits complete run enumeration to 1,000 results per query; this snapshot does not have complete workflow coverage.

## GitHub traffic

Across the complete 14-day UTC window, GitHub reported 614,843 clone events and 241,539 view events for 232 repositories. Unique cloners and visitors are retained per repository only and are not summed.

## npm downloads

Confirmed daily-event sum: 9,770,943 across 403 of 404 packages for October 23 through November 5. 1 npm package is missing download-range evidence. See [npm source evidence](../data/snapshots/2026-11-06/npm-downloads.json) for provider errors. Dates with incomplete package coverage: 2026-10-23, 2026-10-24, 2026-10-25, 2026-10-26, 2026-10-27, 2026-10-28, 2026-10-29, 2026-10-30, 2026-10-31, 2026-11-01, 2026-11-02, 2026-11-03, 2026-11-04, 2026-11-05. Missing package observations remain unknown (null); the sum includes only observed events. This is not a lifetime or rolling-24-hour count. The separate rolling 365 day total is 110,968,826, through 2026-11-05.

## Coverage and gaps

All 232 public repositories were enumerated, including 27 forks and 0 archived repositories. Repository subscriptions and release pagination are complete. Open public issues and PRs are 1,262 and 1,409. Indexed search can differ from repository metadata because sources are not an atomic snapshot. Open issues and PR counts are separate search estimates; the cohort row reports GitHub's combined open_issues_count.

GitHub traffic was available through the owner-authorized ruOS interface. Across all repositories, clone events were 614,843 and view events were 241,539 from 2026-10-23 through 2026-11-05 UTC. Per-repository unique counts are retained in the dated snapshot; they are not summed across repositories. Commits and contributors were not refreshed.

## Running totals and verification

[Running totals](../data/ecosystem-running-totals.json), [daily npm ledger](../data/ecosystem-daily-ledger.json), and [release asset ledger](../data/release-asset-ledger.json) keep providers and metrics separate. Revised daily cells replace earlier observations; overlapping windows are never added. 8 release assets are absent from the complete current inventory; their last observed counts and deletion provenance are retained.

Validation passed: 34,624 unique daily keys, idempotent replay, total reconciliation, complete repository and release pagination, and explicit missing data. [Dated evidence](../data/snapshots/2026-11-06/).

## Progress toward 100 million

Observed combined registry downloads: 113,410,310; remaining: 0. Basis: npm since October 1, 2025 plus cumulative crates.io. npm contributes 111,299,918 through 2026-11-05; crates.io contributes 2,110,392. This is an observed lower bound. Clones and release assets are excluded. [Full npm evidence](../data/snapshots/2026-11-06/npm-downloads.json).
