---
name: ruvnet-metaharness
description: Generate or evolve a repository-specific CLI, MCP and skills harness using MetaHarness, with bounded evaluation and explicit release authority.
---

# Build a repo-specific harness

Read [MetaHarness's current guide](https://github.com/ruvnet/metaharness/blob/main/docs/USERGUIDE.md) and the target repository's instructions. MetaHarness generates a candidate harness; this entrypoint does not implement or certify Darwin, model learning, or sandbox enforcement.

Use `ruvnet_plan` if available for a deterministic advisory scaffold. Otherwise follow this bounded flow:

1. Specify the repository/ref, task, host, budget, data classes, authority and measurable acceptance criteria. Preserve the user's chosen stack. Inspect existing harness files before generating replacements.
2. Check the reviewed CLI version and `--help`. Upstream currently documents `npx metaharness score <repo>` for read-only suitability scoring, and `npx metaharness my-bot --template vertical:coding --host claude-code` for a coding starter. Pin a reviewed version before repeatable execution. Never interpolate an untrusted goal into a shell command.
3. Generate into an isolated directory. Inspect the resulting files and manifest before installing dependencies or running scripts. Keep only the tools the target requires. A host unable to enforce a required restriction needs an actual sandbox; do not silently drop the restriction.
4. Evaluate a fixed baseline and candidate on held-out cases. Record input revision, dependency locks, commands, result hashes, sample count, failures, cost, cold start and p50/p95 latency. Distinguish local dispatch speed from model quality and end-to-end task completion.
5. Promote only when the candidate improves the declared objective, respects the budget, introduces no unacceptable regression, and has a tested rollback. Evaluation must be independent of the candidate. A plan or self-reported pass cannot authorize promotion.
6. Publish or merge when authorized in the task and the gates pass. Preserve evidence and rollback. Never add a schedule or indefinite self-improvement loop without authorization.

Scope reusable memory to the repo and principal. Store validated patterns with provenance; retrieve before repeating an expensive experiment. Do not retain secrets or treat previous outcomes as proof for a new environment.
