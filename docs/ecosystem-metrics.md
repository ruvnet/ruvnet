# Ecosystem metrics

Latest confirmed completed npm UTC day: **2026-11-14**, **611,657 events** across 429 packages. The November 15 source returned all 429 package responses at 2026-11-16T05:42:27Z, but its **22,805 observed events remain provisional**, including a later keyed revision of +5; the confirmed full daily total and growth are null. Counts can mature after the UTC day closes. November 14 UTC ran from November 13 at 7 pm through November 14 at 7 pm in Toronto.

Verified November 16, 2026. Public repositories only. GitHub counts: 2026-11-16T14:08:33.164546+00:00.

| Metric | Count |
| --- | ---: |
| Public owned repositories | 234 |
| Original repositories | 207 |
| Public fork repositories | 27 |
| Stars across all owned repos | 203,811 |
| Stars across originals | 203,535 |
| Forks across all owned repos | 26,934 |
| Followers | 12,504 |
| Repository subscriptions | 1,811 |
| Published releases | 2,563 |
| Current release asset downloads | 120,420 |
| Retained observed release asset downloads | 120,423 |
| Rust crates | 501 |
| crates.io cumulative downloads | 2,257,892 |

## Repository cohorts

| Cohort | Public repositories | Stars | Forks | Subscribers | Open issues + PRs |
| --- | ---: | ---: | ---: | ---: | ---: |
| All owned | 234 | 203,811 | 26,934 | 1,811 | 2,505 |
| Nonfork | 207 | 203,535 | 26,854 | 1,808 | 2,498 |

## Activity: November 2 through November 15, UTC

| Metric | Count |
| --- | ---: |
| Issues opened | 201 |
| Issues closed | 520 |
| PRs opened | 854 |
| PRs merged | 673 |
| Releases published | 119 |
| Workflow runs | Unknown |

Workflow run counts are unknown. GitHub limits complete run enumeration to 1,000 results per query; this snapshot does not have complete workflow coverage.

## GitHub traffic

The requested 14-day UTC window has Unknown exact clone and view totals because 234 of 3276 repository-day cells per metric are missing. Known lower bounds are 779,860 clone events and 177,259 view events across 234 repositories. Unique cloners and visitors are retained per repository only and are not summed.

## Latest daily npm collection

The latest completed UTC day is **2026-11-15**. Its current collection has **429 of 429 eligible packages** observed, with **22,805 observed events** and a full total of **unknown**. Retrieved 2026-11-16T14:08:56.772457+00:00. [Daily source](../data/snapshots/2026-11-16/npm-reconciled-2026-11-15.json). Download events include transitive installs and CI, not unique users.

## Completed download backfill

The current fixed-start registry snapshot and completed cached daily responses are reconciled by package ID and UTC date. Retrieval times remain source-specific.

| UTC day | npm download events | Eligible packages |
| --- | ---: | ---: |
| 2026-11-02 | 901,029 | 427 |
| 2026-11-03 | 695,465 | 427 |
| 2026-11-04 | 825,942 | 427 |
| 2026-11-05 | 885,389 | 427 |
| 2026-11-06 | 1,135,502 | 427 |
| 2026-11-07 | 532,206 | 427 |
| 2026-11-08 | 534,993 | 427 |
| 2026-11-09 | 1,365,665 | 427 |
| 2026-11-10 | 1,297,163 | 428 |
| 2026-11-11 | 1,026,648 | 429 |
| 2026-11-12 | 1,032,765 | 429 |
| 2026-11-13 | 797,701 | 429 |
| 2026-11-14 | 611,657 | 429 |

Latest complete daily observation: **611,657 on 2026-11-14 UTC**. On the same 429 eligible packages, 2026-11-14 recorded 611,657, compared with 797,701 on 2026-11-13, a change of -23.32%. 67 packages increased and 349 decreased. The 0 package expansion contributed 0 2026-11-14 events separately. This is a daily change, not a sustained trend or causal impact of the constellation.

