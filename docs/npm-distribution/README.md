# Ruvnet npm distribution

This rollout makes it easier to find and use Ruvnet packages together. The
baseline reconciles the [November 8 npm inventory](../../data/snapshots/2026-11-08/npm-inventory.json)
with the current public registry. See [ruv.io](https://ruv.io) for the ecosystem.

![Package distribution: discover a workflow, run its quickstart, adopt a package](distribution.svg)

Read the [decision and release gates](ADR-001.md). A source manifest match is
evidence of where to work, not evidence that a quickstart works or that npm
has been updated.

## Reproduce the baseline

Run from the repository root with Python 3.10 or later, a connection to the
public npm APIs, and the existing read-only GitHub CLI connection for source
verification. Use a new cache directory for each collection unless resuming
the same observation.

```sh
python3 scripts/collect-npm-distribution.py \
  --inventory data/snapshots/2026-11-08/npm-inventory.json \
  --cache /tmp/ruvnet-npm-distribution-observation \
  --output /tmp/ruvnet-npm-distribution.json
python3 scripts/resolve-npm-distribution-source.py \
  /tmp/ruvnet-npm-distribution.json /tmp/ruvnet-npm-distribution-verified.json
python3 scripts/assemble-npm-distribution.py \
  /tmp/ruvnet-npm-distribution-verified.json /tmp/ruvnet-npm-distribution.json \
  /tmp/ruvnet-npm-distribution-public.json
```

The expected output is a JSON row per frozen or live package and a source
verification count on stdout. Compare coverage fields with the package count.
An unknown window is null; a date with no confirmed nonzero cohort observation
is treated as unknown pending provider confirmation. The public queue keeps
exact homepage compliance and keyword counts; raw published metadata is in
the local baseline. Source matches inferred from paths require manual review
before batching. Unpacked archive size is **not** cold installed
size; the latter is measured for a release candidate and its pinned baseline.
Collection never installs a package or publishes a release.

## November 8 baseline

The [package queue](../../data/npm-distribution/baseline-2026-11-08.json)
contains 405 frozen packages and three newly observed platform packages.
All 408 published manifests were read. The public source verifier matched
194 source manifests, of which 156 were at the registry-declared location
and 38 were unique matches in the candidate path search. The latter need
manual review before batching. The other packages retain explicit blockers.
Only 32 published npm homepages exactly matched the target at observation.

The October and November 1 through 7 counts were recomputed for all 405
frozen packages from the recorded official npm API range responses, verified
against the receipt digests and timestamps in the [dated snapshot](../../data/snapshots/2026-11-08/npm-downloads.json).
They total 15,468,028 and 5,874,942 observed events respectively. Six October
days remain unknown; the three newly listed packages are outside this frozen
download observation. These values are dated source replays, not fresh range
observations. To reproduce this mode with the original response cache:

```sh
python3 scripts/replay-npm-distribution-ranges.py \
  /tmp/ruvnet-npm-distribution-verified.json \
  data/snapshots/2026-11-08/npm-downloads.json \
  /path/to/recorded-registry-cache /tmp/ruvnet-npm-distribution-replayed.json
```

Pass the replay output as the second input to the assembler. The public
report retains source times and does not fill missing dates with zero.

An [independent range recheck](../../data/npm-distribution/range-recheck-2026-11-08.json)
matched all 376 comparable package totals. The other 32 are still unknown
in that recheck: 29 rate limits and three unavailable range responses for
newly listed builds. The recheck does not overwrite the dated baseline.

## Preview a metadata wave

In an isolated checkout of the owning project, at the source commit recorded
in the public queue, preview a batch before changing any files:

```sh
python3 scripts/prepare-npm-homepage-wave.py \
  /tmp/ruvnet-npm-distribution-public.json ruvnet/metaharness /path/to/checkout
```

Add `--apply` only after review. It edits local homepage fields only. It
refuses a dirty checkout, changed source commit, manifest blob mismatch,
symlinks and ambiguous package paths. Readme, dependency, topic and release
changes remain separate review gates. The script never commits or pushes.

The optional paths begin with [RuVector](https://github.com/ruvnet/ruvector),
[MetaHarness](https://github.com/ruvnet/metaharness), and [Ruflo](https://github.com/ruvnet/ruflo).
The source changes are tracked in [RuVector #1409](https://github.com/ruvnet/RuVector/pull/1409),
[MetaHarness #480](https://github.com/ruvnet/metaharness/pull/480), and
[Ruflo #4896](https://github.com/ruvnet/ruflo/pull/4896). The next source waves
cover [27 MetaHarness examples](https://github.com/ruvnet/metaharness/pull/481),
[22 RuVector platform packages](https://github.com/ruvnet/RuVector/pull/1413),
and [21 Ruflo manifests](https://github.com/ruvnet/ruflo/pull/4897).
The RVF server package's own metadata and guide are tracked in
[RuVector #1414](https://github.com/ruvnet/RuVector/pull/1414).
The pull requests describe what was tested; published npm versions are separate.

Before changing a platform package, confirm the generator actually used by
the active release route. For example, Attention has two routes that must
agree. A historical git head can explain an old package name without proving
that the release route is still active. Keep historical aliases and platforms
with no current release route in review.

## Weave the next integration

[ADR 002](ADR-002.md) defines the review loop. Run the offline planner:

```sh
python3 scripts/package-weave.py
```

The report reconciles the dated registry inventory and manifest graph, shows
required versus possible reach by flagship, lists gaps, and returns the
single next candidate to test. Pass `--baseline`, `--inventory`, or
`--overlay` to point it at a newer observation; use `--no-overlay` to
inspect the frozen graph. The small November 10 overlay uses the existing
distribution collector's manifest logic and stores exact registry response
hashes and times. It is a targeted refresh, not a fresh crawl of every node.

The first two recipes are isolated from the flagships. Run from repository
root with Node 22 or later:

```sh
for recipe in rvf-memory native-routing; do
  npm ci --ignore-scripts --prefix "docs/npm-distribution/recipes/$recipe"
  node "docs/npm-distribution/recipes/$recipe/verify.mjs" > "/tmp/$recipe.json"
done
python3 scripts/package-weave.py \
  --receipt /tmp/rvf-memory.json --receipt /tmp/native-routing.json
```

The RVF receipt should report two persisted records, retrieval of
`release-notes`, and exclusion of `distractor`. Routing should select
`small` and then `large` on the fixed inputs, verify the native engine ran,
and observe TypeScript selection in a clean process without Tiny Dancer.
That fixture checks integration behavior; it is not a production routing
benchmark. The checked-in receipts cover Linux x64 only.

With no explicit receipts, the planner reads the versioned
[observations](../../data/npm-distribution/weave-receipts). Supply the full
desired receipt set when using `--receipt`. A different lock or script makes
an older receipt stale. A reviewer must validate evidence and supported
platforms before any owning repository changes; the planner cannot add
dependencies, publish, or activate itself.
