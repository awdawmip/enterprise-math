import unittest

from control_plane import check_architecture_publication_cutover_evidence as evidence


class ArchitecturePublicationCutoverEvidenceTests(unittest.TestCase):
    def test_proposed_cutover_is_exactly_six_pointer_and_non_authorizing(self):
        report = evidence.prove()
        self.assertEqual(
            "CONTROL_STRUCTURAL_EVIDENCE_ONLY_NOT_GOVERNANCE_APPROVAL",
            report["status"],
        )
        self.assertEqual(6, report["changed_pointer_count"])
        self.assertEqual(6, len(report["changed_pointers"]))
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
