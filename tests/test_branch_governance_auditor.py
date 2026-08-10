import json
import tempfile
import unittest
from pathlib import Path

from tools.audit_branch_lifecycle import (
    LEGACY_RETIREMENT_HEADS,
    classify_branch,
    load_overrides,
    mechanical_candidate,
    name_layer,
    retirement_evidence,
    scope_status,
)


REPO_ROOT = Path(__file__).resolve().parents[1]
SOURCE_HEAD = "260c563c7ba1b9f0dafc56a345e8ed5cd3ed0001"


class BranchGovernanceAuditorTests(unittest.TestCase):
    def test_owner_can_be_behind_without_becoming_replay_required(self):
        self.assertEqual(
            mechanical_candidate("core/a3-relation-state-v2", ahead=4, behind=37),
            "ACTIVE_OWNER",
        )

    def test_large_historical_divergence_is_replay_candidate(self):
        self.assertEqual(
            mechanical_candidate("research/old-tree", ahead=7, behind=200),
            "REPLAY_REQUIRED",
        )

    def test_maintenance_branch_is_recognized_as_maintenance(self):
        self.assertEqual(name_layer("maintenance/result-conservation-core-v1"), "MAINTENANCE")

    def test_semantic_override_can_mark_ahead_branch_absorbed(self):
        overrides = {
            "research/example": {
                "state": "ABSORBED",
                "reason": "semantic replay already entered main",
                "retirement_basis": "LEGACY_PRE_RESULT_CONSERVATION",
                "retired_head": "a" * 40,
                "allowed_paths": [],
                "allowed_prefixes": [],
            }
        }
        result = classify_branch(
            "research/example",
            ahead=3,
            behind=10,
            changed_files=("old.py",),
            overrides=overrides,
        )
        self.assertEqual(result.semantic_state, "ABSORBED")
        self.assertEqual(result.scope_state, "NOT_APPLICABLE")

    def test_exact_owner_assets_are_scope_pure(self):
        override = {
            "state": "ACTIVE_OWNER",
            "reason": "test",
            "allowed_paths": ["owned.py", "tests/test_owned.py"],
            "allowed_prefixes": [],
        }
        scope, unexpected = scope_status(
            "core/example",
            "ACTIVE_OWNER",
            ("owned.py", "tests/test_owned.py"),
            override,
        )
        self.assertEqual(scope, "PURE")
        self.assertEqual(unexpected, ())

    def test_foreign_asset_is_scope_drift_even_when_branch_is_current(self):
        override = {
            "state": "ACTIVE_OWNER",
            "reason": "test",
            "allowed_paths": ["owned.py"],
            "allowed_prefixes": [],
        }
        result = classify_branch(
            "core/example",
            ahead=2,
            behind=0,
            changed_files=("owned.py", "docs/LEGENDRE_FOREIGN.en.md"),
            overrides={"core/example": override},
        )
        self.assertEqual(result.semantic_state, "ACTIVE_OWNER")
        self.assertEqual(result.scope_state, "SCOPE_DRIFT")
        self.assertEqual(result.unexpected_paths, ("docs/LEGENDRE_FOREIGN.en.md",))

    def test_allowed_prefix_supports_owner_families(self):
        override = {
            "state": "ACTIVE_OWNER",
            "reason": "test",
            "allowed_paths": [],
            "allowed_prefixes": ["src/enterprise_math/p017_"],
        }
        scope, unexpected = scope_status(
            "program/p017-legendre",
            "ACTIVE_OWNER",
            (
                "src/enterprise_math/p017_mirror.py",
                "src/enterprise_math/p017_window.py",
            ),
            override,
        )
        self.assertEqual(scope, "PURE")
        self.assertEqual(unexpected, ())

    def test_unconfigured_scope_is_not_silently_pure(self):
        scope, unexpected = scope_status(
            "core/example",
            "ACTIVE_OWNER",
            ("owned.py",),
            None,
        )
        self.assertEqual(scope, "NOT_CONFIGURED")
        self.assertEqual(unexpected, ())

    def test_repository_override_contract_and_certificate_links_are_valid(self):
        overrides = load_overrides(REPO_ROOT / "branch_governance_overrides.json")
        retired = overrides["agent/e001-material-unification"]
        self.assertEqual(retired["retirement_basis"], "RESULT_CONSERVATION")
        self.assertEqual(
            retired["result_conservation_certificate"],
            "result_conservation_e001_material.json",
        )
        for branch, expected_head in LEGACY_RETIREMENT_HEADS.items():
            self.assertEqual(overrides[branch]["retired_head"], expected_head)

    def test_legacy_allowlist_is_frozen_in_code(self):
        data = json.loads(
            (REPO_ROOT / "branch_governance_overrides.json").read_text(encoding="utf-8")
        )
        data["retirement_contract"]["legacy_branches"].append("agent/new-legacy-escape")
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "branch_governance_overrides.json"
            path.write_text(json.dumps(data), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "legacy_branches is frozen"):
                load_overrides(path)

    def test_ahead_positive_mechanical_retirement_is_rejected(self):
        override = {
            "state": "PROVENANCE",
            "reason": "incorrect mechanical claim",
            "retirement_basis": "MECHANICAL_ANCESTRY",
            "allowed_paths": [],
            "allowed_prefixes": [],
        }
        state, reason, certificate = retirement_evidence(
            "agent/example",
            ahead=1,
            branch_head="a" * 40,
            semantic_state="PROVENANCE",
            override=override,
            root=REPO_ROOT,
        )
        self.assertEqual(state, "INVALID_RETIREMENT_EVIDENCE")
        self.assertIn("ahead by 1", reason)
        self.assertIsNone(certificate)

    def test_legacy_retirement_requires_exact_frozen_branch_head(self):
        branch = "engineering/e001-material-pair-impulse"
        override = {
            "state": "PROVENANCE",
            "reason": "legacy source",
            "retirement_basis": "LEGACY_PRE_RESULT_CONSERVATION",
            "retired_head": LEGACY_RETIREMENT_HEADS[branch],
            "allowed_paths": [],
            "allowed_prefixes": [],
        }
        state, _, _ = retirement_evidence(
            branch,
            ahead=8,
            branch_head=LEGACY_RETIREMENT_HEADS[branch],
            semantic_state="PROVENANCE",
            override=override,
            root=REPO_ROOT,
        )
        self.assertEqual(state, "LEGACY_GRANDFATHERED")

        state, reason, _ = retirement_evidence(
            branch,
            ahead=9,
            branch_head="0" * 40,
            semantic_state="PROVENANCE",
            override=override,
            root=REPO_ROOT,
        )
        self.assertEqual(state, "INVALID_RETIREMENT_EVIDENCE")
        self.assertIn("!= branch head", reason)

    def test_e001_semantic_retirement_certificate_matches_exact_source_head(self):
        overrides = load_overrides(REPO_ROOT / "branch_governance_overrides.json")
        override = overrides["agent/e001-material-unification"]
        state, reason, certificate = retirement_evidence(
            "agent/e001-material-unification",
            ahead=29,
            branch_head=SOURCE_HEAD,
            semantic_state="PROVENANCE",
            override=override,
            root=REPO_ROOT,
        )
        self.assertEqual(state, "RESULT_CONSERVATION_CERTIFIED")
        self.assertIn("exact retired source head", reason)
        self.assertEqual(certificate, "result_conservation_e001_material.json")

    def test_result_conservation_retirement_rejects_head_mismatch(self):
        overrides = load_overrides(REPO_ROOT / "branch_governance_overrides.json")
        override = overrides["agent/e001-material-unification"]
        state, reason, _ = retirement_evidence(
            "agent/e001-material-unification",
            ahead=29,
            branch_head="0" * 40,
            semantic_state="PROVENANCE",
            override=override,
            root=REPO_ROOT,
        )
        self.assertEqual(state, "INVALID_RETIREMENT_EVIDENCE")
        self.assertIn("!= branch head", reason)

    def test_unconfigured_ahead_positive_retirement_is_not_silently_accepted(self):
        state, reason, certificate = retirement_evidence(
            "agent/old-source",
            ahead=3,
            branch_head="b" * 40,
            semantic_state="PROVENANCE",
            override=None,
            root=REPO_ROOT,
        )
        self.assertEqual(state, "UNDECLARED_SEMANTIC_RETIREMENT")
        self.assertIn("no explicit retirement declaration", reason)
        self.assertIsNone(certificate)


if __name__ == "__main__":
    unittest.main()
