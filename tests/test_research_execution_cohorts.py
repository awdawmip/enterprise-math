import json
import tempfile
import unittest
from pathlib import Path

import research_execution_cohorts as cohorts


def write_json(path: Path, value: dict):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


class ExecutionCohortTests(unittest.TestCase):
    def publication(self, root: Path, pid: str, task_id: str = "RS-T"):
        write_json(
            root / "research_task_records" / task_id / f"{pid}.json",
            {"publication_id": pid, "task_id": task_id},
        )

    def cohort(self, lanes):
        return {
            "schema": cohorts.SCHEMA,
            "cohort_id": "EC-1",
            "task_id": "RS-T",
            "record_state": "ACTIVE",
            "opened_by": "EM-DVR-ABC123",
            "opened_at": "2026-08-26T20:40:00+08:00",
            "lanes": lanes,
            "two_reference_passes_required": True,
            "synthesis_required": True,
            "working_truth_granted": False,
            "canonical_promotion_granted": False,
        }

    def lane(self, lane_id, pid, prefix, role="RESEARCH"):
        return {
            "lane_id": lane_id,
            "publication_id": pid,
            "lane_role": role,
            "purpose": f"parallel {lane_id}",
            "output_prefix": prefix,
        }

    def test_no_cohort_has_zero_extra_control_object(self):
        with tempfile.TemporaryDirectory() as td:
            self.assertEqual([], cohorts.audit(Path(td)))

    def test_two_lanes_may_share_publication_for_replication(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            self.publication(root, "TP2-P1")
            write_json(
                root / "research_execution_cohorts" / "RS-T" / "EC-1.json",
                self.cohort([
                    self.lane("replica-a", "TP2-P1", "research_returns/parallel/EC-1/replica-a/", "REPLICATION"),
                    self.lane("replica-b", "TP2-P1", "research_returns/parallel/EC-1/replica-b/", "REPLICATION"),
                ]),
            )
            self.assertEqual([], cohorts.audit(root))

    def test_lanes_may_target_different_retained_publications(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            self.publication(root, "TP2-P1")
            self.publication(root, "TP2-P2")
            write_json(
                root / "research_execution_cohorts" / "RS-T" / "EC-1.json",
                self.cohort([
                    self.lane("route-a", "TP2-P1", "research_returns/parallel/EC-1/route-a/"),
                    self.lane("route-b", "TP2-P2", "research_returns/parallel/EC-1/route-b/", "AUDIT"),
                ]),
            )
            self.assertEqual([], cohorts.audit(root))
            self.assertEqual("TP2-P2", cohorts.lane("RS-T", "EC-1", "route-b", root)["publication_id"])

    def test_overlapping_output_namespaces_fail_closed(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            self.publication(root, "TP2-P1")
            write_json(
                root / "research_execution_cohorts" / "RS-T" / "EC-1.json",
                self.cohort([
                    self.lane("a", "TP2-P1", "research_returns/parallel/EC-1/"),
                    self.lane("b", "TP2-P1", "research_returns/parallel/EC-1/b/"),
                ]),
            )
            self.assertTrue(any("overlap" in item for item in cohorts.audit(root)))

    def test_publication_must_belong_to_same_task(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            self.publication(root, "TP2-P1", task_id="RS-OTHER")
            self.publication(root, "TP2-P2", task_id="RS-T")
            write_json(
                root / "research_execution_cohorts" / "RS-T" / "EC-1.json",
                self.cohort([
                    self.lane("a", "TP2-P1", "research_returns/parallel/EC-1/a/"),
                    self.lane("b", "TP2-P2", "research_returns/parallel/EC-1/b/"),
                ]),
            )
            self.assertTrue(any("different task" in item for item in cohorts.audit(root)))

    def test_parallel_cohort_requires_two_lanes(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            self.publication(root, "TP2-P1")
            write_json(
                root / "research_execution_cohorts" / "RS-T" / "EC-1.json",
                self.cohort([self.lane("a", "TP2-P1", "research_returns/parallel/EC-1/a/")]),
            )
            self.assertTrue(any("at least two lanes" in item for item in cohorts.audit(root)))


if __name__ == "__main__":
    unittest.main()
