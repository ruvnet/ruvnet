#!/usr/bin/env python3
"""Reconcile the source and download baselines and create a review queue."""
from __future__ import annotations

import argparse
import collections
import hashlib
import json
import pathlib
import re

PILOTS = {"@ruvector/kge", "@metaharness/host-github-actions", "@ruvector/rvf-mcp-server"}
ENTRY = {"@claude-flow/cli", "@metaharness/darwin", "agentdb", "agentic-flow", "agentic-robotics",
         "dream-machine", "metaharness", "neural-trader", "qudag", "ruflo", "ruvector"}
MIGRATION = {"@ruvnet/agent-harness-generator", "aidefense", "claude-flow", "claude-flow-v3",
             "ruvector-attention-unified-wasm", "ruvector-attention-wasm", "ruvector-core",
             "ruvector-gnn-wasm", "ruvector-graph-transformer-wasm", "ruvector-math-wasm",
             "ruvector-sona", "ruvector-wasm"}
PLATFORM = re.compile(r"(?:^|-)(?:darwin|linux|win32|freebsd|android)-(?:arm64|x64|arm|ia32|riscv64)(?:-|$)")


def lane(name):
    leaf = name.split("/")[-1]
    if name in PILOTS:
        return "pilot"
    if name in ENTRY:
        return "entry_point"
    if PLATFORM.search(leaf):
        return "platform_artifact"
    if name in MIGRATION:
        return "migration_review"
    if leaf.startswith(("host-", "example-", "plugin-")) or leaf.endswith("-examples"):
        return "adapter_plugin_example"
    if name.startswith(("@ruvector/", "@metaharness/", "@claude-flow/")):
        return "feature_fit_review"
    return "discovery_ownership_review"


def unique_rows(data):
    rows = {row["name"]: row for row in data["packages"]}
    if len(rows) != len(data["packages"]):
        raise ValueError("duplicate package IDs")
    return rows


def assemble(source, downloads):
    resolved, ranges = unique_rows(source), unique_rows(downloads)
    if resolved.keys() != ranges.keys():
        raise ValueError("package sets drifted; refresh inventory and replay the same observation")
    if source["frozen_count"] != 405 or downloads["frozen_count"] != 405:
        raise ValueError("expected the 405-package November 8 baseline")
    by_repo = collections.defaultdict(list)
    for name, row in resolved.items():
        dl = ranges[name]
        if any(row[k] != dl[k] for k in ("frozen_cohort", "live_maintainer_listing")):
            raise ValueError("cohort membership drifted")
        reg = row.get("registry") or {}
        if "source_candidate" in reg:
            raise ValueError("unredacted source candidate")
        reg.pop("homepage", None)
        keywords = reg.pop("keywords", None)
        reg["published_keyword_count"] = len(keywords) if isinstance(keywords, list) else None
        if row.get("source"):
            row["source"].pop("push_permission", None)
        row["downloads"] = dl["downloads"]
        row["proposed_lane"] = lane(name)
        row["homepage_target"] = "https://ruv.io"
        if (row["status"] == "source_verified" and row["source"].get("match_kind") == "registry_directory"
                and row["source"].get("source_version_matches_registry") is True
                and row["proposed_lane"] not in {"platform_artifact", "migration_review"}):
            by_repo[row["source"]["name"]].append(name)
    frozen_lanes = collections.Counter(row["proposed_lane"] for row in resolved.values() if row["frozen_cohort"])
    expected_lanes = {"pilot": 3, "entry_point": 11, "adapter_plugin_example": 54,
                      "feature_fit_review": 127, "platform_artifact": 80, "migration_review": 12,
                      "discovery_ownership_review": 118}
    if frozen_lanes != expected_lanes:
        raise ValueError(f"frozen queue classes do not reconcile: {frozen_lanes}")
    priority = {"pilot": 0, "entry_point": 1, "adapter_plugin_example": 2}
    batches = []
    for repo, names in sorted(by_repo.items()):
        names.sort(key=lambda n: (priority.get(lane(n), 3), n))
        for start in range(0, len(names), 30):
            batches.append({"repo": repo, "packages": names[start:start+30],
                            "gate": "group shared release templates and verify instructions before edits"})
    batches.sort(key=lambda b: (min(priority.get(lane(n), 3) for n in b["packages"]), b["repo"]))
    return {
        "schema_version": 1, "observed_at": source["observed_at"],
        "downloads_observed_at": downloads["observed_at"],
        "download_observation": downloads.get("download_observation", "live npm range API"),
        "frozen_count": source["frozen_count"], "live_count": source["live_count"],
        "inventory_sources": source["live_inventory_evidence"],
        "download_inventory_sources": downloads["live_inventory_evidence"],
        "all_zero_cohort_days": downloads["all_zero_cohort_days"],
        "dates_without_confirmed_nonzero_count": downloads["dates_without_confirmed_nonzero_count"],
        "coverage": {**source["coverage"], "downloads": downloads["coverage"]["downloads"]},
        "frozen_lanes": frozen_lanes,
        "source_status": collections.Counter(row["status"] for row in resolved.values()),
        "homepage_registry_match_count": sum((r.get("registry") or {}).get("homepage_exact_target") is True
                                             for r in resolved.values()),
        "candidate_batches": batches,
        "packages": [resolved[n] for n in sorted(resolved)],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("resolved", type=pathlib.Path)
    parser.add_argument("downloads", type=pathlib.Path)
    parser.add_argument("output", type=pathlib.Path)
    args = parser.parse_args()
    raw = [p.read_bytes() for p in (args.resolved, args.downloads)]
    result = assemble(*map(json.loads, raw))
    result["input_sha256"] = [hashlib.sha256(s).hexdigest() for s in raw]
    rows = result.pop("packages")
    prefix = json.dumps(result, indent=2, sort_keys=True)[:-2]
    package_lines = ",\n".join("    " + json.dumps(r, sort_keys=True, separators=(",", ":")) for r in rows)
    args.output.write_text(prefix + ',\n  "packages": [\n' + package_lines + "\n  ]\n}\n")
    written = json.loads(args.output.read_text())
    assert list(unique_rows(written)) == [r["name"] for r in rows]
    print(json.dumps({"packages": len(rows), "coverage": result["coverage"],
                      "source_status": result["source_status"], "batches": len(result["candidate_batches"])}))


if __name__ == "__main__":
    main()
