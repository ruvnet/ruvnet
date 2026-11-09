#!/usr/bin/env python3
"""Verify npm source candidates against public GitHub commits without writing remotely."""
from __future__ import annotations

import argparse
import base64
import concurrent.futures
import functools
import json
import pathlib
import re
import subprocess
import urllib.parse

OWNER_REPO = re.compile(r"ruvnet/[A-Za-z0-9_.-]+\Z", re.I)
SAFE_DIR = re.compile(r"[A-Za-z0-9_.-]+(?:/[A-Za-z0-9_.-]+)*\Z")
SHA = re.compile(r"[a-f0-9]{40}\Z")


@functools.lru_cache(maxsize=1400)
def api(endpoint):
    try:
        result = subprocess.run(["gh", "api", "--method", "GET", endpoint],
                                capture_output=True, timeout=35, check=False)
    except (OSError, subprocess.TimeoutExpired):
        return None
    if result.returncode:
        # GitHub messages may name private targets. Do not retain or print them.
        return None
    try:
        return json.loads(result.stdout)
    except ValueError:
        return None


def repository(candidate):
    if not isinstance(candidate, str) or not OWNER_REPO.fullmatch(candidate):
        return None
    repo = api("repos/" + candidate)
    if not isinstance(repo, dict) or repo.get("private") is not False or repo.get("visibility") != "public":
        return None
    full_name = repo.get("full_name", "")
    if not OWNER_REPO.fullmatch(full_name):
        return None
    branch = urllib.parse.quote(repo["default_branch"], safe="")
    branch_info = api(f"repos/{full_name}/branches/{branch}")
    head = (branch_info or {}).get("commit", {}).get("sha", "")
    if not SHA.fullmatch(head):
        return None
    tree = api(f"repos/{full_name}/git/trees/{head}?recursive=1")
    if not isinstance(tree, dict) or tree.get("truncated") is not False:
        return None
    return {
        "name": full_name, "id": repo["id"], "commit": head, "archived": repo.get("archived"),
        "push_permission": (repo.get("permissions") or {}).get("push"),
        "website_is_ruv_io": (repo.get("homepage") or "").rstrip("/") == "https://ruv.io",
        "topics": [t for t in repo.get("topics", []) if re.fullmatch(r"[a-z0-9-]{1,50}", t)],
        "paths": {p["path"]: p["sha"] for p in tree.get("tree", [])
                  if p.get("type") == "blob" and p.get("mode") in {"100644", "100755"}
                  and SHA.fullmatch(p.get("sha", ""))},
    }


def manifest_at(repo, path):
    digest = repo["paths"].get(path)
    if not digest:
        return None
    payload = api(f"repos/{repo['name']}/git/blobs/{digest}")
    if not isinstance(payload, dict) or payload.get("encoding") != "base64" or payload.get("sha") != digest:
        return None
    try:
        if type(payload.get("size")) is not int or not 0 <= payload["size"] <= 1_000_000:
            return None
        raw = base64.b64decode(payload["content"])
        if len(raw) != payload["size"]:
            return None
        manifest = json.loads(raw)
    except (ValueError, KeyError, TypeError):
        return None
    return (digest, manifest) if isinstance(manifest, dict) else None


def check_source(row, repo):
    reg = row.get("registry") or {}
    candidate = reg.pop("source_candidate", None)
    row["source"] = None
    row["status"] = "registry_manifest_unavailable"
    if "version" not in reg:
        return row
    if reg.get("maintainer_in_latest_manifest") is not True or not row.get("live_maintainer_listing"):
        row["status"] = "maintainership_not_verified"
        return row
    if not candidate:
        row["status"] = "no_owned_source_in_registry_manifest"
        return row
    if not repo:
        row["status"] = "public_owned_repo_or_complete_tree_not_verified"
        return row
    directory = candidate.get("directory")
    if directory is not None and (not isinstance(directory, str) or not SAFE_DIR.fullmatch(directory)
                                  or any(part in {".", ".."} for part in directory.split("/"))):
        row["status"] = "unsafe_source_directory"
        return row
    prefix = directory + "/" if directory else ""
    manifest = prefix + "package.json"
    row["source"] = {k: v for k, v in repo.items() if k != "paths"}
    row["source"].update({"directory": directory, "manifest_path": None, "manifest_blob": None,
                          "source_readme": None})
    exact = manifest_at(repo, manifest)
    match_kind = "registry_directory"
    if not exact or exact[1].get("name") != row["name"]:
        leaf = row["name"].split("/")[-1]
        candidates = sorted(p for p in repo["paths"] if p != manifest and p.endswith("/package.json")
                            and p.split("/")[-2] in {leaf, "ruvector-" + leaf})
        if len(candidates) > 12:
            row["status"] = "ambiguous_source_candidate_paths"
            return row
        matches = [(p, x) for p in candidates if (x := manifest_at(repo, p)) and x[1].get("name") == row["name"]]
        if len(matches) > 1:
            row["status"] = "ambiguous_exact_manifest_matches"
            return row
        if not matches:
            row["status"] = ("source_manifest_name_mismatch" if exact
                             else "source_manifest_or_platform_template_needs_resolution")
            return row
        manifest, exact = matches[0]
        directory = manifest.rsplit("/", 1)[0]
        prefix = directory + "/"
        match_kind = "exact_name_at_unique_package_path"
    digest, metadata = exact
    readme = next((p for p in (prefix + "README.md", prefix + "readme.md", prefix + "README")
                   if p in repo["paths"]), None)
    row["source"].update({"directory": directory, "manifest_path": manifest, "manifest_blob": digest,
                          "match_kind": match_kind,
                          "source_readme": readme, "source_version_matches_registry":
                          metadata.get("version") == reg["version"]})
    if isinstance(metadata.get("os"), list) and isinstance(metadata.get("cpu"), list):
        row["source"]["verified_kind"] = "platform_build"
    reg["source_candidate_verified"] = True
    row["status"] = "source_verified" if not repo["archived"] and repo["push_permission"] is True else "source_verified_review_access"
    return row


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("baseline", type=pathlib.Path)
    parser.add_argument("output", type=pathlib.Path)
    args = parser.parse_args()
    data = json.loads(args.baseline.read_text())
    rows = data["packages"]
    names_in_cohort = {row["name"] for row in rows}
    for row in rows:
        reg = row.get("registry") or {}
        edges = reg.get("dependency_edges")
        if isinstance(edges, dict):
            reg["external_dependency_counts"] = {
                kind: sum(dep not in names_in_cohort for dep in values) for kind, values in edges.items()}
            reg["dependency_edges"] = {
                kind: {dep: version for dep, version in values.items() if dep in names_in_cohort}
                for kind, values in edges.items()}
    candidates = [((r.get("registry") or {}).get("source_candidate") or {}).get("repo") for r in rows]
    names = sorted({n for n in candidates if n})
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        repositories = dict(zip(names, pool.map(repository, names)))
        data["packages"] = list(pool.map(lambda pair: check_source(pair[0], repositories.get(pair[1])),
                                         zip(rows, candidates)))
    data["coverage"]["source_manifest_verified"] = sum(
        (r.get("registry") or {}).get("source_candidate_verified") is True for r in data["packages"])
    args.output.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print(f"Public source manifests verified: {data['coverage']['source_manifest_verified']}/{len(rows)}")


if __name__ == "__main__":
    main()
