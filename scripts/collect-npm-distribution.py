#!/usr/bin/env python3
"""Collect an evidence-only npm rollout baseline; never install or publish."""
from __future__ import annotations

import argparse
import concurrent.futures
import datetime as dt
import hashlib
import json
import pathlib
import re
import time
import urllib.error
import urllib.parse
import urllib.request

REGISTRY = "https://registry.npmjs.org"
DOWNLOADS = "https://api.npmjs.org/downloads/range"
PACKAGE = re.compile(r"(?:@[a-z0-9._-]+/)?[a-z0-9._-]+\Z")
REPO = re.compile(r"[A-Za-z0-9_.-]+\Z")
EDGE_FIELDS = ("dependencies", "optionalDependencies", "peerDependencies", "devDependencies")
WINDOWS = (("october", "2026-10-01", "2026-10-31"),
           ("november_1_to_7", "2026-11-01", "2026-11-07"))

class RegistryRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        source, target = map(urllib.parse.urlsplit, (req.full_url, newurl))
        if target.scheme != "https" or target.netloc != source.netloc:
            raise ValueError("redirect changed registry origin")
        return super().redirect_request(req, fp, code, msg, headers, newurl)


HTTP = urllib.request.build_opener(RegistryRedirect())


def now():
    return dt.datetime.now(dt.timezone.utc).isoformat()


def fetch(url, attempts=4):
    if urllib.parse.urlsplit(url).hostname not in {"registry.npmjs.org", "api.npmjs.org"}:
        raise ValueError("unsupported origin")
    for attempt in range(attempts):
        try:
            request = urllib.request.Request(url, headers={
                "Accept": "application/json", "User-Agent": "ruvnet-npm-distribution-baseline/1"})
            with HTTP.open(request, timeout=22) as response:
                if urllib.parse.urlsplit(response.geturl()).hostname != urllib.parse.urlsplit(url).hostname:
                    raise ValueError("redirect changed origin")
                raw = response.read(8_000_001)
            if len(raw) > 8_000_000:
                raise ValueError("response exceeds bound")
            return json.loads(raw), {"url": url, "sha256": hashlib.sha256(raw).hexdigest(), "observed_at": now()}
        except (urllib.error.URLError, TimeoutError) as exc:
            code = getattr(exc, "code", None)
            if attempt + 1 == attempts or (code is not None and code not in {429, 500, 502, 503, 504}):
                raise
            retry = (exc.headers.get("Retry-After") if isinstance(exc, urllib.error.HTTPError) else None)
            time.sleep(max(2 ** attempt, min(120, int(retry))) if retry and retry.isdigit() else 2 ** attempt)


def safe_text(value, maximum=500):
    return value if isinstance(value, str) and len(value) <= maximum and value.isprintable() else None


def safe_homepage(value):
    if not safe_text(value):
        return None
    try:
        parsed = urllib.parse.urlsplit(value)
    except ValueError:
        return None
    if parsed.scheme not in {"http", "https"} or not parsed.hostname or parsed.username or parsed.password:
        return None
    return urllib.parse.urlunsplit((parsed.scheme, parsed.netloc, parsed.path, "", ""))


def dependency_edges(metadata):
    out = {}
    for field in EDGE_FIELDS:
        group = metadata.get(field, {})
        if not isinstance(group, dict):
            raise ValueError("malformed dependency map")
        out[field] = {n: v if isinstance(v, str) and len(v) <= 200
                         and re.fullmatch(r"[0-9a-zA-Z .*^~<>=|+_-]+", v) else None
                      for n, v in group.items() if PACKAGE.fullmatch(n)}
    return out


