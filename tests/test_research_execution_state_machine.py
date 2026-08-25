import json
from pathlib import Path
import tempfile
import unittest

import tools.research_execution_state as ex


ROOT = Path(__file__).resolve().parents[1]


class ResearchExecutionStateMachineTests(unittest.TestCase):
    def setUp(self):
        self.machine = ex.load_machine(ROOT)

    def test_canonical_machine_is_structurally_valid(self):
        self.assertEqual(ex.validate_machine(self.machine), [])

    def test_pre_math_pending_blocks_both_math_action_classes(self):
        self.assertFalse(ex.allowed_action(self.machine, "PRE_MATH_GATES_PENDING", "MATHEMATICAL_SOURCE_READ"))
        self.assertFalse(ex.allowed_action(self.machine, "PRE_MATH_GATES_PENDING", "MATHEMATICAL_DERIVATION"))

    def test_execution_ready_allows_math(self):
        self.assertTrue(ex.allowed_action(self.machine, "EXECUTION_READY", "MATHEMATICAL_SOURCE_READ"))
        self.assertTrue(ex.allowed_action(self.machine, "EXECUTION_READY", "MATHEMATICAL_DERIVATION"))

    def test_premath_gate_cannot_be_skipped(self):
        with self.assertRaises(ValueError):
            ex.next_state(
                self.machine,
                "PRE_MATH_GATES_PENDING",
                "SUBSTANTIVE_WORK_STARTED",
                {"action_within_taskbook_whitelist": True},
            )

    def test_premath_gate_requires_durable_evidence(self):
        with self.assertRaisesRegex(ValueError, "missing transition evidence"):
            ex.next_state(
                self.machine,
                "PRE_MATH_GATES_PENDING",
                "PRE_MATH_GATES_SATISFIED",
                {},
            )
        target = ex.next_state(
            self.machine,
            "PRE_MATH_GATES_PENDING",
            "PRE_MATH_GATES_SATISFIED",
            {
                "durable_evidence_refs_for_all_pre_math_gates": ["commit:abc123"],
                "remote_verification_if_required_by_gate": "verified",
            },
        )
        self.assertEqual(target, "EXECUTION_READY")

    def test_failed_premath_gate_is_nonstart_not_math_rejection(self):
        target = ex.next_state(
            self.machine,
            "PRE_MATH_GATES_PENDING",
            "PRE_MATH_GATE_FAILED",
            {"failed_gate_id": "STAMP", "failure_evidence_or_reason": "remote stamp absent"},
        )
        self.assertEqual(target, "NONSTART_TERMINAL")

    def test_liveness_failure_requires_durable_reconciliation_before_resume(self):
        target = ex.next_state(
            self.machine,
            "IN_PROGRESS",
            "LIVENESS_OR_CONTINUITY_FAILURE_DETECTED",
            {"reason": "conversation stalled"},
        )
        self.assertEqual(target, "RECOVERY_REQUIRED")
        with self.assertRaisesRegex(ValueError, "durable_frontier_ref"):
            ex.next_state(
                self.machine,
                "RECOVERY_REQUIRED",
                "DURABLE_FRONTIER_RECONCILED",
                {"resume_state": "IN_PROGRESS"},
            )
        resumed = ex.next_state(
            self.machine,
            "RECOVERY_REQUIRED",
            "DURABLE_FRONTIER_RECONCILED",
            {"resume_state": "IN_PROGRESS", "durable_frontier_ref": "commit:def456"},
        )
        self.assertEqual(resumed, "IN_PROGRESS")

    def test_execution_gate_schema_requires_explicit_policy_and_gate_list(self):
        findings = ex.audit_taskbook_execution({}, self.machine)
        codes = {item["code"] for item in findings}
        self.assertIn("EX-STATE-POLICY", codes)
        self.assertIn("EX-GATES", codes)

    def test_valid_premath_gate_schema_passes(self):
        meta = {
            "execution_state_policy": "INHERIT_GLOBAL",
            "execution_gates": [
                {
                    "gate_id": "STAMP",
                    "phase": "PRE_MATH",
                    "must_precede": ["MATHEMATICAL_SOURCE_READ", "MATHEMATICAL_DERIVATION"],
                    "evidence": {"kind": "REMOTE_COMMIT_CONTAINS_FILE"},
                }
            ],
        }
        self.assertEqual(ex.audit_taskbook_execution(meta, self.machine), [])

    def test_premath_gate_must_cover_source_read_and_derivation(self):
        meta = {
            "execution_state_policy": "INHERIT_GLOBAL",
            "execution_gates": [
                {
                    "gate_id": "STAMP",
                    "phase": "PRE_MATH",
                    "must_precede": ["MATHEMATICAL_DERIVATION"],
                    "evidence": {"kind": "REMOTE_COMMIT_CONTAINS_FILE"},
                }
            ],
        }
        codes = {item["code"] for item in ex.audit_taskbook_execution(meta, self.machine)}
        self.assertIn("EX-PREMATH-COVERAGE", codes)

    def test_f5ar_taskbook_declares_machine_readable_premath_gate(self):
        path = ROOT / "research_tasks" / "COHERENT_BRC_F5AR_INDEPENDENT_BRANCH_ONTOLOGY_AXIOM_ADMISSION_REPLICATION_20260825.md"
        self.assertEqual(ex.audit_taskbook_path(path, root=ROOT), [])
        meta, _ = ex.split_taskbook(path.read_text(encoding="utf-8"))
        gates = {gate["gate_id"]: gate for gate in meta["execution_gates"]}
        gate = gates["F5AR-PUBLICATION-LIVENESS-PREMATH"]
        self.assertEqual(gate["phase"], "PRE_MATH")
        self.assertEqual(gate["evidence"]["path"], "evidence/cbrc_f5ar_execution_stamp.json")
        self.assertEqual(gate["evidence"]["required_fields"]["phase"], "STARTED_BEFORE_MATH")
        self.assertIsNone(gate["evidence"]["required_fields"]["admission_verdict"])


if __name__ == "__main__":
    unittest.main()
