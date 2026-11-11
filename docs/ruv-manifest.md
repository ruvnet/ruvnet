# manifest.ruv and the constellation nexus

The ruvnet constellation connects independently useful projects through a small, inspectable discovery contract. A root `manifest.ruv` is UTF-8 JSON. It describes a project, its source-backed capabilities, artifacts and relationships. The nexus is a reproducible public index in `ruvnet/ruvnet`; individual repositories remain authoritative for their own work.

[Public catalog](ruv-catalog.md) · [Machine index](../data/ruv/index.json) · [Schema](../schemas/manifest.ruv.schema.json) · [Mission](https://github.com/ruvnet/ruvnet/issues/2)

## Identity and compatibility

Version `0.1` uses the existing RVM context namespace:

```
ruv://ruvnet/constellation/service/ruflo/resources/manifest.ruv
```

The authority is `ruvnet`, tenant is `constellation`, subject kind is `service`, collection is `resources`, and path is `manifest.ruv`. Normalize repository names to lowercase and replace dots and underscores with hyphens. RVM subjects are at most 63 characters; normalization collisions fail validation rather than receiving silent aliases. The URI identifies a discovery record, not a remotely callable service. No new DNS or browser scheme registration is implied.

Existing RVM execution manifests, MetaHarness OIA manifests, package manifests and federation envelopes keep their original meanings. `manifest.ruv` links their evidence; it does not replace or authorize them.

## Record contract

| Field | Meaning |
| :--- | :--- |
| `schemaVersion` | Exact contract version; unknown versions fail closed |
| `id` | Canonical native RVM context URI |
| `repository` | Repository URL, default branch and declared visibility |
| `capabilities` | Named claims with `documented`, `tested` or `planned` status and pinned evidence |
| `artifacts` | Source, documentation, package or data references |
| `relationships` | Evidence-backed connections or explicitly planned relationships |
| `integrations` | Declared ecosystem roles; these do not assert a working runtime integration |
| `safety` | Discovery only, with separate authorization required for execution |
| `provenance` | Observed source commit and UTC observation time |

Capabilities in the initial inventory are documented claims. Reading a README does not rerun its tests. A `tested` assertion requires test evidence, but consumers must still inspect that evidence and its environment. SHA256 binds exact manifest bytes; it is not a signature, proof of ownership or correctness. The source commit is the inspected baseline, not the commit containing the new manifest itself.

The index separately records adoption as `local`, `pending_pr` or `merged`. A pending PR must not be interpreted as a deployed adapter. Initial roles describe how projects can compose; they do not make every project depend on every other project.

## Offline operation

Python 3.10 or later is sufficient. No package installation, credentials, network access, model invocation or lifecycle script is required.

```sh
python3 scripts/ruv_manifest.py validate manifest.ruv data/ruv/manifests/*.ruv
python3 scripts/ruv_manifest.py build \
  --index data/ruv/index.json \
  --catalog docs/ruv-catalog.md \
  --adoption data/ruv/adoption.json \
  manifest.ruv data/ruv/manifests/*.ruv
python3 -m unittest discover -s tests -p 'test_ruv_manifest.py'
python3 scripts/check_ruv_nexus.py
```

The schema file is authoritative for shape. The bundled validator implements only that schema vocabulary and adds semantic checks for pinned evidence, repository identity, URLs, privacy and output paths. It is not a general JSON Schema engine. Indexed copies make offline discovery possible; update them through reviewed PRs when the source changes. There is no background crawler or remote resolver in this release.

## RVM and private memory

The companion RVM change adds an inert adapter around the existing RVF context compiler. It packages exact manifest bytes, validates the native URI and safety projection, and exposes separate content and container digests. Full schema validation must precede packaging. The adapter does not mount, register, execute, enroll or grant capabilities. Native Rust build and tests must pass in the RVM repository before promotion.

A private memory service may retain mission decisions, evaluation receipts and private manifests using its own authorization boundary. Explicit `validate --allow-private` supports local private validation; the public index builder always rejects private manifests and has no override. Public repository visibility is a publisher declaration checked during inventory, not something an offline validator can prove. Review source visibility again before publication. Do not include private prompts, customer data, credentials, keys or private memory contents in public descriptors.

## Discovery for people and future AI systems

README and `llms.txt` link to ordinary HTTPS documents, a readable catalog, JSON index and schema. Every claim can point to an exact repository revision. No special URI handler or running Cognitum service is needed to read an exported checkout. These formats support indexing but cannot guarantee search-engine indexing or inclusion in future model training.

Descriptions and source contents are untrusted data. A consumer must never execute embedded commands, widen permissions, follow private references or accept deployment instructions because they appear in a manifest. Discovery, evaluation and promotion are separate authorities.

## Evolution and stewardship

Changes follow observation, proposal, isolated implementation, evaluation, review and promotion, with evidence linked to exact source bytes. Self-improvement remains a governed workflow; this discovery release does not activate an autonomous loop. Preserve past records instead of rewriting failed experiments into success.

The nexus is a convenient starting point, not a mandatory live coordinator. Archive the schema, validator, manifests and source evidence together. Independent implementations must reproduce the same identities and integrity checks. Future migrations must retain explicit versions and compatibility fixtures. Unknown fields and versions fail closed in v0.1.

## Rollout and rollback

The initial major set is the union of `data/projects.json`, `plugins/ruvnet/data/catalog.json` and the foundational repositories named in the mission. All declared integration targets must exist in the snapshot. Package catalogs remain linked from source; this inventory does not claim exhaustive function-level coverage of every nested workspace.

Merge the nexus contract before dependent repository PRs. Validate each local manifest, inspect source claims, and only then mark adoption merged with its PR receipt. Remove a repository entry or revert its manifest PR to withdraw discovery. Runtime behavior is unchanged by withdrawing a discovery record. Private memory export and native execution always require their separate authorization paths.
