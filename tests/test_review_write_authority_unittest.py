import json
import unittest
from pathlib import Path

from control_plane import check_review_write_authority as review_write


ROOT = Path(__file__).resolve().parents[1]


class ReviewWriteAuthorityTests(unittest.TestCase):
    def test_review_write_authority_contract_is_consistent(self):
        review_write.check()

    def test_cached_result_and_force_write_are_not_authority(self):
        authority = json.loads(
            (ROOT / "control_plane" / "current_control_authority.json").read_text(
                encoding="utf-8"
            )
        )["review_write_authority"]
        self.assertFalse(authority["caller_cached_result_is_write_authority"])
        self.assertFalse(authority["earlier_read_snapshot_is_write_authority"])
        self.assertFalse(authority["remote_write_force_allowed"])
        self.assertTrue(authority["refresh_result_binding_immediately_before_remote_mutation"])
        self.assertTrue(authority["review_record_result_digest_must_match_mutation_parent_bytes"])

    def test_binding_fault_cannot_be_repaired_by_control_disposition_rewrite(self):
        authority = json.loads(
            (ROOT / "control_plane" / "current_control_authority.json").read_text(
                encoding="utf-8"
            )
        )["review_write_authority"]
        self.assertFalse(authority["binding_mismatch_is_auto_repaired"])
        self.assertFalse(authority["control_plane_may_rewrite_review_disposition"])
        self.assertTrue(authority["binding_mismatch_removes_review_operational_authority"])
        self.assertFalse(authority["nonoperational_review_retains_followup_authority"])


if __name__ == "__main__":
    unittest.main()