def github_source(repository):
    """Return only an exact public-cohort candidate; verify the repo separately."""
    raw = repository.get("url") if isinstance(repository, dict) else repository
    if not isinstance(raw, str):
        return None
    raw = raw.removeprefix("git+")
    if raw.startswith("git@github.com:"):
        raw = "ssh://git@github.com/" + raw.split(":", 1)[1]
    if raw.startswith("github:"):
        raw = "https://github.com/" + raw[len("github:"):]
    if re.fullmatch(r"ruvnet/[A-Za-z0-9_.-]+", raw, re.I):
        raw = "https://github.com/" + raw
    try:
        parsed = urllib.parse.urlsplit(raw)
    except ValueError:
        return None
    if (parsed.scheme not in {"https", "http", "ssh", "git"} or parsed.netloc not in
            {"github.com", "git@github.com"} or parsed.query or parsed.fragment):
        return None
    parts = parsed.path.strip("/").split("/")
    if len(parts) != 2 or parts[0].lower() != "ruvnet":
        return None
    slug = parts[1].removesuffix(".git")
    if slug in {"", ".", ".."} or not REPO.fullmatch(slug):
        return None
    directory = repository.get("directory") if isinstance(repository, dict) else None
    if directory not in (None, ""):
        if (not isinstance(directory, str) or directory.startswith("/") or "\\" in directory
                or any(p in {"", ".", ".."} or not REPO.fullmatch(p) for p in directory.split("/"))):
            return None
    return {"repo": "ruvnet/" + slug, "directory": directory or None}


def inventory():
    names, sources, offset = set(), [], 0
    declared = None
    while offset < 10_000:
        query = urllib.parse.urlencode({"text": "maintainer:ruvnet", "size": 250, "from": offset})
        body, source = fetch(f"{REGISTRY}/-/v1/search?{query}")
        total = body["total"]
        if type(total) is not int or total < 1 or (declared is not None and total != declared):
            raise ValueError("maintainer inventory total changed between pages")
        declared = total
        rows = [item["package"]["name"] for item in body["objects"]]
        if any(not PACKAGE.fullmatch(n) for n in rows) or len(set(rows)) != len(rows) or names.intersection(rows):
            raise ValueError("invalid or overlapping maintainer pagination")
        sources.append({"offset": offset, "rows": len(rows), "reported_total": body["total"], **source})
        names.update(rows)
        offset += len(rows)
        if offset == body["total"]:
            return names, sources
        if not rows or offset > body["total"]:
            break
    raise ValueError("maintainer pagination incomplete")


def latest(name):
    metadata, evidence = fetch(f"{REGISTRY}/{urllib.parse.quote(name, safe='')}/latest")
    if metadata.get("name") != name:
        raise ValueError("manifest identity mismatch")
    maintainers = metadata.get("maintainers")
    maintainer = (any(isinstance(m, dict) and m.get("name") == "ruvnet" for m in maintainers)
                  if isinstance(maintainers, list) else None)
    keywords = metadata.get("keywords")
    version = safe_text(metadata.get("version"), 100)
    if not version:
        raise ValueError("manifest version unavailable")
    size = metadata.get("dist", {}).get("unpackedSize")
    readme = metadata.get("readme")
    return {
        "version": version, "homepage": safe_homepage(metadata.get("homepage")),
        "homepage_exact_target": (metadata.get("homepage") == "https://ruv.io"
                                  if "homepage" in metadata else None),
        "keywords": [k for k in keywords[:100] if safe_text(k, 100)] if isinstance(keywords, list) else None,
        "manifest_readme": bool(readme) if isinstance(readme, str) else None,
        "dependency_edges": dependency_edges(metadata),
        "published_unpacked_bytes": size if type(size) is int and size >= 0 else None,
        "deprecated": bool(metadata.get("deprecated")),
        "maintainer_in_latest_manifest": maintainer,
        "source_candidate": github_source(metadata.get("repository")),
        "source_candidate_verified": False, "registry_evidence": evidence,
    }


def dates(start, end):
    begin, finish = dt.date.fromisoformat(start), dt.date.fromisoformat(end)
    return [(begin + dt.timedelta(days=i)).isoformat() for i in range((finish - begin).days + 1)]


def range_counts(name):
    start, end = WINDOWS[0][1], WINDOWS[-1][2]
    body, evidence = fetch(f"{DOWNLOADS}/{start}:{end}/{urllib.parse.quote(name, safe='')}")
    if body.get("package") != name:
        raise ValueError("range package identity mismatch")
    observed = {}
    days = set(dates(start, end))
    for row in body["downloads"]:
        k, value = row["day"], row["downloads"]
        if k in observed or type(value) is not int or value < 0 or k not in days:
            raise ValueError("invalid daily range response")
        observed[k] = value
    return {"dates": observed, "evidence": evidence}


