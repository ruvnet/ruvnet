import copy
import importlib.util
from pathlib import Path
import unittest


PATH = Path(__file__).resolve().parents[1] / "package-weave.py"
SPEC = importlib.util.spec_from_file_location("weave", PATH)
weave = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(weave)


class WeaveTests(unittest.TestCase):
    def setUp(self):
        def row(name, **edges):
            return {"name": name, "registry": {"dependency_edges": edges}}
        self.baseline = {"packages": [
            row("cli", dependencies={"core": "^1", "opt": "^1"},
                optionalDependencies={"opt": "^1"}),
            row("core", peerDependencies={"opt": "^1"}),
            row("opt", dependencies={"cli": "^1"}),
        ]}
        self.inventory = {"packages": ["cli", "core", "opt"]}
        self.candidate = {
            "id": "memory-v1", "from": "cli", "to": "opt", "mode": "recipe",
            "value": "Persist memory.", "pins": {"cli": "1.0.0", "opt": "1.1.0"},
            "checks": ["persistence", "filter"],
        }
        self.policy = {"entrypoints": ["cli"], "candidates": [self.candidate]}
        self.receipt = {
            "candidate": "memory-v1", "pins": self.candidate["pins"],
            "platform": "linux/x64", "lock_sha256": "f" * 64, "recipe_sha256": "a" * 64,
            "checks": {"persistence": True, "filter": True},
        }

    def report(self, *receipts):
        return weave.plan(self.baseline, self.inventory, self.policy, receipts)

    def test_reach_separates_required_from_optional_overrides(self):
        report = self.report()
        self.assertEqual(report["entrypoints"]["cli"], {
            "required_reachable": 1, "possible_reachable_including_optional_and_peers": 2,
        })
        self.assertEqual(report["next_test"], "memory-v1")
        self.assertFalse(report["promotion_authorized"])

    def test_receipt_advances_candidate_without_authorizing_promotion(self):
        later = {**self.candidate, "id": "routing-v1"}
        self.policy["candidates"].append(later)
        report = self.report(self.receipt)
        self.assertEqual(report["candidates"][0]["state"], "observed_pass_review_ready")
        self.assertEqual(report["next_test"], "routing-v1")
        self.assertFalse(report["promotion_authorized"])
        self.assertEqual(report, self.report(self.receipt))

    def test_incomplete_or_failed_checks_are_not_review_ready(self):
        for val, state in [(None, "needs_more_evidence"), (False, "needs_revision")]:
            self.receipt["checks"]["filter"] = val
            self.assertEqual(self.report(self.receipt)["candidates"][0]["state"], state)

    def test_stale_or_ambiguous_receipt_fails_closed(self):
        stale = copy.deepcopy(self.receipt)
        stale["pins"]["opt"] = "1.1.1"
        with self.assertRaisesRegex(ValueError, "does not match"):
            self.report(stale)
        with self.assertRaisesRegex(ValueError, "duplicate receipt"):
            self.report(self.receipt, self.receipt)

    def test_required_proposal_checks_reverse_path_and_coverage(self):
        self.candidate["mode"] = "required"
        self.assertEqual(self.report()["candidates"][0]["state"], "blocked_potential_cycle")
        self.inventory["packages"].append("new-package")
        report = self.report()
        self.assertEqual(report["coverage"]["new_since_baseline"], ["new-package"])
        self.assertEqual(report["candidates"][0]["state"], "blocked_graph_coverage")


    def test_overlay_adds_verified_nodes_and_keeps_newer_observations(self):
        from urllib.parse import quote
        def observed(name, date):
            return {"name": name, "registry": {
                "maintainer_in_latest_manifest": True,
                "dependency_edges": {},
                "registry_evidence": {
                    "url": f"https://registry.npmjs.org/{quote(name, safe='')}/latest",
                    "sha256": "0" * 64, "observed_at": date,
                },
            }}
        self.baseline["packages"][0]["registry"]["registry_evidence"] = {
            "observed_at": "2026-11-11T00:00:00Z",
        }
        self.inventory["packages"].append("new-package")
        overlay = {"schema_version": 1, "packages": [
            observed("cli", "2026-11-10T00:00:00Z"),
            observed("new-package", "2026-11-10T00:00:00Z"),
        ]}
        report = weave.plan(self.baseline, self.inventory, self.policy, [], overlay)
        self.assertEqual(report["coverage"]["inventory_without_graph"], [])
        self.assertEqual(report["coverage"]["new_since_baseline"], ["new-package"])
        self.assertEqual(report["entrypoints"]["cli"]["required_reachable"], 1)
        overlay["packages"][1]["registry"]["registry_evidence"]["url"] = "https://example.org"
        with self.assertRaisesRegex(ValueError, "invalid manifest overlay"):
            weave.plan(self.baseline, self.inventory, self.policy, [], overlay)
