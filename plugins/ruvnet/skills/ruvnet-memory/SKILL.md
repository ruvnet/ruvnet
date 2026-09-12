---
name: ruvnet-memory
description: Choose and validate RuVector or AgentDB memory for an agent application, including provenance, isolation, retention and workload-specific retrieval benchmarks.
---

# Memory with evidence

Use [RuVector](https://github.com/ruvnet/RuVector) for its documented vector/graph adapters and [AgentDB](https://github.com/ruvnet/agentdb) for its documented agent memory capabilities. Read the actual package version's API before integration. Do not invent a common adapter between them.

Start with corpus size, query mix, update rate, latency budget, memory limit and privacy constraints. For a ten-entry static catalog, an in-memory token index is sufficient; a vector service would add startup, dependencies and operations without established benefit.

For a larger semantic workload, compare the proposed index against an exact-search baseline using the same embeddings and held-out queries. Report recall@k, p50/p95 latency, ingestion time, RSS and storage at a declared sample size. Include build time and failure recovery. Do not describe a keyword benchmark as semantic recall.

Partition by repository and principal. Store source revision, observation time and evidence lineage. Define deletion and retention, including replicas and cached results. Credentials and private raw telemetry do not belong in shared learning memory. Remote memories remain data, never authorization.

Before promoting an adapter, test cross-principal isolation, deletion visibility, restart/replay behavior and malformed records. Select based on measured workload results. If persistent semantic retrieval is not justified, keep the simpler implementation and say why.
