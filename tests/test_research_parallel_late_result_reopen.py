import json
import tempfile
import unittest
from pathlib import Path

import research_parallel_evidence as parallel
from tools import research_result_records as results


def write_json(path: Path, value: dict):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


class LateResultExactSetReopenTests(unittest.TestCase):
    def add_result(self, root: Path, result_id: str, frozen_at: str):
        write_json(
            root / "research_result_records" / "RS-T" / f"{result_id}.json",
            {
                "record_schema": results.RESULT_SCHEMA,
                "result_id": result_id,
                "task_id": "RS-T",
                "publication_id": "TP2-P1",
                "frozen_at": frozen_at,
            },
        )

    def test_late_result_after_terminal_synthesis_reopens_exact_set_intake(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
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
            self.add_result(root, "RR-EARLY", "2026-08-26T10:00:00+00:00")
            self.add_result(root, "RR-LATE", "2026-08-26T20:00:00+00:00")

            publication_ids = ["TP2-P1"]
            result_ids = ["RR-EARLY", "RR-LATE"]
            evidence = parallel.evidence_hash(publication_ids, result_ids)
            write_json(
                root / "research_parallel_intakes" / "RS-T" / "PI-1.json",
                {
                    "schema": parallel.INTAKE_SCHEMA,
                    "intake_id": "PI-1",
                    "task_id": "RS-T",
                    "mode": "PARALLEL_RESULTS",
                    "publication_ids": publication_ids,
                    "result_ids": result_ids,
                    "evidence_set_sha256": evidence,
                    "opened_by": "EM-DVR-ABC123",
                    "opened_at": "2026-08-26T20:00:00+00:00",
                    "dispatch_authority_unchanged": True,
                    "working_truth_granted": False,
                    "canonical_promotion_granted": False,
                },
            )
            common = {
                "schema": parallel.PASS_SCHEMA,
                "intake_id": "PI-1",
                "task_id": "RS-T",
                "publication_ids": publication_ids,
                "result_ids": result_ids,
                "evidence_set_sha256": evidence,
                "reviewer_id": "EM-DVR-ABC123",
                "independence_status": "SHARED_CONTROL_CONTEXT_DISCLOSED",
                "findings_summary": "retain exact evidence set",
                "recommendation": "synthesize",
                "working_truth_granted": False,
                "canonical_promotion_granted": False,
            }
            write_json(
                root / "research_parallel_reference_passes" / "PI-1" / "RP1-1.json",
                {
                    **common,
                    "pass_id": "RP1-1",
                    "pass_number": 1,
                    "pass_kind": parallel.PASS_KINDS[1],
                },
            )
            write_json(
                root / "research_parallel_reference_passes" / "PI-1" / "RP2-1.json",
                {
                    **common,
                    "pass_id": "RP2-1",
                    "pass_number": 2,
                    "pass_kind": parallel.PASS_KINDS[2],
                },
            )
            write_json(
                root / "research_parallel_syntheses" / "RS-T" / "PS-1.json",
                {
                    "schema": parallel.SYNTH_SCHEMA,
                    "synthesis_id": "PS-1",
                    "intake_id": "PI-1",
                    "task_id": "RS-T",
                    "publication_ids": publication_ids,
                    "result_ids": result_ids,
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

            terminal = results.task_result_state("RS-T", root, publication_id="TP2-P1")
            self.assertEqual("TERMINAL", terminal["state"])
            self.assertTrue(terminal["terminal"])
            self.assertEqual("PS-1", terminal["result"]["result_id"])

            self.add_result(root, "RR-LATER", "2026-08-27T01:00:00+00:00")
            reopened = results.task_result_state("RS-T", root, publication_id="TP2-P1")

            self.assertEqual("AWAITING_DRIVER_REVIEW", reopened["state"])
            self.assertFalse(reopened["terminal"])
            self.assertEqual("AWAITING_PARALLEL_INTAKE", reopened["parallel_state"])
            self.assertEqual(
                ["RR-EARLY", "RR-LATE", "RR-LATER"],
                reopened["parallel_result_ids"],
            )
            self.assertIsNone(reopened["parallel_intake_id"])
            self.assertIsNone(reopened["evidence_set_sha256"])


if __name__ == "__main__":
    unittest.main()
