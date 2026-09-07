import unittest
from unittest import mock

from tools import research_dispatch as rd
from tools import research_runtime_reducer as rr


TASK_ID = "RS-REOPEN-SIM"
PUBLICATION = "TP2-REOPEN-CURRENT"
BASE_SHA = "1" * 40


def task():
    return {
        "task_id": TASK_ID,
        "title": "Synthetic result reopen precedence",
        "kind": "RESEARCH",
        "owner": "taskbook/unassigned",
        "base_state": "READY",
        "priority": "P0",
        "leverage": "HIGH",
        "frontier": "simulation",
        "next_action": "continue",
        "dependencies": [],
        "source_refs": [],
        "last_progress_at": "2026-09-01T00:00:00+00:00",
        "hard_block": None,
        "claim_lease_minutes": 30,
        "identity_lane": "REOPEN",
        "publication_id": PUBLICATION,
        "taskbook_blob_sha1": "2" * 40,
        "registration_source": "IMMUTABLE_TASK_RECORD",
    }


def result_state():
    return {
        "state": "RETURN_TO_EXECUTION",
        "terminal": False,
        "result": {
            "result_id": "RR-R1",
            "frozen_at": "2026-09-01T00:05:00+00:00",
            "_record_path": "research_result_records/sim/RR-R1.json",
        },
        "review": {
            "review_id": "DRV-R1",
            "disposition": "REQUEST_REVISION",
            "reviewed_at": "2026-09-01T00:10:00+00:00",
        },
    }


def meta(comment_id, created_at):
    return {
        "server_authenticated": True,
        "issue_number": 240,
        "comment_id": comment_id,
        "author_login": "awdawmip",
        "author_user_id": 30957095,
        "author_association": "OWNER",
        "control_authorized": True,
        "created_at": created_at,
        "updated_at": created_at,
        "edited": False,
    }


def event(kind, comment_id, at, **extra):
    value = {
        "schema": rr.EVENT_SCHEMA,
        "event": kind,
        "task_id": TASK_ID,
        "at": at,
        rd.GITHUB_META_KEY: meta(comment_id, at),
    }
    value.update(extra)
    return value


def claim(comment_id, at, claim_id="c2"):
    return event(
        "CLAIM",
        comment_id,
        at,
        claim_id=claim_id,
        publication_id=PUBLICATION,
        theorem_owner="taskbook/unassigned",
        execution_branch=f"research/reopen-{claim_id}",
        execution_branch_base=BASE_SHA,
        allowed_outputs=["tests/reopen.txt"],
        lease_minutes=30,
    )


def hard_block():
    return {
        "missing_object": "new revision dependency",
        "owner": "revision owner",
        "necessity": "required before revision can continue",
        "unblock_condition": "dependency becomes available",
    }


class ResultReopenRuntimePrecedenceTests(unittest.TestCase):
    def reduce(self, events, now="2026-09-01T00:13:00+00:00"):
        with (
            mock.patch.object(rd.research_result_records, "task_result_state", return_value=result_state()),
            mock.patch.object(rd.research_result_records, "iter_results", return_value=[]),
            mock.patch.object(rd.research_execution_records, "intent_for_claim", return_value=None),
            mock.patch.object(rd.research_cohort_runtime, "task_active_cohort_state", return_value=None),
        ):
            return rd.reduce_definition(task(), events, now=rr.parse_time(now))

    def test_old_review_reopens_historical_return_when_no_post_review_execution_exists(self):
        state = self.reduce(
            [
                claim(1, "2026-09-01T00:01:00+00:00", "c1"),
                event(
                    "HANDOFF",
                    2,
                    "2026-09-01T00:04:00+00:00",
                    claim_id="c1",
                    result_id="RR-R1",
                    next_action="Driver review R1",
                ),
            ]
        )
        self.assertEqual("HANDOFF_READY", state["state"])
        self.assertEqual("NEEDS_DISPATCH", state["dispatch_state"])
        self.assertEqual("RR-R1", state["result_id"])
        self.assertEqual("REQUEST_REVISION", state["driver_disposition"])

    def test_post_review_result_handoff_is_not_reopened_by_old_result(self):
        state = self.reduce(
            [
                claim(10, "2026-09-01T00:11:00+00:00"),
                event(
                    "HANDOFF",
                    11,
                    "2026-09-01T00:12:00+00:00",
                    claim_id="c2",
                    result_id="RR-R2",
                    next_action="Driver review R2",
                ),
            ]
        )
        self.assertEqual("FROZEN_RETURN", state["state"])
        self.assertEqual("AWAITING_REVIEW", state["dispatch_state"])
        self.assertEqual("RR-R2", state["result_id"])

    def test_post_review_hard_block_is_not_erased_by_old_result(self):
        state = self.reduce(
            [
                claim(20, "2026-09-01T00:11:00+00:00"),
                event(
                    "HARD_BLOCK",
                    21,
                    "2026-09-01T00:12:00+00:00",
                    claim_id="c2",
                    hard_block=hard_block(),
                    progress_ref="revision blocked",
                ),
            ]
        )
        self.assertEqual("BLOCKED", state["state"])
        self.assertEqual("BLOCKED", state["dispatch_state"])
        self.assertEqual("new revision dependency", state["hard_block"]["missing_object"])

    def test_post_review_current_generation_supersede_is_not_erased_by_old_result(self):
        state = self.reduce(
            [
                event(
                    "SUPERSEDE",
                    30,
                    "2026-09-01T00:12:00+00:00",
                    publication_id=PUBLICATION,
                    next_action="replacement generation published",
                )
            ]
        )
        self.assertEqual("SUPERSEDED", state["state"])
        self.assertEqual("COMPLETE", state["dispatch_state"])

    def test_ignored_post_review_wrong_claim_event_does_not_create_runtime_precedence(self):
        state = self.reduce(
            [
                claim(40, "2026-09-01T00:01:00+00:00", "c1"),
                event(
                    "HANDOFF",
                    41,
                    "2026-09-01T00:04:00+00:00",
                    claim_id="c1",
                    result_id="RR-R1",
                    next_action="Driver review R1",
                ),
                event(
                    "PROGRESS",
                    42,
                    "2026-09-01T00:12:00+00:00",
                    claim_id="not-live",
                    progress_ref="must remain ignored",
                    next_action="must not acquire precedence",
                    lease_minutes=30,
                ),
            ]
        )
        self.assertEqual("HANDOFF_READY", state["state"])
        self.assertEqual("NEEDS_DISPATCH", state["dispatch_state"])
        self.assertTrue(any("current live claim_id" in item["reason"] for item in state["ignored_events"]))


if __name__ == "__main__":
    unittest.main()
