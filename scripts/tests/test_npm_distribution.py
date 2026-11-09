import base64
import importlib.util
import json
import pathlib
import unittest
import urllib.request
from unittest.mock import patch


def load(name):
    path = pathlib.Path(__file__).resolve().parents[1] / name
    spec = importlib.util.spec_from_file_location(path.stem, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


collector = load("collect-npm-distribution.py")
resolver = load("resolve-npm-distribution-source.py")
assembler = load("assemble-npm-distribution.py")


class CollectorTests(unittest.TestCase):
    def test_public_candidate_requires_exact_github_owner_and_safe_directory(self):
        self.assertEqual(collector.github_source({
            "url": "git+ssh://git@github.com/ruvnet/RuVector.git", "directory": "npm/packages/kge"}),
            {"repo": "ruvnet/RuVector", "directory": "npm/packages/kge"})
        for url, directory in [("https://github.com.evil/ruvnet/repo", None),
                               ("https://github.com/other/repo", None),
                               ("https://github.com/ruvnet/repo?token=x", None),
                               ("https://github.com/ruvnet/repo", "../repo"),
                               ("https://github.com/ruvnet/repo", "x/%2e%2e")]:
            with self.subTest(url=url, directory=directory):
                self.assertIsNone(collector.github_source({"url": url, "directory": directory}))

    def test_cross_origin_redirect_rejected_before_request(self):
        req = urllib.request.Request("https://registry.npmjs.org/example/latest")
        with self.assertRaises(ValueError):
            collector.RegistryRedirect().redirect_request(req, None, 302, "", {}, "https://evil.example")

    def test_redacts_unbounded_metadata(self):
        self.assertIsNone(collector.safe_homepage("https://user:secret@example.org/path"))
        self.assertEqual(collector.safe_homepage("https://ruv.io/?key=secret"), "https://ruv.io/")
        edges = collector.dependency_edges({"dependencies": {"a": "^1.0", "b": "git+ssh://user:key@host/path"}})
        self.assertEqual(edges["dependencies"], {"a": "^1.0", "b": None})

    def test_cohort_all_zero_day_unknown_and_incomplete_range_null(self):
        observed = {"p": {"dates": {"2026-10-01": 0}}, "q": {"dates": {"2026-10-01": 0}}}
        all_zero, unknown = collector.summarize(observed)
        self.assertEqual(all_zero, ["2026-10-01"])
        self.assertIn("2026-10-01", unknown)
        self.assertIsNone(observed["p"]["windows"]["october"]["observed_download_events"])
        partial = {"p": {"dates": {"2026-10-01": 1}}, "q": {"error": "HTTPError"}}
        all_zero, unknown = collector.summarize(partial)
        self.assertEqual(all_zero, [])
        self.assertNotIn("2026-10-01", unknown)
        self.assertIn("2026-10-02", unknown)
        self.assertIsNone(partial["q"]["windows"]["october"])
        self.assertEqual(partial["p"]["windows"]["october"]["observed_days"], 1)

    def test_paginated_inventory_rejects_duplicate(self):
        def page(names):
            return ({"total": 3, "objects": [{"package": {"name": n}} for n in names]}, {})
        with patch.object(collector, "fetch", side_effect=[page(["a", "b"]), page(["b"])]):
            with self.assertRaisesRegex(ValueError, "overlapping"):
                collector.inventory()

    def test_paginated_inventory_rejects_changing_total(self):
        with patch.object(collector, "fetch", side_effect=[
            ({"total": 3, "objects": [{"package": {"name": "a"}}]}, {}),
            ({"total": 2, "objects": [{"package": {"name": "b"}}]}, {}),
        ]):
            with self.assertRaisesRegex(ValueError, "total changed"):
                collector.inventory()


class ResolverTests(unittest.TestCase):
    def row(self, directory=None):
        return {"name": "@ruvector/example", "live_maintainer_listing": True,
                "registry": {"version": "1.0.0", "maintainer_in_latest_manifest": True,
                             "source_candidate": {"repo": "ruvnet/RuVector", "directory": directory}}}

    def test_private_or_unavailable_repo_not_emitted(self):
        with patch.object(resolver, "api", return_value={"private": True, "visibility": "private"}):
            self.assertIsNone(resolver.repository("ruvnet/unlisted"))
        result = resolver.check_source(self.row(), None)
        self.assertIsNone(result["source"])
        self.assertNotIn("source_candidate", result["registry"])

    def test_exact_unique_source_required_and_readme_recorded(self):
        digest = "a" * 40
        raw = json.dumps({"name": "@ruvector/example", "version": "1.0.0"}).encode()
        repo = {"name": "ruvnet/RuVector", "archived": False, "push_permission": True,
                "paths": {"npm/example/package.json": digest, "npm/example/README.md": digest}}
        with patch.object(resolver, "api", return_value={
                "encoding": "base64", "sha": digest, "content": base64.b64encode(raw).decode(), "size": len(raw)}):
            result = resolver.check_source(self.row(), repo)
            self.assertEqual(result["status"], "source_verified")
            self.assertEqual(result["source"]["manifest_path"], "npm/example/package.json")
            self.assertEqual(result["source"]["source_readme"], "npm/example/README.md")
            repo["paths"]["alt/example/package.json"] = digest
            self.assertEqual(resolver.check_source(self.row(), repo)["status"], "ambiguous_exact_manifest_matches")

    def test_rejects_traversal_even_with_owned_repo(self):
        result = resolver.check_source(self.row("x/../y"), {"name": "ruvnet/RuVector"})
        self.assertEqual(result["status"], "unsafe_source_directory")


class AssemblerTests(unittest.TestCase):
    def test_frozen_queue_and_redaction(self):
        names = sorted(assembler.PILOTS | assembler.ENTRY | assembler.MIGRATION)
        names += [f"@ruvector/platform-{n}-linux-x64-gnu" for n in range(80)]
        names += [f"@ruvector/plugin-case-{n}" for n in range(54)]
        names += [f"@ruvector/feature-{n}" for n in range(127)]
        names += [f"misc-{n}" for n in range(118)]
        common = {"frozen_count": 405, "live_count": 405, "observed_at": "fixture",
                  "live_inventory_evidence": [], "coverage": {"downloads": 405},
                  "all_zero_cohort_days": [], "dates_without_confirmed_nonzero_count": []}
        resolved = [{ "name": n, "frozen_cohort": True, "live_maintainer_listing": True,
                      "status": "source_verified",
                      "registry": {"homepage": "https://example.invalid/private",
                                   "homepage_exact_target": False, "keywords": ["private"]},
                      "source": {"name": "ruvnet/fixture", "push_permission": True,
                                 "match_kind": "exact_name_at_unique_package_path"}} for n in names]
        downloaded = [{"name": n, "frozen_cohort": True, "live_maintainer_listing": True,
                       "downloads": None} for n in names]
        result = assembler.assemble({**common, "packages": resolved}, {**common, "packages": downloaded})
        self.assertEqual(len(result["packages"]), 405)
        self.assertEqual(result["frozen_lanes"]["platform_artifact"], 80)
        self.assertEqual(result["candidate_batches"], [])
        self.assertNotIn("private", json.dumps(result))
        self.assertNotIn("push_permission", json.dumps(result))
        downloaded.pop()
        with self.assertRaisesRegex(ValueError, "sets drifted"):
            assembler.assemble({**common, "packages": resolved}, {**common, "packages": downloaded})


if __name__ == "__main__":
    unittest.main()
