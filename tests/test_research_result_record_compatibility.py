from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from control_plane import check_result_review_binding_fault_isolated as binding_check
from tools import research_result_records as records


class ResultRecordCompatibilityTests(unittest.TestCase):
    def test_current_repository_fault_isolated_result_review_audit_passes(self) -> None:
        self.assertEqual([], binding_check.audit())

    def test_current_repository_normalizes_only_named_history(self) -> None:
        results = {item["result_id"]: item for item in records.iter_results(records.ROOT)}
        self.assertEqual("NO_GO", results["RR-8992ACCB57F4A22CB843"]["terminal_verdict"])
        self.assertEqual("NO_GO", results["RR-CBCAF6EF07B1C8493C17"]["terminal_verdict"])
        self.assertEqual("NO_GO", results["RR-E623A0364F580D6D1C0F"]["terminal_verdict"])
        self.assertEqual("RESULT_ONLY", results["RR-4D51F40A41E59F28BA98"]["method_harvest"])
        self.assertNotIn("RR-A33E88150B0DAD0B13B8", results)
        self.assertIn("RR-78BAD07DCE4EA3FC1F40", results)

        boundary = results["RR-8992ACCB57F4A22CB843"]
        boundary_path = records.ROOT / boundary["return_path"]
        self.assertEqual(records._impl._sha256(boundary_path), boundary["return_sha256"])

        pcf4r = results["RR-F24971D684C868A325E2"]
        phase = next(
            row for row in pcf4r["output_manifest"]
            if row["path"].endswith("PHASE_A_FREEZE.md")
        )
        self.assertEqual(records._impl._sha256(records.ROOT / phase["path"]), phase["sha256"])

        reviews = {item["review_id"]: item for item in records.iter_reviews(records.ROOT)}
        self.assertEqual("NONE", reviews["DR-78A3B92E2016DF7AB1D3"]["destination_class"])
        ntirf = reviews["DR-E3B831C16E7BA03B153C"]
        self.assertEqual(records._impl._sha256(records.ROOT / ntirf["review_path"]), ntirf["review_sha256"])
        self.assertIn("DR-4BB8913C8173C7868242", reviews)

    def test_sha_repair_requires_primary_git_blob_identity(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            artifact = root / "artifact.md"
            artifact.write_text("frozen\n", encoding="utf-8")
            record_path = root / "record.json"
            record_path.write_text("{}\n", encoding="utf-8")
            item = {
                "result_id": "RR-TST",
                "_record_path": "record.json",
                "terminal_verdict": "EXACT_OBSTRUCTION",
                "return_path": "artifact.md",
                "return_blob_sha1": records._impl._blob(artifact),
                "return_sha256": "sha256:stale",
                "output_manifest": [
                    {
                        "path": "artifact.md",
                        "git_blob_sha1": records._impl._blob(artifact),
                        "sha256": "sha256:stale",
                    }
                ],
            }
            row = {
                "record_path": "record.json",
                "record_blob_sha1": records._impl._blob(record_path),
                "field_aliases": [
                    {"field": "terminal_verdict", "from": "EXACT_OBSTRUCTION", "to": "NO_GO"}
                ],
                "artifact_sha256_repairs": ["artifact.md"],
                "reason": "test",
            }
            normalized = records._normalize_result_item(item, row, root)
            self.assertEqual("NO_GO", normalized["terminal_verdict"])
            self.assertEqual(records._impl._sha256(artifact), normalized["return_sha256"])
            artifact.write_text("drift\n", encoding="utf-8")
            with self.assertRaisesRegex(records.ResultRecordError, "Git blob drift forbids SHA repair"):
                records._normalize_result_item(item, row, root)

    def test_record_blob_drift_blocks_enum_alias(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            record_path = root / "record.json"
            record_path.write_text("{}\n", encoding="utf-8")
            item = {
                "result_id": "RR-TST",
                "_record_path": "record.json",
                "terminal_verdict": "EXACT_OBSTRUCTION",
                "output_manifest": [],
            }
            row = {
                "record_path": "record.json",
                "record_blob_sha1": "sha1:" + "0" * 40,
                "field_aliases": [
                    {"field": "terminal_verdict", "from": "EXACT_OBSTRUCTION", "to": "NO_GO"}
                ],
                "artifact_sha256_repairs": [],
                "reason": "test",
            }
            with self.assertRaisesRegex(records.ResultRecordError, "immutable record blob drift"):
                records._normalize_result_item(item, row, root)

    def test_missing_return_pointer_may_be_recovered_only_from_exact_manifest_pin(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            artifact = root / "return.md"
            artifact.write_text("frozen\n", encoding="utf-8")
            record_path = root / "record.json"
            record_path.write_text("{}\n", encoding="utf-8")
            item = {
                "result_id": "RR-TST",
                "_record_path": "record.json",
                "output_manifest": [
                    {
                        "path": "return.md",
                        "git_blob_sha1": records._impl._blob(artifact),
                    }
                ],
            }
            row = {
                "record_path": "record.json",
                "record_blob_sha1": records._impl._blob(record_path),
                "field_aliases": [],
                "return_artifact_from_manifest": "return.md",
                "artifact_sha256_repairs": ["return.md"],
                "reason": "test",
            }
            normalized = records._normalize_result_item(item, row, root)
            self.assertEqual("return.md", normalized["return_path"])
            self.assertEqual(records._impl._blob(artifact), normalized["return_blob_sha1"])
            artifact.write_text("drift\n", encoding="utf-8")
            with self.assertRaisesRegex(records.ResultRecordError, "Git blob drift"):
                records._normalize_result_item(item, row, root)


if __name__ == "__main__":
    unittest.main()
