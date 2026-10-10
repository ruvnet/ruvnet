#!/usr/bin/env python3
"""Validate public manifest.ruv records and build offline discovery indexes.

No network access, URI resolution, shell execution, or runtime enrollment. The
JSON Schema constrains the document shape; semantic checks additionally enforce
pinned evidence, public-source boundaries, unique identities, and safe outputs.
Public visibility is a publisher assertion, not an offline proof of GitHub ACLs.
"""

import argparse
import datetime
import hashlib
import html
import json
import os
from pathlib import Path
import re
import sys
import tempfile
from urllib.parse import unquote, urlsplit


SCHEMA_PATH = Path(__file__).resolve().parent.parent / "schemas/manifest.ruv.schema.json"
MAX_MANIFEST_BYTES = 1024 * 1024
ALLOWED_HOSTS = {"github.com", "raw.githubusercontent.com", "www.npmjs.com", "crates.io", "docs.rs"}
SCHEMA_KEYWORDS = {"$schema", "$id", "$defs", "$ref", "title", "description", "type", "const", "enum",
                   "required", "properties", "additionalProperties", "items", "pattern", "minLength", "maxLength"}


class ValidationError(ValueError):
    """A manifest, adoption assertion, or requested output is unsafe or invalid."""


def _object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValidationError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def read_json(path):
    path = Path(path)
    if path.is_symlink() or path.resolve() != path.absolute():
        raise ValidationError(f"symlink input is not permitted: {path}")
    if path.stat().st_size > MAX_MANIFEST_BYTES:
        raise ValidationError(f"JSON input exceeds {MAX_MANIFEST_BYTES} bytes: {path}")
    raw = path.read_bytes()
    try:
        value = json.loads(raw.decode("utf-8"), object_pairs_hook=_object,
                           parse_constant=lambda value: _invalid_constant(value))
    except ValidationError:
        raise
    except (ValueError, RecursionError) as exc:
        raise ValidationError(f"invalid UTF-8 JSON: {path}") from exc
    return value, raw


def _invalid_constant(value):
    raise ValidationError(f"non-JSON numeric constant: {value}")


def check_schema(schema, root=None, location="schema"):
    """Preflight every schema node, including unused definitions and properties."""
    if root is None:
        root = schema
    if not isinstance(schema, dict):
        raise ValidationError(f"{location}: only object schemas are supported")
    if set(schema) - SCHEMA_KEYWORDS:
        raise ValidationError(f"{location}: unsupported schema keywords {sorted(set(schema) - SCHEMA_KEYWORDS)}")
    for key in ("$schema", "$id", "$ref", "title", "description", "pattern"):
        if key in schema and not isinstance(schema[key], str):
            raise ValidationError(f"{location}.{key}: expected string")
    if "type" in schema and schema["type"] not in ("object", "array", "string"):
        raise ValidationError(f"{location}: unsupported schema type")
    if "additionalProperties" in schema and type(schema["additionalProperties"]) is not bool:
        raise ValidationError(f"{location}: additionalProperties must be boolean")
    for key in ("minLength", "maxLength"):
        if key in schema and (type(schema[key]) is not int or schema[key] < 0):
            raise ValidationError(f"{location}.{key}: expected nonnegative integer")
    if "const" in schema and type(schema["const"]) not in (str, bool):
        raise ValidationError(f"{location}: only string or boolean constants are supported")
    if "enum" in schema and (not isinstance(schema["enum"], list) or not schema["enum"] or
                              any(not isinstance(item, str) for item in schema["enum"])):
        raise ValidationError(f"{location}: only nonempty string enums are supported")
    if "required" in schema and (not isinstance(schema["required"], list) or
                                  any(not isinstance(item, str) for item in schema["required"])):
        raise ValidationError(f"{location}: required must be a string array")
    if "pattern" in schema:
        try:
            re.compile(schema["pattern"])
        except re.error as exc:
            raise ValidationError(f"{location}: invalid regular expression") from exc
    if "$ref" in schema:
        ref = schema["$ref"]
        if not ref.startswith("#/$defs/") or ref.count("/") != 2 or ref.split("/")[-1] not in root.get("$defs", {}):
            raise ValidationError(f"{location}: unresolved or unsupported schema reference")
    for key in ("$defs", "properties"):
        if key in schema:
            if not isinstance(schema[key], dict):
                raise ValidationError(f"{location}.{key}: expected object")
            for name, child in schema[key].items():
                check_schema(child, root, f"{location}.{key}.{name}")
    if "items" in schema:
        check_schema(schema["items"], root, f"{location}.items")


