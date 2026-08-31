import json
import tempfile
import unittest
from pathlib import Path

from control_plane import check_publication_quarantine_lineage_forward_safety as safety
from control_plane import research_publication_fault_isolation as publication_isolation


ROOT = Path(__file__).resolve().parents[1]
TASK = "RS-P000-L1-NATIVE-CARRIER-CONTACT-BRIDGE"


class PublicationQuarantineLineageForwardSafetyTests(unittest.TestCase):
    def test_real_native_bridge_fork_has_one_current_head_per_anchor(self):
        anchors = publication_isolation.quarantine_rows(ROOT)[TASK][
            "lineage_anchor_publication_ids"
        ]
        evidence = safety.prove(TASK, anchors, ROOT)
        self.assertEqual(TASK, evidence["task_id"])
        self.assertEqual(set(anchors), set(evidence["anchor_to_current_head"]))
        self.assertEqual(len(anchors), len(evidence["current_active_head_publication_ids"]))
        self.assertFalse(evidence["operational_publication_selected"])
        self.assertFalse(evidence["working_truth_granted"])
        self.assertFalse(evidence["foundation_authority_granted"])
        self.assertFalse(evidence["canonical_promotion_granted"])
        self.assertFalse(evidence["successor_triggered"])

    def test_new_sibling_below_anchor_fails_closed(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            directory = root / "research_task_records" / "T"
            directory.mkdir(parents=True)
            rows = [
                {
                    "record_schema": "ENTERPRISE_MATH_TASK_PUBLICATION_RECORD_V2",
                    "record_state": "ACTIVE",
                    "task_id": "T",
                    "publication_id": "A",
                    "supersedes_publication_id": None,
                },
                {
                    "record_schema": "ENTERPRISE_MATH_TASK_PUBLICATION_RECORD_V2",
                    "record_state": "ACTIVE",
                    "task_id": "T",
                    "publication_id": "B",
                    "supersedes_publication_id": None,
                },
                {
                    "record_schema": "ENTERPRISE_MATH_TASK_PUBLICATION_RECORD_V2",
                    "record_state": "ACTIVE",
                    "task_id": "T",
                    "publication_id": "A1",
                    "supersedes_publication_id": "A",
                },
                {
                    "record_schema": "ENTERPRISE_MATH_TASK_PUBLICATION_RECORD_V2",
                    "record_state": "ACTIVE",
                    "task_id": "T",
                    "publication_id": "A2",
                    "supersedes_publication_id": "A",
                },
            ]
            for row in rows:
                (directory / f"{row['publication_id']}.json").write_text(
                    json.dumps(row), encoding="utf-8"
                )
            with self.assertRaisesRegex(safety.LineageForwardSafetyError, "branches below A"):
                safety.prove("T", ["A", "B"], root)

    def test_unanchored_third_active_head_fails_closed(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            directory = root / "research_task_records" / "T"
            directory.mkdir(parents=True)
            for publication_id in ("A", "B", "C"):
                row = {
                    "record_schema": "ENTERPRISE_MATH_TASK_PUBLICATION_RECORD_V2",
                    "record_state": "ACTIVE",
                    "task_id": "T",
                    "publication_id": publication_id,
                    "supersedes_publication_id": None,
                }
                (directory / f"{publication_id}.json").write_text(
                    json.dumps(row), encoding="utf-8"
                )
            with self.assertRaisesRegex(safety.LineageForwardSafetyError, "belongs to 0 anchored lineages"):
                safety.prove("T", ["A", "B"], root)


if __name__ == "__main__":
    unittest.main()
