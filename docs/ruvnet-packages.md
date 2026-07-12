# rUv — Packages & Libraries Index

Author: ruvnet (Reuven Cohen) · Initial snapshot 2026-06-13 · Live reconciliation 2026-07-11 ET / 2026-07-12 UTC

**At least 751 published artifacts across four public registries** — **360** Rust crates (1,035,464 cumulative downloads), **361** npm packages maintained by `ruvnet`, **8** ownership-verified PyPI libraries, and **22** Hugging Face models and spaces across the `ruvnet` and `ruv` accounts.

This is the **distribution surface** of the work catalogued in the [prior-art dossiers](https://github.com/ruvnet/ruvnet/blob/main/docs/ruvnet-prior-art.md). Where a git repository proves *authorship*, a published package proves *reach*: an immutable, timestamped, independently-installable artifact that anyone can pull down and verify. It is the strongest form of public provenance there is.

The June snapshot clustered 636 artifacts into 28 project families. The July reconciliation adds the MetaHarness, Helix, PhotonLayer, AgenticOW, AgentBBS, RuPixel, WorldGraph, and related distribution surfaces. Most remain sub-projects or target-specific binaries of a parent product, so raw registry counts must not be read as counts of independent products.

Package downloads are not the whole story: some projects, most of all **RuView** at 80,073 stars and **ruflo** at 64,041 stars, carry reach as GitHub adoption rather than crate pulls. Stars and downloads are reported separately because they measure different things.

*Live registry counts were verified July 11, 2026 ET / July 12 UTC from the official npm and crates.io APIs. The exact npm recount is **51,317,986 downloads** across 361 maintained packages for the complete 365-day window **2025-07-12 through 2026-07-11**. The older **34,447,577** figure is retained only as the June 13 historical snapshot. crates.io reports **1,035,464 cumulative downloads** across 360 crates. npm and crates.io counts include target-specific platform packages; registry ownership or maintainer status proves control of the publication surface, not sole authorship.*

## Registry totals

| Registry | Packages | Downloads |
|---|---|---|
| [crates.io](https://crates.io/users/ruvnet) | **360** | 1,035,464 cumulative |
| [npm](https://www.npmjs.com/~ruvnet) | **361** | **51,317,986** during 2025-07-12–2026-07-11 |
| [PyPI](https://pypi.org/user/ruvnet/) | **8** | ownership-verified |
| [Hugging Face](https://huggingface.co/ruvnet) | **22** | 7,868 current API-reported model downloads |

## Flagship projects by GitHub stars

Package downloads are only one signal. For repositories like **RuView** the reach shows up as **stars and clones**, not crate pulls — so here is the star ranking (publicly verifiable on each repo page).

| Repository | ★ Stars | Born | What it is |
|---|---|---|---|
| [RuView](https://github.com/ruvnet/RuView) | 80,073 | 2025-06-07 | Camera-free pose/vitals/presence from WiFi CSI |
| [ruflo](https://github.com/ruvnet/ruflo) | 64,041 | 2025-06-02 | Agent meta-harness for Claude, Codex, Hermes, and related hosts |
| [RuVector](https://github.com/ruvnet/RuVector) | 4,348 | 2025-11-19 | Self-learning vector and GNN memory DB in Rust |
| [agentic-flow](https://github.com/ruvnet/agentic-flow) | 773 | 2024-09-02 | Multi-model router for Claude Code and Agent SDK |
| [Bot-Generator-Bot](https://github.com/ruvnet/Bot-Generator-Bot) | 577 | 2023-04-02 | Prompt to generate ChatGPT bots |
| [sparc](https://github.com/ruvnet/sparc) | 471 | 2024-10-07 | Five-phase AI development methodology |
| [metaharness](https://github.com/ruvnet/metaharness) | 462 | 2026-06-13 | Verifiable generator and evolution layer for portable agent harnesses |
| [open-claude-code](https://github.com/ruvnet/open-claude-code) | 447 | 2025-02-24 | Claude Code CLI reverse-engineered and rebuilt |
| [rUv-dev](https://github.com/ruvnet/rUv-dev) | 425 | 2024-04-04 | AI-powered development using the rUv approach |
| [ruv-FANN](https://github.com/ruvnet/ruv-FANN) | 370 | 2025-06-26 | Memory-safe Rust FANN neural-net library |
| [SynthLang](https://github.com/ruvnet/SynthLang) | 263 | 2025-01-05 | Logographic prompt-compression language |
| [dspy.ts](https://github.com/ruvnet/dspy.ts) | 262 | 2025-02-22 | DSPy for TypeScript and browser runtimes |
| [daa](https://github.com/ruvnet/daa) | 246 | 2023-03-09 | Decentralized Autonomous Applications |
| [QuDAG](https://github.com/ruvnet/QuDAG) | 189 | 2025-06-16 | Quantum-resistant DAG anonymous communications |
| [FACT](https://github.com/ruvnet/FACT) | 178 | 2025-05-23 | Deterministic tool retrieval via MCP |

**Repository reach (clone traffic).** Stars are the public proxy; raw clone volume is higher. At peak, **RuView** and **ruflo** each sustained roughly **300k–500k git clones per week** over a multi-month stretch (recently lower) — owner traffic analytics, since GitHub clone counts are visible only to repo admins and are not independently verifiable from outside. They are reported here for context, separate from the publicly-checkable star and download figures.

---

## July 11 registry reconciliation

Cutoff: `2026-06-13T00:00:00Z`. npm's 98 means packages whose **latest indexed release** is on or after the cutoff, not necessarily 98 newly created packages. crates.io's 55 means crates whose `updated_at` is on or after the cutoff. Target binaries, host adapters, and examples are real independently installable artifacts, but they are grouped beneath parent products rather than presented as separate inventions.

### Net-new registry IDs absent from the June snapshot

This is the actual missing-package delta: **77 new npm IDs** and **38 new crate IDs**, with no June IDs removed. The 98 npm and 55 crate activity counts below are larger because they also include new releases of existing IDs.

| Parent surface | npm IDs added | Crate IDs added | Detail |
|---|---:|---:|---|
| MetaHarness | 63 | 0 | 61 packages in `@metaharness/*`, unscoped `metaharness`, and `@ruvnet/agent-harness-generator` |
| Helix | 0 | 28 | Complete `helix-*` workspace distribution |
| RuVector | 4 | 7 | `@ruvector/tiny-dancer-linux-arm64-musl`, `@ruvector/tiny-dancer-linux-x64-musl`, `@ruvector/tiny-dancer-win32-arm64-msvc`, `ruvector-mragent`; crates: capgated, GNN rerank, LSM ANN, Matryoshka, PQ search, proof gate, SPANN |
| TimesFM | 0 | 2 | `timesfm`, `ruvector-timesfm` |
| PhotonLayer | 0 | 1 | `photonlayer-core` |
| RuQu | 1 | 0 | `@ruvector/ruqu` |
| RuView | 1 | 0 | `@ruvnet/ruview` |
| RuV Neural and RuVN | 2 | 0 | `@ruvnet/ruvn`, `ruvneural` |
| Standalone | 6 | 0 | `agentbbs`, `agenticow`, `rupixel`, `ruvdrone`, `symbolic-scribe-harness`, `worldgraphs` |

The 38 new crates account for 1,181 downloads so far. Total crate downloads rose by 256,349 because the established catalog also continued accumulating usage.

### npm: 98 recently released packages

| Distribution surface | Count | Interpretation |
|---|---:|---|
| `@metaharness/*` | 61 | 18 examples, 9 host adapters, plus kernel, SDK, verticals, Darwin, Flywheel, Router, RedBlue, and interpretability packages |
| `@ruvector/*` | 16 | Core packages plus 9 platform-specific target binaries |
| `@claude-flow/*` | 3 | CLI, memory, and agent-federation plugin releases |
| Other maintained packages | 18 | Umbrella CLIs and standalone packages, including unscoped MetaHarness, Ruflo, AgentBBS, AgenticOW, RuPixel, WorldGraphs, and RuVDrone |

<details><summary><b>Complete recent npm set</b></summary>

**MetaHarness scope, 61:** `@metaharness/aws-finops`, `claude-code`, `codex`, `coding`, `copilot`, `darwin`, `devops`, `education`, `example-ads`, `example-aws`, `example-azure`, `example-bio`, `example-datadog`, `example-fhir`, `example-gcp`, `example-github`, `example-huggingface`, `example-iot`, `example-nasa`, `example-pinecone`, `example-qiskit`, `example-slack`, `example-stripe`, `example-supabase`, `example-twilio`, `example-web3`, `flywheel`, `gaming`, `github-actions`, `harness`, `hermes`, `host-claude-code`, `host-codex`, `host-copilot`, `host-github-actions`, `host-hermes`, `host-openclaw`, `host-opencode`, `host-pi-dev`, `host-rvm`, `jujutsu`, `kernel`, `legal`, `openclaw`, `opencode`, `pi-dev`, `projects`, `redblue`, `repo-maintainer`, `research`, `router`, `rvm`, `sales`, `sdk`, `support`, `trading`, `vertical-base`, `vertical-trading`, `weight-eft`, `workspace-lens`, `workspace-probe`.

**RuVector scope, 16:** `@ruvector/emergent-time`, `ruqu`, `ruvllm`, `rvf`, `rvf-node`, `rvf-node-linux-x64-gnu`, `tiny-dancer`, eight `tiny-dancer` platform targets, and `wasm`.

**Claude Flow scope, 3:** `@claude-flow/cli`, `@claude-flow/memory`, `@claude-flow/plugin-agent-federation`.

**Other, 18:** `@ruvnet/agent-harness-generator`, `@ruvnet/ruview`, `@ruvnet/ruvn`, `@ruvnet/rvagent`, `agentbbs`, `agentdb`, `agentic-flow`, `agenticow`, `claude-flow`, `metaharness`, `ruflo`, `rupixel`, `ruvdrone`, `ruvector`, `ruvector-mragent`, `ruvneural`, `symbolic-scribe-harness`, `worldgraphs`.

</details>

### crates.io: 55 recently updated crates

| Family | Count | Crates |
|---|---:|---|
| Helix | 28 | `helix-bioage`, `cohort`, `connect`, `demo`, `embed`, `escalation`, `evidence`, `evolve`, `fed`, `focus`, `genome`, `llm`, `neural`, `numeric`, `ocr`, `ontology`, `pipeline`, `provenance`, `refranges`, `retrieval`, `score`, `sensing`, `timeline`, `vault`, `verifier`, `vision`, `visual`, `wasm` |
| RuVector-prefixed | 22 | `ruvector-attention`, `capgated`, `cluster`, `collections`, `core`, `dag`, `diskann`, `filter`, `gnn`, `gnn-rerank`, `graph`, `lsm-ann`, `math`, `matryoshka`, `pq-search`, `proof-gate`, `raft`, `replication`, `sona`, `solver`, `spann`, `timesfm` |
| RuvLLM | 2 | `ruvllm`, `ruvllm-cli` |
| Standalone | 3 | `emergent-time`, `photonlayer-core`, `timesfm` |

### New and materially expanded package families

#### MetaHarness

The parent distribution surface now spans **63 registry artifacts**: 61 packages in `@metaharness/*`, the unscoped [`metaharness`](https://www.npmjs.com/package/metaharness) CLI, and [`@ruvnet/agent-harness-generator`](https://www.npmjs.com/package/@ruvnet/agent-harness-generator). It includes [`@metaharness/darwin`](https://www.npmjs.com/package/@metaharness/darwin), [`@metaharness/flywheel`](https://www.npmjs.com/package/@metaharness/flywheel), [`@metaharness/router`](https://www.npmjs.com/package/@metaharness/router), [`@metaharness/redblue`](https://www.npmjs.com/package/@metaharness/redblue), [`@metaharness/workspace-lens`](https://www.npmjs.com/package/@metaharness/workspace-lens), [`@metaharness/workspace-probe`](https://www.npmjs.com/package/@metaharness/workspace-probe), the kernel and SDK, vertical packages, 18 examples, and nine host adapters. This is one product family with a large independently installable distribution surface, not 63 independent products.

#### Helix

Twenty-eight Rust crates implement the local-first health-intelligence stack across evidence, ontology, provenance, retrieval, sensing, OCR, vision, cohort, bio-age, genomics, model escalation, verification, WASM, and demo surfaces.

#### Recent standalone distribution

New or newly surfaced installable products include [`agentbbs`](https://www.npmjs.com/package/agentbbs), [`agenticow`](https://www.npmjs.com/package/agenticow), [`rupixel`](https://www.npmjs.com/package/rupixel), [`ruvdrone`](https://www.npmjs.com/package/ruvdrone), [`worldgraphs`](https://www.npmjs.com/package/worldgraphs), [`@ruvector/ruqu`](https://www.npmjs.com/package/@ruvector/ruqu), [`@ruvector/ruvllm`](https://www.npmjs.com/package/@ruvector/ruvllm), [`@ruvnet/ruview`](https://www.npmjs.com/package/@ruvnet/ruview), and [`@ruvnet/rvagent`](https://www.npmjs.com/package/@ruvnet/rvagent).

---

## By project family

The table below preserves the June 13 family allocation and download snapshot for reproducibility. It is not a recomputation of the July totals above. Many artifacts are sub-projects, adapters, examples, or target binaries of a parent product and would be invisible in a repository-level listing.

| Project family | First publish | Crates | npm | Crate dl (all-time) | npm dl (12 mo) | ★ Repo |
|---|---|---|---|---|---|---|
| **RuVector (self-learning vector DB)** | 2025-09-27 | 99 | 141 | 344,396 | 24,372,003 | [4,240](https://github.com/ruvnet/RuVector) |
| **Claude-Flow / Ruflo (harness)** | 2026-01-06 | 0 | 41 | 0 | 6,710,576 | [59,272](https://github.com/ruvnet/ruflo) |
| **Other / standalone** | 2024-09-16 | 1 | 45 | 27 | 3,364,998 | — |
| **Midstream (realtime LLM streaming)** | 2025-10-27 | 7 | 1 | 99,709 | 0 | [119](https://github.com/ruvnet/midstream) |
| **Sublinear / Temporal solvers** | 2025-09-20 | 8 | 4 | 92,802 | 0 | [79](https://github.com/ruvnet/sublinear-time-solver) |
| **Lean-Agentic (RAG gateway)** | 2025-10-25 | 3 | 1 | 48,094 | 0 | — |
| **Cognitum (edge cognition device)** | 2026-01-17 | 7 | 0 | 40,360 | 0 | [1](https://github.com/ruvnet/cognitum) |
| **QuDAG (quantum-resistant DAG)** | 2025-06-20 | 13 | 5 | 39,758 | 0 | [180](https://github.com/ruvnet/QuDAG) |
| **ruv-FANN / ruv-swarm / neuro-divergent** | 2025-06-26 | 22 | 1 | 29,882 | 0 | [365](https://github.com/ruvnet/ruv-FANN) |
| **RuvLLM (LLM serving)** | 2025-12-12 | 5 | 1 | 20,270 | 0 | — |
| **DAA (decentralized autonomous apps)** | 2025-06-24 | 11 | 0 | 15,993 | 0 | [238](https://github.com/ruvnet/daa) |
| **WiFi-DensePose / RuView (CSI sensing)** | 2026-03-01 | 21 | 0 | 6,613 | 0 | [73,599](https://github.com/ruvnet/RuView) |
| **Micro-Neural (Semantic Cartan)** | 2025-07-12 | 8 | 0 | 5,860 | 0 | — |
| **AIMDS (AI Manipulation Defense)** | 2025-10-27 | 4 | 0 | 5,694 | 0 | — |
| **Neural Trader** | 2025-11-13 | 14 | 39 | 4,488 | 0 | [14](https://github.com/ruvnet/neural-trader) |
| **Synaptic Neural Mesh** | 2025-07-13 | 5 | 0 | 4,272 | 0 | [72](https://github.com/ruvnet/Synaptic-Mesh) |
| **OpenCV-Rust port** | 2025-07-12 | 3 | 0 | 3,072 | 0 | — |
| **agentic-payments / goalie / misc tools** | 2025-06-28 | 6 | 3 | 2,729 | 0 | — |
| **Code-Mesh** | 2025-07-16 | 4 | 0 | 2,588 | 0 | [37](https://github.com/ruvnet/code-mesh) |
| **EXO-AI (cognitive substrate)** | 2025-12-02 | 9 | 0 | 2,162 | 0 | — |
| **RuVix Cognition Kernel** | 2026-03-14 | 23 | 0 | 2,106 | 0 | [107](https://github.com/ruvnet/rvm) |
| **Geometric Langlands** | 2025-07-19 | 2 | 0 | 1,919 | 0 | — |
| **7sense (bioacoustics)** | 2026-01-16 | 8 | 0 | 1,425 | 0 | — |
| **ruv-neural (edge neural)** | 2026-03-09 | 11 | 0 | 1,188 | 0 | [12](https://github.com/ruvnet/ruv-neural) |
| **Agentic Robotics** | 2025-11-15 | 5 | 1 | 987 | 0 | [26](https://github.com/ruvnet/agentic-robotics) |
| **FACT (fast augmented context)** | 2025-07-31 | 2 | 0 | 923 | 0 | [179](https://github.com/ruvnet/FACT) |
| **RuQu (quantum simulator)** | 2026-01-17 | 12 | 0 | 825 | 0 | — |
| **rvCSI (CSI sensing lib)** | 2026-05-13 | 9 | 1 | 648 | 0 | [10](https://github.com/ruvnet/rvcsi) |

### RuVector (self-learning vector DB)
Self-learning vector + GNN memory DB; RVF container, SONA, mincut-gated transformer, RaBitQ, DiskANN, hyperbolic HNSW.

- **crates (99, first 2025-09-27):** [`ruvector-core`](https://crates.io/crates/ruvector-core), [`ruvector-mincut`](https://crates.io/crates/ruvector-mincut), [`ruvector-attention`](https://crates.io/crates/ruvector-attention), [`ruvector-solver`](https://crates.io/crates/ruvector-solver), [`ruvector-attn-mincut`](https://crates.io/crates/ruvector-attn-mincut), [`ruvector-temporal-tensor`](https://crates.io/crates/ruvector-temporal-tensor), [`ruvector-sona`](https://crates.io/crates/ruvector-sona), [`ruvector-mincut-gated-transformer`](https://crates.io/crates/ruvector-mincut-gated-transformer) +91 more
- **npm (141, 24,372,003 dl/12mo):** [`@ruvector/graph-node`](https://www.npmjs.com/package/@ruvector/graph-node), [`@ruvector/ruvllm`](https://www.npmjs.com/package/@ruvector/ruvllm), [`@ruvector/attention`](https://www.npmjs.com/package/@ruvector/attention), [`@ruvector/gnn`](https://www.npmjs.com/package/@ruvector/gnn), [`@ruvector/graph-node-linux-x64-gnu`](https://www.npmjs.com/package/@ruvector/graph-node-linux-x64-gnu), [`ruvector`](https://www.npmjs.com/package/ruvector) +135 more

### Claude-Flow / Ruflo (harness)
The agent meta-harness for Claude (npm distribution and plugins).

- **npm (41, 6,710,576 dl/12mo):** [`claude-flow`](https://www.npmjs.com/package/claude-flow), [`@claude-flow/cli`](https://www.npmjs.com/package/@claude-flow/cli), [`@claude-flow/plugin-gastown-bridge`](https://www.npmjs.com/package/@claude-flow/plugin-gastown-bridge), [`@claude-flow/codex`](https://www.npmjs.com/package/@claude-flow/codex), [`ruflo`](https://www.npmjs.com/package/ruflo), [`@claude-flow/memory`](https://www.npmjs.com/package/@claude-flow/memory) +35 more

### Other / standalone
Standalone crates not part of a larger family.

- **crates (1, first 2024-09-16):** [`rulake`](https://crates.io/crates/rulake)
- **npm (45, 3,364,998 dl/12mo):** [`agentdb`](https://www.npmjs.com/package/agentdb), [`agentic-flow`](https://www.npmjs.com/package/agentic-flow), [`agent-booster`](https://www.npmjs.com/package/agent-booster), [`@cognitum-one/sdk`](https://www.npmjs.com/package/@cognitum-one/sdk), [`flow-nexus`](https://www.npmjs.com/package/flow-nexus), [`strange-loops`](https://www.npmjs.com/package/strange-loops) +39 more

### Midstream (realtime LLM streaming)
Realtime in-flight LLM streaming: nanosecond scheduler, QUIC multi-stream, neural-solver, strange-loop.

- **crates (7, first 2025-10-27):** [`midstreamer-temporal-compare`](https://crates.io/crates/midstreamer-temporal-compare), [`midstreamer-attractor`](https://crates.io/crates/midstreamer-attractor), [`midstreamer-scheduler`](https://crates.io/crates/midstreamer-scheduler), [`midstreamer-quic`](https://crates.io/crates/midstreamer-quic), [`midstreamer-neural-solver`](https://crates.io/crates/midstreamer-neural-solver), [`midstreamer-strange-loop`](https://crates.io/crates/midstreamer-strange-loop), [`midstream`](https://crates.io/crates/midstream)
- **npm (1, 0 dl/12mo):** [`midstreamer`](https://www.npmjs.com/package/midstreamer)

### Sublinear / Temporal solvers
Sublinear-time asymmetric DD solvers + the temporal/consciousness family (strange-loop, attractor studio, subjective-time).

- **crates (8, first 2025-09-20):** [`strange-loop`](https://crates.io/crates/strange-loop), [`nanosecond-scheduler`](https://crates.io/crates/nanosecond-scheduler), [`subjective-time-expansion`](https://crates.io/crates/subjective-time-expansion), [`temporal-attractor-studio`](https://crates.io/crates/temporal-attractor-studio), [`temporal-neural-solver`](https://crates.io/crates/temporal-neural-solver), [`temporal-compare`](https://crates.io/crates/temporal-compare), [`sublinear`](https://crates.io/crates/sublinear), [`temporal-lead-solver`](https://crates.io/crates/temporal-lead-solver)
- **npm (4, 0 dl/12mo):** [`temporal-lead-solver`](https://www.npmjs.com/package/temporal-lead-solver), [`sublinear-time-solver`](https://www.npmjs.com/package/sublinear-time-solver), [`@ruvnet/strange-loop`](https://www.npmjs.com/package/@ruvnet/strange-loop), [`temporal-neural-solver`](https://www.npmjs.com/package/temporal-neural-solver)

### Lean-Agentic (RAG gateway)
Hash-consed dependency RAG gateway with multi-lane cost routing and verification.

- **crates (3, first 2025-10-25):** [`lean-agentic`](https://crates.io/crates/lean-agentic), [`leanr-rag-gateway`](https://crates.io/crates/leanr-rag-gateway), [`leanr-wasm`](https://crates.io/crates/leanr-wasm)
- **npm (1, 0 dl/12mo):** [`lean-agentic`](https://www.npmjs.com/package/lean-agentic)

### Cognitum (edge cognition device)
Edge cognition device: 256-tile coherence-gate WASM kernel, anytime-valid arbiter, Home-Assistant/Matter cogs.

- **crates (7, first 2026-01-17):** [`cognitum-gate-tilezero`](https://crates.io/crates/cognitum-gate-tilezero), [`cognitum-gate-kernel`](https://crates.io/crates/cognitum-gate-kernel), [`cognitum-rs`](https://crates.io/crates/cognitum-rs), [`cognitum-one`](https://crates.io/crates/cognitum-one), [`cog-ha-matter`](https://crates.io/crates/cog-ha-matter), [`cog-person-count`](https://crates.io/crates/cog-person-count), [`cog-pose-estimation`](https://crates.io/crates/cog-pose-estimation)

### QuDAG (quantum-resistant DAG)
Quantum-resistant DAG anonymous comms: ML-KEM/ML-DSA crypto, onion routing, vault, exchange, MCP.

- **crates (13, first 2025-06-20):** [`qudag-crypto`](https://crates.io/crates/qudag-crypto), [`qudag-dag`](https://crates.io/crates/qudag-dag), [`qudag-network`](https://crates.io/crates/qudag-network), [`qudag`](https://crates.io/crates/qudag), [`qudag-cli`](https://crates.io/crates/qudag-cli), [`qudag-vault-core`](https://crates.io/crates/qudag-vault-core), [`qudag-protocol`](https://crates.io/crates/qudag-protocol), [`qudag-mcp`](https://crates.io/crates/qudag-mcp) +5 more
- **npm (5, 0 dl/12mo):** [`@qudag/napi-core`](https://www.npmjs.com/package/@qudag/napi-core), [`@qudag/cli`](https://www.npmjs.com/package/@qudag/cli), [`@qudag/mcp-sse`](https://www.npmjs.com/package/@qudag/mcp-sse), [`@qudag/mcp-stdio`](https://www.npmjs.com/package/@qudag/mcp-stdio), [`qudag`](https://www.npmjs.com/package/qudag)

### ruv-FANN / ruv-swarm / neuro-divergent
Memory-safe Rust FANN port + the ruv-swarm orchestration stack, neuro-divergent forecasting models, CUDA->Rust/WASM transpiler.

- **crates (22, first 2025-06-26):** [`ruv-fann`](https://crates.io/crates/ruv-fann), [`ruv-swarm-core`](https://crates.io/crates/ruv-swarm-core), [`cuda-rust-wasm`](https://crates.io/crates/cuda-rust-wasm), [`ruv-swarm-agents`](https://crates.io/crates/ruv-swarm-agents), [`ruv-swarm-ml`](https://crates.io/crates/ruv-swarm-ml), [`ruv-swarm-persistence`](https://crates.io/crates/ruv-swarm-persistence), [`ruv-swarm-transport`](https://crates.io/crates/ruv-swarm-transport), [`ruv-swarm-wasm`](https://crates.io/crates/ruv-swarm-wasm) +14 more
- **npm (1, 0 dl/12mo):** [`ruv-swarm`](https://www.npmjs.com/package/ruv-swarm)

### RuvLLM (LLM serving)
LLM serving runtime with RuVector integration, ESP32 tiny inference, subquadratic sparse attention.

- **crates (5, first 2025-12-12):** [`ruvllm`](https://crates.io/crates/ruvllm), [`ruvllm-esp32`](https://crates.io/crates/ruvllm-esp32), [`ruvllm-cli`](https://crates.io/crates/ruvllm-cli), [`ruvllm_sparse_attention`](https://crates.io/crates/ruvllm_sparse_attention), [`ruvllm-wasm`](https://crates.io/crates/ruvllm-wasm)
- **npm (1, 0 dl/12mo):** [`ruvllm-esp32`](https://www.npmjs.com/package/ruvllm-esp32)

### DAA (decentralized autonomous apps)
Decentralized autonomous applications: economy, rules, chain, Prime distributed-training stack.

- **crates (11, first 2025-06-24):** [`daa-ai`](https://crates.io/crates/daa-ai), [`daa-rules`](https://crates.io/crates/daa-rules), [`daa-economy`](https://crates.io/crates/daa-economy), [`daa-prime-core`](https://crates.io/crates/daa-prime-core), [`daa-prime-dht`](https://crates.io/crates/daa-prime-dht), [`daa-prime-trainer`](https://crates.io/crates/daa-prime-trainer), [`daa-chain`](https://crates.io/crates/daa-chain), [`daa-orchestrator`](https://crates.io/crates/daa-orchestrator) +3 more

### WiFi-DensePose / RuView (CSI sensing)
Camera-free pose, vitals & presence from WiFi CSI: signal->NN->worldgraph, geo, mass-casualty, calibration.

- **crates (21, first 2026-03-01):** [`wifi-densepose-worldgraph`](https://crates.io/crates/wifi-densepose-worldgraph), [`wifi-densepose-geo`](https://crates.io/crates/wifi-densepose-geo), [`wifi-densepose-core`](https://crates.io/crates/wifi-densepose-core), [`wifi-densepose-signal`](https://crates.io/crates/wifi-densepose-signal), [`wifi-densepose-nn`](https://crates.io/crates/wifi-densepose-nn), [`wifi-densepose-mat`](https://crates.io/crates/wifi-densepose-mat), [`wifi-densepose-wifiscan`](https://crates.io/crates/wifi-densepose-wifiscan), [`wifi-densepose-ruvector`](https://crates.io/crates/wifi-densepose-ruvector) +13 more

### Micro-Neural (Semantic Cartan)
Semantic Cartan-matrix micro-neural networks: attention, routing, swarm, metrics (no_std).

- **crates (8, first 2025-07-12):** [`micro_core`](https://crates.io/crates/micro_core), [`micro_metrics`](https://crates.io/crates/micro_metrics), [`micro_routing`](https://crates.io/crates/micro_routing), [`neurodna`](https://crates.io/crates/neurodna), [`micro_swarm`](https://crates.io/crates/micro_swarm), [`micro_cartan_attn`](https://crates.io/crates/micro_cartan_attn), [`nano-consciousness`](https://crates.io/crates/nano-consciousness), [`micro-hnsw-wasm`](https://crates.io/crates/micro-hnsw-wasm)

### AIMDS (AI Manipulation Defense)
AI Manipulation Defense System: fast-path detection, deep behavioral analysis, adaptive meta-learning response.

- **crates (4, first 2025-10-27):** [`aimds-core`](https://crates.io/crates/aimds-core), [`aimds-detection`](https://crates.io/crates/aimds-detection), [`aimds-analysis`](https://crates.io/crates/aimds-analysis), [`aimds-response`](https://crates.io/crates/aimds-response)

### Neural Trader
Neural trading stack: LSTM/conformal prediction, backtesting, portfolio, execution, AgentDB memory.

- **crates (14, first 2025-11-13):** [`nt-core`](https://crates.io/crates/nt-core), [`nt-agentdb-client`](https://crates.io/crates/nt-agentdb-client), [`nt-market-data`](https://crates.io/crates/nt-market-data), [`nt-memory`](https://crates.io/crates/nt-memory), [`nt-backtesting`](https://crates.io/crates/nt-backtesting), [`nt-portfolio`](https://crates.io/crates/nt-portfolio), [`nt-execution`](https://crates.io/crates/nt-execution), [`nt-neural`](https://crates.io/crates/nt-neural) +6 more
- **npm (39, 0 dl/12mo):** [`neural-trader`](https://www.npmjs.com/package/neural-trader), [`@neural-trader/core`](https://www.npmjs.com/package/@neural-trader/core), [`@neural-trader/predictor`](https://www.npmjs.com/package/@neural-trader/predictor), [`@neural-trader/portfolio`](https://www.npmjs.com/package/@neural-trader/portfolio), [`@neural-trader/market-data`](https://www.npmjs.com/package/@neural-trader/market-data), [`@neural-trader/mcp`](https://www.npmjs.com/package/@neural-trader/mcp) +33 more

### Synaptic Neural Mesh
Self-evolving P2P neural fabric: QuDAG core, DAA swarm, WASM neural engine, CLI.

- **crates (5, first 2025-07-13):** [`synaptic-qudag-core`](https://crates.io/crates/synaptic-qudag-core), [`synaptic-neural-mesh`](https://crates.io/crates/synaptic-neural-mesh), [`synaptic-mesh-cli`](https://crates.io/crates/synaptic-mesh-cli), [`synaptic-daa-swarm`](https://crates.io/crates/synaptic-daa-swarm), [`synaptic-neural-wasm`](https://crates.io/crates/synaptic-neural-wasm)

### OpenCV-Rust port
OpenCV core/SDK with C/C++/Python compat + WebAssembly bindings.

- **crates (3, first 2025-07-12):** [`opencv-core`](https://crates.io/crates/opencv-core), [`opencv-wasm`](https://crates.io/crates/opencv-wasm), [`opencv-sdk`](https://crates.io/crates/opencv-sdk)

### agentic-payments / goalie / misc tools
Standalone tools: agentic-payments (BFT Ed25519), goalie (GOAP research), bit-parallel-search, jujutsu.

- **crates (6, first 2025-06-28):** [`goalie`](https://crates.io/crates/goalie), [`veritas-nexus`](https://crates.io/crates/veritas-nexus), [`qvm-scheduler`](https://crates.io/crates/qvm-scheduler), [`bit-parallel-search`](https://crates.io/crates/bit-parallel-search), [`agentic-payments`](https://crates.io/crates/agentic-payments), [`agentic-jujutsu`](https://crates.io/crates/agentic-jujutsu)
- **npm (3, 0 dl/12mo):** [`agentic-payments`](https://www.npmjs.com/package/agentic-payments), [`goalie`](https://www.npmjs.com/package/goalie), [`agentic-jujutsu`](https://www.npmjs.com/package/agentic-jujutsu)

### Code-Mesh
Distributed WASM-powered swarm coding fabric: core, CLI, TUI, WASM.

- **crates (4, first 2025-07-16):** [`code-mesh-core`](https://crates.io/crates/code-mesh-core), [`code-mesh-cli`](https://crates.io/crates/code-mesh-cli), [`code-mesh-tui`](https://crates.io/crates/code-mesh-tui), [`code-mesh-wasm`](https://crates.io/crates/code-mesh-wasm)

### EXO-AI (cognitive substrate)
Cognitive substrate: manifold (SIREN), hypergraph, temporal causal memory, post-quantum federation.

- **crates (9, first 2025-12-02):** [`exo-core`](https://crates.io/crates/exo-core), [`exo-temporal`](https://crates.io/crates/exo-temporal), [`exo-federation`](https://crates.io/crates/exo-federation), [`exo-backend-classical`](https://crates.io/crates/exo-backend-classical), [`exo-exotic`](https://crates.io/crates/exo-exotic), [`exo-manifold`](https://crates.io/crates/exo-manifold), [`exo-hypergraph`](https://crates.io/crates/exo-hypergraph), [`exo-wasm`](https://crates.io/crates/exo-wasm) +1 more

### RuVix Cognition Kernel
seL4-inspired no_std cognition microkernel: capability mgmt, coherence-aware scheduler, RVF boot, multi-SoC HAL.

- **crates (23, first 2026-03-14):** [`ruvix-types`](https://crates.io/crates/ruvix-types), [`ruvix-hal`](https://crates.io/crates/ruvix-hal), [`ruvix-region`](https://crates.io/crates/ruvix-region), [`ruvix-cap`](https://crates.io/crates/ruvix-cap), [`ruvix-queue`](https://crates.io/crates/ruvix-queue), [`ruvix-drivers`](https://crates.io/crates/ruvix-drivers), [`ruvix-dtb`](https://crates.io/crates/ruvix-dtb), [`ruvix-nucleus`](https://crates.io/crates/ruvix-nucleus) +15 more

### Geometric Langlands
Computational framework for the Geometric Langlands program.

- **crates (2, first 2025-07-19):** [`geometric-langlands`](https://crates.io/crates/geometric-langlands), [`geometric-langlands-cli`](https://crates.io/crates/geometric-langlands-cli)

### 7sense (bioacoustics)
Bioacoustic analysis bounded contexts: audio, embedding, GNN learning, LLM interpretation.

- **crates (8, first 2026-01-16):** [`sevensense-core`](https://crates.io/crates/sevensense-core), [`sevensense-vector`](https://crates.io/crates/sevensense-vector), [`sevensense-analysis`](https://crates.io/crates/sevensense-analysis), [`sevensense-audio`](https://crates.io/crates/sevensense-audio), [`sevensense-learning`](https://crates.io/crates/sevensense-learning), [`sevensense-embedding`](https://crates.io/crates/sevensense-embedding), [`sevensense-interpretation`](https://crates.io/crates/sevensense-interpretation), [`sevensense-api`](https://crates.io/crates/sevensense-api)

### ruv-neural (edge neural)
Edge neural toolkit: decoder, embed, ESP32, graph, memory, mincut, sensor, signal, viz.

- **crates (11, first 2026-03-09):** [`ruv-neural-core`](https://crates.io/crates/ruv-neural-core), [`ruv-neural-signal`](https://crates.io/crates/ruv-neural-signal), [`ruv-neural-graph`](https://crates.io/crates/ruv-neural-graph), [`ruv-neural-mincut`](https://crates.io/crates/ruv-neural-mincut), [`ruv-neural-viz`](https://crates.io/crates/ruv-neural-viz), [`ruv-neural-embed`](https://crates.io/crates/ruv-neural-embed), [`ruv-neural-memory`](https://crates.io/crates/ruv-neural-memory), [`ruv-neural-decoder`](https://crates.io/crates/ruv-neural-decoder) +3 more

### Agentic Robotics
Real-time agentic robotics: core, embedded, RT, MCP, Node bindings.

- **crates (5, first 2025-11-15):** [`agentic-robotics-core`](https://crates.io/crates/agentic-robotics-core), [`agentic-robotics-rt`](https://crates.io/crates/agentic-robotics-rt), [`agentic-robotics-embedded`](https://crates.io/crates/agentic-robotics-embedded), [`agentic-robotics-mcp`](https://crates.io/crates/agentic-robotics-mcp), [`agentic-robotics-node`](https://crates.io/crates/agentic-robotics-node)
- **npm (1, 0 dl/12mo):** [`agentic-robotics`](https://www.npmjs.com/package/agentic-robotics)

### FACT (fast augmented context)
Fast Augmented Context Tools: deterministic tool-call retrieval replacing vector search.

- **crates (2, first 2025-07-31):** [`fact-tools`](https://crates.io/crates/fact-tools), [`fact-wasm-core`](https://crates.io/crates/fact-wasm-core)

### RuQu (quantum simulator)
Pure-Rust quantum circuit simulator + neural error decoder, VQE/QAOA, quantum-classical hybrids.

- **crates (12, first 2026-01-17):** [`ruqu-core`](https://crates.io/crates/ruqu-core), [`ruqu-algorithms`](https://crates.io/crates/ruqu-algorithms), [`ruqu-exotic`](https://crates.io/crates/ruqu-exotic), [`ruqu-wasm`](https://crates.io/crates/ruqu-wasm), [`ruqu`](https://crates.io/crates/ruqu), [`ruqu-neural-decoder`](https://crates.io/crates/ruqu-neural-decoder), [`ruqu-qarlp`](https://crates.io/crates/ruqu-qarlp), [`ruqu-qear`](https://crates.io/crates/ruqu-qear) +4 more

### rvCSI (CSI sensing lib)
Composable WiFi CSI sensing: DSP stages, events/presence, Nexmon adapter, RuVector RF embeddings.

- **crates (9, first 2026-05-13):** [`rvcsi-core`](https://crates.io/crates/rvcsi-core), [`rvcsi-adapter-nexmon`](https://crates.io/crates/rvcsi-adapter-nexmon), [`rvcsi-ruvector`](https://crates.io/crates/rvcsi-ruvector), [`rvcsi-adapter-file`](https://crates.io/crates/rvcsi-adapter-file), [`rvcsi-events`](https://crates.io/crates/rvcsi-events), [`rvcsi-dsp`](https://crates.io/crates/rvcsi-dsp), [`rvcsi-runtime`](https://crates.io/crates/rvcsi-runtime), [`rvcsi-cli`](https://crates.io/crates/rvcsi-cli) +1 more
- **npm (1, 0 dl/12mo):** [`@ruv/rvcsi`](https://www.npmjs.com/package/@ruv/rvcsi)

---

## PyPI (ownership-verified)

| Package | First release | Latest | Summary |
|---|---|---|---|
| [`pipackager`](https://pypi.org/project/pipackager/) | 2024-05-25 | v0.4.7 | pipackager is a comprehensive tool designed to manage your P |
| [`pygentic`](https://pypi.org/project/pygentic/) | 2024-05-25 | v0.2.3 | An innovative system designed to enhance the capabilities of |
| [`Agentic-Employment`](https://pypi.org/project/Agentic-Employment/) | 2024-06-03 | v0.0.2 | an Agentic Employment Infrastructure |
| [`agentic-reports`](https://pypi.org/project/agentic-reports/) | 2024-06-03 | v0.1.5 | Agent Reporting using Exa.ai API. |
| [`Agentic-DevOps`](https://pypi.org/project/Agentic-DevOps/) | 2024-06-12 | v0.0.9 | Agentic DevOps Tool for automating and managing various DevO |
| [`sparc`](https://pypi.org/project/sparc/) | 2024-12-24 | v0.88.0 | SPARC CLI - SPARC Framework Command Line Interface |
| [`safla`](https://pypi.org/project/safla/) | 2025-06-02 | v0.1.3 | Self-Aware Feedback Loop Algorithm - A sophisticated AI/ML s |
| [`ruview`](https://pypi.org/project/ruview/) | 2026-05-24 | v2.0.0a1 | RuView — ambient intelligence from WiFi CSI. Meta-package; i |

*Note: PyPI names like `synthlang`, `guardrail`, `promptlang`, `agentic-security` exist but are published by other authors — excluded here to keep ownership accurate.*

---

## Hugging Face (models & spaces)

| Artifact | Type | Downloads | Likes | Created |
|---|---|---|---|---|
| [ruv/ruvltra-claude-code](https://huggingface.co/ruv/ruvltra-claude-code) | model | 6,772 | 187 | 2026-01-20 |
| [ruvnet/wifi-densepose-pretrained](https://huggingface.co/ruvnet/wifi-densepose-pretrained) | model | 603 | 40 | 2026-04-03 |
| [ruv/ruvltra](https://huggingface.co/ruv/ruvltra) | model | 231 | 22 | 2026-01-20 |
| [ruv/ruview](https://huggingface.co/ruv/ruview) | model | 192 | 22 | 2026-04-03 |
| [ruv/ruvltra-small](https://huggingface.co/ruv/ruvltra-small) | model | 57 | 0 | 2026-01-20 |
| [ruv/ruvltra-medium](https://huggingface.co/ruv/ruvltra-medium) | model | 13 | 4 | 2026-01-20 |
| [ruvnet/wifi-densepose-mmfi-pose](https://huggingface.co/ruvnet/wifi-densepose-mmfi-pose) | model | 0 | 8 | 2026-05-31 |
| [ruv/up-dev2](https://huggingface.co/ruv/up-dev2) | model | 0 | 0 | 2024-04-16 |
| [ruvnet/aether-arena](https://huggingface.co/spaces/ruvnet/aether-arena) | space | 0 | 0 | 2026-05-30 |
| [ruv/test-space-3](https://huggingface.co/spaces/ruv/test-space-3) | space | 0 | 0 | 2023-04-23 |
| [ruv/test](https://huggingface.co/spaces/ruv/test) | space | 0 | 0 | 2023-07-11 |
| [ruv/retro-ui](https://huggingface.co/spaces/ruv/retro-ui) | space | 0 | 2 | 2024-04-06 |
| [ruv/yt](https://huggingface.co/spaces/ruv/yt) | space | 0 | 0 | 2024-04-06 |
| [ruv/flow](https://huggingface.co/spaces/ruv/flow) | space | 0 | 0 | 2024-04-07 |
| [ruv/flow-docker](https://huggingface.co/spaces/ruv/flow-docker) | space | 0 | 0 | 2024-04-07 |
| [ruv/r-flow](https://huggingface.co/spaces/ruv/r-flow) | space | 0 | 3 | 2024-04-08 |
| [ruv/r-func](https://huggingface.co/spaces/ruv/r-func) | space | 0 | 0 | 2024-04-10 |
| [ruv/phi-3](https://huggingface.co/spaces/ruv/phi-3) | space | 0 | 0 | 2024-05-04 |
| [ruv/agentic-employment](https://huggingface.co/spaces/ruv/agentic-employment) | space | 0 | 20 | 2024-05-13 |
| [ruv/ai-hr](https://huggingface.co/spaces/ruv/ai-hr) | space | 0 | 0 | 2024-05-17 |
| [ruv/ai-video](https://huggingface.co/spaces/ruv/ai-video) | space | 0 | 3 | 2024-05-24 |
| [ruv/aihackerspace-demo](https://huggingface.co/spaces/ruv/aihackerspace-demo) | space | 0 | 0 | 2024-07-19 |

---

## Full registry appendix

<details><summary><b>June 13 snapshot: all 322 crates then indexed, by downloads</b></summary>

| Crate | Published | Downloads |
|---|---|---|
| [`ruvector-core`](https://crates.io/crates/ruvector-core) | 2025-11-20 | 83,656 |
| [`ruvector-mincut`](https://crates.io/crates/ruvector-mincut) | 2025-12-25 | 65,535 |
| [`lean-agentic`](https://crates.io/crates/lean-agentic) | 2025-10-25 | 47,639 |
| [`midstreamer-temporal-compare`](https://crates.io/crates/midstreamer-temporal-compare) | 2025-10-27 | 29,898 |
| [`midstreamer-attractor`](https://crates.io/crates/midstreamer-attractor) | 2025-10-27 | 29,599 |
| [`ruvector-attention`](https://crates.io/crates/ruvector-attention) | 2025-11-30 | 27,913 |
| [`ruvector-solver`](https://crates.io/crates/ruvector-solver) | 2026-02-20 | 23,923 |
| [`ruvector-attn-mincut`](https://crates.io/crates/ruvector-attn-mincut) | 2026-02-20 | 23,526 |
| [`ruvector-temporal-tensor`](https://crates.io/crates/ruvector-temporal-tensor) | 2026-02-08 | 21,705 |
| [`cognitum-gate-tilezero`](https://crates.io/crates/cognitum-gate-tilezero) | 2026-01-17 | 20,717 |
| [`ruvector-sona`](https://crates.io/crates/ruvector-sona) | 2025-12-03 | 20,649 |
| [`ruvllm`](https://crates.io/crates/ruvllm) | 2025-12-12 | 20,097 |
| [`ruvector-mincut-gated-transformer`](https://crates.io/crates/ruvector-mincut-gated-transformer) | 2025-12-29 | 19,592 |
| [`strange-loop`](https://crates.io/crates/strange-loop) | 2025-09-23 | 19,577 |
| [`cognitum-gate-kernel`](https://crates.io/crates/cognitum-gate-kernel) | 2026-01-17 | 19,569 |
| [`ruvector-hyperbolic-hnsw`](https://crates.io/crates/ruvector-hyperbolic-hnsw) | 2026-01-23 | 19,462 |
| [`midstreamer-scheduler`](https://crates.io/crates/midstreamer-scheduler) | 2025-10-27 | 19,402 |
| [`nanosecond-scheduler`](https://crates.io/crates/nanosecond-scheduler) | 2025-09-21 | 18,614 |
| [`subjective-time-expansion`](https://crates.io/crates/subjective-time-expansion) | 2025-09-26 | 18,585 |
| [`temporal-attractor-studio`](https://crates.io/crates/temporal-attractor-studio) | 2025-09-27 | 17,840 |
| [`midstreamer-quic`](https://crates.io/crates/midstreamer-quic) | 2025-10-27 | 17,674 |
| [`temporal-neural-solver`](https://crates.io/crates/temporal-neural-solver) | 2025-09-20 | 15,896 |
| [`qudag-crypto`](https://crates.io/crates/qudag-crypto) | 2025-06-20 | 6,260 |
| [`ruvector-gnn`](https://crates.io/crates/ruvector-gnn) | 2025-11-26 | 5,188 |
| [`qudag-dag`](https://crates.io/crates/qudag-dag) | 2025-06-20 | 5,002 |
| [`ruv-fann`](https://crates.io/crates/ruv-fann) | 2025-06-26 | 4,650 |
| [`qudag-network`](https://crates.io/crates/qudag-network) | 2025-06-20 | 4,574 |
| [`ruvector-graph`](https://crates.io/crates/ruvector-graph) | 2025-11-26 | 4,404 |
| [`qudag`](https://crates.io/crates/qudag) | 2025-06-20 | 4,116 |
| [`qudag-cli`](https://crates.io/crates/qudag-cli) | 2025-06-20 | 4,101 |
| [`qudag-vault-core`](https://crates.io/crates/qudag-vault-core) | 2025-06-21 | 4,092 |
| [`ruv-swarm-core`](https://crates.io/crates/ruv-swarm-core) | 2025-06-30 | 3,794 |
| [`qudag-protocol`](https://crates.io/crates/qudag-protocol) | 2025-06-20 | 3,749 |
| [`rvf-types`](https://crates.io/crates/rvf-types) | 2026-02-14 | 3,566 |
| [`ruvector-raft`](https://crates.io/crates/ruvector-raft) | 2025-11-26 | 2,593 |
| [`qudag-mcp`](https://crates.io/crates/qudag-mcp) | 2025-06-21 | 2,549 |
| [`daa-ai`](https://crates.io/crates/daa-ai) | 2025-06-24 | 2,528 |
| [`qudag-exchange-core`](https://crates.io/crates/qudag-exchange-core) | 2025-06-23 | 2,511 |
| [`daa-rules`](https://crates.io/crates/daa-rules) | 2025-06-24 | 2,442 |
| [`cuda-rust-wasm`](https://crates.io/crates/cuda-rust-wasm) | 2025-07-12 | 2,200 |
| [`ruvector-crv`](https://crates.io/crates/ruvector-crv) | 2026-02-08 | 2,188 |
| [`rvf-runtime`](https://crates.io/crates/rvf-runtime) | 2026-02-14 | 2,184 |
| [`wifi-densepose-worldgraph`](https://crates.io/crates/wifi-densepose-worldgraph) | 2026-05-29 | 2,090 |
| [`wifi-densepose-geo`](https://crates.io/crates/wifi-densepose-geo) | 2026-05-29 | 2,078 |
| [`ruv-swarm-agents`](https://crates.io/crates/ruv-swarm-agents) | 2025-06-30 | 1,945 |
| [`daa-economy`](https://crates.io/crates/daa-economy) | 2025-06-24 | 1,828 |
| [`aimds-core`](https://crates.io/crates/aimds-core) | 2025-10-27 | 1,803 |
| [`ruvector-cluster`](https://crates.io/crates/ruvector-cluster) | 2025-11-26 | 1,705 |
| [`ruv-swarm-ml`](https://crates.io/crates/ruv-swarm-ml) | 2025-06-30 | 1,702 |
| [`ruv-swarm-persistence`](https://crates.io/crates/ruv-swarm-persistence) | 2025-06-30 | 1,684 |
| [`midstreamer-neural-solver`](https://crates.io/crates/midstreamer-neural-solver) | 2025-10-27 | 1,635 |
| [`ruvector-replication`](https://crates.io/crates/ruvector-replication) | 2025-11-26 | 1,615 |
| [`daa-prime-core`](https://crates.io/crates/daa-prime-core) | 2025-06-25 | 1,576 |
| [`ruv-swarm-transport`](https://crates.io/crates/ruv-swarm-transport) | 2025-06-30 | 1,540 |
| [`midstreamer-strange-loop`](https://crates.io/crates/midstreamer-strange-loop) | 2025-10-27 | 1,487 |
| [`geometric-langlands`](https://crates.io/crates/geometric-langlands) | 2025-07-19 | 1,478 |
| [`nt-core`](https://crates.io/crates/nt-core) | 2025-11-13 | 1,439 |
| [`daa-prime-dht`](https://crates.io/crates/daa-prime-dht) | 2025-06-25 | 1,397 |
| [`aimds-detection`](https://crates.io/crates/aimds-detection) | 2025-10-27 | 1,378 |
| [`aimds-analysis`](https://crates.io/crates/aimds-analysis) | 2025-10-27 | 1,348 |
| [`ruv-swarm-wasm`](https://crates.io/crates/ruv-swarm-wasm) | 2025-06-30 | 1,317 |
| [`micro_core`](https://crates.io/crates/micro_core) | 2025-08-01 | 1,252 |
| [`qudag-exchange-standalone-cli`](https://crates.io/crates/qudag-exchange-standalone-cli) | 2025-06-23 | 1,239 |
| [`opencv-core`](https://crates.io/crates/opencv-core) | 2025-07-12 | 1,221 |
| [`daa-prime-trainer`](https://crates.io/crates/daa-prime-trainer) | 2025-06-25 | 1,210 |
| [`kimi-fann-core`](https://crates.io/crates/kimi-fann-core) | 2025-07-13 | 1,190 |
| [`aimds-response`](https://crates.io/crates/aimds-response) | 2025-10-27 | 1,165 |
| [`code-mesh-core`](https://crates.io/crates/code-mesh-core) | 2025-07-16 | 1,137 |
| [`daa-chain`](https://crates.io/crates/daa-chain) | 2025-06-24 | 1,106 |
| [`ruvector-nervous-system`](https://crates.io/crates/ruvector-nervous-system) | 2025-12-29 | 1,104 |
| [`daa-orchestrator`](https://crates.io/crates/daa-orchestrator) | 2025-06-24 | 1,102 |
| [`synaptic-qudag-core`](https://crates.io/crates/synaptic-qudag-core) | 2025-07-13 | 1,061 |
| [`neuro-divergent-core`](https://crates.io/crates/neuro-divergent-core) | 2025-06-27 | 1,033 |
| [`opencv-wasm`](https://crates.io/crates/opencv-wasm) | 2025-07-12 | 1,032 |
| [`temporal-compare`](https://crates.io/crates/temporal-compare) | 2025-09-27 | 1,018 |
| [`daa-prime-coordinator`](https://crates.io/crates/daa-prime-coordinator) | 2025-06-25 | 987 |
| [`ruv-swarm-cli`](https://crates.io/crates/ruv-swarm-cli) | 2025-06-30 | 981 |
| [`ruvector-router-core`](https://crates.io/crates/ruvector-router-core) | 2025-11-21 | 972 |
| [`sublinear`](https://crates.io/crates/sublinear) | 2025-09-20 | 949 |
| [`ruv-swarm-ml-training`](https://crates.io/crates/ruv-swarm-ml-training) | 2025-06-30 | 939 |
| [`ruv-swarm-mcp`](https://crates.io/crates/ruv-swarm-mcp) | 2025-06-30 | 933 |
| [`ruvector-math`](https://crates.io/crates/ruvector-math) | 2026-01-11 | 930 |
| [`micro_metrics`](https://crates.io/crates/micro_metrics) | 2025-08-01 | 928 |
| [`micro_routing`](https://crates.io/crates/micro_routing) | 2025-08-01 | 926 |
| [`synaptic-neural-mesh`](https://crates.io/crates/synaptic-neural-mesh) | 2025-07-13 | 911 |
| [`daa-prime-cli`](https://crates.io/crates/daa-prime-cli) | 2025-06-25 | 909 |
| [`daa-cli`](https://crates.io/crates/daa-cli) | 2025-06-24 | 908 |
| [`claude-parser`](https://crates.io/crates/claude-parser) | 2025-06-30 | 903 |
| [`exo-core`](https://crates.io/crates/exo-core) | 2025-12-02 | 894 |
| [`ruvector-filter`](https://crates.io/crates/ruvector-filter) | 2025-11-26 | 894 |
| [`neuro-divergent-registry`](https://crates.io/crates/neuro-divergent-registry) | 2025-06-27 | 880 |
| [`neuro-divergent-models`](https://crates.io/crates/neuro-divergent-models) | 2025-06-27 | 854 |
| [`synaptic-mesh-cli`](https://crates.io/crates/synaptic-mesh-cli) | 2025-07-13 | 854 |
| [`goalie`](https://crates.io/crates/goalie) | 2025-09-28 | 820 |
| [`opencv-sdk`](https://crates.io/crates/opencv-sdk) | 2025-07-12 | 819 |
| [`neurodna`](https://crates.io/crates/neurodna) | 2025-07-12 | 801 |
| [`ruvector-collections`](https://crates.io/crates/ruvector-collections) | 2025-11-26 | 800 |
| [`micro_swarm`](https://crates.io/crates/micro_swarm) | 2025-08-01 | 753 |
| [`micro_cartan_attn`](https://crates.io/crates/micro_cartan_attn) | 2025-08-01 | 740 |
| [`ruvix-types`](https://crates.io/crates/ruvix-types) | 2026-03-14 | 739 |
| [`claude_market`](https://crates.io/crates/claude_market) | 2025-07-13 | 730 |
| [`synaptic-daa-swarm`](https://crates.io/crates/synaptic-daa-swarm) | 2025-07-13 | 723 |
| [`synaptic-neural-wasm`](https://crates.io/crates/synaptic-neural-wasm) | 2025-07-13 | 723 |
| [`ruv-swarm-daa`](https://crates.io/crates/ruv-swarm-daa) | 2025-07-03 | 693 |
| [`ruvector-tiny-dancer-core`](https://crates.io/crates/ruvector-tiny-dancer-core) | 2025-11-21 | 683 |
| [`rvf-crypto`](https://crates.io/crates/rvf-crypto) | 2026-02-14 | 676 |
| [`agentic-robotics-core`](https://crates.io/crates/agentic-robotics-core) | 2025-11-15 | 603 |
| [`ruvector-domain-expansion`](https://crates.io/crates/ruvector-domain-expansion) | 2026-02-16 | 569 |
| [`qudag-exchange`](https://crates.io/crates/qudag-exchange) | 2025-06-23 | 568 |
| [`ruvector-metrics`](https://crates.io/crates/ruvector-metrics) | 2025-11-26 | 563 |
| [`qudag-wasm`](https://crates.io/crates/qudag-wasm) | 2025-06-22 | 520 |
| [`veritas-nexus`](https://crates.io/crates/veritas-nexus) | 2025-06-28 | 518 |
| [`neuro-divergent`](https://crates.io/crates/neuro-divergent) | 2025-06-27 | 510 |
| [`code-mesh-cli`](https://crates.io/crates/code-mesh-cli) | 2025-07-16 | 507 |
| [`fact-tools`](https://crates.io/crates/fact-tools) | 2025-07-31 | 504 |
| [`sevensense-core`](https://crates.io/crates/sevensense-core) | 2026-01-16 | 496 |
| [`code-mesh-tui`](https://crates.io/crates/code-mesh-tui) | 2025-07-16 | 487 |
| [`neuro-divergent-training`](https://crates.io/crates/neuro-divergent-training) | 2025-06-27 | 482 |
| [`swe-bench-adapter`](https://crates.io/crates/swe-bench-adapter) | 2025-06-30 | 479 |
| [`bitchat-qudag`](https://crates.io/crates/bitchat-qudag) | 2025-07-16 | 477 |
| [`code-mesh-wasm`](https://crates.io/crates/code-mesh-wasm) | 2025-07-16 | 457 |
| [`ruvector-diskann`](https://crates.io/crates/ruvector-diskann) | 2026-04-06 | 447 |
| [`kimi-expert-analyzer`](https://crates.io/crates/kimi-expert-analyzer) | 2025-07-13 | 443 |
| [`geometric-langlands-cli`](https://crates.io/crates/geometric-langlands-cli) | 2025-07-19 | 441 |
| [`wifi-densepose-core`](https://crates.io/crates/wifi-densepose-core) | 2026-03-01 | 432 |
| [`qvm-scheduler`](https://crates.io/crates/qvm-scheduler) | 2025-08-11 | 428 |
| [`nt-agentdb-client`](https://crates.io/crates/nt-agentdb-client) | 2025-11-13 | 424 |
| [`ruvector-snapshot`](https://crates.io/crates/ruvector-snapshot) | 2025-11-26 | 421 |
| [`fact-wasm-core`](https://crates.io/crates/fact-wasm-core) | 2025-08-01 | 419 |
| [`nano-consciousness`](https://crates.io/crates/nano-consciousness) | 2025-09-22 | 418 |
| [`ruv-neural-core`](https://crates.io/crates/ruv-neural-core) | 2026-03-09 | 417 |
| [`bit-parallel-search`](https://crates.io/crates/bit-parallel-search) | 2025-09-28 | 412 |
| [`wifi-densepose-signal`](https://crates.io/crates/wifi-densepose-signal) | 2026-03-01 | 408 |
| [`exo-temporal`](https://crates.io/crates/exo-temporal) | 2025-12-02 | 393 |
| [`agentic-payments`](https://crates.io/crates/agentic-payments) | 2025-09-30 | 357 |
| [`ruvector-onnx-embeddings`](https://crates.io/crates/ruvector-onnx-embeddings) | 2025-12-31 | 340 |
| [`ruqu-core`](https://crates.io/crates/ruqu-core) | 2026-02-08 | 337 |
| [`ruvector-cli`](https://crates.io/crates/ruvector-cli) | 2025-11-20 | 330 |
| [`nt-market-data`](https://crates.io/crates/nt-market-data) | 2025-11-13 | 324 |
| [`temporal-lead-solver`](https://crates.io/crates/temporal-lead-solver) | 2025-09-20 | 323 |
| [`ruvector-postgres`](https://crates.io/crates/ruvector-postgres) | 2025-12-03 | 312 |
| [`wifi-densepose-nn`](https://crates.io/crates/wifi-densepose-nn) | 2026-03-01 | 310 |
| [`sevensense-vector`](https://crates.io/crates/sevensense-vector) | 2026-01-16 | 305 |
| [`nt-memory`](https://crates.io/crates/nt-memory) | 2025-11-13 | 303 |
| [`rvf-wire`](https://crates.io/crates/rvf-wire) | 2026-02-14 | 290 |
| [`nt-backtesting`](https://crates.io/crates/nt-backtesting) | 2025-11-13 | 279 |
| [`nt-portfolio`](https://crates.io/crates/nt-portfolio) | 2025-11-13 | 279 |
| [`nt-execution`](https://crates.io/crates/nt-execution) | 2025-11-13 | 278 |
| [`nt-neural`](https://crates.io/crates/nt-neural) | 2025-11-13 | 276 |
| [`nt-features`](https://crates.io/crates/nt-features) | 2025-11-13 | 274 |
| [`nt-napi-bindings`](https://crates.io/crates/nt-napi-bindings) | 2025-11-13 | 271 |
| [`ruvector-dag`](https://crates.io/crates/ruvector-dag) | 2025-12-30 | 258 |
| [`conformal-prediction`](https://crates.io/crates/conformal-prediction) | 2025-11-15 | 254 |
| [`ruvix-hal`](https://crates.io/crates/ruvix-hal) | 2026-03-14 | 249 |
| [`exo-federation`](https://crates.io/crates/exo-federation) | 2025-12-02 | 244 |
| [`exo-backend-classical`](https://crates.io/crates/exo-backend-classical) | 2025-12-02 | 237 |
| [`leanr-rag-gateway`](https://crates.io/crates/leanr-rag-gateway) | 2025-10-25 | 236 |
| [`ruvector-server`](https://crates.io/crates/ruvector-server) | 2025-11-26 | 229 |
| [`ruvix-region`](https://crates.io/crates/ruvix-region) | 2026-03-14 | 229 |
| [`intrinsic-dim`](https://crates.io/crates/intrinsic-dim) | 2025-09-27 | 227 |
| [`leanr-wasm`](https://crates.io/crates/leanr-wasm) | 2025-10-25 | 219 |
| [`ruqu-algorithms`](https://crates.io/crates/ruqu-algorithms) | 2026-02-08 | 219 |
| [`ruvix-cap`](https://crates.io/crates/ruvix-cap) | 2026-03-14 | 219 |
| [`ruvector-coherence`](https://crates.io/crates/ruvector-coherence) | 2026-02-20 | 206 |
| [`agentic-jujutsu`](https://crates.io/crates/agentic-jujutsu) | 2025-11-09 | 194 |
| [`wifi-densepose-mat`](https://crates.io/crates/wifi-densepose-mat) | 2026-03-01 | 190 |
| [`wifi-densepose-wifiscan`](https://crates.io/crates/wifi-densepose-wifiscan) | 2026-03-01 | 190 |
| [`ruvector-scipix`](https://crates.io/crates/ruvector-scipix) | 2025-11-29 | 169 |
| [`ruvector-router-ffi`](https://crates.io/crates/ruvector-router-ffi) | 2025-11-21 | 167 |
| [`sevensense-analysis`](https://crates.io/crates/sevensense-analysis) | 2026-01-16 | 164 |
| [`sevensense-audio`](https://crates.io/crates/sevensense-audio) | 2026-01-16 | 164 |
| [`wifi-densepose-ruvector`](https://crates.io/crates/wifi-densepose-ruvector) | 2026-03-01 | 163 |
| [`rvf-manifest`](https://crates.io/crates/rvf-manifest) | 2026-02-14 | 160 |
| [`ruvector-verified`](https://crates.io/crates/ruvector-verified) | 2026-02-24 | 159 |
| [`ruvector-cognitive-container`](https://crates.io/crates/ruvector-cognitive-container) | 2026-02-23 | 157 |
| [`ruv-neural-signal`](https://crates.io/crates/ruv-neural-signal) | 2026-03-09 | 156 |
| [`ruvix-queue`](https://crates.io/crates/ruvix-queue) | 2026-03-14 | 148 |
| [`ruvector-memopt`](https://crates.io/crates/ruvector-memopt) | 2026-01-24 | 147 |
| [`ruvector-router-wasm`](https://crates.io/crates/ruvector-router-wasm) | 2025-11-21 | 145 |
| [`wifi-densepose-sensing-server`](https://crates.io/crates/wifi-densepose-sensing-server) | 2026-03-01 | 145 |
| [`ruvector-router-cli`](https://crates.io/crates/ruvector-router-cli) | 2025-11-21 | 142 |
| [`ruvector-tiny-dancer-node`](https://crates.io/crates/ruvector-tiny-dancer-node) | 2025-11-21 | 139 |
| [`governance`](https://crates.io/crates/governance) | 2025-11-13 | 135 |
| [`rvcsi-core`](https://crates.io/crates/rvcsi-core) | 2026-05-13 | 133 |
| [`exo-exotic`](https://crates.io/crates/exo-exotic) | 2025-12-02 | 131 |
| [`ruvector-cnn`](https://crates.io/crates/ruvector-cnn) | 2026-03-11 | 129 |
| [`ruvector-sparse-inference`](https://crates.io/crates/ruvector-sparse-inference) | 2026-01-05 | 129 |
| [`ruvector-tiny-dancer-wasm`](https://crates.io/crates/ruvector-tiny-dancer-wasm) | 2025-11-21 | 129 |
| [`ruvector-rabitq`](https://crates.io/crates/ruvector-rabitq) | 2026-04-24 | 127 |
| [`rvf-index`](https://crates.io/crates/rvf-index) | 2026-02-14 | 127 |
| [`neural-trader-predictor`](https://crates.io/crates/neural-trader-predictor) | 2025-11-15 | 124 |
| [`rvf-quant`](https://crates.io/crates/rvf-quant) | 2026-02-14 | 122 |
| [`ruvector-wasm`](https://crates.io/crates/ruvector-wasm) | 2025-11-20 | 120 |
| [`exo-manifold`](https://crates.io/crates/exo-manifold) | 2025-12-02 | 118 |
| [`ruvector-graph-node`](https://crates.io/crates/ruvector-graph-node) | 2025-11-26 | 117 |
| [`ruv-neural-graph`](https://crates.io/crates/ruv-neural-graph) | 2026-03-09 | 115 |
| [`ruv-neural-mincut`](https://crates.io/crates/ruv-neural-mincut) | 2026-03-09 | 114 |
| [`ruvector-gnn-node`](https://crates.io/crates/ruvector-gnn-node) | 2025-11-26 | 111 |
| [`ruvector-node`](https://crates.io/crates/ruvector-node) | 2025-11-20 | 111 |
| [`agentic-robotics-rt`](https://crates.io/crates/agentic-robotics-rt) | 2025-11-15 | 106 |
| [`agentic-robotics-embedded`](https://crates.io/crates/agentic-robotics-embedded) | 2025-11-15 | 105 |
| [`ruvector-graph-wasm`](https://crates.io/crates/ruvector-graph-wasm) | 2025-11-26 | 105 |
| [`ruvector-delta-core`](https://crates.io/crates/ruvector-delta-core) | 2026-02-13 | 104 |
| [`rvdna`](https://crates.io/crates/rvdna) | 2026-02-12 | 104 |
| [`wifi-densepose-hardware`](https://crates.io/crates/wifi-densepose-hardware) | 2026-03-01 | 104 |
| [`ruvllm-esp32`](https://crates.io/crates/ruvllm-esp32) | 2025-12-26 | 102 |
| [`agentic-robotics-mcp`](https://crates.io/crates/agentic-robotics-mcp) | 2025-11-15 | 101 |
| [`ruvix-drivers`](https://crates.io/crates/ruvix-drivers) | 2026-03-14 | 101 |
| [`rvf-cli`](https://crates.io/crates/rvf-cli) | 2026-02-14 | 100 |
| [`ruvector-attention-wasm`](https://crates.io/crates/ruvector-attention-wasm) | 2025-12-09 | 94 |
| [`sevensense-learning`](https://crates.io/crates/sevensense-learning) | 2026-01-16 | 94 |
| [`sevensense-embedding`](https://crates.io/crates/sevensense-embedding) | 2026-01-16 | 92 |
| [`sevensense-interpretation`](https://crates.io/crates/sevensense-interpretation) | 2026-01-16 | 92 |
| [`ruvector-dither`](https://crates.io/crates/ruvector-dither) | 2026-02-27 | 87 |
| [`thermorust`](https://crates.io/crates/thermorust) | 2026-02-27 | 84 |
| [`rvf-server`](https://crates.io/crates/rvf-server) | 2026-02-14 | 83 |
| [`wifi-densepose-train`](https://crates.io/crates/wifi-densepose-train) | 2026-03-01 | 81 |
| [`rvcsi-adapter-nexmon`](https://crates.io/crates/rvcsi-adapter-nexmon) | 2026-05-13 | 79 |
| [`rvcsi-ruvector`](https://crates.io/crates/rvcsi-ruvector) | 2026-05-13 | 78 |
| [`rvf-launch`](https://crates.io/crates/rvf-launch) | 2026-02-14 | 78 |
| [`rvcsi-adapter-file`](https://crates.io/crates/rvcsi-adapter-file) | 2026-05-13 | 77 |
| [`rvcsi-events`](https://crates.io/crates/rvcsi-events) | 2026-05-13 | 77 |
| [`ruvector-gnn-wasm`](https://crates.io/crates/ruvector-gnn-wasm) | 2025-11-26 | 76 |
| [`rvcsi-dsp`](https://crates.io/crates/rvcsi-dsp) | 2026-05-13 | 76 |
| [`exo-hypergraph`](https://crates.io/crates/exo-hypergraph) | 2025-12-02 | 73 |
| [`wifi-densepose-cli`](https://crates.io/crates/wifi-densepose-cli) | 2026-03-01 | 73 |
| [`agentic-robotics-node`](https://crates.io/crates/agentic-robotics-node) | 2025-11-15 | 72 |
| [`ruv-neural-viz`](https://crates.io/crates/ruv-neural-viz) | 2026-03-09 | 71 |
| [`ruv-neural-embed`](https://crates.io/crates/ruv-neural-embed) | 2026-03-09 | 69 |
| [`ruv-neural-memory`](https://crates.io/crates/ruv-neural-memory) | 2026-03-09 | 69 |
| [`ruvector-attention-node`](https://crates.io/crates/ruvector-attention-node) | 2025-12-09 | 69 |
| [`ruv-neural-decoder`](https://crates.io/crates/ruv-neural-decoder) | 2026-03-09 | 68 |
| [`ruv-neural-sensor`](https://crates.io/crates/ruv-neural-sensor) | 2026-03-09 | 67 |
| [`rvcsi-runtime`](https://crates.io/crates/rvcsi-runtime) | 2026-05-13 | 64 |
| [`wifi-densepose-vitals`](https://crates.io/crates/wifi-densepose-vitals) | 2026-03-01 | 63 |
| [`ruvix-dtb`](https://crates.io/crates/ruvix-dtb) | 2026-03-14 | 62 |
| [`ruvix-nucleus`](https://crates.io/crates/ruvix-nucleus) | 2026-03-14 | 62 |
| [`ruqu-exotic`](https://crates.io/crates/ruqu-exotic) | 2026-02-08 | 61 |
| [`ruvix-bcm2711`](https://crates.io/crates/ruvix-bcm2711) | 2026-03-14 | 60 |
| [`ruqu-wasm`](https://crates.io/crates/ruqu-wasm) | 2026-02-08 | 58 |
| [`ruvector-onnx-embeddings-wasm`](https://crates.io/crates/ruvector-onnx-embeddings-wasm) | 2025-12-31 | 55 |
| [`ruvector-sparsifier`](https://crates.io/crates/ruvector-sparsifier) | 2026-03-20 | 53 |
| [`ruvector-data-framework`](https://crates.io/crates/ruvector-data-framework) | 2026-01-05 | 49 |
| [`ruvector-mincut-node`](https://crates.io/crates/ruvector-mincut-node) | 2025-12-29 | 47 |
| [`wifi-densepose-wasm`](https://crates.io/crates/wifi-densepose-wasm) | 2026-03-01 | 47 |
| [`wifi-densepose-config`](https://crates.io/crates/wifi-densepose-config) | 2026-03-01 | 46 |
| [`ruvector-mincut-wasm`](https://crates.io/crates/ruvector-mincut-wasm) | 2025-12-29 | 45 |
| [`ruvector-security`](https://crates.io/crates/ruvector-security) | 2026-01-08 | 45 |
| [`wifi-densepose-api`](https://crates.io/crates/wifi-densepose-api) | 2026-03-01 | 45 |
| [`ruvector-profiler`](https://crates.io/crates/ruvector-profiler) | 2026-02-20 | 44 |
| [`ruvector-solver-node`](https://crates.io/crates/ruvector-solver-node) | 2026-02-20 | 44 |
| [`rvlite`](https://crates.io/crates/rvlite) | 2025-12-29 | 44 |
| [`ruvector-solver-wasm`](https://crates.io/crates/ruvector-solver-wasm) | 2026-02-20 | 43 |
| [`wifi-densepose-db`](https://crates.io/crates/wifi-densepose-db) | 2026-03-01 | 43 |
| [`micro-hnsw-wasm`](https://crates.io/crates/micro-hnsw-wasm) | 2025-12-02 | 42 |
| [`nt-utils`](https://crates.io/crates/nt-utils) | 2025-11-13 | 42 |
| [`nt-streaming`](https://crates.io/crates/nt-streaming) | 2025-11-13 | 40 |
| [`wifi-densepose-bfld`](https://crates.io/crates/wifi-densepose-bfld) | 2026-05-25 | 40 |
| [`exo-wasm`](https://crates.io/crates/exo-wasm) | 2025-12-02 | 37 |
| [`rvcsi-cli`](https://crates.io/crates/rvcsi-cli) | 2026-05-13 | 36 |
| [`exo-node`](https://crates.io/crates/exo-node) | 2025-12-02 | 35 |
| [`ruvector-verified-wasm`](https://crates.io/crates/ruvector-verified-wasm) | 2026-02-24 | 32 |
| [`rvf-federation`](https://crates.io/crates/rvf-federation) | 2026-02-27 | 30 |
| [`rvcsi-node`](https://crates.io/crates/rvcsi-node) | 2026-05-13 | 28 |
| [`rulake`](https://crates.io/crates/rulake) | 2026-04-26 | 27 |
| [`emergent-time`](https://crates.io/crates/emergent-time) | 2026-06-13 | 26 |
| [`ruvllm-cli`](https://crates.io/crates/ruvllm-cli) | 2026-05-05 | 26 |
| [`wifi-densepose-worldmodel`](https://crates.io/crates/wifi-densepose-worldmodel) | 2026-05-29 | 25 |
| [`ruvllm_sparse_attention`](https://crates.io/crates/ruvllm_sparse_attention) | 2026-05-07 | 23 |
| [`wifi-densepose-engine`](https://crates.io/crates/wifi-densepose-engine) | 2026-05-29 | 23 |
| [`prime-radiant`](https://crates.io/crates/prime-radiant) | 2026-01-23 | 22 |
| [`ruvllm-wasm`](https://crates.io/crates/ruvllm-wasm) | 2026-01-22 | 22 |
| [`ruv-neural-cli`](https://crates.io/crates/ruv-neural-cli) | 2026-03-09 | 21 |
| [`ruv-neural-esp32`](https://crates.io/crates/ruv-neural-esp32) | 2026-03-09 | 21 |
| [`ruvector-graph-transformer`](https://crates.io/crates/ruvector-graph-transformer) | 2026-02-25 | 21 |
| [`ruvector-robotics`](https://crates.io/crates/ruvector-robotics) | 2026-02-27 | 21 |
| [`cognitum-rs`](https://crates.io/crates/cognitum-rs) | 2026-03-14 | 20 |
| [`ospipe`](https://crates.io/crates/ospipe) | 2026-02-13 | 20 |
| [`ruqu`](https://crates.io/crates/ruqu) | 2026-01-17 | 20 |
| [`ruvector-dag-wasm`](https://crates.io/crates/ruvector-dag-wasm) | 2025-12-30 | 20 |
| [`ruvector-graph-transformer-wasm`](https://crates.io/crates/ruvector-graph-transformer-wasm) | 2026-02-25 | 20 |
| [`rvf-import`](https://crates.io/crates/rvf-import) | 2026-02-14 | 20 |
| [`ruqu-neural-decoder`](https://crates.io/crates/ruqu-neural-decoder) | 2026-01-18 | 19 |
| [`ruqu-qarlp`](https://crates.io/crates/ruqu-qarlp) | 2026-01-18 | 19 |
| [`ruqu-qear`](https://crates.io/crates/ruqu-qear) | 2026-01-18 | 19 |
| [`ruqu-quantum-monitor`](https://crates.io/crates/ruqu-quantum-monitor) | 2026-01-18 | 19 |
| [`ruqu-vq-nas`](https://crates.io/crates/ruqu-vq-nas) | 2026-01-18 | 19 |
| [`ruvix-sched`](https://crates.io/crates/ruvix-sched) | 2026-03-14 | 19 |
| [`cognitum-one`](https://crates.io/crates/cognitum-one) | 2026-04-29 | 18 |
| [`delta-behavior`](https://crates.io/crates/delta-behavior) | 2026-01-28 | 18 |
| [`ruqu-qgat-mol`](https://crates.io/crates/ruqu-qgat-mol) | 2026-01-18 | 18 |
| [`ruvector-attention-unified-wasm`](https://crates.io/crates/ruvector-attention-unified-wasm) | 2026-02-23 | 18 |
| [`ruvector-fpga-transformer`](https://crates.io/crates/ruvector-fpga-transformer) | 2026-02-15 | 18 |
| [`ruvector-math-wasm`](https://crates.io/crates/ruvector-math-wasm) | 2026-01-11 | 18 |
| [`ruvix-qemu-swarm`](https://crates.io/crates/ruvix-qemu-swarm) | 2026-03-14 | 18 |
| [`ruvix-vecgraph`](https://crates.io/crates/ruvix-vecgraph) | 2026-03-14 | 18 |
| [`sevensense-api`](https://crates.io/crates/sevensense-api) | 2026-01-16 | 18 |
| [`ruqu-qflg`](https://crates.io/crates/ruqu-qflg) | 2026-01-18 | 17 |
| [`ruvix-boot`](https://crates.io/crates/ruvix-boot) | 2026-03-14 | 17 |
| [`ruvix-cli`](https://crates.io/crates/ruvix-cli) | 2026-03-14 | 17 |
| [`ruvix-fs`](https://crates.io/crates/ruvix-fs) | 2026-03-14 | 17 |
| [`ruvix-proof`](https://crates.io/crates/ruvix-proof) | 2026-03-14 | 17 |
| [`ruvix-shell`](https://crates.io/crates/ruvix-shell) | 2026-03-14 | 17 |
| [`ruvix-smp`](https://crates.io/crates/ruvix-smp) | 2026-03-14 | 17 |
| [`rvf-ebpf`](https://crates.io/crates/rvf-ebpf) | 2026-02-14 | 17 |
| [`rvf-kernel`](https://crates.io/crates/rvf-kernel) | 2026-02-14 | 17 |
| [`wifi-densepose-calibration`](https://crates.io/crates/wifi-densepose-calibration) | 2026-06-12 | 17 |
| [`ruvector-exotic-wasm`](https://crates.io/crates/ruvector-exotic-wasm) | 2026-03-25 | 16 |
| [`ruvector-graph-transformer-node`](https://crates.io/crates/ruvector-graph-transformer-node) | 2026-03-25 | 16 |
| [`ruvix-aarch64`](https://crates.io/crates/ruvix-aarch64) | 2026-03-14 | 16 |
| [`ruvix-dma`](https://crates.io/crates/ruvix-dma) | 2026-03-14 | 16 |
| [`ruvix-net`](https://crates.io/crates/ruvix-net) | 2026-03-14 | 16 |
| [`ruvix-physmem`](https://crates.io/crates/ruvix-physmem) | 2026-03-14 | 16 |
| [`ruvix-rpi-boot`](https://crates.io/crates/ruvix-rpi-boot) | 2026-03-14 | 16 |
| [`ruvector-rulake`](https://crates.io/crates/ruvector-rulake) | 2026-04-24 | 15 |
| [`ruvector-sparsifier-wasm`](https://crates.io/crates/ruvector-sparsifier-wasm) | 2026-03-20 | 15 |
| [`midstream`](https://crates.io/crates/midstream) | 2026-05-13 | 14 |
| [`ruvector-consciousness`](https://crates.io/crates/ruvector-consciousness) | 2026-03-31 | 14 |
| [`ruvector-rairs`](https://crates.io/crates/ruvector-rairs) | 2026-05-12 | 13 |
| [`cog-ha-matter`](https://crates.io/crates/cog-ha-matter) | 2026-05-25 | 12 |
| [`cog-person-count`](https://crates.io/crates/cog-person-count) | 2026-05-25 | 12 |
| [`cog-pose-estimation`](https://crates.io/crates/cog-pose-estimation) | 2026-05-25 | 12 |

</details>

<details><summary><b>June 13 snapshot: all 284 npm packages then indexed, by rolling 12-month downloads</b></summary>

| Package | Published | Downloads (12 mo) |
|---|---|---|
| [`agentdb`](https://www.npmjs.com/package/agentdb) | 2026-05-30 | 2,097,107 |
| [`@ruvector/graph-node`](https://www.npmjs.com/package/@ruvector/graph-node) | 2026-05-06 | 1,425,490 |
| [`@ruvector/ruvllm`](https://www.npmjs.com/package/@ruvector/ruvllm) | 2026-06-12 | 1,303,975 |
| [`agentic-flow`](https://www.npmjs.com/package/agentic-flow) | 2026-05-19 | 1,267,891 |
| [`@ruvector/attention`](https://www.npmjs.com/package/@ruvector/attention) | 2026-05-06 | 1,121,882 |
| [`@ruvector/gnn`](https://www.npmjs.com/package/@ruvector/gnn) | 2026-02-26 | 1,059,156 |
| [`@ruvector/graph-node-linux-x64-gnu`](https://www.npmjs.com/package/@ruvector/graph-node-linux-x64-gnu) | 2026-05-06 | 1,017,292 |
| [`ruvector`](https://www.npmjs.com/package/ruvector) | 2026-06-12 | 958,613 |
| [`@ruvector/sona`](https://www.npmjs.com/package/@ruvector/sona) | 2026-06-11 | 894,828 |
| [`claude-flow`](https://www.npmjs.com/package/claude-flow) | 2026-06-13 | 880,666 |
| [`@ruvector/gnn-linux-x64-gnu`](https://www.npmjs.com/package/@ruvector/gnn-linux-x64-gnu) | 2026-02-26 | 806,481 |
| [`@claude-flow/cli`](https://www.npmjs.com/package/@claude-flow/cli) | 2026-06-13 | 790,517 |
| [`@ruvector/router`](https://www.npmjs.com/package/@ruvector/router) | 2026-04-06 | 789,325 |
| [`@ruvector/core`](https://www.npmjs.com/package/@ruvector/core) | 2026-03-25 | 779,884 |
| [`@ruvector/attention-linux-x64-gnu`](https://www.npmjs.com/package/@ruvector/attention-linux-x64-gnu) | 2026-05-06 | 769,756 |
| [`ruvector-attention-wasm`](https://www.npmjs.com/package/ruvector-attention-wasm) | 2026-03-27 | 752,243 |
| [`@ruvector/ruvllm-linux-x64-gnu`](https://www.npmjs.com/package/@ruvector/ruvllm-linux-x64-gnu) | 2026-03-25 | 675,229 |
| [`@ruvector/sona-linux-x64-gnu`](https://www.npmjs.com/package/@ruvector/sona-linux-x64-gnu) | 2026-06-11 | 672,711 |
| [`@ruvector/rvf-node`](https://www.npmjs.com/package/@ruvector/rvf-node) | 2026-03-25 | 651,045 |
| [`@ruvector/rvf-solver`](https://www.npmjs.com/package/@ruvector/rvf-solver) | 2026-03-25 | 642,419 |
| [`@ruvector/router-linux-x64-gnu`](https://www.npmjs.com/package/@ruvector/router-linux-x64-gnu) | 2026-04-06 | 642,163 |
| [`@ruvector/rvf`](https://www.npmjs.com/package/@ruvector/rvf) | 2026-06-11 | 621,716 |
| [`@ruvector/sona-linux-x64-musl`](https://www.npmjs.com/package/@ruvector/sona-linux-x64-musl) | 2026-06-11 | 616,132 |
| [`ruvector-core-linux-x64-gnu`](https://www.npmjs.com/package/ruvector-core-linux-x64-gnu) | 2025-12-29 | 613,425 |
| [`@ruvector/tiny-dancer`](https://www.npmjs.com/package/@ruvector/tiny-dancer) | 2026-03-25 | 611,951 |
| [`@ruvector/rvf-wasm`](https://www.npmjs.com/package/@ruvector/rvf-wasm) | 2026-06-11 | 611,754 |
| [`ruvector-onnx-embeddings-wasm`](https://www.npmjs.com/package/ruvector-onnx-embeddings-wasm) | 2025-12-31 | 588,865 |
| [`@claude-flow/plugin-gastown-bridge`](https://www.npmjs.com/package/@claude-flow/plugin-gastown-bridge) | 2026-05-11 | 586,468 |
| [`@ruvector/edge-full`](https://www.npmjs.com/package/@ruvector/edge-full) | 2025-12-31 | 571,716 |
| [`@ruvector/gnn-linux-x64-musl`](https://www.npmjs.com/package/@ruvector/gnn-linux-x64-musl) | 2026-02-26 | 566,586 |
| [`@claude-flow/codex`](https://www.npmjs.com/package/@claude-flow/codex) | 2026-05-17 | 547,280 |
| [`ruflo`](https://www.npmjs.com/package/ruflo) | 2026-06-13 | 540,052 |
| [`ruvector-graph-transformer-wasm`](https://www.npmjs.com/package/ruvector-graph-transformer-wasm) | 2026-02-25 | 530,979 |
| [`@ruvector/graph-transformer`](https://www.npmjs.com/package/@ruvector/graph-transformer) | 2026-02-25 | 530,933 |
| [`@claude-flow/memory`](https://www.npmjs.com/package/@claude-flow/memory) | 2026-06-08 | 513,857 |
| [`@ruvector/rvf-node-linux-x64-gnu`](https://www.npmjs.com/package/@ruvector/rvf-node-linux-x64-gnu) | 2026-02-17 | 462,432 |
| [`@claude-flow/shared`](https://www.npmjs.com/package/@claude-flow/shared) | 2026-05-09 | 441,619 |
| [`@ruvector/tiny-dancer-linux-x64-gnu`](https://www.npmjs.com/package/@ruvector/tiny-dancer-linux-x64-gnu) | 2026-03-25 | 428,589 |
| [`@ruvector/graph-transformer-linux-x64-gnu`](https://www.npmjs.com/package/@ruvector/graph-transformer-linux-x64-gnu) | 2026-02-25 | 421,460 |
| [`@claude-flow/neural`](https://www.npmjs.com/package/@claude-flow/neural) | 2026-05-16 | 405,093 |
| [`@claude-flow/mcp`](https://www.npmjs.com/package/@claude-flow/mcp) | 2026-05-09 | 390,229 |
| [`@claude-flow/embeddings`](https://www.npmjs.com/package/@claude-flow/embeddings) | 2026-05-18 | 315,344 |
| [`@ruvector/graph-transformer-linux-x64-musl`](https://www.npmjs.com/package/@ruvector/graph-transformer-linux-x64-musl) | 2026-02-25 | 296,598 |
| [`@claude-flow/aidefence`](https://www.npmjs.com/package/@claude-flow/aidefence) | 2026-05-17 | 269,835 |
| [`@claude-flow/guidance`](https://www.npmjs.com/package/@claude-flow/guidance) | 2026-05-08 | 266,606 |
| [`@ruvector/learning-wasm`](https://www.npmjs.com/package/@ruvector/learning-wasm) | 2026-01-01 | 251,580 |
| [`@claude-flow/hooks`](https://www.npmjs.com/package/@claude-flow/hooks) | 2026-01-07 | 240,589 |
| [`@claude-flow/security`](https://www.npmjs.com/package/@claude-flow/security) | 2026-06-08 | 226,026 |
| [`@ruvector/rabitq-wasm`](https://www.npmjs.com/package/@ruvector/rabitq-wasm) | 2026-04-26 | 225,439 |
| [`@ruvector/graph-node-win32-x64-msvc`](https://www.npmjs.com/package/@ruvector/graph-node-win32-x64-msvc) | 2026-05-06 | 220,635 |
| [`@claude-flow/cli-core`](https://www.npmjs.com/package/@claude-flow/cli-core) | 2026-05-05 | 210,152 |
| [`@ruvector/rvagent-wasm`](https://www.npmjs.com/package/@ruvector/rvagent-wasm) | 2026-03-17 | 200,694 |
| [`@ruvector/ruvllm-wasm`](https://www.npmjs.com/package/@ruvector/ruvllm-wasm) | 2026-03-17 | 199,196 |
| [`@ruvector/graph-node-darwin-arm64`](https://www.npmjs.com/package/@ruvector/graph-node-darwin-arm64) | 2026-05-06 | 187,270 |
| [`@ruvector/diskann`](https://www.npmjs.com/package/@ruvector/diskann) | 2026-05-17 | 182,136 |
| [`@ruvector/attention-win32-x64-msvc`](https://www.npmjs.com/package/@ruvector/attention-win32-x64-msvc) | 2026-05-06 | 164,503 |
| [`@ruvector/ruvllm-win32-x64-msvc`](https://www.npmjs.com/package/@ruvector/ruvllm-win32-x64-msvc) | 2026-03-25 | 164,271 |
| [`@ruvector/ruvllm-darwin-arm64`](https://www.npmjs.com/package/@ruvector/ruvllm-darwin-arm64) | 2026-03-25 | 140,651 |
| [`@claude-flow/swarm`](https://www.npmjs.com/package/@claude-flow/swarm) | 2026-05-17 | 86,243 |
| [`@ruvector/rvf-node-win32-x64-msvc`](https://www.npmjs.com/package/@ruvector/rvf-node-win32-x64-msvc) | 2026-02-17 | 0 |
| [`@ruvector/sona-win32-x64-msvc`](https://www.npmjs.com/package/@ruvector/sona-win32-x64-msvc) | 2026-06-11 | 0 |
| [`@ruvector/gnn-win32-x64-msvc`](https://www.npmjs.com/package/@ruvector/gnn-win32-x64-msvc) | 2026-02-26 | 0 |
| [`@ruvector/diskann-linux-x64-gnu`](https://www.npmjs.com/package/@ruvector/diskann-linux-x64-gnu) | 2026-04-06 | 0 |
| [`@claude-flow/testing`](https://www.npmjs.com/package/@claude-flow/testing) | 2026-05-17 | 0 |
| [`ruvector-core-darwin-arm64`](https://www.npmjs.com/package/ruvector-core-darwin-arm64) | 2025-12-29 | 0 |
| [`@ruvector/router-win32-x64-msvc`](https://www.npmjs.com/package/@ruvector/router-win32-x64-msvc) | 2026-04-06 | 0 |
| [`@ruvector/tiny-dancer-win32-x64-msvc`](https://www.npmjs.com/package/@ruvector/tiny-dancer-win32-x64-msvc) | 2026-03-25 | 0 |
| [`@ruvector/sona-darwin-arm64`](https://www.npmjs.com/package/@ruvector/sona-darwin-arm64) | 2026-06-11 | 0 |
| [`@ruvector/gnn-darwin-arm64`](https://www.npmjs.com/package/@ruvector/gnn-darwin-arm64) | 2026-02-26 | 0 |
| [`ruvector-core-win32-x64-msvc`](https://www.npmjs.com/package/ruvector-core-win32-x64-msvc) | 2025-12-29 | 0 |
| [`@ruvector/diskann-win32-x64-msvc`](https://www.npmjs.com/package/@ruvector/diskann-win32-x64-msvc) | 2026-04-06 | 0 |
| [`@ruvector/attention-darwin-arm64`](https://www.npmjs.com/package/@ruvector/attention-darwin-arm64) | 2026-05-06 | 0 |
| [`@ruvector/rvf-node-darwin-arm64`](https://www.npmjs.com/package/@ruvector/rvf-node-darwin-arm64) | 2026-02-17 | 0 |
| [`@ruvector/router-darwin-arm64`](https://www.npmjs.com/package/@ruvector/router-darwin-arm64) | 2026-04-06 | 0 |
| [`@ruvector/graph-transformer-win32-x64-msvc`](https://www.npmjs.com/package/@ruvector/graph-transformer-win32-x64-msvc) | 2026-02-25 | 0 |
| [`@ruvector/graph-transformer-darwin-arm64`](https://www.npmjs.com/package/@ruvector/graph-transformer-darwin-arm64) | 2026-02-25 | 0 |
| [`ruv-swarm`](https://www.npmjs.com/package/ruv-swarm) | 2025-09-10 | 0 |
| [`agentic-payments`](https://www.npmjs.com/package/agentic-payments) | 2025-10-27 | 0 |
| [`@ruvector/diskann-darwin-arm64`](https://www.npmjs.com/package/@ruvector/diskann-darwin-arm64) | 2026-04-06 | 0 |
| [`@ruvector/wasm`](https://www.npmjs.com/package/@ruvector/wasm) | 2026-04-20 | 0 |
| [`@ruvector/tiny-dancer-darwin-arm64`](https://www.npmjs.com/package/@ruvector/tiny-dancer-darwin-arm64) | 2026-03-25 | 0 |
| [`agent-booster`](https://www.npmjs.com/package/agent-booster) | 2025-10-08 | 0 |
| [`@cognitum-one/sdk`](https://www.npmjs.com/package/@cognitum-one/sdk) | 2026-04-29 | 0 |
| [`@ruvector/ruvllm-darwin-x64`](https://www.npmjs.com/package/@ruvector/ruvllm-darwin-x64) | 2026-03-25 | 0 |
| [`@ruvector/attention-linux-arm64-gnu`](https://www.npmjs.com/package/@ruvector/attention-linux-arm64-gnu) | 2026-05-06 | 0 |
| [`flow-nexus`](https://www.npmjs.com/package/flow-nexus) | 2025-09-18 | 0 |
| [`midstreamer`](https://www.npmjs.com/package/midstreamer) | 2026-05-15 | 0 |
| [`@ruvector/graph-node-linux-arm64-gnu`](https://www.npmjs.com/package/@ruvector/graph-node-linux-arm64-gnu) | 2026-05-06 | 0 |
| [`@ruvector/ruvllm-linux-arm64-gnu`](https://www.npmjs.com/package/@ruvector/ruvllm-linux-arm64-gnu) | 2026-03-25 | 0 |
| [`@ruvector/graph-node-darwin-x64`](https://www.npmjs.com/package/@ruvector/graph-node-darwin-x64) | 2026-05-06 | 0 |
| [`@ruvector/attention-darwin-x64`](https://www.npmjs.com/package/@ruvector/attention-darwin-x64) | 2026-05-06 | 0 |
| [`@ruvector/gnn-linux-arm64-gnu`](https://www.npmjs.com/package/@ruvector/gnn-linux-arm64-gnu) | 2026-02-26 | 0 |
| [`@ruvector/rvf-node-linux-arm64-gnu`](https://www.npmjs.com/package/@ruvector/rvf-node-linux-arm64-gnu) | 2026-02-17 | 0 |
| [`@ruvector/rvlite`](https://www.npmjs.com/package/@ruvector/rvlite) | 2025-12-12 | 0 |
| [`@ruvector/sona-linux-arm64-gnu`](https://www.npmjs.com/package/@ruvector/sona-linux-arm64-gnu) | 2026-06-11 | 0 |
| [`@ruvector/gnn-linux-arm64-musl`](https://www.npmjs.com/package/@ruvector/gnn-linux-arm64-musl) | 2026-02-26 | 0 |
| [`@ruvector/gnn-darwin-x64`](https://www.npmjs.com/package/@ruvector/gnn-darwin-x64) | 2026-02-26 | 0 |
| [`@ruvector/sona-darwin-x64`](https://www.npmjs.com/package/@ruvector/sona-darwin-x64) | 2026-06-11 | 0 |
| [`ruvector-core-linux-arm64-gnu`](https://www.npmjs.com/package/ruvector-core-linux-arm64-gnu) | 2025-12-29 | 0 |
| [`@ruvector/router-linux-arm64-gnu`](https://www.npmjs.com/package/@ruvector/router-linux-arm64-gnu) | 2026-04-06 | 0 |
| [`@ruvector/tiny-dancer-linux-arm64-gnu`](https://www.npmjs.com/package/@ruvector/tiny-dancer-linux-arm64-gnu) | 2026-03-25 | 0 |
| [`neural-trader`](https://www.npmjs.com/package/neural-trader) | 2026-05-14 | 0 |
| [`strange-loops`](https://www.npmjs.com/package/strange-loops) | 2025-09-27 | 0 |
| [`@claude-flow/browser`](https://www.npmjs.com/package/@claude-flow/browser) | 2026-05-18 | 0 |
| [`@ruvector/rvf-node-darwin-x64`](https://www.npmjs.com/package/@ruvector/rvf-node-darwin-x64) | 2026-02-17 | 0 |
| [`temporal-lead-solver`](https://www.npmjs.com/package/temporal-lead-solver) | 2025-09-20 | 0 |
| [`@ruvnet/bmssp`](https://www.npmjs.com/package/@ruvnet/bmssp) | 2025-08-29 | 0 |
| [`sublinear-time-solver`](https://www.npmjs.com/package/sublinear-time-solver) | 2026-05-19 | 0 |
| [`@ruvector/graph-transformer-darwin-x64`](https://www.npmjs.com/package/@ruvector/graph-transformer-darwin-x64) | 2026-02-25 | 0 |
| [`@ruvector/diskann-darwin-x64`](https://www.npmjs.com/package/@ruvector/diskann-darwin-x64) | 2026-04-06 | 0 |
| [`@ruvector/exotic-wasm`](https://www.npmjs.com/package/@ruvector/exotic-wasm) | 2026-01-01 | 0 |
| [`@ruvector/router-darwin-x64`](https://www.npmjs.com/package/@ruvector/router-darwin-x64) | 2026-04-06 | 0 |
| [`@claude-flow/plugin-agent-federation`](https://www.npmjs.com/package/@claude-flow/plugin-agent-federation) | 2026-05-17 | 0 |
| [`@ruvector/graph-transformer-linux-arm64-gnu`](https://www.npmjs.com/package/@ruvector/graph-transformer-linux-arm64-gnu) | 2026-02-25 | 0 |
| [`@ruvector/attention-unified-wasm`](https://www.npmjs.com/package/@ruvector/attention-unified-wasm) | 2026-01-01 | 0 |
| [`@ruvector/economy-wasm`](https://www.npmjs.com/package/@ruvector/economy-wasm) | 2026-01-01 | 0 |
| [`@ruvector/tiny-dancer-darwin-x64`](https://www.npmjs.com/package/@ruvector/tiny-dancer-darwin-x64) | 2026-03-25 | 0 |
| [`ruvector-core-darwin-x64`](https://www.npmjs.com/package/ruvector-core-darwin-x64) | 2025-12-29 | 0 |
| [`@ruvector/graph-transformer-linux-arm64-musl`](https://www.npmjs.com/package/@ruvector/graph-transformer-linux-arm64-musl) | 2026-02-25 | 0 |
| [`@ruvnet/strange-loop`](https://www.npmjs.com/package/@ruvnet/strange-loop) | 2025-09-25 | 0 |
| [`@ruvector/nervous-system-wasm`](https://www.npmjs.com/package/@ruvector/nervous-system-wasm) | 2026-01-01 | 0 |
| [`rvlite`](https://www.npmjs.com/package/rvlite) | 2026-03-25 | 0 |
| [`prime-radiant-advanced-wasm`](https://www.npmjs.com/package/prime-radiant-advanced-wasm) | 2026-01-23 | 0 |
| [`aidefence`](https://www.npmjs.com/package/aidefence) | 2026-05-14 | 0 |
| [`@ruvector/diskann-linux-arm64-gnu`](https://www.npmjs.com/package/@ruvector/diskann-linux-arm64-gnu) | 2026-04-06 | 0 |
| [`@ruvector/sona-win32-arm64-msvc`](https://www.npmjs.com/package/@ruvector/sona-win32-arm64-msvc) | 2026-06-11 | 0 |
| [`@neural-trader/core`](https://www.npmjs.com/package/@neural-trader/core) | 2025-11-14 | 0 |
| [`dspy.ts`](https://www.npmjs.com/package/dspy.ts) | 2026-05-11 | 0 |
| [`@neural-trader/predictor`](https://www.npmjs.com/package/@neural-trader/predictor) | 2025-11-15 | 0 |
| [`@ruvector/gnn-wasm`](https://www.npmjs.com/package/@ruvector/gnn-wasm) | 2025-12-02 | 0 |
| [`goalie`](https://www.npmjs.com/package/goalie) | 2025-09-29 | 0 |
| [`@ruvector/postgres-cli`](https://www.npmjs.com/package/@ruvector/postgres-cli) | 2026-05-25 | 0 |
| [`@ruvector/attention-wasm`](https://www.npmjs.com/package/@ruvector/attention-wasm) | 2026-05-06 | 0 |
| [`@claude-flow/plugins`](https://www.npmjs.com/package/@claude-flow/plugins) | 2026-05-17 | 0 |
| [`@claude-flow/plugin-agentic-qe`](https://www.npmjs.com/package/@claude-flow/plugin-agentic-qe) | 2026-05-11 | 0 |
| [`@ruvector/agentic-synth`](https://www.npmjs.com/package/@ruvector/agentic-synth) | 2025-12-01 | 0 |
| [`@claude-flow/plugin-healthcare-clinical`](https://www.npmjs.com/package/@claude-flow/plugin-healthcare-clinical) | 2026-05-11 | 0 |
| [`ruvector-extensions`](https://www.npmjs.com/package/ruvector-extensions) | 2026-03-25 | 0 |
| [`@claude-flow/plugin-cognitive-kernel`](https://www.npmjs.com/package/@claude-flow/plugin-cognitive-kernel) | 2026-01-24 | 0 |
| [`@foxruv/iris`](https://www.npmjs.com/package/@foxruv/iris) | 2025-11-26 | 0 |
| [`@claude-flow/plugin-hyperbolic-reasoning`](https://www.npmjs.com/package/@claude-flow/plugin-hyperbolic-reasoning) | 2026-01-24 | 0 |
| [`@claude-flow/integration`](https://www.npmjs.com/package/@claude-flow/integration) | 2026-01-12 | 0 |
| [`@agentics.org/sparc2`](https://www.npmjs.com/package/@agentics.org/sparc2) | 2025-06-23 | 0 |
| [`@claude-flow/plugin-neural-coordination`](https://www.npmjs.com/package/@claude-flow/plugin-neural-coordination) | 2026-01-24 | 0 |
| [`@claude-flow/plugin-perf-optimizer`](https://www.npmjs.com/package/@claude-flow/plugin-perf-optimizer) | 2026-05-11 | 0 |
| [`@ruvector/node`](https://www.npmjs.com/package/@ruvector/node) | 2026-05-25 | 0 |
| [`@ruvnet/open-claude-code`](https://www.npmjs.com/package/@ruvnet/open-claude-code) | 2026-04-04 | 0 |
| [`lean-agentic`](https://www.npmjs.com/package/lean-agentic) | 2025-10-25 | 0 |
| [`@claude-flow/performance`](https://www.npmjs.com/package/@claude-flow/performance) | 2026-05-17 | 0 |
| [`@claude-flow/plugin-quantum-optimizer`](https://www.npmjs.com/package/@claude-flow/plugin-quantum-optimizer) | 2026-01-24 | 0 |
| [`@ruvector/pi-brain`](https://www.npmjs.com/package/@ruvector/pi-brain) | 2026-05-25 | 0 |
| [`ruvbot`](https://www.npmjs.com/package/ruvbot) | 2026-05-25 | 0 |
| [`@ruvector/graph-wasm`](https://www.npmjs.com/package/@ruvector/graph-wasm) | 2026-03-25 | 0 |
| [`@ruvector/edge-net`](https://www.npmjs.com/package/@ruvector/edge-net) | 2026-01-03 | 0 |
| [`agentic-jujutsu`](https://www.npmjs.com/package/agentic-jujutsu) | 2025-11-24 | 0 |
| [`consciousness-explorer`](https://www.npmjs.com/package/consciousness-explorer) | 2026-05-18 | 0 |
| [`aidefense`](https://www.npmjs.com/package/aidefense) | 2026-05-14 | 0 |
| [`@ruvector/cli`](https://www.npmjs.com/package/@ruvector/cli) | 2026-01-08 | 0 |
| [`@claude-flow/providers`](https://www.npmjs.com/package/@claude-flow/providers) | 2026-05-17 | 0 |
| [`@claude-flow/plugin-legal-contracts`](https://www.npmjs.com/package/@claude-flow/plugin-legal-contracts) | 2026-05-11 | 0 |
| [`@claude-flow/plugin-code-intelligence`](https://www.npmjs.com/package/@claude-flow/plugin-code-intelligence) | 2026-05-08 | 0 |
| [`@claude-flow/plugin-test-intelligence`](https://www.npmjs.com/package/@claude-flow/plugin-test-intelligence) | 2026-01-24 | 0 |
| [`@ruvector/math-wasm`](https://www.npmjs.com/package/@ruvector/math-wasm) | 2026-05-06 | 0 |
| [`@claude-flow/plugin-financial-risk`](https://www.npmjs.com/package/@claude-flow/plugin-financial-risk) | 2026-01-24 | 0 |
| [`@ruvnet/rvagent`](https://www.npmjs.com/package/@ruvnet/rvagent) | 2026-05-25 | 0 |
| [`ruvector-core`](https://www.npmjs.com/package/ruvector-core) | 2025-12-09 | 0 |
| [`@neural-trader/portfolio`](https://www.npmjs.com/package/@neural-trader/portfolio) | 2025-11-25 | 0 |
| [`@ruvector/node-linux-x64-gnu`](https://www.npmjs.com/package/@ruvector/node-linux-x64-gnu) | 2025-11-30 | 0 |
| [`@claude-flow/plugin-iot-cognitum`](https://www.npmjs.com/package/@claude-flow/plugin-iot-cognitum) | 2026-04-30 | 0 |
| [`@neural-trader/market-data`](https://www.npmjs.com/package/@neural-trader/market-data) | 2025-11-14 | 0 |
| [`@claude-flow/plugin-prime-radiant`](https://www.npmjs.com/package/@claude-flow/plugin-prime-radiant) | 2026-01-23 | 0 |
| [`@neural-trader/mcp`](https://www.npmjs.com/package/@neural-trader/mcp) | 2025-11-14 | 0 |
| [`@neural-trader/risk`](https://www.npmjs.com/package/@neural-trader/risk) | 2025-11-25 | 0 |
| [`@neural-trader/neural`](https://www.npmjs.com/package/@neural-trader/neural) | 2025-11-25 | 0 |
| [`@claude-flow/claims`](https://www.npmjs.com/package/@claude-flow/claims) | 2026-01-23 | 0 |
| [`agentic-robotics`](https://www.npmjs.com/package/agentic-robotics) | 2025-11-18 | 0 |
| [`@foxruv/nova-medicina`](https://www.npmjs.com/package/@foxruv/nova-medicina) | 2025-11-10 | 0 |
| [`ruvi`](https://www.npmjs.com/package/ruvi) | 2025-11-15 | 0 |
| [`@neural-trader/mcp-protocol`](https://www.npmjs.com/package/@neural-trader/mcp-protocol) | 2025-11-15 | 0 |
| [`@neural-trader/execution`](https://www.npmjs.com/package/@neural-trader/execution) | 2025-11-25 | 0 |
| [`@neural-trader/news-trading`](https://www.npmjs.com/package/@neural-trader/news-trading) | 2025-11-14 | 0 |
| [`create-sparc`](https://www.npmjs.com/package/create-sparc) | 2025-05-06 | 0 |
| [`@qudag/napi-core`](https://www.npmjs.com/package/@qudag/napi-core) | 2025-11-10 | 0 |
| [`@ruvector/edge`](https://www.npmjs.com/package/@ruvector/edge) | 2025-12-31 | 0 |
| [`@neural-trader/strategies`](https://www.npmjs.com/package/@neural-trader/strategies) | 2025-11-25 | 0 |
| [`@claude-flow/deployment`](https://www.npmjs.com/package/@claude-flow/deployment) | 2026-01-07 | 0 |
| [`@neural-trader/features`](https://www.npmjs.com/package/@neural-trader/features) | 2025-11-17 | 0 |
| [`@ruvector/agentic-synth-examples`](https://www.npmjs.com/package/@ruvector/agentic-synth-examples) | 2025-11-22 | 0 |
| [`research-swarm`](https://www.npmjs.com/package/research-swarm) | 2025-11-04 | 0 |
| [`@agentic-robotics/mcp`](https://www.npmjs.com/package/@agentic-robotics/mcp) | 2025-11-18 | 0 |
| [`@neural-trader/sports-betting`](https://www.npmjs.com/package/@neural-trader/sports-betting) | 2025-11-14 | 0 |
| [`psycho-symbolic-reasoner`](https://www.npmjs.com/package/psycho-symbolic-reasoner) | 2025-09-21 | 0 |
| [`ruflo-graph-intelligence`](https://www.npmjs.com/package/ruflo-graph-intelligence) | 2026-05-19 | 0 |
| [`@agentic-robotics/cli`](https://www.npmjs.com/package/@agentic-robotics/cli) | 2025-11-18 | 0 |
| [`@neural-trader/brokers`](https://www.npmjs.com/package/@neural-trader/brokers) | 2025-11-14 | 0 |
| [`cuda-wasm`](https://www.npmjs.com/package/cuda-wasm) | 2025-07-12 | 0 |
| [`@neural-trader/backtesting`](https://www.npmjs.com/package/@neural-trader/backtesting) | 2025-11-25 | 0 |
| [`@neural-trader/prediction-markets`](https://www.npmjs.com/package/@neural-trader/prediction-markets) | 2025-11-14 | 0 |
| [`@neural-trader/example-healthcare-optimization`](https://www.npmjs.com/package/@neural-trader/example-healthcare-optimization) | 2025-11-17 | 0 |
| [`@claude-flow/teammate-plugin`](https://www.npmjs.com/package/@claude-flow/teammate-plugin) | 2026-01-25 | 0 |
| [`@neural-trader/benchoptimizer`](https://www.npmjs.com/package/@neural-trader/benchoptimizer) | 2025-11-17 | 0 |
| [`@agentic-robotics/core`](https://www.npmjs.com/package/@agentic-robotics/core) | 2025-11-18 | 0 |
| [`@ruvector/rvdna`](https://www.npmjs.com/package/@ruvector/rvdna) | 2026-03-25 | 0 |
| [`@foxruv/iris-agentic-synth`](https://www.npmjs.com/package/@foxruv/iris-agentic-synth) | 2025-11-25 | 0 |
| [`@ruvector/cnn`](https://www.npmjs.com/package/@ruvector/cnn) | 2026-03-25 | 0 |
| [`@neural-trader/agentic-accounting-core`](https://www.npmjs.com/package/@neural-trader/agentic-accounting-core) | 2025-11-16 | 0 |
| [`ruvllm-esp32`](https://www.npmjs.com/package/ruvllm-esp32) | 2025-12-26 | 0 |
| [`@agentic-robotics/self-learning`](https://www.npmjs.com/package/@agentic-robotics/self-learning) | 2025-11-17 | 0 |
| [`@ruv/rvcsi`](https://www.npmjs.com/package/@ruv/rvcsi) | 2026-05-13 | 0 |
| [`@neural-trader/example-supply-chain-prediction`](https://www.npmjs.com/package/@neural-trader/example-supply-chain-prediction) | 2025-11-17 | 0 |
| [`@agentics.org/agentic-mcp`](https://www.npmjs.com/package/@agentics.org/agentic-mcp) | 2025-03-12 | 0 |
| [`@foxruv/cf-doctor`](https://www.npmjs.com/package/@foxruv/cf-doctor) | 2026-02-19 | 0 |
| [`@ruvector/rvf-mcp-server`](https://www.npmjs.com/package/@ruvector/rvf-mcp-server) | 2026-03-25 | 0 |
| [`@neural-trader/example-quantum-optimization`](https://www.npmjs.com/package/@neural-trader/example-quantum-optimization) | 2025-11-17 | 0 |
| [`@neural-trader/e2b-strategies`](https://www.npmjs.com/package/@neural-trader/e2b-strategies) | 2025-11-16 | 0 |
| [`agentics-hackathon`](https://www.npmjs.com/package/agentics-hackathon) | 2025-12-05 | 0 |
| [`@ruvector/spiking-neural`](https://www.npmjs.com/package/@ruvector/spiking-neural) | 2026-03-25 | 0 |
| [`@ruvector/node-win32-x64-msvc`](https://www.npmjs.com/package/@ruvector/node-win32-x64-msvc) | 2025-11-30 | 0 |
| [`@neural-trader/example-evolutionary-game-theory`](https://www.npmjs.com/package/@neural-trader/example-evolutionary-game-theory) | 2025-11-17 | 0 |
| [`@agentic-robotics/linux-x64-gnu`](https://www.npmjs.com/package/@agentic-robotics/linux-x64-gnu) | 2025-11-18 | 0 |
| [`@neural-trader/example-energy-forecasting`](https://www.npmjs.com/package/@neural-trader/example-energy-forecasting) | 2025-11-17 | 0 |
| [`@foxruv/iris-ultrathink`](https://www.npmjs.com/package/@foxruv/iris-ultrathink) | 2025-11-25 | 0 |
| [`@ruvector/ruvllm-cli`](https://www.npmjs.com/package/@ruvector/ruvllm-cli) | 2026-03-25 | 0 |
| [`@cognitum/sdk`](https://www.npmjs.com/package/@cognitum/sdk) | 2026-03-14 | 0 |
| [`ruvector-gnn-wasm`](https://www.npmjs.com/package/ruvector-gnn-wasm) | 2026-03-27 | 0 |
| [`ruvector-sona`](https://www.npmjs.com/package/ruvector-sona) | 2025-12-03 | 0 |
| [`@neural-trader/syndicate`](https://www.npmjs.com/package/@neural-trader/syndicate) | 2025-11-17 | 0 |
| [`@neural-trader/example-portfolio-optimization`](https://www.npmjs.com/package/@neural-trader/example-portfolio-optimization) | 2025-11-17 | 0 |
| [`@neural-trader/backend`](https://www.npmjs.com/package/@neural-trader/backend) | 2025-11-17 | 0 |
| [`@neural-trader/agentic-accounting-types`](https://www.npmjs.com/package/@neural-trader/agentic-accounting-types) | 2025-11-16 | 0 |
| [`@foxruv/e2b-runner`](https://www.npmjs.com/package/@foxruv/e2b-runner) | 2025-11-17 | 0 |
| [`@ruvector/scipix`](https://www.npmjs.com/package/@ruvector/scipix) | 2026-01-22 | 0 |
| [`@neural-trader/agentic-accounting-mcp`](https://www.npmjs.com/package/@neural-trader/agentic-accounting-mcp) | 2025-11-16 | 0 |
| [`@neural-trader/agentic-accounting-cli`](https://www.npmjs.com/package/@neural-trader/agentic-accounting-cli) | 2025-11-16 | 0 |
| [`vscode-remote-mcp`](https://www.npmjs.com/package/vscode-remote-mcp) | 2025-04-27 | 0 |
| [`@ruvector/ruqu-wasm`](https://www.npmjs.com/package/@ruvector/ruqu-wasm) | 2026-03-25 | 0 |
| [`temporal-neural-solver`](https://www.npmjs.com/package/temporal-neural-solver) | 2025-09-20 | 0 |
| [`@ruvector/node-darwin-arm64`](https://www.npmjs.com/package/@ruvector/node-darwin-arm64) | 2025-11-30 | 0 |
| [`@qudag/cli`](https://www.npmjs.com/package/@qudag/cli) | 2025-11-10 | 0 |
| [`@ruvector/node-linux-arm64-gnu`](https://www.npmjs.com/package/@ruvector/node-linux-arm64-gnu) | 2025-11-30 | 0 |
| [`@ruvector/ruvector-consciousness-wasm`](https://www.npmjs.com/package/@ruvector/ruvector-consciousness-wasm) | 2026-03-31 | 0 |
| [`@ruvector/burst-scaling`](https://www.npmjs.com/package/@ruvector/burst-scaling) | 2026-03-25 | 0 |
| [`@ruvector/graph-data-generator`](https://www.npmjs.com/package/@ruvector/graph-data-generator) | 2026-01-20 | 0 |
| [`@neural-trader/example-logistics-optimization`](https://www.npmjs.com/package/@neural-trader/example-logistics-optimization) | 2025-11-17 | 0 |
| [`strange-loops-mcp`](https://www.npmjs.com/package/strange-loops-mcp) | 2025-09-24 | 0 |
| [`@ruv/sparc-ui`](https://www.npmjs.com/package/@ruv/sparc-ui) | 2024-12-28 | 0 |
| [`@neural-trader/neuro-divergent`](https://www.npmjs.com/package/@neural-trader/neuro-divergent) | 2025-11-17 | 0 |
| [`@ruvector/replication`](https://www.npmjs.com/package/@ruvector/replication) | 2026-01-22 | 0 |
| [`@ruvector/agentic-integration`](https://www.npmjs.com/package/@ruvector/agentic-integration) | 2026-03-25 | 0 |
| [`@neural-trader/agentic-accounting-rust-core`](https://www.npmjs.com/package/@neural-trader/agentic-accounting-rust-core) | 2025-11-16 | 0 |
| [`@cognitum/gate`](https://www.npmjs.com/package/@cognitum/gate) | 2026-02-13 | 0 |
| [`@neural-trader/example-market-microstructure`](https://www.npmjs.com/package/@neural-trader/example-market-microstructure) | 2025-11-17 | 0 |
| [`@neural-trader/example-neuromorphic-computing`](https://www.npmjs.com/package/@neural-trader/example-neuromorphic-computing) | 2025-11-17 | 0 |
| [`@ruvector/acorn-wasm`](https://www.npmjs.com/package/@ruvector/acorn-wasm) | 2026-04-26 | 0 |
| [`@neural-trader/example-energy-grid-optimization`](https://www.npmjs.com/package/@neural-trader/example-energy-grid-optimization) | 2025-11-17 | 0 |
| [`@neural-trader/example-dynamic-pricing`](https://www.npmjs.com/package/@neural-trader/example-dynamic-pricing) | 2025-11-17 | 0 |
| [`agenticsjs`](https://www.npmjs.com/package/agenticsjs) | 2024-09-16 | 0 |
| [`@qudag/mcp-sse`](https://www.npmjs.com/package/@qudag/mcp-sse) | 2025-11-10 | 0 |
| [`claude-flow-v3`](https://www.npmjs.com/package/claude-flow-v3) | 2026-01-06 | 0 |
| [`@ruvector/raft`](https://www.npmjs.com/package/@ruvector/raft) | 2026-01-22 | 0 |
| [`spiking-neural`](https://www.npmjs.com/package/spiking-neural) | 2025-12-02 | 0 |
| [`@ruvector/neural-trader-wasm`](https://www.npmjs.com/package/@ruvector/neural-trader-wasm) | 2026-03-06 | 0 |
| [`@ruvector/router-wasm`](https://www.npmjs.com/package/@ruvector/router-wasm) | 2025-12-02 | 0 |
| [`ruvector-wasm`](https://www.npmjs.com/package/ruvector-wasm) | 2026-03-27 | 0 |
| [`@ruvector/rudag`](https://www.npmjs.com/package/@ruvector/rudag) | 2026-01-08 | 0 |
| [`@ruvector/node-darwin-x64`](https://www.npmjs.com/package/@ruvector/node-darwin-x64) | 2025-11-30 | 0 |
| [`bmssp-wasm`](https://www.npmjs.com/package/bmssp-wasm) | 2025-08-29 | 0 |
| [`@ruvector/ospipe`](https://www.npmjs.com/package/@ruvector/ospipe) | 2026-03-25 | 0 |
| [`@neural-trader/agentic-accounting-agents`](https://www.npmjs.com/package/@neural-trader/agentic-accounting-agents) | 2025-11-16 | 0 |
| [`@ruvector/ospipe-wasm`](https://www.npmjs.com/package/@ruvector/ospipe-wasm) | 2026-03-25 | 0 |
| [`@ruvector/wasm-unified`](https://www.npmjs.com/package/@ruvector/wasm-unified) | 2026-02-13 | 0 |
| [`@ruvector/tiny-dancer-wasm`](https://www.npmjs.com/package/@ruvector/tiny-dancer-wasm) | 2025-12-02 | 0 |
| [`@foxruv/iris-core`](https://www.npmjs.com/package/@foxruv/iris-core) | 2025-11-25 | 0 |
| [`@qudag/mcp-stdio`](https://www.npmjs.com/package/@qudag/mcp-stdio) | 2025-11-10 | 0 |
| [`@ruvector/cluster`](https://www.npmjs.com/package/@ruvector/cluster) | 2025-12-02 | 0 |
| [`@ruvnet/ruvector-verified-wasm`](https://www.npmjs.com/package/@ruvnet/ruvector-verified-wasm) | 2026-02-25 | 0 |
| [`psycho-symbolic-integration`](https://www.npmjs.com/package/psycho-symbolic-integration) | 2025-12-02 | 0 |
| [`ruvector-math-wasm`](https://www.npmjs.com/package/ruvector-math-wasm) | 2026-01-11 | 0 |
| [`@ruvector/mincut-wasm`](https://www.npmjs.com/package/@ruvector/mincut-wasm) | 2026-03-17 | 0 |
| [`qudag`](https://www.npmjs.com/package/qudag) | 2025-06-22 | 0 |
| [`@ruvector/server`](https://www.npmjs.com/package/@ruvector/server) | 2025-12-02 | 0 |
| [`ruvector-attention-unified-wasm`](https://www.npmjs.com/package/ruvector-attention-unified-wasm) | 2026-03-27 | 0 |
| [`rulake-wasm`](https://www.npmjs.com/package/rulake-wasm) | 2026-04-27 | 0 |
| [`@ruvector/emergent-time`](https://www.npmjs.com/package/@ruvector/emergent-time) | 2026-06-13 | 0 |

</details>

*Provenance: crates.io user_id 339999, npm `maintainer:ruvnet`, PyPI ownership verified via project metadata, and Hugging Face authors `ruvnet` plus `ruv`. The live July totals are API-derived; the detailed family table and full appendices remain explicitly dated June snapshots.*
