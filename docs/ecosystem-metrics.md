# Ecosystem metrics

Latest confirmed npm UTC day: **2026-11-17**, **937,157 events** across 429 packages. Latest completed UTC day 2026-11-27 has **29,037 observed events from 11/430 packages**, retrieved 2026-11-28T13:27:21.619393+00:00; full total and growth remain null. Provider revisions and missing observations remain explicit.

Verified November 28, 2026. Public repositories only. GitHub counts: 2026-11-28T13:21:38.260373+00:00.

| Metric | Count |
| --- | ---: |
| Public owned repositories | 235 |
| Original repositories | 208 |
| Public fork repositories | 27 |
| Stars across all owned repos | 205,605 |
| Stars across originals | 205,329 |
| Forks across all owned repos | 27,206 |
| Followers | 12,628 |
| Repository subscriptions | 1,822 |
| Published releases | 2,596 |
| Current release asset downloads | 124,271 |
| Retained observed release asset downloads | 124,274 |
| Rust crates | 501 |
| crates.io cumulative downloads | 2,321,390 |

## Repository cohorts

| Cohort | Public repositories | Stars | Forks | Subscribers | Open issues + PRs |
| --- | ---: | ---: | ---: | ---: | ---: |
| All owned | 235 | 205,605 | 27,206 | 1,822 | 2,592 |
| Nonfork | 208 | 205,329 | 27,125 | 1,819 | 2,585 |

## Activity: November 14 through November 27, UTC

| Metric | Count |
| --- | ---: |
| Issues opened | 112 |
| Issues closed | 96 |
| PRs opened | 332 |
| PRs merged | 173 |
| Releases published | 36 |
| Workflow runs | Unknown |

Workflow run counts are unknown. GitHub limits complete run enumeration to 1,000 results per query; this snapshot does not have complete workflow coverage.

## GitHub traffic

The requested 14-day UTC window has Unknown exact clone and view totals because 12 of 3290 repository-day cells per metric are missing. Known lower bounds are 676,729 clone events and 152,661 view events across 235 repositories. Unique cloners and visitors are retained per repository only and are not summed.

## Latest daily npm collection

The latest completed UTC day is **2026-11-27**. Its current collection has **11 of 430 eligible packages** observed, with **29,037 observed events** and a full total of **unknown**. Retrieved 2026-11-28T13:27:21.619393+00:00. [Daily source](../data/snapshots/2026-11-28/npm-reconciled-2026-11-27.json). Download events include transitive installs and CI, not unique users.

## Completed download backfill

The current fixed-start registry snapshot and completed cached daily responses are reconciled by package ID and UTC date. Retrieval times remain source-specific.

| UTC day | npm download events | Observed / eligible packages |
| --- | ---: | ---: |
| 2026-11-14 | 611,657 | 429/429 |
| 2026-11-15 | 539,258 | 429/429 |
| 2026-11-16 | 751,377 | 429/429 |
| 2026-11-17 | 937,157 | 429/429 |
| 2026-11-18 | 420,550 (provisional) | 271/430 |
| 2026-11-19 | 414,240 (provisional) | 219/430 |
| 2026-11-20 | 264,094 (provisional) | 200/430 |
| 2026-11-21 | 107,907 (provisional) | 75/430 |
| 2026-11-22 | 117,189 (provisional) | 75/430 |
| 2026-11-23 | 159,045 (provisional) | 75/430 |
| 2026-11-24 | 151,037 (provisional) | 75/430 |
| 2026-11-25 | 307,674 (provisional) | 75/430 |
| 2026-11-26 | 276,812 (provisional) | 75/430 |

Latest complete daily observation: **937,157 on 2026-11-17 UTC**. On the same 429 eligible packages, 2026-11-17 recorded 937,157, compared with 751,377 on 2026-11-16, a change of 24.73%. 233 packages increased and 143 decreased. The 0 package expansion contributed 0 2026-11-17 events separately. This is a daily change, not a sustained trend or causal impact of the constellation.

The npm only billion goal has **125,398,719 observed events since October 1, 2025**, using the dated baseline through 2026-11-15 plus disjoint completed daily cells. It is a lower bound with historical coverage gaps. Annual charts and the mixed provider milestone keep their original npm dates.

## Retained range and observed daily coverage

Observed sum across recorded cells for 2026-11-14 through 2026-11-27: 5,087,034. Full 7/30/prior30 comparable totals and growth remain null wherever coverage is incomplete.

## Matched weekly subset ending 2026-11-17

