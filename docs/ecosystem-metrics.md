# Ecosystem metrics

Verified November 11, 2026. Public repositories only. GitHub counts: 2026-11-11T14:04:41.724701+00:00.

| Metric | Count |
| --- | ---: |
| Public owned repositories | 234 |
| Original repositories | 207 |
| Public fork repositories | 27 |
| Stars across all owned repos | 202,802 |
| Stars across originals | 202,537 |
| Forks across all owned repos | 26,812 |
| Followers | 12,383 |
| Repository subscriptions | 1,814 |
| Published releases | 2,544 |
| Current release asset downloads | 117,801 |
| Retained observed release asset downloads | 117,804 |
| Rust crates | 498 |
| crates.io cumulative downloads | 2,207,985 |

## Repository cohorts

| Cohort | Public repositories | Stars | Forks | Subscribers | Open issues + PRs |
| --- | ---: | ---: | ---: | ---: | ---: |
| All owned | 234 | 202,802 | 26,812 | 1,814 | 2,452 |
| Nonfork | 207 | 202,537 | 26,732 | 1,811 | 2,445 |

## Activity: October 28 through November 10, UTC

| Metric | Count |
| --- | ---: |
| Issues opened | 210 |
| Issues closed | 533 |
| PRs opened | 827 |
| PRs merged | 618 |
| Releases published | 114 |
| Workflow runs | Unknown |

Workflow run counts are unknown. GitHub limits complete run enumeration to 1,000 results per query; this snapshot does not have complete workflow coverage.

## GitHub traffic

Across the complete 14-day UTC window, GitHub reported 726,847 clone events and 221,422 view events for 234 repositories. Unique cloners and visitors are retained per repository only and are not summed.

## Latest independently verified npm day

**1,297,163 npm download events on November 10, 2026 UTC**, across all **412 eligible packages**. The current inventory is **427**; **15** packages first published after the target UTC day ended are explicitly excluded. Verified through 2026-11-11T13:58:24.253010+00:00. These are events, including transitive installs and CI, not unique users. [Daily observation](../data/snapshots/2026-11-11/npm-daily-points.json).

The annual-range source remains dated November 9 through November 8. Its rolling, monthly and mixed-provider milestone figures below deliberately retain their own provenance and exclude this newer daily increment. November 9 remains unverified. The separate npm-only billion-goal lower bound is **115,187,731** observed events since October 1, 2025, with missing days disclosed in the running JSON.

## Retained npm annual-range evidence

Observed daily-event sum: 10,035,300 across recorded cells for October 28 through November 10 UTC. Coverage varies by day: November 10 is complete for 412 eligible packages; other dates retain incomplete historical range coverage. Exact comparable-window growth remains unknown. Twenty-two current inventory packages lack retained annual-range evidence; new point observations do not fill their historical cells. See the running JSON for per-day coverage.

## Coverage and gaps

All 234 public repositories were enumerated, including 27 forks and 0 archived repositories. Repository subscriptions and release pagination are complete. Open public issues and PRs are 1,241 and 1,209. Indexed search can differ from repository metadata because sources are not an atomic snapshot. Open issues and PR counts are separate search estimates; the cohort row reports GitHub's combined open_issues_count.

GitHub traffic was available through the owner-authorized ruOS interface. Across all repositories, clone events were 726,847 and view events were 221,422 from 2026-10-28 through 2026-11-10 UTC. Per-repository unique counts are retained in the dated snapshot; they are not summed across repositories. Commits and contributors were not refreshed.

## Running totals and verification

[Running totals](../data/ecosystem-running-totals.json), [daily npm ledger](../data/ecosystem-daily-ledger.json), and [release asset ledger](../data/release-asset-ledger.json) keep providers and metrics separate. Revised daily cells replace earlier observations; overlapping windows are never added. 8 release assets are absent from the complete current inventory; their last observed counts and deletion provenance are retained.

Validation passed: 39,124 unique daily keys, idempotent replay, total reconciliation, complete repository and release pagination, and explicit missing data. [Dated evidence](../data/snapshots/2026-11-11/).

## Progress toward 100 million

Observed combined registry downloads: 116,098,553; remaining: 0. Basis: npm since October 1, 2025 plus cumulative crates.io. npm contributes 113,890,568 through 2026-11-08; crates.io contributes 2,207,985. This is an observed lower bound. Clones and release assets are excluded. [Full npm evidence](../data/snapshots/2026-11-09/npm-downloads.json).

## Comparison coverage and integration review

The fixed 412-package 7-day, 30-day and preceding 30-day windows have incomplete historical coverage. Exact window totals and growth remain null; observed lower bounds and cell coverage are retained in the running summary. No causal claim is made for the constellation focus. No forecast is issued without three comparable complete weekdays.

The November 8 distribution baseline has 408 IDs; current inventory has 427, with 19 additions and no removals. Twenty targeted published manifests, including Darwin, were read; all other graph nodes retain their older observation dates. Declared source paths are not treated as verified source checkouts. No external adoption count is inferred from transitive installs.

Darwin 0.14.0 already documents optional RuFANN screening and declares exact peer ruv-fann 0.1.2. Current ruv-fann 0.3.0 does not satisfy that peer. Frozen candidate pins were preserved; no duplicate dependency or silent upgrade was added. This is a static compatibility finding, not a reproduced install failure. The candidate has no bound recipe, held-out evaluator, equal-budget or fallback receipt; no experiment, package install, engineering merge or release ran. [Manifest and candidate evidence](../data/snapshots/2026-11-11/npm-new-manifests.json).
