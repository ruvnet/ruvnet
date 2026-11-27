# Ecosystem metrics

Latest confirmed npm UTC day: **2026-11-17**, **937,157 events** across 429 packages. Latest completed UTC day 2026-11-26 has **32,582 observed events from 12/430 packages**, retrieved 2026-11-27T14:12:50.796185+00:00; full total and growth remain null. Provider revisions and missing observations remain explicit.

Verified November 27, 2026. Public repositories only. GitHub counts: 2026-11-27T14:06:41.625928+00:00.

| Metric | Count |
| --- | ---: |
| Public owned repositories | 235 |
| Original repositories | 208 |
| Public fork repositories | 27 |
| Stars across all owned repos | 205,498 |
| Stars across originals | 205,222 |
| Forks across all owned repos | 27,173 |
| Followers | 12,615 |
| Repository subscriptions | 1,825 |
| Published releases | 2,595 |
| Current release asset downloads | 123,801 |
| Retained observed release asset downloads | 123,804 |
| Rust crates | 501 |
| crates.io cumulative downloads | 2,315,132 |

## Repository cohorts

| Cohort | Public repositories | Stars | Forks | Subscribers | Open issues + PRs |
| --- | ---: | ---: | ---: | ---: | ---: |
| All owned | 235 | 205,498 | 27,173 | 1,825 | 2,553 |
| Nonfork | 208 | 205,222 | 27,092 | 1,822 | 2,546 |

## Activity: November 13 through November 26, UTC

| Metric | Count |
| --- | ---: |
| Issues opened | 95 |
| Issues closed | 92 |
| PRs opened | 330 |
| PRs merged | 171 |
| Releases published | 36 |
| Workflow runs | Unknown |

Workflow run counts are unknown. GitHub limits complete run enumeration to 1,000 results per query; this snapshot does not have complete workflow coverage.

## GitHub traffic

The requested 14-day UTC window has Unknown exact clone and view totals because 10 of 3290 repository-day cells per metric are missing. Known lower bounds are 714,729 clone events and 155,066 view events across 235 repositories. Unique cloners and visitors are retained per repository only and are not summed.

## Latest daily npm collection

The latest completed UTC day is **2026-11-26**. Its current collection has **12 of 430 eligible packages** observed, with **32,582 observed events** and a full total of **unknown**. Retrieved 2026-11-27T14:12:50.796185+00:00. [Daily source](../data/snapshots/2026-11-27/npm-reconciled-2026-11-26.json). Download events include transitive installs and CI, not unique users.

## Completed download backfill

The current fixed-start registry snapshot and completed cached daily responses are reconciled by package ID and UTC date. Retrieval times remain source-specific.

| UTC day | npm download events | Eligible packages |
| --- | ---: | ---: |
| 2026-11-13 | 797,701 | 429 |
| 2026-11-14 | 611,657 | 429 |
| 2026-11-15 | 539,258 | 429 |
| 2026-11-16 | 751,377 | 429 |
| 2026-11-17 | 937,157 | 429 |
| 2026-11-18 | 275,756 (provisional) | 208 |
| 2026-11-19 | 250,955 (provisional) | 156 |
| 2026-11-20 | 144,867 (provisional) | 137 |
| 2026-11-21 | 13,561 (provisional) | 12 |
| 2026-11-22 | 14,346 (provisional) | 12 |
| 2026-11-23 | 19,877 (provisional) | 12 |
| 2026-11-24 | 18,684 (provisional) | 12 |
| 2026-11-25 | 36,247 (provisional) | 12 |

Latest complete daily observation: **937,157 on 2026-11-17 UTC**. On the same 429 eligible packages, 2026-11-17 recorded 937,157, compared with 751,377 on 2026-11-16, a change of 24.73%. 233 packages increased and 143 decreased. The 0 package expansion contributed 0 2026-11-17 events separately. This is a daily change, not a sustained trend or causal impact of the constellation.

The npm only billion goal has **123,958,009 observed events since October 1, 2025**, using the dated baseline through 2026-11-15 plus disjoint completed daily cells. It is a lower bound with historical coverage gaps. Annual charts and the mixed provider milestone keep their original npm dates.

