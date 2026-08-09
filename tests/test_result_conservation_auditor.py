import unittest

from tools.check_references import (
    RESULT_CONSERVATION_FATES,
    validate_result_conservation_manifest,
)


SOURCE_HEAD = "260c563c7ba1b9f0dafc56a345e8ed5cd3ed0001"


def valid_manifest():
    return {
        "schema": "ENTERPRISE_MATH_RESULT_CONSERVATION_V1",
        "source_owner": {
            "id": "PR #116",
            "source_head": SOURCE_HEAD,
            "retirement_state": "L5_PROVENANCE",
        },
        "closure_state": "RESOLVED",
        "inventory_complete": True,
        "inventory_basis": ["full semantic audit of the frozen source snapshot"],
        "closure_evidence": ["final accounting comment"],
        "unresolved_results": [],
        "results": [
            {
                "id": "R-1",
                "statement": "one semantic result",
                "fate": "INTEGRATE",
                "source_evidence": ["source.py@SOURCE_HEAD"],
                "targets": ["PR #274 / canonical main"],
                "rationale": "transported without semantic loss",
                "evidence": ["fresh final-combination CI"],
            }
        ],
    }


class ResultConservationAuditorTests(unittest.TestCase):
    def test_valid_resolved_manifest_passes(self):
        self.assertEqual(validate_result_conservation_manifest(valid_manifest()), [])

    def test_exact_five_fate_vocabulary_is_stable(self):
        self.assertEqual(
            RESULT_CONSERVATION_FATES,
            {
                "INTEGRATE",
                "SUPERSEDED",
                "COMPARATOR-NEGATIVE",
                "OWNER_MOVED",
                "REJECTED",
            },
        )
        manifest = valid_manifest()
        manifest["results"][0]["fate"] = "COMPARATOR/NEGATIVE"
        errors = validate_result_conservation_manifest(manifest)
        self.assertTrue(any(".fate must be one of" in error for error in errors))

    def test_retirement_fails_with_unresolved_result(self):
        manifest = valid_manifest()
        manifest["unresolved_results"] = ["R-2"]
        errors = validate_result_conservation_manifest(manifest)
        self.assertTrue(any("unresolved_results" in error for error in errors))

    def test_retirement_requires_explicit_complete_inventory_assertion(self):
        manifest = valid_manifest()
        manifest["inventory_complete"] = False
        errors = validate_result_conservation_manifest(manifest)
        self.assertTrue(any("inventory_complete" in error for error in errors))

    def test_duplicate_semantic_result_ids_are_rejected(self):
        manifest = valid_manifest()
        duplicate = dict(manifest["results"][0])
        duplicate["fate"] = "SUPERSEDED"
        manifest["results"].append(duplicate)
        errors = validate_result_conservation_manifest(manifest)
        self.assertTrue(any("duplicate result id R-1" in error for error in errors))

    def test_each_result_requires_target_rationale_and_evidence(self):
        manifest = valid_manifest()
        result = manifest["results"][0]
        result["targets"] = []
        result["rationale"] = ""
        result["evidence"] = []
        errors = validate_result_conservation_manifest(manifest)
        self.assertTrue(any("targets" in error for error in errors))
        self.assertTrue(any("rationale" in error for error in errors))
        self.assertTrue(any("evidence" in error for error in errors))

    def test_source_snapshot_must_be_frozen_git_sha(self):
        manifest = valid_manifest()
        manifest["source_owner"]["source_head"] = "latest"
        errors = validate_result_conservation_manifest(manifest)
        self.assertTrue(any("40-hex Git SHA" in error for error in errors))

    def test_all_five_fates_are_individually_accepted(self):
        manifest = valid_manifest()
        manifest["results"] = []
        for index, fate in enumerate(sorted(RESULT_CONSERVATION_FATES), start=1):
            manifest["results"].append(
                {
                    "id": f"R-{index}",
                    "statement": fate,
                    "fate": fate,
                    "source_evidence": [f"source-{index}"],
                    "targets": [f"target-{index}"],
                    "rationale": "explicit semantic disposition",
                    "evidence": ["review evidence"],
                }
            )
        self.assertEqual(validate_result_conservation_manifest(manifest), [])


if __name__ == "__main__":
    unittest.main()
