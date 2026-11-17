# Ecosystem metrics

Latest confirmed npm UTC day: **2026-11-14**, **611,657 events** across 429 packages. Latest completed UTC day 2026-11-16 has **49 observed events from 3/429 packages**, retrieved 2026-11-17T13:50:58.957030+00:00; full total and growth remain null. Provider revisions and missing observations remain explicit.

Verified November 17, 2026. Public repositories only. GitHub counts: 2026-11-17T13:48:45.457333+00:00.

| Metric | Count |
| --- | ---: |
| Public owned repositories | 234 |
| Original repositories | 207 |
| Public fork repositories | 27 |
| Stars across all owned repos | 203,992 |
| Stars across originals | 203,716 |
| Forks across all owned repos | 26,967 |
| Followers | 12,515 |
| Repository subscriptions | 1,813 |
| Published releases | 2,564 |
| Current release asset downloads | 120,644 |
| Retained observed release asset downloads | 120,647 |
| Rust crates | 501 |
| crates.io cumulative downloads | 2,262,136 |

## Repository cohorts

| Cohort | Public repositories | Stars | Forks | Subscribers | Open issues + PRs |
| --- | ---: | ---: | ---: | ---: | ---: |
| All owned | 234 | 203,992 | 26,967 | 1,813 | 2,524 |
| Nonfork | 207 | 203,716 | 26,887 | 1,810 | 2,517 |

## Activity: November 3 through November 16, UTC

| Metric | Count |
| --- | ---: |
| Issues opened | 200 |
| Issues closed | 519 |
| PRs opened | 863 |
| PRs merged | 673 |
| Releases published | 119 |
| Workflow runs | Unknown |

Workflow run counts are unknown. GitHub limits complete run enumeration to 1,000 results per query; this snapshot does not have complete workflow coverage.

## GitHub traffic

Across the complete 14-day UTC window, GitHub reported 851,971 clone events and 204,204 view events for 234 repositories. Unique cloners and visitors are retained per repository only and are not summed.

## Latest daily npm collection

The latest completed UTC day is **2026-11-16**. Its current collection has **3 of 429 eligible packages** observed, with **49 observed events** and a full total of **unknown**. Retrieved 2026-11-17T13:50:58.957030+00:00. [Daily source](../data/snapshots/2026-11-17/npm-reconciled-2026-11-16.json). Download events include transitive installs and CI, not unique users.

## Completed download backfill

The current fixed-start registry snapshot and completed cached daily responses are reconciled by package ID and UTC date. Retrieval times remain source-specific.

| UTC day | npm download events | Eligible packages |
| --- | ---: | ---: |
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
| 2026-11-15 | 22,811 (provisional) | 429 |

Latest complete daily observation: **611,657 on 2026-11-14 UTC**. On the same 429 eligible packages, 2026-11-14 recorded 611,657, compared with 797,701 on 2026-11-13, a change of -23.32%. 67 packages increased and 349 decreased. The 0 package expansion contributed 0 2026-11-14 events separately. This is a daily change, not a sustained trend or causal impact of the constellation.

The npm only billion goal has **120,946,202 observed events since October 1, 2025**, using the dated baseline through 2026-11-15 plus disjoint completed daily cells. It is a lower bound with historical coverage gaps. Annual charts and the mixed provider milestone keep their original npm dates.

## Retained range and observed daily coverage

Observed sum across recorded cells for 2026-11-03 through 2026-11-16: 10,763,956. Full 7/30/prior30 comparable totals and growth remain null wherever coverage is incomplete.

## Matched weekly subset ending 2026-11-14

Across the same **409 packages**, 2026-11-08 through 2026-11-14 recorded **6,396,155** events versus **5,874,942** for 2026-11-01 through 2026-11-07, **+8.87%**. 270 increased and 128 decreased. 20 IDs lack comparable coverage and are excluded. Download reach does not establish direct adoption or causal impact. [Evidence](../data/snapshots/2026-11-17/npm-weekly-subset.json).

## Coverage and gaps

All 234 public repositories were enumerated, including 27 forks and 0 archived repositories. Repository subscriptions and release pagination are complete. Open public issues and PRs are 1,270 and 1,252. Indexed search can differ from repository metadata because sources are not an atomic snapshot. Open issues and PR counts are separate search estimates; the cohort row reports GitHub's combined open_issues_count.

GitHub traffic was available through the owner-authorized ruOS interface. Across all repositories, clone events were 851,971 and view events were 204,204 from 2026-11-03 through 2026-11-16 UTC. Per-repository unique counts are retained in the dated snapshot; they are not summed across repositories. Commits and contributors were not refreshed.

## Running totals and verification

[Running totals](../data/ecosystem-running-totals.json), [daily npm ledger](../data/ecosystem-daily-ledger.json), and [release asset ledger](../data/release-asset-ledger.json) keep providers and metrics separate. Revised daily cells replace earlier observations; overlapping windows are never added. 8 release assets are absent from the complete current inventory; their last observed counts and deletion provenance are retained.

Validation passed: 44,249 unique daily keys, idempotent replay, total reconciliation, complete repository and release pagination, and explicit missing data. [Dated evidence](../data/snapshots/2026-11-17/).

## Progress toward 100 million

Observed combined registry downloads: 123,208,278; remaining: 0. Basis: npm since October 1, 2025 plus cumulative crates.io. npm contributes 120,946,142 through 2026-11-15; crates.io contributes 2,262,136. This is an observed lower bound. Clones and release assets are excluded. [Full npm evidence](../data/snapshots/2026-11-16/npm-downloads.json).

## Integration review

Current manifests were observed; existing recipes retain dated execution evidence. No new dependency, install, learning gain or package release is claimed. Missing frozen evaluator and fallback evidence remain gates.

## Collection controls and integration evidence

Existing fixed-start npm evidence retains its original retrieval date. Covered-day revisions adjust that baseline once; only dates after 2026-11-15 contribute disjoint increments. Current bounded backfill progress is partial and recorded in the provider receipt; no completion promise is made. The legacy collector safety change remains in [PR 39](https://github.com/ruvnet/ruvnet/pull/39) for separate engineering review. [Integration evidence](../data/snapshots/2026-11-17/integration-health-receipt.json) records current capability, graph coverage and unresolved gates without claiming a new install, learning result or adoption.

The secondary mixed-provider milestone retains the original unrevised npm measurement of 120,946,142 events retrieved November 16 at 05:42 UTC. The canonical npm headline additionally reconciles covered-day revisions and disjoint later observations; it is an observed lower bound, not lifetime downloads.

Six unique manifests were refreshed, including the three original pilots, at November 17 retrieval times. The retained November 10 graph overlay accounts for 410 of 429 package IDs; 19 nodes remain unobserved. No new install, dependency edge, learning gain, external adoption or package release is claimed.

The frozen npm revision batch ends at 2026-11-17T13:50:58Z and covers 3/429 packages for November 16 (49 events). The worker was separately observed collecting at 13:51:29 UTC with 4/429 covered and 425 remaining; that later checkpoint is not the canonical total. [Worker receipt](../data/snapshots/2026-11-17/npm-worker-outcome.json). November 16 UTC ran from November 15 at 7 pm through November 16 at 7 pm in Toronto.
