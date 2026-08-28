from __future__ import annotations

import unittest
from datetime import datetime, timezone

import research_control_dispatch
from tools import research_runtime


NOW = datetime(2026, 8, 28, 8, 0, tzinfo=timezone.utc)


def leased_task(task_id: str = "RS-TEST") -> dict:
    return {
        "task_id": task_id,
        "kind": "RESEARCH",
        "state": "IN_PROGRESS",
        "dispatch_state": "LEASED",
        "claim_id": f"CLM-{task_id}",
        "researcher_id": "EM-TEST-000001",
        "lease_until": "2026-08-28T10:00:00+00:00",
    }


def leased_lane() -> dict:
    value = leased_task("RS-COHORT")
    value.update(
        {
            "execution_cohort_id": "COH-1",
            "execution_lane_id": "LANE-A",
        }
    )
    return value


def target(state: dict, surface: str = research_control_dispatch.ORDINARY_TASK) -> dict:
    return {"surface": surface, "state": state}


def observation(
    state: dict,
    at: str,
    *,
    evidence_kind: str = "TASK_RESEARCH_RESPONSE",
    claim_id: str | None = None,
) -> dict[str, str]:
    return {
        "claim_id": claim_id or state["claim_id"],
        "activity_evidence_kind": evidence_kind,
        "last_verified_activity_at": at,
    }


