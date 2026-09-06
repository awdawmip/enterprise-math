from __future__ import annotations

import unittest
from pathlib import Path
from unittest import mock

from tools import research_dispatch as dispatch


class ReopenClaimOverlayTests(unittest.TestCase):
    def task(self) -> dict:
        return {
            "task_id": "RS-REOPEN",
            "publication_id": "TP2-REOPEN",
            "registration_source": "IMMUTABLE_TASK_RECORD",
        }

    def result_state(self) -> dict:
        return {
            "state": "RETURN_TO_EXECUTION",
            "terminal": False,
            "result": {
                "result_id": "RR-OLD",
                "_record_path": "research_result_records/RS-REOPEN/RR-OLD.json",
            },
            "review": {
                "review_id": "DR-REV",
                "reviewed_at": "2026-09-06T07:00:00+00:00",
                "disposition": "REQUEST_REVISION",
                "terminal": False,
            },
        }

    def test_live_post_review_claim_survives_return_to_execution_overlay(self) -> None:
        reduced = {
            "state": "CLAIMED",
            "dispatch_state": "LEASED",
            "claim_id": "claim-after-review",
            "actor": "ChatGPT TASK_RESEARCH",
            "researcher_id": "EM-TEST-ABC123",
            "identity_source": "CLAIM",
            "lease_until": "2026-09-07T07:10:00+00:00",
        }
        out = dispatch._overlay_result_state(
            self.task(), reduced, Path("."), self.result_state()
        )
        self.assertEqual("LEASED", out["dispatch_state"])
        self.assertEqual("CLAIMED", out["state"])
        self.assertEqual("claim-after-review", out["claim_id"])
        self.assertEqual("EM-TEST-ABC123", out["researcher_id"])
        self.assertEqual("2026-09-07T07:10:00+00:00", out["lease_until"])
        self.assertEqual("RR-OLD", out["result_id"])
        self.assertEqual("REQUEST_REVISION", out["driver_disposition"])

    def test_claimless_reopen_still_requests_fresh_owner(self) -> None:
        reduced = {
            "state": "BLOCKED",
            "dispatch_state": "BLOCKED",
            "claim_id": None,
            "actor": None,
            "researcher_id": None,
            "identity_source": None,
            "lease_until": None,
        }
        out = dispatch._overlay_result_state(
            self.task(), reduced, Path("."), self.result_state()
        )
        self.assertEqual("HANDOFF_READY", out["state"])
        self.assertEqual("NEEDS_DISPATCH", out["dispatch_state"])
        self.assertIsNone(out["claim_id"])
        self.assertEqual("REQUEST_REVISION", out["driver_disposition"])

    def test_three_argument_registered_event_filter_loads_result_lifecycle(self) -> None:
        task = self.task()
        with mock.patch.object(
            dispatch._core.research_result_records,
            "task_result_state",
            return_value=None,
        ) as lifecycle:
            accepted, rejected = dispatch._filter_registered_events(task, [], Path("."))
        self.assertEqual([], accepted)
        self.assertEqual([], rejected)
        lifecycle.assert_called_once_with("RS-REOPEN", Path("."), "TP2-REOPEN")


if __name__ == "__main__":
    unittest.main()
