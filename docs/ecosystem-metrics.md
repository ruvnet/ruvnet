# Ecosystem metrics

Verified November 15, 2026. Public repositories only. GitHub counts: 2026-11-15T13:23:03.592119+00:00.

| Metric | Count |
| --- | ---: |
| Public owned repositories | 234 |
| Original repositories | 207 |
| Public fork repositories | 27 |
| Stars across all owned repos | 203,627 |
| Stars across originals | 203,351 |
| Forks across all owned repos | 26,919 |
| Followers | 12,493 |
| Repository subscriptions | 1,808 |
| Published releases | 2,563 |
| Current release asset downloads | 119,858 |
| Retained observed release asset downloads | 119,861 |
| Rust crates | 501 |
| crates.io cumulative downloads | 2,251,140 |

## Repository cohorts

| Cohort | Public repositories | Stars | Forks | Subscribers | Open issues + PRs |
| --- | ---: | ---: | ---: | ---: | ---: |
| All owned | 234 | 203,627 | 26,919 | 1,808 | 2,467 |
| Nonfork | 207 | 203,351 | 26,839 | 1,805 | 2,460 |

## Activity: November 1 through November 14, UTC

| Metric | Count |
| --- | ---: |
| Issues opened | 210 |
| Issues closed | 537 |
| PRs opened | 885 |
| PRs merged | 700 |
| Releases published | 124 |
| Workflow runs | Unknown |

Workflow run counts are unknown. GitHub limits complete run enumeration to 1,000 results per query; this snapshot does not have complete workflow coverage.

## GitHub traffic

Across the complete 14-day UTC window, GitHub reported 833,472 clone events and 191,123 view events for 234 repositories. Unique cloners and visitors are retained per repository only and are not summed.

## Latest daily npm collection

The latest completed UTC day is **2026-11-14**. Its current collection has **4 of 429 eligible packages** observed, with **52 observed events** and a full total of **unknown**. Retrieved 2026-11-15T13:23:18.696526+00:00. [Daily source](../data/snapshots/2026-11-15/npm-daily-points.json). Download events include transitive installs and CI, not unique users.

## Completed download backfill

The completed November 9 through 13 source responses were collected November 12 through 14 and are reused without repeated provider calls.

| UTC day | npm download events | Eligible packages |
| --- | ---: | ---: |
| 2026-11-09 | 1,365,665 | 411 |
| 2026-11-10 | 1,297,163 | 412 |
| 2026-11-11 | 1,026,648 | 429 |
| 2026-11-12 | 1,032,765 | 429 |
| 2026-11-13 | 797,701 | 429 |

Latest complete daily observation: **797,701 on 2026-11-13 UTC**. On the same 429 eligible packages, November 13 recorded 797,701, compared with 1,032,765 on November 12, a change of -22.76%. 145 packages increased and 272 decreased. This is a daily change, not a sustained trend or causal impact of the constellation.

The npm only billion goal has **119,410,562 observed events since October 1, 2025**, using the dated baseline through 2026-11-08 plus disjoint completed daily cells. It is a lower bound with historical coverage gaps. Annual charts and the mixed provider milestone keep their original npm dates.

## Retained range and observed daily coverage

Observed sum across recorded cells for 2026-11-01 through 2026-11-14: 11,783,226. Full 7/30/prior30 comparable totals and growth remain null wherever coverage is incomplete.

## Matched weekly subset ending 2026-11-13

Across the same **405 packages**, 2026-11-07 through 2026-11-13 recorded **6,123,443** npm events versus **5,861,968** on 2026-10-31 through 2026-11-06, a change of **+4.46%**. 24 current inventory IDs lack complete coverage across both windows and are excluded. This does not fill the incomplete full-inventory window or establish causal constellation impact. [Subset evidence](../data/snapshots/2026-11-15/npm-weekly-subset.json).

## Coverage and gaps

All 234 public repositories were enumerated, including 27 forks and 0 archived repositories. Repository subscriptions and release pagination are complete. Open public issues and PRs are 1,256 and 1,209. Indexed search can differ from repository metadata because sources are not an atomic snapshot. Open issues and PR counts are separate search estimates; the cohort row reports GitHub's combined open_issues_count.

GitHub traffic was available through the owner-authorized ruOS interface. Across all repositories, clone events were 833,472 and view events were 191,123 from 2026-11-01 through 2026-11-14 UTC. Per-repository unique counts are retained in the dated snapshot; they are not summed across repositories. Commits and contributors were not refreshed.

## Running totals and verification

[Running totals](../data/ecosystem-running-totals.json), [daily npm ledger](../data/ecosystem-daily-ledger.json), and [release asset ledger](../data/release-asset-ledger.json) keep providers and metrics separate. Revised daily cells replace earlier observations; overlapping windows are never added. 8 release assets are absent from the complete current inventory; their last observed counts and deletion provenance are retained.

Validation passed: 42,289 unique daily keys, idempotent replay, total reconciliation, complete repository and release pagination, and explicit missing data. [Dated evidence](../data/snapshots/2026-11-15/).

## Progress toward 100 million

Observed combined registry downloads: 116,141,708; remaining: 0. Basis: npm since October 1, 2025 plus cumulative crates.io. npm contributes 113,890,568 through 2026-11-08; crates.io contributes 2,251,140. This is an observed lower bound. Clones and release assets are excluded. [Full npm evidence](../data/snapshots/2026-11-09/npm-downloads.json).

## Integration review

Current manifests were observed; existing recipes retain dated execution evidence. No new dependency, install, learning gain or package release is claimed. Missing frozen evaluator and fallback evidence remain gates.
