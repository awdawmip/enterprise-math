import unittest

from enterprise_math import research_runtime as rr


class PreFinalGateTests(unittest.TestCase):
    def test_open_parent_with_next_action_cannot_finalize(self):
        verdict = rr.pre_final_gate(
            parent_objective_complete=False,
            next_executable_action="run successor-gate evaluation",
        )
        self.assertFalse(verdict["final_allowed"])
        self.assertEqual("EXECUTE_NEXT_ACTION_IN_SAME_TURN", verdict["required_transition"])

    def test_open_parent_without_next_action_still_fails_closed(self):
        verdict = rr.pre_final_gate(parent_objective_complete=False)
        self.assertFalse(verdict["final_allowed"])
        self.assertEqual("RESOLVE_NEXT_ACTION_OR_TERMINAL_BLOCK", verdict["required_transition"])

    def test_subflow_terminal_requires_parent_reevaluation(self):
        verdict = rr.pre_final_gate(
            parent_objective_complete=False,
            terminal_scope="SUBFLOW",
            next_executable_action="inspect parent portfolio",
        )
        self.assertFalse(verdict["final_allowed"])
        self.assertEqual("REEVALUATE_PARENT_OBJECTIVE", verdict["required_transition"])
        self.assertEqual("SUBFLOW", verdict["terminal_scope"])

    def test_task_terminal_requires_parent_reevaluation(self):
        verdict = rr.pre_final_gate(
            parent_objective_complete=False,
            terminal_scope="TASK",
        )
        self.assertFalse(verdict["final_allowed"])
        self.assertEqual("REEVALUATE_PARENT_OBJECTIVE", verdict["required_transition"])
        self.assertEqual("TASK_TERMINAL_IS_LOCAL_NOT_PARENT_TERMINAL", verdict["reason"])

    def test_parent_completion_allows_terminal_final(self):
        verdict = rr.pre_final_gate(
            parent_objective_complete=True,
            terminal_scope="PARENT_OBJECTIVE",
        )
        self.assertTrue(verdict["final_allowed"])
        self.assertEqual("PARENT_USER_OBJECTIVE_COMPLETE", verdict["reason"])
        self.assertEqual("PARENT_OBJECTIVE", verdict["terminal_scope"])

    def test_parent_scope_cannot_be_declared_while_parent_is_open(self):
        with self.assertRaises(rr.RuntimeStateError):
            rr.pre_final_gate(
                parent_objective_complete=False,
                terminal_scope="PARENT_OBJECTIVE",
            )

    def test_explicit_user_stop_allows_final_without_claiming_parent_complete(self):
        verdict = rr.pre_final_gate(
            parent_objective_complete=False,
            next_executable_action="resume audit",
            user_requested_stop=True,
        )
        self.assertTrue(verdict["final_allowed"])
        self.assertTrue(verdict["recovery_record_required"])

    def test_genuine_terminal_block_allows_recovery_final(self):
        verdict = rr.pre_final_gate(
            parent_objective_complete=False,
            terminal_block_reason="MISSING_USER_DATA",
        )
        self.assertTrue(verdict["final_allowed"])
        self.assertEqual("EMIT_BLOCKED_FINAL_WITH_RECOVERY_RECORD", verdict["required_transition"])
        self.assertTrue(verdict["recovery_record_required"])

    def test_unknown_block_reason_is_rejected(self):
        with self.assertRaises(rr.RuntimeStateError):
            rr.pre_final_gate(
                parent_objective_complete=False,
                terminal_block_reason="JUST_FEELS_DONE",
            )

    def test_unknown_terminal_scope_is_rejected(self):
        with self.assertRaises(rr.RuntimeStateError):
            rr.pre_final_gate(
                parent_objective_complete=False,
                terminal_scope="SOMETHING_ELSE",
            )


if __name__ == "__main__":
    unittest.main()
