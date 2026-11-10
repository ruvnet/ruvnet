#!/usr/bin/env python3
"""Plan the next bounded npm integration from published metadata and receipts."""

import argparse
from datetime import datetime
import hashlib
import json
from pathlib import Path
import re
from urllib.parse import quote


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data/npm-distribution"
RUNTIME_KINDS = ("dependencies", "optionalDependencies", "peerDependencies")
EXACT = re.compile(r"(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)")
ID = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")
PLATFORM = re.compile(r"[a-z0-9_-]+/[a-z0-9_-]+")


def unique(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def timestamp(value):
    result = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if result.tzinfo is None:
        raise ValueError("manifest observation timestamp must include a time zone")
    return result


def merge_overlay(baseline, inventory, overlay):
    if overlay is None:
        return baseline
    names = set(inventory["packages"])
    source_rows = baseline["packages"]
    merged = {row["name"]: row for row in source_rows}
    if len(merged) != len(source_rows):
        raise ValueError("duplicate package row")
    observed = set()
    if overlay["schema_version"] != 1:
        raise ValueError("unsupported manifest overlay")
    for row in overlay["packages"]:
        name, manifest = row["name"], row["registry"]
        evidence = manifest["registry_evidence"]
        if (name not in names or name in observed
                or manifest["maintainer_in_latest_manifest"] is not True
                or evidence["url"] != f"https://registry.npmjs.org/{quote(name, safe='')}/latest"
                or not re.fullmatch(r"[0-9a-f]{64}", evidence["sha256"])
                or not evidence["observed_at"]):
            raise ValueError(f"invalid manifest overlay row: {name}")
        observed.add(name)
        old_manifest = (merged.get(name, {}).get("registry") or {})
        old_at = (old_manifest.get("registry_evidence") or {}).get("observed_at")
        new_at = timestamp(evidence["observed_at"])
        if not old_at or new_at >= timestamp(old_at):
            merged[name] = row
    return {**baseline, "packages": list(merged.values())}


def graph(baseline):
    rows = baseline["packages"]
    names = {row["name"] for row in rows}
    if len(names) != len(rows):
        raise ValueError("duplicate package row")
    result, missing = {}, []
    for row in rows:
        published = row.get("registry") or {}
        edges = published.get("dependency_edges")
        if edges is None:
            missing.append(row["name"])
        result[row["name"]] = {
            kind: {target for target in (edges or {}).get(kind, {}) if target in names}
            for kind in RUNTIME_KINDS
        }
        # npm optionalDependencies overrides duplicate dependencies entries.
        result[row["name"]]["dependencies"] -= result[row["name"]]["optionalDependencies"]
    return result, sorted(missing)


def reachable(edges, root, kinds):
    seen, pending = {root}, [root]
    while pending:
        node = pending.pop()
        for kind in kinds:
            for target in edges[node][kind] - seen:
                pending.append(target)
                seen.add(target)
    return seen - {root}


def plan(baseline, inventory, policy, receipts, overlay=None):
    edges, missing = graph(merge_overlay(baseline, inventory, overlay))
    current = set(inventory["packages"])
    if len(current) != len(inventory["packages"]):
        raise ValueError("duplicate inventory package")
    roots = policy["entrypoints"]
    if not roots or len(roots) != len(set(roots)) or not set(roots) <= edges.keys():
        raise ValueError("invalid entrypoint list")
    reach = {root: reachable(edges, root, RUNTIME_KINDS) for root in roots}
    all_reached = set(roots).union(*reach.values())

    results = {}
    for receipt in receipts:
        key = receipt["candidate"]
        if key in results:
            raise ValueError(f"duplicate receipt for {key}")
        results[key] = receipt

    decisions, seen = [], set()
    for candidate in policy["candidates"]:
        key = candidate["id"]
        source, target, pins = candidate["from"], candidate["to"], candidate["pins"]
        checks = candidate["checks"]
        mode = candidate["mode"]
        if (not ID.fullmatch(key) or key in seen or source == target
                or {source, target} != pins.keys()
                or any(not EXACT.fullmatch(version) for version in pins.values())
                or not checks or len(checks) != len(set(checks))
                or any(not ID.fullmatch(check) for check in checks)
                or mode not in ("recipe", "required")):
            raise ValueError(f"invalid candidate: {key}")
        seen.add(key)
        receipt = results.get(key)
        check_values = None
        if receipt is not None:
            check_values = receipt["checks"]
            if (receipt["pins"] != pins or set(check_values) != set(checks)
                    or any(v is not None and type(v) is not bool for v in check_values.values())
                    or not PLATFORM.fullmatch(receipt["platform"])
                    or not re.fullmatch(r"[0-9a-f]{64}", receipt["lock_sha256"])
                    or not re.fullmatch(r"[0-9a-f]{64}", receipt["recipe_sha256"])):
                raise ValueError(f"receipt does not match candidate contract: {key}")

        existing = [kind for kind in RUNTIME_KINDS if target in edges.get(source, {}).get(kind, ())]
        if {source, target} - current or {source, target} - edges.keys():
            state = "needs_manifest_baseline"
        elif mode == "required" and (missing or current - edges.keys()):
            state = "blocked_graph_coverage"
        elif mode == "required" and target in edges[source]["dependencies"]:
            state = "already_required"
        elif mode == "required" and source in reachable(edges, target, RUNTIME_KINDS):
            state = "blocked_potential_cycle"
        elif mode == "required":
            state = "requires_owning_repo_review"
        elif receipt is None:
            state = "ready_to_test"
        elif any(value is False for value in check_values.values()):
            state = "needs_revision"
        elif all(value is True for value in check_values.values()):
            state = "observed_pass_review_ready"
        else:
            state = "needs_more_evidence"
        decisions.append({
            "id": key, "from": source, "to": target, "mode": mode,
            "pins": pins, "value": candidate["value"], "state": state,
            "baseline_manifest_relationships": existing,
            "receipt_platform": receipt["platform"] if receipt is not None else None,
            "receipt_lock_sha256": receipt["lock_sha256"] if receipt is not None else None,
            "receipt_recipe_sha256": receipt["recipe_sha256"] if receipt is not None else None,
        })

    if results.keys() - seen:
        raise ValueError("receipt references a candidate outside the policy")
    return {
        "schema_version": 1,
        "baseline_observed_at": baseline.get("observed_at"),
        "inventory_observed_at": inventory.get("retrieved_at"),
        "overlay_observed_at": overlay.get("observed_at") if overlay else None,
        "coverage": {
            "baseline_packages": len(baseline["packages"]), "inventory_packages": len(current),
            "graph_packages": len(edges), "overlay_packages": len(overlay["packages"]) if overlay else 0,
            "new_since_baseline": sorted(current - {row["name"] for row in baseline["packages"]}),
            "inventory_without_graph": sorted(current - edges.keys()),
            "no_longer_listed": sorted(edges.keys() - current),
            "missing_manifest_edges": missing,
            "not_reached_from_entrypoints": len(edges.keys() - all_reached),
        },
        "entrypoints": {
            root: {
                "required_reachable": len(reachable(edges, root, ("dependencies",))),
                "possible_reachable_including_optional_and_peers": len(reach[root]),
            } for root in roots
        },
        "candidates": decisions,
        "next_test": next((row["id"] for row in decisions if row["state"] == "ready_to_test"), None),
        "promotion_authorized": False,
    }


def verify_receipt_artifacts(policy, receipts):
    candidates = {row["id"]: row for row in policy["candidates"]}
    root = ROOT / "docs/npm-distribution/recipes"
    for receipt in receipts:
        recipe = candidates.get(receipt["candidate"], {}).get("recipe")
        if not recipe or not ID.fullmatch(recipe):
            raise ValueError("receipt has no declared local recipe")
        for field, filename in (("recipe_sha256", "verify.mjs"), ("lock_sha256", "package-lock.json")):
            path = root / recipe / filename
            if not path.resolve().is_relative_to(root.resolve()):
                raise ValueError(f"recipe file escapes recipe directory: {recipe}")
            if hashlib.sha256(path.read_bytes()).hexdigest() != receipt[field]:
                raise ValueError(f"receipt artifact digest mismatch: {recipe}/{filename}")


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--baseline", type=Path, default=DATA / "baseline-2026-11-08.json")
    parser.add_argument("--inventory", type=Path, default=ROOT / "data/snapshots/2026-11-10/npm-inventory.json")
    parser.add_argument("--policy", type=Path, default=DATA / "weave-policy.json")
    parser.add_argument("--overlay", type=Path, default=DATA / "weave-manifests-2026-11-10.json")
    parser.add_argument("--no-overlay", action="store_true")
    parser.add_argument("--receipt", action="append", type=Path, default=[])
    args = parser.parse_args(argv)
    try:
        receipts = args.receipt or sorted((DATA / "weave-receipts").glob("*.json"))
        inputs = [args.baseline, args.inventory, args.policy, *receipts]
        if not args.no_overlay:
            inputs.append(args.overlay)
        payloads = [path.read_bytes() for path in inputs]
        baseline, inventory, policy, *receipts = [
            json.loads(payload, object_pairs_hook=unique) for payload in payloads
        ]
        overlay = None if args.no_overlay else receipts.pop()
        verify_receipt_artifacts(policy, receipts)
        report = plan(baseline, inventory, policy, receipts, overlay)
        report["inputs_sha256"] = [hashlib.sha256(payload).hexdigest() for payload in payloads]
        print(json.dumps(report, indent=2, sort_keys=True))
    except (OSError, ValueError, TypeError, KeyError, AttributeError) as error:
        parser.exit(2, f"package weave: {error}\n")


if __name__ == "__main__":
    main()
