import unittest

from tools import research_runtime_reducer as rr


def task():
    return {
        "task_id": "RS-T1",
        "base_state": "READY",
        "priority": "P0",
        "leverage": "HIGH",
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


class ResultHandoffDispatchGuardTests(unittest.TestCase):
    def reduce(self, handoff_extra):
        rid = rr.researcher_id_for_claim(task(), "c1")
        return rr.reduce_task(
            task(),
            [
                event("CLAIM", "2026-09-01T00:00:00+00:00", lease_minutes=30),
                event(
                    "HANDOFF",
                    "2026-09-01T00:10:00+00:00",
                    researcher_id=rid,
                    next_action="Driver review exact frozen result",
                    **handoff_extra,
                ),
            ],
            default_lease_minutes=30,
            now=rr.parse_time("2026-09-01T00:11:00+00:00"),
        )

    def test_result_bearing_handoff_waits_for_review(self):
        state = self.reduce({"result_id": "RR-TEST-123"})
        self.assertEqual("FROZEN_RETURN", state["state"])
        self.assertEqual("AWAITING_REVIEW", state["dispatch_state"])
        self.assertEqual("RR-TEST-123", state["result_id"])
        self.assertIsNone(state["claim_id"])

    def test_result_bearing_handoff_is_not_a_fresh_candidate(self):
        state = self.reduce({"result_id": "RR-TEST-123"})
        state.update({"kind": "RESEARCH", "priority": "P0", "leverage": "HIGH"})
        self.assertIsNone(rr.select_state([state], rr.load_policy(), kind="RESEARCH"))

    def test_explicit_driver_review_terminal_scope_waits_without_result_id(self):
        state = self.reduce(
            {"terminal_scope": "RESEARCH_RETURN_FROZEN_AWAITING_DRIVER_REVIEW"}
        )
        self.assertEqual("FROZEN_RETURN", state["state"])
        self.assertEqual("AWAITING_REVIEW", state["dispatch_state"])
        self.assertNotIn("result_id", state)
        self.assertEqual(
            "RESEARCH_RETURN_FROZEN_AWAITING_DRIVER_REVIEW",
            state["terminal_scope"],
        )
        self.assertIsNone(state["claim_id"])

    def test_explicit_driver_review_terminal_scope_is_not_a_fresh_candidate(self):
        state = self.reduce(
            {"terminal_scope": "RESEARCH_RETURN_FROZEN_AWAITING_DRIVER_REVIEW"}
        )
        state.update({"kind": "RESEARCH", "priority": "P0", "leverage": "HIGH"})
        self.assertIsNone(rr.select_state([state], rr.load_policy(), kind="RESEARCH"))

    def test_legacy_terminal_candidate_waits_for_driver_review(self):
        state = self.reduce(
            {"terminal_candidate": "SUCCESS_REVIEW_COMPLETE_AWAITING_DRIVER_DECISION"}
        )
        self.assertEqual("FROZEN_RETURN", state["state"])
        self.assertEqual("AWAITING_REVIEW", state["dispatch_state"])
        self.assertEqual(
            "SUCCESS_REVIEW_COMPLETE_AWAITING_DRIVER_DECISION",
            state["terminal_candidate"],
        )
        self.assertIsNone(state["claim_id"])

    def test_plain_handoff_remains_dispatchable(self):
        state = self.reduce({})
        self.assertEqual("HANDOFF_READY", state["state"])
        self.assertEqual("NEEDS_DISPATCH", state["dispatch_state"])
        self.assertNotIn("result_id", state)

    def test_unrecognized_terminal_scope_does_not_invent_review_authority(self):
        state = self.reduce({"terminal_scope": "RESEARCHER_TO_RESEARCHER_CONTINUATION"})
        self.assertEqual("HANDOFF_READY", state["state"])
        self.assertEqual("NEEDS_DISPATCH", state["dispatch_state"])
        self.assertNotIn("terminal_scope", state)

    def test_malformed_result_id_does_not_open_fresh_dispatch(self):
        state = self.reduce({"result_id": "   "})
        self.assertEqual("CLAIMED", state["state"])
        self.assertEqual("LEASED", state["dispatch_state"])
        self.assertEqual("c1", state["claim_id"])
        self.assertTrue(any("result_id" in item["reason"] for item in state["ignored_events"]))


if __name__ == "__main__":
    unittest.main()
