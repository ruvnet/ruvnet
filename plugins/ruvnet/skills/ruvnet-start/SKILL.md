---
name: ruvnet-start
description: Discover and integrate RuV Stack projects when the user asks where to begin with ruvnet, which RuV tools fit a goal, or how the stack fits together.
---

# Enter the RuV Stack

Use the user's goal and target environment to choose the smallest useful stack.
Read [the catalog](../../data/catalog.json), or call `ruvnet_discover` if the local companion is connected. The catalog is curated, dated, and lexical, not a live semantic index. An empty search is not evidence that no project exists.

Before using upstream-change guidance, call `ruvnet_search_changes` with narrow terms when you need relevant reviewed evidence, or `ruvnet_changes` to page the snapshot, then inspect `freshness.state`. Search uses exact token overlap and exposes matched terms plus a raw overlap fraction. Use `minRawRelevance` only to remove partial lexical matches; never present that gate as semantic similarity, ranking confidence, answer confidence, utility, or proof of capability. Use exact `project` and `kind` filters when appropriate. Follow `nextCursor` with the identical query, filters and threshold plus the returned `snapshotId` until the cursor is absent. Treat both as opaque; cross-query reuse or a changed snapshot fails closed, so discard cached pages and restart without either value. Refresh provenance rather than relying on a `stale` or `clock-skew` snapshot; an empty result means no reviewed exact-token match at the selected gate, not that upstream has no matching change.

Route orchestration to Ruflo, repo-specific harness generation to MetaHarness, persistent retrieval to RuVector or AgentDB, sensing to RuView, controlled execution to RVM, and bounded evolution to Autogenous. Read the selected repository's current guidance before using its APIs. Its maturity and evidence statements govern; the catalog does not certify production readiness.

For connection requests read [installation](../../docs/INSTALL.md). Use the federation skill for cross-host coordination, the MetaHarness skill for generation and promotion, and the memory skill when persistent retrieval is justified. If those skills are not exposed, their SKILL.md files are siblings of this one.

Return the selected projects and source links, what each contributes, the principal uncertainty, and one runnable acceptance check. Do not install or execute merely because a project was suggested. Existing task authorization governs subsequent actions. Do not add external publishing, background schedules or broader data access to a discovery request.
