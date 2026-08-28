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
                "/composes/canonical_dispatch",
                "/lease_model/session_liveness/semantic_scope",
                "/lease_model/session_liveness/renewed_by",
            },
            set(proof["changed_pointers"]),
        )
        self.assertEqual(
            "tools/research_dispatch.py",
            proof["protected_after"]["/dispatch/tool"],
        )

    def test_runtime_bundle_targets_recovery_aware_route_and_owner_scope_liveness(self):
        proof = equivalence.prove(ROOT)
        self.assertEqual(
            "research_control_dispatch.py",
            proof["after_values"]["/composes/canonical_dispatch"],
        )
        self.assertEqual(
            "EXACT_OWNER_SCOPE_CURRENT_WINNING_CLAIM",
            proof["after_values"]["/lease_model/session_liveness/semantic_scope"],
        )
        self.assertEqual(
            [
                "TASK_RESEARCH_RESPONSE_BOUND_TO_EXACT_CLAIM_ID",
                "DURABLE_EXECUTION_PROGRESS_BOUND_TO_EXACT_CLAIM_ID",
            ],
            proof["after_values"]["/lease_model/session_liveness/renewed_by"],
        )


if __name__ == "__main__":
    unittest.main()
