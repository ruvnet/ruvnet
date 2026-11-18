# Ecosystem metrics

Latest confirmed npm UTC day: **2026-11-16**, **751,377 events** across 429 packages. Latest completed UTC day 2026-11-17 has **4 observed events from 3/429 packages**, retrieved 2026-11-18T13:44:19.364153+00:00; full total and growth remain null. Provider revisions and missing observations remain explicit.

Verified November 18, 2026. Public repositories only. GitHub counts: 2026-11-18T13:41:45.569465+00:00.

| Metric | Count |
| --- | ---: |
| Public owned repositories | 235 |
| Original repositories | 208 |
| Public fork repositories | 27 |
| Stars across all owned repos | 204,152 |
| Stars across originals | 203,876 |
| Forks across all owned repos | 26,985 |
| Followers | 12,526 |
| Repository subscriptions | 1,816 |
| Published releases | 2,569 |
| Current release asset downloads | 120,822 |
| Retained observed release asset downloads | 120,825 |
| Rust crates | 501 |
| crates.io cumulative downloads | 2,266,990 |

## Repository cohorts

| Cohort | Public repositories | Stars | Forks | Subscribers | Open issues + PRs |
| --- | ---: | ---: | ---: | ---: | ---: |
| All owned | 235 | 204,152 | 26,985 | 1,816 | 2,508 |
| Nonfork | 208 | 203,876 | 26,905 | 1,813 | 2,501 |

## Activity: November 4 through November 17, UTC

| Metric | Count |
| --- | ---: |
| Issues opened | 197 |
| Issues closed | 533 |
| PRs opened | 863 |
| PRs merged | 688 |
| Releases published | 121 |
| Workflow runs | Unknown |

Workflow run counts are unknown. GitHub limits complete run enumeration to 1,000 results per query; this snapshot does not have complete workflow coverage.

## GitHub traffic

The requested 14-day UTC window has Unknown exact clone and view totals because 2 of 3290 repository-day cells per metric are missing. Known lower bounds are 876,485 clone events and 199,846 view events across 235 repositories. Unique cloners and visitors are retained per repository only and are not summed.

## Latest daily npm collection

The latest completed UTC day is **2026-11-17**. Its current collection has **3 of 429 eligible packages** observed, with **4 observed events** and a full total of **unknown**. Retrieved 2026-11-18T13:44:19.364153+00:00. [Daily source](../data/snapshots/2026-11-18/npm-reconciled-2026-11-17.json). Download events include transitive installs and CI, not unique users.

## Completed download backfill

The current fixed-start registry snapshot and completed cached daily responses are reconciled by package ID and UTC date. Retrieval times remain source-specific.

| UTC day | npm download events | Eligible packages |
| --- | ---: | ---: |
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
| 2026-11-15 | 539,258 | 429 |
| 2026-11-16 | 751,377 | 429 |

Latest complete daily observation: **751,377 on 2026-11-16 UTC**. On the same 429 eligible packages, 2026-11-16 recorded 751,377, compared with 539,258 on 2026-11-15, a change of 39.34%. 281 packages increased and 126 decreased. The 0 package expansion contributed 0 2026-11-16 events separately. This is a daily change, not a sustained trend or causal impact of the constellation.

The npm only billion goal has **122,213,981 observed events since October 1, 2025**, using the dated baseline through 2026-11-15 plus disjoint completed daily cells. It is a lower bound with historical coverage gaps. Annual charts and the mixed provider milestone keep their original npm dates.

## Retained range and observed daily coverage

Observed sum across recorded cells for 2026-11-04 through 2026-11-17: 11,336,270. Full 7/30/prior30 comparable totals and growth remain null wherever coverage is incomplete.

## Matched weekly subset ending 2026-11-16

Across the same **427 packages**, 2026-11-10 through 2026-11-16 recorded **5,853,964** events versus **5,975,162** for 2026-11-03 through 2026-11-09, **-2.03%**. 146 increased and 273 decreased. 3 IDs lack comparable coverage and are excluded. Download reach does not establish direct adoption or causal impact. [Evidence](../data/snapshots/2026-11-18/npm-weekly-subset.json).

## Coverage and gaps

All 235 public repositories were enumerated, including 27 forks and 0 archived repositories. Repository subscriptions and release pagination are complete. Open public issues and PRs are 1,263 and 1,243. Indexed search can differ from repository metadata because sources are not an atomic snapshot. Open issues and PR counts are separate search estimates; the cohort row reports GitHub's combined open_issues_count.

GitHub traffic was partially available through the owner-authorized ruOS interface. Missing dates: 2026-11-17; missing cells are null, never zero. The known lower bounds above cover 3287 of 3290 expected repository-day cells per metric from 2026-11-04 through 2026-11-17 UTC. Commits and contributors were not refreshed.

## Running totals and verification

[Running totals](../data/ecosystem-running-totals.json), [daily npm ledger](../data/ecosystem-daily-ledger.json), and [release asset ledger](../data/release-asset-ledger.json) keep providers and metrics separate. Revised daily cells replace earlier observations; overlapping windows are never added. 8 release assets are absent from the complete current inventory; their last observed counts and deletion provenance are retained.

Validation passed: 45,174 unique daily keys, idempotent replay, total reconciliation, complete repository and release pagination, and explicit missing data. [Dated evidence](../data/snapshots/2026-11-18/).

## Progress toward 100 million

Observed combined registry downloads: 123,213,132; remaining: 0. Basis: npm since October 1, 2025 plus cumulative crates.io. npm contributes 120,946,142 through 2026-11-15; crates.io contributes 2,266,990. This is an observed lower bound. Clones and release assets are excluded. [Full npm evidence](../data/snapshots/2026-11-16/npm-downloads.json).

## Integration review

Current manifests were observed; existing recipes retain dated execution evidence. No new dependency, install, learning gain or package release is claimed. Missing frozen evaluator and fallback evidence remain gates.

## Collection controls and integration evidence

Existing fixed-start npm evidence retains its original retrieval date. Covered-day revisions adjust that baseline once; only dates after 2026-11-15 contribute disjoint increments. Current bounded backfill progress is partial and recorded in the provider receipt; no completion promise is made. The legacy collector safety change remains in [PR 39](https://github.com/ruvnet/ruvnet/pull/39) for separate engineering review. [Integration evidence](../data/snapshots/2026-11-18/integration-health-receipt.json) records current capability, graph coverage and unresolved gates without claiming a new install, learning result or adoption.

The secondary mixed-provider milestone retains the original unrevised npm measurement of 120,946,142 events retrieved November 16 at 05:42 UTC. The canonical npm headline additionally reconciles covered-day revisions and disjoint later observations; it is an observed lower bound, not lifetime downloads.

Four published npm manifests and three distinct current source pilot manifests were inspected, with source and registry observations kept separate. The retained graph overlay and unobserved inventory IDs retain their explicit dates and coverage in the integration receipt. No new install, dependency edge, learning gain, external adoption or package release is claimed.

Collection recovered from a transient full temporary root filesystem by using the existing healthy home volume on the same approved host. No credential, host, provider or schedule changed; existing successful caches were preserved.
