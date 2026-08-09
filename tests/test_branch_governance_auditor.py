import unittest

from tools.audit_branch_lifecycle import (
    classify_branch,
    mechanical_candidate,
    scope_status,
)


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

    def test_semantic_override_can_mark_ahead_branch_absorbed(self):
        overrides = {
            "research/example": {
                "state": "ABSORBED",
                "reason": "semantic replay already entered main",
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


if __name__ == "__main__":
    unittest.main()
