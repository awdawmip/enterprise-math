import unittest
from datetime import datetime, timezone

from tools import research_runtime_reducer as rr


def task(task_id="RS-T1", state="READY", priority="P1", leverage="HIGH"):
    return {
        "task_id": task_id,
        "base_state": state,
        "priority": priority,
        "leverage": leverage,
        "kind": "RESEARCH",
        "last_progress_at": "2026-09-01T00:00:00+00:00",
        "next_action": "continue",
    }


def event(kind, at, claim_id="c1", **extra):
    value = {
        "schema": rr.EVENT_SCHEMA,
        "event": kind,
        "task_id": "RS-T1",
        "claim_id": claim_id,
        "at": at,
    }
    value.update(extra)
    return value


class RuntimeReducerTests(unittest.TestCase):
    def now(self, value):
        return rr.parse_time(value)

    def test_policy_is_current_only(self):
        policy = rr.load_policy()
        self.assertEqual([], rr.validate_policy(policy))
        self.assertIsNone(policy["legacy_task_definition_source"])
        self.assertFalse(policy["legacy_runtime_on_main"])

    def test_second_claim_cannot_preempt_live_owner(self):
        state = rr.reduce_task(
            task(),
            [event("CLAIM", "2026-09-01T00:00:00+00:00"), event("CLAIM", "2026-09-01T00:01:00+00:00", claim_id="c2")],
            default_lease_minutes=30,
            now=self.now("2026-09-01T00:05:00+00:00"),
        )
        self.assertEqual("c1", state["claim_id"])
        self.assertEqual(1, len(state["ignored_events"]))

    def test_expired_claim_returns_to_handoff(self):
        state = rr.reduce_task(
            task(),
            [event("CLAIM", "2026-09-01T00:00:00+00:00", lease_minutes=30)],
            default_lease_minutes=30,
            now=self.now("2026-09-01T00:31:00+00:00"),
        )
        self.assertEqual("HANDOFF_READY", state["state"])
        self.assertEqual("NEEDS_DISPATCH", state["dispatch_state"])

    def test_handoff_releases_identity(self):
        rid = rr.researcher_id_for_claim(task(), "c1")
        state = rr.reduce_task(
            task(),
            [
                event("CLAIM", "2026-09-01T00:00:00+00:00"),
                event("HANDOFF", "2026-09-01T00:10:00+00:00", researcher_id=rid, next_action="resume exact frontier"),
            ],
            default_lease_minutes=30,
            now=self.now("2026-09-01T00:11:00+00:00"),
        )
        self.assertEqual("HANDOFF_READY", state["state"])
        self.assertIsNone(state["claim_id"])
        self.assertEqual(rid, state["last_researcher_id"])

    def test_selection_is_deterministic(self):
        policy = rr.load_policy()
        states = [
            {**task("RS-R", state="READY", priority="P0"), "state": "READY", "dispatch_state": "NEEDS_DISPATCH"},
            {**task("RS-H", state="HANDOFF_READY", priority="P2", leverage="LOW"), "state": "HANDOFF_READY", "dispatch_state": "NEEDS_DISPATCH"},
        ]
        self.assertEqual("RS-H", rr.select_state(states, policy)["task_id"])


if __name__ == "__main__":
    unittest.main()
