from pathlib import Path
import unittest

import tools.research_execution_state as ex


ROOT = Path(__file__).resolve().parents[1]


class ResearchExecutionStateMachineTests(unittest.TestCase):
    def setUp(self):
        self.machine = ex.load_machine(ROOT)

    def test_canonical_machine_is_structurally_valid(self):
        self.assertEqual(ex.validate_machine(self.machine), [])

    def test_pre_math_pending_blocks_all_math_action_classes(self):
        self.assertFalse(ex.allowed_action(self.machine, "PRE_MATH_GATES_PENDING", "MATHEMATICAL_SOURCE_READ"))
        self.assertFalse(ex.allowed_action(self.machine, "PRE_MATH_GATES_PENDING", "POST_FREEZE_SOURCE_READ"))
        self.assertFalse(ex.allowed_action(self.machine, "PRE_MATH_GATES_PENDING", "MATHEMATICAL_DERIVATION"))

    def test_execution_ready_allows_math_by_state(self):
        self.assertTrue(ex.allowed_action(self.machine, "EXECUTION_READY", "MATHEMATICAL_SOURCE_READ"))
        self.assertTrue(ex.allowed_action(self.machine, "EXECUTION_READY", "POST_FREEZE_SOURCE_READ"))
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
            ex.next_state(self.machine, "PRE_MATH_GATES_PENDING", "PRE_MATH_GATES_SATISFIED", {})
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
                "authority_body": "prove the selected claim",
            },
        )
        self.assertEqual(target, "DISPATCH_READY")

    def test_authority_event_must_match_normalized_authority_kind(self):
        spec = {
            "task_id": "BAD-AUTH",
            "authority_kind": "SCHEDULER_TASK",
            "authority_ref": "claim:1",
            "execution_gates": [],
        }
        with self.assertRaisesRegex(ValueError, "requires normalized authority_kind=DIRECT_USER_TASK"):
            ex.next_state(
                self.machine,
                "UNBOUND",
                "DIRECT_USER_TASK_AUTHORITY_ACCEPTED",
                {
                    "user_instruction_ref": "conversation:turn42",
                    "task_scope_snapshot": "do the task",
                    "normalized_execution_spec": spec,
                    "authority_body": "do the task",
                },
            )

    def test_authority_transition_rejects_undeclared_premath_constraint(self):
        spec = {
            "task_id": "DIRECT-2",
            "authority_kind": "DIRECT_USER_TASK",
            "authority_ref": "conversation:turn43",
            "execution_gates": [],
        }
        with self.assertRaisesRegex(ValueError, "EX-PREMATH-UNDECLARED"):
            ex.next_state(
                self.machine,
                "UNBOUND",
                "DIRECT_USER_TASK_AUTHORITY_ACCEPTED",
                {
                    "user_instruction_ref": "conversation:turn43",
                    "task_scope_snapshot": "Before mathematics, write a remote execution stamp.",
                    "normalized_execution_spec": spec,
                    "authority_body": "Before mathematics, write a remote execution stamp.",
                },
            )

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
                "authority_body": "scheduled task",
            },
        )
        self.assertEqual(target, "DISPATCH_READY")
        self.assertFalse(ex.allowed_action(self.machine, target, "MATHEMATICAL_DERIVATION"))

    def test_direct_user_return_can_terminate_without_fake_driver_acceptance(self):
        target = ex.next_state(
            self.machine,
            "RETURNED",
            "RETURN_DELIVERED_WITHOUT_DRIVER_REVIEW",
            {
                "authority_kind": "DIRECT_USER_TASK",
                "delivery_ref": "conversation:final",
                "execution_gate_ledger_complete": True,
            },
        )
        self.assertEqual(target, "DELIVERED_UNREVIEWED")
        with self.assertRaisesRegex(ValueError, "allowed only"):
            ex.next_state(
                self.machine,
                "RETURNED",
                "RETURN_DELIVERED_WITHOUT_DRIVER_REVIEW",
                {
                    "authority_kind": "SCHEDULER_TASK",
                    "delivery_ref": "scheduler:return",
                    "execution_gate_ledger_complete": True,
                },
            )

    def test_handoff_same_conversation_resume_requires_gate_ledger_reconciliation(self):
        with self.assertRaisesRegex(ValueError, "exact true"):
            ex.next_state(
                self.machine,
                "HANDOFF_READY",
                "SAME_CONVERSATION_EXECUTION_RESUMED",
                {
                    "durable_handoff_ref": "commit:h1",
                    "resume_authority_ref": "conversation:same",
                    "execution_gate_ledger_reconciled": False,
                },
            )
        target = ex.next_state(
            self.machine,
            "HANDOFF_READY",
            "SAME_CONVERSATION_EXECUTION_RESUMED",
            {
                "durable_handoff_ref": "commit:h1",
                "resume_authority_ref": "conversation:same",
                "execution_gate_ledger_reconciled": True,
            },
        )
        self.assertEqual(target, "IN_PROGRESS")

    def test_liveness_failure_requires_durable_state_and_gate_reconciliation_before_resume(self):
        target = ex.next_state(
            self.machine,
            "IN_PROGRESS",
            "LIVENESS_OR_CONTINUITY_FAILURE_DETECTED",
            {"reason": "conversation stalled"},
        )
        self.assertEqual(target, "RECOVERY_REQUIRED")
        with self.assertRaisesRegex(ValueError, "execution_gate_ledger_reconciled"):
            ex.next_state(
                self.machine,
                "RECOVERY_REQUIRED",
                "DURABLE_FRONTIER_RECONCILED",
                {"resume_state": "IN_PROGRESS", "durable_frontier_ref": "commit:def456"},
            )
        resumed = ex.next_state(
            self.machine,
            "RECOVERY_REQUIRED",
            "DURABLE_FRONTIER_RECONCILED",
            {
                "resume_state": "IN_PROGRESS",
                "durable_frontier_ref": "commit:def456",
                "execution_gate_ledger_reconciled": True,
            },
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

    def test_post_freeze_source_read_inherits_premath_source_guard(self):
        meta = {
            "execution_state_policy": "INHERIT_GLOBAL",
            "execution_gates": [
                {
                    "gate_id": "START",
                    "phase": "PRE_MATH",
                    "must_precede": ["MATHEMATICAL_SOURCE_READ", "MATHEMATICAL_DERIVATION"],
                    "evidence": {"kind": "STAMP"},
                },
                {
                    "gate_id": "PHASE-A-FREEZE",
                    "phase": "MID_EXECUTION",
                    "must_precede": ["POST_FREEZE_SOURCE_READ"],
                    "evidence": {"kind": "FROZEN_RETURN_AND_CHECKER"},
                },
            ],
        }
        allowed, blockers = ex.allowed_task_action(meta, self.machine, "EXECUTION_READY", "POST_FREEZE_SOURCE_READ", set())
        self.assertFalse(allowed)
        self.assertEqual(blockers, ["PHASE-A-FREEZE", "START"])
        allowed, blockers = ex.allowed_task_action(meta, self.machine, "IN_PROGRESS", "MATHEMATICAL_SOURCE_READ", {"START"})
        self.assertTrue(allowed)
        self.assertEqual(blockers, [])
        allowed, blockers = ex.allowed_task_action(meta, self.machine, "IN_PROGRESS", "POST_FREEZE_SOURCE_READ", {"START"})
        self.assertFalse(allowed)
        self.assertEqual(blockers, ["PHASE-A-FREEZE"])
        allowed, blockers = ex.allowed_task_action(meta, self.machine, "IN_PROGRESS", "POST_FREEZE_SOURCE_READ", {"START", "PHASE-A-FREEZE"})
        self.assertTrue(allowed)
        self.assertEqual(blockers, [])

    def test_gate_ledger_blocks_return_even_when_state_allows_it(self):
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
        allowed, blockers = ex.allowed_task_action(meta, self.machine, "IN_PROGRESS", "RETURN_WRITE", set())
        self.assertFalse(allowed)
        self.assertEqual(blockers, ["FINAL"])
        allowed, blockers = ex.allowed_task_action(meta, self.machine, "IN_PROGRESS", "RETURN_WRITE", {"FINAL"})
        self.assertTrue(allowed)
        self.assertEqual(blockers, [])

    def test_mid_execution_gate_can_guard_verdict_freeze(self):
        meta = {
            "execution_state_policy": "INHERIT_GLOBAL",
            "execution_gates": [
                {
                    "gate_id": "CHECKER",
                    "phase": "MID_EXECUTION",
                    "must_precede": ["VERDICT_FREEZE"],
                    "evidence": {"kind": "CHECKER_PASS"},
                }
            ],
        }
        allowed, blockers = ex.allowed_task_action(meta, self.machine, "IN_PROGRESS", "VERDICT_FREEZE", set())
        self.assertFalse(allowed)
        self.assertEqual(blockers, ["CHECKER"])
        allowed, blockers = ex.allowed_task_action(meta, self.machine, "IN_PROGRESS", "VERDICT_FREEZE", {"CHECKER"})
        self.assertTrue(allowed)
        self.assertEqual(blockers, [])

    def test_f5ar_taskbook_declares_all_machine_readable_execution_gates(self):
        path = ROOT / "research_tasks" / "COHERENT_BRC_F5AR_INDEPENDENT_BRANCH_ONTOLOGY_AXIOM_ADMISSION_REPLICATION_20260825.md"
        self.assertEqual(ex.audit_taskbook_path(path, root=ROOT), [])
        meta, _ = ex.split_taskbook(path.read_text(encoding="utf-8"))
        gates = {gate["gate_id"]: gate for gate in meta["execution_gates"]}
        start = gates["F5AR-PUBLICATION-LIVENESS-PREMATH"]
        self.assertEqual(start["phase"], "PRE_MATH")
        self.assertEqual(start["evidence"]["path"], "evidence/cbrc_f5ar_execution_stamp.json")
        self.assertEqual(start["evidence"]["required_fields"]["phase"], "STARTED_BEFORE_MATH")
        self.assertIsNone(start["evidence"]["required_fields"]["admission_verdict"])
        allowed, blockers = ex.allowed_task_action(meta, self.machine, "EXECUTION_READY", "POST_FREEZE_SOURCE_READ", set())
        self.assertFalse(allowed)
        self.assertIn("F5AR-PUBLICATION-LIVENESS-PREMATH", blockers)
        checkpoint_a = gates["F5AR-CHECKPOINT-A-BEFORE-VERDICT"]
        checkpoint_b = gates["F5AR-CHECKPOINT-B-BEFORE-VERDICT"]
        self.assertIn("VERDICT_FREEZE", checkpoint_a["must_precede"])
        self.assertIn("VERDICT_FREEZE", checkpoint_b["must_precede"])
        final_gate = gates["F5AR-FINAL-MATERIALIZATION"]
        self.assertEqual(final_gate["phase"], "PRE_RETURN")
        self.assertIn("RETURN_WRITE", final_gate["must_precede"])
        allowed, blockers = ex.allowed_task_action(
            meta,
            self.machine,
            "IN_PROGRESS",
            "VERDICT_FREEZE",
            {"F5AR-PUBLICATION-LIVENESS-PREMATH"},
        )
        self.assertFalse(allowed)
        self.assertEqual(
            blockers,
            ["F5AR-CHECKPOINT-A-BEFORE-VERDICT", "F5AR-CHECKPOINT-B-BEFORE-VERDICT"],
        )


if __name__ == "__main__":
    unittest.main()