Across the same **429 packages**, 2026-11-11 through 2026-11-17 recorded **5,696,563** events versus **6,576,860** for 2026-11-04 through 2026-11-10, **-13.38%**. 107 increased and 314 decreased. 1 IDs lack comparable coverage and are excluded. Download reach does not establish direct adoption or causal impact. [Evidence](../data/snapshots/2026-11-28/npm-weekly-subset.json).

## Coverage and gaps

All 235 public repositories were enumerated, including 27 forks and 0 archived repositories. Repository subscriptions and release pagination are complete. Open public issues and PRs are 1,269 and 1,320. Indexed search can differ from repository metadata because sources are not an atomic snapshot. Open issues and PR counts are separate search estimates; the cohort row reports GitHub's combined open_issues_count.

GitHub traffic was partially available through the owner-authorized ruOS interface. Missing dates: 2026-11-17, 2026-11-18, 2026-11-19, 2026-11-20, 2026-11-21, 2026-11-22, 2026-11-23, 2026-11-24, 2026-11-25, 2026-11-26, 2026-11-27; missing cells are null, never zero. The known lower bounds above cover 3278 of 3290 expected repository-day cells per metric from 2026-11-14 through 2026-11-27 UTC. Commits and contributors were not refreshed.

## Running totals and verification

[Running totals](../data/ecosystem-running-totals.json), [daily npm ledger](../data/ecosystem-daily-ledger.json), and [release asset ledger](../data/release-asset-ledger.json) keep providers and metrics separate. Revised daily cells replace earlier observations; overlapping windows are never added. 8 release assets are absent from the complete current inventory; their last observed counts and deletion provenance are retained.

Validation passed: 51,451 unique daily keys, idempotent replay, total reconciliation, complete repository and release pagination, and explicit missing data. [Dated evidence](../data/snapshots/2026-11-28/).

## Progress toward 100 million

Observed combined registry downloads: 123,267,532; remaining: 0. Basis: npm since October 1, 2025 plus cumulative crates.io. npm contributes 120,946,142 through 2026-11-15; crates.io contributes 2,321,390. This is an observed lower bound. Clones and release assets are excluded. [Full npm evidence](../data/snapshots/2026-11-16/npm-downloads.json).

## Integration review

Current manifests were observed; existing recipes retain dated execution evidence. No new dependency, install, learning gain or package release is claimed. Missing frozen evaluator and fallback evidence remain gates.

## Collection controls and integration evidence

Existing fixed-start npm evidence retains its original retrieval date. Covered-day revisions adjust that baseline once; only dates after 2026-11-15 contribute disjoint increments. Current bounded backfill progress is partial and recorded in the provider receipt; no completion promise is made. The legacy collector safety change remains in [PR 39](https://github.com/ruvnet/ruvnet/pull/39) for separate engineering review. [Integration evidence](../data/snapshots/2026-11-28/integration-health-receipt.json) records current capability, graph coverage and unresolved gates without claiming a new install, learning result or adoption.

The secondary mixed-provider milestone retains the original unrevised npm measurement of 120,946,142 events retrieved November 16 at 05:42 UTC. The canonical npm headline additionally reconciles covered-day revisions and disjoint later observations; it is an observed lower bound, not lifetime downloads.

Latest seven completed UTC dates (2026-11-21 through 2026-11-27): **1,148,701 observed npm events**, 461/3,010 eligible package-day observations. Full-window total and growth remain unknown. No short-horizon forecast is issued while comparable complete observations are missing.

The next pinned Darwin/RuFANN screening candidate remains unexecuted pending a frozen held-out evaluator and fallback. Current published Darwin 0.16.0 declares the exact ruv-fann 0.1.2 peer; the latest ruv-fann 0.3.0 is outside that range. No default dependency or release change is proposed. See [candidate review](../data/snapshots/2026-11-28/darwin-candidate-review.json).

Four published npm manifests and three distinct current source pilot manifests were inspected, with source and registry observations kept separate. The retained graph overlay and unobserved inventory IDs retain their explicit dates and coverage in the integration receipt. No new install, dependency edge, learning gain, external adoption or package release is claimed.

Source caches, tools and temporary files use the existing authorized data volume on the same host. No credential, host, provider or schedule changed; existing successful caches were reused.

## Checkpoint recovery

The original collector host, provider lease and existing cache checkpoints were verified. The November 9 through 11 cache reconciled to 1,287 existing ledger cells, with no backfill request for those dates. This frozen snapshot records only verified observations. The bounded npm worker may collect further responses independently; incomplete days remain unknown.
