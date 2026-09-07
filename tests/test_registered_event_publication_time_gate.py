import unittest
from pathlib import Path
from unittest import mock

from tools import research_dispatch as rd
from tools import research_runtime_reducer as rr


TASK_ID = "RS-PUBTIME-SIM"
PUBLICATION = "TP2-PUBTIME-CURRENT"
PUBLISHED_AT = "2026-09-01T10:00:00+00:00"
BASE_SHA = "1" * 40


def task(*, base_state="READY"):
    return {
        "task_id": TASK_ID,
        "title": "Synthetic publication event causality",
        "kind": "RESEARCH",
        "owner": "taskbook/unassigned",
        "base_state": base_state,
        "priority": "P0",
        "leverage": "HIGH",
        "frontier": "simulation",
        "next_action": "continue",
        "dependencies": [],
        "source_refs": [],
        "last_progress_at": PUBLISHED_AT,
        "hard_block": {
            "missing_object": "x",
            "owner": "y",
            "necessity": "z",
            "unblock_condition": "w",
        } if base_state == "BLOCKED" else None,
        "claim_lease_minutes": 30,
        "identity_lane": "PUBTIME",
        "publication_id": PUBLICATION,
        "publication_published_at": PUBLISHED_AT,
        "taskbook_blob_sha1": "sha1:" + "2" * 40,
        "registration_source": "IMMUTABLE_TASK_RECORD",
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


def claim(comment_id, at):
    return event(
        "CLAIM",
        comment_id,
        at,
        claim_id=f"claim-{comment_id}",
        publication_id=PUBLICATION,
        theorem_owner="taskbook/unassigned",
        execution_branch=f"research/pubtime-{comment_id}",
        execution_branch_base=BASE_SHA,
        allowed_outputs=["tests/pubtime.txt"],
        lease_minutes=30,
    )


class RegisteredEventPublicationTimeGateTests(unittest.TestCase):
    def reduce(self, definition, events, now="2026-09-01T10:02:00+00:00"):
        with (
            mock.patch.object(rd.research_result_records, "task_result_state", return_value=None),
            mock.patch.object(rd.research_result_records, "iter_results", return_value=[]),
            mock.patch.object(rd.research_execution_records, "intent_for_claim", return_value=None),
            mock.patch.object(rd.research_cohort_runtime, "task_active_cohort_state", return_value=None),
        ):
            return rd.reduce_definition(
                definition, events, now=rr.parse_time(now), root=Path(".")
            )

    def test_claim_created_before_publication_cannot_be_retroactively_accepted(self):
        state = self.reduce(task(), [claim(1, "2026-09-01T09:59:59+00:00")])
        self.assertEqual("READY", state["state"])
        self.assertEqual("NEEDS_DISPATCH", state["dispatch_state"])
        self.assertTrue(any("predates current task publication" in item["reason"] for item in state["ignored_events"]))

    def test_claim_at_publication_boundary_is_allowed(self):
        state = self.reduce(task(), [claim(2, PUBLISHED_AT)], now="2026-09-01T10:01:00+00:00")
        self.assertEqual("CLAIMED", state["state"])
        self.assertEqual("LEASED", state["dispatch_state"])

    def test_claim_after_publication_is_allowed(self):
        state = self.reduce(task(), [claim(3, "2026-09-01T10:00:01+00:00")])
        self.assertEqual("CLAIMED", state["state"])
        self.assertEqual("LEASED", state["dispatch_state"])

    def test_current_generation_supersede_before_publication_is_rejected(self):
        state = self.reduce(
            task(),
            [
                event(
                    "SUPERSEDE",
                    4,
                    "2026-09-01T09:59:59+00:00",
                    publication_id=PUBLICATION,
                    next_action="future generation placeholder",
                )
            ],
        )
        self.assertEqual("READY", state["state"])
        self.assertEqual("NEEDS_DISPATCH", state["dispatch_state"])

    def test_current_generation_unblock_before_publication_is_rejected(self):
        state = self.reduce(
            task(base_state="BLOCKED"),
            [
                event(
                    "UNBLOCK",
                    5,
                    "2026-09-01T09:59:59+00:00",
                    publication_id=PUBLICATION,
                    next_action="future generation placeholder",
                )
            ],
        )
        self.assertEqual("BLOCKED", state["state"])
        self.assertEqual("BLOCKED", state["dispatch_state"])

    def test_pre_cutover_publicationless_legacy_supersede_remains_compatible(self):
        state = self.reduce(
            task(),
            [
                event(
                    "SUPERSEDE",
                    6,
                    "2026-08-27T23:59:00+00:00",
                    next_action="legacy replay",
                )
            ],
        )
        self.assertEqual("SUPERSEDED", state["state"])
        self.assertEqual("COMPLETE", state["dispatch_state"])

    def test_registered_definition_propagates_publication_timestamp(self):
        record = {
            "task_id": TASK_ID,
            "publication_id": PUBLICATION,
            "published_at": PUBLISHED_AT,
            "taskbook_path": "unused.md",
            "taskbook_blob_sha1": "sha1:" + "2" * 40,
            "record_state": "ACTIVE",
            "claimable": True,
            "kind": "RESEARCH",
            "owner": "taskbook/unassigned",
            "frontier": "simulation",
            "next_action": "continue",
        }
        meta_value = {
            "task_id": TASK_ID,
            "title": "Synthetic",
            "base_state": "READY",
            "priority": "P0",
            "leverage": "HIGH",
            "frontier": "simulation",
            "next_action": "continue",
            "dependencies": [],
            "source_refs": [],
        }
        with mock.patch.object(rd, "_parse_taskbook", return_value=meta_value):
            definition = rd.registered_definition(record, Path("."))
        self.assertEqual(PUBLISHED_AT, definition["publication_published_at"])


if __name__ == "__main__":
    unittest.main()
