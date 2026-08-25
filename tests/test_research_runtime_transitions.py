import unittest

from tools import research_runtime as rr
from tools import research_scheduler as rs


def task():
    return {
        "task_id": "RS-RUNTIME-E2E",
        "title": "runtime e2e",
        "kind": "RESEARCH",
        "owner": "owner/a",
        "base_state": "READY",
        "priority": "P1",
        "leverage": "HIGH",
        "frontier": "frontier",
        "next_action": "initial action",
        "dependencies": [],
        "source_refs": [],
        "last_progress_ref": "seed",
        "last_progress_at": "2026-08-25T11:00:00+08:00",
        "hard_block": None,
    }


def event(kind, at, *, actor="chat-A", claim_id="claim-1", **extra):
    value = {
        "schema": "ENTERPRISE_MATH_SCHEDULER_EVENT_V1",
        "event": kind,
        "task_id": "RS-RUNTIME-E2E",
        "actor": actor,
        "at": at,
        "claim_id": claim_id,
    }
    value.update(extra)
    return value


def reduce(events, now):
    return rs.reduce_task(
        task(),
        events,
        default_lease_minutes=120,
        session_liveness_minutes=10,
        now=rs.parse_time(now),
    )


class RuntimeTransitionTests(unittest.TestCase):
    def test_task_done_returns_to_parent_instead_of_final(self):
        state = reduce(
            [
                event("CLAIM", "2026-08-25T12:00:00+08:00"),
                event(
                    "PROGRESS",
                    "2026-08-25T12:05:00+08:00",
                    progress_ref="commit:task-result",
                    next_action="freeze task return",
                ),
                event("DONE", "2026-08-25T12:06:00+08:00", progress_ref="commit:task-return"),
            ],
            "2026-08-25T12:07:00+08:00",
        )
        self.assertEqual("COMPLETE", state["dispatch_state"])

        runtime = rr.build_runtime_snapshot(
            parent_objective="finish the research-control repair program",
            parent_objective_complete=False,
            current_subflow="repair scheduler lease model",
            scheduler_state=state,
            terminal_scope="TASK",
        )
        self.assertFalse(runtime["final_gate"]["final_allowed"])
        self.assertEqual(
            "REEVALUATE_PARENT_OBJECTIVE",
            runtime["final_gate"]["required_transition"],
        )
        self.assertEqual("TASK", runtime["terminal_scope"])

    def test_parent_reevaluation_with_successor_action_must_continue_same_turn(self):
        state = reduce(
            [
                event("CLAIM", "2026-08-25T12:00:00+08:00"),
                event("DONE", "2026-08-25T12:05:00+08:00", progress_ref="commit:done"),
            ],
            "2026-08-25T12:06:00+08:00",
        )
        runtime = rr.build_runtime_snapshot(
            parent_objective="repair all liveness defects",
            parent_objective_complete=False,
            scheduler_state=state,
            terminal_scope="NONE",
            next_executable_action="start terminal-scope repair",
        )
        self.assertFalse(runtime["final_gate"]["final_allowed"])
        self.assertEqual(
            "EXECUTE_NEXT_ACTION_IN_SAME_TURN",
            runtime["final_gate"]["required_transition"],
        )

    def test_stale_session_adoption_preserves_owner_and_resumes_unfinished_unit(self):
        claimed = event("CLAIM", "2026-08-25T12:00:00+08:00")
        stale = reduce([claimed], "2026-08-25T12:11:00+08:00")
        researcher_id = stale["researcher_id"]
        self.assertEqual("STALE_RECOVERABLE", stale["dispatch_state"])

        adopted = reduce(
            [
                claimed,
                event(
                    "SESSION_ADOPT",
                    "2026-08-25T12:12:00+08:00",
                    actor="chat-B",
                    recovery_ref="commit:verified-frontier",
                    unfinished_unit="unit-4",
                    next_action="execute unit-4",
                ),
            ],
            "2026-08-25T12:13:00+08:00",
        )
        self.assertEqual("claim-1", adopted["claim_id"])
        self.assertEqual(researcher_id, adopted["researcher_id"])

        runtime = rr.build_runtime_snapshot(
            parent_objective="complete exact repository task",
            parent_objective_complete=False,
            scheduler_state=adopted,
        )
        self.assertEqual("claim-1", runtime["owner_claim"]["claim_id"])
        self.assertEqual("LIVE", runtime["session"]["state"])
        self.assertEqual("commit:verified-frontier", runtime["durable_frontier"]["recovery_ref"])
        self.assertEqual("unit-4", runtime["current_unfinished_unit"])
        self.assertEqual("execute unit-4", runtime["next_executable_action"])
        self.assertFalse(runtime["final_gate"]["final_allowed"])
        self.assertEqual(
            "EXECUTE_NEXT_ACTION_IN_SAME_TURN",
            runtime["final_gate"]["required_transition"],
        )

    def test_parent_terminal_is_the_only_normal_completion_final(self):
        runtime = rr.build_runtime_snapshot(
            parent_objective="repair all liveness defects",
            parent_objective_complete=True,
            terminal_scope="PARENT_OBJECTIVE",
        )
        self.assertTrue(runtime["final_gate"]["final_allowed"])
        self.assertEqual(
            "EMIT_PARENT_TERMINAL_FINAL",
            runtime["final_gate"]["required_transition"],
        )


if __name__ == "__main__":
    unittest.main()
