"""Actual local storage -> audit -> Result/cohort/CLI reference-policy regressions."""
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

import research_parallel_evidence as parallel
from control_plane import immutable_write_transaction as transaction
from tools import research_cohort_runtime as cohorts
from tools import research_result_records as results
import test_research_parallel_result_runtime as fixtures


class AsNeededParallelReferenceTests(unittest.TestCase):
    def prepare(self, root, numbers=(), *, reviewed=False):
        fixture = fixtures.ParallelResultRuntimeTests()
        fixture.setup_parallel(root)
        if reviewed:
            fixture.resolve_source_reviews(root)
        digest = fixture.intake(root)
        pass_ids = fixture.passes(root, digest, numbers)
        return {
            "schema": parallel.SYNTH_SCHEMA,
            "synthesis_id": "PS-1",
            "intake_id": "PI-1",
            "task_id": "RS-T",
            "publication_ids": ["TP2-P1"],
            "result_ids": ["RR-EARLY", "RR-LATE"],
            "evidence_set_sha256": digest,
            "reference_pass_ids": pass_ids,
            "reference_review_status": "RECORDED" if pass_ids else "NOT_PERFORMED",
            "disposition": "RETURN_FOR_MORE_RESEARCH",
            "operational_publication_id": "TP2-P1",
            "task_terminal": False,
            "working_truth_granted": False,
            "canonical_promotion_granted": False,
        }

    def save(self, root, synthesis):
        return parallel.write_synthesis(synthesis, root)

    def runtime(self, root):
        # The review sources and exact-set authority are real fixture files.
        # Only the existing historical follow-up transport boundary is isolated.
        with mock.patch.object(results._driver_followup, "state_for_review", return_value={
            "required": False, "ready": True, "state": "LEGACY_PRE_CUTOVER", "packet": None,
        }):
            return results.task_result_state("RS-T", root, publication_id="TP2-P1")

    def add_cohort(self, root):
        for rid, lane in (("RR-EARLY", "a"), ("RR-LATE", "b")):
            path = root / "research_result_records" / "RS-T" / f"{rid}.json"
            value = json.loads(path.read_text())
            value.update(execution_cohort_id="EC-1", execution_lane_id=lane)
            fixtures.write_json(path, value)
        fixtures.write_json(root / "research_execution_cohorts" / "RS-T" / "EC-1.json", {
            "schema": "ENTERPRISE_MATH_PARALLEL_EXECUTION_COHORT_V1",
            "cohort_id": "EC-1", "task_id": "RS-T", "record_state": "ACTIVE",
            "opened_by": "EM-DVR-ABC123", "opened_at": "2026-08-26T20:00:00+00:00",
            "lanes": [{"lane_id": lane, "publication_id": "TP2-P1", "lane_role": "RESEARCH",
                       "purpose": f"route {lane}", "output_prefix": f"research_returns/EC-1/{lane}/"}
                      for lane in ("a", "b")],
            "synthesis_required": True,
            "working_truth_granted": False, "canonical_promotion_granted": False,
        })

    def test_zero_one_three_and_nonconsecutive_references_persist_without_review_credit(self):
        for numbers in ((), (7,), (3, 1, 2), (9, 2)):
            with self.subTest(numbers=numbers), tempfile.TemporaryDirectory() as td:
                root = Path(td)
                synthesis = self.prepare(root, numbers)
                saved = self.save(root, synthesis)
                self.assertEqual(synthesis, json.loads(saved.read_text()))
                evidence = parallel.state("RS-T", "TP2-P1", root)
                self.assertEqual("PARALLEL_SYNTHESIS_NONTERMINAL", evidence["parallel_state"])
                self.assertEqual(len(numbers), evidence["reference_pass_count"])
                self.assertEqual(sorted(synthesis["reference_pass_ids"]), evidence["reference_pass_ids"])
                self.assertEqual(synthesis["reference_review_status"], evidence["reference_review_status"])
                state = self.runtime(root)
                self.assertEqual("AWAITING_RESULT_REVIEW_AUTHORITY", state["parallel_state"])
                self.assertFalse(state["terminal"])
                self.assertEqual(len(numbers), state["reference_pass_count"])
                self.assertEqual(["RR-EARLY", "RR-LATE"], state["pending_result_review_ids"])
                fixtures.ParallelResultRuntimeTests().resolve_source_reviews(root)
                continued = self.runtime(root)
                self.assertEqual("RETURN_TO_EXECUTION", continued["state"])
                self.assertFalse(continued["terminal"])
                self.assertEqual(sorted(synthesis["reference_pass_ids"]), continued["reference_pass_ids"])

    def test_formal_terminal_requires_actual_review_authority_not_reference_count(self):
        for numbers in ((), (7,), (3, 1, 2)):
            with self.subTest(numbers=numbers), tempfile.TemporaryDirectory() as td:
                root = Path(td)
                synthesis = self.prepare(root, numbers, reviewed=True)
                synthesis.update(task_terminal=True, terminal_control_disposition="ACCEPTED", disposition="KEEP_PARALLEL")
                self.save(root, synthesis)
                state = self.runtime(root)
                self.assertTrue(state["terminal"])
                self.assertEqual("TERMINAL", state["state"])
                self.assertEqual({"RR-EARLY", "RR-LATE"}, set(state["result_operational_review_authority"]))
                self.assertEqual(len(numbers), state["reference_pass_count"])
                self.add_cohort(root)
                with mock.patch.object(results._driver_followup, "state_for_review", return_value={
                    "required": False, "ready": True, "state": "LEGACY_PRE_CUTOVER", "packet": None,
                }):
                    cohort = cohorts.cohort_state("RS-T", "EC-1", root)
                self.assertTrue(cohort["terminal"])
                self.assertEqual("PARALLEL_SYNTHESIS_TERMINAL", cohort["state"])
                self.assertEqual(len(numbers), cohort["reference_pass_count"])

    def test_task_terminal_self_report_cannot_close_result_or_cohort(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            synthesis = self.prepare(root)
            synthesis.update(task_terminal=True, terminal_control_disposition="ACCEPTED")
            # Deliberate invalid-input fixture bypasses transaction validation.
            fixtures.write_json(root / "research_parallel_syntheses" / "RS-T" / "PS-1.json", synthesis)
            self.assertTrue(any("requires at least one review" in error for error in parallel.audit(root)))
            self.assertFalse(self.runtime(root)["terminal"])
            self.add_cohort(root)
            cohort = cohorts.cohort_state("RS-T", "EC-1", root)
            self.assertFalse(cohort["terminal"])
            self.assertEqual("AWAITING_RESULT_REVIEW_AUTHORITY", cohort["state"])

    def test_cohort_keeps_existing_followup_and_control_disposition_gates(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            synthesis = self.prepare(root, reviewed=True)
            synthesis["task_terminal"] = True
            path = self.save(root, synthesis)
            self.add_cohort(root)
            self.assertEqual("TERMINAL_SYNTHESIS_MISSING_CONTROL_DISPOSITION",
                             cohorts.cohort_state("RS-T", "EC-1", root)["state"])
            synthesis["terminal_control_disposition"] = "ACCEPTED"
            fixtures.write_json(path, synthesis)
            with mock.patch.object(results._driver_followup, "state_for_review", return_value={
                "required": True, "ready": False, "state": "AWAITING_DRIVER_FOLLOWUP", "packet": None,
            }):
                state = cohorts.cohort_state("RS-T", "EC-1", root)
            self.assertFalse(state["terminal"])
            self.assertEqual("AWAITING_RESULT_REVIEW_FOLLOWUP", state["state"])

    def test_reference_labels_do_not_force_method_order(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            synthesis = self.prepare(root, (2, 1, 9))
            for number, kind in ((2, "SEMANTIC_EVIDENCE_CROSSCHECK"),
                                 (1, "ADVERSARIAL_CONTROL_CROSSCHECK"), (9, "COUNTEREXAMPLE_CHECK")):
                path = root / "research_parallel_reference_passes" / "PI-1" / f"RP{number}-1.json"
                value = json.loads(path.read_text())
                value["pass_kind"] = kind
                fixtures.write_json(path, value)
            self.save(root, synthesis)
            self.assertEqual([], parallel.audit(root))

    def test_omitted_third_reference_unknown_reference_and_false_status_rollback(self):
        for defect in ("omit_third", "unknown", "duplicate", "false_status", "wrong_hash"):
            with self.subTest(defect=defect), tempfile.TemporaryDirectory() as td:
                root = Path(td)
                synthesis = self.prepare(root, (1, 2, 3))
                originals = {path: path.read_bytes() for path in root.rglob("*.json")}
                if defect == "omit_third": synthesis["reference_pass_ids"].pop()
                elif defect == "unknown": synthesis["reference_pass_ids"][-1] = "RP-MISSING"
                elif defect == "duplicate": synthesis["reference_pass_ids"][-1] = synthesis["reference_pass_ids"][0]
                elif defect == "false_status": synthesis["reference_review_status"] = "NOT_PERFORMED"
                else: synthesis["evidence_set_sha256"] = "sha256:" + "0" * 64
                with self.assertRaises((parallel.ParallelEvidenceError, transaction.ImmutableWriteTransactionError)):
                    self.save(root, synthesis)
                self.assertFalse((root / "research_parallel_syntheses" / "RS-T" / "PS-1.json").exists())
                self.assertTrue(all(path.read_bytes() == content for path, content in originals.items()))

    def test_zero_references_must_explicitly_disclose_not_performed(self):
        for status in (None, "RECORDED"):
            with self.subTest(status=status), tempfile.TemporaryDirectory() as td:
                root = Path(td)
                synthesis = self.prepare(root)
                if status is None: synthesis.pop("reference_review_status")
                else: synthesis["reference_review_status"] = status
                with self.assertRaisesRegex(parallel.ParallelEvidenceError, "NOT_PERFORMED"):
                    self.save(root, synthesis)

    def test_invalid_and_duplicate_positive_labels_are_rejected(self):
        for label in (0, -1, True, "3", 1):
            with self.subTest(label=label), tempfile.TemporaryDirectory() as td:
                root = Path(td)
                synthesis = self.prepare(root, (1, 3))
                path = root / "research_parallel_reference_passes" / "PI-1" / "RP3-1.json"
                value = json.loads(path.read_text())
                value["pass_number"] = label
                fixtures.write_json(path, value)
                with self.assertRaises(parallel.ParallelEvidenceError):
                    self.save(root, synthesis)

    def test_complete_resolution_projection_and_cli_preserve_third_reference(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            synthesis = self.prepare(root, (3, 1, 2))
            self.save(root, synthesis)
            fixtures.write_json(root / "research_task_publication_resolutions.json", {"resolutions": [{
                "task_id": "RS-T", "parallel_intake_id": "PI-1", "parallel_synthesis_id": "PS-1",
                "retained_parallel_publication_ids": ["TP2-P1"],
                "reference_process": {"reference_pass_ids": synthesis["reference_pass_ids"],
                                      "reference_review_status": "RECORDED"},
            }]})
            self.assertEqual([], parallel.audit(root))
            # Running the actual CLI beside this isolated fixture makes its
            # normal ROOT calculation read these files, with no reader mocks.
            script = root / "research_parallel_evidence.py"
            script.write_bytes(Path(parallel.__file__).read_bytes())
            audited = subprocess.run([sys.executable, str(script), "audit"], capture_output=True, text=True)
            self.assertEqual(0, audited.returncode, audited.stdout + audited.stderr)
            output = subprocess.run([sys.executable, str(script), "state", "--task-id", "RS-T",
                                     "--publication-id", "TP2-P1"], capture_output=True, text=True, check=True)
            state = json.loads(output.stdout)
            self.assertEqual(3, state["reference_pass_count"])
            self.assertEqual(sorted(synthesis["reference_pass_ids"]), state["reference_pass_ids"])

    def test_late_references_preserve_history_and_require_current_synthesis(self):
        for initial, later in (((), (3,)), ((1,), (3, 2))):
            with self.subTest(initial=initial, later=later), tempfile.TemporaryDirectory() as td:
                root = Path(td)
                synthesis = self.prepare(root, initial, reviewed=True)
                old_path = self.save(root, synthesis)
                old_bytes = old_path.read_bytes()
                added = fixtures.ParallelResultRuntimeTests().passes(root, synthesis["evidence_set_sha256"], later)
                self.assertEqual([], parallel.audit(root))
                pending = self.runtime(root)
                self.assertEqual("AWAITING_SYNTHESIS", pending["parallel_state"])
                self.assertEqual(["PS-1"], pending["stale_synthesis_ids"])
                self.assertFalse(pending["terminal"])
                next_synthesis = {**synthesis, "synthesis_id": "PS-2",
                                  "reference_pass_ids": synthesis["reference_pass_ids"] + added,
                                  "reference_review_status": "RECORDED"}
                self.save(root, next_synthesis)
                continued = self.runtime(root)
                self.assertEqual("RETURN_TO_EXECUTION", continued["state"])
                self.assertEqual("PS-2", continued["result"]["result_id"])
                self.assertEqual(len(initial) + len(later), continued["reference_pass_count"])
                self.assertEqual(old_bytes, old_path.read_bytes())
                self.assertEqual([], parallel.audit(root))

    def test_public_writer_rechecks_reference_set_and_rolls_back_its_own_file(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            synthesis = self.prepare(root, (1, 2))
            originals = {path: path.read_bytes() for path in root.rglob("*.json")}
            exclusive_write = transaction._write_exclusive

            def append_during_write(row):
                exclusive_write(row)
                fixtures.ParallelResultRuntimeTests().passes(root, synthesis["evidence_set_sha256"], (3,))

            with mock.patch.object(transaction, "_write_exclusive", side_effect=append_during_write):
                with self.assertRaisesRegex(parallel.ParallelEvidenceError, "complete recorded reference set"):
                    self.save(root, synthesis)
            self.assertFalse((root / "research_parallel_syntheses" / "RS-T" / "PS-1.json").exists())
            self.assertTrue(all(path.read_bytes() == content for path, content in originals.items()))
            self.assertTrue((root / "research_parallel_reference_passes" / "PI-1" / "RP3-1.json").exists())

    def test_public_cli_writes_zero_and_three_reference_syntheses(self):
        for numbers in ((), (3, 1, 2)):
            with self.subTest(numbers=numbers), tempfile.TemporaryDirectory() as td:
                root = Path(td)
                synthesis = self.prepare(root, numbers)
                script = root / "research_parallel_evidence.py"
                script.write_bytes(Path(parallel.__file__).read_bytes())
                record = root / "candidate.json"
                record.write_text(json.dumps(synthesis))
                env = {**os.environ, "PYTHONPATH": str(Path(parallel.__file__).parent)}
                output = subprocess.run([sys.executable, str(script), "write-synthesis", "--record-file", str(record)],
                                        capture_output=True, text=True, env=env)
                self.assertEqual(0, output.returncode, output.stdout + output.stderr)
                saved = json.loads(output.stdout)
                self.assertTrue(saved["saved"])
                self.assertEqual(synthesis, json.loads((root / saved["path"]).read_text()))
                self.assertEqual([], parallel.audit(root))


if __name__ == "__main__":
    unittest.main()
