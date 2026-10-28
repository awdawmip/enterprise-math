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

    def test_superseded_blocked_task_exposes_its_retirement_evidence(self):
        old_block = {
            "missing_object": "an immutable review result",
            "owner": "line Driver",
            "necessity": "review the returned evidence",
            "unblock_condition": "the exact review is published",
        }
        source_task = {
            **task("GV-OLD-REVIEW", state="BLOCKED"),
            "kind": "GOVERNANCE",
            "hard_block": old_block,
            "last_progress_ref": "old-review-input.md",
        }
        retirement = event(
            "SUPERSEDE",
            "2026-09-01T00:10:00+00:00",
            claim_id=None,
            task_id="GV-OLD-REVIEW",
            progress_ref="completed-review-retirement.md",
            next_action="Continue the open portfolio",
        )
        state = rr.reduce_task(
            source_task,
            [retirement],
            default_lease_minutes=30,
            now=self.now("2026-09-01T00:11:00+00:00"),
        )
        self.assertEqual("SUPERSEDED", state["state"])
        self.assertEqual("COMPLETE", state["dispatch_state"])
        self.assertIsNone(state["hard_block"])
        self.assertIsNone(state["claim_id"])
        self.assertIsNone(state["lease_until"])
        self.assertEqual("completed-review-retirement.md", state["last_progress_ref"])
        self.assertEqual(retirement["at"], state["last_progress_at"])
        self.assertEqual("Continue the open portfolio", state["next_action"])
        # The current projection changes; the frozen task and event remain intact.
        self.assertEqual(old_block, source_task["hard_block"])
        self.assertEqual("old-review-input.md", source_task["last_progress_ref"])
        self.assertEqual("completed-review-retirement.md", retirement["progress_ref"])

    def test_supersede_without_new_reference_preserves_previous_evidence(self):
        state = rr.reduce_task(
            {**task(), "last_progress_ref": "existing-evidence.md"},
            [event("SUPERSEDE", "2026-09-01T00:10:00+00:00", claim_id=None)],
            default_lease_minutes=30,
            now=self.now("2026-09-01T00:11:00+00:00"),
        )
        self.assertEqual("COMPLETE", state["dispatch_state"])
        self.assertEqual("existing-evidence.md", state["last_progress_ref"])
        self.assertEqual("continue", state["next_action"])


if __name__ == "__main__":
    unittest.main()
