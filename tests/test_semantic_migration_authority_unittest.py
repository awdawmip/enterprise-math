import json
import unittest
from pathlib import Path

from control_plane import check_semantic_migration_authority as authority_check


ROOT = Path(__file__).resolve().parents[1]


class SemanticMigrationAuthorityTests(unittest.TestCase):
    def test_authority_contract_is_self_consistent(self):
        authority_check.check()

    def test_control_mode_cannot_turn_verification_request_into_task(self):
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
            migration[
                "future_real_verification_task_requires_immutable_v2_publication_by_authorized_role"
            ]
        )

    def test_large_mixed_json_cleanup_is_exact_span_by_default(self):
        authority = json.loads(
            (ROOT / "control_plane" / "current_control_authority.json").read_text(
                encoding="utf-8"
            )
        )
        migration = authority["semantic_migration"]
        self.assertEqual(
            "FORBIDDEN_BY_DEFAULT",
            migration["large_or_mixed_json_whole_file_reserialization_for_pointer_cleanup"],
        )
        self.assertTrue(migration["exact_expected_git_blob_required_before_pending_patch"])
        self.assertTrue(migration["dry_run_required_before_write"])
        self.assertTrue(migration["non_target_text_segments_must_remain_byte_identical"])
        self.assertTrue(migration["protected_selector_must_remain_exact"])


if __name__ == "__main__":
    unittest.main()
