# Ecosystem metrics

Verified October 19, 2026. Public repositories only. GitHub counts: 2026-10-19T12:53:39+00:00.

| Metric | Count |
| --- | ---: |
| Public owned repositories | 227 |
| Original repositories | 200 |
| Public fork repositories | 27 |
| Stars across all owned repos | 192,547 |
| Stars across originals | 192,284 |
| Forks across all owned repos | 25,634 |
| Followers | 11,921 |
| Repository subscriptions | 1,788 |
| Published releases | 2,379 |
| Current release asset downloads | 110,180 |
| Retained observed release asset downloads | 110,183 |
| Rust crates | 481 |
| crates.io cumulative downloads | 1,904,903 |

## Repository cohorts

| Cohort | Public repositories | Stars | Forks | Subscribers | Open issues + PRs |
| --- | ---: | ---: | ---: | ---: | ---: |
| All owned | 227 | 192,547 | 25,634 | 1,788 | 2,825 |
| Nonfork | 200 | 192,284 | 25,555 | 1,785 | 2,815 |

## Activity: October 5 through October 18, UTC

| Metric | Count |
| --- | ---: |
| Issues opened | 256 |
| Issues closed | 203 |
| PRs opened | 794 |
| PRs merged | 511 |
| Releases published | 64 |
| Workflow runs | Unknown |

Workflow run counts are unknown. GitHub limits complete run enumeration to 1,000 results per query; this snapshot does not have complete workflow coverage.

## GitHub traffic

Across the complete 14-day UTC window, GitHub reported 768,061 clone events and 165,068 view events for all 227 repositories with no missing repo/day cells. Unique cloners and visitors are available per repository only and are not summed. The Oct 5–13 site-harness rows are known zeros because its public repository was created on Oct 14.

## npm downloads

The sum of confirmed daily responses is 5,542,873 for October 5–18. Five dates (Oct 6, 13–15, 18) returned zero across every package; these cohort-wide zeros are recorded as unknown pending provider confirmation/backfill, not treated as zero demand. The other nine dates cover all 401 packages. This observed daily window is not a lifetime count. The separate rolling 365 day total is 97,770,971, through 2026-10-17.

## Coverage and gaps

All 227 public repositories were enumerated, including 27 forks and 0 archived repositories. Repository subscriptions and release pagination are complete. Open public issues and PRs are 1,551 and 1,272. Indexed search can differ from repository metadata because sources are not an atomic snapshot. Open issues and PR counts are separate search estimates; the cohort row reports GitHub's combined open_issues_count.

## Running totals and verification

[Running totals](../data/ecosystem-running-totals.json), [daily npm ledger](../data/ecosystem-daily-ledger.json), and [release asset ledger](../data/release-asset-ledger.json) keep providers and metrics separate. Revised daily cells replace earlier observations; overlapping windows are never added. 8 release assets are absent from the complete current inventory; their last observed counts and deletion provenance are retained.

Observed running traffic since 2026-09-30: 1,056,640 clone events and 230,830 view events through Oct 18. These are event totals, not unique people; unique counts are retained per repository only. Commits and contributors were not refreshed.

Validation passed: 18,965 unique daily keys, idempotent replay, total reconciliation, complete repository and release pagination, and explicit missing data. [Dated evidence](../data/snapshots/2026-10-19/). [Source/version watermark](../data/snapshots/2026-10-19/collection-watermark.json).

## Progress toward 100 million

Observed combined registry downloads: 99,802,370; remaining: 197,630. Basis: npm since October 1, 2025 plus cumulative crates.io. npm contributes 97,897,467 through 2026-10-17; crates.io contributes 1,904,903. This is an observed lower bound. Clones and release assets are excluded. [Full npm evidence](../data/snapshots/2026-10-19/npm-downloads.json).