def validate_schema(value, schema, root=None, location="$"):
    """Evaluate only the vocabulary used in our vendored, trusted schema.

    Unknown keywords fail closed instead of silently diverging when the schema
    changes. This is deliberately not a general purpose JSON Schema engine.
    """
    if root is None:
        check_schema(schema)
        root = schema
    if "$ref" in schema:
        ref = schema["$ref"]
        if not ref.startswith("#/$defs/") or ref.count("/") != 2:
            raise ValidationError("only local schema definition references are supported")
        validate_schema(value, root["$defs"][ref.split("/")[-1]], root, location)
    expected = schema.get("type")
    types = {"object": dict, "array": list, "string": str}
    if expected and (expected not in types or not isinstance(value, types[expected])):
        raise ValidationError(f"{location}: expected {expected}")
    if "const" in schema and (value != schema["const"] or type(value) is not type(schema["const"])):
        raise ValidationError(f"{location}: expected constant {schema['const']!r}")
    if "enum" in schema and value not in schema["enum"]:
        raise ValidationError(f"{location}: unsupported value {value!r}")
    if isinstance(value, str):
        if len(value) < schema.get("minLength", 0) or len(value) > schema.get("maxLength", 100000):
            raise ValidationError(f"{location}: invalid string length")
        if "pattern" in schema and re.search(schema["pattern"], value) is None:
            raise ValidationError(f"{location}: string does not match required pattern")
        if any(ord(char) < 32 or ord(char) == 127 or 0xD800 <= ord(char) <= 0xDFFF for char in value):
            raise ValidationError(f"{location}: control characters and lone surrogates are not permitted")
    if isinstance(value, dict):
        missing = set(schema.get("required", [])) - set(value)
        if missing:
            raise ValidationError(f"{location}: missing fields {sorted(missing)}")
        properties = schema.get("properties", {})
        if schema.get("additionalProperties") is False and set(value) - set(properties):
            raise ValidationError(f"{location}: unknown fields {sorted(set(value) - set(properties))}")
        for key in value.keys() & properties.keys():
            validate_schema(value[key], properties[key], root, f"{location}.{key}")
    if isinstance(value, list) and "items" in schema:
        for index, item in enumerate(value):
            validate_schema(item, schema["items"], root, f"{location}[{index}]")


def public_url(url):
    try:
        parsed = urlsplit(url)
        unsafe = (parsed.scheme != "https" or parsed.hostname not in ALLOWED_HOSTS or
                  parsed.netloc != parsed.hostname or parsed.username or parsed.password or
                  parsed.port or parsed.query or parsed.fragment or not parsed.path.startswith("/"))
    except ValueError as exc:
        raise ValidationError("malformed HTTPS URL") from exc
    decoded = unquote(parsed.path)
    if unsafe or any(ord(char) < 33 or ord(char) == 127 for char in url + decoded):
        raise ValidationError(f"unsafe or unsupported public URL: {url}")
    if any(char in decoded for char in "\\<>\"`{}[]()") or any(part in {".", "..", ""} for part in decoded.split("/")[1:]):
        raise ValidationError(f"unsafe public URL path: {url}")
    if decoded != parsed.path:
        raise ValidationError("percent-encoded URL paths are unsupported in v0.1")
    return parsed


def source_url(url, repository, revision=None):
    parsed = public_url(url)
    repo_path = urlsplit(repository).path
    if parsed.hostname == "github.com":
        if parsed.path[:len(repo_path)].lower() != repo_path.lower():
            raise ValidationError("source URL must belong to this declared public repository")
        rest = parsed.path[len(repo_path):]
        if not rest.startswith("/blob/"):
            raise ValidationError("source evidence must use a pinned GitHub blob URL")
        parts = rest.split("/")
        pinned, source_path = parts[2], parts[3:]
    elif parsed.hostname == "raw.githubusercontent.com":
        prefix = repo_path + "/"
        if not parsed.path.lower().startswith(prefix.lower()):
            raise ValidationError("raw source URL must belong to this declared public repository")
        parts = parsed.path[len(prefix):].split("/")
        pinned, source_path = parts[0], parts[1:]
    else:
        raise ValidationError("source evidence requires a GitHub blob or raw content URL")
    if not re.fullmatch(r"[a-f0-9]{40}|[a-f0-9]{64}", pinned) or not source_path:
        raise ValidationError("source URL must include a full commit and a file path")
    if revision is not None and pinned != revision:
        raise ValidationError("source URL commit and evidence revision differ")


def _unique(values, description):
    seen = set()
    for value in values:
        if value in seen:
            raise ValidationError(f"duplicate {description}: {value}")
        seen.add(value)


