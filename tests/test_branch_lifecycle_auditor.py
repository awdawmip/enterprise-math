import json
import tempfile
import unittest
from pathlib import Path

from tools.audit_branch_lifecycle import (
    classify_branch,
    load_overrides,
    mechanical_candidate,
    name_layer,
)


class BranchLifecycleAuditorTests(unittest.TestCase):
    def test_name_layers(self):
        self.assertEqual(name_layer("main"), "L0_CANONICAL")
        self.assertEqual(name_layer("core/a2-future-quotient-v2"), "L1_CORE_OWNER")
        self.assertEqual(name_layer("program/p018-precision-v2"), "L2_PROGRAM_OWNER")
        self.assertEqual(name_layer("bridge/a3-a4-v2"), "L3_BRIDGE")
        self.assertEqual(name_layer("integration/replay"), "L4_INTEGRATION")
        self.assertEqual(name_layer("checkpoint/old"), "L5_PROVENANCE")

    def test_ahead_zero_is_mechanically_absorbed(self):
        self.assertEqual(mechanical_candidate("research/old", 0, 200), "ABSORBED")

    def test_large_divergence_is_replay_required_when_ahead(self):
        self.assertEqual(
            mechanical_candidate("research/large", 5, 50),
            "REPLAY_REQUIRED",
        )
        self.assertEqual(
            mechanical_candidate("agent/large", 101, 2),
            "REPLAY_REQUIRED",
        )

    def test_current_owner_and_bridge_names_have_expected_candidate(self):
        self.assertEqual(
            mechanical_candidate("core/a3-relation-state-v2", 3, 2),
            "ACTIVE_OWNER",
        )
        self.assertEqual(
            mechanical_candidate("program/p018-precision-v2", 4, 1),
            "ACTIVE_OWNER",
        )
        self.assertEqual(
            mechanical_candidate("bridge/a3-a4-v2", 2, 3),
            "ACTIVE_BRIDGE",
        )

    def test_unclassified_short_branch_requires_review(self):
        self.assertEqual(
            mechanical_candidate("research/small-special-case", 2, 3),
            "NEEDS_REVIEW",
        )

    def test_semantic_override_can_absorb_ahead_branch(self):
        overrides = {
            "research/replayed": {
                "state": "ABSORBED",
                "reason": "same theorem and exact implementation blobs are on main",
            }
        }
        audit = classify_branch("research/replayed", 2, 64, overrides)
        self.assertEqual(audit.mechanical_candidate, "REPLAY_REQUIRED")
        self.assertEqual(audit.semantic_state, "ABSORBED")

    def test_override_schema_validation(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "overrides.json"
            path.write_text(
                json.dumps(
                    {
                        "schema": "ENTERPRISE_MATH_BRANCH_LIFECYCLE_OVERRIDES_V1",
                        "branches": {
                            "research/example": {
                                "state": "PROVENANCE",
                                "reason": "historical audit anchor",
                            }
                        },
                    }
                ),
                encoding="utf-8",
            )
            loaded = load_overrides(path)
            self.assertEqual(loaded["research/example"]["state"], "PROVENANCE")

    def test_invalid_override_state_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "overrides.json"
            path.write_text(
                json.dumps(
                    {
                        "schema": "ENTERPRISE_MATH_BRANCH_LIFECYCLE_OVERRIDES_V1",
                        "branches": {
                            "research/example": {
                                "state": "MAYBE",
                                "reason": "bad state",
                            }
                        },
                    }
                ),
                encoding="utf-8",
            )
            with self.assertRaises(ValueError):
                load_overrides(path)


if __name__ == "__main__":
    unittest.main()
