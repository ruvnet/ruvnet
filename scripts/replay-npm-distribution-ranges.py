#!/usr/bin/env python3
"""Recompute a frozen range from recorded provider responses, without changing dates."""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import pathlib
import urllib.parse


def load_collector():
    path = pathlib.Path(__file__).with_name("collect-npm-distribution.py")
    spec = importlib.util.spec_from_file_location("distribution_collector", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def replay(baseline, published_snapshot, cache, collector):
    start, end = published_snapshot["requested_start"], published_snapshot["requested_end"]
    evidence = {r["package"]: r for r in published_snapshot["packages"]}
    if len(evidence) != len(published_snapshot["packages"]):
        raise ValueError("duplicate published receipt")
    frozen = {r["name"] for r in baseline["packages"] if r["frozen_cohort"]}
    if len(frozen) != 405 or frozen != set(evidence):
        raise ValueError("frozen registry receipts do not reconcile")
    expected = set(collector.dates(collector.WINDOWS[0][1], collector.WINDOWS[-1][2]))
    ranges = {}
    for name in sorted(frozen):
        url = f"{collector.DOWNLOADS}/{start}:{end}/{urllib.parse.quote(name, safe='')}"
        path = cache / (hashlib.sha256(url.encode()).hexdigest() + ".json")
        if not path.is_file():
            ranges[name] = {"error": "historical_provider_response_unavailable"}
            continue
        raw = path.read_bytes()
        body, receipt = json.loads(raw)
        expected_receipt = evidence[name]
        if (receipt["source"] != url or receipt["response_sha256"] != expected_receipt["response_sha256"]
                or receipt["retrieved_at"] != expected_receipt["retrieved_at"] or body["package"] != name):
            raise ValueError("recorded registry response identity or receipt mismatch")
        counts = {}
        for row in body["downloads"]:
            day, value = row["day"], row["downloads"]
            if day not in expected:
                continue
            if day in counts or type(value) is not int or value < 0:
                raise ValueError("invalid recorded daily value")
            counts[day] = value
        ranges[name] = {
            "dates": counts, "collection_kind": "recomputed_from_frozen_registry_response",
            "evidence": {"url": url, "observed_at": receipt["retrieved_at"],
                         "sha256": receipt["response_sha256"],
                         "checkpoint_sha256": hashlib.sha256(raw).hexdigest()},
        }
    all_zero, unknown = collector.summarize(ranges)
    return {"frozen_count": baseline["frozen_count"], "live_count": baseline["live_count"],
            "observed_at": published_snapshot["retrieved_at"],
            "live_inventory_evidence": baseline["live_inventory_evidence"],
            "download_observation": "recomputed from recorded official range API responses",
            "all_zero_cohort_days": all_zero, "dates_without_confirmed_nonzero_count": unknown,
            "coverage": {"downloads": sum("evidence" in r for r in ranges.values())},
            "packages": [{"name": r["name"], "frozen_cohort": r["frozen_cohort"],
                          "live_maintainer_listing": r["live_maintainer_listing"],
                          "downloads": ranges.get(r["name"], {"error": "outside_frozen_registry_observation"})}
                         for r in baseline["packages"]]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for field in ("baseline", "published_snapshot", "cache", "output"):
        parser.add_argument(field, type=pathlib.Path)
    args = parser.parse_args()
    result = replay(json.loads(args.baseline.read_text()), json.loads(args.published_snapshot.read_text()),
                    args.cache, load_collector())
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"coverage": result["coverage"], "unknown_days": result["dates_without_confirmed_nonzero_count"]}))


if __name__ == "__main__":
    main()
