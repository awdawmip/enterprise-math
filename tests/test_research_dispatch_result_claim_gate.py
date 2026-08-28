import unittest
from pathlib import Path
from unittest import mock

from tools import research_dispatch as dispatch


ROOT = Path(__file__).resolve().parents[1]


def task():
    return {
        "task_id": "RS-LIFECYCLE-GATE-TEST",
        "registration_source": "IMMUTABLE_TASK_RECORD",
        "publication_id": "TP2-LIFECYCLEGATE000001",
        "claim_lease_minutes": 120,
    }


def claim(created_at, *, declared_at="1900-01-01T00:00:00+00:00", claim_id="claim-1"):
    return {
        "schema": dispatch.EVENT_SCHEMA,
        "event": "CLAIM",
        "task_id": "RS-LIFECYCLE-GATE-TEST",
        "claim_id": claim_id,
        "publication_id": "TP2-LIFECYCLEGATE000001",
        "at": declared_at,
        "theorem_owner": "LIFECYCLE_GATE",
        "execution_branch": "research/lifecycle-gate-test",
        "execution_branch_base": "a" * 40,
        "allowed_outputs": ["research_returns/"],
        "_github": {
            "server_authenticated": True,
            "issue_number": 240,
            "comment_id": 1,
            "control_authorized": True,
            "created_at": created_at,
            "updated_at": created_at,
            "edited": False,
        },
    }


def state(kind, *, reviewed_at=None):
    review = None
    terminal = False
    if kind == "TERMINAL":
        terminal = True
        review = {
            "review_id": "DR-TERMINAL",
            "disposition": "ACCEPTED",
            "reviewed_at": reviewed_at or "2026-08-27T10:10:00+00:00",
        }
    elif kind == "RETURN_TO_EXECUTION":
        review = {
            "review_id": "DR-RETURN",
            "disposition": "RETURN_TO_EXECUTION",
            "reviewed_at": reviewed_at or "2026-08-27T10:10:00+00:00",
        }
    return {
        "state": kind,
        "result": {
            "result_id": "RR-LIFECYCLE",
            "frozen_at": "2026-08-27T10:00:00+00:00",
        },
        "review": review,
        "terminal": terminal,
    }


class RegisteredResultClaimGateTests(unittest.TestCase):
    def _filter(self, event, result_state):
        intent = {
            "researcher_id": "EM-LIFE-ABC123",
            "owner_lease_minutes": 120,
        }
        with mock.patch.object(
            dispatch.research_result_records, "task_result_state", return_value=result_state
        ), mock.patch.object(
            dispatch.research_result_records, "iter_results", return_value=[]
        ), mock.patch.object(
            dispatch.research_execution_records, "intent_for_claim", return_value=intent
        ):
            return dispatch._filter_registered_events(task(), [event], ROOT)

    def test_historical_claim_before_result_freeze_is_preserved(self):
        accepted, rejected = self._filter(
            claim("2026-08-27T09:59:59+00:00"), state("AWAITING_DRIVER_REVIEW")
        )
        self.assertEqual(1, len(accepted))
        self.assertEqual([], rejected)

    def test_claim_after_freeze_is_rejected_while_awaiting_driver_review(self):
        accepted, rejected = self._filter(
            claim("2026-08-27T10:00:01+00:00"), state("AWAITING_DRIVER_REVIEW")
        )
        self.assertEqual([], accepted)
        self.assertIn("Driver review is pending", rejected[0]["reason"])

    def test_claim_after_freeze_is_rejected_after_terminal_review(self):
        accepted, rejected = self._filter(
            claim("2026-08-27T11:00:00+00:00"), state("TERMINAL")
        )
        self.assertEqual([], accepted)
        self.assertIn("task is terminal", rejected[0]["reason"])

    def test_nonterminal_driver_review_reopens_only_at_reviewed_at(self):
        frozen_interval, rejected_before = self._filter(
            claim("2026-08-27T10:05:00+00:00", claim_id="before-reopen"),
            state("RETURN_TO_EXECUTION", reviewed_at="2026-08-27T10:10:00+00:00"),
        )
        reopened, rejected_after = self._filter(
            claim("2026-08-27T10:10:01+00:00", claim_id="after-reopen"),
            state("RETURN_TO_EXECUTION", reviewed_at="2026-08-27T10:10:00+00:00"),
        )
        self.assertEqual([], frozen_interval)
        self.assertIn("before the authoritative", rejected_before[0]["reason"])
        self.assertEqual(1, len(reopened))
        self.assertEqual([], rejected_after)

    def test_body_declared_clock_cannot_backdate_past_server_created_at(self):
        accepted, rejected = self._filter(
            claim(
                "2026-08-27T10:00:01+00:00",
                declared_at="1900-01-01T00:00:00+00:00",
            ),
            state("AWAITING_DRIVER_REVIEW"),
        )
        self.assertEqual([], accepted)
        self.assertIn("Driver review is pending", rejected[0]["reason"])

    def test_parallel_synthetic_result_recovers_latest_component_freeze(self):
        result_state = {
            "state": "AWAITING_DRIVER_REVIEW",
            "result": {
                "result_id": "PI-1",
                "parallel_result_ids": ["RR-A", "RR-B"],
            },
            "review": None,
            "terminal": False,
            "parallel_result_ids": ["RR-A", "RR-B"],
        }
        records = [
            {"result_id": "RR-A", "frozen_at": "2026-08-27T09:00:00+00:00"},
            {"result_id": "RR-B", "frozen_at": "2026-08-27T10:00:00+00:00"},
        ]
        with mock.patch.object(
            dispatch.research_result_records, "iter_results", return_value=records
        ):
            reason = dispatch._claim_result_gate_reason(
                claim("2026-08-27T10:00:01+00:00"), result_state, ROOT
            )
        self.assertIn("Driver review is pending", reason)


if __name__ == "__main__":
    unittest.main()
