# Ecosystem metrics

Verified October 15, 2026. Public repositories only. GitHub counts: 2026-10-15T12:07:44+00:00.

| Metric | Count |
| --- | ---: |
| Public owned repositories | 226 |
| Original repositories | 199 |
| Public fork repositories | 27 |
| Stars across all owned repos | 189,740 |
| Stars across originals | 189,478 |
| Forks across all owned repos | 25,379 |
| Followers | 11,810 |
| Repository subscriptions | 1,771 |
| Published releases | 2,372 |
| Current release asset downloads | 109,230 |
| Retained observed release asset downloads | 109,233 |
| Rust crates | 481 |
| crates.io cumulative downloads | 1,880,174 |

## Repository cohorts

| Cohort | Public repositories | Stars | Forks | Subscribers | Open issues + PRs |
| --- | ---: | ---: | ---: | ---: | ---: |
| All owned | 226 | 189,740 | 25,379 | 1,771 | 2,741 |
| Nonfork | 199 | 189,478 | 25,300 | 1,768 | 2,731 |

## Activity: October 1 through October 14, UTC

| Metric | Count |
| --- | ---: |
| Issues opened | 315 |
| Issues closed | 213 |
| PRs opened | 876 |
| PRs merged | 532 |
| Releases published | 68 |
| Workflow runs | Unknown |

Workflow run counts are unknown. GitHub limits complete run enumeration to 1,000 results per query; this snapshot does not have complete workflow coverage.

## GitHub traffic

Across the complete 14-day UTC window, GitHub reported 838,888 clone events and 167,556 view events for 226 repositories. Unique cloners and visitors are available per repository only and are not summed. The Oct 1–13 site-harness rows are known zeros because its public repository was created on Oct 14.

## npm downloads

Observed 7,171,466 downloads across 399 of 401 packages for October 1 through October 14. Range responses are complete for the collected cohort. 2 npm packages are explicitly missing because their range endpoint returned HTTP 404 after bounded retries. The trailing zero-only date(s) 2026-10-13, 2026-10-14 are provisional and excluded from totals. This window is not a lifetime count. The separate rolling 365 day total is 97,022,120, through 2026-10-12.

## Latest confirmed npm day

**2026-10-12: 692,161 downloads** across 399 of 401 packages. This is a completed UTC calendar day, not a rolling 24-hour total. Newer zero-only dates are provisional and excluded. [Per-package snapshot](../data/snapshots/2026-10-15/npm-last-day.json).

## Traffic running totals

From 2026-10-01 through 2026-10-14 UTC (the complete observed period), GitHub reports 838,888 clone events and 167,556 view events across 226 repositories. These are events, not unique people. Per-repository unique counts are retained but not summed.

## Coverage and gaps

All 226 public repositories were enumerated, including 27 forks and 0 archived repositories. Repository subscriptions and release pagination are complete. Open public issues and PRs are 1,895 and 1,283. Indexed search can differ from repository metadata because sources are not an atomic snapshot. Open issues and PR counts are separate search estimates; the cohort row reports GitHub's combined open_issues_count.

GitHub traffic was available through the owner-authorized ruOS interface. Across all repositories, clone events were 838,888 and view events were 167,556 from 2026-10-01 through 2026-10-14 UTC. Per-repository unique counts are retained in the dated snapshot; they are not summed across repositories. Commits and contributors were not refreshed.

## Running totals and verification

[Running totals](../data/ecosystem-running-totals.json), [daily npm ledger](../data/ecosystem-daily-ledger.json), and [release asset ledger](../data/release-asset-ledger.json) keep providers and metrics separate. Revised daily cells replace earlier observations; overlapping windows are never added. 8 release assets are absent from the complete current inventory; their last observed counts and deletion provenance are retained.

Validation passed: 14,785 unique daily keys, idempotent replay, total reconciliation, complete repository and release pagination, and explicit missing data. [Dated evidence](../data/snapshots/2026-10-15/).

## Progress toward 100 million

Observed combined registry downloads: 98,950,384; remaining: 1,049,616. Basis: npm since October 1, 2025 plus cumulative crates.io. npm contributes 97,070,210 through 2026-10-12; crates.io contributes 1,880,174. This is an observed lower bound. Clones and release assets are excluded. [Full npm evidence](../data/snapshots/2026-10-15/npm-downloads.json).
