import unittest
from unittest import mock

from tools import research_dispatch as rd
from tools import research_runtime_reducer as rr


PUB = "TP2-SCOPE-GUARD"
BASE_SHA = "1" * 40


def task():
    return {
        "task_id": "RS-SCOPE-GUARD",
        "title": "Registered HANDOFF scope guard",
        "kind": "RESEARCH",
        "owner": "taskbook/unassigned",
        "base_state": "READY",
        "priority": "P0",
        "leverage": "HIGH",
        "frontier": "scope",
        "next_action": "continue",
        "dependencies": [],
        "source_refs": [],
        "last_progress_at": "2026-09-07T02:17:00+00:00",
        "hard_block": None,
        "claim_lease_minutes": 10,
        "identity_lane": "SCOPE",
        "publication_id": PUB,
        "taskbook_blob_sha1": "2" * 40,
        "registration_source": "IMMUTABLE_TASK_RECORD",
    }


def meta(comment_id, at):
    return {
        "server_authenticated": True,
        "issue_number": 240,
        "comment_id": comment_id,
        "author_login": "awdawmip",
        "author_user_id": 30957095,
        "author_association": "OWNER",
        "control_authorized": True,
        "created_at": at,
        "updated_at": at,
        "edited": False,
    }


def event(kind, comment_id, at, **extra):
    value = {
        "schema": rr.EVENT_SCHEMA,
        "event": kind,
        "task_id": "RS-SCOPE-GUARD",
        "at": at,
        rd.GITHUB_META_KEY: meta(comment_id, at),
    }
    value.update(extra)
    return value


def claim(comment_id=1, at="2026-09-07T02:21:00+00:00", claim_id="c1"):
    return event(
        "CLAIM",
        comment_id,
        at,
        claim_id=claim_id,
        publication_id=PUB,
        theorem_owner="taskbook/unassigned",
        execution_branch=f"research/scope-{claim_id}",
        execution_branch_base=BASE_SHA,
        allowed_outputs=["tests/scope.txt"],
        lease_minutes=10,
    )


