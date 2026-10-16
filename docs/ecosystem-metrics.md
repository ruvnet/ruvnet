# Ecosystem metrics

Verified October 16, 2026. Public repositories only. GitHub counts: 2026-10-16T12:21:49+00:00.

| Metric | Count |
| --- | ---: |
| Public owned repositories | 226 |
| Original repositories | 199 |
| Public fork repositories | 27 |
| Stars across all owned repos | 190,591 |
| Stars across originals | 190,329 |
| Forks across all owned repos | 25,450 |
| Followers | 11,834 |
| Repository subscriptions | 1,776 |
| Published releases | 2,373 |
| Current release asset downloads | 109,564 |
| Retained observed release asset downloads | 109,567 |
| Rust crates | 481 |
| crates.io cumulative downloads | 1,888,727 |

## Repository cohorts

| Cohort | Public repositories | Stars | Forks | Subscribers | Open issues + PRs |
| --- | ---: | ---: | ---: | ---: | ---: |
| All owned | 226 | 190,591 | 25,450 | 1,776 | 2,763 |
| Nonfork | 199 | 190,329 | 25,371 | 1,773 | 2,753 |

## Activity: October 2 through October 15, UTC

| Metric | Count |
| --- | ---: |
| Issues opened | 307 |
| Issues closed | 214 |
| PRs opened | 858 |
| PRs merged | 527 |
| Open issues at collection | 1,901 |
| Open pull requests at collection | 1,300 |
| Releases published | 67 |
| Workflow runs | Unknown |

Workflow run counts are unknown. GitHub limits complete run enumeration to 1,000 results per query; this snapshot does not have complete workflow coverage.

## GitHub traffic

Across the complete 14-day UTC window, GitHub reported 823,469 clone events and 164,098 view events for 226 repositories. Unique cloners and visitors are available per repository only and are not summed. Days before a public repository was created are known zeros; this refresh records 92 such clone/view repository-days across five repositories.

## npm downloads

Observed 6,567,706 downloads across 399 of 401 packages for October 2 through October 15. Confirmed daily coverage ends October 12, so this is a partial 14-day total; October 13–15 remain provisional unknowns and are excluded. Range responses are complete for the collected cohort. 2 npm packages are explicitly missing because their range endpoint returned HTTP 404 after bounded retries. Latest confirmed daily count: 692,161 npm download events on 2026-10-12 across 399 packages; this is the latest complete UTC date, not a rolling 24-hour total. The trailing zero-only dates 2026-10-13, 2026-10-14, and 2026-10-15 are provisional and excluded from totals. This window is not a lifetime count. The separate rolling 365 day total is 97,022,120, through 2026-10-12.

## Coverage and gaps

All 226 public repositories were enumerated, including 27 forks and 0 archived repositories. Repository subscriptions and release pagination are complete. Open public issues and PRs are 1,901 and 1,300. Indexed search can differ from repository metadata because sources are not an atomic snapshot. Open issues and PR counts are separate search estimates; the cohort row reports GitHub's combined open_issues_count.

GitHub traffic was available through the owner-authorized ruOS interface. Across all repositories, clone events were 823,469 and view events were 164,098 from 2026-10-02 through 2026-10-15 UTC. Per-repository unique counts are retained in the dated snapshot; they are not summed across repositories. Commits and contributors were not refreshed.

## Running totals and verification

[Running totals](../data/ecosystem-running-totals.json), [daily npm ledger](../data/ecosystem-daily-ledger.json), and [release asset ledger](../data/release-asset-ledger.json) keep providers and metrics separate. Revised daily cells replace earlier observations; overlapping windows are never added. 8 release assets are absent from the complete current inventory; their last observed counts and deletion provenance are retained.

Validation passed: 15,650 unique daily keys, idempotent replay, total reconciliation, complete repository and release pagination, and explicit missing data. [Dated evidence](../data/snapshots/2026-10-16/).

## Progress toward 100 million

Observed combined registry downloads: 98,958,937; remaining: 1,041,063. Basis: npm since October 1, 2025 plus cumulative crates.io. npm contributes 97,070,210 through 2026-10-12; crates.io contributes 1,888,727. This is an observed lower bound. Clones and release assets are excluded. [Full npm evidence](../data/snapshots/2026-10-16/npm-downloads.json).