def checkpointed(cache, operation, name):
    path = cache / (hashlib.sha256(f"{operation.__name__}:{name}".encode()).hexdigest() + ".json")
    if path.exists():
        return json.loads(path.read_text())
    try:
        result = operation(name)
    except (ValueError, KeyError, TypeError, urllib.error.URLError, TimeoutError) as exc:
        return {"error": type(exc).__name__, "http_status": getattr(exc, "code", None)}
    tmp = path.with_suffix(".tmp")
    tmp.write_text(json.dumps(result, sort_keys=True))
    tmp.replace(path)
    return result


def summarize(results):
    expected = dates(WINDOWS[0][1], WINDOWS[-1][2])
    usable = [r["dates"] for r in results.values() if "dates" in r]
    if any(set(series) - set(expected) for series in usable):
        raise ValueError("checkpoint contains a date outside the canonical calendar")
    all_zero = {day for day in expected if len(usable) == len(results) and usable
                and all(series.get(day) == 0 for series in usable)}
    # Missing responses cannot turn a date with no observed nonzero value into a verified zero.
    unknown = {day for day in expected if not any((series.get(day) or 0) > 0 for series in usable)}
    for result in results.values():
        if "dates" not in result:
            result["windows"] = {label: None for label, _, _ in WINDOWS}
            continue
        rows = result.pop("dates")
        result["windows"] = {}
        for label, start, end in WINDOWS:
            window = dates(start, end)
            counts = [rows[day] for day in window if day in rows and day not in unknown]
            result["windows"][label] = {"observed_download_events": sum(counts) if counts else None,
                                          "expected_days": len(window), "observed_days": len(counts)}
    return sorted(all_zero), sorted(unknown)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--inventory", type=pathlib.Path, required=True)
    parser.add_argument("--cache", type=pathlib.Path, required=True)
    parser.add_argument("--output", type=pathlib.Path, required=True)
    parser.add_argument("--phase", choices=["metadata", "downloads", "all"], default="all")
    args = parser.parse_args()
    args.cache.mkdir(parents=True, exist_ok=True)
    frozen = json.loads(args.inventory.read_text())["packages"]
    if len(frozen) != len(set(frozen)) or not frozen or any(not PACKAGE.fullmatch(n) for n in frozen):
        raise ValueError("invalid frozen package inventory")
    live, sources = inventory()
    names = sorted(set(frozen) | live)
    groups = {}
    for operation, workers in ((latest, 4), (range_counts, 2)):
        if args.phase not in {"all", "metadata" if operation is latest else "downloads"}:
            continue
        with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as pool:
            groups[operation.__name__] = {}
            for index, (name, result) in enumerate(zip(names, pool.map(
                    lambda name: checkpointed(args.cache, operation, name), names)), 1):
                groups[operation.__name__][name] = result
                if index % 50 == 0 or index == len(names):
                    print(f"{operation.__name__}: {index}/{len(names)}", flush=True)
    counts = groups.get("range_counts", {})
    all_zero, unknown = summarize(counts) if counts else (None, None)
    metadata = groups.get("latest", {})
    rows = [{"name": n, "frozen_cohort": n in frozen, "live_maintainer_listing": n in live,
             "registry": metadata.get(n), "downloads": counts.get(n)} for n in names]
    out = {"schema_version": 1, "observed_at": now(), "frozen_count": len(frozen), "live_count": len(live),
           "live_inventory_evidence": sources, "all_zero_cohort_days": all_zero,
           "dates_without_confirmed_nonzero_count": unknown,
           "coverage": {"metadata": sum("version" in r for r in metadata.values()),
                        "downloads": sum("evidence" in r for r in counts.values())},
           "packages": rows}
    tmp = args.output.with_suffix(".tmp")
    tmp.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
    tmp.replace(args.output)


if __name__ == "__main__":
    main()
