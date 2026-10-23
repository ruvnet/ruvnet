# Ecosystem metrics

Verified October 23, 2026. Public repositories only. GitHub counts: 2026-10-23T12:09:21+00:00.

| Metric | Count |
| --- | ---: |
| Public owned repositories | 229 |
| Original repositories | 202 |
| Public fork repositories | 27 |
| Stars across all owned repos | 194,890 |
| Stars across originals | 194,626 |
| Forks across all owned repos | 25,857 |
| Followers | 12,030 |
| Repository subscriptions | 1,782 |
| Published releases | 2,406 |
| Current release asset downloads | 110,899 |
| Retained observed release asset downloads | 110,902 |
| Rust crates | 481 |
| crates.io cumulative downloads | 1,945,305 |

## Repository cohorts

| Cohort | Public repositories | Stars | Forks | Subscribers | Open issues + PRs |
| --- | ---: | ---: | ---: | ---: | ---: |
| All owned | 229 | 194,890 | 25,857 | 1,782 | 2,799 |
| Nonfork | 202 | 194,626 | 25,778 | 1,779 | 2,789 |

## Activity: October 9 through October 22, UTC

| Metric | Count |
| --- | ---: |
| Issues opened | 247 |
| Issues closed | 174 |
| PRs opened | 748 |
| PRs merged | 460 |
| Releases published | 74 |
| Workflow runs | Unknown |

Workflow run counts are unknown. GitHub limits complete run enumeration to 1,000 results per query; this snapshot does not have complete workflow coverage.

## GitHub traffic

The requested 14-day UTC window has Unknown exact clone and view totals because 4 of 3206 repository-day cells per metric are missing. Known lower bounds are 751,700 clone events and 147,653 view events across 229 repositories. Unique cloners and visitors are retained per repository only and are not summed.

## npm downloads

Confirmed daily-event sum: 3,856,136 across 401 of 401 packages for October 9 through October 22. All inventory packages have download-range evidence. All-package-zero days 2026-10-13, 2026-10-14, 2026-10-15, 2026-10-19, 2026-10-20, 2026-10-21, 2026-10-22 are unknown (null), not zero, and excluded from the sum. This is not a lifetime or rolling-24-hour count. The separate rolling 365 day total is 98,249,631, through 2026-10-18.

## Coverage and gaps

All 229 public repositories were enumerated, including 27 forks and 0 archived repositories. Repository subscriptions and release pagination are complete. Open public issues and PRs are 1,540 and 1,257. Indexed search can differ from repository metadata because sources are not an atomic snapshot. Open issues and PR counts are separate search estimates; the cohort row reports GitHub's combined open_issues_count.

GitHub traffic was partially available through the owner-authorized ruOS interface. Missing dates: 2026-10-22; missing cells are null, never zero. The known lower bounds above cover 3202 of 3206 expected repository-day cells per metric from 2026-10-09 through 2026-10-22 UTC. Commits and contributors were not refreshed.

## Running totals and verification

[Running totals](../data/ecosystem-running-totals.json), [daily npm ledger](../data/ecosystem-daily-ledger.json), and [release asset ledger](../data/release-asset-ledger.json) keep providers and metrics separate. Revised daily cells replace earlier observations; overlapping windows are never added. 8 release assets are absent from the complete current inventory; their last observed counts and deletion provenance are retained.

Validation passed: 22,445 unique daily keys, idempotent replay, total reconciliation, complete repository and release pagination, and explicit missing data. [Dated evidence](../data/snapshots/2026-10-23/).

## Progress toward 100 million

Observed combined registry downloads: 100,336,176; remaining: 0. Basis: npm since October 1, 2025 plus cumulative crates.io. npm contributes 98,390,871 through 2026-10-18; crates.io contributes 1,945,305. This is an observed lower bound. Clones and release assets are excluded. [Full npm evidence](../data/snapshots/2026-10-23/npm-downloads.json).