def validate_manifest(manifest, schema=None, allow_private=False):
    if schema is None:
        schema, _ = read_json(SCHEMA_PATH)
    validate_schema(manifest, schema)
    if manifest["repository"]["visibility"] != "public" and not allow_private:
        raise ValidationError("private manifests require explicit local validation and cannot enter public indexes")
    repository = manifest["repository"]["url"]
    repo_url = public_url(repository)
    repo_name = repo_url.path.split("/")[-1].lower().replace(".", "-").replace("_", "-")
    expected_id = f"ruv://ruvnet/constellation/service/{repo_name}/resources/manifest.ruv"
    if manifest["id"] != expected_id:
        raise ValidationError("manifest identity must match its repository name")
    public_url(manifest["nexus"])
    try:
        datetime.datetime.fromisoformat(manifest["provenance"]["observedAt"].replace("Z", "+00:00"))
    except ValueError as exc:
        raise ValidationError("provenance observedAt is not a valid UTC timestamp") from exc
    _unique((cap["id"] for cap in manifest["capabilities"]), "capability id")
    _unique((item["id"] for item in manifest["artifacts"]), "artifact id")
    _unique(((rel["type"], rel["target"]) for rel in manifest["relationships"]), "relationship")
    _unique(((item["role"], item["project"]) for item in manifest["integrations"]), "integration")
    for claim in manifest["capabilities"] + manifest["relationships"]:
        if claim["status"] != "planned" and not claim["evidence"]:
            raise ValidationError("documented or tested claims require pinned evidence")
        if claim["status"] == "tested" and not any(item["kind"] == "test" for item in claim["evidence"]):
            raise ValidationError("tested claims require test evidence")
        for evidence in claim["evidence"]:
            source_url(evidence["url"], repository, evidence["revision"])
    for artifact in manifest["artifacts"]:
        parsed = public_url(artifact["url"])
        if parsed.hostname in {"github.com", "raw.githubusercontent.com"}:
            source_url(artifact["url"], repository)
        elif artifact["kind"] != "package":
            raise ValidationError("non-source registry URLs require artifact kind package")
    return manifest


def load_manifests(paths, root, allow_private=False):
    root = Path(root).resolve()
    schema, _ = read_json(SCHEMA_PATH)
    records = []
    for path in paths:
        path = Path(path).absolute()
        try:
            relative = path.relative_to(root)
        except ValueError as exc:
            raise ValidationError(f"manifest is outside the explicit root: {path}") from exc
        manifest, raw = read_json(path)
        validate_manifest(manifest, schema, allow_private=allow_private)
        records.append({"manifest": manifest, "path": relative.as_posix(),
                        "sha256": hashlib.sha256(raw).hexdigest(), "adoption": {"status": "local"}})
    _unique((record["manifest"]["id"] for record in records), "manifest id")
    return sorted(records, key=lambda record: record["manifest"]["id"])


def apply_adoption(records, adoption):
    if not isinstance(adoption, dict):
        raise ValidationError("adoption data must be an object keyed by manifest identity")
    by_id = {record["manifest"]["id"]: record for record in records}
    for identity, assertion in adoption.items():
        if identity not in by_id or not isinstance(assertion, dict):
            raise ValidationError("adoption references an unknown manifest or malformed assertion")
        if set(assertion) - {"status", "pr"} or assertion.get("status") not in {"local", "pending_pr", "merged"}:
            raise ValidationError("adoption requires status local, pending_pr or merged")
        if assertion["status"] == "pending_pr" and "pr" not in assertion:
            raise ValidationError("pending_pr adoption requires a public PR URL")
        if "pr" in assertion:
            if assertion["status"] == "local":
                raise ValidationError("local adoption cannot claim a PR")
            public_url(assertion["pr"])
            repository = by_id[identity]["manifest"]["repository"]["url"]
            if not re.fullmatch(re.escape(repository) + r"/pull/[1-9][0-9]*", assertion["pr"], flags=re.I):
                raise ValidationError("adoption PR must belong to the manifest repository")
        by_id[identity]["adoption"] = assertion


def _markdown(text):
    return html.escape(text, quote=False).replace("\\", "\\\\").replace("|", "\\|").replace("[", "\\[").replace("]", "\\]").replace("*", "\\*").replace("_", "\\_").replace("`", "\\`")