The npm only billion goal has **120,946,147 observed events since October 1, 2025**, using the dated baseline through 2026-11-15 plus disjoint completed daily cells. It is a lower bound with historical coverage gaps. Annual charts and the mixed provider milestone keep their original npm dates.

## Retained range and observed daily coverage

Observed sum across recorded cells for 2026-11-02 through 2026-11-15: 11,664,930. Full 7/30/prior30 comparable totals and growth remain null wherever coverage is incomplete.

## Matched weekly subset ending 2026-11-14

Across the same **409 packages**, 2026-11-08 through 2026-11-14 recorded **6,396,155** npm events versus **5,874,942** on 2026-11-01 through 2026-11-07, a change of **+8.87%**. 270 increased and 128 decreased. 20 inventory IDs lack full coverage across both windows and remain outside this comparison. Dependency edges and download reach do not establish direct adoption or causal impact. [Subset evidence](../data/snapshots/2026-11-16/npm-weekly-subset.json).

## Coverage and gaps

All 234 public repositories were enumerated, including 27 forks and 0 archived repositories. Repository subscriptions and release pagination are complete. Open public issues and PRs are 1,264 and 1,240. Indexed search can differ from repository metadata because sources are not an atomic snapshot. Open issues and PR counts are separate search estimates; the cohort row reports GitHub's combined open_issues_count.

GitHub traffic was partially available through the owner-authorized ruOS interface. Missing dates: 2026-11-15; missing cells are null, never zero. The known lower bounds above cover 3042 of 3276 expected repository-day cells per metric from 2026-11-02 through 2026-11-15 UTC. Commits and contributors were not refreshed.

## Running totals and verification

[Running totals](../data/ecosystem-running-totals.json), [daily npm ledger](../data/ecosystem-daily-ledger.json), and [release asset ledger](../data/release-asset-ledger.json) keep providers and metrics separate. Revised daily cells replace earlier observations; overlapping windows are never added. 8 release assets are absent from the complete current inventory; their last observed counts and deletion provenance are retained.

Validation passed: 43,778 unique daily keys, idempotent replay, total reconciliation, complete repository and release pagination, and explicit missing data. [Dated evidence](../data/snapshots/2026-11-16/).

## Progress toward 100 million

Observed combined registry downloads: 123,204,034; remaining: 0. Basis: npm since October 1, 2025 plus cumulative crates.io. npm contributes 120,946,142 through 2026-11-15; crates.io contributes 2,257,892. This is an observed lower bound. Clones and release assets are excluded. [Full npm evidence](../data/snapshots/2026-11-16/npm-downloads.json).

## Integration review

Current manifests were observed; existing recipes retain dated execution evidence. No new dependency, install, learning gain or package release is claimed. Missing frozen evaluator and fallback evidence remain gates.

## Collection controls and integration evidence

This run reused the existing fixed-start registry workflow cache. One redundant daily npm request completed before cache reconciliation stopped the new worker; its later value revised one canonical cell from 0 to 5. No npm download worker is claimed to be active. The legacy registry workflow request implementation does not yet enforce the owner’s shared 30 second sequential pace and persistent cooldown policy; the separate [engineering guard PR 39](https://github.com/ruvnet/ruvnet/pull/39) must pass before another download crawl. No additional full crawl was run here.

Three unique manifests were refreshed: @metaharness/darwin, @ruvector/e-means and ruv-fann. Original pilot manifests retain their November 15 evidence; the rest retain dated or unknown graph evidence. The existing dependency graph accounts for 410 of 429 current package IDs, leaving 19 graph nodes unobserved. The existing CI recipe closes an equivalent-integration finding; this run does not establish a new install, held-out learning improvement, external adoption or package release. [Integration receipt](../data/snapshots/2026-11-16/integration-health-receipt.json).

The secondary mixed-provider milestone retains the original, unrevised npm registry measurement of 120,946,142 events retrieved 2026-11-16T05:42:27Z, plus its separately timestamped crates component. The canonical npm headline is 120,946,147 after the explicit +5 covered-day revision; these are dated source versions, not an unexplained discrepancy.
