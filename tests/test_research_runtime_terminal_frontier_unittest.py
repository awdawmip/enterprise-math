import unittest

from tools import research_runtime as rt


def state():
    return {
        "parent_objective": {"objective_id": "OBJ", "status": "OPEN"},
        "task_registration": {"registry_key": "RS-X", "state": "CLAIMABLE"},
        "task": {
            "task_id": "RS-X",
            "status": "ACTIVE",
            "taskbook_source": "source",
            "owner_branch": "research/x",
        },
        "owner_claim": {
            "claim_id": "claim-x",
            "researcher_id": "EM-X-ABC123",
            "owner_lease_until": "2026-08-26T12:00:00+08:00",
        },
        "session": {
            "session_id": "session-x",
            "last_activity_at": "2026-08-25T12:00:00+08:00",
        },
        "durable_frontier": {
            "remote_head": "head",
            "execution_stamp": "stamp",
            "durable_outputs": ["checkpoint.md"],
        },
        "current_unfinished_unit": "old local unit",
        "next_action": {"description": "old local action", "executable": True},
        "terminal_scope": None,
        "final_allowed": False,
        "control": {},
    }


class TerminalFrontierClearingTests(unittest.TestCase):
    def assert_recompute_parent_without_old_local_frontier(self, out):
        self.assertEqual(out["runtime_phase"], "REEVALUATE_PARENT")
        self.assertIsNone(out["current_unfinished_unit"])
        self.assertIsNone(out["next_action"])
        self.assertFalse(out["final_allowed"])
        decision = rt.pre_final_gate(out)
        self.assertEqual(decision["transition"], "RECOMPUTE_PARENT_STATE")
        self.assertFalse(decision["canonical_final_allowed"])

    def test_subflow_complete_clears_local_frontier_before_parent_recompute(self):
        out = rt.apply_terminal_event(state(), "SUBFLOW_COMPLETE")
        self.assertEqual(out["terminal_scope"], "SUBFLOW")
        self.assert_recompute_parent_without_old_local_frontier(out)

    def test_task_frozen_clears_local_frontier_before_parent_recompute(self):
        out = rt.apply_terminal_event(state(), "TASK_FROZEN")
        self.assertEqual(out["terminal_scope"], "TASK")
        self.assertEqual(out["task"]["status"], "FROZEN")
        self.assert_recompute_parent_without_old_local_frontier(out)


if __name__ == "__main__":
    unittest.main()
