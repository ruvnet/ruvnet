# Ecosystem metrics

Verified November 12, 2026. Public repositories only. GitHub counts: 2026-11-12T13:45:39.404872+00:00.

| Metric | Count |
| --- | ---: |
| Public owned repositories | 234 |
| Original repositories | 207 |
| Public fork repositories | 27 |
| Stars across all owned repos | 203,015 |
| Stars across originals | 202,750 |
| Forks across all owned repos | 26,845 |
| Followers | 12,436 |
| Repository subscriptions | 1,808 |
| Published releases | 2,556 |
| Current release asset downloads | 118,658 |
| Retained observed release asset downloads | 118,661 |
| Rust crates | 500 |
| crates.io cumulative downloads | 2,226,548 |

## Repository cohorts

| Cohort | Public repositories | Stars | Forks | Subscribers | Open issues + PRs |
| --- | ---: | ---: | ---: | ---: | ---: |
| All owned | 234 | 203,015 | 26,845 | 1,808 | 2,429 |
| Nonfork | 207 | 202,750 | 26,765 | 1,805 | 2,422 |

## Activity: October 29 through November 11, UTC

| Metric | Count |
| --- | ---: |
| Issues opened | 220 |
| Issues closed | 536 |
| PRs opened | 904 |
| PRs merged | 695 |
| Releases published | 124 |
| Workflow runs | Unknown |

Workflow run counts are unknown. GitHub limits complete run enumeration to 1,000 results per query; this snapshot does not have complete workflow coverage.

## GitHub traffic

Across the complete 14-day UTC window, GitHub reported 746,596 clone events and 214,429 view events for 234 repositories. Unique cloners and visitors are retained per repository only and are not summed.

## Latest daily npm collection

**Unknown npm download events on November 11, 2026 UTC**, across **67 observed packages** of **429 eligible**. Current inventory: **429**; **0** postwindow publications excluded. Retrieved 2026-11-12T13:50:35.976365+00:00. Download events include transitive installs and CI, not unique users. [Daily observation](../data/snapshots/2026-11-12/npm-daily-points.json).

HTTP 429 rate limiting prevented a complete current total. Observed November 11 lower bound: **105,755 events**, covering 67 of 429 packages; 362 remain unobserved. No zero filling or full-cohort forecast. Last confirmed complete daily total: **1,297,163 on 2026-11-10 UTC**. Only 67 packages have observations across the three requested daily dates. This incomplete subset cannot establish ecosystem growth. No full portfolio comparison or causal impact is claimed.

The npm only billion goal has **115,438,537 observed events since October 1, 2025**, combining the dated fixed-start baseline with disjoint completed daily cells. Historical gaps remain. The annual-range charts and mixed-provider milestone retain their original npm dates.

## Retained range and observed daily coverage

Observed sum across recorded cells for 2026-10-29 through 2026-11-11: 9,576,191. Complete eligible coverage on the bounded daily dates is separate from incomplete historical range coverage. Full 7/30/prior30 comparable growth remains null.

## Coverage and gaps

All 234 public repositories were enumerated, including 27 forks and 0 archived repositories. Repository subscriptions and release pagination are complete. Open public issues and PRs are 1,246 and 1,181. Indexed search can differ from repository metadata because sources are not an atomic snapshot. Open issues and PR counts are separate search estimates; the cohort row reports GitHub's combined open_issues_count.

GitHub traffic was available through the owner-authorized ruOS interface. Across all repositories, clone events were 746,596 and view events were 214,429 from 2026-10-29 through 2026-11-11 UTC. Per-repository unique counts are retained in the dated snapshot; they are not summed across repositories. Commits and contributors were not refreshed.

## Running totals and verification

[Running totals](../data/ecosystem-running-totals.json), [daily npm ledger](../data/ecosystem-daily-ledger.json), and [release asset ledger](../data/release-asset-ledger.json) keep providers and metrics separate. Revised daily cells replace earlier observations; overlapping windows are never added. 8 release assets are absent from the complete current inventory; their last observed counts and deletion provenance are retained.

Validation passed: 39,659 unique daily keys, idempotent replay, total reconciliation, complete repository and release pagination, and explicit missing data. [Dated evidence](../data/snapshots/2026-11-12/).

## Progress toward 100 million

Observed combined registry downloads: 116,117,116; remaining: 0. Basis: npm since October 1, 2025 plus cumulative crates.io. npm contributes 113,890,568 through 2026-11-08; crates.io contributes 2,226,548. This is an observed lower bound. Clones and release assets are excluded. [Full npm evidence](../data/snapshots/2026-11-09/npm-downloads.json).

## Integration review

Four current published manifests were reviewed, including two newly discovered IDs, @metaharness/autogenous and @ruvector/e-means. Darwin 0.14.0 declares exact optional RuFANN peer 0.1.2, which does not accept ruv-fann 0.3.0. e-means 0.1.0 declares Darwin 0.13.0 or 0.13.1, which excludes 0.14.0. Existing equivalent optional paths are present. These are static compatibility findings; no installation failure, useful learning gain, dependency change or release is claimed. A frozen recipe, lockfile, held-out evaluator and equal-budget fallback evidence remain missing. Other manifest nodes retain prior observation dates. No new external adoption count was verified. [Manifest evidence](../data/snapshots/2026-11-12/npm-new-manifests.json).
