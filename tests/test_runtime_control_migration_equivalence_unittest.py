import json
import unittest
from pathlib import Path

from control_plane import check_runtime_control_migration_equivalence as equivalence


ROOT = Path(__file__).resolve().parents[1]


class RuntimeControlMigrationEquivalenceTests(unittest.TestCase):
    def test_runtime_bundle_changes_only_registered_control_pointers(self):
        proof = equivalence.prove(ROOT)
        self.assertTrue(proof["non_target_structure_equal"])
        self.assertEqual(
            proof["non_target_structure_sha256"],
            proof["proposed_non_target_structure_sha256"],
        )
        self.assertEqual(
            {
                "/canonical_live_dispatch",
                "/owner_lease_is_session_liveness",
                "/stale_valid_owner_action",
            },
            set(proof["changed_pointers"]),
        )
        self.assertEqual(
            "tools/research_dispatch.py",
            proof["protected_after"]["/fresh_task_selector"],
        )
        self.assertEqual(proof["protected_before"], proof["protected_after"])
        self.assertEqual(proof["before_values"], proof["after_values"])

    def test_runtime_bundle_targets_recovery_aware_route_and_owner_scope_liveness(self):
        proof = equivalence.prove(ROOT)
        self.assertEqual(
            "research_control_dispatch.py",
            proof["after_values"]["/canonical_live_dispatch"],
        )
        self.assertIs(proof["after_values"]["/owner_lease_is_session_liveness"], False)
        self.assertEqual(
            "ADOPT_EXISTING_CLAIM",
            proof["after_values"]["/stale_valid_owner_action"],
        )
        # Exact activity evidence moved to its owning dispatch contract in V2.
        routing = json.loads((ROOT / "research_dispatch_contract.json").read_text(encoding="utf-8"))[
            "session_liveness_routing"
        ]
        self.assertEqual(
            ["TASK_RESEARCH_RESPONSE", "DURABLE_EXECUTION_PROGRESS"],
            routing["allowed_activity_evidence_kinds"],
        )
        self.assertIn("task_id", routing["activity_evidence_required_fields"])
        self.assertIn("claim_id", routing["activity_evidence_required_fields"])
        self.assertIn("exact claim_id", routing["owner_scope_key"])
        self.assertIs(routing["conversation_activity_is_owner_scope_liveness"], False)


if __name__ == "__main__":
    unittest.main()
