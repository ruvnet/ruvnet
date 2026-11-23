# Ecosystem metrics

Latest confirmed npm UTC day: **2026-11-17**, **937,157 events** across 429 packages. The latest day with partial evidence, November 20, has **100,811 observed events from 71 of 430 eligible packages**. The November 23 replay used npm responses retrieved through November 23 at 14:32:43 UTC. The full total and growth remain unknown. Provider revisions and missing observations remain explicit.

Verified November 21, 2026. Public repositories only. GitHub counts: 2026-11-21T19:16:39.798897+00:00.

| Metric | Count |
| --- | ---: |
| Public owned repositories | 235 |
| Original repositories | 208 |
| Public fork repositories | 27 |
| Stars across all owned repos | 204,553 |
| Stars across originals | 204,277 |
| Forks across all owned repos | 27,019 |
| Followers | 12,574 |
| Repository subscriptions | 1,816 |
| Published releases | 2,582 |
| Current release asset downloads | 122,103 |
| Retained observed release asset downloads | 122,106 |
| Rust crates | 501 |
| crates.io cumulative downloads | 2,288,278 |

## Repository cohorts

| Cohort | Public repositories | Stars | Forks | Subscribers | Open issues + PRs |
| --- | ---: | ---: | ---: | ---: | ---: |
| All owned | 235 | 204,553 | 27,019 | 1,816 | 2,480 |
| Nonfork | 208 | 204,277 | 26,938 | 1,813 | 2,473 |

## Activity: November 7 through November 20, UTC

| Metric | Count |
| --- | ---: |
| Issues opened | 113 |
| Issues closed | 137 |
| PRs opened | 639 |
| PRs merged | 494 |
| Releases published | 113 |
| Workflow runs | Unknown |

Workflow run counts are unknown. GitHub limits complete run enumeration to 1,000 results per query; this snapshot does not have complete workflow coverage.

## GitHub traffic

The requested 14-day UTC window has Unknown exact clone and view totals because 50 of 3290 repository-day cells per metric are missing. Known lower bounds are 859,237 clone events and 184,820 view events across 235 repositories. Unique cloners and visitors are retained per repository only and are not summed.

## Latest daily npm collection

For **November 20 UTC**, **71 of 430 eligible packages** account for at least **100,811 downloads**. The full total is unknown. [November 20 evidence](../data/snapshots/2026-11-23/npm-143243-utc/npm-reconciled-2026-11-20.json). November 21 and 22 have no observations in this published ledger. Download events include transitive installs and CI, not unique users.

## Daily npm backfill

The current fixed-start registry snapshot and completed cached daily responses are reconciled by package ID and UTC date. Retrieval times remain source-specific.

| UTC day | npm download events | Packages observed |
| --- | ---: | ---: |
| 2026-11-07 | 532,206 | 427 |
| 2026-11-08 | 534,993 | 427 |
| 2026-11-09 | 1,365,665 | 427 |
| 2026-11-10 | 1,297,163 | 428 |
| 2026-11-11 | 1,026,648 | 429 |
| 2026-11-12 | 1,032,765 | 429 |
| 2026-11-13 | 797,701 | 429 |
| 2026-11-14 | 611,657 | 429 |
| 2026-11-15 | 539,258 | 429 |
| 2026-11-16 | 751,377 | 429 |
| 2026-11-17 | 937,157 | 429 |
| 2026-11-18 | 223,627 (lower bound) | 142 of 430 |
| 2026-11-19 | 186,058 (lower bound) | 90 of 430 |
| 2026-11-20 | 100,811 (lower bound) | 71 of 430 |

Latest complete daily observation: **937,157 on 2026-11-17 UTC**. On the same 429 eligible packages, 2026-11-17 recorded 937,157, compared with 751,377 on 2026-11-16, a change of 24.73%. 233 packages increased and 143 decreased. The 0 package expansion contributed 0 2026-11-17 events separately. This is a daily change, not a sustained trend or causal impact of the constellation.

The npm only billion goal has **123,661,630 observed events since October 1, 2025**, using the dated baseline through 2026-11-15 plus disjoint completed daily cells. It is a lower bound with historical coverage gaps. Annual charts and the mixed provider milestone keep their original npm dates.

## Retained range and observed daily coverage

