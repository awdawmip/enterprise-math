import unittest

from control_plane import check_architecture_publication_cutover_evidence as evidence


class ArchitecturePublicationCutoverEvidenceTests(unittest.TestCase):
    def test_current_six_pointer_cutover_needs_no_change_and_grants_no_authority(self):
        report = evidence.prove()
        self.assertEqual(
            "CURRENT_ARCHITECTURE_V2_POINTERS_VERIFIED_NO_CHANGE_REQUIRED",
            report["status"],
        )
        self.assertEqual("VERIFIED_NO_POINTER_CHANGE_REQUIRED", report["registry_state"])
        self.assertEqual(6, report["registered_pointer_count"])
        self.assertEqual(6, len(report["before_values"]))
        self.assertEqual(0, report["changed_pointer_count"])
        self.assertEqual([], report["changed_pointers"])
        self.assertEqual(report["before_values"], report["after_values"])
        self.assertTrue(report["non_target_structure_equal"])
        self.assertEqual(
            report["non_target_structure_sha256"],
            report["proposed_non_target_structure_sha256"],
        )
        self.assertFalse(report["governance_approval_granted"])
        self.assertFalse(report["migration_authority_granted"])

    def test_research_semantic_sentinels_are_digest_identical(self):
        report = evidence.prove()
        self.assertGreaterEqual(len(report["semantic_sentinel_digests"]), 10)
        for row in report["semantic_sentinel_digests"].values():
            self.assertEqual(row["before"], row["after"])


if __name__ == "__main__":
    unittest.main()