class RegisteredHandoffScopeGuardTests(unittest.TestCase):
    def reduce(self, events, now):
        with (
            mock.patch.object(rd.research_result_records, "task_result_state", return_value=None),
            mock.patch.object(rd.research_execution_records, "intent_for_claim", return_value=None),
            mock.patch.object(rd.research_cohort_runtime, "task_active_cohort_state", return_value=None),
        ):
            return rd.reduce_definition(task(), events, now=rr.parse_time(now))

    def test_post_cutover_unscoped_handoff_blocks_after_valid_claim_expires(self):
        state = self.reduce(
            [
                claim(),
                event(
                    "HANDOFF",
                    2,
                    "2026-09-07T02:22:00+00:00",
                    claim_id="c1",
                    next_action="ambiguous",
                ),
            ],
            "2026-09-07T02:40:00+00:00",
        )
        self.assertEqual("BLOCKED", state["state"])
        self.assertEqual("BLOCKED", state["dispatch_state"])
        self.assertEqual("REGISTERED_HANDOFF_SCOPE_REQUIRED", state["hard_block"]["code"])

    def test_post_cutover_unscoped_handoff_preserves_live_owner_before_expiry(self):
        state = self.reduce(
            [
                claim(),
                event(
                    "HANDOFF",
                    2,
                    "2026-09-07T02:22:00+00:00",
                    claim_id="c1",
                    next_action="ambiguous",
                ),
            ],
            "2026-09-07T02:25:00+00:00",
        )
        self.assertEqual("LEASED", state["dispatch_state"])
        self.assertEqual("c1", state["claim_id"])

    def test_explicit_continuation_remains_dispatchable(self):
        state = self.reduce(
            [
                claim(),
                event(
                    "HANDOFF",
                    2,
                    "2026-09-07T02:22:00+00:00",
                    claim_id="c1",
                    next_action="continue",
                    handoff_scope="CONTINUATION",
                ),
            ],
            "2026-09-07T02:25:00+00:00",
        )
        self.assertEqual("HANDOFF_READY", state["state"])
        self.assertEqual("NEEDS_DISPATCH", state["dispatch_state"])

    def test_explicit_frozen_return_waits_review(self):
        state = self.reduce(
            [
                claim(),
                event(
                    "HANDOFF",
                    2,
                    "2026-09-07T02:22:00+00:00",
                    claim_id="c1",
                    next_action="Driver review",
                    handoff_scope="FROZEN_RETURN_AWAITING_DRIVER_REVIEW",
                ),
            ],
            "2026-09-07T02:25:00+00:00",
        )
        self.assertEqual("FROZEN_RETURN", state["state"])
        self.assertEqual("AWAITING_REVIEW", state["dispatch_state"])

    def test_pre_cutover_plain_handoff_remains_legacy_compatible(self):
        state = self.reduce(
            [
                claim(at="2026-09-07T02:18:00+00:00"),
                event(
                    "HANDOFF",
                    2,
                    "2026-09-07T02:19:00+00:00",
                    claim_id="c1",
                    next_action="legacy continuation",
                ),
            ],
            "2026-09-07T02:19:30+00:00",
        )
        self.assertEqual("HANDOFF_READY", state["state"])
        self.assertEqual("NEEDS_DISPATCH", state["dispatch_state"])

    def test_scoped_correction_before_expiry_supersedes_ambiguous_handoff(self):
        state = self.reduce(
            [
                claim(),
                event(
                    "HANDOFF",
                    2,
                    "2026-09-07T02:22:00+00:00",
                    claim_id="c1",
                    next_action="ambiguous",
                ),
                event(
                    "HANDOFF",
                    3,
                    "2026-09-07T02:24:00+00:00",
                    claim_id="c1",
                    next_action="Driver review",
                    result_id="RR-CORRECTED",
                ),
            ],
            "2026-09-07T02:25:00+00:00",
        )
        self.assertEqual("FROZEN_RETURN", state["state"])
        self.assertEqual("AWAITING_REVIEW", state["dispatch_state"])
        self.assertEqual("RR-CORRECTED", state["result_id"])

    def test_wrong_claim_ambiguous_handoff_cannot_block_fresh_task(self):
        state = self.reduce(
            [
                claim(),
                event(
                    "HANDOFF",
                    2,
                    "2026-09-07T02:22:00+00:00",
                    claim_id="wrong",
                    next_action="must not block",
                ),
            ],
            "2026-09-07T02:40:00+00:00",
        )
        self.assertEqual("HANDOFF_READY", state["state"])
        self.assertEqual("NEEDS_DISPATCH", state["dispatch_state"])

    def test_unclaimed_ambiguous_handoff_cannot_block_fresh_task(self):
        state = self.reduce(
            [
                event(
                    "HANDOFF",
                    2,
                    "2026-09-07T02:22:00+00:00",
                    claim_id="ghost",
                    next_action="must not block",
                ),
            ],
            "2026-09-07T02:40:00+00:00",
        )
        self.assertEqual("READY", state["state"])
        self.assertEqual("NEEDS_DISPATCH", state["dispatch_state"])

    def test_invalid_scope_cannot_hide_behind_result_id(self):
        state = self.reduce(
            [
                claim(),
                event(
                    "HANDOFF",
                    2,
                    "2026-09-07T02:22:00+00:00",
                    claim_id="c1",
                    next_action="bad scope",
                    result_id="RR-X",
                    handoff_scope="NOT_A_SCOPE",
                ),
            ],
            "2026-09-07T02:40:00+00:00",
        )
        self.assertEqual("BLOCKED", state["dispatch_state"])
        self.assertEqual("REGISTERED_HANDOFF_SCOPE_REQUIRED", state["hard_block"]["code"])

    def test_continuation_scope_cannot_contradict_result_return(self):
        state = self.reduce(
            [
                claim(),
                event(
                    "HANDOFF",
                    2,
                    "2026-09-07T02:22:00+00:00",
                    claim_id="c1",
                    next_action="contradiction",
                    result_id="RR-X",
                    handoff_scope="CONTINUATION",
                ),
            ],
            "2026-09-07T02:40:00+00:00",
        )
        self.assertEqual("BLOCKED", state["dispatch_state"])
        self.assertEqual("REGISTERED_HANDOFF_SCOPE_REQUIRED", state["hard_block"]["code"])

    def test_wrong_claim_invalid_done_does_not_gain_blocking_authority(self):
        state = self.reduce(
            [
                claim(),
                event(
                    "DONE",
                    2,
                    "2026-09-07T02:22:00+00:00",
                    claim_id="wrong",
                    progress_ref="invalid terminal attempt",
                ),
            ],
            "2026-09-07T02:40:00+00:00",
        )
        self.assertEqual("HANDOFF_READY", state["state"])
        self.assertEqual("NEEDS_DISPATCH", state["dispatch_state"])

    def test_valid_claim_invalid_done_still_fails_closed(self):
        state = self.reduce(
            [
                claim(),
                event(
                    "DONE",
                    2,
                    "2026-09-07T02:22:00+00:00",
                    claim_id="c1",
                    progress_ref="invalid terminal attempt",
                ),
            ],
            "2026-09-07T02:40:00+00:00",
        )
        self.assertEqual("BLOCKED", state["dispatch_state"])
        self.assertEqual(
            "REGISTERED_DONE_REQUIRES_TERMINAL_DRIVER_REVIEW",
            state["hard_block"]["code"],
        )


if __name__ == "__main__":
    unittest.main()
