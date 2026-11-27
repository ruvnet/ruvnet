"""Adversarial contract checks for the offline public constellation index."""

import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch


SCRIPT = Path(__file__).resolve().parents[1] / "scripts/ruv_manifest.py"
spec = importlib.util.spec_from_file_location("ruv_manifest", SCRIPT)
ruv = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ruv)
COMMIT = "a" * 40


def manifest(repo="ruflo"):
    identity = f"ruv://ruvnet/constellation/service/{repo.lower().replace('_', '-').replace('.', '-')}/resources/manifest.ruv"
    source = f"https://github.com/ruvnet/{repo}/blob/{COMMIT}/README.md"
    return {
        "schemaVersion": "0.1", "id": identity, "name": repo,
        "summary": "Public discovery metadata", "nexus": "https://github.com/ruvnet/ruvnet",
        "repository": {"url": f"https://github.com/ruvnet/{repo}", "defaultBranch": "main", "visibility": "public"},
        "capabilities": [{"id": "coordinate", "description": "Coordinate bounded work", "status": "documented",
                          "evidence": [{"url": source, "revision": COMMIT, "kind": "documentation"}]}],
        "artifacts": [{"id": "readme", "kind": "docs", "url": source}], "relationships": [],
        "integrations": [{"role": "discovery", "project": identity, "status": "declared"}],
        "safety": {"discoveryOnly": True, "executionRequiresAuthorization": True},
        "provenance": {"sourceCommit": COMMIT, "observedAt": "2026-10-10T03:00:00Z"},
    }


class ContractTests(unittest.TestCase):
    def assert_invalid(self, record):
        with self.assertRaises(ruv.ValidationError):
            ruv.validate_manifest(record)

    def test_valid_record_and_native_rvm_subject_normalization(self):
        for repo in ("ruflo", "RuVector", "core-memory", "foo.bar", "foo_bar"):
            self.assertEqual(ruv.validate_manifest(manifest(repo))["name"], repo)
        self.assert_invalid(manifest("a" * 64))

    def test_unknown_version_and_undeclared_fields_rejected(self):
        record = manifest()
        record["schemaVersion"] = "0.2"
        self.assert_invalid(record)
        record = manifest()
        record["commands"] = ["run untrusted code"]
        self.assert_invalid(record)

    def test_private_manifest_and_unauthorized_execution_rejected(self):
        record = manifest()
        record["repository"]["visibility"] = "private"
        self.assert_invalid(record)
        ruv.validate_manifest(record, allow_private=True)
        for value in (False, 1):
            record = manifest()
            record["safety"]["discoveryOnly"] = value
            self.assert_invalid(record)
        record = manifest()
        record["integrations"][0]["status"] = "active"
        self.assert_invalid(record)

    def test_mismatched_identity_commit_and_invalid_date_rejected(self):
        record = manifest()
        record["id"] = manifest("rvm")["id"]
        self.assert_invalid(record)
        for value in ("a" * 39, "A" * 40, "not-a-commit"):
            record = manifest()
            record["provenance"]["sourceCommit"] = value
            self.assert_invalid(record)
        record = manifest()
        record["provenance"]["observedAt"] = "2026-02-30T03:00:00Z"
        self.assert_invalid(record)

    def test_duplicate_capabilities_and_unsupported_status(self):
        record = manifest()
        record["capabilities"].append(copy.deepcopy(record["capabilities"][0]))
        self.assert_invalid(record)
        record = manifest()
        record["capabilities"][0]["status"] = "production"
        self.assert_invalid(record)

    def test_claim_evidence_boundary(self):
        record = manifest()
        record["capabilities"][0]["evidence"] = []
        self.assert_invalid(record)
        record["capabilities"][0]["status"] = "planned"
        ruv.validate_manifest(record)
        record = manifest()
        record["capabilities"][0]["status"] = "tested"
        self.assert_invalid(record)
        record["capabilities"][0]["evidence"][0]["kind"] = "test"
        ruv.validate_manifest(record)

    def test_pinned_evidence_must_match_revision_and_public_repository(self):
        for url in (f"https://github.com/ruvnet/private-memory/blob/{COMMIT}/README.md",
                    "https://github.com/ruvnet/ruflo/blob/main/README.md",
                    f"https://github.com/ruvnet/ruflo/blob/{'b' * 40}/README.md",
                    f"https://github.com/ruvnet/ruflo/blob/{COMMIT}",
                    f"https://github.com/ruvnet/ruflo-extra/blob/{COMMIT}/README.md"):
            record = manifest()
            record["capabilities"][0]["evidence"][0]["url"] = url
            self.assert_invalid(record)

    def test_url_attack_cases(self):
        for url in ("http://github.com/ruvnet/ruflo", "file:///etc/passwd", "javascript:alert(1)",
                    "https://localhost/a", "https://127.0.0.1/a", "https://github.com:443/a",
                    "https://token@github.com/a", "https://github.com/a?token=secret",
                    "https://github.com/a#secret", "https://github.com/a/../b",
                    "https://github.com/a/%2e%2e/b", "https://github.com/a/%0Ab",
                    "https://github.com/a\\b", "https://github.com/a//b",
                    "https://github.com/a)![injected](https://evil.example)"):
            with self.subTest(url=url):
                with self.assertRaises(ruv.ValidationError):
                    ruv.public_url(url)

    def test_duplicate_json_keys_and_non_json_numbers_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "manifest.ruv"
            for body in ('{"id":"a", "id":"b"}', '{"a":NaN}'):
                path.write_text(body)
                with self.assertRaises(ruv.ValidationError):
                    ruv.read_json(path)

    def test_surrogate_text_and_oversized_integers_fail_cleanly(self):
        record = manifest()
        record["summary"] = "\ud800"
        self.assert_invalid(record)
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "manifest.ruv"
            path.write_text('{"x":' + "1" * 5000 + '}')
            with self.assertRaises(ruv.ValidationError):
                ruv.read_json(path)

    def test_schema_unknown_keywords_fail_closed(self):
        with self.assertRaises(ruv.ValidationError):
            ruv.validate_schema({}, {"type": "object", "unknownKeyword": True})

    def test_schema_preflight_rejects_unused_and_unsupported_forms(self):
        for schema in (
            {"type": "object", "additionalProperties": {"type": "string"}},
            {"type": "object", "$defs": {"unused": {"minimum": 1}}},
            {"type": "object", "properties": {"absent": {"format": "email"}}},
            {"type": "object", "properties": {"absent": {"items": [{"type": "string"}]}}},
            {"type": "object", "properties": {"absent": {"type": ["string", "object"]}}},
            {"type": "object", "properties": {"absent": {"pattern": "["}}},
            {"type": "object", "$defs": {"unused": {"$ref": "#/$defs/missing"}}},
        ):
            with self.subTest(schema=schema):
                with self.assertRaises(ruv.ValidationError):
                    ruv.validate_schema({"x": 1}, schema)


class IndexTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.one = self.root / "ruflo.ruv"
        self.two = self.root / "rvm.ruv"
        self.one.write_text(json.dumps(manifest("ruflo")))
        self.two.write_text(json.dumps(manifest("rvm")))
        self.index = self.root / "index.json"
        self.catalog = self.root / "catalog.md"

    def tearDown(self):
        self.temp.cleanup()

    def build(self, paths=None, **kwargs):
        args = ["build", "--root", str(self.root), "--index", str(kwargs.get("index", self.index)),
                "--catalog", str(kwargs.get("catalog", self.catalog))]
        if "adoption" in kwargs:
            args += ["--adoption", str(kwargs["adoption"])]
        return ruv.main(args + [str(path) for path in (paths or [self.one, self.two])])

    def test_deterministic_offline_index_and_exact_bytes_hash(self):
        with patch("socket.socket", side_effect=AssertionError("network prohibited")), patch("subprocess.Popen", side_effect=AssertionError("execution prohibited")):
            self.assertEqual(self.build(), 0)
            first = self.index.read_bytes(), self.catalog.read_bytes()
            self.assertEqual(self.build(paths=[self.two, self.one]), 0)
            self.assertEqual(first, (self.index.read_bytes(), self.catalog.read_bytes()))
        index = json.loads(self.index.read_text())
        self.assertEqual(index["entries"][0]["sha256"], hashlib.sha256(self.one.read_bytes()).hexdigest())
        self.assertEqual(index["entries"][0]["path"], "ruflo.ruv")
        self.assertEqual(index["entries"][0]["adoption"]["status"], "local")

    def test_duplicate_ids_and_normalized_collisions_fail(self):
        self.two.write_text(self.one.read_text())
        self.assertEqual(self.build(), 1)
        self.assertFalse(self.index.exists())
        self.one.write_text(json.dumps(manifest("foo_bar")))
        self.two.write_text(json.dumps(manifest("foo.bar")))
        self.assertEqual(self.build(), 1)

    def test_output_path_collisions_do_not_modify_inputs(self):
        original = self.one.read_bytes()
        self.assertEqual(self.build(index=self.one), 1)
        self.assertEqual(self.one.read_bytes(), original)
        self.assertEqual(self.build(catalog=self.index), 1)
        self.assertFalse(self.index.exists())

    def test_output_symlinks_rejected(self):
        original = self.one.read_bytes()
        self.index.symlink_to(self.one)
        self.assertEqual(self.build(), 1)
        self.assertEqual(self.one.read_bytes(), original)

    def test_output_ancestor_files_do_not_partially_replace_index(self):
        self.index.write_text("previous index")
        blocker = self.root / "file"
        blocker.write_text("not a directory")
        self.assertEqual(self.build(catalog=blocker / "catalog.md"), 1)
        self.assertEqual(self.index.read_text(), "previous index")
        self.assertEqual(self.build(catalog=self.index / "catalog.md"), 1)

    def test_all_outputs_stage_before_any_replacement(self):
        self.index.write_text("previous index")
        self.catalog.write_text("previous catalog")
        original = tempfile.NamedTemporaryFile
        calls = 0

        def fail_second(**kwargs):
            nonlocal calls
            calls += 1
            if calls == 2:
                raise OSError("simulated second output failure")
            return original(**kwargs)

        with patch.object(ruv.tempfile, "NamedTemporaryFile", side_effect=fail_second):
            self.assertEqual(self.build(), 1)
        self.assertEqual(self.index.read_text(), "previous index")
        self.assertEqual(self.catalog.read_text(), "previous catalog")
        self.assertEqual(list(self.root.glob(".index.json.*")), [])

    def test_parent_symlinks_and_input_symlinks_rejected(self):
        link = self.root / "linked"
        target = self.root / "real"
        target.mkdir()
        link.symlink_to(target, target_is_directory=True)
        self.assertEqual(self.build(index=link / "index.json"), 1)
        symlink = self.root / "input.ruv"
        symlink.symlink_to(self.one)
        self.assertEqual(self.build(paths=[symlink]), 1)

    def test_pending_pr_separate_from_capability_status(self):
        adoption = self.root / "adoption.json"
        adoption.write_text(json.dumps({manifest()["id"]: {"status": "pending_pr", "pr": "https://github.com/ruvnet/ruflo/pull/42"}}))
        self.assertEqual(self.build(adoption=adoption), 0)
        entry = json.loads(self.index.read_text())["entries"][0]
        self.assertEqual(entry["adoption"]["status"], "pending_pr")
        self.assertEqual(entry["manifest"]["capabilities"][0]["status"], "documented")
        adoption.write_text(json.dumps({manifest()["id"]: {"status": "pending_pr", "pr": "https://github.com/ruvnet/other/pull/42"}}))
        self.assertEqual(self.build(adoption=adoption), 1)

    def test_private_local_validation_never_enters_public_index(self):
        record = manifest("core-memory")
        record["repository"]["visibility"] = "private"
        self.one.write_text(json.dumps(record))
        self.assertEqual(ruv.main(["validate", "--root", str(self.root), "--allow-private", str(self.one)]), 0)
        self.assertEqual(ruv.main(["validate", "--root", str(self.root), str(self.one)]), 1)
        self.assertEqual(self.build(), 1)
        self.assertFalse(self.index.exists())
        with self.assertRaises(SystemExit):
            ruv.main(["build", "--allow-private", "--index", str(self.index), "--catalog", str(self.catalog), str(self.one)])

    def test_markdown_escapes_untrusted_text(self):
        record = manifest()
        record["summary"] = "<script>alert(1)</script> | [x](https://evil.example)"
        self.one.write_text(json.dumps(record))
        self.assertEqual(self.build(), 0)
        rendered = self.catalog.read_text()
        self.assertNotIn("<script>", rendered)
        self.assertIn("&lt;script&gt;", rendered)
        self.assertIn("\\|", rendered)
        self.assertIn("\\[x\\]", rendered)


if __name__ == "__main__":
    unittest.main()