def catalog(records):
    lines = ["# ruvnet constellation", "", "Public discovery metadata for people and AI systems. This catalog does not grant execution rights or certify correctness.", "", "Capability status and repository adoption are separate publisher assertions. A pending PR is not an adopted integration. Source visibility must be reviewed independently before publication.", "", "| Project | Purpose | Capabilities | Adoption |", "| :--- | :--- | :--- | :--- |"]
    for record in records:
        manifest = record["manifest"]
        capabilities = "; ".join(f"{_markdown(item['id'])} ({item['status']})" for item in manifest["capabilities"]) or "None declared"
        adoption = record["adoption"]
        status = adoption["status"]
        if "pr" in adoption:
            status = f"[{status}]({adoption['pr']})"
        lines.append(f"| [{_markdown(manifest['name'])}]({manifest['repository']['url']}) | {_markdown(manifest['summary'])} | {capabilities} | {status} |")
    for record in records:
        manifest = record["manifest"]
        lines.extend(["", f"## {_markdown(manifest['name'])}", "", f"Identity: `{manifest['id']}`", "", f"Source revision: `{manifest['provenance']['sourceCommit']}`. Observed: {manifest['provenance']['observedAt']}.", "", f"Manifest SHA256: `{record['sha256']}`."])
        for capability in manifest["capabilities"]:
            lines.extend(["", f"### {_markdown(capability['id'])}", "", f"{_markdown(capability['description'])} Status: {capability['status']}."])
            for evidence in capability["evidence"]:
                lines.extend(["", f"[{evidence['kind']} evidence]({evidence['url']})"])
        if manifest["integrations"]:
            lines.extend(["", "Declared integration roles (discovery metadata only):", ""])
            for item in manifest["integrations"]:
                lines.append(f"* {_markdown(item['role'])}: `{item['project']}`")
    return "\n".join(lines) + "\n"


def check_outputs(paths, inputs, root):
    root = Path(root).resolve()
    resolved = []
    input_paths = {Path(path).resolve() for path in inputs} | {SCHEMA_PATH.resolve(), Path(__file__).resolve()}
    for path in paths:
        path = Path(path).absolute()
        if path.resolve() != path or path.is_symlink():
            raise ValidationError(f"output cannot traverse symlinks: {path}")
        try:
            path.relative_to(root)
        except ValueError as exc:
            raise ValidationError("output must be inside the explicit root") from exc
        if path in input_paths or path in resolved or (path.exists() and not path.is_file()):
            raise ValidationError(f"output path collision: {path}")
        if any(parent.exists() and not parent.is_dir() for parent in path.parents):
            raise ValidationError(f"output ancestor is not a directory: {path}")
        if any(previous in path.parents or path in previous.parents for previous in resolved):
            raise ValidationError(f"output files cannot be ancestors of each other: {path}")
        resolved.append(path)
    return resolved


def write_outputs(outputs):
    """Prepare all files before replacing any; this is not a multi-file transaction."""
    staged = []
    try:
        for path, content in outputs:
            path.parent.mkdir(parents=True, exist_ok=True)
            with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", newline="\n", dir=path.parent, prefix=f".{path.name}.", delete=False) as handle:
                temp = Path(handle.name)
                staged.append((temp, path))
                handle.write(content)
        for temp, path in staged:
            os.replace(temp, path)
    finally:
        for temp, _ in staged:
            if temp.exists():
                temp.unlink()


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    for name in ("validate", "build"):
        command = commands.add_parser(name)
        command.add_argument("--root", default=".", help="explicit boundary for all input manifests and generated outputs")
        command.add_argument("manifests", nargs="+", help="explicit local files; directories, remote URIs and discovery are unsupported")
        if name == "validate":
            command.add_argument("--allow-private", action="store_true", help="validate explicitly supplied private manifests locally; never available to build")
        if name == "build":
            command.add_argument("--index", required=True)
            command.add_argument("--catalog", required=True)
            command.add_argument("--adoption", help="optional reviewed repository PR status assertions")
    args = parser.parse_args(argv)
    try:
        records = load_manifests(args.manifests, args.root, allow_private=getattr(args, "allow_private", False))
        if args.command == "build":
            inputs = list(args.manifests)
            if args.adoption:
                adoption, _ = read_json(args.adoption)
                apply_adoption(records, adoption)
                inputs.append(args.adoption)
            outputs = check_outputs([args.index, args.catalog], inputs, args.root)
            index = {"schemaVersion": "0.1", "kind": "ruv-nexus-index", "discoveryOnly": True, "entries": records}
            write_outputs([(outputs[0], json.dumps(index, sort_keys=True, indent=2, ensure_ascii=False) + "\n"),
                           (outputs[1], catalog(records))])
        print(f"Validated {len(records)} manifest(s). No network or execution performed.")
        return 0
    except (OSError, ValidationError, RecursionError) as exc:
        print(f"manifest.ruv: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
