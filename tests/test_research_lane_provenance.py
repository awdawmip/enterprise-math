import json
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from tools import research_execution_records as executions
from tools import research_result_records as results


def write_json(path: Path, value: dict):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


class LaneProvenanceTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.task_id = "RS-T"
        for pid, digit in (("TP2-P1", "1"), ("TP2-P2", "2")):
            taskbook = self.root / "research_tasks" / f"{pid}.md"
            taskbook.parent.mkdir(parents=True, exist_ok=True)
            taskbook.write_text("fixture\n", encoding="utf-8")
            write_json(
                self.root / "research_task_records" / self.task_id / f"{pid}.json",
                {
                    "record_schema": "ENTERPRISE_MATH_TASK_PUBLICATION_RECORD_V2",
                    "task_id": self.task_id,
                    "publication_id": pid,
                    "record_state": "ACTIVE",
                    "claimable": True,
                    "taskbook_path": f"research_tasks/{pid}.md",
                    "taskbook_blob_sha1": "sha1:" + digit * 40,
                },
            )
        write_json(
            self.root / "research_execution_cohorts" / self.task_id / "EC-1.json",
            {
                "schema": "ENTERPRISE_MATH_PARALLEL_EXECUTION_COHORT_V1",
                "cohort_id": "EC-1",
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

    def prepare(self, lane_id, claim_id, publication_output):
        with mock.patch.object(
            executions.research_taskbook,
            "split_taskbook",
            return_value=({"identity_lane": "TEST"}, ""),
        ):
            return executions.prepare_intent(
                task_id=self.task_id,
                claim_id=claim_id,
                researcher_id="EM-TEST-ABC123",
                theorem_owner="TEST_OWNER",
                execution_branch=f"research/{lane_id}",
                execution_branch_base="a" * 40,
                allowed_outputs=[publication_output],
                owner_lease_minutes=120,
                prepared_at="2026-08-27T00:02:00+00:00",
                execution_cohort_id="EC-1",
                execution_lane_id=lane_id,
                root=self.root,
            )

    def test_lane_execution_pins_lane_publication_and_namespace(self):
        record = self.prepare(
            "route-b",
            "claim-shared",
            "research_returns/parallel/EC-1/route-b/",
        )
        self.assertEqual("TP2-P2", record["publication_id"])
        self.assertEqual("EC-1", record["execution_cohort_id"])
        self.assertEqual("route-b", record["execution_lane_id"])
        self.assertEqual(
            "research_returns/parallel/EC-1/route-b/",
            record["lane_output_prefix"],
        )

    def test_same_claim_id_is_scoped_independently_by_lane(self):
        a = self.prepare(
            "route-a",
            "same-claim",
            "research_returns/parallel/EC-1/route-a/",
        )
        b = self.prepare(
            "route-b",
            "same-claim",
            "research_returns/parallel/EC-1/route-b/",
        )
        write_json(
            self.root / "research_execution_records" / self.task_id / f"{a['execution_record_id']}.json",
            a,
        )
        write_json(
            self.root / "research_execution_records" / self.task_id / f"{b['execution_record_id']}.json",
            b,
        )
        self.assertNotEqual(a["execution_record_id"], b["execution_record_id"])
        self.assertIsNone(executions.intent_for_claim(self.task_id, "same-claim", self.root))
        self.assertEqual(
            a["execution_record_id"],
            executions.intent_for_claim(
                self.task_id,
                "same-claim",
                self.root,
                execution_cohort_id="EC-1",
                execution_lane_id="route-a",
            )["execution_record_id"],
        )
        self.assertEqual([], executions.audit(self.root))

    def test_lane_execution_rejects_output_namespace_escape(self):
        with self.assertRaisesRegex(executions.ExecutionRecordError, "output_prefix"):
            self.prepare(
                "route-a",
                "escape",
                "research_returns/parallel/EC-1/route-b/",
            )

    def test_lane_result_freezes_retained_publication_and_copies_scope_to_review(self):
        execution = self.prepare(
            "route-b",
            "result-claim",
            "research_returns/parallel/EC-1/route-b/",
        )
        write_json(
            self.root / "research_execution_records" / self.task_id / f"{execution['execution_record_id']}.json",
            execution,
        )
        return_path = self.root / "research_returns/parallel/EC-1/route-b/return.md"
        return_path.parent.mkdir(parents=True, exist_ok=True)
        return_path.write_text("frozen result\n", encoding="utf-8")
        result = results.freeze_result(
            execution_record_id=execution["execution_record_id"],
            return_path=return_path,
            output_paths=[return_path],
            owner_head="b" * 40,
            terminal_verdict="PASS",
            hard_target_disposition="LANE_COMPLETE",
            unresolved_residue="NONE",
            method_harvest="RESULT_ONLY",
            independence_status="NOT_APPLICABLE",
            source_exposure_status="NOT_APPLICABLE",
            next_control_plane_recommendation="REFERENCE_PASS_1",
            frozen_at="2026-08-27T00:03:00+00:00",
            root=self.root,
        )
        self.assertEqual("TP2-P2", result["publication_id"])
        self.assertEqual("EC-1", result["execution_cohort_id"])
        self.assertEqual("route-b", result["execution_lane_id"])
        result_path = self.root / "research_result_records" / self.task_id / f"{result['result_id']}.json"
        write_json(result_path, result)
        loaded = dict(result)
        loaded["_record_path"] = result_path.relative_to(self.root).as_posix()
        review_path = self.root / "driver_reviews" / "review.md"
        review_path.parent.mkdir(parents=True, exist_ok=True)
        review_path.write_text("review\n", encoding="utf-8")
        review = results.review_result(
            result=loaded,
            driver_id="EM-DVR-ABC123",
            disposition="ACCEPTED",
            review_path=review_path,
            destination_class="NONE",
            destination_ref_or_none="",
            reviewed_at="2026-08-27T00:04:00+00:00",
            root=self.root,
        )
        self.assertEqual("EC-1", review["execution_cohort_id"])
        self.assertEqual("route-b", review["execution_lane_id"])
        review_dir = self.root / "research_result_reviews" / result["result_id"]
        write_json(review_dir / f"{review['review_id']}.json", review)
        self.assertEqual([], results.audit(self.root))


if __name__ == "__main__":
    unittest.main()
