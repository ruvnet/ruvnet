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

The optional paths begin with [RuVector](https://github.com/ruvnet/ruvector),
[MetaHarness](https://github.com/ruvnet/metaharness), and [Ruflo](https://github.com/ruvnet/ruflo).
