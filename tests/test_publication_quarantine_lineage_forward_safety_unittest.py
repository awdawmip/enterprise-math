import json
import tempfile
import unittest
from pathlib import Path

from control_plane import check_publication_quarantine_lineage_forward_safety as safety
from control_plane import research_publication_fault_isolation as publication_isolation


ROOT = Path(__file__).resolve().parents[1]
TASK = "RS-P000-L1-NATIVE-CARRIER-CONTACT-BRIDGE"


class PublicationQuarantineLineageForwardSafetyTests(unittest.TestCase):
    def test_real_native_bridge_fork_is_quarantined_or_resolved_exactly(self):
        quarantines = publication_isolation.quarantine_rows(ROOT)
        if TASK in quarantines:
            anchors = quarantines[TASK]["lineage_anchor_publication_ids"]
            evidence = safety.prove(TASK, anchors, ROOT)
            self.assertEqual(TASK, evidence["task_id"])
            self.assertEqual(set(anchors), set(evidence["anchor_to_current_head"]))
            self.assertEqual(len(anchors), len(evidence["current_active_head_publication_ids"]))
            self.assertFalse(evidence["operational_publication_selected"])
            self.assertFalse(evidence["working_truth_granted"])
            self.assertFalse(evidence["foundation_authority_granted"])
            self.assertFalse(evidence["canonical_promotion_granted"])
            self.assertFalse(evidence["successor_triggered"])
            return

        registry = json.loads(
            (ROOT / "research_task_publication_resolutions.json").read_text(
                encoding="utf-8"
            )
        )
        rows = [row for row in registry.get("resolutions", []) if row.get("task_id") == TASK]
        self.assertEqual(1, len(rows))
        row = rows[0]
        expected_heads = {
            "TP2-3F6A92D8C1E740B5A2C9",
            "TP2-4A84B81FD5CAB8CD0359",
            "TP2-FBDBDBE1C5BDF65F97A0",
        }
        self.assertEqual(
            "TP2-FBDBDBE1C5BDF65F97A0",
            row["operational_publication_id"],
        )
        self.assertEqual(expected_heads, set(row["retained_parallel_publication_ids"]))
        self.assertEqual(
            expected_heads - {row["operational_publication_id"]},
            set(row["quarantined_publication_ids"]),
        )
        self.assertFalse(row["working_truth_granted"])
        self.assertFalse(row["canonical_promotion_granted"])
        self.assertFalse(row["successor_triggered"])

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
