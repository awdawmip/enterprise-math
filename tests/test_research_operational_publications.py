import json
import tempfile
import unittest
from pathlib import Path

import research_operational_publications as operational


def write_json(path: Path, value: dict):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


class OperationalPublicationTests(unittest.TestCase):
    def publication(self, root: Path, pid: str, *, task_id="RS-T", supersedes=None, state="ACTIVE"):
        write_json(
            root / "research_task_records" / task_id / f"{pid}.json",
            {
                "record_schema": operational.RECORD_SCHEMA,
                "record_state": state,
                "task_id": task_id,
                "publication_id": pid,
                "supersedes_publication_id": supersedes,
            },
        )

    def resolution(self, root: Path, row: dict):
        write_json(
            root / "research_task_publication_resolutions.json",
            {
                "schema": operational.RESOLUTION_SCHEMA,
                "status": "ACTIVE",
                "resolutions": [row],
            },
        )

    def synthesis(self, root: Path, publication_ids, operational_pid="TP2-B"):
        write_json(
            root / "research_parallel_syntheses" / "RS-T" / "PS-1.json",
            {
                "schema": operational.SYNTHESIS_SCHEMA,
                "synthesis_id": "PS-1",
                "task_id": "RS-T",
                "publication_ids": publication_ids,
                "reference_pass_ids": ["RP1", "RP2"],
                "operational_publication_id": operational_pid,
            },
        )

    def row(self):
        return {
            "task_id": "RS-T",
            "operational_publication_id": "TP2-B",
            "canonical_publication_id": "TP2-B",
            "retained_parallel_publication_ids": ["TP2-A", "TP2-B"],
            "quarantined_publication_ids": ["TP2-A"],
            "parallel_synthesis_id": "PS-1",
            "working_truth_granted": False,
            "canonical_promotion_granted": False,
            "successor_triggered": False,
        }

    def test_single_head_needs_no_resolution(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            self.publication(root, "TP2-A")
            value = operational.selection("RS-T", root)
            self.assertEqual("TP2-A", value["operational_publication_id"])
            self.assertEqual(["TP2-A"], value["retained_parallel_publication_ids"])
            self.assertEqual("SINGLE_ACTIVE_HEAD", value["selection_source"])

    def test_multiple_heads_are_retained_not_rejected(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            self.publication(root, "TP2-A")
            self.publication(root, "TP2-B")
            self.synthesis(root, ["TP2-A", "TP2-B"])
            self.resolution(root, self.row())
            value = operational.selection("RS-T", root)
            self.assertEqual("TP2-B", value["operational_publication_id"])
            self.assertEqual(["TP2-A", "TP2-B"], value["retained_parallel_publication_ids"])
            self.assertEqual("EXPLICIT_PARALLEL_SYNTHESIS_RESOLUTION", value["selection_source"])

    def test_multiple_heads_without_resolution_fail_closed_but_records_remain(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            self.publication(root, "TP2-A")
            self.publication(root, "TP2-B")
            with self.assertRaisesRegex(operational.OperationalPublicationError, "retained"):
                operational.selection("RS-T", root)
            self.assertEqual(2, len(operational.iter_publications(root)))

    def test_resolution_must_retain_every_active_head(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            self.publication(root, "TP2-A")
            self.publication(root, "TP2-B")
            self.synthesis(root, ["TP2-A", "TP2-B"])
            row = self.row()
            row["retained_parallel_publication_ids"] = ["TP2-B"]
            row["quarantined_publication_ids"] = []
            self.resolution(root, row)
            with self.assertRaisesRegex(operational.OperationalPublicationError, "retained parallel head set mismatch"):
                operational.selection("RS-T", root)

    def test_parallel_operational_selection_requires_two_pass_synthesis(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            self.publication(root, "TP2-A")
            self.publication(root, "TP2-B")
            self.resolution(root, self.row())
            with self.assertRaisesRegex(operational.OperationalPublicationError, "missing parallel synthesis"):
                operational.selection("RS-T", root)

    def test_synthesis_must_agree_with_operational_selection(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            self.publication(root, "TP2-A")
            self.publication(root, "TP2-B")
            self.synthesis(root, ["TP2-A", "TP2-B"], operational_pid="TP2-A")
            self.resolution(root, self.row())
            with self.assertRaisesRegex(operational.OperationalPublicationError, "disagrees"):
                operational.selection("RS-T", root)

    def test_superseded_generation_is_history_not_active_parallel_head(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            self.publication(root, "TP2-A")
            self.publication(root, "TP2-B", supersedes="TP2-A")
            value = operational.selection("RS-T", root)
            self.assertEqual("TP2-B", value["operational_publication_id"])
            self.assertEqual(["TP2-B"], value["retained_parallel_publication_ids"])
            self.assertEqual(2, len(operational.iter_publications(root)))


class RepositoryOperationalPublicationTests(unittest.TestCase):
    def test_current_repository_operational_selection_is_auditable(self):
        root = Path(__file__).resolve().parents[1]
        self.assertEqual([], operational.audit(root))


if __name__ == "__main__":
    unittest.main()