Observed sum across recorded cells for 2026-11-07 through 2026-11-20: 9,937,086. Full 7/30/prior30 comparable totals and growth remain null wherever coverage is incomplete.

## Matched weekly subset ending 2026-11-17

Across the same **429 packages**, 2026-11-11 through 2026-11-17 recorded **5,696,563** events versus **6,576,860** for 2026-11-04 through 2026-11-10, **-13.38%**. 107 increased and 314 decreased. 1 IDs lack comparable coverage and are excluded. Download reach does not establish direct adoption or causal impact. [Evidence](../data/snapshots/2026-11-21/npm-weekly-subset.json).

## Coverage and gaps

All 235 public repositories were enumerated, including 27 forks and 0 archived repositories. Repository subscriptions and release pagination are complete. Open public issues and PRs are 1,235 and 1,243. Indexed search can differ from repository metadata because sources are not an atomic snapshot. Open issues and PR counts are separate search estimates; the cohort row reports GitHub's combined open_issues_count.

GitHub traffic was partially available through the owner-authorized ruOS interface. Missing dates: 2026-11-17, 2026-11-18, 2026-11-19, 2026-11-20; missing cells are null, never zero. The known lower bounds above cover 3240 of 3290 expected repository-day cells per metric from 2026-11-07 through 2026-11-20 UTC. Commits and contributors were not refreshed.

## Running totals and verification

[Running totals](../data/ecosystem-running-totals.json), [daily npm ledger](../data/ecosystem-daily-ledger.json), and [release asset ledger](../data/release-asset-ledger.json) keep providers and metrics separate. Revised daily cells replace earlier observations; overlapping windows are never added. 8 release assets are absent from the complete current inventory; their last observed counts and deletion provenance are retained.

The [first November 23 replay](../data/snapshots/2026-11-23/npm-cache-replay/npm-backfill-replay.json) added 144 package and date records. The [second replay](../data/snapshots/2026-11-23/npm-143243-utc/npm-backfill-replay.json) added 42 more, bringing the ledger to 47,313 unique keys. Across both replays, 27 observations matched existing records and 305,573 downloads were newly documented. Replaying the same responses adds zero events. [November 21 evidence for other metrics](../data/snapshots/2026-11-21/).

## Progress toward 100 million

Observed combined registry downloads: 123,234,420; remaining: 0. Basis: npm since October 1, 2025 plus cumulative crates.io. npm contributes 120,946,142 through 2026-11-15; crates.io contributes 2,288,278. This is an observed lower bound. Clones and release assets are excluded. [Full npm evidence](../data/snapshots/2026-11-16/npm-downloads.json).

## Integration review

Current manifests were observed; existing recipes retain dated execution evidence. No new dependency, install, learning gain or package release is claimed. Missing frozen evaluator and fallback evidence remain gates.

## Collection controls and integration evidence

Existing fixed-start npm evidence retains its original retrieval date. Covered-day revisions adjust that baseline once; only dates after 2026-11-15 contribute disjoint increments. Current bounded backfill progress is partial and recorded in the provider receipt; no completion promise is made. The legacy collector safety change remains in [PR 39](https://github.com/ruvnet/ruvnet/pull/39) for separate engineering review. [Integration evidence](../data/snapshots/2026-11-21/integration-health-receipt.json) records current capability, graph coverage and unresolved gates without claiming a new install, learning result or adoption.

The secondary mixed-provider milestone retains the original unrevised npm measurement of 120,946,142 events retrieved November 16 at 05:42 UTC. The canonical npm headline additionally reconciles covered-day revisions and disjoint later observations; it is an observed lower bound, not lifetime downloads.

Four published npm manifests and three distinct current source pilot manifests were inspected, with source and registry observations kept separate. The retained graph overlay and unobserved inventory IDs retain their explicit dates and coverage in the integration receipt. No new install, dependency edge, learning gain, external adoption or package release is claimed.

Source caches, tools and temporary files use the existing authorized data volume on the same host. No credential, host, provider or schedule changed; existing successful caches were reused.

## Checkpoint recovery

The original collector host and provider cache were recovered. The November 9 through 11 cache reconciled to 1,287 existing ledger cells, with no backfill request for those dates. This frozen snapshot records only verified observations. The bounded npm worker may collect further responses independently; incomplete days remain unknown.
