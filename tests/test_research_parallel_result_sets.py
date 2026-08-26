import unittest
from unittest import mock

from tools import research_execution_records as executions
from tools import research_result_records as results


class ResultGenerationAndParallelSetTests(unittest.TestCase):
    def result(self, rid, publication_id, frozen_at="2026-08-26T01:00:00+00:00"):
        return {
            "result_id": rid,
            "task_id": "RS-T",
            "publication_id": publication_id,
            "frozen_at": frozen_at,
            "_record_path": f"research_result_records/RS-T/{rid}.json",
        }

    def review(self, rid, review_id=None, disposition="ACCEPTED"):
        return {
            "review_id": review_id or "RV-" + rid,
            "result_id": rid,
            "disposition": disposition,
        }

    def resolution(self, operational="RR-B", retained=None, operational_review_id=None):
        row = {
            "task_id": "RS-T",
            "publication_id": "TP-CURRENT",
            "operational_result_id": operational,
            "retained_parallel_result_ids": retained or ["RR-A", "RR-B"],
            "parallel_intake_id": "PI-T",
            "relationship": "COMPATIBLE_COMPLEMENTARY",
            "final_disposition": "KEEP_PARALLEL_AND_SELECT_OPERATIONAL_RESULT",
            "epistemic_preference": False,
            "working_truth_granted": False,
            "canonical_promotion_granted": False,
            "delete_or_rewrite_nonoperational_results": False,
        }
        if operational_review_id is not None:
            row["operational_review_id"] = operational_review_id
        return row

    def test_old_terminal_result_does_not_close_new_current_generation(self):
        old = self.result("RR-OLD", "TP-OLD")
        with mock.patch.object(results, "iter_results", return_value=[old]), mock.patch.object(
            results.research_task_records,
            "current_records",
            return_value={"RS-T": {"publication_id": "TP-NEW"}},
        ):
            self.assertIsNone(results.task_result_state("RS-T"))

    def test_current_generation_result_controls_current_state(self):
        old = self.result("RR-OLD", "TP-OLD")
        new = self.result("RR-NEW", "TP-NEW")
        with mock.patch.object(results, "iter_results", return_value=[old, new]), mock.patch.object(
            results.research_task_records,
            "current_records",
            return_value={"RS-T": {"publication_id": "TP-NEW"}},
        ), mock.patch.object(results, "reviews_for_result", return_value=[]), mock.patch.object(
            results, "result_set_resolutions", return_value={}
        ):
            state = results.task_result_state("RS-T")
        self.assertEqual("AWAITING_DRIVER_REVIEW", state["state"])
        self.assertEqual("RR-NEW", state["result"]["result_id"])

    def test_explicit_historical_generation_remains_queryable(self):
        old = self.result("RR-OLD", "TP-OLD")
        new = self.result("RR-NEW", "TP-NEW")
        with mock.patch.object(results, "iter_results", return_value=[old, new]), mock.patch.object(
            results, "reviews_for_result", return_value=[self.review("RR-OLD")]
        ), mock.patch.object(results, "result_set_resolutions", return_value={}):
            state = results.task_result_state("RS-T", publication_id="TP-OLD")
        self.assertEqual("TERMINAL", state["state"])
        self.assertEqual("RR-OLD", state["result"]["result_id"])

    def test_multiple_results_without_resolution_do_not_use_latest_timestamp(self):
        first = self.result("RR-A", "TP-CURRENT", "2099-01-01T00:00:00+00:00")
        second = self.result("RR-B", "TP-CURRENT", "1900-01-01T00:00:00+00:00")
        with mock.patch.object(results, "iter_results", return_value=[first, second]), mock.patch.object(
            results, "result_set_resolutions", return_value={}
        ):
            state = results.task_result_state("RS-T", publication_id="TP-CURRENT")
        self.assertEqual("AWAITING_DRIVER_REVIEW", state["state"])
        self.assertEqual("PARALLEL_RESULTS_AWAITING_RECONCILIATION", state["parallel_state"])
        self.assertIsNone(state["operational_result_id"])
        self.assertFalse(state["terminal"])
        self.assertEqual({"RR-A", "RR-B"}, set(state["retained_parallel_result_ids"]))

    def test_explicit_operational_result_binds_runtime_without_rejecting_other_result(self):
        first = self.result("RR-A", "TP-CURRENT")
        second = self.result("RR-B", "TP-CURRENT")
        resolution = self.resolution(operational_review_id="RV-B")
        with mock.patch.object(results, "iter_results", return_value=[first, second]), mock.patch.object(
            results, "result_set_resolutions", return_value={("RS-T", "TP-CURRENT"): resolution}
        ), mock.patch.object(
            results,
            "reviews_for_result",
            side_effect=lambda rid, root=results.ROOT: [self.review(rid, "RV-B")] if rid == "RR-B" else [],
        ):
            state = results.task_result_state("RS-T", publication_id="TP-CURRENT")
        self.assertEqual("TERMINAL", state["state"])
        self.assertTrue(state["terminal"])
        self.assertEqual("RR-B", state["operational_result_id"])
        self.assertEqual("PARALLEL_RESULTS_OPERATIONALLY_BOUND", state["parallel_state"])
        self.assertEqual({"RR-A", "RR-B"}, set(state["retained_parallel_result_ids"]))

    def test_new_parallel_result_makes_old_resolution_locally_stale_not_global_failure(self):
        values = [
            self.result("RR-A", "TP-CURRENT"),
            self.result("RR-B", "TP-CURRENT"),
            self.result("RR-C", "TP-CURRENT"),
        ]
        resolution = self.resolution()
        with mock.patch.object(results, "iter_results", return_value=values), mock.patch.object(
            results, "result_set_resolutions", return_value={("RS-T", "TP-CURRENT"): resolution}
        ):
            state = results.task_result_state("RS-T", publication_id="TP-CURRENT")
        self.assertEqual("PARALLEL_RESULTS_AWAITING_RECONCILIATION", state["parallel_state"])
        self.assertFalse(state["terminal"])
        self.assertIn("stale", state["reconciliation_reason"])

    def test_multiple_driver_reviews_require_explicit_review_binding(self):
        only = self.result("RR-A", "TP-CURRENT")
        reviews = [
            self.review("RR-A", "RV-1", "ACCEPTED"),
            self.review("RR-A", "RV-2", "REQUEST_REVISION"),
        ]
        with mock.patch.object(results, "iter_results", return_value=[only]), mock.patch.object(
            results, "result_set_resolutions", return_value={}
        ), mock.patch.object(results, "reviews_for_result", return_value=reviews):
            state = results.task_result_state("RS-T", publication_id="TP-CURRENT")
        self.assertEqual("AWAITING_DRIVER_REVIEW", state["state"])
        self.assertEqual("PARALLEL_REVIEWS_AWAITING_RECONCILIATION", state["parallel_review_state"])
        self.assertFalse(state["terminal"])
        self.assertIsNone(state["review"])


