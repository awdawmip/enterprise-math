import unittest
from unittest import mock

from tools import research_execution_records as executions
from tools import research_result_records as results


class ResultGenerationStateTests(unittest.TestCase):
    def result(self, rid, publication_id, frozen_at):
        return {
            "result_id": rid,
            "task_id": "RS-T",
            "publication_id": publication_id,
            "frozen_at": frozen_at,
        }

    def review(self, rid, disposition="ACCEPTED"):
        return {
            "review_id": "RV-" + rid,
            "result_id": rid,
            "disposition": disposition,
        }

    def test_old_terminal_result_does_not_close_new_current_generation(self):
        old = self.result("RR-OLD", "TP-OLD", "2026-08-26T01:00:00+00:00")
        with mock.patch.object(results, "iter_results", return_value=[old]), mock.patch.object(
            results.research_task_records,
            "current_records",
            return_value={"RS-T": {"publication_id": "TP-NEW"}},
        ), mock.patch.object(results, "latest_review", return_value=self.review("RR-OLD")):
            self.assertIsNone(results.task_result_state("RS-T"))

    def test_current_generation_result_controls_current_state(self):
        old = self.result("RR-OLD", "TP-OLD", "2026-08-26T01:00:00+00:00")
        new = self.result("RR-NEW", "TP-NEW", "2026-08-26T02:00:00+00:00")
        with mock.patch.object(results, "iter_results", return_value=[old, new]), mock.patch.object(
            results.research_task_records,
            "current_records",
            return_value={"RS-T": {"publication_id": "TP-NEW"}},
        ), mock.patch.object(results, "latest_review", side_effect=lambda rid, root=results.ROOT: None if rid == "RR-NEW" else self.review(rid)):
            state = results.task_result_state("RS-T")
        self.assertEqual("AWAITING_DRIVER_REVIEW", state["state"])
        self.assertEqual("RR-NEW", state["result"]["result_id"])

    def test_explicit_historical_generation_remains_queryable(self):
        old = self.result("RR-OLD", "TP-OLD", "2026-08-26T01:00:00+00:00")
        new = self.result("RR-NEW", "TP-NEW", "2026-08-26T02:00:00+00:00")
        with mock.patch.object(results, "iter_results", return_value=[old, new]), mock.patch.object(
            results, "latest_review", return_value=self.review("RR-OLD")
        ):
            state = results.task_result_state("RS-T", publication_id="TP-OLD")
        self.assertEqual("TERMINAL", state["state"])
        self.assertEqual("RR-OLD", state["result"]["result_id"])


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
