# ruvnet — account-wide repository lineage and public prior-art dossier

A dated, commit-anchored working record of repositories associated with the **[ruvnet](https://github.com/ruvnet)** GitHub user account. The June table is preserved as a historical snapshot; the July reconciliation distinguishes what remains public, what is an owned non-fork, and what is a fork. Two kinds of evidence are kept separate:

- **Repository lineage:** a root commit proves that the current repository history contains that commit and its self-asserted Git author date. It does not prove when GitHub first served the commit, when the repository became public, or when a later feature appeared. Repository `created_at`, release timestamps, registry publication records, feature commits, tests, and independent archives are stronger public-appearance evidence.
- **Claimed novelty (scoped candidate):** where a project appears to contain a first-of-its-kind combination or application, the claim is written as an explicit predicate with named prior art. A repository root is a lineage anchor, not by itself proof that every current feature existed at genesis.

Confidence reflects how defensible the scoped predicate is against the named prior art. Git author dates are self-asserted and may be imported from another repository. Four July additions demonstrate this directly: their earliest reachable roots predate creation of the standalone repository.

> Companion: [RuVector internal-systems prior-art dossier](https://gist.github.com/ruvnet/86d6968783ff1629e7481d9c92d0bed8) — a deeper, per-crate provenance record for the RuVector repo specifically.

> **Technical and legal scope:** This is a technical provenance record and non-exhaustive related-work review, not a patentability, inventorship, freedom-to-operate, or legal prior-art opinion. Items published after a claim cutoff are subsequent related work, not prior art against that cutoff.

## Account lineage at a glance

- **Historical June 13 index:** 247 repository rows derived from an authenticated account inventory that reported 296 entries. Because that source included non-public state, the 247-row table is preserved as a historical authenticated snapshot, not described as a current public or non-fork count.
- **Live July 11 account surface:** 197 public repositories, comprising 173 owned non-forks and 24 forks.
- **Cutoff delta (`created_at >= 2026-06-13T00:00:00Z`):** 20 public repositories created under the account, comprising 15 owned source repositories and 5 forks.
- **Live flagship adoption:** RuView 80.1k stars; ruflo 64.0k; RuVector 4.35k; MetaHarness 462, retrieved 2026-07-11 UTC. Rounded values are used because stars are volatile.
- Earliest AI-tooling wave: **March 2023** — the ChatGPT-plugin / early-agent era.
- The account's work clusters into: agentic orchestration and harnesses, vector, memory and neural systems, distributed, consensus and quantum systems, and security, sensing and signals.

### July 11, 2026 provenance delta

The table below adds the 15 owned source repositories created on or after the cutoff. Genesis is the earliest root commit reachable in the repository. Four split repositories preserve history that predates repository creation; that is useful provenance, but it must not be confused with the date the standalone repository became public.

| Repository | GitHub `created_at` | Earliest reachable root | Commit | Scope |
|---|---:|---:|---|---|
| [metaharness](https://github.com/ruvnet/metaharness) | 2026-06-13 | 2026-06-13 | [`bbc5ce50`](https://github.com/ruvnet/metaharness/commit/bbc5ce506198e97b84e5c5d8dd0ba4f63ee10f45) | Portable agent-harness generator, Darwin evolution, Flywheel promotion, signed lineage, nine host adapters |
| [rufield](https://github.com/ruvnet/rufield) | 2026-06-14 | 2026-06-14 | [`c6abe927`](https://github.com/ruvnet/rufield/commit/c6abe927461767baae3fdfd7eaec6bcb7b3095e3) | Multimodal Field Sensing schema and Rust reference stack; v0.1's real adapter is captured WiFi CSI replay, while other modalities are schema or synthetic |
| [ruv-drone](https://github.com/ruvnet/ruv-drone) | 2026-06-16 | 2026-05-30 | [`bc01b9b6`](https://github.com/ruvnet/ruv-drone/commit/bc01b9b62464008f75c41b70a6b682e3bf79b6fb) | Civilian cooperative UAV fleet coordination; history split from earlier work |
| [worldgraph](https://github.com/ruvnet/worldgraph) | 2026-06-16 | 2026-05-21 | [`c285e5cc`](https://github.com/ruvnet/worldgraph/commit/c285e5ccd6ffeff92b23e11e3340c97680e0f223) | Privacy-aware environmental digital twin; history split from earlier work |
| [ruvn](https://github.com/ruvnet/ruvn) | 2026-06-16 | 2026-06-16 | [`5e92fb37`](https://github.com/ruvnet/ruvn/commit/5e92fb37047c1be1575f3b774127c59a9ff28a6a) | Graded, cited, multi-host AI research harness |
| [rvdna](https://github.com/ruvnet/rvdna) | 2026-06-17 | 2026-02-11 | [`92b145f1`](https://github.com/ruvnet/rvdna/commit/92b145f1acb3566809d3d7ba2612f0e2e612510a) | Rust and WASM genomic analysis; history split from earlier work |
| [ruqu](https://github.com/ruvnet/ruqu) | 2026-06-17 | 2026-01-17 | [`6eb55720`](https://github.com/ruvnet/ruqu/commit/6eb55720b7f001f39c43c123560f6d47a321d6ef) | Rust and WASM quantum circuit toolkit; history split from earlier work |
| [PhotonLayer](https://github.com/ruvnet/PhotonLayer) | 2026-06-18 | 2026-06-18 | [`a31aae7e`](https://github.com/ruvnet/PhotonLayer/commit/a31aae7eeccea21a43eb9029def8cb11587c9083) | Pure-Rust software simulator for task-trained optics; fabricated-optic validation remains roadmap |
| [SonicChamber](https://github.com/ruvnet/SonicChamber) | 2026-06-22 | 2026-06-22 | [`911c68a0`](https://github.com/ruvnet/SonicChamber/commit/911c68a041c9f8d401f4bd35be7c59d32196529f) | Acoustic digital-human and ultrasound simulation workbench |
| [rupixel](https://github.com/ruvnet/rupixel) | 2026-06-25 | 2026-06-25 | [`01637f5d`](https://github.com/ruvnet/rupixel/commit/01637f5df91ed7e7d3864133e2edee55dddb4e4b) | Pixel-native visual retrieval on the RuVector ANN substrate |
| [helix](https://github.com/ruvnet/helix) | 2026-06-26 | 2026-06-25 | [`71cd815c`](https://github.com/ruvnet/helix/commit/71cd815c4fc7538a30976c7d88cbb374c4b1ffc4) | Local-first health research and personal decision support with evidence gating; not a medical device |
| [hackerone](https://github.com/ruvnet/hackerone) | 2026-06-27 | 2026-06-27 | [`73852a72`](https://github.com/ruvnet/hackerone/commit/73852a72655bae2b6586ddbb8f86c43a0cda0075) | Safety-contained vulnerability triage and researcher harness |
| [CVE-bench](https://github.com/ruvnet/CVE-bench) | 2026-06-27 | 2026-06-27 | [`53f7b5f0`](https://github.com/ruvnet/CVE-bench/commit/53f7b5f071c9383b618e8687aff6694a3bc3be55) | Reproduce-and-fix security benchmark with executable tests and cost Pareto reporting; current validated seed dataset n=5 |
| [agenticow](https://github.com/ruvnet/agenticow) | 2026-06-28 | 2026-06-28 | [`1588c4af`](https://github.com/ruvnet/agenticow/commit/1588c4af00afdd5e23c045e5415c2a0d7f683348) | Copy-on-write branching and rollback for embedded vector memory |
| [rvFACE](https://github.com/ruvnet/rvFACE) | 2026-07-02 | 2026-07-02 | [`48f46a50`](https://github.com/ruvnet/rvFACE/commit/48f46a507de30e02fce05c710ed9f170ea894936) | Rust and WASM face-recognition SDK; deployment requires explicit consent, retention limits, biometric governance, and fitness validation |

**Public forks created in the cutoff window:** [AgentBBS](https://github.com/ruvnet/AgentBBS), forked from `mpiorowski/late-sh`; [Repo-Explainer](https://github.com/ruvnet/Repo-Explainer), from `stuinfla/Repo-Explainer`; [retort](https://github.com/ruvnet/retort), from `adrianco/retort`; [experiments](https://github.com/ruvnet/experiments), from `SWE-bench/experiments`; and [unsorry](https://github.com/ruvnet/unsorry), from `agenticsnz/unsorry`. They are part of the account surface but excluded from original-work and genesis-claim counts.

### Newly assessed scoped candidate claims

These are working candidate claims at medium confidence, not declarations that the underlying primitives were invented here.

1. **MetaHarness:** first known public runnable open-source implementation matching the combined predicate of deterministic repository-to-harness generation, nine host targets, benchmark-gated mutation, signed lineage, and replayable promotion receipts. Prior art: AutoGen, CrewAI, LangGraph, DSPy optimizers, GEPA, and agent scaffold generators.
2. **AgenticOW:** first known public runnable embedded vector-memory implementation matching the combined predicate of Git-style copy-on-write branching, per-agent snapshots, diff, rollback, and merge without duplicating the base vector store. Prior art: Git object storage, MVCC, database snapshots, and vector-database collection aliases.
3. **RuField MFS:** first known public open specification matching the combined predicate of WiFi, radar, ultrasound, infrared, and quantum-sensor observations normalized into one privacy-aware, provenance-rich field-event model with a Rust reference stack. Current implementation qualifier: captured WiFi CSI replay is the real v0.1 adapter; other modalities are schema or synthetic. Earlier related work: OGC SensorThings, ROS messages, OpenTelemetry, and multimodal sensor-fusion schemas.
4. **CVE-bench:** first known public benchmark matching the combined predicate of public CVE reproduction, upstream regression tests extracted from public fix commits or linked fix PRs when present, patch execution, and a cost Pareto leaderboard for agentic repair. Current validation qualifier: seed dataset n=5. Earlier related work: CyberSecEval, SecBench, SWE-bench, and vulnerability-repair datasets.
5. **PhotonLayer:** first known public pure-Rust software simulator matching the combined predicate of a trainable phase mask, task-useful sensor-pixel compression, deterministic execution, and BLAKE3-bound receipts. Fabricated-optic validation is not yet claimed. Earlier related work: diffractive neural networks, learned optics, lensless imaging, and optical neural accelerators.

### Historical earliest root commits from the June inventory

This subsection preserves the June authenticated snapshot and may include repositories that are no longer public. A row is not a claim of current unauthenticated availability.

| Genesis date | Repo | Commit | First-line message |
|---|---|---|---|
| 2023-02-13 | [powerprompt](https://github.com/ruvnet/powerprompt) | [`b0e8dfa5`](https://github.com/ruvnet/powerprompt/commit/b0e8dfa5) | Initial commit |
| 2023-03-09 | [daa](https://github.com/ruvnet/daa) | [`30e53358`](https://github.com/ruvnet/daa/commit/30e53358) | Initial commit |
| 2023-03-15 | [openai_devops](https://github.com/ruvnet/openai_devops) | [`d9fafd7e`](https://github.com/ruvnet/openai_devops/commit/d9fafd7e) | Initial commit |
| 2023-03-18 | [promptlang](https://github.com/ruvnet/promptlang) | [`ee287e59`](https://github.com/ruvnet/promptlang/commit/ee287e59) | Initial commit |
| 2023-03-18 | [aiscreenplay](https://github.com/ruvnet/aiscreenplay) | [`35da55b6`](https://github.com/ruvnet/aiscreenplay/commit/35da55b6) | Initial commit |
| 2023-03-19 | [textclassifier](https://github.com/ruvnet/textclassifier) | [`487b6fc3`](https://github.com/ruvnet/textclassifier/commit/487b6fc3) | Initial commit |
| 2023-03-19 | [taxbot_prvt](https://github.com/ruvnet/taxbot_prvt) | [`02ca802a`](https://github.com/ruvnet/taxbot_prvt/commit/02ca802a) | Initial commit |
| 2023-03-20 | [vcbot](https://github.com/ruvnet/vcbot) | [`8d0eb88d`](https://github.com/ruvnet/vcbot/commit/8d0eb88d) | Initial commit |
| 2023-03-21 | [AiToml](https://github.com/ruvnet/AiToml) | [`e98be084`](https://github.com/ruvnet/AiToml/commit/e98be084) | Initial commit |
| 2023-03-21 | [Ai-Code-Generator-](https://github.com/ruvnet/Ai-Code-Generator-) | [`40acd006`](https://github.com/ruvnet/Ai-Code-Generator-/commit/40acd006) | Initial commit |
| 2023-03-22 | [retro-ai-ui](https://github.com/ruvnet/retro-ai-ui) | [`5869def8`](https://github.com/ruvnet/retro-ai-ui/commit/5869def8) | Initial commit |
| 2023-03-23 | [chatgpt_plugin_python](https://github.com/ruvnet/chatgpt_plugin_python) | [`331803bd`](https://github.com/ruvnet/chatgpt_plugin_python/commit/331803bd) | Initial commit |
| 2023-03-23 | [AP-Casper](https://github.com/ruvnet/AP-Casper) | [`48a38534`](https://github.com/ruvnet/AP-Casper/commit/48a38534) | Initial commit |
| 2023-03-24 | [ChatGPT-Trading-Bot-for-KuCoin](https://github.com/ruvnet/ChatGPT-Trading-Bot-for-KuCoin) | [`e651ee64`](https://github.com/ruvnet/ChatGPT-Trading-Bot-for-KuCoin/commit/e651ee64) | Initial commit |

*(Also present but predating the AI work: `airbot` 2016-06-09, `SVGart` 2016-12-19.)*

---

## Detailed provenance by cluster

Each entry: **genesis commit (proof)** · what it is · scoped first-of-kind claim (if any) · named external prior art · confidence.

Star counts in the detailed sections and complete table are preserved from the June 13 snapshot. Use the live flagship values above for current adoption.

### Agentic orchestration, harnesses & MCP

#### [ruflo](https://github.com/ruvnet/ruflo) — [`7c1f9402`](https://github.com/ruvnet/ruflo/commit/7c1f9402) · **2025-06-02**  ·  59272★
A meta-harness for Claude that deploys multi-agent swarms with adaptive memory, self-learning hooks, HNSW-indexed hybrid memory, and RAG, evolved from the claude-flow lineage.

- **Scoped claim (medium):** First open-source meta-harness purpose-built for Claude's native multi-agent API combining swarm topology selection, self-learning hooks, HNSW hybrid memory, and RAG in one package.
- **Prior art:** AutoGen (MS, 2023), CrewAI (2024), LangGraph (2024), Auto-GPT (2023), OpenAI Swarm (Dec 2024), Anthropic managed-agents API.

#### [agentic-flow](https://github.com/ruvnet/agentic-flow) — [`4db75395`](https://github.com/ruvnet/agentic-flow/commit/4db75395) · **2024-09-02**  ·  746★
A drop-in layer for Claude Code / Agent SDK that dynamically switches between lower-cost AI models based on task complexity.

- **Scoped claim (medium):** First open-source model-routing shim integrated into the Claude Code/Agent SDK extension point doing real-time complexity-based tier switching (WASM booster -> Haiku -> Sonnet/Opus) within a session.
- **Prior art:** RouteLLM (2024), Martian router, OpenRouter cost-routing, LiteLLM proxy.

#### [flow-nexus](https://github.com/ruvnet/flow-nexus) — [`c0e84960`](https://github.com/ruvnet/flow-nexus/commit/c0e84960) · **2025-08-25**  ·  94★
A competitive agentic platform built entirely on MCP for deploying swarms, distributed neural training, and coding challenges.

- **Scoped claim (low):** First full-stack competitive agentic platform implemented exclusively via the MCP tool layer rather than a proprietary API.
- **Prior art:** Contexta AI, AWS Serverless MCP, Azure AI Agent Service (MCP, May 2025), Replit, e2b, Kaggle.

#### [rUv-dev](https://github.com/ruvnet/rUv-dev) — [`a03620a7`](https://github.com/ruvnet/rUv-dev/commit/a03620a7) · **2024-04-04**  ·  426★
An AI-powered development toolset embodying the rUv approach, combining SPARC methodology with multi-model AI coding assistance.

- **Claim:** none distinguishable — established space.
- **Prior art:** Cursor, Copilot, Cline/Roo, Kiro (AWS), Devin, Aider.

#### [sparc](https://github.com/ruvnet/sparc) — [`a7ec7d5d`](https://github.com/ruvnet/sparc/commit/a7ec7d5d) · **2024-10-07**  ·  467★
A five-phase structured methodology for AI-assisted development (Specification, Pseudocode, Architecture, Refinement, Completion) with 17 specialized agent modes.

- **Scoped claim (medium):** First publicly documented named five-phase AI development methodology mapping each phase to a distinct specialized agent role, implemented as a runnable Claude Code mode set.
- **Earlier related work at cutoff:** Waterfall and iterative SDLCs, TDD, BDD.
- **Subsequent or cutoff-unverified related work:** BMAD Method, AWS AI-DLC, Kiro spec-driven development.

#### [sparc-ide](https://github.com/ruvnet/sparc-ide) — [`2d857126`](https://github.com/ruvnet/sparc-ide/commit/2d857126) · **2025-05-06**  ·  35★
A custom IDE built around the SPARC methodology, integrating AI agent modes into the editor.

- **Scoped claim (low):** First IDE whose core editing workflow is structured around the five SPARC phases rather than treating AI as a bolt-on.
- **Prior art:** Cursor, Windsurf, Copilot Workspace, Devin, Replit AI, Zed.

#### [code-mesh](https://github.com/ruvnet/code-mesh) — [`7c954f74`](https://github.com/ruvnet/code-mesh/commit/7c954f74) · **2025-07-16**  ·  37★
An agentic coding fabric connecting multiple AI coding agents into a collaborative mesh.

- **Claim:** none distinguishable — established space.
- **Prior art:** CrewAI, AutoGen, LangGraph, OpenAI Swarm, Copilot Workspace.

#### [agentic-devops](https://github.com/ruvnet/agentic-devops) — [`3fef505e`](https://github.com/ruvnet/agentic-devops/commit/3fef505e) · **2024-06-10**  ·  46★
An interactive CLI that automates DevOps tasks by orchestrating AI agents through a terminal interface across clouds.

- **Scoped claim (low):** First interactive CLI surfacing AI agent orchestration as the primary interface for end-to-end multi-cloud DevOps automation.
- **Prior art:** Pulumi AI, Warp AI, Dagger AI, k8sgpt, OpenInterpreter.

#### [dynamo-mcp](https://github.com/ruvnet/dynamo-mcp) — [`52cdbac7`](https://github.com/ruvnet/dynamo-mcp/commit/52cdbac7) · **2025-04-25**  ·  50★
A dynamic MCP registry exposing Cookiecutter project templates through MCP tools for runtime discovery and scaffolding.

- **Scoped claim (medium):** First MCP server acting as a live Cookiecutter template registry enabling agents to enumerate and instantiate templates over MCP at runtime.
- **Earlier related work at cutoff:** Cookiecutter (2013), static MCP-server cookiecutters (2024 to early 2025).
- **Subsequent related work:** DynamicMcp Ruby gem (August 2025).

#### [federated-mcp](https://github.com/ruvnet/federated-mcp) — [`3d7e4696`](https://github.com/ruvnet/federated-mcp/commit/3d7e4696) · **2024-11-26**  ·  64★
An MCP implementation adding a federation layer for multiple MCP servers to interoperate across network boundaries.

- **Scoped claim (medium):** First open-source reference implementation of a federated MCP topology (multi-server routing + lifecycle) on top of the official MCP spec.
- **Prior art:** Anthropic MCP spec (Nov 2024), OAuth/OIDC federation, ActivityPub, gRPC service mesh.

#### [AiToml](https://github.com/ruvnet/AiToml) — [`e98be084`](https://github.com/ruvnet/AiToml/commit/e98be084) · **2023-03-21**  ·  67★
A declarative TOML specification for AI-centric workflows: fine-tuning pipelines, feedback loops, prompt chains, ML components.

- **Scoped claim (medium):** First formal workflow specification using TOML designed for AI/ML pipeline primitives rather than general-purpose task orchestration.
- **Prior art:** Airflow DAGs, GitHub Actions YAML, Step Functions, DVC pipelines, W&B configs.

#### [agileagents](https://github.com/ruvnet/agileagents) — [`1bed97e0`](https://github.com/ruvnet/agileagents/commit/1bed97e0) · **2024-05-17**  ·  42★
An open-source framework for deploying intelligent agents as serverless containers to AWS, Azure, GCP.

- **Claim:** none distinguishable — established space.
- **Prior art:** Bedrock Agents, Azure AI Agent Service, Vertex AI Agents, HF Inference Endpoints.

#### [q-star](https://github.com/ruvnet/q-star) — [`113a9c69`](https://github.com/ruvnet/q-star/commit/113a9c69) · **2023-11-24**  ·  96★
A reinforcement-learning framework implementing a Q-learning variant for agent decision-making on top of Microsoft AutoGen.

- **Scoped claim (medium):** First open-source implementation combining Q-Star (tabular Q-learning variant) with AutoGen's multi-agent conversation primitives as the action-selection mechanism.
- **Prior art:** Q-learning (Watkins 1989), Agent Q (MCTS+RL, 2024), AutoGen (2023), ReAct (2022).

### Vector, memory, neural & retrieval

#### [RuVector](https://github.com/ruvnet/RuVector) — [`ea3e70aa`](https://github.com/ruvnet/RuVector/commit/ea3e70aa) · **2025-11-19**  ·  4240★
A Rust vector database combining HNSW ANN search with an online GNN layer (SONA) that restructures index topology in real time from query patterns and feedback.

- **Scoped claim (medium):** First open-source vector store where the HNSW graph topology is continuously reshaped at sub-millisecond latency by an embedded GNN trained on live retrieval-feedback, without a separate offline reindex.
- **Prior art:** FAISS (Meta, 2017, static); Qdrant/Milvus (manual reindex); DiskANN (offline construction).

#### [ruv-FANN](https://github.com/ruvnet/ruv-FANN) — [`ad7cce73`](https://github.com/ruvnet/ruv-FANN/commit/ad7cce73) · **2025-06-26**  ·  365★
A memory-safe idiomatic Rust rewrite of the classic FANN C library, preserving its API while eliminating unsafe memory operations.

- **Scoped claim (medium):** First feature-complete memory-safe Rust port of the FANN API (Nissen 2003) suitable as a drop-in replacement on embedded/WASM targets.
- **Prior art:** FANN (Nissen, 2003, C); fann-rs (thin FFI binding); burn/candle (different API surface).

#### [agentdb](https://github.com/ruvnet/agentdb) — [`8b3388b2`](https://github.com/ruvnet/agentdb/commit/8b3388b2) · **2026-05-06**  ·  66★
A vector memory store for agents that updates embedding weights and retrieval rankings from agent usage signals so retrieval improves with every interaction.

- **Scoped claim (medium):** First agent-native vector store treating every optimizer trial, reflexion, and LM response as a first-class training event continuously fine-tuning retrieval weights in-process.
- **Prior art:** MemGPT/Letta (paging, no online fine-tune); Mem0 (extraction); A-MEM (link evolution); HippoRAG (offline).

#### [VIVIAN](https://github.com/ruvnet/VIVIAN) — [`e8dc86d5`](https://github.com/ruvnet/VIVIAN/commit/e8dc86d5) · **2023-03-31**  ·  42★
A vector index infrastructure layer for autonomous networks providing virtual addressability and lifecycle management of indexes across distributed agents.

- **Claim:** none distinguishable — established space.
- **Prior art:** pgvector (single-node); Weaviate/Pinecone (managed); FAISS sharding.

#### [dspy.ts](https://github.com/ruvnet/dspy.ts) — [`68447191`](https://github.com/ruvnet/dspy.ts/commit/68447191) · **2025-02-22**  ·  259★
A TypeScript/browser port of Stanford DSPy with static types that persists optimizer trials and LM responses to an AgentDB vector store for cross-session learning.

- **Scoped claim (medium):** First TypeScript DSPy port that natively persists optimizer trajectories to a vector store for retrieval-augmented prompt bootstrapping across sessions.
- **Prior art:** DSPy (Stanford, 2023, arXiv:2310.03714); Ax (axllm.dev, TS port, no persistent trajectory store).

#### [SynthLang](https://github.com/ruvnet/SynthLang) — [`976b553d`](https://github.com/ruvnet/SynthLang/commit/976b553d) · **2025-01-05**  ·  260★
A symbolic meta-language for LLM prompts using logographic glyphs and mathematical notation to compress instructions 40-70% in token count while preserving intent.

- **Scoped claim (medium):** First prompt-compression scheme mapping natural-language instructions to a logography-inspired glyph vocabulary as the primary compression primitive, vs extractive pruning or soft-prompt embeddings.
- **Prior art:** LLMLingua/LLMLingua-2 (MS, 2023-24, extractive); LongLLMLingua; 500xCompressor (ACL 2025).

#### [FACT](https://github.com/ruvnet/FACT) — [`3e78593c`](https://github.com/ruvnet/FACT/commit/3e78593c) · **2025-05-23**  ·  179★
A retrieval pattern that replaces vector search by caching static prompt tokens in the LLM KV cache and routing live lookups through deterministic authenticated MCP tool calls, sub-100ms and auditable.

- **Scoped claim (medium):** First retrieval architecture eliminating the vector-search step by combining provider-side prompt-KV caching with MCP-brokered deterministic tool calls as the sole retrieval path.
- **Prior art:** RAGCache/TurboRAG (2024, still retrieval-gated); cache-augmented generation 'Don't Do RAG' (2024, no tool routing).

#### [nova](https://github.com/ruvnet/nova) — [`2881b757`](https://github.com/ruvnet/nova/commit/2881b757) · **2025-01-30**  ·  40★
A knowledge-distillation pipeline extracting domain-specific knowledge from large models into compact specialist models.

- **Claim:** none distinguishable — established space.
- **Prior art:** Hinton distillation (2015); LIMA (2023); phi series; Alpaca/Vicuna.

#### [SAFLA](https://github.com/ruvnet/SAFLA) — [`02e555ec`](https://github.com/ruvnet/SAFLA/commit/02e555ec) · **2025-05-31**  ·  154★
A Python framework for autonomous agents with a metacognitive feedback loop, layered memory (vector/episodic/semantic/working), a self-awareness engine, delta-based improvement scoring, and MCP orchestration.

- **Scoped claim (medium):** First open-source Python framework to formalize a delta-evaluation metric for per-cycle self-improvement within a metacognitive agent loop integrating hybrid memory and MCP orchestration.
- **Earlier related work at cutoff:** MAPE-K (IBM autonomic, 2003); MemGPT; AutoGen; CrewAI.
- **Subsequent related work:** MAPE-for-AI-agents (arXiv:2510.27051).

#### [neural-trader](https://github.com/ruvnet/neural-trader) — [`0c8d7fcc`](https://github.com/ruvnet/neural-trader/commit/0c8d7fcc) · **2025-06-20**  ·  14★
A neural-network trading system using time-series models for signal generation, backtesting, and portfolio risk management.

- **Claim:** none distinguishable — established space.
- **Prior art:** QuantLib; FinRL (2021); Stable Baselines; LSTM/Transformer trading literature.

#### [agentic-difusion](https://github.com/ruvnet/agentic-difusion) — [`9ed049f7`](https://github.com/ruvnet/agentic-difusion/commit/9ed049f7) · **2025-05-11**  ·  36★
A system applying diffusion denoising principles to iterative code refinement, where each diffusion step is a targeted code edit evaluated by an execution signal.

- **Scoped claim (low):** First application of a discrete-diffusion denoising schedule to agentic code refinement where each denoising step is an autonomous edit-execute-score agent turn rather than a neural forward pass.
- **Prior art:** Diffusion-LM (Li 2022); MDLM/SEDD (2024); AgentRefine (ICLR 2025).

#### [strawberry-phi](https://github.com/ruvnet/strawberry-phi) — [`60d64639`](https://github.com/ruvnet/strawberry-phi/commit/60d64639) · **2024-09-12**  ·  59★
A fine-tuning and chain-of-thought reasoning project on Microsoft's Phi small-model family, adding extended-thinking reasoning.

- **Claim:** none distinguishable — established space.
- **Earlier related work at cutoff:** Phi-1, Phi-2 and Phi-3 base models; OpenAI o1.
- **Subsequent or cutoff-unverified related work:** DeepSeek-R1 and Qwen thinking variants.

### Distributed systems, consensus & quantum

#### [QuDAG](https://github.com/ruvnet/QuDAG) — [`69f0c963`](https://github.com/ruvnet/QuDAG/commit/69f0c963) · **2025-06-16**  ·  180★
A DAG-based anonymous communication protocol that uses post-quantum cryptography (ML-KEM/Dilithium) instead of classical elliptic-curve or RSA primitives used by Tor and I2P.

- **Scoped claim (medium):** First open-source implementation combining a DAG routing topology with NIST-standardized post-quantum KEMs (ML-KEM/Dilithium) for anonymous message routing, as of mid-2025.
- **Earlier related work at cutoff:** Tor; I2P; Nym; arXiv:2405.06126 on theoretical quantum-secure anonymous networks.
- **Subsequent related work:** QADR, arXiv:2511.15272, on quantum-resistant anonymous data reporting.

#### [daa](https://github.com/ruvnet/daa) — [`30e53358`](https://github.com/ruvnet/daa/commit/30e53358) · **2023-03-09**  ·  238★
A framework for building self-managing applications that autonomously adapt their behavior and resource usage without human intervention.

- **Claim:** none distinguishable — established space.
- **Prior art:** Autonomic computing (IBM, 2001); self-healing systems (Kephart & Chess 2003); Kubernetes Operators; LangChain/AutoGen; Ray.

#### [Synaptic-Mesh](https://github.com/ruvnet/Synaptic-Mesh) — [`30463806`](https://github.com/ruvnet/Synaptic-Mesh/commit/30463806) · **2025-07-13**  ·  72★
A peer-to-peer mesh network where each node runs a local learning agent that continuously updates its model weights based on local experience and peer gossip.

- **Scoped claim (low):** First system branding each P2P mesh node as an individually-learning neural agent with gossip-based weight propagation, vs federated learning's centralized aggregator.
- **Prior art:** Federated learning (McMahan et al. 2017, FedAvg); Gossip learning (Ormandi et al. 2013); Agentic Neural Networks (arxiv 2506.09046); P2P NTK distributed gradient descent (arxiv 2409.15267); libp2p gossipsub.

#### [sublinear-time-solver](https://github.com/ruvnet/sublinear-time-solver) — [`316ec6d7`](https://github.com/ruvnet/sublinear-time-solver/commit/316ec6d7) · **2025-09-19**  ·  79★
A Rust and WASM library that solves asymmetric diagonally dominant linear systems in sublinear time using Neumann series expansion and local push random-walk algorithms, exposed via npm CLI.

- **Scoped claim (medium):** First WASM-packaged, browser/npm-runnable implementation of sublinear-time solvers for asymmetric (RDD/CDD) systems, extending beyond the symmetric SDD case of Spielman-Teng and KMP.
- **Prior art:** Spielman-Teng nearly-linear SDD solvers (2004+); Koutis-Miller-Peng (KMP); arxiv 2509.13891 (theoretical asymmetric sublinear solver, Sep 2025); SciPy sparse solvers.

#### [rvm](https://github.com/ruvnet/rvm) — [`f39c3adf`](https://github.com/ruvnet/rvm/commit/f39c3adf) · **2026-04-04**  ·  107★
A Rust virtual machine runtime designed as a secure, memory-safe execution host purpose-built for autonomous AI agents rather than general-purpose code.

- **Scoped claim (low):** First VM with an instruction set and isolation model designed specifically around agentic workloads (tool calls, long-horizon tasks, capability tokens) rather than adapting a general-purpose VM.
- **Earlier related work at cutoff:** Wasmtime and Wasmer agent sandboxes; Firecracker microVMs; E2B; WASI; USPTO patent 12547703.
- **Subsequent or cutoff-unverified related work:** Vercel Open Agents.

#### [midstream](https://github.com/ruvnet/midstream) — [`e8b8a87a`](https://github.com/ruvnet/midstream/commit/e8b8a87a) · **2025-01-06**  ·  119★
A platform that enables AI applications to act on partial streaming LLM responses before the full generation is complete, reducing end-to-end latency for agentic pipelines.

- **Scoped claim (low):** First platform-level abstraction for triggering downstream agent actions on in-flight LLM token streams rather than on completion events.
- **Prior art:** Anthropic/OpenAI streaming SSE; LMQL; SGLang early branching; Semantic Kernel streaming; speculative decoding.

#### [skygraph](https://github.com/ruvnet/skygraph) — [`685a2661`](https://github.com/ruvnet/skygraph/commit/685a2661) · **2026-06-10**  ·  12★
A Rust graph system for satellite orbital data, modeling satellite constellations as nodes and inter-satellite or ground-station links as edges for visibility, routing, or coverage analysis.

- **Claim:** none distinguishable — established space.
- **Prior art:** Ansys STK; Celestrak/orekit; NetworkX LEO routing research; Starlink inter-satellite laser links; Poliastro.

#### [RuLake](https://github.com/ruvnet/RuLake) — [`1d0cc353`](https://github.com/ruvnet/RuLake/commit/1d0cc353) · **2026-04-24**  ·  10★
A data lake implementation in Rust, providing columnar storage, partitioning, and query capabilities with Rust memory-safety and performance.

- **Claim:** none distinguishable — established space.
- **Prior art:** Apache Iceberg; Delta Lake; Apache Hudi; DataFusion; Lance; Polars; object_store crate.

#### [quantum-magnetic-navigation](https://github.com/ruvnet/quantum-magnetic-navigation) — [`4872989a`](https://github.com/ruvnet/quantum-magnetic-navigation/commit/4872989a) · **2025-04-18**  ·  41★
A navigation system using quantum magnetometers to match real-time magnetic field readings against preloaded magnetic anomaly maps, enabling GPS-level positioning indoors, underwater, and in jammed environments.

- **Scoped claim (medium):** First open-source, software-complete implementation combining quantum-magnetometer sensor drivers, magnetic anomaly map matching, and a full navigation pipeline for robotics/transport.
- **Earlier related work at cutoff:** Lockheed Martin Dark Ice; Fraunhofer IAF NV-diamond magnetometer; NOAA World Magnetic Model; naval SQUID navigation; cold-atom IMUs from AOSense and Muquans.
- **Subsequent related work:** arXiv:2512.11300.

#### [Agent-Name-Service](https://github.com/ruvnet/Agent-Name-Service) — [`b5c30372`](https://github.com/ruvnet/Agent-Name-Service/commit/b5c30372) · **2025-05-15**  ·  74★
An implementation of the OWASP GenAI Security Project's ANS protocol, a DNS-inspired registry for secure discovery and capability-aware resolution of AI agents using PKI and zero-knowledge proofs.

- **Claim:** none distinguishable — established space.
- **Earlier related work at cutoff:** DNS; OWASP ANS v1.0; codegrande/agent-name-service; W3C DID; MCP.
- **Subsequent related work:** ACNBP, arXiv:2506.13590.

#### [optimizer](https://github.com/ruvnet/optimizer) — [`9ec50785`](https://github.com/ruvnet/optimizer/commit/9ec50785) · **2026-01-24**  ·  1★
A Rust optimizer library implementing mathematical or combinatorial optimization algorithms with performance-oriented Rust idioms.

- **Claim:** none distinguishable — established space.
- **Prior art:** OSQP; HiGHS; argmin crate; nalgebra/faer; or-tools.

### Security, sensing & signals

#### [RuView](https://github.com/ruvnet/RuView) — [`6cab2309`](https://github.com/ruvnet/RuView/commit/6cab2309) · **2025-06-07**  ·  73599★
Turns commodity WiFi CSI signals into real-time camera-free spatial intelligence: pose estimation, vital-sign monitoring, presence detection.

- **Scoped claim (medium):** First open-source system combining real-time CSI-based DensePose with simultaneous vital-sign (breathing/heartbeat) extraction and presence detection in one deployable commodity-hardware pipeline; the CMU 2023 paper established the model but shipped no integrated real-time appliance.
- **Prior art:** DensePose From WiFi (CMU, arXiv:2301.00250, 2023); WiDar 3.0 (IEEE ToMC 2021); FallDeFi (SenSys 2018).

#### [agentic-security](https://github.com/ruvnet/agentic-security) — [`693a4b04`](https://github.com/ruvnet/agentic-security/commit/693a4b04) · **2024-11-02**  ·  46★
An open-source agentic LLM vulnerability scanner and red-teaming toolkit that fuzzes agent workflows for jailbreaks, prompt injection, and multimodal attacks.

- **Scoped claim (medium):** First open-source toolkit targeting agentic workflow security (multi-step agent pipelines) rather than single-turn LLM outputs.
- **Earlier related work at cutoff:** Perez et al. 2022 automated red teaming; MART; Garak; Microsoft PyRIT.
- **Subsequent or cutoff-unverified related work:** Agent Security Bench; RedTeamLLM, arXiv:2505.06913.

#### [ultrasonic](https://github.com/ruvnet/ultrasonic) — [`bfe93c56`](https://github.com/ruvnet/ultrasonic/commit/bfe93c56) · **2025-06-09**  ·  90★
A steganography framework that embeds/extracts encrypted agentic AI commands in audio/video using ultrasonic frequencies (18-20 kHz) as a covert channel.

- **Scoped claim (medium):** First framework designed to encode structured, encrypted AI agent commands (not arbitrary binary) into ultrasonic frequencies of media, targeting AI-pipeline covert orchestration as the use-case.
- **Prior art:** Echo hiding (Bender 1996); SilverPush ultrasonic beacons (2014); LSB/DWT audio steganography; USPTO 7231271/7555432.

#### [cognitum](https://github.com/ruvnet/cognitum) — [`52b25167`](https://github.com/ruvnet/cognitum/commit/52b25167) · **2025-11-23**  ·  1★
A Verilog-described edge AI seed device for on-chip neural inference, targeting ultra-low-power/FPGA-class deployment.

- **Claim:** none distinguishable — established space.
- **Prior art:** FPGA DNN accelerators in Verilog; QAT NN layers for FPGA edge AI (MDPI 2023); Edge TPU; hls4ml.

#### [rvcsi](https://github.com/ruvnet/rvcsi) — [`acd5689d`](https://github.com/ruvnet/rvcsi/commit/acd5689d) · **2026-05-13**  ·  10★
A RuVector-integrated channel-state-information sensing library providing CSI capture, processing, and vectorized feature extraction for ML inference.

- **Scoped claim (low):** First library co-locating CSI feature extraction with a vector database (HNSW-indexed RuVector) for semantic nearest-neighbor retrieval over CSI patterns; prior CSI toolkits provide raw capture only.
- **Prior art:** Nexmon CSI (WOOT 2019); ESP32 CSI Toolkit (arXiv:2104.14342); PicoScenes (IEEE TNET 2022); Intel 5300 CSI Tool.

#### [Project-Sentinel](https://github.com/ruvnet/Project-Sentinel) — [`fe7bcfba`](https://github.com/ruvnet/Project-Sentinel/commit/fe7bcfba) · **2026-04-22**  ·  0★
An autonomous security and monitoring system performing continuous threat detection or anomaly alerting across a perimeter or infrastructure.

- **Claim:** none distinguishable — established space.
- **Prior art:** Wazuh; OSSEC; Suricata; Falco; AWS GuardDuty; Darktrace.

#### [auto-browser](https://github.com/ruvnet/auto-browser) — [`e14619c0`](https://github.com/ruvnet/auto-browser/commit/e14619c0) · **2025-01-20**  ·  94★
A CLI tool for configurable web automation using AI assistance to generate and apply reusable browser interaction templates.

- **Scoped claim (medium):** First CLI-native tool combining NL-described browser tasks with persistent, AI-generated, version-controllable reusable session templates; Stagehand/Skyvern are SDK/service-oriented.
- **Prior art:** Stagehand (Browserbase, 2024); Skyvern; Playwright MCP server (2024); Selenium/Playwright.

#### [guardrail](https://github.com/ruvnet/guardrail) — [`d8ac7d8d`](https://github.com/ruvnet/guardrail/commit/d8ac7d8d) · **2023-12-03**  ·  152★
A data-analysis and AI content-generation tool with sentiment analysis and safety filtering backed by OpenAI GPT.

- **Claim:** none distinguishable — established space.
- **Prior art:** Guardrails AI (Rajpal 2023); NeMo Guardrails (2023); Llama Guard (2023); Perspective API; OpenAI Moderation.

#### [rudevolution](https://github.com/ruvnet/rudevolution) — [`afde93e8`](https://github.com/ruvnet/rudevolution/commit/afde93e8) · **2026-04-03**  ·  101★
An AI decompiler that semantically recovers original variable/function names from binaries and claims to prove correctness of the recovered semantics.

- **Scoped claim (medium):** First decompiler combining semantic LLM name recovery with a formal correctness-proof layer; DIRTY recovers names/types but does not verify semantic equivalence, DeGPT optimises output without a proof step.
- **Prior art:** DIRE (2019); DIRTY (USENIX Security 2022); DeGPT (NDSS 2024); VarBERT (S&P 2024); Ghidra; Hex-Rays.

#### [promptlang](https://github.com/ruvnet/promptlang) — [`ee287e59`](https://github.com/ruvnet/promptlang/commit/ee287e59) · **2023-03-18**  ·  132★
A programming language treating prompts as first-class constructs for composing and controlling AI interactions.

- **Scoped claim (medium):** First prompt-oriented language exposing imperative control flow, typed variables, and composable prompt modules as a standalone parseable language (not embedded in Python).
- **Prior art:** LMQL (PLDI 2023, Python-embedded); Guidance (MS 2023, decorators); SGLang (2023); IBM PDL.

#### [symbolic-scribe](https://github.com/ruvnet/symbolic-scribe) — [`dd03d857`](https://github.com/ruvnet/symbolic-scribe/commit/dd03d857) · **2024-11-27**  ·  84★
A tooling layer for symbolic reasoning and mathematical prompt construction bridging LLM reasoning with formal/CAS verification.

- **Scoped claim (low):** First developer-facing toolkit wrapping CAS integration as a reusable prompt-construction library for LLM math pipelines, separating symbolic formalization from generation as a composable module.
- **Prior art:** PAL (Gao 2022); Program-of-Thought (2023); SymCode (2024); Wolfram Alpha LLM plugin; Lean/Coq+LLM.

---

## Scoped global-first claims — shortlist

Working scoped candidate claims at medium confidence, ordered by lineage date. The root commit links identify project lineage only. Each candidate still requires a feature-level commit, evidence path or executable test, release or registry timestamp, and an explicit prior-art cutoff before it should be presented as a concluded first.

| Date | Project | Scoped claim | Conf. |
|---|---|---|---|
| 2023-03-18 | [promptlang](https://github.com/ruvnet/promptlang) [`ee287e59`](https://github.com/ruvnet/promptlang/commit/ee287e59) | First known standalone parseable prompt-oriented language combining imperative control flow, typed variables, and composable prompt modules. | medium |
| 2023-03-21 | [AiToml](https://github.com/ruvnet/AiToml) [`e98be084`](https://github.com/ruvnet/AiToml/commit/e98be084) | First known formal TOML workflow specification designed specifically for AI and ML pipeline primitives rather than general task orchestration. | medium |
| 2023-11-24 | [q-star](https://github.com/ruvnet/q-star) [`113a9c69`](https://github.com/ruvnet/q-star/commit/113a9c69) | First known open-source implementation combining a Q-Star tabular Q-learning variant with AutoGen multi-agent conversations as the action-selection mechanism. | medium |
| 2024-09-02 | [agentic-flow](https://github.com/ruvnet/agentic-flow) [`4db75395`](https://github.com/ruvnet/agentic-flow/commit/4db75395) | First known open-source model-routing shim integrated with Claude Code or Agent SDK extension points for in-session complexity-based tier switching. | medium |
| 2024-10-07 | [sparc](https://github.com/ruvnet/sparc) [`a7ec7d5d`](https://github.com/ruvnet/sparc/commit/a7ec7d5d) | First known named five-phase AI development methodology mapping every phase to a distinct specialized agent role in a runnable mode set. | medium |
| 2024-11-02 | [agentic-security](https://github.com/ruvnet/agentic-security) [`693a4b04`](https://github.com/ruvnet/agentic-security/commit/693a4b04) | First open-source toolkit targeting agentic workflow security (multi-step agent pipelines) rather than single-turn LLM outputs. | medium |
| 2024-11-26 | [federated-mcp](https://github.com/ruvnet/federated-mcp) [`3d7e4696`](https://github.com/ruvnet/federated-mcp/commit/3d7e4696) | First known open-source reference implementation of federated MCP with multi-server routing and lifecycle management over the official protocol. | medium |
| 2025-01-05 | [SynthLang](https://github.com/ruvnet/SynthLang) [`976b553d`](https://github.com/ruvnet/SynthLang/commit/976b553d) | First known prompt-compression scheme using a logography-inspired glyph vocabulary as the primary compression primitive. | medium |
| 2025-01-20 | [auto-browser](https://github.com/ruvnet/auto-browser) [`e14619c0`](https://github.com/ruvnet/auto-browser/commit/e14619c0) | First known CLI-native browser tool combining natural-language tasks with persistent, AI-generated, version-controlled reusable session templates. | medium |
| 2025-02-22 | [dspy.ts](https://github.com/ruvnet/dspy.ts) [`68447191`](https://github.com/ruvnet/dspy.ts/commit/68447191) | First known TypeScript DSPy port that persists optimizer trajectories to a vector store for cross-session retrieval-augmented prompt bootstrapping. | medium |
| 2025-04-18 | [quantum-magnetic-navigation](https://github.com/ruvnet/quantum-magnetic-navigation) [`4872989a`](https://github.com/ruvnet/quantum-magnetic-navigation/commit/4872989a) | First known open-source software-complete stack combining quantum-magnetometer drivers, magnetic-anomaly map matching, and a navigation pipeline. | medium |
| 2025-04-25 | [dynamo-mcp](https://github.com/ruvnet/dynamo-mcp) [`52cdbac7`](https://github.com/ruvnet/dynamo-mcp/commit/52cdbac7) | First known MCP server acting as a live Cookiecutter registry that lets agents enumerate and instantiate templates at runtime. | medium |
| 2025-05-23 | [FACT](https://github.com/ruvnet/FACT) [`3e78593c`](https://github.com/ruvnet/FACT/commit/3e78593c) | First known retrieval architecture eliminating vector search by combining provider-side prompt-KV caching with deterministic authenticated MCP tool calls. | medium |
| 2025-05-31 | [SAFLA](https://github.com/ruvnet/SAFLA) [`02e555ec`](https://github.com/ruvnet/SAFLA/commit/02e555ec) | First known open-source Python framework formalizing a per-cycle delta-evaluation metric inside a metacognitive loop with hybrid memory and MCP. | medium |
| 2025-06-02 | [ruflo](https://github.com/ruvnet/ruflo) [`7c1f9402`](https://github.com/ruvnet/ruflo/commit/7c1f9402) | First known open-source Claude-oriented meta-harness combining swarm topology selection, self-learning hooks, HNSW hybrid memory, and RAG in one package. | medium |
| 2025-06-07 | [RuView](https://github.com/ruvnet/RuView) [`6cab2309`](https://github.com/ruvnet/RuView/commit/6cab2309) | First known open-source deployable commodity-hardware pipeline combining real-time CSI pose estimation, vital-sign extraction, and presence detection. | medium |
| 2025-06-09 | [ultrasonic](https://github.com/ruvnet/ultrasonic) [`bfe93c56`](https://github.com/ruvnet/ultrasonic/commit/bfe93c56) | First known framework designed to encode structured encrypted AI-agent commands, rather than arbitrary binary, into ultrasonic media channels. | medium |
| 2025-06-16 | [QuDAG](https://github.com/ruvnet/QuDAG) [`69f0c963`](https://github.com/ruvnet/QuDAG/commit/69f0c963) | First known open-source implementation combining DAG routing with NIST-standardized post-quantum KEMs for anonymous message routing. | medium |
| 2025-06-26 | [ruv-FANN](https://github.com/ruvnet/ruv-FANN) [`ad7cce73`](https://github.com/ruvnet/ruv-FANN/commit/ad7cce73) | First known feature-complete memory-safe Rust port of the FANN API suitable for embedded and WASM targets. | medium |
| 2025-09-19 | [sublinear-time-solver](https://github.com/ruvnet/sublinear-time-solver) [`316ec6d7`](https://github.com/ruvnet/sublinear-time-solver/commit/316ec6d7) | First known WASM-packaged browser and npm implementation of sublinear-time solvers for asymmetric RDD and CDD systems. | medium |
| 2025-11-19 | [RuVector](https://github.com/ruvnet/RuVector) [`ea3e70aa`](https://github.com/ruvnet/RuVector/commit/ea3e70aa) | First known open-source vector store whose embedded GNN continuously reshapes HNSW topology from live retrieval feedback without separate offline reindexing. | medium |
| 2026-04-03 | [rudevolution](https://github.com/ruvnet/rudevolution) [`afde93e8`](https://github.com/ruvnet/rudevolution/commit/afde93e8) | First decompiler combining semantic LLM name recovery with a formal correctness-proof layer | medium |
| 2026-05-06 | [agentdb](https://github.com/ruvnet/agentdb) [`8b3388b2`](https://github.com/ruvnet/agentdb/commit/8b3388b2) | First known agent-native vector store treating optimizer trials, reflexions, and model responses as first-class in-process retrieval-training events. | medium |

---

## Historical June 13 repository-lineage table

This table preserves 247 rows visible to the authenticated inventory process on June 13. It is not the current public inventory: 94 rows are no longer public non-forks, and some links may now require authorization or fail. As of July 11, the account exposes 197 public repositories, including 173 non-forks; excluding 6 empty non-forks leaves 167 public non-forks with commit history. A future full regeneration should replace this historical table with those 167 unauthenticatedly verifiable rows.

| Date | Repo | Genesis commit | Stars | First-line message |
|---|---|---|---|---|
| 2016-06-09 | [airbot](https://github.com/ruvnet/airbot) | [`86e450a8`](https://github.com/ruvnet/airbot/commit/86e450a8) | 0 | init commit - airbot based on keystonejs |
| 2016-12-19 | [SVGart](https://github.com/ruvnet/SVGart) | [`51f99346`](https://github.com/ruvnet/SVGart/commit/51f99346) | 8 | Initial commit |
| 2023-02-13 | [powerprompt](https://github.com/ruvnet/powerprompt) | [`b0e8dfa5`](https://github.com/ruvnet/powerprompt/commit/b0e8dfa5) | 19 | Initial commit |
| 2023-03-09 | [daa](https://github.com/ruvnet/daa) | [`30e53358`](https://github.com/ruvnet/daa/commit/30e53358) | 238 | Initial commit |
| 2023-03-15 | [openai_devops](https://github.com/ruvnet/openai_devops) | [`d9fafd7e`](https://github.com/ruvnet/openai_devops/commit/d9fafd7e) | 70 | Initial commit |
| 2023-03-18 | [promptlang](https://github.com/ruvnet/promptlang) | [`ee287e59`](https://github.com/ruvnet/promptlang/commit/ee287e59) | 132 | Initial commit |
| 2023-03-18 | [aiscreenplay](https://github.com/ruvnet/aiscreenplay) | [`35da55b6`](https://github.com/ruvnet/aiscreenplay/commit/35da55b6) | 16 | Initial commit |
| 2023-03-19 | [textclassifier](https://github.com/ruvnet/textclassifier) | [`487b6fc3`](https://github.com/ruvnet/textclassifier/commit/487b6fc3) | 19 | Initial commit |
| 2023-03-19 | [taxbot_prvt](https://github.com/ruvnet/taxbot_prvt) | [`02ca802a`](https://github.com/ruvnet/taxbot_prvt/commit/02ca802a) | 1 | Initial commit |
| 2023-03-20 | [vcbot](https://github.com/ruvnet/vcbot) | [`8d0eb88d`](https://github.com/ruvnet/vcbot/commit/8d0eb88d) | 21 | Initial commit |
| 2023-03-21 | [AiToml](https://github.com/ruvnet/AiToml) | [`e98be084`](https://github.com/ruvnet/AiToml/commit/e98be084) | 67 | Initial commit |
| 2023-03-21 | [Ai-Code-Generator-](https://github.com/ruvnet/Ai-Code-Generator-) | [`40acd006`](https://github.com/ruvnet/Ai-Code-Generator-/commit/40acd006) | 12 | Initial commit |
| 2023-03-22 | [retro-ai-ui](https://github.com/ruvnet/retro-ai-ui) | [`5869def8`](https://github.com/ruvnet/retro-ai-ui/commit/5869def8) | 15 | Initial commit |
| 2023-03-23 | [chatgpt_plugin_python](https://github.com/ruvnet/chatgpt_plugin_python) | [`331803bd`](https://github.com/ruvnet/chatgpt_plugin_python/commit/331803bd) | 96 | Initial commit |
| 2023-03-23 | [AP-Casper](https://github.com/ruvnet/AP-Casper) | [`48a38534`](https://github.com/ruvnet/AP-Casper/commit/48a38534) | 2 | Initial commit |
| 2023-03-24 | [ChatGPT-Trading-Bot-for-KuCoin](https://github.com/ruvnet/ChatGPT-Trading-Bot-for-KuCoin) | [`e651ee64`](https://github.com/ruvnet/ChatGPT-Trading-Bot-for-KuCoin/commit/e651ee64) | 23 | Initial commit |
| 2023-03-26 | [2BotTalk](https://github.com/ruvnet/2BotTalk) | [`e92184c7`](https://github.com/ruvnet/2BotTalk/commit/e92184c7) | 15 | Initial commit |
| 2023-03-26 | [console-streamer](https://github.com/ruvnet/console-streamer) | [`0d26c2ea`](https://github.com/ruvnet/console-streamer/commit/0d26c2ea) | 7 | Initial commit |
| 2023-03-28 | [Swagger-ChatGPT-Plugin-Creator](https://github.com/ruvnet/Swagger-ChatGPT-Plugin-Creator) | [`790731b9`](https://github.com/ruvnet/Swagger-ChatGPT-Plugin-Creator/commit/790731b9) | 44 | Initial commit |
| 2023-03-28 | [chatgpt_tatum_plugin](https://github.com/ruvnet/chatgpt_tatum_plugin) | [`fce622bb`](https://github.com/ruvnet/chatgpt_tatum_plugin/commit/fce622bb) | 11 | Initial commit |
| 2023-03-28 | [chatgpt-aws-price-list-plugin](https://github.com/ruvnet/chatgpt-aws-price-list-plugin) | [`b48c6931`](https://github.com/ruvnet/chatgpt-aws-price-list-plugin/commit/b48c6931) | 8 | Initial commit |
| 2023-03-30 | [paris](https://github.com/ruvnet/paris) | [`26f8e8e8`](https://github.com/ruvnet/paris/commit/26f8e8e8) | 32 | Initial commit |
| 2023-03-31 | [VIVIAN](https://github.com/ruvnet/VIVIAN) | [`e8dc86d5`](https://github.com/ruvnet/VIVIAN/commit/e8dc86d5) | 42 | Initial commit |
| 2023-04-02 | [Bot-Generator-Bot](https://github.com/ruvnet/Bot-Generator-Bot) | [`d88a98d8`](https://github.com/ruvnet/Bot-Generator-Bot/commit/d88a98d8) | 569 | Initial commit |
| 2023-04-10 | [ruvnet](https://github.com/ruvnet/ruvnet) | [`0154f716`](https://github.com/ruvnet/ruvnet/commit/0154f716) | 210 | Initial commit |
| 2023-04-10 | [ARCADIA](https://github.com/ruvnet/ARCADIA) | [`3b73482c`](https://github.com/ruvnet/ARCADIA/commit/3b73482c) | 50 | Initial commit |
| 2023-04-13 | [Surfer](https://github.com/ruvnet/Surfer) | [`083a185f`](https://github.com/ruvnet/Surfer/commit/083a185f) | 88 | Initial commit |
| 2023-04-17 | [p2pGPT](https://github.com/ruvnet/p2pGPT) | [`3024ab62`](https://github.com/ruvnet/p2pGPT/commit/3024ab62) | 6 | Initial commit |
| 2023-04-17 | [CodeGPT](https://github.com/ruvnet/CodeGPT) | [`3e79f75b`](https://github.com/ruvnet/CodeGPT/commit/3e79f75b) | 4 | Create readme.md |
| 2023-04-22 | [chatgpt-openai-api-plugin](https://github.com/ruvnet/chatgpt-openai-api-plugin) | [`d3820387`](https://github.com/ruvnet/chatgpt-openai-api-plugin/commit/d3820387) | 147 | Initial commit |
| 2023-05-03 | [Prompt-Engine](https://github.com/ruvnet/Prompt-Engine) | [`0ad5b4f6`](https://github.com/ruvnet/Prompt-Engine/commit/0ad5b4f6) | 86 | Initial commit |
| 2023-10-24 | [openai-cost-estimator](https://github.com/ruvnet/openai-cost-estimator) | [`04da8fa6`](https://github.com/ruvnet/openai-cost-estimator/commit/04da8fa6) | 14 | Initial commit |
| 2023-11-15 | [coding-wingman](https://github.com/ruvnet/coding-wingman) | [`be1ee344`](https://github.com/ruvnet/coding-wingman/commit/be1ee344) | 27 | Initial commit |
| 2023-11-24 | [q-star](https://github.com/ruvnet/q-star) | [`113a9c69`](https://github.com/ruvnet/q-star/commit/113a9c69) | 96 | Initial commit |
| 2023-11-30 | [gpts](https://github.com/ruvnet/gpts) | [`49a66b84`](https://github.com/ruvnet/gpts/commit/49a66b84) | 297 | Initial commit |
| 2023-12-03 | [guardrail](https://github.com/ruvnet/guardrail) | [`d8ac7d8d`](https://github.com/ruvnet/guardrail/commit/d8ac7d8d) | 152 | Initial commit |
| 2023-12-06 | [ruvbot](https://github.com/ruvnet/ruvbot) | [`0372bc2d`](https://github.com/ruvnet/ruvbot/commit/0372bc2d) | 46 | Initial commit |
| 2023-12-14 | [agentX](https://github.com/ruvnet/agentX) | [`85f5858a`](https://github.com/ruvnet/agentX/commit/85f5858a) | 6 | Initial commit |
| 2023-12-20 | [docker](https://github.com/ruvnet/docker) | [`cd5e8a7b`](https://github.com/ruvnet/docker/commit/cd5e8a7b) | 0 | Initial commit |
| 2023-12-22 | [santa-ai-workshop](https://github.com/ruvnet/santa-ai-workshop) | [`f9daec0b`](https://github.com/ruvnet/santa-ai-workshop/commit/f9daec0b) | 6 | Initial commit |
| 2024-01-29 | [chat-ui](https://github.com/ruvnet/chat-ui) | [`3dc7d682`](https://github.com/ruvnet/chat-ui/commit/3dc7d682) | 0 | Initial commit |
| 2024-01-29 | [agent-gpt](https://github.com/ruvnet/agent-gpt) | [`8d8a9f92`](https://github.com/ruvnet/agent-gpt/commit/8d8a9f92) | 0 | Initial commit |
| 2024-02-01 | [opengpt](https://github.com/ruvnet/opengpt) | [`46a79253`](https://github.com/ruvnet/opengpt/commit/46a79253) | 0 | Initial commit |
| 2024-04-04 | [rUv-dev](https://github.com/ruvnet/rUv-dev) | [`a03620a7`](https://github.com/ruvnet/rUv-dev/commit/a03620a7) | 426 | Initial commit |
| 2024-04-08 | [r-flow](https://github.com/ruvnet/r-flow) | [`b49f1587`](https://github.com/ruvnet/r-flow/commit/b49f1587) | 6 | Initial commit |
| 2024-05-03 | [rUv-Enterprise-AI-Guide](https://github.com/ruvnet/rUv-Enterprise-AI-Guide) | [`2061c824`](https://github.com/ruvnet/rUv-Enterprise-AI-Guide/commit/2061c824) | 89 | Initial commit |
| 2024-05-07 | [AiHCC](https://github.com/ruvnet/AiHCC) | [`6ce5b70a`](https://github.com/ruvnet/AiHCC/commit/6ce5b70a) | 23 | Initial commit |
| 2024-05-13 | [agentic-employment](https://github.com/ruvnet/agentic-employment) | [`36ebf292`](https://github.com/ruvnet/agentic-employment/commit/36ebf292) | 55 | Initial commit |
| 2024-05-15 | [e2b-config](https://github.com/ruvnet/e2b-config) | [`15be43da`](https://github.com/ruvnet/e2b-config/commit/15be43da) | 0 | Create readme.md |
| 2024-05-16 | [aws-dev](https://github.com/ruvnet/aws-dev) | [`c640d2bc`](https://github.com/ruvnet/aws-dev/commit/c640d2bc) | 18 | Initial commit |
| 2024-05-17 | [agileagents](https://github.com/ruvnet/agileagents) | [`1bed97e0`](https://github.com/ruvnet/agileagents/commit/1bed97e0) | 42 | Initial commit |
| 2024-05-22 | [ai-stream](https://github.com/ruvnet/ai-stream) | [`26d6c00e`](https://github.com/ruvnet/ai-stream/commit/26d6c00e) | 2 | Initial commit |
| 2024-05-24 | [ai-video](https://github.com/ruvnet/ai-video) | [`662067b9`](https://github.com/ruvnet/ai-video/commit/662067b9) | 47 | Initial commit |
| 2024-05-24 | [supa-ruv](https://github.com/ruvnet/supa-ruv) | [`c9606d11`](https://github.com/ruvnet/supa-ruv/commit/c9606d11) | 18 | Initial commit |
| 2024-05-25 | [pygentic](https://github.com/ruvnet/pygentic) | [`9f586f38`](https://github.com/ruvnet/pygentic/commit/9f586f38) | 27 | Initial commit |
| 2024-05-25 | [ai-gist](https://github.com/ruvnet/ai-gist) | [`656e88d1`](https://github.com/ruvnet/ai-gist/commit/656e88d1) | 16 | Initial commit |
| 2024-05-25 | [pipackager](https://github.com/ruvnet/pipackager) | [`c7853077`](https://github.com/ruvnet/pipackager/commit/c7853077) | 11 | Initial commit |
| 2024-05-25 | [q-space](https://github.com/ruvnet/q-space) | [`7f497b7d`](https://github.com/ruvnet/q-space/commit/7f497b7d) | 9 | Initial commit |
| 2024-05-26 | [codecraft](https://github.com/ruvnet/codecraft) | [`b9b1b676`](https://github.com/ruvnet/codecraft/commit/b9b1b676) | 10 | Initial commit |
| 2024-05-27 | [climative](https://github.com/ruvnet/climative) | [`2be92554`](https://github.com/ruvnet/climative/commit/2be92554) | 0 | Initial commit |
| 2024-06-01 | [agentic-reports](https://github.com/ruvnet/agentic-reports) | [`f7379f60`](https://github.com/ruvnet/agentic-reports/commit/f7379f60) | 48 | Initial commit |
| 2024-06-02 | [markov-chains](https://github.com/ruvnet/markov-chains) | [`1a1f6165`](https://github.com/ruvnet/markov-chains/commit/1a1f6165) | 11 | Initial commit |
| 2024-06-05 | [agentic-voice](https://github.com/ruvnet/agentic-voice) | [`4e1afb6a`](https://github.com/ruvnet/agentic-voice/commit/4e1afb6a) | 118 | Initial commit |
| 2024-06-08 | [open-space](https://github.com/ruvnet/open-space) | [`14ad6d6e`](https://github.com/ruvnet/open-space/commit/14ad6d6e) | 13 | Initial commit |
| 2024-06-08 | [agentic-capacity-exchange](https://github.com/ruvnet/agentic-capacity-exchange) | [`2d17b299`](https://github.com/ruvnet/agentic-capacity-exchange/commit/2d17b299) | 10 | Initial commit |
| 2024-06-10 | [agentic-devops](https://github.com/ruvnet/agentic-devops) | [`3fef505e`](https://github.com/ruvnet/agentic-devops/commit/3fef505e) | 46 | Initial commit |
| 2024-06-19 | [agentic-dashboard](https://github.com/ruvnet/agentic-dashboard) | [`d60e1e91`](https://github.com/ruvnet/agentic-dashboard/commit/d60e1e91) | 6 | Initial commit |
| 2024-06-23 | [agentic-artifacts](https://github.com/ruvnet/agentic-artifacts) | [`fcc0db84`](https://github.com/ruvnet/agentic-artifacts/commit/fcc0db84) | 14 | Initial commit |
| 2024-06-25 | [agentic-gradio](https://github.com/ruvnet/agentic-gradio) | [`8c4752dd`](https://github.com/ruvnet/agentic-gradio/commit/8c4752dd) | 5 | Initial commit |
| 2024-07-03 | [agentXNG](https://github.com/ruvnet/agentXNG) | [`b13ec9f8`](https://github.com/ruvnet/agentXNG/commit/b13ec9f8) | 15 | Initial commit |
| 2024-07-03 | [justintimegcp_dashboard](https://github.com/ruvnet/justintimegcp_dashboard) | [`11b94f01`](https://github.com/ruvnet/justintimegcp_dashboard/commit/11b94f01) | 0 | Initial commit |
| 2024-08-12 | [jit-chat-replit](https://github.com/ruvnet/jit-chat-replit) | [`fcec7441`](https://github.com/ruvnet/jit-chat-replit/commit/fcec7441) | 0 | Initial commit |
| 2024-08-14 | [agentic-music](https://github.com/ruvnet/agentic-music) | [`75b5146e`](https://github.com/ruvnet/agentic-music/commit/75b5146e) | 3 | Initial commit |
| 2024-08-21 | [voicebot](https://github.com/ruvnet/voicebot) | [`bc25da0b`](https://github.com/ruvnet/voicebot/commit/bc25da0b) | 102 | Initial commit |
| 2024-08-27 | [agentic-flows](https://github.com/ruvnet/agentic-flows) | [`3ec27c79`](https://github.com/ruvnet/agentic-flows/commit/3ec27c79) | 4 | Initial commit |
| 2024-08-28 | [supabase-authentication](https://github.com/ruvnet/supabase-authentication) | [`61bcd544`](https://github.com/ruvnet/supabase-authentication/commit/61bcd544) | 17 | Initial commit |
| 2024-08-28 | [jit-streamlit](https://github.com/ruvnet/jit-streamlit) | [`33a92cb3`](https://github.com/ruvnet/jit-streamlit/commit/33a92cb3) | 0 | Initial commit |
| 2024-09-02 | [agentic-flow](https://github.com/ruvnet/agentic-flow) | [`4db75395`](https://github.com/ruvnet/agentic-flow/commit/4db75395) | 746 | Use tech stack vite_react_shadcn |
| 2024-09-02 | [ruv-js](https://github.com/ruvnet/ruv-js) | [`a227ad3b`](https://github.com/ruvnet/ruv-js/commit/a227ad3b) | 0 | Use tech stack vite_react_shadcn |
| 2024-09-02 | [agentic-workers](https://github.com/ruvnet/agentic-workers) | [`a227ad3b`](https://github.com/ruvnet/agentic-workers/commit/a227ad3b) | 0 | Use tech stack vite_react_shadcn |
| 2024-09-02 | [llamastack-dev](https://github.com/ruvnet/llamastack-dev) | [`a227ad3b`](https://github.com/ruvnet/llamastack-dev/commit/a227ad3b) | 0 | Use tech stack vite_react_shadcn |
| 2024-09-03 | [boilerplate](https://github.com/ruvnet/boilerplate) | [`b6d54357`](https://github.com/ruvnet/boilerplate/commit/b6d54357) | 0 | Use tech stack vite_react_shadcn |
| 2024-09-03 | [venture-co-pilot](https://github.com/ruvnet/venture-co-pilot) | [`1b22c035`](https://github.com/ruvnet/venture-co-pilot/commit/1b22c035) | 0 | Use tech stack vite_react_shadcn |
| 2024-09-03 | [muse-document-narration](https://github.com/ruvnet/muse-document-narration) | [`5fb2de70`](https://github.com/ruvnet/muse-document-narration/commit/5fb2de70) | 0 | Use tech stack vite_react_shadcn |
| 2024-09-04 | [bank-analytics-hub](https://github.com/ruvnet/bank-analytics-hub) | [`a03eaf12`](https://github.com/ruvnet/bank-analytics-hub/commit/a03eaf12) | 0 | Use tech stack vite_react_shadcn |
| 2024-09-04 | [pdf-highlight-hub](https://github.com/ruvnet/pdf-highlight-hub) | [`7c6eab3b`](https://github.com/ruvnet/pdf-highlight-hub/commit/7c6eab3b) | 0 | Use tech stack vite_react_shadcn |
| 2024-09-04 | [jit-pdfviewer](https://github.com/ruvnet/jit-pdfviewer) | [`7c6eab3b`](https://github.com/ruvnet/jit-pdfviewer/commit/7c6eab3b) | 0 | Use tech stack vite_react_shadcn |
| 2024-09-06 | [friendly-ui-canvas](https://github.com/ruvnet/friendly-ui-canvas) | [`ea35e291`](https://github.com/ruvnet/friendly-ui-canvas/commit/ea35e291) | 0 | Use tech stack vite_react_shadcn |
| 2024-09-07 | [aihl](https://github.com/ruvnet/aihl) | [`049b883e`](https://github.com/ruvnet/aihl/commit/049b883e) | 18 | Use tech stack vite_react_shadcn |
| 2024-09-07 | [ai-hacker-league](https://github.com/ruvnet/ai-hacker-league) | [`049b883e`](https://github.com/ruvnet/ai-hacker-league/commit/049b883e) | 1 | Use tech stack vite_react_shadcn |
| 2024-09-09 | [demo-proxy-app](https://github.com/ruvnet/demo-proxy-app) | [`9b024064`](https://github.com/ruvnet/demo-proxy-app/commit/9b024064) | 4 | first commit |
| 2024-09-10 | [llamastack](https://github.com/ruvnet/llamastack) | [`b09cadd0`](https://github.com/ruvnet/llamastack/commit/b09cadd0) | 43 | Initial commit |
| 2024-09-12 | [strawberry-phi](https://github.com/ruvnet/strawberry-phi) | [`60d64639`](https://github.com/ruvnet/strawberry-phi/commit/60d64639) | 59 | Use tech stack vite_react_shadcn |
| 2024-09-12 | [strawberry-phi-99-bd7efd10](https://github.com/ruvnet/strawberry-phi-99-bd7efd10) | [`60d64639`](https://github.com/ruvnet/strawberry-phi-99-bd7efd10/commit/60d64639) | 0 | Use tech stack vite_react_shadcn |
| 2024-09-14 | [drupaljs](https://github.com/ruvnet/drupaljs) | [`539ef219`](https://github.com/ruvnet/drupaljs/commit/539ef219) | 37 | Use tech stack vite_react_shadcn |
| 2024-09-14 | [hft](https://github.com/ruvnet/hft) | [`23b7dd76`](https://github.com/ruvnet/hft/commit/23b7dd76) | 3 | Initial commit |
| 2024-09-15 | [agenticsjs](https://github.com/ruvnet/agenticsjs) | [`234fa825`](https://github.com/ruvnet/agenticsjs/commit/234fa825) | 32 | Use tech stack vite_react_shadcn |
| 2024-09-15 | [code-red](https://github.com/ruvnet/code-red) | [`156d60ac`](https://github.com/ruvnet/code-red/commit/156d60ac) | 0 | Use tech stack vite_react_shadcn |
| 2024-09-18 | [healthcompliancehub](https://github.com/ruvnet/healthcompliancehub) | [`8e87ac80`](https://github.com/ruvnet/healthcompliancehub/commit/8e87ac80) | 0 | Use tech stack vite_react_shadcn |
| 2024-09-18 | [startup-sailor-navigator](https://github.com/ruvnet/startup-sailor-navigator) | [`d21b48b6`](https://github.com/ruvnet/startup-sailor-navigator/commit/d21b48b6) | 0 | Use tech stack vite_react_shadcn |
| 2024-09-19 | [infinity-ui](https://github.com/ruvnet/infinity-ui) | [`af790ffd`](https://github.com/ruvnet/infinity-ui/commit/af790ffd) | 9 | Use tech stack vite_react_shadcn |
| 2024-09-21 | [electo1-js](https://github.com/ruvnet/electo1-js) | [`ca9abec7`](https://github.com/ruvnet/electo1-js/commit/ca9abec7) | 12 | Use tech stack vite_react_shadcn |
| 2024-09-21 | [Electo1](https://github.com/ruvnet/Electo1) | [`66b51c87`](https://github.com/ruvnet/Electo1/commit/66b51c87) | 6 | Initial commit |
| 2024-09-23 | [vocalize](https://github.com/ruvnet/vocalize) | [`592327ec`](https://github.com/ruvnet/vocalize/commit/592327ec) | 0 | Use tech stack vite_react_shadcn |
| 2024-09-24 | [kellogg-mbai](https://github.com/ruvnet/kellogg-mbai) | [`ab6260ba`](https://github.com/ruvnet/kellogg-mbai/commit/ab6260ba) | 0 | Use tech stack vite_react_shadcn |
| 2024-09-28 | [ruv-engineer-dev](https://github.com/ruvnet/ruv-engineer-dev) | [`2da1d107`](https://github.com/ruvnet/ruv-engineer-dev/commit/2da1d107) | 0 | Use tech stack vite_react_shadcn |
| 2024-09-28 | [voic](https://github.com/ruvnet/voic) | [`27189234`](https://github.com/ruvnet/voic/commit/27189234) | 0 | Use tech stack vite_react_shadcn_ts |
| 2024-09-29 | [langchainjs](https://github.com/ruvnet/langchainjs) | [`dcf613e1`](https://github.com/ruvnet/langchainjs/commit/dcf613e1) | 0 | Use tech stack vite_react_shadcn_ts |
| 2024-10-02 | [agentic-copilot](https://github.com/ruvnet/agentic-copilot) | [`155fdd4c`](https://github.com/ruvnet/agentic-copilot/commit/155fdd4c) | 0 | Use tech stack vite_react_shadcn |
| 2024-10-04 | [agentic-search](https://github.com/ruvnet/agentic-search) | [`bbb22dfa`](https://github.com/ruvnet/agentic-search/commit/bbb22dfa) | 41 | Initial commit |
| 2024-10-05 | [agentic-preview](https://github.com/ruvnet/agentic-preview) | [`206bbfe6`](https://github.com/ruvnet/agentic-preview/commit/206bbfe6) | 13 | Initial commit |
| 2024-10-07 | [sparc](https://github.com/ruvnet/sparc) | [`a7ec7d5d`](https://github.com/ruvnet/sparc/commit/a7ec7d5d) | 467 | Initial commit |
| 2024-10-07 | [vitejs-hello-world](https://github.com/ruvnet/vitejs-hello-world) | [`c8470d7c`](https://github.com/ruvnet/vitejs-hello-world/commit/c8470d7c) | 0 | Use tech stack vite_react_shadcn |
| 2024-10-08 | [baxi-help](https://github.com/ruvnet/baxi-help) | [`5b6be8c9`](https://github.com/ruvnet/baxi-help/commit/5b6be8c9) | 0 | Use tech stack vite_react_shadcn |
| 2024-10-11 | [fireflies-webook](https://github.com/ruvnet/fireflies-webook) | [`37807cee`](https://github.com/ruvnet/fireflies-webook/commit/37807cee) | 21 | Initial commit |
| 2024-10-16 | [pwa-framework](https://github.com/ruvnet/pwa-framework) | [`82e1ec93`](https://github.com/ruvnet/pwa-framework/commit/82e1ec93) | 0 | Use tech stack vite_react_shadcn_ts |
| 2024-10-18 | [contextual-retrevial](https://github.com/ruvnet/contextual-retrevial) | [`726cff9b`](https://github.com/ruvnet/contextual-retrevial/commit/726cff9b) | 8 | Initial commit |
| 2024-10-19 | [agentic-scraper](https://github.com/ruvnet/agentic-scraper) | [`8f2d8ae7`](https://github.com/ruvnet/agentic-scraper/commit/8f2d8ae7) | 11 | Initial commit |
| 2024-10-26 | [local-logic](https://github.com/ruvnet/local-logic) | [`ef96bea3`](https://github.com/ruvnet/local-logic/commit/ef96bea3) | 14 | Initial commit |
| 2024-10-29 | [spare](https://github.com/ruvnet/spare) | [`b2c9c6ab`](https://github.com/ruvnet/spare/commit/b2c9c6ab) | 0 | Initial commit |
| 2024-11-02 | [agentic-security](https://github.com/ruvnet/agentic-security) | [`693a4b04`](https://github.com/ruvnet/agentic-security/commit/693a4b04) | 46 | Initial commit |
| 2024-11-09 | [brian-chat](https://github.com/ruvnet/brian-chat) | [`13375841`](https://github.com/ruvnet/brian-chat/commit/13375841) | 0 | Use tech stack vite_react_shadcn_ts |
| 2024-11-09 | [bandmate](https://github.com/ruvnet/bandmate) | [`fff36fc5`](https://github.com/ruvnet/bandmate/commit/fff36fc5) | 0 | Use tech stack vite_react_shadcn |
| 2024-11-15 | [aido](https://github.com/ruvnet/aido) | [`ba302d93`](https://github.com/ruvnet/aido/commit/ba302d93) | 36 | Initial commit |
| 2024-11-17 | [brian-ai](https://github.com/ruvnet/brian-ai) | [`539c637c`](https://github.com/ruvnet/brian-ai/commit/539c637c) | 0 | Initial commit |
| 2024-11-23 | [jit](https://github.com/ruvnet/jit) | [`85832b2a`](https://github.com/ruvnet/jit/commit/85832b2a) | 0 | Initial commit |
| 2024-11-26 | [federated-mcp](https://github.com/ruvnet/federated-mcp) | [`3d7e4696`](https://github.com/ruvnet/federated-mcp/commit/3d7e4696) | 64 | Initial commit |
| 2024-11-27 | [symbolic-scribe](https://github.com/ruvnet/symbolic-scribe) | [`dd03d857`](https://github.com/ruvnet/symbolic-scribe/commit/dd03d857) | 84 | Use tech stack vite_react_shadcn_ts |
| 2024-11-27 | [reflective-engineer](https://github.com/ruvnet/reflective-engineer) | [`dd03d857`](https://github.com/ruvnet/reflective-engineer/commit/dd03d857) | 57 | Use tech stack vite_react_shadcn_ts |
| 2024-12-05 | [spare-dev](https://github.com/ruvnet/spare-dev) | [`0e832bc1`](https://github.com/ruvnet/spare-dev/commit/0e832bc1) | 0 | Initial commit |
| 2024-12-10 | [quantum_cryptocurrency](https://github.com/ruvnet/quantum_cryptocurrency) | [`045b9383`](https://github.com/ruvnet/quantum_cryptocurrency/commit/045b9383) | 25 | Initial commit |
| 2024-12-13 | [hydrophone](https://github.com/ruvnet/hydrophone) | [`2b6a9f27`](https://github.com/ruvnet/hydrophone/commit/2b6a9f27) | 0 | Initial commit |
| 2024-12-17 | [omnipotent](https://github.com/ruvnet/omnipotent) | [`dac288de`](https://github.com/ruvnet/omnipotent/commit/dac288de) | 22 | Use tech stack vite_react_shadcn_ts |
| 2024-12-19 | [ruvi](https://github.com/ruvnet/ruvi) | [`e1496866`](https://github.com/ruvnet/ruvi/commit/e1496866) | 0 | Use tech stack vite_react_shadcn_ts |
| 2024-12-20 | [genesis](https://github.com/ruvnet/genesis) | [`08ee7de9`](https://github.com/ruvnet/genesis/commit/08ee7de9) | 39 | Initial commit |
| 2024-12-23 | [terrascape](https://github.com/ruvnet/terrascape) | [`5ef043c8`](https://github.com/ruvnet/terrascape/commit/5ef043c8) | 0 | Initial commit |
| 2024-12-31 | [AutoSurveyAI](https://github.com/ruvnet/AutoSurveyAI) | [`8f4f5174`](https://github.com/ruvnet/AutoSurveyAI/commit/8f4f5174) | 0 | Initial commit |
| 2025-01-05 | [SynthLang](https://github.com/ruvnet/SynthLang) | [`976b553d`](https://github.com/ruvnet/SynthLang/commit/976b553d) | 260 | Initial commit |
| 2025-01-06 | [midstream](https://github.com/ruvnet/midstream) | [`e8b8a87a`](https://github.com/ruvnet/midstream/commit/e8b8a87a) | 119 | Initial commit |
| 2025-01-07 | [inflight](https://github.com/ruvnet/inflight) | [`06e4ad34`](https://github.com/ruvnet/inflight/commit/06e4ad34) | 44 | Initial commit |
| 2025-01-11 | [AiCodeCalc](https://github.com/ruvnet/AiCodeCalc) | [`ef0dba34`](https://github.com/ruvnet/AiCodeCalc/commit/ef0dba34) | 16 | Use tech stack vite_react_shadcn_ts |
| 2025-01-11 | [ai-browse](https://github.com/ruvnet/ai-browse) | [`1b1e1de8`](https://github.com/ruvnet/ai-browse/commit/1b1e1de8) | 6 | Initial commit |
| 2025-01-13 | [police_data](https://github.com/ruvnet/police_data) | [`14e6c75b`](https://github.com/ruvnet/police_data/commit/14e6c75b) | 0 | Initial commit |
| 2025-01-20 | [auto-browser](https://github.com/ruvnet/auto-browser) | [`e14619c0`](https://github.com/ruvnet/auto-browser/commit/e14619c0) | 94 | Initial commit |
| 2025-01-23 | [hacker-league](https://github.com/ruvnet/hacker-league) | [`7265a46b`](https://github.com/ruvnet/hacker-league/commit/7265a46b) | 33 | add initial workspace configuration |
| 2025-01-30 | [nova](https://github.com/ruvnet/nova) | [`2881b757`](https://github.com/ruvnet/nova/commit/2881b757) | 40 | Initial commit |
| 2025-02-02 | [tariffic](https://github.com/ruvnet/tariffic) | [`88871740`](https://github.com/ruvnet/tariffic/commit/88871740) | 3 | Use tech stack vite_react_shadcn_ts |
| 2025-02-16 | [hello_world_agent](https://github.com/ruvnet/hello_world_agent) | [`a98c1956`](https://github.com/ruvnet/hello_world_agent/commit/a98c1956) | 99 | Initial commit |
| 2025-02-22 | [dspy.ts](https://github.com/ruvnet/dspy.ts) | [`68447191`](https://github.com/ruvnet/dspy.ts/commit/68447191) | 259 | Initial commit |
| 2025-02-23 | [onnx-agent](https://github.com/ruvnet/onnx-agent) | [`500e4655`](https://github.com/ruvnet/onnx-agent/commit/500e4655) | 22 | Initial commit |
| 2025-02-24 | [open-claude-code](https://github.com/ruvnet/open-claude-code) | [`2c25d1cb`](https://github.com/ruvnet/open-claude-code/commit/2c25d1cb) | 390 | Initial commit |
| 2025-03-03 | [headsup](https://github.com/ruvnet/headsup) | [`5c56ef47`](https://github.com/ruvnet/headsup/commit/5c56ef47) | 0 | Use tech stack vite_react_shadcn_ts |
| 2025-03-04 | [livekit-template](https://github.com/ruvnet/livekit-template) | [`ce63f4d7`](https://github.com/ruvnet/livekit-template/commit/ce63f4d7) | 0 | Use tech stack vite_react_shadcn_ts |
| 2025-03-13 | [sthesia](https://github.com/ruvnet/sthesia) | [`67c0f97d`](https://github.com/ruvnet/sthesia/commit/67c0f97d) | 0 | Use tech stack vite_react_shadcn_ts |
| 2025-03-17 | [hacker-console-coach](https://github.com/ruvnet/hacker-console-coach) | [`c14911cb`](https://github.com/ruvnet/hacker-console-coach/commit/c14911cb) | 0 | Use tech stack vite_react_shadcn_ts |
| 2025-03-18 | [cyber-risk](https://github.com/ruvnet/cyber-risk) | [`5aa9c316`](https://github.com/ruvnet/cyber-risk/commit/5aa9c316) | 0 | Use tech stack vite_react_shadcn_ts |
| 2025-03-19 | [clothesbin](https://github.com/ruvnet/clothesbin) | [`cd3b1a18`](https://github.com/ruvnet/clothesbin/commit/cd3b1a18) | 0 | Use tech stack vite_react_shadcn_ts |
| 2025-03-20 | [vibing](https://github.com/ruvnet/vibing) | [`ecbfa842`](https://github.com/ruvnet/vibing/commit/ecbfa842) | 11 | Use tech stack vite_react_shadcn_ts |
| 2025-03-31 | [phone-agent](https://github.com/ruvnet/phone-agent) | [`4c6b93bc`](https://github.com/ruvnet/phone-agent/commit/4c6b93bc) | 17 | Initial commit |
| 2025-03-31 | [ruvcode](https://github.com/ruvnet/ruvcode) | [`cf95fca1`](https://github.com/ruvnet/ruvcode/commit/cf95fca1) | 0 | Initial commit |
| 2025-03-31 | [myart-agent](https://github.com/ruvnet/myart-agent) | [`66f79455`](https://github.com/ruvnet/myart-agent/commit/66f79455) | 0 | Initial commit |
| 2025-04-06 | [roomodes](https://github.com/ruvnet/roomodes) | [`1ec9aa6c`](https://github.com/ruvnet/roomodes/commit/1ec9aa6c) | 13 | Initial commit |
| 2025-04-08 | [a2amcp](https://github.com/ruvnet/a2amcp) | [`fbe339a6`](https://github.com/ruvnet/a2amcp/commit/fbe339a6) | 0 | Use tech stack vite_react_shadcn_ts |
| 2025-04-18 | [quantum-magnetic-navigation](https://github.com/ruvnet/quantum-magnetic-navigation) | [`4872989a`](https://github.com/ruvnet/quantum-magnetic-navigation/commit/4872989a) | 41 | Initial commit |
| 2025-04-22 | [FunFairChatbot](https://github.com/ruvnet/FunFairChatbot) | [`828a1eb9`](https://github.com/ruvnet/FunFairChatbot/commit/828a1eb9) | 0 | Initial commit |
| 2025-04-24 | [befree](https://github.com/ruvnet/befree) | [`e84e188f`](https://github.com/ruvnet/befree/commit/e84e188f) | 0 | Initial commit |
| 2025-04-25 | [dynamo-mcp](https://github.com/ruvnet/dynamo-mcp) | [`52cdbac7`](https://github.com/ruvnet/dynamo-mcp/commit/52cdbac7) | 50 | Initial commit |
| 2025-04-25 | [vsc-remote-mcp](https://github.com/ruvnet/vsc-remote-mcp) | [`d41c887e`](https://github.com/ruvnet/vsc-remote-mcp/commit/d41c887e) | 15 | Initial commit |
| 2025-04-25 | [image-agent](https://github.com/ruvnet/image-agent) | [`4bf96fe1`](https://github.com/ruvnet/image-agent/commit/4bf96fe1) | 4 | Initial commit with ad-generator and project struc |
| 2025-04-27 | [codeswarm](https://github.com/ruvnet/codeswarm) | [`9833d8ac`](https://github.com/ruvnet/codeswarm/commit/9833d8ac) | 0 | Use tech stack vite_react_shadcn_ts |
| 2025-05-01 | [vibecast](https://github.com/ruvnet/vibecast) | [`2fdbbc51`](https://github.com/ruvnet/vibecast/commit/2fdbbc51) | 42 | Initial commit |
| 2025-05-01 | [agentic-robotics](https://github.com/ruvnet/agentic-robotics) | [`2fdbbc51`](https://github.com/ruvnet/agentic-robotics/commit/2fdbbc51) | 26 | Initial commit |
| 2025-05-05 | [ClaimDefendAI](https://github.com/ruvnet/ClaimDefendAI) | [`4cc05e43`](https://github.com/ruvnet/ClaimDefendAI/commit/4cc05e43) | 0 | Initial commit |
| 2025-05-06 | [sparc-ide](https://github.com/ruvnet/sparc-ide) | [`2d857126`](https://github.com/ruvnet/sparc-ide/commit/2d857126) | 35 | Initial commit |
| 2025-05-06 | [agentics-meetup](https://github.com/ruvnet/agentics-meetup) | [`8ad35460`](https://github.com/ruvnet/agentics-meetup/commit/8ad35460) | 2 | Initial commit |
| 2025-05-07 | [dq](https://github.com/ruvnet/dq) | [`4e50e251`](https://github.com/ruvnet/dq/commit/4e50e251) | 0 | Initial commit |
| 2025-05-09 | [proptax](https://github.com/ruvnet/proptax) | [`7b4c1f15`](https://github.com/ruvnet/proptax/commit/7b4c1f15) | 0 | Initial commit |
| 2025-05-09 | [property-tax-advocate](https://github.com/ruvnet/property-tax-advocate) | [`9a06ef94`](https://github.com/ruvnet/property-tax-advocate/commit/9a06ef94) | 0 | Use tech stack vite_react_shadcn_ts |
| 2025-05-11 | [agentic-difusion](https://github.com/ruvnet/agentic-difusion) | [`9ed049f7`](https://github.com/ruvnet/agentic-difusion/commit/9ed049f7) | 36 | Initial commit |
| 2025-05-15 | [Agent-Name-Service](https://github.com/ruvnet/Agent-Name-Service) | [`b5c30372`](https://github.com/ruvnet/Agent-Name-Service/commit/b5c30372) | 74 | Initial commit |
| 2025-05-18 | [codex-one](https://github.com/ruvnet/codex-one) | [`1e55a638`](https://github.com/ruvnet/codex-one/commit/1e55a638) | 27 | Initial commit |
| 2025-05-21 | [GenAI-Superstream](https://github.com/ruvnet/GenAI-Superstream) | [`517fa751`](https://github.com/ruvnet/GenAI-Superstream/commit/517fa751) | 59 | Initial commit |
| 2025-05-23 | [FACT](https://github.com/ruvnet/FACT) | [`3e78593c`](https://github.com/ruvnet/FACT/commit/3e78593c) | 179 | Initial commit |
| 2025-05-31 | [SAFLA](https://github.com/ruvnet/SAFLA) | [`02e555ec`](https://github.com/ruvnet/SAFLA/commit/02e555ec) | 154 | Initial commit |
| 2025-06-02 | [ruflo](https://github.com/ruvnet/ruflo) | [`7c1f9402`](https://github.com/ruvnet/ruflo/commit/7c1f9402) | 59272 | Initial commit |
| 2025-06-04 | [olympic-donation](https://github.com/ruvnet/olympic-donation) | [`f65a1a47`](https://github.com/ruvnet/olympic-donation/commit/f65a1a47) | 0 | Initial commit |
| 2025-06-04 | [profylr](https://github.com/ruvnet/profylr) | [`6517086e`](https://github.com/ruvnet/profylr/commit/6517086e) | 0 | Initial commit |
| 2025-06-05 | [hiring-agent-ai](https://github.com/ruvnet/hiring-agent-ai) | [`7d9d1408`](https://github.com/ruvnet/hiring-agent-ai/commit/7d9d1408) | 0 | Use tech stack vite_react_shadcn_ts |
| 2025-06-07 | [RuView](https://github.com/ruvnet/RuView) | [`6cab2309`](https://github.com/ruvnet/RuView/commit/6cab2309) | 73599 | Initial commit |
| 2025-06-09 | [ultrasonic](https://github.com/ruvnet/ultrasonic) | [`bfe93c56`](https://github.com/ruvnet/ultrasonic/commit/bfe93c56) | 90 | Initial commit |
| 2025-06-12 | [claude-test](https://github.com/ruvnet/claude-test) | [`93634dce`](https://github.com/ruvnet/claude-test/commit/93634dce) | 13 | Initial commit |
| 2025-06-16 | [QuDAG](https://github.com/ruvnet/QuDAG) | [`69f0c963`](https://github.com/ruvnet/QuDAG/commit/69f0c963) | 180 | Initial commit |
| 2025-06-17 | [neighborhoodies-shop](https://github.com/ruvnet/neighborhoodies-shop) | [`de026d92`](https://github.com/ruvnet/neighborhoodies-shop/commit/de026d92) | 0 | Use tech stack vite_react_shadcn_ts |
| 2025-06-17 | [neighborhoodies](https://github.com/ruvnet/neighborhoodies) | [`d2052bda`](https://github.com/ruvnet/neighborhoodies/commit/d2052bda) | 0 | Initial commit |
| 2025-06-20 | [neural-trader](https://github.com/ruvnet/neural-trader) | [`0c8d7fcc`](https://github.com/ruvnet/neural-trader/commit/0c8d7fcc) | 14 | Initial commit |
| 2025-06-25 | [yyz-agentics-june](https://github.com/ruvnet/yyz-agentics-june) | [`bfd0c30e`](https://github.com/ruvnet/yyz-agentics-june/commit/bfd0c30e) | 31 | Create README.MD |
| 2025-06-25 | [daa-dashboard](https://github.com/ruvnet/daa-dashboard) | [`0cf59cab`](https://github.com/ruvnet/daa-dashboard/commit/0cf59cab) | 0 | Use tech stack vite_react_shadcn_ts |
| 2025-06-26 | [ruv-FANN](https://github.com/ruvnet/ruv-FANN) | [`ad7cce73`](https://github.com/ruvnet/ruv-FANN/commit/ad7cce73) | 365 | Initial commit |
| 2025-06-27 | [semantic-navigator](https://github.com/ruvnet/semantic-navigator) | [`42caf096`](https://github.com/ruvnet/semantic-navigator/commit/42caf096) | 0 | Use tech stack vite_react_shadcn_ts |
| 2025-06-30 | [easygig-process-flow](https://github.com/ruvnet/easygig-process-flow) | [`d03e3120`](https://github.com/ruvnet/easygig-process-flow/commit/d03e3120) | 0 | Use tech stack vite_react_shadcn_ts |
| 2025-06-30 | [easygig-ai](https://github.com/ruvnet/easygig-ai) | [`b3631b49`](https://github.com/ruvnet/easygig-ai/commit/b3631b49) | 0 | Initial commit |
| 2025-07-04 | [dutch-tax](https://github.com/ruvnet/dutch-tax) | [`e4f134aa`](https://github.com/ruvnet/dutch-tax/commit/e4f134aa) | 0 | Initial commit: Dutch tax processing system |
| 2025-07-12 | [swarm-world](https://github.com/ruvnet/swarm-world) | [`2f7ce566`](https://github.com/ruvnet/swarm-world/commit/2f7ce566) | 19 | Initial commit |
| 2025-07-13 | [Synaptic-Mesh](https://github.com/ruvnet/Synaptic-Mesh) | [`30463806`](https://github.com/ruvnet/Synaptic-Mesh/commit/30463806) | 72 | Initial commit |
| 2025-07-16 | [code-mesh](https://github.com/ruvnet/code-mesh) | [`7c954f74`](https://github.com/ruvnet/code-mesh/commit/7c954f74) | 37 | Initial commit |
| 2025-07-17 | [neural-flow-trader](https://github.com/ruvnet/neural-flow-trader) | [`d2462c09`](https://github.com/ruvnet/neural-flow-trader/commit/d2462c09) | 0 | Use tech stack vite_react_shadcn_ts |
| 2025-08-11 | [Quantum-Virtual-Machine](https://github.com/ruvnet/Quantum-Virtual-Machine) | [`d22d3a83`](https://github.com/ruvnet/Quantum-Virtual-Machine/commit/d22d3a83) | 14 | Initial commit |
| 2025-08-14 | [alienator](https://github.com/ruvnet/alienator) | [`3a438416`](https://github.com/ruvnet/alienator/commit/3a438416) | 16 | Use tech stack vite_react_shadcn_ts_20250728_minor |
| 2025-08-19 | [flow-cloud](https://github.com/ruvnet/flow-cloud) | [`6c1c795d`](https://github.com/ruvnet/flow-cloud/commit/6c1c795d) | 1 | Initial commit |
| 2025-08-25 | [flow-nexus](https://github.com/ruvnet/flow-nexus) | [`c0e84960`](https://github.com/ruvnet/flow-nexus/commit/c0e84960) | 94 | Initial commit |
| 2025-09-13 | [chatgpt-dev-mode](https://github.com/ruvnet/chatgpt-dev-mode) | [`f796e1d5`](https://github.com/ruvnet/chatgpt-dev-mode/commit/f796e1d5) | 25 | Initial commit |
| 2025-09-19 | [sublinear-time-solver](https://github.com/ruvnet/sublinear-time-solver) | [`316ec6d7`](https://github.com/ruvnet/sublinear-time-solver/commit/316ec6d7) | 79 | Initial commit |
| 2025-09-24 | [agentic-catalog](https://github.com/ruvnet/agentic-catalog) | [`dcd152b9`](https://github.com/ruvnet/agentic-catalog/commit/dcd152b9) | 0 | Initial commit |
| 2025-10-07 | [goap-ui](https://github.com/ruvnet/goap-ui) | [`b29de928`](https://github.com/ruvnet/goap-ui/commit/b29de928) | 0 | [skip lovable] Use tech stack vite_react_shadcn_ts |
| 2025-10-13 | [agentic-tribe](https://github.com/ruvnet/agentic-tribe) | [`62388c19`](https://github.com/ruvnet/agentic-tribe/commit/62388c19) | 10 | Initial commit |
| 2025-11-11 | [claude-code-voyage](https://github.com/ruvnet/claude-code-voyage) | [`4e996d2e`](https://github.com/ruvnet/claude-code-voyage/commit/4e996d2e) | 0 | [skip lovable] Use tech stack vite_react_shadcn_ts |
| 2025-11-13 | [ruv.io](https://github.com/ruvnet/ruv.io) | [`e79a45e4`](https://github.com/ruvnet/ruv.io/commit/e79a45e4) | 20 | Initial commit |
| 2025-11-19 | [RuVector](https://github.com/ruvnet/RuVector) | [`ea3e70aa`](https://github.com/ruvnet/RuVector/commit/ea3e70aa) | 4240 | Initial commit |
| 2025-11-23 | [cognitum](https://github.com/ruvnet/cognitum) | [`52b25167`](https://github.com/ruvnet/cognitum/commit/52b25167) | 1 | Initial commit |
| 2025-11-24 | [musicai](https://github.com/ruvnet/musicai) | [`4c8d016a`](https://github.com/ruvnet/musicai/commit/4c8d016a) | 26 | Initial commit |
| 2025-12-01 | [evolven](https://github.com/ruvnet/evolven) | [`4272dc90`](https://github.com/ruvnet/evolven/commit/4272dc90) | 0 | Initial commit |
| 2025-12-23 | [agentchip](https://github.com/ruvnet/agentchip) | [`6e8c1674`](https://github.com/ruvnet/agentchip/commit/6e8c1674) | 1 | Initial commit |
| 2025-12-29 | [agvend](https://github.com/ruvnet/agvend) | [`71eb22db`](https://github.com/ruvnet/agvend/commit/71eb22db) | 0 | Initial commit |
| 2026-01-07 | [artista](https://github.com/ruvnet/artista) | [`cc21ae3a`](https://github.com/ruvnet/artista/commit/cc21ae3a) | 0 | Initial commit |
| 2026-01-13 | [marketing](https://github.com/ruvnet/marketing) | [`fe459976`](https://github.com/ruvnet/marketing/commit/fe459976) | 101 | Initial commit |
| 2026-01-13 | [workday-magento-desktop](https://github.com/ruvnet/workday-magento-desktop) | [`4683b713`](https://github.com/ruvnet/workday-magento-desktop/commit/4683b713) | 0 | Initial commit |
| 2026-01-24 | [optimizer](https://github.com/ruvnet/optimizer) | [`9ec50785`](https://github.com/ruvnet/optimizer/commit/9ec50785) | 1 | Initial release: RuVector Memory Optimizer v0.1.0 |
| 2026-01-25 | [huron-bangalore](https://github.com/ruvnet/huron-bangalore) | [`4041532b`](https://github.com/ruvnet/huron-bangalore/commit/4041532b) | 1 | Initial commit |
| 2026-02-07 | [ghub](https://github.com/ruvnet/ghub) | [`007531fd`](https://github.com/ruvnet/ghub/commit/007531fd) | 0 | Initial commit |
| 2026-02-11 | [huron-portland](https://github.com/ruvnet/huron-portland) | [`43b538a1`](https://github.com/ruvnet/huron-portland/commit/43b538a1) | 0 | Initial commit - based on huron-bangalore |
| 2026-02-23 | [Patents](https://github.com/ruvnet/Patents) | [`47a2ddbb`](https://github.com/ruvnet/Patents/commit/47a2ddbb) | 0 | Initial commit: patent portfolio system with agent |
| 2026-03-04 | [workday-desktop](https://github.com/ruvnet/workday-desktop) | [`5276ef07`](https://github.com/ruvnet/workday-desktop/commit/5276ef07) | 0 | Initial commit |
| 2026-04-03 | [rudevolution](https://github.com/ruvnet/rudevolution) | [`afde93e8`](https://github.com/ruvnet/rudevolution/commit/afde93e8) | 101 | feat: ruDevolution — AI-Powered JavaScript Decompi |
| 2026-04-04 | [rvm](https://github.com/ruvnet/rvm) | [`f39c3adf`](https://github.com/ruvnet/rvm/commit/f39c3adf) | 107 | Initial commit |
| 2026-04-07 | [musica](https://github.com/ruvnet/musica) | [`0f466eca`](https://github.com/ruvnet/musica/commit/0f466eca) | 17 | Initial commit |
| 2026-04-15 | [ruvultra](https://github.com/ruvnet/ruvultra) | [`78c31f36`](https://github.com/ruvnet/ruvultra/commit/78c31f36) | 0 | Initial v0.3-base — 91-tool MCP + profile helper + |
| 2026-04-17 | [ruos-macair](https://github.com/ruvnet/ruos-macair) | [`2bb46446`](https://github.com/ruvnet/ruos-macair/commit/2bb46446) | 9 | feat: ruOS MacBook Air 2012 — bootable USB build s |
| 2026-04-20 | [obsidian-brain](https://github.com/ruvnet/obsidian-brain) | [`e05b2856`](https://github.com/ruvnet/obsidian-brain/commit/e05b2856) | 17 | initial: obsidian-brain plugin — RuVector Brain br |
| 2026-04-22 | [Connectome-OS](https://github.com/ruvnet/Connectome-OS) | [`09a201bf`](https://github.com/ruvnet/Connectome-OS/commit/09a201bf) | 8 | initial: Connectome OS — README + project framing |
| 2026-04-22 | [Project-Sentinel](https://github.com/ruvnet/Project-Sentinel) | [`fe7bcfba`](https://github.com/ruvnet/Project-Sentinel/commit/fe7bcfba) | 0 | Initial commit: Project Sentinel planning delivera |
| 2026-04-24 | [RuLake](https://github.com/ruvnet/RuLake) | [`1d0cc353`](https://github.com/ruvnet/RuLake/commit/1d0cc353) | 10 | Initial commit: ruLake — a cache-coherent vector e |
| 2026-04-28 | [cognitum-claude-plugin](https://github.com/ruvnet/cognitum-claude-plugin) | [`c2d6acf2`](https://github.com/ruvnet/cognitum-claude-plugin/commit/c2d6acf2) | 5 | Initial cognitum-mcp plugin |
| 2026-05-06 | [agentdb](https://github.com/ruvnet/agentdb) | [`8b3388b2`](https://github.com/ruvnet/agentdb/commit/8b3388b2) | 66 | init: agentdb package source + marketing UI |
| 2026-05-13 | [rvcsi](https://github.com/ruvnet/rvcsi) | [`acd5689d`](https://github.com/ruvnet/rvcsi/commit/acd5689d) | 10 | rvCSI 0.3.0 — edge RF sensing runtime (extracted f |
| 2026-06-10 | [skygraph](https://github.com/ruvnet/skygraph) | [`685a2661`](https://github.com/ruvnet/skygraph/commit/685a2661) | 12 | SkyGraph: realtime all-sky dashboard — live ADS-B, |
| 2026-06-11 | [ruv-neural](https://github.com/ruvnet/ruv-neural) | [`1ece3afa`](https://github.com/ruvnet/ruv-neural/commit/1ece3afa) | 12 | Initial: rUv Neural — brain-network topology analy |
| 2026-06-11 | [drdv](https://github.com/ruvnet/drdv) | [`aa27fb76`](https://github.com/ruvnet/drdv/commit/aa27fb76) | 0 | Initial commit |

---

## Honest scope notes

- **Current public inventory:** 197 repositories, comprising 173 non-forks and 24 forks. Six public non-forks are empty, leaving 167 with commit history.
- **Historical table limitation:** the June table includes rows that are now private, transferred, deleted, or otherwise unavailable to unauthenticated readers. It is retained only as a labeled snapshot.
- **Root dates are lineage metadata, not public timestamps.** Git author dates are self-asserted; imported history can predate repository creation, while squash merges and reinitialization can collapse or erase earlier work.
- **Underlying primitives are external.** MCP (Anthropic, Nov 2024), HNSW, LoRA, FANN, DSPy, post-quantum KEMs, WiFi-CSI DensePose, diffusion LMs, DAG ledgers, autonomic computing — all credited to their originators in the prior-art lines. The claims are scoped to the specific synthesis or first runnable implementation.
- **Some repos implement a published external spec** (e.g. Agent-Name-Service implements the OWASP ANS protocol; federated-mcp extends Anthropic's MCP). For those the novelty is the implementation/extension layer, explicitly noted.
- **Many low-star repos are demos, course material, or app prototypes** — included in the provenance table for completeness but without novelty claims.
- **Validation invariant:** a current-public claim should return HTTP 200 to an unauthenticated reader and should name a feature commit, evidence path or test, release or registry timestamp, claim predicate, and prior-art cutoff. Rows that do not meet that invariant remain historical lineage notes rather than conclusive prior-art proof.

*Built from GitHub repository metadata and git history. Repository lineage, public availability, feature evidence, adoption metrics, and novelty are separate evidentiary layers and are reported as such.*
