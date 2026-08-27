import json
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from tools import research_cohort_runtime as cohort_runtime
import research_parallel_evidence as parallel


def write_json(path: Path, value: dict):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


class CohortRuntimeTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.task_id = "RS-T"
        self.cohort_id = "EC-1"
        write_json(
            self.root / "research_execution_cohorts" / self.task_id / f"{self.cohort_id}.json",
            {
                "schema": "ENTERPRISE_MATH_PARALLEL_EXECUTION_COHORT_V1",
                "cohort_id": self.cohort_id,
                "task_id": self.task_id,
                "record_state": "ACTIVE",
                "opened_by": "EM-DVR-ABC123",
                "opened_at": "2026-08-27T00:00:00+00:00",
                "lanes": [
                    {
                        "lane_id": "route-a",
                        "publication_id": "TP2-P1",
                        "lane_role": "RESEARCH",
                        "purpose": "route A",
                        "output_prefix": "research_returns/parallel/EC-1/route-a/",
                    },
                    {
                        "lane_id": "route-b",
                        "publication_id": "TP2-P2",
                        "lane_role": "AUDIT",
                        "purpose": "route B",
                        "output_prefix": "research_returns/parallel/EC-1/route-b/",
                    },
                ],
                "two_reference_passes_required": True,
                "synthesis_required": True,
                "working_truth_granted": False,
                "canonical_promotion_granted": False,
            },
        )

    def add_result(self, result_id, lane_id, publication_id):
        write_json(
            self.root / "research_result_records" / self.task_id / f"{result_id}.json",
            {
                "record_schema": "ENTERPRISE_MATH_RESEARCH_RESULT_RECORD_V1",
                "result_id": result_id,
                "task_id": self.task_id,
                "publication_id": publication_id,
                "execution_cohort_id": self.cohort_id,
                "execution_lane_id": lane_id,
            },
        )

    def test_first_lane_result_never_terminalizes_whole_cohort(self):
        self.add_result("RR-A", "route-a", "TP2-P1")
        state = cohort_runtime.cohort_state(self.task_id, self.cohort_id, self.root)
        self.assertEqual("COHORT_EXECUTION_ACTIVE", state["state"])
        self.assertFalse(state["terminal"])
        self.assertEqual(["route-b"], state["missing_lane_ids"])
        self.assertEqual("DISPATCH_OR_COMPLETE_MISSING_LANES", state["next_control_action"])

    def test_all_lanes_complete_routes_to_parallel_intake_not_latest_wins(self):
        self.add_result("RR-A", "route-a", "TP2-P1")
        self.add_result("RR-B", "route-b", "TP2-P2")
        state = cohort_runtime.cohort_state(self.task_id, self.cohort_id, self.root)
        self.assertEqual("AWAITING_PARALLEL_INTAKE", state["state"])
        self.assertFalse(state["terminal"])
        self.assertEqual([], state["missing_lane_ids"])
        self.assertEqual(["RR-A", "RR-B"], state["result_ids"])

    def test_exact_cohort_evidence_requires_both_reference_passes_before_synthesis(self):
        self.add_result("RR-A", "route-a", "TP2-P1")
        self.add_result("RR-B", "route-b", "TP2-P2")
        pids = ["TP2-P1", "TP2-P2"]
        rids = ["RR-A", "RR-B"]
        digest = parallel.evidence_hash(pids, rids)
        intake_id = "PI-EC1"
        write_json(
            self.root / "research_parallel_intakes" / self.task_id / f"{intake_id}.json",
            {
                "schema": parallel.INTAKE_SCHEMA,
                "intake_id": intake_id,
                "task_id": self.task_id,
                "mode": "PARALLEL_RESULTS",
                "publication_ids": pids,
                "result_ids": rids,
                "evidence_set_sha256": digest,
            },
        )
        state = cohort_runtime.cohort_state(self.task_id, self.cohort_id, self.root)
        self.assertEqual("AWAITING_REFERENCE_PASS_1", state["state"])
        write_json(
            self.root / "research_parallel_reference_passes" / intake_id / "P1.json",
            {
                "schema": parallel.PASS_SCHEMA,
                "pass_id": "P1",
                "intake_id": intake_id,
                "pass_number": 1,
                "evidence_set_sha256": digest,
            },
        )
        state = cohort_runtime.cohort_state(self.task_id, self.cohort_id, self.root)
        self.assertEqual("AWAITING_REFERENCE_PASS_2", state["state"])
        write_json(
            self.root / "research_parallel_reference_passes" / intake_id / "P2.json",
            {
                "schema": parallel.PASS_SCHEMA,
                "pass_id": "P2",
                "intake_id": intake_id,
                "pass_number": 2,
                "evidence_set_sha256": digest,
            },
        )
        state = cohort_runtime.cohort_state(self.task_id, self.cohort_id, self.root)
        self.assertEqual("AWAITING_SYNTHESIS", state["state"])
        self.assertFalse(state["terminal"])

    def test_result_with_wrong_lane_publication_fails_closed(self):
        self.add_result("RR-BAD", "route-a", "TP2-P2")
        with self.assertRaisesRegex(cohort_runtime.CohortRuntimeError, "publication differs"):
            cohort_runtime.cohort_state(self.task_id, self.cohort_id, self.root)

    def test_task_state_is_terminal_when_every_active_cohort_has_terminal_synthesis(self):
        cohorts = [
            {"cohort_id": "EC-1", "task_id": self.task_id, "record_state": "ACTIVE"},
            {"cohort_id": "EC-2", "task_id": self.task_id, "record_state": "ACTIVE"},
        ]
        terminal_states = {
            "EC-1": {
                "execution_cohort_id": "EC-1",
                "state": "PARALLEL_SYNTHESIS_TERMINAL",
                "terminal": True,
                "terminal_control_disposition": "ACCEPTED",
            },
            "EC-2": {
                "execution_cohort_id": "EC-2",
                "state": "PARALLEL_SYNTHESIS_TERMINAL",
                "terminal": True,
                "terminal_control_disposition": "CLOSED",
            },
        }
        with mock.patch.object(cohort_runtime, "active_cohorts", return_value=cohorts), mock.patch.object(
            cohort_runtime,
            "cohort_state",
            side_effect=lambda task, cohort, root: terminal_states[cohort],
        ):
            state = cohort_runtime.task_active_cohort_state(self.task_id, self.root)
        self.assertEqual("TERMINAL_PARALLEL_COHORTS", state["state"])
        self.assertTrue(state["terminal"])
        self.assertEqual(["EC-1", "EC-2"], state["terminal_cohort_ids"])
        self.assertEqual(["ACCEPTED", "CLOSED"], state["terminal_control_dispositions"])
        self.assertEqual("REEVALUATE_PARENT", state["next_control_action"])

    def test_new_incomplete_cohort_reopens_derived_task_state_without_rewriting_old_terminal_cohort(self):
        cohorts = [
            {"cohort_id": "EC-OLD", "task_id": self.task_id, "record_state": "ACTIVE"},
            {"cohort_id": "EC-NEW", "task_id": self.task_id, "record_state": "ACTIVE"},
        ]
        states = {
            "EC-OLD": {
                "execution_cohort_id": "EC-OLD",
                "state": "PARALLEL_SYNTHESIS_TERMINAL",
                "terminal": True,
                "terminal_control_disposition": "ACCEPTED",
            },
            "EC-NEW": {
                "execution_cohort_id": "EC-NEW",
                "state": "COHORT_EXECUTION_ACTIVE",
                "terminal": False,
                "missing_lane_ids": ["replication-2"],
            },
        }
        with mock.patch.object(cohort_runtime, "active_cohorts", return_value=cohorts), mock.patch.object(
            cohort_runtime,
            "cohort_state",
            side_effect=lambda task, cohort, root: states[cohort],
        ):
            state = cohort_runtime.task_active_cohort_state(self.task_id, self.root)
        self.assertEqual("ACTIVE_PARALLEL_COHORTS", state["state"])
        self.assertFalse(state["terminal"])
        self.assertEqual(["EC-OLD"], state["terminal_cohort_ids"])
        self.assertEqual("RESOLVE_ACTIVE_COHORT_LANES_AND_SYNTHESIS", state["next_control_action"])


if __name__ == "__main__":
    unittest.main()
