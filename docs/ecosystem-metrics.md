# Ecosystem metrics

Verified October 20, 2026. Public repositories only. GitHub counts: 2026-10-20T12:55:13+00:00.

| Metric | Count |
| --- | ---: |
| Public owned repositories | 227 |
| Original repositories | 200 |
| Public fork repositories | 27 |
| Stars across all owned repos | 193,368 |
| Stars across originals | 193,105 |
| Forks across all owned repos | 25,696 |
| Followers | 11,943 |
| Repository subscriptions | 1,786 |
| Published releases | 2,384 |
| Current release asset downloads | 110,367 |
| Retained observed release asset downloads | 110,370 |
| Rust crates | 481 |
| crates.io cumulative downloads | 1,916,107 |

## Repository cohorts

| Cohort | Public repositories | Stars | Forks | Subscribers | Open issues + PRs |
| --- | ---: | ---: | ---: | ---: | ---: |
| All owned | 227 | 193,368 | 25,696 | 1,786 | 2,764 |
| Nonfork | 200 | 193,105 | 25,617 | 1,783 | 2,754 |

## Activity: October 6 through October 19, UTC

| Metric | Count |
| --- | ---: |
| Issues opened | 238 |
| Issues closed | 197 |
| PRs opened | 707 |
| PRs merged | 421 |
| Releases published | 64 |
| Workflow runs | Unknown |

Workflow run counts are unknown. GitHub limits complete run enumeration to 1,000 results per query; this snapshot does not have complete workflow coverage.

## GitHub traffic

Across the complete 14-day UTC window, GitHub reported 754,064 clone events and 163,457 view events for 227 repositories. Unique cloners and visitors are available per repository only and are not summed. The Oct 1–13 site-harness rows are known zeros because its public repository was created on Oct 14.

## npm downloads

Confirmed daily-event sum: 5,225,040 across 401 of 401 packages for October 6 through October 19. All inventory packages have download-range evidence. All-package-zero days 2026-10-06, 2026-10-13, 2026-10-14, 2026-10-15, 2026-10-19 are unknown (null), not zero, and excluded from the sum. This is not a lifetime or rolling-24-hour count. The separate rolling 365 day total is 98,249,631, through 2026-10-18.

## Coverage and gaps

All 227 public repositories were enumerated, including 27 forks and 0 archived repositories. Repository subscriptions and release pagination are complete. Open public issues and PRs are 1,524 and 1,238. Indexed search can differ from repository metadata because sources are not an atomic snapshot. Open issues and PR counts are separate search estimates; the cohort row reports GitHub's combined open_issues_count.

GitHub traffic was available through the owner-authorized ruOS interface. Across all repositories, clone events were 754,064 and view events were 163,457 from 2026-10-06 through 2026-10-19 UTC. Per-repository unique counts are retained in the dated snapshot; they are not summed across repositories. Commits and contributors were not refreshed.

## Running totals and verification

[Running totals](../data/ecosystem-running-totals.json), [daily npm ledger](../data/ecosystem-daily-ledger.json), and [release asset ledger](../data/release-asset-ledger.json) keep providers and metrics separate. Revised daily cells replace earlier observations; overlapping windows are never added. 8 release assets are absent from the complete current inventory; their last observed counts and deletion provenance are retained.

Validation passed: 19,820 unique daily keys, idempotent replay, total reconciliation, complete repository and release pagination, and explicit missing data. [Dated evidence](../data/snapshots/2026-10-20/).

## Progress toward 100 million

Observed combined registry downloads: 100,306,978; remaining: 0. Basis: npm since October 1, 2025 plus cumulative crates.io. npm contributes 98,390,871 through 2026-10-18; crates.io contributes 1,916,107. This is an observed lower bound. Clones and release assets are excluded. [Full npm evidence](../data/snapshots/2026-10-20/npm-downloads.json).
