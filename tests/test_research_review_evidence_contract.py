import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ReviewEvidenceContractTests(unittest.TestCase):
    def test_contract_splits_storage_from_operational_authority(self):
        contract = json.loads(
            (ROOT / "research_review_evidence_contract.json").read_text(encoding="utf-8")
        )
        self.assertEqual(
            "research_review_evidence.py", contract["authority_reducer"]
        )
        self.assertEqual(
            "research_review_evidence_store.py",
            contract["append_only_store_implementation"],
        )
        self.assertEqual(
            "control_plane/research_review_evidence_store.py",
            contract["store_compatibility_shim"],
        )
        self.assertEqual(
            "tools/research_result_records.py", contract["runtime_consumer"]
        )
        self.assertFalse(contract["latest_review_wins"])
        self.assertTrue(contract["all_reviews_retained"])
        self.assertIn(
            "MULTIPLE_DRIVER_REVIEWS_ARE_NOT_RESOLVED_BY_LATEST_TIMESTAMP_WINS",
            contract["core_invariants"],
        )
        self.assertIn(
            "REPOSITORY_ROOT_STORAGE_SEMANTICS_SURVIVE_INTERNAL_COMPATIBILITY_SHIMS",
            contract["core_invariants"],
        )
        self.assertIn(
            "OFFLINE_AUDIT_IS_REQUIRED_BUT_IS_NOT_A_SUBSTITUTE_FOR_RUNTIME_FAIL_CLOSED_VALIDATION",
            contract["core_invariants"],
        )

    def test_reference_integrity_executes_review_authority_audit(self):
        workflow = (ROOT / ".github/workflows/reference-integrity.yml").read_text(
            encoding="utf-8"
        )
        self.assertIn(
            "run: python research_review_evidence.py audit", workflow
        )


if __name__ == "__main__":
    unittest.main()
