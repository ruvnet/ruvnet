# RuV Stack entrypoint validation

Assessment date: 2026-09-12. Scope: new plugin, marketplace manifests, README entry point and CI. No production changes to x.ruv.io.

## Results

| Gate | Evidence |
| --- | --- |
| Local CLI and MCP | 8 Node tests passed, including official SDK negotiation and a real subprocess stdio lifecycle |
| Coverage | 100% lines, 100% functions, 98.81% branches across production bin/lib modules; Node built-in coverage |
| Host manifests | Claude Code 2.1.269 marketplace validator; Codex plugin ingestion validator; all four skill validators passed |
| Metadata | Local validator checks catalog boundaries, marketplace source paths, skill references and fixed remote URL |
| Dependencies | npm audit: zero reported vulnerabilities across 94 installed packages; [raw result](dependency-audit.json) |
| Ruflo scan | @claude-flow/cli@3.25.6, deep/all scan: zero critical, high, medium or low signals |
| MetaHarness | metaharness@0.4.16 read-only score: CLI + MCP, scaffoldReady true, hard constraints 6/6; [raw score](metaharness-score.json) |
| Remote smoke | Connected x.ruv.io MCP channel_list returned public channel metadata; no write probe performed |
| Packaging | npm pack dry run contains manifests, skills, catalog, CLI/MCP, docs and validation scripts; no node_modules or credentials |

MetaHarness scores and estimated cost are heuristics, not measured compile probability, security assurance or actual model spending. The local companion itself performs no model inference.

## Benchmark

[Raw measurements](benchmark.json): Node v24.19.0, linux/x64, 10 catalog records, 10,000 warm queries after 1,000 warm-up calls, 20 independent CLI launches.

* Discovery p50: 0.000742 ms; p95: 0.001012 ms.
* Cold CLI p50: 59.34 ms; p95: 63.00 ms.
* Benchmark process RSS: 48050176 bytes.
* Gates: discovery p95 below 5 ms; cold CLI p95 below 1000 ms. Both passed.

These are local keyword lookup and process launch measurements. They exclude embedding/search recall, SDK startup, federation network latency, model inference and end-to-end agent performance. No speedup over RuVector or competing platforms is claimed. Pre-indexed tokens and lazy SDK loading keep this small workload simple.

## Threat model and disposition

| Boundary / abuse case | Control / evidence | Residual risk |
| --- | --- | --- |
| Model requests shell execution or publishing | No production child-process, network or write APIs; tools are an explicit read-only allowlist | Host still has other tools outside this package |
| Arbitrary file or URL read | Resource URIs and catalog path are fixed; path traversal cases rejected in protocol tests | A compromised local installation can modify its own source |
| Prompt injection in a goal or federation message | Goal is serialized as data, never interpolated into command templates; federation skill denies authority from messages | Instruction following depends on the host/model; this is not a universal prompt-injection defense |
| Memory exhaustion from a huge stdio line | 64 KiB limit applied before SDK buffering; oversized-frame subprocess test | Host must bound process lifetime, total throughput and concurrent usage |
| OAuth/private key leakage | No credentials in config; direct host-managed federation OAuth; personal keys remain with the user's client | Remote gateway behavior is outside this repository's audit |
| Supply-chain substitution | Exact SDK 1.30.0, npm lock with integrity hashes, ignored lifecycle scripts, pinned CI actions | Advisory coverage is time-bounded and does not prove absence of unknown vulnerabilities |
| Unvalidated capability claims | Dated catalog, per-project maturity boundaries, empty-search disclosure, execution flag false | Lexical discovery can miss relevant projects; source descriptions can age |

No confirmed critical or high issues remain in the scoped review. Ruflo scanner output was inspected as a signal, not taken as a proof of security. Dependency advisory data was queried on 2026-09-12 via npm audit; the API does not expose a global feed revision. The pinned Ruflo scanner was invoked via npx outside the shipped dependency set.

Lockfile SHA-256: `dc2e33b25aeb4704b6cd8b79c1bf89694520c575f8c9a930ca7e7f41a23dd9bf`.

## Reproduce

```bash
cd plugins/ruvnet
npm ci --ignore-scripts
npm run check
node --test --experimental-test-coverage test/core.test.mjs test/mcp.test.mjs
npm audit --json
npm pack --dry-run --ignore-scripts
```

From the repository root:

```bash
npx -y @claude-flow/cli@3.25.6 security scan --target plugins/ruvnet --depth deep --type all
npx -y metaharness@0.4.16 score plugins/ruvnet --json
npx -y @anthropic-ai/claude-code@2.1.269 plugin validate .
```

## Limits

No fresh ChatGPT, Claude chat, Lovable or Codex GUI installation was exercised. Claude marketplace schema validation and MCP SDK interoperability are verified, not equivalent to those UI flows. Codex CLI was unavailable. The repository marketplace is not an official vendor directory listing. No new remote discovery tools were deployed, no npm release was published, and no autonomous execution engine is implemented by this read-only entrypoint. The real MetaHarness remains the generation/evolution integration.

CI runs Node 22 and 24 tests, metadata validation, benchmarks, audit and packaging. Its status is attached to the pushed commit; local success does not imply a completed remote CI run. To roll back, revert the entrypoint commit and remove the corresponding host plugin/configuration; revoke OAuth separately when appropriate.
