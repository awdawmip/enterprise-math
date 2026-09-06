import unittest
from unittest import mock

from tools import research_dispatch as rd
from tools import research_runtime_reducer as rr


CURRENT_PUBLICATION = "TP2-CURRENT"
OLD_PUBLICATION = "TP2-OLD"
BASE_SHA = "1" * 40


def task(*, base_state="READY", hard_block=None):
    return {
        "task_id": "RS-SIM-CONTROL",
        "title": "Synthetic control-plane simulation",
        "kind": "RESEARCH",
        "owner": "taskbook/unassigned",
        "base_state": base_state,
        "priority": "P0",
        "leverage": "HIGH",
        "frontier": "simulation",
        "next_action": "continue",
        "dependencies": [],
        "source_refs": [],
        "last_progress_at": "2026-09-01T00:00:00+00:00",
        "hard_block": hard_block,
        "claim_lease_minutes": 10,
        "identity_lane": "SIM",
        "publication_id": CURRENT_PUBLICATION,
        "taskbook_blob_sha1": "2" * 40,
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
        "task_id": "RS-SIM-CONTROL",
        "at": at,
        rd.GITHUB_META_KEY: meta(comment_id, at),
    }
    value.update(extra)
    return value


def claim(comment_id=1, at="2026-09-01T00:00:00+00:00", claim_id="c1"):
    return event(
        "CLAIM",
        comment_id,
        at,
        claim_id=claim_id,
        publication_id=CURRENT_PUBLICATION,
        theorem_owner="taskbook/unassigned",
        execution_branch=f"research/sim-{claim_id}",
        execution_branch_base=BASE_SHA,
        allowed_outputs=["tests/sim.txt"],
        lease_minutes=10,
    )


class ControlPlaneAdversarialSimulation(unittest.TestCase):
    def reduce(self, definition, events, now):
        with (
            mock.patch.object(rd.research_result_records, "task_result_state", return_value=None),
            mock.patch.object(rd.research_execution_records, "intent_for_claim", return_value=None),
            mock.patch.object(rd.research_cohort_runtime, "task_active_cohort_state", return_value=None),
        ):
            return rd.reduce_definition(definition, events, now=rr.parse_time(now))

    def test_invalid_done_without_later_recovery_fails_closed(self):
        events = [
            claim(),
            event(
                "DONE",
                2,
                "2026-09-01T00:01:00+00:00",
                claim_id="c1",
                progress_ref="premature",
            ),
        ]
        state = self.reduce(task(), events, "2026-09-01T00:20:00+00:00")
        self.assertEqual("BLOCKED", state["dispatch_state"])
        self.assertEqual(
            "REGISTERED_DONE_REQUIRES_TERMINAL_DRIVER_REVIEW",
            state["hard_block"]["code"],
        )

    def test_invalid_done_does_not_resurrect_after_later_valid_progress_and_expiry(self):
        events = [
            claim(),
            event(
                "DONE",
                2,
                "2026-09-01T00:01:00+00:00",
                claim_id="c1",
                progress_ref="premature",
            ),
            event(
                "PROGRESS",
                3,
                "2026-09-01T00:02:00+00:00",
                claim_id="c1",
                progress_ref="continued-after-correction",
                next_action="continue",
                lease_minutes=10,
            ),
        ]
        state = self.reduce(task(), events, "2026-09-01T00:20:00+00:00")
        self.assertEqual("HANDOFF_READY", state["state"])
        self.assertEqual("NEEDS_DISPATCH", state["dispatch_state"])

    def test_mismatched_publication_supercede_cannot_close_current_generation(self):
        events = [
            event(
                "SUPERSEDE",
                10,
                "2026-09-01T00:03:00+00:00",
                publication_id=OLD_PUBLICATION,
                next_action="old generation only",
            )
        ]
        state = self.reduce(task(), events, "2026-09-01T00:04:00+00:00")
        self.assertEqual("READY", state["state"])
        self.assertEqual("NEEDS_DISPATCH", state["dispatch_state"])
        self.assertTrue(any("publication_id" in x["reason"] for x in state["ignored_events"]))

    def test_post_cutover_publicationless_supercede_fails_closed(self):
        events = [
            event(
                "SUPERSEDE",
                11,
                "2026-09-01T00:03:00+00:00",
                next_action="unbound mutation",
            )
        ]
        state = self.reduce(task(), events, "2026-09-01T00:04:00+00:00")
        self.assertEqual("READY", state["state"])
        self.assertEqual("NEEDS_DISPATCH", state["dispatch_state"])
        self.assertTrue(any("publication_id" in x["reason"] for x in state["ignored_events"]))

    def test_current_publication_supercede_remains_authoritative(self):
        events = [
            event(
                "SUPERSEDE",
                12,
                "2026-09-01T00:03:00+00:00",
                publication_id=CURRENT_PUBLICATION,
                next_action="superseded correctly",
            )
        ]
        state = self.reduce(task(), events, "2026-09-01T00:04:00+00:00")
        self.assertEqual("SUPERSEDED", state["state"])
        self.assertEqual("COMPLETE", state["dispatch_state"])

    def test_mismatched_publication_unblock_cannot_reopen_current_generation(self):
        block = {
            "missing_object": "x",
            "owner": "y",
            "necessity": "z",
            "unblock_condition": "w",
        }
        events = [
            event(
                "UNBLOCK",
                13,
                "2026-09-01T00:03:00+00:00",
                publication_id=OLD_PUBLICATION,
                next_action="old generation unblock",
            )
        ]
        state = self.reduce(task(base_state="BLOCKED", hard_block=block), events, "2026-09-01T00:04:00+00:00")
        self.assertEqual("BLOCKED", state["state"])
        self.assertEqual("BLOCKED", state["dispatch_state"])

    def test_claim_bound_progress_may_omit_publication_id_after_bound_claim(self):
        events = [
            claim(),
            event(
                "PROGRESS",
                2,
                "2026-09-01T00:01:00+00:00",
                claim_id="c1",
                progress_ref="bound by live claim",
                next_action="continue",
                lease_minutes=10,
            ),
        ]
        state = self.reduce(task(), events, "2026-09-01T00:02:00+00:00")
        self.assertEqual("IN_PROGRESS", state["state"])
        self.assertEqual("LEASED", state["dispatch_state"])


if __name__ == "__main__":
    unittest.main()
