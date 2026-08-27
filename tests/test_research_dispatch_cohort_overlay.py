import unittest
from unittest import mock

from tools import research_dispatch as dispatch
from tools import research_scheduler as scheduler


TASK = {
    "task_id": "RS-T",
    "title": "test",
    "kind": "RESEARCH",
    "owner": "TEST",
    "priority": "P1",
    "leverage": "HIGH",
    "frontier": "test",
    "registration_source": "IMMUTABLE_TASK_RECORD",
    "publication_id": "TP2-OP",
}


class DispatchCohortOverlayTests(unittest.TestCase):
    def active_state(self):
        return {
            "task_id": "RS-T",
            "state": "ACTIVE_PARALLEL_COHORTS",
            "terminal": False,
            "active_cohort_ids": ["EC-1"],
            "cohorts": [
                {
                    "task_id": "RS-T",
                    "execution_cohort_id": "EC-1",
                    "state": "COHORT_EXECUTION_ACTIVE",
                    "terminal": False,
                    "missing_lane_ids": ["audit"],
                }
            ],
            "next_control_action": "RESOLVE_ACTIVE_COHORT_LANES_AND_SYNTHESIS",
        }

    def test_active_cohort_projects_task_to_cohort_active_and_clears_global_owner(self):
        state = {
            "state": "READY",
            "dispatch_state": "LEASED",
            "claim_id": "task-global-claim",
            "actor": "owner",
            "researcher_id": "EM-TEST-ABC123",
            "identity_source": "CLAIM",
            "lease_until": "2026-08-27T10:00:00+00:00",
        }
        with mock.patch.object(
            dispatch.research_cohort_runtime,
            "task_active_cohort_state",
            return_value=self.active_state(),
        ):
            value = dispatch._overlay_active_cohort(TASK, state, root=dispatch.ROOT)
        self.assertEqual("PARALLEL_COHORT", value["state"])
        self.assertEqual("COHORT_ACTIVE", value["dispatch_state"])
        self.assertIsNone(value["claim_id"])
        self.assertIsNone(value["researcher_id"])
        self.assertEqual("task-global-claim", value["suppressed_task_global_claim"]["claim_id"])
        self.assertEqual(["EC-1"], value["active_cohort_state"]["active_cohort_ids"])
        self.assertIn("research_lane_dispatch.py", value["next_action"])

    def test_active_cohort_overrides_ordinary_terminal_overlay_without_deleting_result_evidence(self):
        state = {
            "state": "DONE",
            "dispatch_state": "COMPLETE",
            "result_id": "RR-OLD",
            "review_id": "DR-OLD",
            "driver_disposition": "ACCEPTED",
            "claim_id": None,
            "actor": None,
            "researcher_id": None,
            "identity_source": None,
            "lease_until": None,
        }
        with mock.patch.object(
            dispatch.research_cohort_runtime,
            "task_active_cohort_state",
            return_value=self.active_state(),
        ):
            value = dispatch._overlay_active_cohort(TASK, state, root=dispatch.ROOT)
        self.assertEqual("COHORT_ACTIVE", value["dispatch_state"])
        self.assertEqual("RR-OLD", value["result_id"])
        self.assertEqual("DR-OLD", value["review_id"])
        self.assertEqual("ACCEPTED", value["driver_disposition"])

    def test_no_active_cohort_leaves_ordinary_state_unchanged(self):
        state = {"state": "READY", "dispatch_state": "NEEDS_DISPATCH", "claim_id": None}
        with mock.patch.object(
            dispatch.research_cohort_runtime,
            "task_active_cohort_state",
            return_value=None,
        ):
            value = dispatch._overlay_active_cohort(TASK, state, root=dispatch.ROOT)
        self.assertIs(value, state)

    def test_task_global_selector_ignores_cohort_active(self):
        policy = {
            "selection_policy": {
                "state_order": ["HANDOFF_READY", "READY", "BACKLOG"],
                "priority_order": ["P0", "P1", "P2"],
                "leverage_order": ["CRITICAL", "HIGH", "MEDIUM", "LOW"],
            }
        }
        states = [
            {
                "task_id": "RS-COHORT",
                "kind": "RESEARCH",
                "state": "PARALLEL_COHORT",
                "dispatch_state": "COHORT_ACTIVE",
                "priority": "P0",
                "leverage": "CRITICAL",
                "last_progress_at": "2026-08-27T00:00:00+00:00",
            },
            {
                "task_id": "RS-ORDINARY",
                "kind": "RESEARCH",
                "state": "READY",
                "dispatch_state": "NEEDS_DISPATCH",
                "priority": "P2",
                "leverage": "LOW",
                "last_progress_at": "2026-08-27T00:00:00+00:00",
            },
        ]
        with mock.patch.object(dispatch, "load_json", return_value=policy), mock.patch.object(
            dispatch, "effective_states", return_value=states
        ):
            chosen = dispatch.select_task(
                [],
                now=scheduler.parse_time("2026-08-27T01:00:00+00:00"),
                kind="RESEARCH",
                root=dispatch.ROOT,
            )
        self.assertEqual("RS-ORDINARY", chosen["task_id"])


if __name__ == "__main__":
    unittest.main()
