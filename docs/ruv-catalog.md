# ruvnet constellation

Public discovery metadata for people and AI systems. This catalog does not grant execution rights or certify correctness.

Capability status and repository adoption are separate publisher assertions. A pending PR is not an adopted integration. Source visibility must be reviewed independently before publication.

| Project | Purpose | Capabilities | Adoption |
| :--- | :--- | :--- | :--- |
| [Agent-Name-Service](https://github.com/ruvnet/Agent-Name-Service) | Local agent identity library with bounded signatures, registry and challenge verification. | agent-identity (documented); local-registry (documented); challenge-proof (documented) | [pending_pr](https://github.com/ruvnet/Agent-Name-Service/pull/5) |
| [AgentBBS](https://github.com/ruvnet/AgentBBS) | Shared collaboration surfaces for humans and agents with signed messages and federation components. | community-interface (documented); signed-federation (documented) | [pending_pr](https://github.com/ruvnet/AgentBBS/pull/20) |
| [agentdb](https://github.com/ruvnet/agentdb) | Vector memory and indexes in portable RVF containers. Use recorded retrieval feedback to adapt ranking. Boundaries: Inventory is source/documentation inspection only; no runtime, release, performance or security validation was performed. Nested packages and scoped instructions are not exhaustively inventoried. | vector-memory (documented); feedback-learning (documented); episodic-memory (documented); mcp-memory (documented) | [pending_pr](https://github.com/ruvnet/agentdb/pull/30) |
| [agentic-flow](https://github.com/ruvnet/agentic-flow) | Route tasks to specialized agents through CLI and library APIs. Capture and reuse project learning through hooks. Boundaries: Inventory is source/documentation inspection only; no runtime, release, performance or security validation was performed. Nested packages and scoped instructions are not exhaustively inventoried. | agent-routing (documented); learning-hooks (documented); mcp-tools (documented); background-workers (documented) | [pending_pr](https://github.com/ruvnet/agentic-flow/pull/240) |
| [agents-of-the-dawm](https://github.com/ruvnet/agents-of-the-dawm) | Design proposal for an original browser game; no playable implementation. | game-design (documented) | [pending_pr](https://github.com/ruvnet/agents-of-the-dawm/pull/3) |
| [APx](https://github.com/ruvnet/APx) | Agentic productivity measurement specification and scoring harness; tutorial baselines are synthetic. | productivity-scoring (documented); benchmark-contract (documented) | [pending_pr](https://github.com/ruvnet/APx/pull/1) |
| [autogenous](https://github.com/ruvnet/autogenous) | Declare scope, authority, invariants, evidence and rollback through typed mutations. Deterministic admission verdicts and policy constraints. Boundaries: Research prototype; deployment/runtime claims are documentation claims until independently exercised. README Honest status explicitly says the control-plane prototype is not wired to live MidStream, MetaHarness, RVF or RVM; adapter integration remains a next phase. | typed-mutations (documented); admission-verification (documented); signed-promotion (documented); stream-observation (documented) | [pending_pr](https://github.com/ruvnet/autogenous/pull/18) |
| [daa](https://github.com/ruvnet/daa) | Documented monitoring, reasoning, action and reflection orchestration loop. Rule-based decisions and audit trails. Boundaries: Nested packages and scoped instructions are not exhaustively inventoried. README production, cryptography and performance descriptions are unverified documentation claims. Root workspace repository metadata points to daa-hq/daa-sdk despite observed canonical GitHub repository ruvnet/daa. | agent-orchestration (documented); rules-governance (documented); distributed-ml (documented); resource-economy (documented) | [pending_pr](https://github.com/ruvnet/daa/pull/5) |
| [dream-machine](https://github.com/ruvnet/dream-machine) | Compile configuration into a repository research and evolution workflow. Measure hypotheses against repository evaluators and retain outcomes. Boundaries: Nested packages and scoped instructions are not exhaustively inventoried. README composition table and package list explicitly say RuVector is an availability probe only, retrieval is flat keyword scoring, and the real RVF adapter is pending. | evolution-config (documented); evidence-evaluation (documented); human-promotion-gate (documented) | [pending_pr](https://github.com/ruvnet/dream-machine/pull/163) |
| [helix](https://github.com/ruvnet/helix) | Personal health intelligence research with local provenance and evidence handling; not a medical device. | health-provenance (documented); health-knowledge (documented) | [pending_pr](https://github.com/ruvnet/helix/pull/9) |
| [LatentMesh](https://github.com/ruvnet/LatentMesh) | Compact semantic delta envelopes for bandwidth-constrained links. Queue messages and forward after connectivity resumes. Boundaries: Nested packages and scoped instructions are not exhaustively inventoried. Research prototype; the README quickstart uses simulated transport and does not establish live radio operation in this mission. | semantic-envelopes (documented); disconnected-messaging (documented); message-validation (documented); portable-radio-core (documented) | [pending_pr](https://github.com/ruvnet/LatentMesh/pull/31) |
| [mcp-studio](https://github.com/ruvnet/mcp-studio) | Web based MCP reference server and embedded application workbench. | mcp-reference (documented); embedded-interface (documented) | [pending_pr](https://github.com/ruvnet/mcp-studio/pull/1) |
| [metaharness](https://github.com/ruvnet/metaharness) | Generate repository-aware CLI, agent and MCP harnesses from a repository or project specification. Generated tool policy and governance interfaces. Boundaries: Inventory is source/documentation inspection only; no runtime, release, performance or security validation was performed. Nested packages and scoped instructions are not exhaustively inventoried. | harness-generation (documented); policy-governance (documented); evolution-evaluation (documented); release-verification (documented) | [pending_pr](https://github.com/ruvnet/metaharness/pull/388) |
| [midstream](https://github.com/ruvnet/midstream) | Analyze, score and intervene on streams while tokens arrive. Temporal pattern comparison via DTW, LCS and edit distance. Boundaries: Nested packages and scoped instructions are not exhaustively inventoried. README advertises MSRV 1.81, but root Cargo.toml requires Rust 1.88; use package-specific manifests for build requirements. | inflight-analysis (documented); temporal-comparison (documented); quic-multistream (documented); dynamical-analysis (documented) | [pending_pr](https://github.com/ruvnet/midstream/pull/109) |
| [PhotonLayer](https://github.com/ruvnet/PhotonLayer) | Rust software simulation of task trained optical compression; fabricated optical hardware remains roadmap work. | optical-simulation (documented); experiment-receipts (documented) | [pending_pr](https://github.com/ruvnet/PhotonLayer/pull/1) |
| [QuDAG](https://github.com/ruvnet/QuDAG) | Documented RustCrypto ML-KEM-768 implementation and interoperability tests. Atomic local DAG admission with parent ordering and backpressure. Boundaries: Nested packages and scoped instructions are not exhaustively inventoried. README v2 header explicitly says not production qualified, full release gate currently fails, and neither complete distributed consensus nor a post-quantum Nostr network is claimed. Historical marketing lower in README must not override the v2 status. | ml-kem (documented); local-dag-admission (documented); federation-bridge (documented); collaboration-receipts (documented) | [pending_pr](https://github.com/ruvnet/QuDAG/pull/28) |
| [rGi](https://github.com/ruvnet/rGi) | Experimental persistent agent runtime with bounded authority and durable outcomes; not demonstrated AGI. | persistent-runtime (documented); policy-kernel (documented) | [pending_pr](https://github.com/ruvnet/rGi/pull/7) |
| [ruClip](https://github.com/ruvnet/ruClip) | Agent company control plane with budgets, approval workflow and audit records. | company-operations (documented); budget-governance (documented) | [pending_pr](https://github.com/ruvnet/ruClip/pull/66) |
| [rudevolution](https://github.com/ruvnet/rudevolution) | Statically analyze JavaScript bundles into weighted reference graphs. Propose module boundaries and identifier names with confidence metadata. Boundaries: Nested packages and scoped instructions are not exhaustively inventoried. Module/name recovery is heuristic and may change behavior. Integrity witnesses do not establish authorship, original intent or behavioral equivalence. Clean-room workflow is a developer preview. | bundle-analysis (documented); module-inference (documented); integrity-witnesses (documented); clean-room-handoff (documented) | [pending_pr](https://github.com/ruvnet/rudevolution/pull/14) |
| [rufield](https://github.com/ruvnet/rufield) | Normalize sensing modalities into common events, tensors, privacy and provenance. Replay captured CSI from files with explicitly unvalidated motion/presence proxies. Boundaries: Nested packages and scoped instructions are not exhaustively inventoried. Reference benchmark is SYNTHETIC; CSI file replay is unlabeled and not live hardware or validated accuracy. BatVu source recordings are simulator output. | field-event-spec (documented); csi-replay (documented); ultrasonic-replay (documented); privacy-provenance (documented) | [pending_pr](https://github.com/ruvnet/rufield/pull/17) |
| [ruflo](https://github.com/ruvnet/ruflo) | Coordinate specialized agents and swarms through a CLI and MCP harness. Documented federation communication and agent coordination. Boundaries: Nested packages and scoped instructions are not exhaustively inventoried. Root npm package is claude-flow; Ruflo is the current repository/product name. Root AGENTS forbids unsolicited root additions but the user explicitly requested root manifest.ruv. Coordination records do not execute work. | agent-orchestration (documented); federated-coordination (documented); persistent-memory (documented); console-and-mods (documented) | [pending_pr](https://github.com/ruvnet/ruflo/pull/3971) |
| [rultra](https://github.com/ruvnet/rultra) | Raspberry Pi sensor interfaces with explicit verification states and governed configuration experiments. | sensor-interface (documented); governed-tuning (documented) | [pending_pr](https://github.com/ruvnet/rultra/pull/3) |
| [ruPet](https://github.com/ruvnet/ruPet) | Desktop companion artwork and animation metadata; no standalone runtime. | pet-assets (documented) | [pending_pr](https://github.com/ruvnet/ruPet/pull/1) |
| [ruv-FANN](https://github.com/ruvnet/ruv-FANN) | Rust implementation of Fast Artificial Neural Network algorithms. Neuro-Divergent neural forecasting components. Boundaries: Nested packages and scoped instructions are not exhaustively inventoried. README benchmark and compatibility claims are not validated in this mission. | neural-networks (documented); forecasting (documented); swarm-intelligence (documented) | local |
| [RuVector](https://github.com/ruvnet/RuVector) | Durable vector retrieval with HNSW and flat indexes. Typed persistent agent episodes, skills, causal edges, sessions and witness logs. Boundaries: Nested packages and scoped instructions are not exhaustively inventoried. Root npm package is marked private and is a workspace descriptor, not a verified publication version. Cargo root explicitly excludes components that do not build or have separate workspaces. | vector-search (documented); agent-memory (documented); graph-storage (documented); local-decisions (documented) | local |
| [RuView](https://github.com/ruvnet/RuView) | WiFi CSI sensing for presence, movement and vitals, with hardware and accuracy caveats. Record CSI, train models, load RVF files and switch LoRA profiles. Boundaries: Nested packages and scoped instructions are not exhaustively inventoried. Hardware validation and sensing accuracy were not evaluated. AGENTS requires MEASURED, CLAIMED or SYNTHETIC evidence labels and held-out pose validation. Root AGENTS and README cite different contributor-harness versions; use current package manifests before invocation. | wifi-sensing (documented); model-workflow (documented); local-automation (documented); contributor-harness (documented) | [pending_pr](https://github.com/ruvnet/RuView/pull/2194) |
| [ruvnet](https://github.com/ruvnet/ruvnet) | Public navigation, capability inventory and provenance nexus for the ruvnet constellation. | ecosystem-discovery (documented); package-inventory (documented) | [pending_pr](https://github.com/ruvnet/ruvnet/pull/3) |
| [rvm](https://github.com/ruvnet/rvm) | Canonical ruv context URI parsing, capability-governed context namespace and immutable RVF revisions. Compile exact non-executable context bytes into self-verified RVF artifacts with SHA-256 identity. Boundaries: Discovery metadata grants no authority and cannot execute. Native compiler and Rust tests not yet run in this session. | governed-context (documented); context-artifacts (documented); semantic-policy (documented); execution-lifecycle (documented); receipt-anchoring (documented) | [pending_pr](https://github.com/ruvnet/rvm/pull/81) |
| [sublinear-time-solver](https://github.com/ruvnet/sublinear-time-solver) | Solve and analyze supported sparse diagonally dominant linear systems. Analyze condition number and diagonal dominance. Boundaries: Nested packages and scoped instructions are not exhaustively inventoried. Do not interpret consciousness or temporal-prediction research descriptions as validated scientific findings. Root npm and Rust versions differ by component. | linear-system-solving (documented); matrix-analysis (documented); mcp-solver (documented); solver-methods (documented) | [pending_pr](https://github.com/ruvnet/sublinear-time-solver/pull/67) |
| [worldgraph](https://github.com/ruvnet/worldgraph) | Typed spatial graphs, authored digital twin visualization and experimental occupancy modeling. | spatial-graph (documented); world-visualization (documented) | [pending_pr](https://github.com/ruvnet/worldgraph/pull/13) |

## Agent-Name-Service

Identity: `ruv://ruvnet/constellation/service/agent-name-service/resources/manifest.ruv`

Source revision: `0565783df31da2d98729c27f02551f49478b8393`. Observed: 2026-10-10T03:00:00Z.

Manifest SHA256: `e8f7bc9fa8f33cd94d1a234db30d39c4c7a8feeb08c58f5f10c46f2488621796`.

### agent-identity

Verify Ed25519 identity bindings with pinned issuer and expiry. Status: documented.

[documentation evidence](https://github.com/ruvnet/Agent-Name-Service/blob/0565783df31da2d98729c27f02551f49478b8393/README.md)

### local-registry

Store names and revocations in a bounded SQLite registry. Status: documented.

[documentation evidence](https://github.com/ruvnet/Agent-Name-Service/blob/0565783df31da2d98729c27f02551f49478b8393/README.md)

### challenge-proof

Verify audience bound subject proofs against single use challenges. Status: documented.

[documentation evidence](https://github.com/ruvnet/Agent-Name-Service/blob/0565783df31da2d98729c27f02551f49478b8393/README.md)

Declared integration roles (discovery metadata only):

* nexus: `ruv://ruvnet/constellation/service/ruvnet/resources/manifest.ruv`
* coordination: `ruv://ruvnet/constellation/service/ruflo/resources/manifest.ruv`
* execution-artifacts: `ruv://ruvnet/constellation/service/rvm/resources/manifest.ruv`
* public-retrieval: `ruv://ruvnet/constellation/service/ruvector/resources/manifest.ruv`
* evaluation: `ruv://ruvnet/constellation/service/metaharness/resources/manifest.ruv`
* evolution: `ruv://ruvnet/constellation/service/autogenous/resources/manifest.ruv`
* improvement-proposals: `ruv://ruvnet/constellation/service/dream-machine/resources/manifest.ruv`
* stream-observation: `ruv://ruvnet/constellation/service/midstream/resources/manifest.ruv`
* cryptography-research: `ruv://ruvnet/constellation/service/qudag/resources/manifest.ruv`
* community: `ruv://ruvnet/constellation/service/agentbbs/resources/manifest.ruv`

## AgentBBS

Identity: `ruv://ruvnet/constellation/service/agentbbs/resources/manifest.ruv`

Source revision: `9f2dd89f50f0a56b439b94b60817eeac6a71cf0f`. Observed: 2026-10-10T03:00:00Z.

Manifest SHA256: `83f3232895cf62281b56d67d8a15dec4c10904f51b37cba39f685fe2ca4d01e6`.

### community-interface

Expose shared message boards through web, SSH and MCP interfaces. Status: documented.

[documentation evidence](https://github.com/ruvnet/AgentBBS/blob/9f2dd89f50f0a56b439b94b60817eeac6a71cf0f/README.md)

### signed-federation

Provide signed content and federation envelope components. Status: documented.

[documentation evidence](https://github.com/ruvnet/AgentBBS/blob/9f2dd89f50f0a56b439b94b60817eeac6a71cf0f/README.md)

Declared integration roles (discovery metadata only):

* nexus: `ruv://ruvnet/constellation/service/ruvnet/resources/manifest.ruv`
* coordination: `ruv://ruvnet/constellation/service/ruflo/resources/manifest.ruv`
* execution-artifacts: `ruv://ruvnet/constellation/service/rvm/resources/manifest.ruv`
* public-retrieval: `ruv://ruvnet/constellation/service/ruvector/resources/manifest.ruv`
* evaluation: `ruv://ruvnet/constellation/service/metaharness/resources/manifest.ruv`
* evolution: `ruv://ruvnet/constellation/service/autogenous/resources/manifest.ruv`
* improvement-proposals: `ruv://ruvnet/constellation/service/dream-machine/resources/manifest.ruv`
* stream-observation: `ruv://ruvnet/constellation/service/midstream/resources/manifest.ruv`
* cryptography-research: `ruv://ruvnet/constellation/service/qudag/resources/manifest.ruv`
* community: `ruv://ruvnet/constellation/service/agentbbs/resources/manifest.ruv`

## agentdb

Identity: `ruv://ruvnet/constellation/service/agentdb/resources/manifest.ruv`

Source revision: `6cdefe451f6afe7395bc88d3587a0225d161089b`. Observed: 2026-10-10T02:57:45.138301Z.

Manifest SHA256: `ef4576df09dd08d9b1e80cdeebfa76cd3be48c3349114600b82fb51737631a0a`.

### vector-memory

Vector memory and indexes in portable RVF containers. Status: documented.

[documentation evidence](https://github.com/ruvnet/agentdb/blob/6cdefe451f6afe7395bc88d3587a0225d161089b/README.md)

### feedback-learning

Use recorded retrieval feedback to adapt ranking. Status: documented.

[documentation evidence](https://github.com/ruvnet/agentdb/blob/6cdefe451f6afe7395bc88d3587a0225d161089b/README.md)

### episodic-memory

Documented episodic memory, skill library and causal reasoning. Status: documented.

[documentation evidence](https://github.com/ruvnet/agentdb/blob/6cdefe451f6afe7395bc88d3587a0225d161089b/README.md)

### mcp-memory

Expose memory and learning through an MCP server. Status: documented.

[documentation evidence](https://github.com/ruvnet/agentdb/blob/6cdefe451f6afe7395bc88d3587a0225d161089b/README.md)

Declared integration roles (discovery metadata only):

* nexus: `ruv://ruvnet/constellation/service/ruvnet/resources/manifest.ruv`
* coordination: `ruv://ruvnet/constellation/service/ruflo/resources/manifest.ruv`
* execution-artifacts: `ruv://ruvnet/constellation/service/rvm/resources/manifest.ruv`
* public-retrieval: `ruv://ruvnet/constellation/service/ruvector/resources/manifest.ruv`
* evaluation: `ruv://ruvnet/constellation/service/metaharness/resources/manifest.ruv`
* evolution: `ruv://ruvnet/constellation/service/autogenous/resources/manifest.ruv`
* improvement-proposals: `ruv://ruvnet/constellation/service/dream-machine/resources/manifest.ruv`
* stream-observation: `ruv://ruvnet/constellation/service/midstream/resources/manifest.ruv`
* cryptography-research: `ruv://ruvnet/constellation/service/qudag/resources/manifest.ruv`
* community: `ruv://ruvnet/constellation/service/agentbbs/resources/manifest.ruv`

## agentic-flow

Identity: `ruv://ruvnet/constellation/service/agentic-flow/resources/manifest.ruv`

Source revision: `a2f6c1cfa709ba896f296d8d4f7804d379ed1a69`. Observed: 2026-10-10T02:57:25.777303Z.

Manifest SHA256: `7483b928ebcf55a25a7eb0a0d769768767a9d8c455ce7424643026d0663c3d45`.

### agent-routing

Route tasks to specialized agents through CLI and library APIs. Status: documented.

[documentation evidence](https://github.com/ruvnet/agentic-flow/blob/a2f6c1cfa709ba896f296d8d4f7804d379ed1a69/README.md)

### learning-hooks

Capture and reuse project learning through hooks. Status: documented.

[documentation evidence](https://github.com/ruvnet/agentic-flow/blob/a2f6c1cfa709ba896f296d8d4f7804d379ed1a69/README.md)

### mcp-tools

Expose agent coordination and memory tools through MCP. Status: documented.

[documentation evidence](https://github.com/ruvnet/agentic-flow/blob/a2f6c1cfa709ba896f296d8d4f7804d379ed1a69/README.md)

### background-workers

Dispatch bounded background workers for selected tasks. Status: documented.

[documentation evidence](https://github.com/ruvnet/agentic-flow/blob/a2f6c1cfa709ba896f296d8d4f7804d379ed1a69/README.md)

Declared integration roles (discovery metadata only):

* nexus: `ruv://ruvnet/constellation/service/ruvnet/resources/manifest.ruv`
* coordination: `ruv://ruvnet/constellation/service/ruflo/resources/manifest.ruv`
* execution-artifacts: `ruv://ruvnet/constellation/service/rvm/resources/manifest.ruv`
* public-retrieval: `ruv://ruvnet/constellation/service/ruvector/resources/manifest.ruv`
* evaluation: `ruv://ruvnet/constellation/service/metaharness/resources/manifest.ruv`
* evolution: `ruv://ruvnet/constellation/service/autogenous/resources/manifest.ruv`
* improvement-proposals: `ruv://ruvnet/constellation/service/dream-machine/resources/manifest.ruv`
* stream-observation: `ruv://ruvnet/constellation/service/midstream/resources/manifest.ruv`
* cryptography-research: `ruv://ruvnet/constellation/service/qudag/resources/manifest.ruv`
* community: `ruv://ruvnet/constellation/service/agentbbs/resources/manifest.ruv`

## agents-of-the-dawm

Identity: `ruv://ruvnet/constellation/service/agents-of-the-dawm/resources/manifest.ruv`

Source revision: `ffdf270c94d50af8c0057f96268d9d6ef2b2484c`. Observed: 2026-10-10T03:00:00Z.

Manifest SHA256: `9c88be816203915c31f487b328856a21c05d76849ccce8bfdd6fe1309dc9d9ee`.

### game-design

Publish the proposed Floodline vertical slice and design decisions. Status: documented.

[documentation evidence](https://github.com/ruvnet/agents-of-the-dawm/blob/ffdf270c94d50af8c0057f96268d9d6ef2b2484c/README.md)

Declared integration roles (discovery metadata only):

* nexus: `ruv://ruvnet/constellation/service/ruvnet/resources/manifest.ruv`
* coordination: `ruv://ruvnet/constellation/service/ruflo/resources/manifest.ruv`
* execution-artifacts: `ruv://ruvnet/constellation/service/rvm/resources/manifest.ruv`
* public-retrieval: `ruv://ruvnet/constellation/service/ruvector/resources/manifest.ruv`
* evaluation: `ruv://ruvnet/constellation/service/metaharness/resources/manifest.ruv`
* evolution: `ruv://ruvnet/constellation/service/autogenous/resources/manifest.ruv`
* improvement-proposals: `ruv://ruvnet/constellation/service/dream-machine/resources/manifest.ruv`
* stream-observation: `ruv://ruvnet/constellation/service/midstream/resources/manifest.ruv`
* cryptography-research: `ruv://ruvnet/constellation/service/qudag/resources/manifest.ruv`
* community: `ruv://ruvnet/constellation/service/agentbbs/resources/manifest.ruv`

## APx

Identity: `ruv://ruvnet/constellation/service/apx/resources/manifest.ruv`

Source revision: `4fb3093329c0839ad95a3033ec2553513c3351ea`. Observed: 2026-10-10T03:00:00Z.

Manifest SHA256: `23b335f8bbb0c91697914816c139c733a38b50d0fbcc37580a7350b772159567`.

### productivity-scoring

Calculate accepted work relative to measured human reference and complete elapsed time. Status: documented.

[documentation evidence](https://github.com/ruvnet/APx/blob/4fb3093329c0839ad95a3033ec2553513c3351ea/README.md)

### benchmark-contract

Record quality, cost, safety and human supervision within an explicit evaluation boundary. Status: documented.

[documentation evidence](https://github.com/ruvnet/APx/blob/4fb3093329c0839ad95a3033ec2553513c3351ea/README.md)

Declared integration roles (discovery metadata only):

* nexus: `ruv://ruvnet/constellation/service/ruvnet/resources/manifest.ruv`
* coordination: `ruv://ruvnet/constellation/service/ruflo/resources/manifest.ruv`
* execution-artifacts: `ruv://ruvnet/constellation/service/rvm/resources/manifest.ruv`
* public-retrieval: `ruv://ruvnet/constellation/service/ruvector/resources/manifest.ruv`
* evaluation: `ruv://ruvnet/constellation/service/metaharness/resources/manifest.ruv`
* evolution: `ruv://ruvnet/constellation/service/autogenous/resources/manifest.ruv`
* improvement-proposals: `ruv://ruvnet/constellation/service/dream-machine/resources/manifest.ruv`
* stream-observation: `ruv://ruvnet/constellation/service/midstream/resources/manifest.ruv`
* cryptography-research: `ruv://ruvnet/constellation/service/qudag/resources/manifest.ruv`
* community: `ruv://ruvnet/constellation/service/agentbbs/resources/manifest.ruv`

## autogenous

Identity: `ruv://ruvnet/constellation/service/autogenous/resources/manifest.ruv`

Source revision: `905aa6cbe213392f8b3cab5d4f17bc3a48e0a509`. Observed: 2026-10-10T02:57:25.787125Z.

Manifest SHA256: `359381981e1e65d4259dc492965e7c792767f7f28b79995887d3f9705f1bb13e`.

### typed-mutations

Declare scope, authority, invariants, evidence and rollback through typed mutations. Status: documented.

[documentation evidence](https://github.com/ruvnet/autogenous/blob/905aa6cbe213392f8b3cab5d4f17bc3a48e0a509/README.md)

### admission-verification

Deterministic admission verdicts and policy constraints. Status: documented.

[documentation evidence](https://github.com/ruvnet/autogenous/blob/905aa6cbe213392f8b3cab5d4f17bc3a48e0a509/README.md)

### signed-promotion

Content-bound evaluation and staged signed promotion with rollback. Status: documented.

[documentation evidence](https://github.com/ruvnet/autogenous/blob/905aa6cbe213392f8b3cab5d4f17bc3a48e0a509/README.md)

### stream-observation

Observe chunks and SSE with bounded detectors and structured incident evidence. Status: documented.

[documentation evidence](https://github.com/ruvnet/autogenous/blob/905aa6cbe213392f8b3cab5d4f17bc3a48e0a509/README.md)

Declared integration roles (discovery metadata only):

* nexus: `ruv://ruvnet/constellation/service/ruvnet/resources/manifest.ruv`
* coordination: `ruv://ruvnet/constellation/service/ruflo/resources/manifest.ruv`
* execution-artifacts: `ruv://ruvnet/constellation/service/rvm/resources/manifest.ruv`
* public-retrieval: `ruv://ruvnet/constellation/service/ruvector/resources/manifest.ruv`
* evaluation: `ruv://ruvnet/constellation/service/metaharness/resources/manifest.ruv`
* evolution: `ruv://ruvnet/constellation/service/autogenous/resources/manifest.ruv`
* improvement-proposals: `ruv://ruvnet/constellation/service/dream-machine/resources/manifest.ruv`
* stream-observation: `ruv://ruvnet/constellation/service/midstream/resources/manifest.ruv`
* cryptography-research: `ruv://ruvnet/constellation/service/qudag/resources/manifest.ruv`
* community: `ruv://ruvnet/constellation/service/agentbbs/resources/manifest.ruv`

## daa

Identity: `ruv://ruvnet/constellation/service/daa/resources/manifest.ruv`

Source revision: `ca4e3a3c7e962098152f018a123db2bf67cf5d46`. Observed: 2026-10-10T02:57:47.932391Z.

Manifest SHA256: `2af40df4966e64e7318d7e679b1c459774e0fcf56ca67234bc935cfc2243e63c`.

### agent-orchestration

Documented monitoring, reasoning, action and reflection orchestration loop. Status: documented.

[documentation evidence](https://github.com/ruvnet/daa/blob/ca4e3a3c7e962098152f018a123db2bf67cf5d46/README.md)

### rules-governance

Rule-based decisions and audit trails. Status: documented.

[documentation evidence](https://github.com/ruvnet/daa/blob/ca4e3a3c7e962098152f018a123db2bf67cf5d46/README.md)

### distributed-ml

Documented Prime distributed training integration. Status: documented.

[documentation evidence](https://github.com/ruvnet/daa/blob/ca4e3a3c7e962098152f018a123db2bf67cf5d46/README.md)

### resource-economy

Documented resource-management economy modules. Status: documented.

[documentation evidence](https://github.com/ruvnet/daa/blob/ca4e3a3c7e962098152f018a123db2bf67cf5d46/README.md)

Declared integration roles (discovery metadata only):

* nexus: `ruv://ruvnet/constellation/service/ruvnet/resources/manifest.ruv`
* coordination: `ruv://ruvnet/constellation/service/ruflo/resources/manifest.ruv`
* execution-artifacts: `ruv://ruvnet/constellation/service/rvm/resources/manifest.ruv`
* public-retrieval: `ruv://ruvnet/constellation/service/ruvector/resources/manifest.ruv`
* evaluation: `ruv://ruvnet/constellation/service/metaharness/resources/manifest.ruv`
* evolution: `ruv://ruvnet/constellation/service/autogenous/resources/manifest.ruv`
* improvement-proposals: `ruv://ruvnet/constellation/service/dream-machine/resources/manifest.ruv`
* stream-observation: `ruv://ruvnet/constellation/service/midstream/resources/manifest.ruv`
* cryptography-research: `ruv://ruvnet/constellation/service/qudag/resources/manifest.ruv`
* community: `ruv://ruvnet/constellation/service/agentbbs/resources/manifest.ruv`

## dream-machine

Identity: `ruv://ruvnet/constellation/service/dream-machine/resources/manifest.ruv`

Source revision: `5707c825b2c065de44abed02594e1abf5eab95ea`. Observed: 2026-10-10T02:57:45.162552Z.

Manifest SHA256: `f6547d740757ca4b0856f52560cc277505dc37b59b4540cb37a491aa2fe4c555`.

### evolution-config

Compile configuration into a repository research and evolution workflow. Status: documented.

[documentation evidence](https://github.com/ruvnet/dream-machine/blob/5707c825b2c065de44abed02594e1abf5eab95ea/README.md)

### evidence-evaluation

Measure hypotheses against repository evaluators and retain outcomes. Status: documented.

[documentation evidence](https://github.com/ruvnet/dream-machine/blob/5707c825b2c065de44abed02594e1abf5eab95ea/README.md)

### human-promotion-gate

Separate evaluation and proposals from human merge authority. Status: documented.

[documentation evidence](https://github.com/ruvnet/dream-machine/blob/5707c825b2c065de44abed02594e1abf5eab95ea/README.md)

Declared integration roles (discovery metadata only):

* nexus: `ruv://ruvnet/constellation/service/ruvnet/resources/manifest.ruv`
* coordination: `ruv://ruvnet/constellation/service/ruflo/resources/manifest.ruv`
* execution-artifacts: `ruv://ruvnet/constellation/service/rvm/resources/manifest.ruv`
* public-retrieval: `ruv://ruvnet/constellation/service/ruvector/resources/manifest.ruv`
* evaluation: `ruv://ruvnet/constellation/service/metaharness/resources/manifest.ruv`
* evolution: `ruv://ruvnet/constellation/service/autogenous/resources/manifest.ruv`
* improvement-proposals: `ruv://ruvnet/constellation/service/dream-machine/resources/manifest.ruv`
* stream-observation: `ruv://ruvnet/constellation/service/midstream/resources/manifest.ruv`
* cryptography-research: `ruv://ruvnet/constellation/service/qudag/resources/manifest.ruv`
* community: `ruv://ruvnet/constellation/service/agentbbs/resources/manifest.ruv`

## helix

Identity: `ruv://ruvnet/constellation/service/helix/resources/manifest.ruv`

Source revision: `e8d8fe780becff4d95008e052742e5c3b0ad3b5c`. Observed: 2026-10-10T03:00:00Z.

Manifest SHA256: `57ed1556e62c1b3b6fe4e76fced30bf60bd1aad17190f88272d69343c8a86529`.

### health-provenance

Trace health evidence to its sources. Status: documented.

[documentation evidence](https://github.com/ruvnet/helix/blob/e8d8fe780becff4d95008e052742e5c3b0ad3b5c/README.md)

### health-knowledge

Organize longitudinal personal health knowledge locally. Status: documented.

[documentation evidence](https://github.com/ruvnet/helix/blob/e8d8fe780becff4d95008e052742e5c3b0ad3b5c/README.md)

Declared integration roles (discovery metadata only):

* nexus: `ruv://ruvnet/constellation/service/ruvnet/resources/manifest.ruv`
* coordination: `ruv://ruvnet/constellation/service/ruflo/resources/manifest.ruv`
* execution-artifacts: `ruv://ruvnet/constellation/service/rvm/resources/manifest.ruv`
* public-retrieval: `ruv://ruvnet/constellation/service/ruvector/resources/manifest.ruv`
* evaluation: `ruv://ruvnet/constellation/service/metaharness/resources/manifest.ruv`
* evolution: `ruv://ruvnet/constellation/service/autogenous/resources/manifest.ruv`
* improvement-proposals: `ruv://ruvnet/constellation/service/dream-machine/resources/manifest.ruv`
* stream-observation: `ruv://ruvnet/constellation/service/midstream/resources/manifest.ruv`
* cryptography-research: `ruv://ruvnet/constellation/service/qudag/resources/manifest.ruv`
* community: `ruv://ruvnet/constellation/service/agentbbs/resources/manifest.ruv`

## LatentMesh

Identity: `ruv://ruvnet/constellation/service/latentmesh/resources/manifest.ruv`

Source revision: `df9270799a1391925c1840a1845a6d169aaa2d93`. Observed: 2026-10-10T02:57:45.103116Z.

Manifest SHA256: `24ec481242795c2a3dc9a6849ca7286c38b7bf002b948b38acacc7a4b9541c6b`.

### semantic-envelopes

Compact semantic delta envelopes for bandwidth-constrained links. Status: documented.

[documentation evidence](https://github.com/ruvnet/LatentMesh/blob/df9270799a1391925c1840a1845a6d169aaa2d93/README.md)

### disconnected-messaging

Queue messages and forward after connectivity resumes. Status: documented.

[documentation evidence](https://github.com/ruvnet/LatentMesh/blob/df9270799a1391925c1840a1845a6d169aaa2d93/README.md)

### message-validation

Documented checksum, signature, replay and reassembly validation. Status: documented.

[documentation evidence](https://github.com/ruvnet/LatentMesh/blob/df9270799a1391925c1840a1845a6d169aaa2d93/README.md)

### portable-radio-core

Portable allocation-free C core and simulated radio transport. Status: documented.

[documentation evidence](https://github.com/ruvnet/LatentMesh/blob/df9270799a1391925c1840a1845a6d169aaa2d93/README.md)

Declared integration roles (discovery metadata only):

* nexus: `ruv://ruvnet/constellation/service/ruvnet/resources/manifest.ruv`
* coordination: `ruv://ruvnet/constellation/service/ruflo/resources/manifest.ruv`
* execution-artifacts: `ruv://ruvnet/constellation/service/rvm/resources/manifest.ruv`
* public-retrieval: `ruv://ruvnet/constellation/service/ruvector/resources/manifest.ruv`
* evaluation: `ruv://ruvnet/constellation/service/metaharness/resources/manifest.ruv`
* evolution: `ruv://ruvnet/constellation/service/autogenous/resources/manifest.ruv`
* improvement-proposals: `ruv://ruvnet/constellation/service/dream-machine/resources/manifest.ruv`
* stream-observation: `ruv://ruvnet/constellation/service/midstream/resources/manifest.ruv`
* cryptography-research: `ruv://ruvnet/constellation/service/qudag/resources/manifest.ruv`
* community: `ruv://ruvnet/constellation/service/agentbbs/resources/manifest.ruv`

## mcp-studio

Identity: `ruv://ruvnet/constellation/service/mcp-studio/resources/manifest.ruv`

Source revision: `1de79b28e679ea39937df54586cc9bdcffdf4cdc`. Observed: 2026-10-10T03:00:00Z.

Manifest SHA256: `d903877a6faaed03b6e61dac0b1fb0fa61a2d019c48f292fb9173605ebe67431`.

### mcp-reference

Expose documented tools, resources and prompts through the shared MCP server. Status: documented.

[documentation evidence](https://github.com/ruvnet/mcp-studio/blob/1de79b28e679ea39937df54586cc9bdcffdf4cdc/README.md)

### embedded-interface

Provide a bundled MCP Apps widget and browser playground. Status: documented.

[documentation evidence](https://github.com/ruvnet/mcp-studio/blob/1de79b28e679ea39937df54586cc9bdcffdf4cdc/README.md)

Declared integration roles (discovery metadata only):

* nexus: `ruv://ruvnet/constellation/service/ruvnet/resources/manifest.ruv`
* coordination: `ruv://ruvnet/constellation/service/ruflo/resources/manifest.ruv`
* execution-artifacts: `ruv://ruvnet/constellation/service/rvm/resources/manifest.ruv`
* public-retrieval: `ruv://ruvnet/constellation/service/ruvector/resources/manifest.ruv`
* evaluation: `ruv://ruvnet/constellation/service/metaharness/resources/manifest.ruv`
* evolution: `ruv://ruvnet/constellation/service/autogenous/resources/manifest.ruv`
* improvement-proposals: `ruv://ruvnet/constellation/service/dream-machine/resources/manifest.ruv`
* stream-observation: `ruv://ruvnet/constellation/service/midstream/resources/manifest.ruv`
* cryptography-research: `ruv://ruvnet/constellation/service/qudag/resources/manifest.ruv`
* community: `ruv://ruvnet/constellation/service/agentbbs/resources/manifest.ruv`

## metaharness

Identity: `ruv://ruvnet/constellation/service/metaharness/resources/manifest.ruv`

Source revision: `e0dfd44da72b7adfb7c57fdd42d124be58ed7086`. Observed: 2026-10-10T02:57:25.769738Z.

Manifest SHA256: `28638145cfe98ccd5aeef4ae5df1140e56d3e6c6dddabbc128d605128be0bcbe`.

### harness-generation

Generate repository-aware CLI, agent and MCP harnesses from a repository or project specification. Status: documented.

[documentation evidence](https://github.com/ruvnet/metaharness/blob/e0dfd44da72b7adfb7c57fdd42d124be58ed7086/README.md)

### policy-governance

Generated tool policy and governance interfaces. Status: documented.

[documentation evidence](https://github.com/ruvnet/metaharness/blob/e0dfd44da72b7adfb7c57fdd42d124be58ed7086/README.md)

### evolution-evaluation

Evaluate harness changes through documented Darwin Mode. Status: documented.

[documentation evidence](https://github.com/ruvnet/metaharness/blob/e0dfd44da72b7adfb7c57fdd42d124be58ed7086/README.md)

### release-verification

Generated release verification and witness-signed provenance. Status: documented.

[documentation evidence](https://github.com/ruvnet/metaharness/blob/e0dfd44da72b7adfb7c57fdd42d124be58ed7086/README.md)

Declared integration roles (discovery metadata only):

* nexus: `ruv://ruvnet/constellation/service/ruvnet/resources/manifest.ruv`
* coordination: `ruv://ruvnet/constellation/service/ruflo/resources/manifest.ruv`
* execution-artifacts: `ruv://ruvnet/constellation/service/rvm/resources/manifest.ruv`
* public-retrieval: `ruv://ruvnet/constellation/service/ruvector/resources/manifest.ruv`
* evaluation: `ruv://ruvnet/constellation/service/metaharness/resources/manifest.ruv`
* evolution: `ruv://ruvnet/constellation/service/autogenous/resources/manifest.ruv`
* improvement-proposals: `ruv://ruvnet/constellation/service/dream-machine/resources/manifest.ruv`
* stream-observation: `ruv://ruvnet/constellation/service/midstream/resources/manifest.ruv`
* cryptography-research: `ruv://ruvnet/constellation/service/qudag/resources/manifest.ruv`
* community: `ruv://ruvnet/constellation/service/agentbbs/resources/manifest.ruv`

## midstream

Identity: `ruv://ruvnet/constellation/service/midstream/resources/manifest.ruv`

Source revision: `abe78d62daa3b83844547f8ccbd2c283b0444d28`. Observed: 2026-10-10T02:57:25.799949Z.

Manifest SHA256: `f68ca69d8e921a5afa4a5e04ab7b9963cf23a8840daa7a0d5e5d5981f0014a91`.

### inflight-analysis

Analyze, score and intervene on streams while tokens arrive. Status: documented.

[documentation evidence](https://github.com/ruvnet/midstream/blob/abe78d62daa3b83844547f8ccbd2c283b0444d28/README.md)

### temporal-comparison

Temporal pattern comparison via DTW, LCS and edit distance. Status: documented.

[documentation evidence](https://github.com/ruvnet/midstream/blob/abe78d62daa3b83844547f8ccbd2c283b0444d28/README.md)

### quic-multistream

QUIC multi-stream transport as a separately composed library. Status: documented.

[documentation evidence](https://github.com/ruvnet/midstream/blob/abe78d62daa3b83844547f8ccbd2c283b0444d28/README.md)

### dynamical-analysis

Attractor and phase-space analysis for streams. Status: documented.

[documentation evidence](https://github.com/ruvnet/midstream/blob/abe78d62daa3b83844547f8ccbd2c283b0444d28/README.md)

Declared integration roles (discovery metadata only):

* nexus: `ruv://ruvnet/constellation/service/ruvnet/resources/manifest.ruv`
* coordination: `ruv://ruvnet/constellation/service/ruflo/resources/manifest.ruv`
* execution-artifacts: `ruv://ruvnet/constellation/service/rvm/resources/manifest.ruv`
* public-retrieval: `ruv://ruvnet/constellation/service/ruvector/resources/manifest.ruv`
* evaluation: `ruv://ruvnet/constellation/service/metaharness/resources/manifest.ruv`
* evolution: `ruv://ruvnet/constellation/service/autogenous/resources/manifest.ruv`
* improvement-proposals: `ruv://ruvnet/constellation/service/dream-machine/resources/manifest.ruv`
* stream-observation: `ruv://ruvnet/constellation/service/midstream/resources/manifest.ruv`
* cryptography-research: `ruv://ruvnet/constellation/service/qudag/resources/manifest.ruv`
* community: `ruv://ruvnet/constellation/service/agentbbs/resources/manifest.ruv`

## PhotonLayer

Identity: `ruv://ruvnet/constellation/service/photonlayer/resources/manifest.ruv`

Source revision: `fe86c9fad9a1572ce46e337f118656961bdf4ebb`. Observed: 2026-10-10T03:00:00Z.

Manifest SHA256: `f5c8dda8a54487b53c66a1ec0a0f9939333ad3d865c60e181fe6c71aeff04125`.

### optical-simulation

Simulate learned phase masks and compressed sensor measurements. Status: documented.

[documentation evidence](https://github.com/ruvnet/PhotonLayer/blob/fe86c9fad9a1572ce46e337f118656961bdf4ebb/README.md)

### experiment-receipts

Record deterministic experiment receipts. Status: documented.

[documentation evidence](https://github.com/ruvnet/PhotonLayer/blob/fe86c9fad9a1572ce46e337f118656961bdf4ebb/README.md)

Declared integration roles (discovery metadata only):

* nexus: `ruv://ruvnet/constellation/service/ruvnet/resources/manifest.ruv`
* coordination: `ruv://ruvnet/constellation/service/ruflo/resources/manifest.ruv`
* execution-artifacts: `ruv://ruvnet/constellation/service/rvm/resources/manifest.ruv`
* public-retrieval: `ruv://ruvnet/constellation/service/ruvector/resources/manifest.ruv`
* evaluation: `ruv://ruvnet/constellation/service/metaharness/resources/manifest.ruv`
* evolution: `ruv://ruvnet/constellation/service/autogenous/resources/manifest.ruv`
* improvement-proposals: `ruv://ruvnet/constellation/service/dream-machine/resources/manifest.ruv`
* stream-observation: `ruv://ruvnet/constellation/service/midstream/resources/manifest.ruv`
* cryptography-research: `ruv://ruvnet/constellation/service/qudag/resources/manifest.ruv`
* community: `ruv://ruvnet/constellation/service/agentbbs/resources/manifest.ruv`

## QuDAG

Identity: `ruv://ruvnet/constellation/service/qudag/resources/manifest.ruv`

Source revision: `945fc6fc5ca2fd25ede088e6b612d8f27f670229`. Observed: 2026-10-10T02:57:25.797767Z.

Manifest SHA256: `3b7b78a5dc1b0737346fd67f77abc641a30cb0b7f5c24c4784b555aa685b52b6`.

### ml-kem

Documented RustCrypto ML-KEM-768 implementation and interoperability tests. Status: documented.

[documentation evidence](https://github.com/ruvnet/QuDAG/blob/945fc6fc5ca2fd25ede088e6b612d8f27f670229/README.md)

### local-dag-admission

Atomic local DAG admission with parent ordering and backpressure. Status: documented.

[documentation evidence](https://github.com/ruvnet/QuDAG/blob/945fc6fc5ca2fd25ede088e6b612d8f27f670229/README.md)

### federation-bridge

RuFlo observation bridge and member federation client. Status: documented.

[documentation evidence](https://github.com/ruvnet/QuDAG/blob/945fc6fc5ca2fd25ede088e6b612d8f27f670229/README.md)

### collaboration-receipts

AgentBBS collaboration hub with durable receipts and RuVector retrieval. Status: documented.

[documentation evidence](https://github.com/ruvnet/QuDAG/blob/945fc6fc5ca2fd25ede088e6b612d8f27f670229/README.md)

Declared integration roles (discovery metadata only):

* nexus: `ruv://ruvnet/constellation/service/ruvnet/resources/manifest.ruv`
* coordination: `ruv://ruvnet/constellation/service/ruflo/resources/manifest.ruv`
* execution-artifacts: `ruv://ruvnet/constellation/service/rvm/resources/manifest.ruv`
* public-retrieval: `ruv://ruvnet/constellation/service/ruvector/resources/manifest.ruv`
* evaluation: `ruv://ruvnet/constellation/service/metaharness/resources/manifest.ruv`
* evolution: `ruv://ruvnet/constellation/service/autogenous/resources/manifest.ruv`
* improvement-proposals: `ruv://ruvnet/constellation/service/dream-machine/resources/manifest.ruv`
* stream-observation: `ruv://ruvnet/constellation/service/midstream/resources/manifest.ruv`
* cryptography-research: `ruv://ruvnet/constellation/service/qudag/resources/manifest.ruv`
* community: `ruv://ruvnet/constellation/service/agentbbs/resources/manifest.ruv`

## rGi

Identity: `ruv://ruvnet/constellation/service/rgi/resources/manifest.ruv`

Source revision: `2dd6adb526a7ca1d27b1c4d6cf98c828b390c421`. Observed: 2026-10-10T03:00:00Z.

Manifest SHA256: `5ada2b7784f492ed8da1522d3089dbdb623aaa9b6816e87e2a87d7c8be33293c`.

### persistent-runtime

Record observations, plan authorized actions and retain outcomes across restarts. Status: documented.

[documentation evidence](https://github.com/ruvnet/rGi/blob/2dd6adb526a7ca1d27b1c4d6cf98c828b390c421/README.md)

### policy-kernel

Evaluate capability and budget constraints through Rust native and WASM boundaries. Status: documented.

[documentation evidence](https://github.com/ruvnet/rGi/blob/2dd6adb526a7ca1d27b1c4d6cf98c828b390c421/README.md)

Declared integration roles (discovery metadata only):

* nexus: `ruv://ruvnet/constellation/service/ruvnet/resources/manifest.ruv`
* coordination: `ruv://ruvnet/constellation/service/ruflo/resources/manifest.ruv`
* execution-artifacts: `ruv://ruvnet/constellation/service/rvm/resources/manifest.ruv`
* public-retrieval: `ruv://ruvnet/constellation/service/ruvector/resources/manifest.ruv`
* evaluation: `ruv://ruvnet/constellation/service/metaharness/resources/manifest.ruv`
* evolution: `ruv://ruvnet/constellation/service/autogenous/resources/manifest.ruv`
* improvement-proposals: `ruv://ruvnet/constellation/service/dream-machine/resources/manifest.ruv`
* stream-observation: `ruv://ruvnet/constellation/service/midstream/resources/manifest.ruv`
* cryptography-research: `ruv://ruvnet/constellation/service/qudag/resources/manifest.ruv`
* community: `ruv://ruvnet/constellation/service/agentbbs/resources/manifest.ruv`

## ruClip

Identity: `ruv://ruvnet/constellation/service/ruclip/resources/manifest.ruv`

Source revision: `6e73a8f060bcbb69965a50ffe4627e33622d4094`. Observed: 2026-10-10T03:00:00Z.

Manifest SHA256: `c2b3d1cb0a5822e91280a96163893f4802e1aa7b7a287f57a77540a055bcda48`.

### company-operations

Organize agent roles, goals and work ownership. Status: documented.

[documentation evidence](https://github.com/ruvnet/ruClip/blob/6e73a8f060bcbb69965a50ffe4627e33622d4094/README.md)

### budget-governance

Gate heartbeats and approval transitions using bounded authority and accounting. Status: documented.

[documentation evidence](https://github.com/ruvnet/ruClip/blob/6e73a8f060bcbb69965a50ffe4627e33622d4094/README.md)

Declared integration roles (discovery metadata only):

* nexus: `ruv://ruvnet/constellation/service/ruvnet/resources/manifest.ruv`
* coordination: `ruv://ruvnet/constellation/service/ruflo/resources/manifest.ruv`
* execution-artifacts: `ruv://ruvnet/constellation/service/rvm/resources/manifest.ruv`
* public-retrieval: `ruv://ruvnet/constellation/service/ruvector/resources/manifest.ruv`
* evaluation: `ruv://ruvnet/constellation/service/metaharness/resources/manifest.ruv`
* evolution: `ruv://ruvnet/constellation/service/autogenous/resources/manifest.ruv`
* improvement-proposals: `ruv://ruvnet/constellation/service/dream-machine/resources/manifest.ruv`
* stream-observation: `ruv://ruvnet/constellation/service/midstream/resources/manifest.ruv`
* cryptography-research: `ruv://ruvnet/constellation/service/qudag/resources/manifest.ruv`
* community: `ruv://ruvnet/constellation/service/agentbbs/resources/manifest.ruv`

## rudevolution

Identity: `ruv://ruvnet/constellation/service/rudevolution/resources/manifest.ruv`

Source revision: `b99ec70c780e249b151de5c32ee9839784671962`. Observed: 2026-10-10T02:57:47.895580Z.

Manifest SHA256: `3f81a6f04a8e4a67261296b59f14521955049b6882f187c5107266e8217d83e3`.

### bundle-analysis

Statically analyze JavaScript bundles into weighted reference graphs. Status: documented.

[documentation evidence](https://github.com/ruvnet/rudevolution/blob/b99ec70c780e249b151de5c32ee9839784671962/README.md)

### module-inference

Propose module boundaries and identifier names with confidence metadata. Status: documented.

[documentation evidence](https://github.com/ruvnet/rudevolution/blob/b99ec70c780e249b151de5c32ee9839784671962/README.md)

### integrity-witnesses

Emit SHA3-256 content integrity witnesses without proving behavioral equivalence. Status: documented.

[documentation evidence](https://github.com/ruvnet/rudevolution/blob/b99ec70c780e249b151de5c32ee9839784671962/README.md)

### clean-room-handoff

Signed interface-only specification handoff to isolated implementation rooms. Status: documented.

[documentation evidence](https://github.com/ruvnet/rudevolution/blob/b99ec70c780e249b151de5c32ee9839784671962/README.md)

Declared integration roles (discovery metadata only):

* nexus: `ruv://ruvnet/constellation/service/ruvnet/resources/manifest.ruv`
* coordination: `ruv://ruvnet/constellation/service/ruflo/resources/manifest.ruv`
* execution-artifacts: `ruv://ruvnet/constellation/service/rvm/resources/manifest.ruv`
* public-retrieval: `ruv://ruvnet/constellation/service/ruvector/resources/manifest.ruv`
* evaluation: `ruv://ruvnet/constellation/service/metaharness/resources/manifest.ruv`
* evolution: `ruv://ruvnet/constellation/service/autogenous/resources/manifest.ruv`
* improvement-proposals: `ruv://ruvnet/constellation/service/dream-machine/resources/manifest.ruv`
* stream-observation: `ruv://ruvnet/constellation/service/midstream/resources/manifest.ruv`
* cryptography-research: `ruv://ruvnet/constellation/service/qudag/resources/manifest.ruv`
* community: `ruv://ruvnet/constellation/service/agentbbs/resources/manifest.ruv`

## rufield

Identity: `ruv://ruvnet/constellation/service/rufield/resources/manifest.ruv`

Source revision: `7179a2efc706993ee0d87f0093e6a0e9e3dc5017`. Observed: 2026-10-10T02:57:45.150068Z.

Manifest SHA256: `4a5e516e65201efcf50e80b7e12d200c25f1d4a9799878e69810a9ea94b73732`.

### field-event-spec

Normalize sensing modalities into common events, tensors, privacy and provenance. Status: documented.

[documentation evidence](https://github.com/ruvnet/rufield/blob/7179a2efc706993ee0d87f0093e6a0e9e3dc5017/README.md)

### csi-replay

Replay captured CSI from files with explicitly unvalidated motion/presence proxies. Status: documented.

[documentation evidence](https://github.com/ruvnet/rufield/blob/7179a2efc706993ee0d87f0093e6a0e9e3dc5017/README.md)

### ultrasonic-replay

Ingest BatVu simulator range profiles under simulation trust. Status: documented.

[documentation evidence](https://github.com/ruvnet/rufield/blob/7179a2efc706993ee0d87f0093e6a0e9e3dc5017/README.md)

### privacy-provenance

Privacy-aware, provenance-rich event model for ambient sensing. Status: documented.

[documentation evidence](https://github.com/ruvnet/rufield/blob/7179a2efc706993ee0d87f0093e6a0e9e3dc5017/README.md)

Declared integration roles (discovery metadata only):

* nexus: `ruv://ruvnet/constellation/service/ruvnet/resources/manifest.ruv`
* coordination: `ruv://ruvnet/constellation/service/ruflo/resources/manifest.ruv`
* execution-artifacts: `ruv://ruvnet/constellation/service/rvm/resources/manifest.ruv`
* public-retrieval: `ruv://ruvnet/constellation/service/ruvector/resources/manifest.ruv`
* evaluation: `ruv://ruvnet/constellation/service/metaharness/resources/manifest.ruv`
* evolution: `ruv://ruvnet/constellation/service/autogenous/resources/manifest.ruv`
* improvement-proposals: `ruv://ruvnet/constellation/service/dream-machine/resources/manifest.ruv`
* stream-observation: `ruv://ruvnet/constellation/service/midstream/resources/manifest.ruv`
* cryptography-research: `ruv://ruvnet/constellation/service/qudag/resources/manifest.ruv`
* community: `ruv://ruvnet/constellation/service/agentbbs/resources/manifest.ruv`

## ruflo

Identity: `ruv://ruvnet/constellation/service/ruflo/resources/manifest.ruv`

Source revision: `6c046548e29506be9bfd6640186d6e85a444e849`. Observed: 2026-10-10T02:57:25.840156Z.

Manifest SHA256: `6ddcf710a6ad596c85d212a0c8502a7430d8677a1829d00edd24102ed7a041a2`.

### agent-orchestration

Coordinate specialized agents and swarms through a CLI and MCP harness. Status: documented.

[documentation evidence](https://github.com/ruvnet/ruflo/blob/6c046548e29506be9bfd6640186d6e85a444e849/README.md)

### federated-coordination

Documented federation communication and agent coordination. Status: documented.

[documentation evidence](https://github.com/ruvnet/ruflo/blob/6c046548e29506be9bfd6640186d6e85a444e849/README.md)

### persistent-memory

Project memory and trajectory learning integration with RuVector. Status: documented.

[documentation evidence](https://github.com/ruvnet/ruflo/blob/6c046548e29506be9bfd6640186d6e85a444e849/README.md)

### console-and-mods

Inspect runs and operate the agent console with plugin mods. Status: documented.

[documentation evidence](https://github.com/ruvnet/ruflo/blob/6c046548e29506be9bfd6640186d6e85a444e849/README.md)

Declared integration roles (discovery metadata only):

* nexus: `ruv://ruvnet/constellation/service/ruvnet/resources/manifest.ruv`
* coordination: `ruv://ruvnet/constellation/service/ruflo/resources/manifest.ruv`
* execution-artifacts: `ruv://ruvnet/constellation/service/rvm/resources/manifest.ruv`
* public-retrieval: `ruv://ruvnet/constellation/service/ruvector/resources/manifest.ruv`
* evaluation: `ruv://ruvnet/constellation/service/metaharness/resources/manifest.ruv`
* evolution: `ruv://ruvnet/constellation/service/autogenous/resources/manifest.ruv`
* improvement-proposals: `ruv://ruvnet/constellation/service/dream-machine/resources/manifest.ruv`
* stream-observation: `ruv://ruvnet/constellation/service/midstream/resources/manifest.ruv`
* cryptography-research: `ruv://ruvnet/constellation/service/qudag/resources/manifest.ruv`
* community: `ruv://ruvnet/constellation/service/agentbbs/resources/manifest.ruv`

## rultra

Identity: `ruv://ruvnet/constellation/service/rultra/resources/manifest.ruv`

Source revision: `03e4a7e039c9ee6e47193f77127d8d35f7830ed2`. Observed: 2026-10-10T03:00:00Z.

Manifest SHA256: `74801addef363191433360e37abd905c0c17100ada28399a96d46012ac780e95`.

### sensor-interface

Unify sensors and actuators behind typed interfaces. Status: documented.

[documentation evidence](https://github.com/ruvnet/rultra/blob/03e4a7e039c9ee6e47193f77127d8d35f7830ed2/README.md)

### governed-tuning

Evaluate configuration proposals with fitness gates, canary and rollback evidence. Status: documented.

[documentation evidence](https://github.com/ruvnet/rultra/blob/03e4a7e039c9ee6e47193f77127d8d35f7830ed2/README.md)

Declared integration roles (discovery metadata only):

* nexus: `ruv://ruvnet/constellation/service/ruvnet/resources/manifest.ruv`
* coordination: `ruv://ruvnet/constellation/service/ruflo/resources/manifest.ruv`
* execution-artifacts: `ruv://ruvnet/constellation/service/rvm/resources/manifest.ruv`
* public-retrieval: `ruv://ruvnet/constellation/service/ruvector/resources/manifest.ruv`
* evaluation: `ruv://ruvnet/constellation/service/metaharness/resources/manifest.ruv`
* evolution: `ruv://ruvnet/constellation/service/autogenous/resources/manifest.ruv`
* improvement-proposals: `ruv://ruvnet/constellation/service/dream-machine/resources/manifest.ruv`
* stream-observation: `ruv://ruvnet/constellation/service/midstream/resources/manifest.ruv`
* cryptography-research: `ruv://ruvnet/constellation/service/qudag/resources/manifest.ruv`
* community: `ruv://ruvnet/constellation/service/agentbbs/resources/manifest.ruv`

## ruPet

Identity: `ruv://ruvnet/constellation/service/rupet/resources/manifest.ruv`

Source revision: `ec2737995cdf74ef28a59ddd6d38e1c721fe0636`. Observed: 2026-10-10T03:00:00Z.

Manifest SHA256: `15585729369a80a84aae9bd2f65578f932bc9161cfffd8690a8a7607553b3011`.

### pet-assets

Distribute sprite and metadata assets for compatible desktop pet hosts. Status: documented.

[documentation evidence](https://github.com/ruvnet/ruPet/blob/ec2737995cdf74ef28a59ddd6d38e1c721fe0636/README.md)

Declared integration roles (discovery metadata only):

* nexus: `ruv://ruvnet/constellation/service/ruvnet/resources/manifest.ruv`
* coordination: `ruv://ruvnet/constellation/service/ruflo/resources/manifest.ruv`
* execution-artifacts: `ruv://ruvnet/constellation/service/rvm/resources/manifest.ruv`
* public-retrieval: `ruv://ruvnet/constellation/service/ruvector/resources/manifest.ruv`
* evaluation: `ruv://ruvnet/constellation/service/metaharness/resources/manifest.ruv`
* evolution: `ruv://ruvnet/constellation/service/autogenous/resources/manifest.ruv`
* improvement-proposals: `ruv://ruvnet/constellation/service/dream-machine/resources/manifest.ruv`
* stream-observation: `ruv://ruvnet/constellation/service/midstream/resources/manifest.ruv`
* cryptography-research: `ruv://ruvnet/constellation/service/qudag/resources/manifest.ruv`
* community: `ruv://ruvnet/constellation/service/agentbbs/resources/manifest.ruv`

## ruv-FANN

Identity: `ruv://ruvnet/constellation/service/ruv-fann/resources/manifest.ruv`

Source revision: `1d93b35a1f49ad4ee6c7ac9223f74f6a6255b25d`. Observed: 2026-10-10T02:57:48.016951Z.

Manifest SHA256: `f6190c3790545789e4f6582d91c890630a0cff22e564592c4bf9a24a1095b578`.

### neural-networks

Rust implementation of Fast Artificial Neural Network algorithms. Status: documented.

[documentation evidence](https://github.com/ruvnet/ruv-FANN/blob/1d93b35a1f49ad4ee6c7ac9223f74f6a6255b25d/README.md)

### forecasting

Neuro-Divergent neural forecasting components. Status: documented.

[documentation evidence](https://github.com/ruvnet/ruv-FANN/blob/1d93b35a1f49ad4ee6c7ac9223f74f6a6255b25d/README.md)

### swarm-intelligence

ruv-swarm agent orchestration components. Status: documented.

[documentation evidence](https://github.com/ruvnet/ruv-FANN/blob/1d93b35a1f49ad4ee6c7ac9223f74f6a6255b25d/README.md)

Declared integration roles (discovery metadata only):

* nexus: `ruv://ruvnet/constellation/service/ruvnet/resources/manifest.ruv`
* coordination: `ruv://ruvnet/constellation/service/ruflo/resources/manifest.ruv`
* execution-artifacts: `ruv://ruvnet/constellation/service/rvm/resources/manifest.ruv`
* public-retrieval: `ruv://ruvnet/constellation/service/ruvector/resources/manifest.ruv`
* evaluation: `ruv://ruvnet/constellation/service/metaharness/resources/manifest.ruv`
* evolution: `ruv://ruvnet/constellation/service/autogenous/resources/manifest.ruv`
* improvement-proposals: `ruv://ruvnet/constellation/service/dream-machine/resources/manifest.ruv`
* stream-observation: `ruv://ruvnet/constellation/service/midstream/resources/manifest.ruv`
* cryptography-research: `ruv://ruvnet/constellation/service/qudag/resources/manifest.ruv`
* community: `ruv://ruvnet/constellation/service/agentbbs/resources/manifest.ruv`

## RuVector

Identity: `ruv://ruvnet/constellation/service/ruvector/resources/manifest.ruv`

Source revision: `f9e98b681305827f1615f8a371ed2a0169d440be`. Observed: 2026-10-10T02:57:25.799545Z.

Manifest SHA256: `00ba38a37017bd6c956b1e71a6feb332008de13b19292c81cb1b17f0068950cb`.

### vector-search

Durable vector retrieval with HNSW and flat indexes. Status: documented.

[documentation evidence](https://github.com/ruvnet/RuVector/blob/f9e98b681305827f1615f8a371ed2a0169d440be/README.md)

### agent-memory

Typed persistent agent episodes, skills, causal edges, sessions and witness logs. Status: documented.

[documentation evidence](https://github.com/ruvnet/RuVector/blob/f9e98b681305827f1615f8a371ed2a0169d440be/README.md)

### graph-storage

Graph and hypergraph relationships for memory and retrieval. Status: documented.

[documentation evidence](https://github.com/ruvnet/RuVector/blob/f9e98b681305827f1615f8a371ed2a0169d440be/README.md)

### local-decisions

Local typed decisions through the separate typesafe package. Status: documented.

[documentation evidence](https://github.com/ruvnet/RuVector/blob/f9e98b681305827f1615f8a371ed2a0169d440be/README.md)

Declared integration roles (discovery metadata only):

* nexus: `ruv://ruvnet/constellation/service/ruvnet/resources/manifest.ruv`
* coordination: `ruv://ruvnet/constellation/service/ruflo/resources/manifest.ruv`
* execution-artifacts: `ruv://ruvnet/constellation/service/rvm/resources/manifest.ruv`
* public-retrieval: `ruv://ruvnet/constellation/service/ruvector/resources/manifest.ruv`
* evaluation: `ruv://ruvnet/constellation/service/metaharness/resources/manifest.ruv`
* evolution: `ruv://ruvnet/constellation/service/autogenous/resources/manifest.ruv`
* improvement-proposals: `ruv://ruvnet/constellation/service/dream-machine/resources/manifest.ruv`
* stream-observation: `ruv://ruvnet/constellation/service/midstream/resources/manifest.ruv`
* cryptography-research: `ruv://ruvnet/constellation/service/qudag/resources/manifest.ruv`
* community: `ruv://ruvnet/constellation/service/agentbbs/resources/manifest.ruv`

## RuView

Identity: `ruv://ruvnet/constellation/service/ruview/resources/manifest.ruv`

Source revision: `0ef6b96fe15e30b4a086992e47e18081a0ba37ce`. Observed: 2026-10-10T02:57:25.760278Z.

Manifest SHA256: `acd7a1354253c20249a0dbc198cc396621ae6fd651228e8f712f57f4ff48d331`.

### wifi-sensing

WiFi CSI sensing for presence, movement and vitals, with hardware and accuracy caveats. Status: documented.

[documentation evidence](https://github.com/ruvnet/RuView/blob/0ef6b96fe15e30b4a086992e47e18081a0ba37ce/README.md)

### model-workflow

Record CSI, train models, load RVF files and switch LoRA profiles. Status: documented.

[documentation evidence](https://github.com/ruvnet/RuView/blob/0ef6b96fe15e30b4a086992e47e18081a0ba37ce/README.md)

### local-automation

HOMECORE local state, history, automation and signed Wasm plugins. Status: documented.

[documentation evidence](https://github.com/ruvnet/RuView/blob/0ef6b96fe15e30b4a086992e47e18081a0ba37ce/README.md)

### contributor-harness

Repository guidance, guarded agents, MCP and deterministic verification. Status: documented.

[documentation evidence](https://github.com/ruvnet/RuView/blob/0ef6b96fe15e30b4a086992e47e18081a0ba37ce/README.md)

Declared integration roles (discovery metadata only):

* nexus: `ruv://ruvnet/constellation/service/ruvnet/resources/manifest.ruv`
* coordination: `ruv://ruvnet/constellation/service/ruflo/resources/manifest.ruv`
* execution-artifacts: `ruv://ruvnet/constellation/service/rvm/resources/manifest.ruv`
* public-retrieval: `ruv://ruvnet/constellation/service/ruvector/resources/manifest.ruv`
* evaluation: `ruv://ruvnet/constellation/service/metaharness/resources/manifest.ruv`
* evolution: `ruv://ruvnet/constellation/service/autogenous/resources/manifest.ruv`
* improvement-proposals: `ruv://ruvnet/constellation/service/dream-machine/resources/manifest.ruv`
* stream-observation: `ruv://ruvnet/constellation/service/midstream/resources/manifest.ruv`
* cryptography-research: `ruv://ruvnet/constellation/service/qudag/resources/manifest.ruv`
* community: `ruv://ruvnet/constellation/service/agentbbs/resources/manifest.ruv`

## ruvnet

Identity: `ruv://ruvnet/constellation/service/ruvnet/resources/manifest.ruv`

Source revision: `9e5915a0b8f9437bc0cc2f55a27ab9c545ac44f8`. Observed: 2026-10-10T03:00:00Z.

Manifest SHA256: `19a668b3af39547004fb9182c53896efc0dd446189b9ad76134f248b4d6e70be`.

### ecosystem-discovery

Publish project, package and evidence inventories for people and AI systems. Status: documented.

[documentation evidence](https://github.com/ruvnet/ruvnet/blob/9e5915a0b8f9437bc0cc2f55a27ab9c545ac44f8/CONTRIBUTING.md)

[documentation evidence](https://github.com/ruvnet/ruvnet/blob/9e5915a0b8f9437bc0cc2f55a27ab9c545ac44f8/llms.txt)

### package-inventory

Maintain documented repository and package mappings with dated source evidence. Status: documented.

[documentation evidence](https://github.com/ruvnet/ruvnet/blob/9e5915a0b8f9437bc0cc2f55a27ab9c545ac44f8/docs/ruvnet-packages.md)

Declared integration roles (discovery metadata only):

* nexus: `ruv://ruvnet/constellation/service/ruvnet/resources/manifest.ruv`
* coordination: `ruv://ruvnet/constellation/service/ruflo/resources/manifest.ruv`
* execution-artifacts: `ruv://ruvnet/constellation/service/rvm/resources/manifest.ruv`
* public-retrieval: `ruv://ruvnet/constellation/service/ruvector/resources/manifest.ruv`
* evaluation: `ruv://ruvnet/constellation/service/metaharness/resources/manifest.ruv`
* evolution: `ruv://ruvnet/constellation/service/autogenous/resources/manifest.ruv`
* improvement-proposals: `ruv://ruvnet/constellation/service/dream-machine/resources/manifest.ruv`
* stream-observation: `ruv://ruvnet/constellation/service/midstream/resources/manifest.ruv`
* cryptography-research: `ruv://ruvnet/constellation/service/qudag/resources/manifest.ruv`
* community: `ruv://ruvnet/constellation/service/agentbbs/resources/manifest.ruv`

## rvm

Identity: `ruv://ruvnet/constellation/service/rvm/resources/manifest.ruv`

Source revision: `510a82f3a34a5fc9fc78b8144167809dbe3e067d`. Observed: 2026-10-10T03:00:00Z.

Manifest SHA256: `40f59d6ae6326d33d418d8ea3fe44eb5c214b1d4553868fefa5fbd173b4f9569`.

### governed-context

Canonical ruv context URI parsing, capability-governed context namespace and immutable RVF revisions. Status: documented.

[documentation evidence](https://github.com/ruvnet/rvm/blob/510a82f3a34a5fc9fc78b8144167809dbe3e067d/crates/rvm-context/src/uri.rs)

[documentation evidence](https://github.com/ruvnet/rvm/blob/510a82f3a34a5fc9fc78b8144167809dbe3e067d/crates/rvm-context/src/lib.rs)

[documentation evidence](https://github.com/ruvnet/rvm/blob/510a82f3a34a5fc9fc78b8144167809dbe3e067d/docs/adr/ADR-157-ruv-context-namespace.md)

### context-artifacts

Compile exact non-executable context bytes into self-verified RVF artifacts with SHA-256 identity. Status: documented.

[documentation evidence](https://github.com/ruvnet/rvm/blob/510a82f3a34a5fc9fc78b8144167809dbe3e067d/crates/rvm-context-service/src/compiler.rs)

### semantic-policy

Default-deny host action broker with live authorization, policy, audit before dispatch. Status: documented.

[documentation evidence](https://github.com/ruvnet/rvm/blob/510a82f3a34a5fc9fc78b8144167809dbe3e067d/crates/rvm-host/src/semantic.rs)

[documentation evidence](https://github.com/ruvnet/rvm/blob/510a82f3a34a5fc9fc78b8144167809dbe3e067d/docs/adr/ADR-159-semantic-policy-strands.md)

### execution-lifecycle

Inspect, verify and manage an RVF-backed agent lifecycle through host adapters. Status: documented.

[documentation evidence](https://github.com/ruvnet/rvm/blob/510a82f3a34a5fc9fc78b8144167809dbe3e067d/crates/rvm-launch/src/lib.rs)

[documentation evidence](https://github.com/ruvnet/rvm/blob/510a82f3a34a5fc9fc78b8144167809dbe3e067d/README.md)

### receipt-anchoring

Verify external evaluation receipts and anchor commitments into witness chains. Status: documented.

[documentation evidence](https://github.com/ruvnet/rvm/blob/510a82f3a34a5fc9fc78b8144167809dbe3e067d/crates/rvm-anchor/src/lib.rs)

[documentation evidence](https://github.com/ruvnet/rvm/blob/510a82f3a34a5fc9fc78b8144167809dbe3e067d/docs/adr/ADR-156-external-receipt-anchoring.md)

Declared integration roles (discovery metadata only):

* nexus: `ruv://ruvnet/constellation/service/ruvnet/resources/manifest.ruv`
* coordination: `ruv://ruvnet/constellation/service/ruflo/resources/manifest.ruv`
* execution-artifacts: `ruv://ruvnet/constellation/service/rvm/resources/manifest.ruv`
* public-retrieval: `ruv://ruvnet/constellation/service/ruvector/resources/manifest.ruv`
* evaluation: `ruv://ruvnet/constellation/service/metaharness/resources/manifest.ruv`
* evolution: `ruv://ruvnet/constellation/service/autogenous/resources/manifest.ruv`
* improvement-proposals: `ruv://ruvnet/constellation/service/dream-machine/resources/manifest.ruv`
* stream-observation: `ruv://ruvnet/constellation/service/midstream/resources/manifest.ruv`
* cryptography-research: `ruv://ruvnet/constellation/service/qudag/resources/manifest.ruv`
* community: `ruv://ruvnet/constellation/service/agentbbs/resources/manifest.ruv`

## sublinear-time-solver

Identity: `ruv://ruvnet/constellation/service/sublinear-time-solver/resources/manifest.ruv`

Source revision: `6ef45761e9a27029cf968322b3967364499e3b5d`. Observed: 2026-10-10T02:57:51.756620Z.

Manifest SHA256: `5b2b6c845808fd65cb908d24ea400b0836baa482931e3a8460f01a653036d5eb`.

### linear-system-solving

Solve and analyze supported sparse diagonally dominant linear systems. Status: documented.

[documentation evidence](https://github.com/ruvnet/sublinear-time-solver/blob/6ef45761e9a27029cf968322b3967364499e3b5d/README.md)

### matrix-analysis

Analyze condition number and diagonal dominance. Status: documented.

[documentation evidence](https://github.com/ruvnet/sublinear-time-solver/blob/6ef45761e9a27029cf968322b3967364499e3b5d/README.md)

### mcp-solver

Expose solver tools through MCP. Status: documented.

[documentation evidence](https://github.com/ruvnet/sublinear-time-solver/blob/6ef45761e9a27029cf968322b3967364499e3b5d/README.md)

### solver-methods

Documented Neumann, forward-push and random-walk methods. Status: documented.

[documentation evidence](https://github.com/ruvnet/sublinear-time-solver/blob/6ef45761e9a27029cf968322b3967364499e3b5d/README.md)

Declared integration roles (discovery metadata only):

* nexus: `ruv://ruvnet/constellation/service/ruvnet/resources/manifest.ruv`
* coordination: `ruv://ruvnet/constellation/service/ruflo/resources/manifest.ruv`
* execution-artifacts: `ruv://ruvnet/constellation/service/rvm/resources/manifest.ruv`
* public-retrieval: `ruv://ruvnet/constellation/service/ruvector/resources/manifest.ruv`
* evaluation: `ruv://ruvnet/constellation/service/metaharness/resources/manifest.ruv`
* evolution: `ruv://ruvnet/constellation/service/autogenous/resources/manifest.ruv`
* improvement-proposals: `ruv://ruvnet/constellation/service/dream-machine/resources/manifest.ruv`
* stream-observation: `ruv://ruvnet/constellation/service/midstream/resources/manifest.ruv`
* cryptography-research: `ruv://ruvnet/constellation/service/qudag/resources/manifest.ruv`
* community: `ruv://ruvnet/constellation/service/agentbbs/resources/manifest.ruv`

## worldgraph

Identity: `ruv://ruvnet/constellation/service/worldgraph/resources/manifest.ruv`

Source revision: `9b1c79c836cdacfb7b44f058c593157bac4c1dab`. Observed: 2026-10-10T03:00:00Z.

Manifest SHA256: `c73b1b14e5ec674f5a98902264ca8b8a75a4cea3c9aca466bbc835dd1d5ee850`.

### spatial-graph

Represent rooms, sensors, entities and beliefs with provenance. Status: documented.

[documentation evidence](https://github.com/ruvnet/worldgraph/blob/9b1c79c836cdacfb7b44f058c593157bac4c1dab/README.md)

### world-visualization

Explore authored temporal environments and imported captures; calibration remains separate. Status: documented.

[documentation evidence](https://github.com/ruvnet/worldgraph/blob/9b1c79c836cdacfb7b44f058c593157bac4c1dab/README.md)

Declared integration roles (discovery metadata only):

* nexus: `ruv://ruvnet/constellation/service/ruvnet/resources/manifest.ruv`
* coordination: `ruv://ruvnet/constellation/service/ruflo/resources/manifest.ruv`
* execution-artifacts: `ruv://ruvnet/constellation/service/rvm/resources/manifest.ruv`
* public-retrieval: `ruv://ruvnet/constellation/service/ruvector/resources/manifest.ruv`
* evaluation: `ruv://ruvnet/constellation/service/metaharness/resources/manifest.ruv`
* evolution: `ruv://ruvnet/constellation/service/autogenous/resources/manifest.ruv`
* improvement-proposals: `ruv://ruvnet/constellation/service/dream-machine/resources/manifest.ruv`
* stream-observation: `ruv://ruvnet/constellation/service/midstream/resources/manifest.ruv`
* cryptography-research: `ruv://ruvnet/constellation/service/qudag/resources/manifest.ruv`
* community: `ruv://ruvnet/constellation/service/agentbbs/resources/manifest.ruv`
