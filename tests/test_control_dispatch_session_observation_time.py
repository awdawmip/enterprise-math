import unittest
from datetime import datetime, timezone

import research_control_dispatch as rcd
from tools import research_runtime


NOW = datetime(2026, 9, 7, 1, 30, 0, tzinfo=timezone.utc)
TASK_ID = "RS-LIVENESS-SIM"
CLAIM_ID = "claim-live-1"


def leased_target():
    return {
        "surface": rcd.ORDINARY_TASK,
        "state": {
            "task_id": TASK_ID,
            "kind": "RESEARCH",
            "state": "IN_PROGRESS",
            "dispatch_state": "LEASED",
            "claim_id": CLAIM_ID,
            "researcher_id": "EM-LIVE-TEST",
            "actor": "tester",
            "lease_until": "2026-09-07T02:00:00+00:00",
        },
    }


def observation(at):
    return {
        TASK_ID: {
            "claim_id": CLAIM_ID,
            "activity_evidence_kind": "TASK_RESEARCH_RESPONSE",
            "last_verified_activity_at": at,
        }
    }


class SessionObservationTimeTests(unittest.TestCase):
    def route(self, observations):
        return rcd.route_from_candidates(
            [leased_target()],
            observations=observations,
            now=NOW,
            fresh_task=None,
            fresh_lane=None,
        )

    def test_future_verified_activity_fails_closed(self):
        with self.assertRaisesRegex(research_runtime.RuntimeStateError, "future"):
            self.route(observation("2099-01-01T00:00:00+00:00"))

    def test_runtime_dispatch_itself_rejects_future_activity(self):
        with self.assertRaisesRegex(research_runtime.RuntimeStateError, "future"):
            research_runtime.dispatch_decision(
                leased_target()["state"],
                session_last_activity_at="2099-01-01T00:00:00+00:00",
                now=NOW,
            )

    def test_activity_exactly_now_remains_valid(self):
        result = self.route(observation("2026-09-07T01:30:00+00:00"))
        self.assertEqual(research_runtime.NO_DISPATCH, result["action"])
        self.assertEqual([TASK_ID], result["active_owned_targets"])

    def test_recent_past_activity_remains_valid(self):
        result = self.route(observation("2026-09-07T01:25:00+00:00"))
        self.assertEqual(research_runtime.NO_DISPATCH, result["action"])
        self.assertEqual([TASK_ID], result["active_owned_targets"])

    def test_stale_past_activity_still_adopts_existing_claim(self):
        result = self.route(observation("2026-09-07T01:00:00+00:00"))
        self.assertEqual(research_runtime.ADOPT_OWNER_CLAIM, result["action"])
        self.assertEqual(CLAIM_ID, result["claim_id"])
        self.assertFalse(result["new_claim_required"])

    def test_foreign_future_claim_observation_is_ignored_not_promoted(self):
        foreign = {
            TASK_ID: {
                "claim_id": "not-the-live-claim",
                "activity_evidence_kind": "TASK_RESEARCH_RESPONSE",
                "last_verified_activity_at": "2099-01-01T00:00:00+00:00",
            }
        }
        result = self.route(foreign)
        self.assertEqual("VERIFY_SESSION_LIVENESS", result["action"])
        self.assertEqual(CLAIM_ID, result["targets"][0]["claim_id"])


if __name__ == "__main__":
    unittest.main()