class RecoverBeforeFreshDispatchTests(unittest.TestCase):
    def test_stale_valid_owner_is_adopted_before_fresh_dispatch(self) -> None:
        owned = leased_task()
        fresh = {
            "task_id": "RS-FRESH",
            "dispatch_state": "NEEDS_DISPATCH",
            "kind": "RESEARCH",
        }
        result = research_control_dispatch.route_from_candidates(
            [target(owned)],
            observations={"RS-TEST": observation(owned, "2026-08-28T07:40:00+00:00")},
            now=NOW,
            fresh_task=fresh,
            fresh_lane=None,
        )
        self.assertEqual(result["action"], research_runtime.ADOPT_OWNER_CLAIM)
        self.assertEqual(result["claim_id"], owned["claim_id"])
        self.assertTrue(result["owner_claim_preserved"])
        self.assertFalse(result["new_claim_required"])

    def test_active_owner_scope_does_not_block_independent_fresh_dispatch(self) -> None:
        owned = leased_task()
        fresh = {
            "task_id": "RS-FRESH",
            "dispatch_state": "NEEDS_DISPATCH",
            "kind": "RESEARCH",
        }
        result = research_control_dispatch.route_from_candidates(
            [target(owned)],
            observations={"RS-TEST": observation(owned, "2026-08-28T07:55:00+00:00")},
            now=NOW,
            fresh_task=fresh,
            fresh_lane=None,
        )
        self.assertEqual(result["action"], research_runtime.CLAIM_NEW_OWNER)
        self.assertEqual(result["target"]["task_id"], "RS-FRESH")
        self.assertTrue(result["new_claim_required"])

    def test_durable_execution_progress_is_valid_owner_scope_liveness(self) -> None:
        owned = leased_task()
        result = research_control_dispatch.route_from_candidates(
            [target(owned)],
            observations={
                "RS-TEST": observation(
                    owned,
                    "2026-08-28T07:55:00+00:00",
                    evidence_kind="DURABLE_EXECUTION_PROGRESS",
                )
            },
            now=NOW,
            fresh_task=None,
            fresh_lane=None,
        )
        self.assertEqual(result["action"], research_runtime.NO_DISPATCH)
        self.assertEqual(result["active_owned_targets"], ["RS-TEST"])

    def test_unknown_session_liveness_is_not_false_no_dispatch(self) -> None:
        result = research_control_dispatch.route_from_candidates(
            [target(leased_task())],
            observations={},
            now=NOW,
            fresh_task=None,
            fresh_lane=None,
        )
        self.assertEqual(result["action"], "VERIFY_SESSION_LIVENESS")
        self.assertFalse(result["new_claim_required"])
        self.assertEqual(result["targets"][0]["claim_id"], "CLM-RS-TEST")

    def test_foreign_claim_activity_cannot_keep_current_owner_active(self) -> None:
        owned = leased_task()
        result = research_control_dispatch.route_from_candidates(
            [target(owned)],
            observations={
                "RS-TEST": observation(
                    owned,
                    "2026-08-28T07:59:00+00:00",
                    claim_id="CLM-OLD-OR-FOREIGN",
                )
            },
            now=NOW,
            fresh_task=None,
            fresh_lane=None,
        )
        self.assertEqual(result["action"], "VERIFY_SESSION_LIVENESS")
        self.assertEqual(result["targets"][0]["claim_id"], owned["claim_id"])

    def test_stale_cohort_lane_preserves_exact_lane_owner_scope(self) -> None:
        lane = leased_lane()
        key = "RS-COHORT::COH-1::LANE-A"
        result = research_control_dispatch.route_from_candidates(
            [target(lane, research_control_dispatch.COHORT_LANE)],
            observations={key: observation(lane, "2026-08-28T07:30:00+00:00")},
            now=NOW,
            fresh_task=None,
            fresh_lane=None,
        )
        self.assertEqual(result["action"], research_runtime.ADOPT_OWNER_CLAIM)
        self.assertEqual(result["surface"], research_control_dispatch.COHORT_LANE)
        self.assertEqual(result["target_key"], key)
        self.assertEqual(result["claim_id"], lane["claim_id"])
        self.assertFalse(result["new_claim_required"])

    def test_fresh_cohort_lane_is_used_when_no_task_global_target_exists(self) -> None:
        lane = {
            "task_id": "RS-COHORT",
            "execution_cohort_id": "COH-1",
            "execution_lane_id": "LANE-B",
            "dispatch_state": "NEEDS_DISPATCH",
        }
        result = research_control_dispatch.route_from_candidates(
            [],
            observations={},
            now=NOW,
            fresh_task=None,
            fresh_lane=lane,
        )
        self.assertEqual(result["action"], research_runtime.CLAIM_NEW_OWNER)
        self.assertEqual(result["surface"], research_control_dispatch.COHORT_LANE)
        self.assertEqual(result["target_key"], "RS-COHORT::COH-1::LANE-B")

    def test_no_dispatch_requires_no_recovery_and_no_fresh_target(self) -> None:
        result = research_control_dispatch.route_from_candidates(
            [],
            observations={},
            now=NOW,
            fresh_task=None,
            fresh_lane=None,
        )
        self.assertEqual(result["action"], research_runtime.NO_DISPATCH)
        self.assertFalse(result["new_claim_required"])

    def test_session_observation_schema_binds_claim_and_activity_kind(self) -> None:
        payload = {
            "schema": research_control_dispatch.SESSION_OBSERVATION_SCHEMA,
            "observations": [
                {
                    "task_id": "RS-TEST",
                    "claim_id": "CLM-RS-TEST",
                    "activity_evidence_kind": "TASK_RESEARCH_RESPONSE",
                    "last_verified_activity_at": "2026-08-28T07:55:00+00:00",
                }
            ],
        }
        parsed = research_control_dispatch.parse_session_observations(payload)
        self.assertEqual(parsed["RS-TEST"]["claim_id"], "CLM-RS-TEST")
        self.assertEqual(
            parsed["RS-TEST"]["activity_evidence_kind"],
            "TASK_RESEARCH_RESPONSE",
        )

    def test_control_plane_response_is_rejected_as_owner_scope_liveness(self) -> None:
        payload = {
            "schema": research_control_dispatch.SESSION_OBSERVATION_SCHEMA,
            "observations": [
                {
                    "task_id": "RS-TEST",
                    "claim_id": "CLM-RS-TEST",
                    "activity_evidence_kind": "CONTROL_PLANE_RESPONSE",
                    "last_verified_activity_at": "2026-08-28T07:59:00+00:00",
                }
            ],
        }
        with self.assertRaises(research_control_dispatch.ControlDispatchError):
            research_control_dispatch.parse_session_observations(payload)

    def test_session_observation_schema_rejects_partial_lane_identity(self) -> None:
        payload = {
            "schema": research_control_dispatch.SESSION_OBSERVATION_SCHEMA,
            "observations": [
                {
                    "task_id": "RS-COHORT",
                    "execution_cohort_id": "COH-1",
                    "claim_id": "CLM-RS-COHORT",
                    "activity_evidence_kind": "TASK_RESEARCH_RESPONSE",
                    "last_verified_activity_at": "2026-08-28T07:30:00+00:00",
                }
            ],
        }
        with self.assertRaises(research_control_dispatch.ControlDispatchError):
            research_control_dispatch.parse_session_observations(payload)


if __name__ == "__main__":
    unittest.main()