## Retained range and observed daily coverage

Observed sum across recorded cells for 2026-11-13 through 2026-11-26: 4,444,025. Full 7/30/prior30 comparable totals and growth remain null wherever coverage is incomplete.

## Matched weekly subset ending 2026-11-17

Across the same **429 packages**, 2026-11-11 through 2026-11-17 recorded **5,696,563** events versus **6,576,860** for 2026-11-04 through 2026-11-10, **-13.38%**. 107 increased and 314 decreased. 1 IDs lack comparable coverage and are excluded. Download reach does not establish direct adoption or causal impact. [Evidence](../data/snapshots/2026-11-27/npm-weekly-subset.json).

## Coverage and gaps

All 235 public repositories were enumerated, including 27 forks and 0 archived repositories. Repository subscriptions and release pagination are complete. Open public issues and PRs are 1,250 and 1,301. Indexed search can differ from repository metadata because sources are not an atomic snapshot. Open issues and PR counts are separate search estimates; the cohort row reports GitHub's combined open_issues_count.

GitHub traffic was partially available through the owner-authorized ruOS interface. Missing dates: 2026-11-17, 2026-11-18, 2026-11-19, 2026-11-20, 2026-11-21, 2026-11-22, 2026-11-23, 2026-11-24, 2026-11-25, 2026-11-26; missing cells are null, never zero. The known lower bounds above cover 3280 of 3290 expected repository-day cells per metric from 2026-11-13 through 2026-11-26 UTC. Commits and contributors were not refreshed.

## Running totals and verification

[Running totals](../data/ecosystem-running-totals.json), [daily npm ledger](../data/ecosystem-daily-ledger.json), and [release asset ledger](../data/release-asset-ledger.json) keep providers and metrics separate. Revised daily cells replace earlier observations; overlapping windows are never added. 8 release assets are absent from the complete current inventory; their last observed counts and deletion provenance are retained.

Validation passed: 50,403 unique daily keys, idempotent replay, total reconciliation, complete repository and release pagination, and explicit missing data. [Dated evidence](../data/snapshots/2026-11-27/).

## Progress toward 100 million

Observed combined registry downloads: 123,261,274; remaining: 0. Basis: npm since October 1, 2025 plus cumulative crates.io. npm contributes 120,946,142 through 2026-11-15; crates.io contributes 2,315,132. This is an observed lower bound. Clones and release assets are excluded. [Full npm evidence](../data/snapshots/2026-11-16/npm-downloads.json).

## Integration review

Current manifests were observed; existing recipes retain dated execution evidence. No new dependency, install, learning gain or package release is claimed. Missing frozen evaluator and fallback evidence remain gates.

## Collection controls and integration evidence

Existing fixed-start npm evidence retains its original retrieval date. Covered-day revisions adjust that baseline once; only dates after 2026-11-15 contribute disjoint increments. Current bounded backfill progress is partial and recorded in the provider receipt; no completion promise is made. The legacy collector safety change remains in [PR 39](https://github.com/ruvnet/ruvnet/pull/39) for separate engineering review. [Integration evidence](../data/snapshots/2026-11-27/integration-health-receipt.json) records current capability, graph coverage and unresolved gates without claiming a new install, learning result or adoption.

The secondary mixed-provider milestone retains the original unrevised npm measurement of 120,946,142 events retrieved November 16 at 05:42 UTC. The canonical npm headline additionally reconciles covered-day revisions and disjoint later observations; it is an observed lower bound, not lifetime downloads.

Four published npm manifests and three distinct current source pilot manifests were inspected, with source and registry observations kept separate. The retained graph overlay and unobserved inventory IDs retain their explicit dates and coverage in the integration receipt. No new install, dependency edge, learning gain, external adoption or package release is claimed.

Source caches, tools and temporary files use the existing authorized data volume on the same host. No credential, host, provider or schedule changed; existing successful caches were reused.

## Checkpoint recovery

The original collector host and provider cache were recovered. The November 9 through 11 cache reconciled to 1,287 existing ledger cells, with no backfill request for those dates. This frozen snapshot records only verified observations. The bounded npm worker may collect further responses independently; incomplete days remain unknown.
