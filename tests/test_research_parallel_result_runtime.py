import json
import tempfile
import unittest
from pathlib import Path
from unittest import mock

import research_parallel_evidence as parallel
from tools import research_result_records as results


def write_json(path: Path, value: dict):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


class ParallelResultRuntimeTests(unittest.TestCase):
    def result(self, root: Path, rid: str, frozen_at: str):
        write_json(
            root / "research_result_records" / "RS-T" / f"{rid}.json",
            {
                "record_schema": results.RESULT_SCHEMA,
                "result_id": rid,
                "task_id": "RS-T",
                "publication_id": "TP2-P1",
                "frozen_at": frozen_at,
            },
        )

    def review(self, root: Path, rid: str):
        suffix = rid.removeprefix("RR-")
        write_json(
            root / "research_result_reviews" / rid / f"DR-{suffix}.json",
            {
                "record_schema": results.REVIEW_SCHEMA,
                "review_id": f"DR-{suffix}",
                "result_id": rid,
                "task_id": "RS-T",
                "driver_id": "EM-DVR-ABC123",
                "reviewed_at": "2026-08-26T19:30:00+08:00",
                "disposition": "ACCEPTED",
                "terminal": True,
            },
        )

    def publication(self, root: Path):
        write_json(
            root / "research_task_records" / "RS-T" / "TP2-P1.json",
            {
                "record_schema": "ENTERPRISE_MATH_TASK_PUBLICATION_RECORD_V2",
                "record_state": "ACTIVE",
                "task_id": "RS-T",
                "publication_id": "TP2-P1",
                "publication_generation": 1,
                "supersedes_publication_id": None,
            },
        )

    def intake(self, root: Path):
        evidence = parallel.evidence_hash(["TP2-P1"], ["RR-EARLY", "RR-LATE"])
        write_json(
            root / "research_parallel_intakes" / "RS-T" / "PI-1.json",
            {
                "schema": parallel.INTAKE_SCHEMA,
                "intake_id": "PI-1",
                "task_id": "RS-T",
                "mode": "PARALLEL_RESULTS",
                "publication_ids": ["TP2-P1"],
                "result_ids": ["RR-EARLY", "RR-LATE"],
                "evidence_set_sha256": evidence,
                "opened_by": "EM-DVR-ABC123",
                "opened_at": "2026-08-26T20:00:00+08:00",
                "dispatch_authority_unchanged": True,
                "working_truth_granted": False,
                "canonical_promotion_granted": False,
            },
        )
        return evidence

    def passes(self, root: Path, evidence: str):
        common = {
            "schema": parallel.PASS_SCHEMA,
            "intake_id": "PI-1",
            "task_id": "RS-T",
            "publication_ids": ["TP2-P1"],
            "result_ids": ["RR-EARLY", "RR-LATE"],
            "evidence_set_sha256": evidence,
            "reviewer_id": "EM-DVR-ABC123",
            "independence_status": "SHARED_CONTROL_CONTEXT_DISCLOSED",
            "findings_summary": "retain both",
            "recommendation": "synthesize",
            "working_truth_granted": False,
            "canonical_promotion_granted": False,
        }
        write_json(
            root / "research_parallel_reference_passes" / "PI-1" / "RP1-1.json",
            {**common, "pass_id": "RP1-1", "pass_number": 1, "pass_kind": parallel.PASS_KINDS[1]},
        )
        write_json(
            root / "research_parallel_reference_passes" / "PI-1" / "RP2-1.json",
            {**common, "pass_id": "RP2-1", "pass_number": 2, "pass_kind": parallel.PASS_KINDS[2]},
        )

    def setup_parallel(self, root: Path):
        self.publication(root)
        self.result(root, "RR-EARLY", "2026-08-26T10:00:00+00:00")
        self.result(root, "RR-LATE", "2026-08-26T20:00:00+00:00")

    def resolve_source_reviews(self, root: Path):
        self.review(root, "RR-EARLY")
        self.review(root, "RR-LATE")

    def followup_ready(self):
        return {
            "required": False,
            "ready": True,
            "state": "LEGACY_PRE_CUTOVER",
            "packet": None,
        }

    def test_multiple_results_never_latest_win(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            self.setup_parallel(root)
            state = results.task_result_state("RS-T", root, publication_id="TP2-P1")
            self.assertEqual("AWAITING_DRIVER_REVIEW", state["state"])
            self.assertEqual("AWAITING_RESULT_REVIEW_AUTHORITY", state["parallel_state"])
            self.assertEqual(["RR-EARLY", "RR-LATE"], state["parallel_result_ids"])
            self.assertEqual(["RR-EARLY", "RR-LATE"], state["pending_result_review_ids"])
            self.assertNotEqual("RR-LATE", state["result"]["result_id"])

    def test_two_passes_then_nonterminal_synthesis_returns_to_execution(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            self.setup_parallel(root)
            self.resolve_source_reviews(root)
            evidence = self.intake(root)
            self.passes(root, evidence)
            write_json(
                root / "research_parallel_syntheses" / "RS-T" / "PS-1.json",
                {
                    "schema": parallel.SYNTH_SCHEMA,
                    "synthesis_id": "PS-1",
                    "intake_id": "PI-1",
                    "task_id": "RS-T",
                    "publication_ids": ["TP2-P1"],
                    "result_ids": ["RR-EARLY", "RR-LATE"],
                    "evidence_set_sha256": evidence,
                    "reference_pass_ids": ["RP1-1", "RP2-1"],
                    "disposition": "KEEP_PARALLEL",
                    "operational_publication_id": "TP2-P1",
                    "task_terminal": False,
                    "working_truth_granted": False,
                    "canonical_promotion_granted": False,
                },
            )
            with mock.patch.object(
                results._driver_followup,
                "state_for_review",
                return_value=self.followup_ready(),
            ):
                state = results.task_result_state("RS-T", root, publication_id="TP2-P1")
            self.assertEqual("RETURN_TO_EXECUTION", state["state"])
            self.assertEqual("PARALLEL_SYNTHESIS_NONTERMINAL", state["parallel_state"])
            self.assertEqual("PS-1", state["result"]["result_id"])
            self.assertEqual({"RR-EARLY", "RR-LATE"}, set(state["result_review_authority"]))

    def test_terminal_synthesis_without_control_disposition_fails_closed(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            self.setup_parallel(root)
            self.resolve_source_reviews(root)
            evidence = self.intake(root)
            self.passes(root, evidence)
            write_json(
                root / "research_parallel_syntheses" / "RS-T" / "PS-1.json",
                {
                    "schema": parallel.SYNTH_SCHEMA,
                    "synthesis_id": "PS-1",
                    "intake_id": "PI-1",
                    "task_id": "RS-T",
                    "publication_ids": ["TP2-P1"],
                    "result_ids": ["RR-EARLY", "RR-LATE"],
                    "evidence_set_sha256": evidence,
                    "reference_pass_ids": ["RP1-1", "RP2-1"],
                    "disposition": "KEEP_PARALLEL",
                    "operational_publication_id": "TP2-P1",
                    "task_terminal": True,
                    "working_truth_granted": False,
                    "canonical_promotion_granted": False,
                },
            )
            with mock.patch.object(
                results._driver_followup,
                "state_for_review",
                return_value=self.followup_ready(),
            ):
                state = results.task_result_state("RS-T", root, publication_id="TP2-P1")
            self.assertEqual("AWAITING_DRIVER_REVIEW", state["state"])
            self.assertFalse(state["terminal"])
            self.assertEqual("TERMINAL_SYNTHESIS_MISSING_CONTROL_DISPOSITION", state["parallel_state"])
            self.assertEqual({"RR-EARLY", "RR-LATE"}, set(state["result_review_authority"]))

    def test_terminal_synthesis_with_explicit_control_disposition_can_close(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            self.setup_parallel(root)
            self.resolve_source_reviews(root)
            evidence = self.intake(root)
            self.passes(root, evidence)
            write_json(
                root / "research_parallel_syntheses" / "RS-T" / "PS-1.json",
                {
                    "schema": parallel.SYNTH_SCHEMA,
                    "synthesis_id": "PS-1",
                    "intake_id": "PI-1",
                    "task_id": "RS-T",
                    "publication_ids": ["TP2-P1"],
                    "result_ids": ["RR-EARLY", "RR-LATE"],
                    "evidence_set_sha256": evidence,
                    "reference_pass_ids": ["RP1-1", "RP2-1"],
                    "disposition": "KEEP_PARALLEL",
                    "operational_publication_id": "TP2-P1",
                    "task_terminal": True,
                    "terminal_control_disposition": "ACCEPTED",
                    "working_truth_granted": False,
                    "canonical_promotion_granted": False,
                },
            )
            with mock.patch.object(
                results._driver_followup,
                "state_for_review",
                return_value=self.followup_ready(),
            ):
                state = results.task_result_state("RS-T", root, publication_id="TP2-P1")
            self.assertEqual("TERMINAL", state["state"])
            self.assertTrue(state["terminal"])
            self.assertEqual("PS-1", state["result"]["result_id"])
            self.assertEqual("ACCEPTED", state["review"]["disposition"])
            self.assertEqual({"RR-EARLY", "RR-LATE"}, set(state["result_review_authority"]))


if __name__ == "__main__":
    unittest.main()
