import json
import tempfile
import unittest
from pathlib import Path

import research_parallel_evidence as parallel


ROOT = Path(__file__).resolve().parents[1]


def write_json(path: Path, value: dict):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


class ParallelEvidenceStateTests(unittest.TestCase):
    def make_result(self, root: Path, result_id: str, publication_id: str = "TP2-P1"):
        write_json(
            root / "research_result_records" / "RS-T" / f"{result_id}.json",
            {
                "result_id": result_id,
                "task_id": "RS-T",
                "publication_id": publication_id,
            },
        )

    def make_publication(self, root: Path, publication_id: str = "TP2-P1"):
        write_json(
            root / "research_task_records" / "RS-T" / f"{publication_id}.json",
            {
                "publication_id": publication_id,
                "task_id": "RS-T",
            },
        )

    def test_single_result_keeps_low_burden_flow(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            self.make_result(root, "RR-1")
            state = parallel.state("RS-T", "TP2-P1", root)
            self.assertEqual("SINGLE_RESULT_FLOW", state["parallel_state"])

    def test_two_results_do_not_latest_win(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            self.make_result(root, "RR-1")
            self.make_result(root, "RR-2")
            state = parallel.state("RS-T", "TP2-P1", root)
            self.assertEqual("AWAITING_PARALLEL_INTAKE", state["parallel_state"])
            self.assertEqual(["RR-1", "RR-2"], state["result_ids"])

    def test_two_reference_passes_then_synthesis(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            self.make_publication(root)
            self.make_result(root, "RR-1")
            self.make_result(root, "RR-2")
            evidence = parallel.evidence_hash(["TP2-P1"], ["RR-1", "RR-2"])
            intake = {
                "schema": parallel.INTAKE_SCHEMA,
                "intake_id": "PI-1",
                "task_id": "RS-T",
                "mode": "PARALLEL_RESULTS",
                "publication_ids": ["TP2-P1"],
                "result_ids": ["RR-1", "RR-2"],
                "evidence_set_sha256": evidence,
                "opened_by": "EM-DVR-ABC123",
                "opened_at": "2026-08-26T20:00:00+08:00",
                "dispatch_authority_unchanged": True,
                "working_truth_granted": False,
                "canonical_promotion_granted": False,
            }
            write_json(root / "research_parallel_intakes" / "RS-T" / "PI-1.json", intake)
            self.assertEqual("AWAITING_REFERENCE_PASS_1", parallel.state("RS-T", "TP2-P1", root)["parallel_state"])

            common = {
                "schema": parallel.PASS_SCHEMA,
                "intake_id": "PI-1",
                "task_id": "RS-T",
                "publication_ids": ["TP2-P1"],
                "result_ids": ["RR-1", "RR-2"],
                "evidence_set_sha256": evidence,
                "reviewer_id": "EM-DVR-ABC123",
                "independence_status": "SHARED_CONTROL_CONTEXT_DISCLOSED",
                "findings_summary": "both retained",
                "recommendation": "continue",
                "working_truth_granted": False,
                "canonical_promotion_granted": False,
            }
            pass1 = {**common, "pass_id": "RP1-1", "pass_number": 1, "pass_kind": parallel.PASS_KINDS[1]}
            write_json(root / "research_parallel_reference_passes" / "PI-1" / "RP1-1.json", pass1)
            self.assertEqual("AWAITING_REFERENCE_PASS_2", parallel.state("RS-T", "TP2-P1", root)["parallel_state"])

            pass2 = {**common, "pass_id": "RP2-1", "pass_number": 2, "pass_kind": parallel.PASS_KINDS[2]}
            write_json(root / "research_parallel_reference_passes" / "PI-1" / "RP2-1.json", pass2)
            self.assertEqual("AWAITING_SYNTHESIS", parallel.state("RS-T", "TP2-P1", root)["parallel_state"])

            synthesis = {
                "schema": parallel.SYNTH_SCHEMA,
                "synthesis_id": "PS-1",
                "intake_id": "PI-1",
                "task_id": "RS-T",
                "publication_ids": ["TP2-P1"],
                "result_ids": ["RR-1", "RR-2"],
                "evidence_set_sha256": evidence,
                "reference_pass_ids": ["RP1-1", "RP2-1"],
                "disposition": "KEEP_PARALLEL",
                "operational_publication_id": "TP2-P1",
                "task_terminal": False,
                "working_truth_granted": False,
                "canonical_promotion_granted": False,
            }
            write_json(root / "research_parallel_syntheses" / "RS-T" / "PS-1.json", synthesis)
            self.assertEqual("PARALLEL_SYNTHESIS_NONTERMINAL", parallel.state("RS-T", "TP2-P1", root)["parallel_state"])
            self.assertEqual([], parallel.audit(root))

    def test_changed_evidence_set_cannot_reuse_old_passes(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            self.make_publication(root)
            self.make_result(root, "RR-1")
            self.make_result(root, "RR-2")
            wrong = "sha256:" + "0" * 64
            write_json(
                root / "research_parallel_intakes" / "RS-T" / "PI-1.json",
                {
                    "schema": parallel.INTAKE_SCHEMA,
                    "intake_id": "PI-1",
                    "task_id": "RS-T",
                    "mode": "PARALLEL_RESULTS",
                    "publication_ids": ["TP2-P1"],
                    "result_ids": ["RR-1", "RR-2"],
                    "evidence_set_sha256": wrong,
                    "opened_by": "EM-DVR-ABC123",
                    "opened_at": "2026-08-26T20:00:00+08:00",
                    "dispatch_authority_unchanged": True,
                    "working_truth_granted": False,
                    "canonical_promotion_granted": False,
                },
            )
            self.assertTrue(any("evidence_set_sha256 mismatch" in item for item in parallel.audit(root)))


class RepositoryParallelEvidenceTests(unittest.TestCase):
    def test_repository_declared_parallel_evidence_is_auditable(self):
        self.assertEqual([], parallel.audit(ROOT))


if __name__ == "__main__":
    unittest.main()
