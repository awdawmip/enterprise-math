from pathlib import Path
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

    def test_execution_ready_allows_math_by_state(self):
        self.assertTrue(ex.allowed_action(self.machine, "EXECUTION_READY", "MATHEMATICAL_SOURCE_READ"))
        self.assertTrue(ex.allowed_action(self.machine, "EXECUTION_READY", "MATHEMATICAL_DERIVATION"))

    def test_premath_gate_cannot_be_skipped(self):
        with self.assertRaises(ValueError):
            ex.next_state(
                self.machine,
                "PRE_MATH_GATES_PENDING",
                "SUBSTANTIVE_WORK_STARTED",
                {"action_within_task_scope": True},
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

    def test_false_boolean_cannot_fake_transition_pass(self):
        with self.assertRaisesRegex(ValueError, "exact true"):
            ex.next_state(
                self.machine,
                "IN_PROGRESS",
                "RETURN_ARTIFACT_PERSISTED",
                {"durable_return_ref": "commit:abc", "return_write_action_guard_pass": False},
            )

    def test_direct_user_task_can_enter_same_execution_lifecycle_without_taskbook(self):
        spec = {
            "task_id": "DIRECT-1",
            "authority_kind": "DIRECT_USER_TASK",
            "authority_ref": "conversation:turn42",
            "execution_gates": [],
        }
        self.assertEqual(ex.audit_execution_spec(spec, self.machine), [])
        target = ex.next_state(
            self.machine,
            "UNBOUND",
            "DIRECT_USER_TASK_AUTHORITY_ACCEPTED",
            {
                "user_instruction_ref": "conversation:turn42",
                "task_scope_snapshot": "prove the selected claim",
                "normalized_execution_spec": spec,
            },
        )
        self.assertEqual(target, "DISPATCH_READY")

    def test_direct_user_before_math_constraint_must_be_normalized_into_gate(self):
        spec = {
            "task_id": "DIRECT-2",
            "authority_kind": "DIRECT_USER_TASK",
            "authority_ref": "conversation:turn43",
            "execution_gates": [],
        }
        findings = ex.audit_execution_spec(
            spec,
            self.machine,
            authority_body="Before mathematics, write a remote execution stamp.",
        )
        self.assertIn("EX-PREMATH-UNDECLARED", {item["code"] for item in findings})

    def test_scheduler_task_authority_is_distinct_from_execution_ready(self):
        spec = {
            "task_id": "RS-SCHEDULED",
            "authority_kind": "SCHEDULER_TASK",
            "authority_ref": "Issue #240 claim:xyz",
            "execution_gates": [],
        }
        self.assertEqual(ex.audit_execution_spec(spec, self.machine), [])
        target = ex.next_state(
            self.machine,
            "UNBOUND",
            "SCHEDULER_TASK_AUTHORITY_ACCEPTED",
            {
                "scheduler_task_id": "RS-SCHEDULED",
                "scheduler_authority_ref": "Issue #240 claim:xyz",
                "normalized_execution_spec": spec,
            },
        )
        self.assertEqual(target, "DISPATCH_READY")
        self.assertFalse(ex.allowed_action(self.machine, target, "MATHEMATICAL_DERIVATION"))

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

    def test_obvious_prose_premath_gate_cannot_remain_undeclared(self):
        meta = {"execution_state_policy": "INHERIT_GLOBAL", "execution_gates": []}
        findings = ex.audit_taskbook_execution(
            meta,
            self.machine,
            body="Before mathematics, create and verify the execution stamp.",
        )
        self.assertIn("EX-PREMATH-UNDECLARED", {item["code"] for item in findings})

    def test_prereturn_gate_must_cover_return_write(self):
        meta = {
            "execution_state_policy": "INHERIT_GLOBAL",
            "execution_gates": [
                {
                    "gate_id": "FINAL",
                    "phase": "PRE_RETURN",
                    "must_precede": ["CHECKPOINT_WRITE"],
                    "evidence": {"kind": "CHECKER_PASS"},
                }
            ],
        }
        codes = {item["code"] for item in ex.audit_taskbook_execution(meta, self.machine)}
        self.assertIn("EX-PRERETURN-COVERAGE", codes)

    def test_gate_ledger_blocks_action_even_when_state_allows_it(self):
        meta = {
            "execution_state_policy": "INHERIT_GLOBAL",
            "execution_gates": [
                {
                    "gate_id": "FINAL",
                    "phase": "PRE_RETURN",
                    "must_precede": ["RETURN_WRITE"],
                    "evidence": {"kind": "CHECKER_PASS"},
                }
            ],
        }
        allowed, blockers = ex.allowed_task_action(
            meta, self.machine, "IN_PROGRESS", "RETURN_WRITE", set()
        )
        self.assertFalse(allowed)
        self.assertEqual(blockers, ["FINAL"])
        allowed, blockers = ex.allowed_task_action(
            meta, self.machine, "IN_PROGRESS", "RETURN_WRITE", {"FINAL"}
        )
        self.assertTrue(allowed)
        self.assertEqual(blockers, [])

    def test_mid_execution_gate_can_guard_checkpoint_write(self):
        meta = {
            "execution_state_policy": "INHERIT_GLOBAL",
            "execution_gates": [
                {
                    "gate_id": "CHECKER",
                    "phase": "MID_EXECUTION",
                    "must_precede": ["CHECKPOINT_WRITE"],
                    "evidence": {"kind": "CHECKER_PASS"},
                }
            ],
        }
        allowed, blockers = ex.allowed_task_action(
            meta, self.machine, "IN_PROGRESS", "CHECKPOINT_WRITE", set()
        )
        self.assertFalse(allowed)
        self.assertEqual(blockers, ["CHECKER"])

    def test_f5ar_taskbook_declares_machine_readable_premath_and_prereturn_gates(self):
        path = ROOT / "research_tasks" / "COHERENT_BRC_F5AR_INDEPENDENT_BRANCH_ONTOLOGY_AXIOM_ADMISSION_REPLICATION_20260825.md"
        self.assertEqual(ex.audit_taskbook_path(path, root=ROOT), [])
        meta, _ = ex.split_taskbook(path.read_text(encoding="utf-8"))
        gates = {gate["gate_id"]: gate for gate in meta["execution_gates"]}
        gate = gates["F5AR-PUBLICATION-LIVENESS-PREMATH"]
        self.assertEqual(gate["phase"], "PRE_MATH")
        self.assertEqual(gate["evidence"]["path"], "evidence/cbrc_f5ar_execution_stamp.json")
        self.assertEqual(gate["evidence"]["required_fields"]["phase"], "STARTED_BEFORE_MATH")
        self.assertIsNone(gate["evidence"]["required_fields"]["admission_verdict"])
        final_gate = gates["F5AR-FINAL-MATERIALIZATION"]
        self.assertEqual(final_gate["phase"], "PRE_RETURN")
        self.assertIn("RETURN_WRITE", final_gate["must_precede"])


if __name__ == "__main__":
    unittest.main()