class ExecutionGenerationAuditTests(unittest.TestCase):
    def publication(self, publication_id, blob):
        return {
            "record_schema": "ENTERPRISE_MATH_TASK_PUBLICATION_RECORD_V2",
            "record_state": "ACTIVE",
            "task_id": "RS-T",
            "publication_id": publication_id,
            "taskbook_path": "research_tasks/T.md",
            "taskbook_blob_sha1": blob,
        }

    def execution(self, publication_id, blob):
        return {
            "_record_path": "research_execution_records/RS-T/ER-T.json",
            "record_schema": executions.SCHEMA,
            "execution_record_id": "ER-T",
            "task_id": "RS-T",
            "publication_id": publication_id,
            "taskbook_path": "research_tasks/T.md",
            "taskbook_blob_sha1": blob,
            "claim_id": "claim-1",
            "researcher_id": "EM-T-ABC123",
            "theorem_owner": "THEOREM_T",
            "execution_branch": "research/t",
            "execution_branch_base": "a" * 40,
            "allowed_outputs": ["research_returns/T.md"],
        }

    def test_historical_execution_validates_against_its_own_publication_generation(self):
        old_blob = "sha1:" + "1" * 40
        new_blob = "sha1:" + "2" * 40
        pubs = [self.publication("TP-OLD", old_blob), self.publication("TP-NEW", new_blob)]
        with mock.patch.object(executions, "iter_records", return_value=[self.execution("TP-OLD", old_blob)]), mock.patch.object(
            executions.research_task_records, "iter_records", return_value=pubs
        ):
            self.assertEqual([], executions.audit())

    def test_execution_with_unknown_publication_generation_fails_closed(self):
        blob = "sha1:" + "1" * 40
        pubs = [self.publication("TP-NEW", "sha1:" + "2" * 40)]
        with mock.patch.object(executions, "iter_records", return_value=[self.execution("TP-MISSING", blob)]), mock.patch.object(
            executions.research_task_records, "iter_records", return_value=pubs
        ):
            errors = executions.audit()
        self.assertTrue(any("unknown publication generation" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
