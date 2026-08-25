import json
import pathlib
import unittest

from tools import research_scheduler as rs

ROOT = pathlib.Path(__file__).resolve().parents[1]


def task():
    return {
        "task_id": "RS-RUNTIME-LIVE",
        "title": "runtime liveness test",
        "kind": "RESEARCH",
        "owner": "owner/a",
        "base_state": "READY",
        "priority": "P1",
        "leverage": "HIGH",
        "frontier": "frontier",
        "next_action": "initial next",
        "dependencies": [],
        "source_refs": [],
        "last_progress_ref": "seed",
        "last_progress_at": "2026-08-25T11:00:00+08:00",
        "hard_block": None,
    }


def event(kind, at, *, claim_id="claim-1", actor="chat-A", **extra):
    value = {
        "schema": "ENTERPRISE_MATH_SCHEDULER_EVENT_V1",
        "event": kind,
        "task_id": "RS-RUNTIME-LIVE",
        "actor": actor,
        "at": at,
    }
    if claim_id is not None:
        value["claim_id"] = claim_id
    value.update(extra)
    return value


class SchedulerSessionLivenessTests(unittest.TestCase):
    def reduce(self, events, now):
        return rs.reduce_task(
            task(),
            events,
            default_lease_minutes=120,
            session_liveness_minutes=10,
            now=rs.parse_time(now),
        )

    def test_canonical_liveness_overlay_admits_recovery_event_and_state(self):
        overlay = json.loads((ROOT / "research_scheduler_liveness.json").read_text(encoding="utf-8"))
        config = overlay["scheduler_config_overlay"]
        self.assertEqual(10, config["session_liveness_minutes"])
        self.assertIn("SESSION_ADOPT", config["additional_event_types"])
        self.assertIn("STALE_RECOVERABLE", config["additional_computed_dispatch_states"])
        self.assertIn("DORMANT", config["additional_computed_dispatch_states"])
        self.assertTrue(overlay["owner_claim_lease"]["renewed_by_live_heartbeat"])

    def test_session_can_go_stale_while_owner_claim_remains_live(self):
        state = self.reduce(
            [event("CLAIM", "2026-08-25T12:00:00+08:00")],
            "2026-08-25T12:11:00+08:00",
        )
        self.assertEqual("STALE", state["session_state"])
        self.assertEqual("STALE_RECOVERABLE", state["dispatch_state"])
        self.assertEqual("claim-1", state["claim_id"])
        self.assertIsNotNone(state["researcher_id"])
        self.assertIsNotNone(state["owner_lease_until"])

    def test_live_heartbeat_renews_owner_even_if_session_later_goes_stale(self):
        state = rs.reduce_task(
            task(),
            [
                event("CLAIM", "2026-08-25T12:00:00+08:00", lease_minutes=30),
                event("HEARTBEAT", "2026-08-25T12:05:00+08:00", lease_minutes=30),
            ],
            default_lease_minutes=30,
            session_liveness_minutes=10,
            now=rs.parse_time("2026-08-25T12:31:00+08:00"),
        )
        self.assertEqual("STALE", state["session_state"])
        self.assertEqual("STALE_RECOVERABLE", state["dispatch_state"])
        self.assertEqual("claim-1", state["claim_id"])
        self.assertTrue(state["owner_lease_until"].startswith("2026-08-25T04:35:00"))

    def test_stale_owner_claim_is_not_newly_dispatchable(self):
        cfg = {
            "schema": "ENTERPRISE_MATH_RESEARCH_SCHEDULER_V1",
            "claim_lease_minutes": 120,
            "session_liveness_minutes": 10,
            "selection_policy": {
                "state_order": ["HANDOFF_READY", "READY"],
                "priority_order": ["P0", "P1", "P2", "P3"],
                "leverage_order": ["HIGH", "MEDIUM", "LOW"],
            },
            "tasks": [task()],
        }
        events = [event("CLAIM", "2026-08-25T12:00:00+08:00")]
        chosen = rs.select_task(cfg, events, rs.parse_time("2026-08-25T12:11:00+08:00"))
        self.assertIsNone(chosen)

    def test_replacement_conversation_adopts_same_claim_and_identity(self):
        claim = event("CLAIM", "2026-08-25T12:00:00+08:00")
        initial = self.reduce([claim], "2026-08-25T12:11:00+08:00")
        researcher_id = initial["researcher_id"]
        adopted = self.reduce(
            [
                claim,
                event(
                    "SESSION_ADOPT",
                    "2026-08-25T12:12:00+08:00",
                    actor="chat-B",
                    recovery_ref="commit:durable-frontier",
                    unfinished_unit="checker step 4",
                    next_action="run checker step 4",
                ),
            ],
            "2026-08-25T12:13:00+08:00",
        )
        self.assertEqual("claim-1", adopted["claim_id"])
        self.assertEqual(researcher_id, adopted["researcher_id"])
        self.assertEqual("chat-B", adopted["actor"])
        self.assertEqual("LIVE", adopted["session_state"])
        self.assertEqual("LEASED", adopted["dispatch_state"])
        self.assertEqual("commit:durable-frontier", adopted["last_recovery_ref"])
        self.assertEqual("checker step 4", adopted["current_unfinished_unit"])
        self.assertEqual("run checker step 4", adopted["next_action"])
        self.assertEqual("seed", adopted["last_progress_ref"])

    def test_second_claim_cannot_preempt_stale_owner_claim(self):
        state = self.reduce(
            [
                event("CLAIM", "2026-08-25T12:00:00+08:00"),
                event("CLAIM", "2026-08-25T12:11:00+08:00", claim_id="claim-2", actor="chat-B"),
            ],
            "2026-08-25T12:12:00+08:00",
        )
        self.assertEqual("claim-1", state["claim_id"])
        self.assertEqual("STALE_RECOVERABLE", state["dispatch_state"])
        self.assertTrue(any("not dispatchable" in item["reason"] for item in state["ignored_events"]))

    def test_heartbeat_cannot_revive_stale_session_without_recovery(self):
        state = self.reduce(
            [
                event("CLAIM", "2026-08-25T12:00:00+08:00"),
                event("HEARTBEAT", "2026-08-25T12:11:00+08:00"),
            ],
            "2026-08-25T12:12:00+08:00",
        )
        self.assertEqual("STALE", state["session_state"])
        self.assertEqual("STALE_RECOVERABLE", state["dispatch_state"])
        self.assertTrue(any("SESSION_ADOPT" in item["reason"] for item in state["ignored_events"]))

    def test_durable_progress_can_reestablish_live_session(self):
        state = self.reduce(
            [
                event("CLAIM", "2026-08-25T12:00:00+08:00"),
                event(
                    "PROGRESS",
                    "2026-08-25T12:11:00+08:00",
                    progress_ref="commit:new-progress",
                    next_action="continue proof",
                ),
            ],
            "2026-08-25T12:12:00+08:00",
        )
        self.assertEqual("LIVE", state["session_state"])
        self.assertEqual("LEASED", state["dispatch_state"])
        self.assertEqual("commit:new-progress", state["last_progress_ref"])

    def test_adoption_requires_verified_recovery_fields(self):
        state = self.reduce(
            [
                event("CLAIM", "2026-08-25T12:00:00+08:00"),
                event("SESSION_ADOPT", "2026-08-25T12:11:00+08:00", actor="chat-B"),
            ],
            "2026-08-25T12:12:00+08:00",
        )
        self.assertEqual("STALE_RECOVERABLE", state["dispatch_state"])
        self.assertEqual("chat-A", state["actor"])
        self.assertTrue(any("recovery_ref" in item["reason"] for item in state["ignored_events"]))

    def test_owner_expiry_releases_claim_after_stale_period(self):
        state = self.reduce(
            [event("CLAIM", "2026-08-25T12:00:00+08:00")],
            "2026-08-25T14:01:00+08:00",
        )
        self.assertEqual("HANDOFF_READY", state["state"])
        self.assertEqual("NEEDS_DISPATCH", state["dispatch_state"])
        self.assertIsNone(state["claim_id"])
        self.assertEqual("NONE", state["session_state"])


if __name__ == "__main__":
    unittest.main()
