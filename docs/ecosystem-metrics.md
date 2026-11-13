# Ecosystem metrics

Verified November 13, 2026. Public repositories only. GitHub counts: 2026-11-13T13:48:51.725966+00:00.

| Metric | Count |
| --- | ---: |
| Public owned repositories | 234 |
| Original repositories | 207 |
| Public fork repositories | 27 |
| Stars across all owned repos | 203,168 |
| Stars across originals | 202,903 |
| Forks across all owned repos | 26,862 |
| Followers | 12,463 |
| Repository subscriptions | 1,806 |
| Published releases | 2,559 |
| Current release asset downloads | 118,999 |
| Retained observed release asset downloads | 119,002 |
| Rust crates | 500 |
| crates.io cumulative downloads | 2,238,352 |

## Repository cohorts

| Cohort | Public repositories | Stars | Forks | Subscribers | Open issues + PRs |
| --- | ---: | ---: | ---: | ---: | ---: |
| All owned | 234 | 203,168 | 26,862 | 1,806 | 2,440 |
| Nonfork | 207 | 202,903 | 26,782 | 1,803 | 2,433 |

## Activity: October 30 through November 12, UTC

| Metric | Count |
| --- | ---: |
| Issues opened | 219 |
| Issues closed | 539 |
| PRs opened | 910 |
| PRs merged | 718 |
| Releases published | 125 |
| Workflow runs | Unknown |

Workflow run counts are unknown. GitHub limits complete run enumeration to 1,000 results per query; this snapshot does not have complete workflow coverage.

## GitHub traffic

Across the complete 14-day UTC window, GitHub reported 765,547 clone events and 203,123 view events for 234 repositories. Unique cloners and visitors are retained per repository only and are not summed.

## Latest daily npm collection

The latest completed UTC day is **2026-11-12**. Its current collection has **2 of 429 eligible packages** observed, with **118 observed events** and a full total of **unknown**. Retrieved 2026-11-13T13:50:55.435179+00:00. [Daily source](../data/snapshots/2026-11-13/npm-daily-points.json). Download events include transitive installs and CI, not unique users.

## Completed download backfill

The completed November 9 through 11 source responses were collected November 12 and are reused without repeated provider calls.

| UTC day | npm download events | Eligible packages |
| --- | ---: | ---: |
| 2026-11-09 | 1,365,665 | 411 |
| 2026-11-10 | 1,297,163 | 412 |
| 2026-11-11 | 1,026,648 | 429 |

Latest complete daily observation: **1,026,648 on 2026-11-11 UTC**. On the same 412 eligible packages, November 11 recorded 1,015,012, compared with 1,297,163 on November 10, a change of -21.75%. 88 packages increased and 285 decreased. The 17 package expansion contributed 11,636 November 11 events separately. This is a daily change, not a sustained trend or causal impact of the constellation.

The npm only billion goal has **117,580,162 observed events since October 1, 2025**, using the dated baseline through 2026-11-08 plus disjoint completed daily cells. It is a lower bound with historical coverage gaps. Annual charts and the mixed provider milestone keep their original npm dates.

## Retained range and observed daily coverage

Observed sum across recorded cells for 2026-10-30 through 2026-11-12: 11,045,611. Full 7/30/prior30 comparable totals and growth remain null wherever coverage is incomplete.

## Coverage and gaps

All 234 public repositories were enumerated, including 27 forks and 0 archived repositories. Repository subscriptions and release pagination are complete. Open public issues and PRs are 1,250 and 1,188. Indexed search can differ from repository metadata because sources are not an atomic snapshot. Open issues and PR counts are separate search estimates; the cohort row reports GitHub's combined open_issues_count.

GitHub traffic was available through the owner-authorized ruOS interface. Across all repositories, clone events were 765,547 and view events were 203,123 from 2026-10-30 through 2026-11-12 UTC. Per-repository unique counts are retained in the dated snapshot; they are not summed across repositories. Commits and contributors were not refreshed.

## Running totals and verification

[Running totals](../data/ecosystem-running-totals.json), [daily npm ledger](../data/ecosystem-daily-ledger.json), and [release asset ledger](../data/release-asset-ledger.json) keep providers and metrics separate. Revised daily cells replace earlier observations; overlapping windows are never added. 8 release assets are absent from the complete current inventory; their last observed counts and deletion provenance are retained.

Validation passed: 40,493 unique daily keys, idempotent replay, total reconciliation, complete repository and release pagination, and explicit missing data. [Dated evidence](../data/snapshots/2026-11-13/).

## Progress toward 100 million

Observed combined registry downloads: 116,128,920; remaining: 0. Basis: npm since October 1, 2025 plus cumulative crates.io. npm contributes 113,890,568 through 2026-11-08; crates.io contributes 2,238,352. This is an observed lower bound. Clones and release assets are excluded. [Full npm evidence](../data/snapshots/2026-11-09/npm-downloads.json).

## Integration review

Current manifests were observed; existing recipes retain dated execution evidence. No new dependency, install, learning gain or package release is claimed. Missing frozen evaluator and fallback evidence remain gates.
