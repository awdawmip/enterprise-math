import unittest
from unittest import mock

from tools import research_lane_dispatch as lane_dispatch


class LaneDispatchTests(unittest.TestCase):
    def cohort(self):
        return {
            "cohort_id": "EC-1",
            "task_id": "RS-T",
            "record_state": "ACTIVE",
            "lanes": [
                {"lane_id": "research", "lane_role": "RESEARCH", "publication_id": "TP2-P1", "output_prefix": "research_returns/parallel/EC-1/research/"},
                {"lane_id": "audit", "lane_role": "AUDIT", "publication_id": "TP2-P2", "output_prefix": "research_returns/parallel/EC-1/audit/"},
            ],
        }

    def reduced(self, lane_id):
        return {
            "task_id": "RS-T",
            "execution_cohort_id": "EC-1",
            "execution_lane_id": lane_id,
            "dispatch_state": "NEEDS_DISPATCH",
            "state": "READY",
        }

    def test_frozen_lane_is_not_automatically_redispatched(self):
        with mock.patch.object(lane_dispatch.research_cohort_runtime, "active_cohorts", return_value=[self.cohort()]), mock.patch.object(
            lane_dispatch.research_cohort_runtime,
            "lane_results",
            side_effect=lambda task, cohort, lane, root: ([{"result_id": "RR-R"}] if lane == "research" else []),
        ), mock.patch.object(
            lane_dispatch.research_lane_claims,
            "reduce_lane",
            side_effect=lambda task, cohort, lane, events, now, root: self.reduced(lane),
        ):
            states = lane_dispatch.lane_states("RS-T", [], now=object())
        by_lane = {row["execution_lane_id"]: row for row in states}
        self.assertEqual("AWAITING_COHORT_REFERENCE", by_lane["research"]["dispatch_state"])
        self.assertEqual(["RR-R"], by_lane["research"]["result_ids"])
        self.assertEqual("NEEDS_DISPATCH", by_lane["audit"]["dispatch_state"])

    def test_selector_chooses_missing_lane_not_completed_lane(self):
        with mock.patch.object(
            lane_dispatch,
            "lane_states",
            return_value=[
                {"execution_cohort_id": "EC-1", "execution_lane_id": "a", "dispatch_state": "AWAITING_COHORT_REFERENCE"},
                {"execution_cohort_id": "EC-1", "execution_lane_id": "b", "dispatch_state": "NEEDS_DISPATCH"},
            ],
        ):
            chosen = lane_dispatch.select_lane("RS-T", [], now=object())
        self.assertEqual("b", chosen["execution_lane_id"])

    def test_multiple_frozen_results_are_retained_not_rejected(self):
        frozen = [{"result_id": "RR-A"}, {"result_id": "RR-B"}]
        with mock.patch.object(lane_dispatch.research_cohort_runtime, "active_cohorts", return_value=[self.cohort()]), mock.patch.object(
            lane_dispatch.research_cohort_runtime,
            "lane_results",
            side_effect=lambda task, cohort, lane, root: (frozen if lane == "research" else []),
        ), mock.patch.object(
            lane_dispatch.research_lane_claims,
            "reduce_lane",
            side_effect=lambda task, cohort, lane, events, now, root: self.reduced(lane),
        ):
            states = lane_dispatch.lane_states("RS-T", [], now=object())
        research = next(row for row in states if row["execution_lane_id"] == "research")
        self.assertEqual(["RR-A", "RR-B"], research["result_ids"])


if __name__ == "__main__":
    unittest.main()
