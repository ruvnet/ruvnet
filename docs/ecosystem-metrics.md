# Ecosystem metrics

Verified October 22, 2026. Public repositories only. GitHub counts: 2026-10-22T12:12:26+00:00.

| Metric | Count |
| --- | ---: |
| Public owned repositories | 229 |
| Original repositories | 202 |
| Public fork repositories | 27 |
| Stars across all owned repos | 194,447 |
| Stars across originals | 194,183 |
| Forks across all owned repos | 25,807 |
| Followers | 11,988 |
| Repository subscriptions | 1,782 |
| Published releases | 2,402 |
| Current release asset downloads | 110,687 |
| Retained observed release asset downloads | 110,690 |
| Rust crates | 481 |
| crates.io cumulative downloads | 1,940,361 |

## Repository cohorts

| Cohort | Public repositories | Stars | Forks | Subscribers | Open issues + PRs |
| --- | ---: | ---: | ---: | ---: | ---: |
| All owned | 229 | 194,447 | 25,807 | 1,782 | 2,790 |
| Nonfork | 202 | 194,183 | 25,728 | 1,779 | 2,780 |

## Activity: October 8 through October 21, UTC

| Metric | Count |
| --- | ---: |
| Issues opened | 248 |
| Issues closed | 184 |
| PRs opened | 729 |
| PRs merged | 461 |
| Releases published | 69 |
| Workflow runs | Unknown |

Workflow run counts are unknown. GitHub limits complete run enumeration to 1,000 results per query; this snapshot does not have complete workflow coverage.

## GitHub traffic

Across the complete 14-day UTC window, GitHub reported 739,270 clone events and 154,730 view events for 229 repositories. Unique cloners and visitors are available per repository only and are not summed. The Oct 1–13 site-harness rows are known zeros because its public repository was created on Oct 14.

## npm downloads

Confirmed daily-event sum: 4,403,766 across 401 of 401 packages for October 8 through October 21. All inventory packages have download-range evidence. All-package-zero days 2026-10-13, 2026-10-14, 2026-10-15, 2026-10-19, 2026-10-20, 2026-10-21 are unknown (null), not zero, and excluded from the sum. This is not a lifetime or rolling-24-hour count. The separate rolling 365 day total is 98,249,631, through 2026-10-18.

## Coverage and gaps

All 229 public repositories were enumerated, including 27 forks and 0 archived repositories. Repository subscriptions and release pagination are complete. Open public issues and PRs are 1,536 and 1,252. Indexed search can differ from repository metadata because sources are not an atomic snapshot. Open issues and PR counts are separate search estimates; the cohort row reports GitHub's combined open_issues_count.

GitHub traffic was available through the owner-authorized ruOS interface. Across all repositories, clone events were 739,270 and view events were 154,730 from 2026-10-08 through 2026-10-21 UTC. Per-repository unique counts are retained in the dated snapshot; they are not summed across repositories. Commits and contributors were not refreshed.

## Running totals and verification

[Running totals](../data/ecosystem-running-totals.json), [daily npm ledger](../data/ecosystem-daily-ledger.json), and [release asset ledger](../data/release-asset-ledger.json) keep providers and metrics separate. Revised daily cells replace earlier observations; overlapping windows are never added. 8 release assets are absent from the complete current inventory; their last observed counts and deletion provenance are retained.

Validation passed: 21,586 unique daily keys, idempotent replay, total reconciliation, complete repository and release pagination, and explicit missing data. [Dated evidence](../data/snapshots/2026-10-22/).

## Progress toward 100 million

Observed combined registry downloads: 100,331,232; remaining: 0. Basis: npm since October 1, 2025 plus cumulative crates.io. npm contributes 98,390,871 through 2026-10-18; crates.io contributes 1,940,361. This is an observed lower bound. Clones and release assets are excluded. [Full npm evidence](../data/snapshots/2026-10-22/npm-downloads.json).
