#!/usr/bin/env python3
"""Preview or apply homepage-only edits to a pinned, clean local checkout."""
from __future__ import annotations

import argparse
import json
import pathlib
import re
import subprocess

TARGET = "https://ruv.io"
SAFE_REPO = re.compile(r"ruvnet/[A-Za-z0-9_.-]+\Z", re.I)
SAFE_PATH = re.compile(r"(?:[A-Za-z0-9_.-]+/)*package\.json\Z")
SHA = re.compile(r"[0-9a-f]{40}\Z")


def git(root, *args):
    return subprocess.check_output(["git", "-C", str(root), *args], text=True).strip()


def prepare(root, queue, repo, wave):
    if not SAFE_REPO.fullmatch(repo) or wave < 1:
        raise ValueError("invalid repository or wave")
    if pathlib.Path(git(root, "rev-parse", "--show-toplevel")).resolve() != root:
        raise ValueError("pass the repository root")
    if git(root, "status", "--porcelain=v1", "--untracked-files=all"):
        raise ValueError("use a clean isolated checkout")
    batches = [b for b in queue["candidate_batches"] if b["repo"] == repo]
    if wave > len(batches):
        raise ValueError("requested wave not found")
    packages = batches[wave - 1]["packages"]
    if not 1 <= len(packages) <= 40 or len(packages) != len(set(packages)):
        raise ValueError("invalid wave size or duplicate package")
    rows = {r["name"]: r for r in queue["packages"]}
    head = git(root, "rev-parse", "HEAD")
    edits, seen = [], set()
    for name in packages:
        row = rows[name]
        source = row.get("source") or {}
        manifest = source.get("manifest_path")
        blob = source.get("manifest_blob")
        if (row["status"] != "source_verified" or source.get("match_kind") != "registry_directory"
                or source.get("source_version_matches_registry") is not True
                or source.get("name") != repo or source.get("commit") != head):
            raise ValueError(f"{name}: exact fresh source required; recollect after branch drift")
        if (not isinstance(manifest, str) or not SAFE_PATH.fullmatch(manifest)
                or any(part in {".", ".."} for part in manifest.split("/"))
                or not isinstance(blob, str) or not SHA.fullmatch(blob) or manifest in seen):
            raise ValueError(f"{name}: invalid or duplicate source path")
        seen.add(manifest)
        path = root / manifest
        if path.resolve() != path or not path.is_file() or path.stat().st_size > 1_000_000:
            raise ValueError(f"{name}: source must be a regular, bounded file inside the checkout")
        if git(root, "hash-object", "--", manifest) != blob:
            raise ValueError(f"{name}: local manifest differs from the verified blob")
        raw = path.read_bytes()
        contents = json.loads(raw)
        if contents.get("name") != name:
            raise ValueError(f"{name}: unexpected source manifest name")
        if contents.get("homepage") == TARGET:
            continue
        edited = dict(contents, homepage=TARGET)
        indent = re.search(rb"\n([\t ]+)\"", raw)
        line_ending = "\r\n" if b"\r\n" in raw else "\n"
        output = json.dumps(edited, ensure_ascii=False, indent=indent.group(1).decode() if indent else 2)
        output = output.replace("\n", line_ending) + line_ending
        if {k for k in contents.keys() | edited.keys() if contents.get(k) != edited.get(k)} != {"homepage"}:
            raise ValueError("unexpected semantic edit")
        edits.append((name, path, output))
    return head, edits


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("baseline", type=pathlib.Path)
    parser.add_argument("repository")
    parser.add_argument("checkout", type=pathlib.Path)
    parser.add_argument("--wave", type=int, default=1)
    parser.add_argument("--apply", action="store_true", help="write only to the isolated local checkout")
    args = parser.parse_args()
    root = args.checkout.resolve()
    head, edits = prepare(root, json.loads(args.baseline.read_text()), args.repository, args.wave)
    if args.apply:
        # Preflight the complete wave before writing any file; no commits or network writes.
        for _, path, contents in edits:
            path.write_bytes(contents.encode())
    print(json.dumps({"repository": args.repository, "verified_head": head, "applied_locally": args.apply,
                      "packages": [{"name": n, "path": str(p.relative_to(root))} for n, p, _ in edits]}, indent=2))


if __name__ == "__main__":
    main()
