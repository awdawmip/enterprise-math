import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class CurrentControlSemanticSafetyTests(unittest.TestCase):
    def test_large_mixed_json_requires_exact_span_registered_migration(self):
        authority = json.loads(
            (ROOT / "control_plane" / "current_control_authority.json").read_text(
                encoding="utf-8"
            )
        )
        migration = authority["semantic_migration"]
        self.assertEqual(
            "control_plane/apply_registered_json_migration.py",
            migration["safe_exact_span_applier"],
        )
        self.assertEqual(
            "FORBIDDEN_BY_DEFAULT",
            migration["large_or_mixed_json_whole_file_reserialization_for_pointer_cleanup"],
        )
        self.assertTrue(migration["exact_expected_git_blob_required_before_pending_patch"])
        self.assertTrue(migration["dry_run_required_before_write"])
        self.assertTrue(migration["non_target_json_structure_must_remain_equal"])
        self.assertTrue(migration["non_target_text_segments_must_remain_byte_identical"])
        self.assertTrue(migration["protected_selector_must_remain_exact"])
        self.assertTrue(migration["write_mode_may_change_only_registered_approved_pointers"])

    def test_uncertain_semantics_stay_nonexecutive_until_authorized_role_publishes(self):
        authority = json.loads(
            (ROOT / "control_plane" / "current_control_authority.json").read_text(
                encoding="utf-8"
            )
        )
        migration = authority["semantic_migration"]
        self.assertFalse(migration["verification_request_is_task"])
        self.assertFalse(migration["verification_request_is_claimable"])
        self.assertFalse(migration["verification_request_grants_authority"])
        self.assertTrue(
            migration["future_real_verification_task_requires_immutable_v2_publication_by_authorized_role"]
        )


if __name__ == "__main__":
    unittest.main()
