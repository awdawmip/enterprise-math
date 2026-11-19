import json
import tempfile
import unittest
from pathlib import Path

import research_operational_publications as operational
import research_parallel_evidence as parallel
from test_research_task_record_compatibility import _write_current_record, _write_semantic_fixture


def write_json(path: Path, value: dict):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


class OperationalPublicationTests(unittest.TestCase):
    def publication(self, root: Path, pid: str, *, task_id="RS-T", supersedes=None, state="ACTIVE"):
        if not (root / "research_task_semantic_integrity_quarantines.json").exists():
            _write_semantic_fixture(root)
        _write_current_record(
            root, task_id=task_id, publication_id=pid,
            parent_objective_id="OBJ-OPERATIONAL-FIXTURE",
            record_state=state, supersedes_publication_id=supersedes,
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

    def synthesis(self, root: Path, publication_ids, operational_pid="TP2-B", reference_ids=None):
        reference_ids = ["RP1", "RP2"] if reference_ids is None else reference_ids
        digest = parallel.evidence_hash(publication_ids, [])
        write_json(root / "research_parallel_intakes" / "RS-T" / "PI-1.json", {
            "schema": parallel.INTAKE_SCHEMA, "intake_id": "PI-1", "task_id": "RS-T",
            "mode": "PARALLEL_PUBLICATIONS", "publication_ids": publication_ids,
            "result_ids": [], "evidence_set_sha256": digest,
            "opened_by": "EM-DVR-ABC123", "opened_at": "2026-08-26T20:00:00+00:00",
            "dispatch_authority_unchanged": True, "working_truth_granted": False,
            "canonical_promotion_granted": False,
        })
        for number, pass_id in enumerate(reference_ids, 1):
            write_json(root / "research_parallel_reference_passes" / "PI-1" / f"{pass_id}.json", {
                "schema": parallel.PASS_SCHEMA, "pass_id": pass_id, "intake_id": "PI-1",
                "task_id": "RS-T", "pass_number": number, "pass_kind": "EVIDENCE_CROSSCHECK",
                "publication_ids": publication_ids, "result_ids": [], "evidence_set_sha256": digest,
                "reviewer_id": "EM-DVR-ABC123", "independence_status": "SHARED_CONTROL_CONTEXT_DISCLOSED",
                "findings_summary": "retain both publications", "recommendation": "select operational publication",
                "working_truth_granted": False, "canonical_promotion_granted": False,
            })
        write_json(
            root / "research_parallel_syntheses" / "RS-T" / "PS-1.json",
            {
                "schema": operational.SYNTHESIS_SCHEMA,
                "synthesis_id": "PS-1",
                "intake_id": "PI-1",
                "task_id": "RS-T",
                "publication_ids": publication_ids,
                "result_ids": [],
                "evidence_set_sha256": digest,
                "reference_pass_ids": reference_ids,
                "reference_review_status": "NOT_PERFORMED" if reference_ids == [] else "RECORDED",
                "operational_publication_id": operational_pid,
                "disposition": "KEEP_PARALLEL", "task_terminal": False,
                "working_truth_granted": False, "canonical_promotion_granted": False,
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

    def test_reference_count_does_not_gate_operational_selection(self):
        for references in ([], ["RP7"], ["RP3", "RP1", "RP2"]):
            with self.subTest(references=references), tempfile.TemporaryDirectory() as td:
                root = Path(td)
                self.publication(root, "TP2-A")
                self.publication(root, "TP2-B")
                self.synthesis(root, ["TP2-A", "TP2-B"], reference_ids=references)
                self.resolution(root, self.row())
                value = operational.selection("RS-T", root)
                self.assertEqual("TP2-B", value["operational_publication_id"])
                self.assertEqual(["TP2-A", "TP2-B"], value["retained_parallel_publication_ids"])

    def test_late_reference_requires_current_synthesis_and_resolution_without_rewriting_history(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            self.publication(root, "TP2-A")
            self.publication(root, "TP2-B")
            self.synthesis(root, ["TP2-A", "TP2-B"], reference_ids=[])
            row = self.row()
            self.resolution(root, row)
            self.assertEqual("PS-1", operational.selection("RS-T", root)["parallel_synthesis_id"])
            old_path = root / "research_parallel_syntheses" / "RS-T" / "PS-1.json"
            old_bytes = old_path.read_bytes()
            synthesis = json.loads(old_bytes)
            write_json(root / "research_parallel_reference_passes" / "PI-1" / "RP3.json", {
                "schema": parallel.PASS_SCHEMA, "pass_id": "RP3", "intake_id": "PI-1",
                "task_id": "RS-T", "pass_number": 3, "pass_kind": "COUNTEREXAMPLE_CHECK",
                "publication_ids": ["TP2-A", "TP2-B"], "result_ids": [],
                "evidence_set_sha256": synthesis["evidence_set_sha256"],
                "reviewer_id": "EM-DVR-ABC123", "independence_status": "SHARED_CONTROL_CONTEXT_DISCLOSED",
                "findings_summary": "retain both publications after added check", "recommendation": "continue selection",
                "working_truth_granted": False, "canonical_promotion_granted": False,
            })
            self.assertEqual([], parallel.audit(root))
            with self.assertRaisesRegex(operational.OperationalPublicationError, "current reference snapshot"):
                operational.selection("RS-T", root)
            synthesis.update(synthesis_id="PS-2", reference_pass_ids=["RP3"], reference_review_status="RECORDED")
            parallel.write_synthesis(synthesis, root)
            with self.assertRaisesRegex(operational.OperationalPublicationError, "current reference snapshot"):
                operational.selection("RS-T", root)
            row["parallel_synthesis_id"] = "PS-2"
            self.resolution(root, row)
            self.assertEqual("PS-2", operational.selection("RS-T", root)["parallel_synthesis_id"])
            self.assertEqual(old_bytes, old_path.read_bytes())
            self.assertEqual([], parallel.audit(root))

    def test_multiple_heads_without_resolution_fail_closed_but_records_remain(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            self.publication(root, "TP2-A")
            self.publication(root, "TP2-B")
            with self.assertRaisesRegex(operational.OperationalPublicationError, "retained"):
                operational.selection("RS-T", root)
            self.assertEqual(
                {"TP2-A", "TP2-B"},
                {r["publication_id"] for r in operational.iter_publications(root) if r["task_id"] == "RS-T"},
            )

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

    def test_parallel_operational_selection_requires_explicit_synthesis(self):
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
            self.assertEqual(
                {"TP2-A", "TP2-B"},
                {r["publication_id"] for r in operational.iter_publications(root) if r["task_id"] == "RS-T"},
            )


class RepositoryOperationalPublicationTests(unittest.TestCase):
    def test_current_repository_operational_selection_is_auditable(self):
        root = Path(__file__).resolve().parents[1]
        self.assertEqual([], operational.audit(root))


if __name__ == "__main__":
    unittest.main()
