# Ecosystem metrics

Verified October 17, 2026. Public repositories only. GitHub counts: 2026-10-17T12:40:14+00:00.

| Metric | Count |
| --- | ---: |
| Public owned repositories | 227 |
| Original repositories | 200 |
| Public fork repositories | 27 |
| Stars across all owned repos | 191,155 |
| Stars across originals | 190,893 |
| Forks across all owned repos | 25,512 |
| Followers | 11,859 |
| Repository subscriptions | 1,779 |
| Published releases | 2,377 |
| Current release assets | 664 |
| Current release asset downloads | 109,776 |
| Retained observed release asset downloads | 109,779 |
| Rust crates | 481 |
| crates.io cumulative downloads | 1,896,424 |

## Repository cohorts

| Cohort | Public repositories | Stars | Forks | Subscribers | Open issues + PRs |
| --- | ---: | ---: | ---: | ---: | ---: |
| All owned | 227 | 191,155 | 25,512 | 1,779 | 2,805 |
| Nonfork | 200 | 190,893 | 25,433 | 1,776 | 2,795 |

## Activity: October 3 through October 16, UTC

| Metric | Count |
| --- | ---: |
| Issues opened | 297 |
| Issues closed | 204 |
| PRs opened | 825 |
| PRs merged | 508 |
| Releases published | 65 |
| Workflow runs | Unknown |

Workflow run counts are unknown. GitHub limits complete run enumeration to 1,000 results per query; this snapshot does not have complete workflow coverage.

## GitHub traffic

Across the complete 14-day UTC window, GitHub reported 808,366 clone events and 162,950 view events for 227 repositories. Unique cloners and visitors are available per repository only and are not summed. Known pre-creation zero rows are retained separately in the dated traffic audit (108 repository/metric/day cells); they are not evidence of traffic activity.

## npm downloads

Observed 5,922,340 downloads on reported dates October 3–12 across 399 of 401 packages. This is partial coverage, not a complete 14-day total: October 13–16 are unknown and excluded, and 2 packages have HTTP 404 range responses after bounded retries. October 6 was reported as an all-zero cohort day and is flagged for provider-latency review. This is not a lifetime count. The separate rolling 365 day total is 97,022,120, through 2026-10-12.

## Latest confirmed npm day

**2026-10-12: 692,161 downloads** across 399 of 401 packages. This is a completed UTC calendar day, not a rolling 24-hour total. Newer zero-only dates are provisional and excluded. [Per-package snapshot](../data/snapshots/2026-10-17/npm-last-day.json).

## Traffic running totals

From 2026-10-03 through 2026-10-16 UTC (the complete observed period), GitHub reports 808,366 clone events and 162,950 view events across 227 repositories. These are events, not unique people. Per-repository unique counts are retained but not summed.

## Coverage and gaps

All 227 public repositories were enumerated, including 27 forks and 0 archived repositories. Repository subscriptions and release pagination are complete. Open public issues and PRs are 1,915 and 1,331. Indexed search can differ from repository metadata because sources are not an atomic snapshot. Open issues and PR counts are separate search estimates; the cohort row reports GitHub's combined open_issues_count.

GitHub traffic was available through the owner-authorized ruOS interface. Across all repositories, clone events were 808,366 and view events were 162,950 from 2026-10-03 through 2026-10-16 UTC. Per-repository unique counts are retained in the dated snapshot; they are not summed across repositories. Commits and contributors were not refreshed.

## Running totals and verification

[Running totals](../data/ecosystem-running-totals.json), [daily npm ledger](../data/ecosystem-daily-ledger.json), and [release asset ledger](../data/release-asset-ledger.json) keep providers and metrics separate. Revised daily cells replace earlier observations; overlapping windows are never added. 8 release assets are absent from the complete current inventory; their last observed counts and deletion provenance are retained.

Validation passed: 16,529 unique daily keys, idempotent replay, total reconciliation, complete repository and release pagination, and explicit missing data. [Dated evidence](../data/snapshots/2026-10-17/).

## Progress toward 100 million

Observed combined registry downloads: 98,966,634; remaining: 1,033,366. Basis: npm since October 1, 2025 plus cumulative crates.io. npm contributes 97,070,210 through 2026-10-12; crates.io contributes 1,896,424. This is an observed lower bound. Clones and release assets are excluded. [Full npm evidence](../data/snapshots/2026-10-17/npm-downloads.json).
