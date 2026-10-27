"""Regression for a real posted RESUME rejected after nonterminal review.

The frozen fixture is five original GitHub server comment envelopes plus the
Source Result/Review view and intents, pinned at bfdeab630ff99aa8229c99f69e85ed522bc07b1d.
Repository lookups return those frozen inputs; parsing, authentication, lifecycle
filtering, intent binding, chronological reduction, CAS and live binding run as
production code. This does not exercise Native sessions or grant execution.
"""
from __future__ import annotations

import copy
from contextlib import ExitStack
import json
from pathlib import Path
import unittest
from unittest import mock

from control_plane import research_handoff_scope_runtime as scope
from control_plane import research_runtime_guard_core as guard
from tools import research_dispatch as dispatch
from tools import research_runtime_reducer as reducer

ROOT = Path(__file__).resolve().parents[1]
FIXTURE = json.loads((ROOT / "tests/fixtures/claim6077_actual_control.json").read_text())
TASK_ID = FIXTURE["task"]["task_id"]
NEW_CLAIM = FIXTURE["comments"][-1]["id"]


class ReviewedFrozenReturnResumeTests(unittest.TestCase):
    def setUp(self):
        self.task = copy.deepcopy(FIXTURE["task"])
        self.result = copy.deepcopy(FIXTURE["result_state"])
        self.events = dispatch.events_from_github_comments(
            copy.deepcopy(FIXTURE["comments"]), root=ROOT)
        self.now = reducer.parse_time(FIXTURE["observed_at"])
        self.intents = {x["claim_id"]: copy.deepcopy(x)
                        for x in FIXTURE["execution_intents"]}
        stack = self.enterContext(ExitStack())
        stack.enter_context(mock.patch.object(
            dispatch.research_result_records, "task_result_state",
            side_effect=lambda *a, **k: self.result))
        stack.enter_context(mock.patch.object(
            dispatch.research_result_records, "iter_results",
            side_effect=lambda *a, **k: [self.result["result"]] if self.result else []))
        stack.enter_context(mock.patch.object(
            dispatch.research_execution_records, "intent_for_claim",
            side_effect=lambda task, claim, root: self.intents.get(claim)))
        stack.enter_context(mock.patch.object(
            dispatch.research_cohort_runtime, "task_active_cohort_state",
            return_value=None))
        stack.enter_context(mock.patch.object(
            guard, "_registered_definition", side_effect=lambda *a: self.task))
        # This is the same existing adapter installed by canonical bootstrap.
        scope.install(ROOT)

    def reduce(self, events=None):
        return dispatch.reduce_definition(self.task,
            self.events if events is None else events, now=self.now, root=ROOT)

    def binding(self, events=None):
        return guard.canonical_live_claim_binding(TASK_ID,
            self.events if events is None else events, now=self.now, root=ROOT)

    def assert_new_claim_rejected(self):
        state = self.reduce()
        self.assertNotEqual(self.events[-1]["claim_id"], state.get("claim_id"))
        with self.assertRaises(guard.RuntimeAuthorizationError):
            self.binding()
        return state

    def test_actual_five_events_keep_dispatch_and_guard_on_one_winner(self):
        state = self.reduce()
        binding = self.binding()
        new = self.events[-1]
        self.assertEqual([5710114816, 5715323149, 5744808484,
                          5745200026, 6204642392],
                         [e["_github"]["comment_id"] for e in self.events])
        self.assertEqual("LEASED", state["dispatch_state"])
        self.assertEqual([], state["ignored_events"])
        self.assertEqual(new["claim_id"], state["claim_id"])
        self.assertEqual(new["claim_id"], binding["claim_id"])
        self.assertEqual(NEW_CLAIM, binding["server_comment_id"])
        self.assertEqual(new["session_id"], binding["session_id"])
        self.assertEqual(new["researcher_id"], binding["researcher_id"])
        self.assertEqual(new["publication_id"], binding["publication_id"])
        self.assertEqual(new["continuation"], binding["continuation"])

    def test_without_adapter_the_real_frozen_state_is_still_not_dispatchable(self):
        authenticated, _ = dispatch._event_authentication_filter(self.task, self.events)
        filtered, _ = dispatch._filter_registered_events(
            self.task, authenticated, ROOT, self.result)
        state = reducer.reduce_task(self.task, filtered,
            default_lease_minutes=180, now=self.now)
        self.assertEqual("FROZEN_RETURN", state["state"])
        self.assertEqual("RESUME requires a released or expired predecessor claim",
                         state["ignored_events"][-1]["reason"])

    def test_no_claim_is_manufactured_from_review_alone(self):
        state = self.reduce(self.events[:-1])
        self.assertEqual("NEEDS_DISPATCH", state["dispatch_state"])
        self.assertIsNone(state["claim_id"])
        with self.assertRaises(guard.RuntimeAuthorizationError):
            self.binding(self.events[:-1])

    def test_unreviewed_frozen_return_stays_closed(self):
        self.result.update(state="AWAITING_DRIVER_REVIEW", review=None)
        state = self.assert_new_claim_rejected()
        self.assertEqual("AWAITING_REVIEW", state["dispatch_state"])

    def test_terminal_accepted_review_does_not_reopen(self):
        self.result.update(state="TERMINAL", terminal=True)
        self.result["review"].update(disposition="ACCEPTED", terminal=True)
        state = self.assert_new_claim_rejected()
        self.assertEqual("COMPLETE", state["dispatch_state"])

    def test_result_control_withheld_does_not_reopen(self):
        self.result.update(state="RESULT_CONTROL_AUTHORITY_WITHHELD")
        self.assert_new_claim_rejected()

    def test_different_frozen_result_is_not_reopened_by_old_review(self):
        self.events[-2]["result_id"] = "RR-UNREVIEWED-OTHER"
        self.assert_new_claim_rejected()

    def test_missing_reviewed_result_binding_is_not_frozen_reopen_authority(self):
        self.result["result"].pop("result_id")
        self.assert_new_claim_rejected()

    def test_reviewed_result_from_another_task_or_publication_is_not_authority(self):
        for key, value in (("task_id", "RS-OTHER"), ("publication_id", "TP2-OTHER")):
            with self.subTest(key=key):
                original = self.result["result"][key]
                self.result["result"][key] = value
                self.assert_new_claim_rejected()
                self.result["result"][key] = original

    def test_claim_before_review_is_rejected(self):
        self.result["review"]["reviewed_at"] = "2026-10-16T00:00:00+00:00"
        self.assert_new_claim_rejected()

    def test_stale_predecessor_claim_cas_is_rejected(self):
        self.events[-1]["continuation"]["expected_previous_claim_id"] = "stale"
        self.assert_new_claim_rejected()

    def test_stale_predecessor_comment_cas_is_rejected(self):
        self.events[-1]["continuation"]["expected_previous_comment_id"] -= 1
        self.assert_new_claim_rejected()

    def test_wrong_predecessor_identity_is_rejected(self):
        self.events[-1]["continuation"]["previous_researcher_id"] = "EM-T6-ABC123"
        self.assert_new_claim_rejected()

    def test_wrong_publication_is_rejected(self):
        self.events[-1]["publication_id"] = "TP2-WRONG"
        self.assert_new_claim_rejected()

    def test_edited_or_unauthorized_successor_is_rejected(self):
        for key, value in (("edited", True), ("control_authorized", False)):
            with self.subTest(key=key):
                self.events[-1]["_github"][key] = value
                self.assert_new_claim_rejected()
                self.events[-1]["_github"][key] = not value

    def test_expired_new_claim_is_not_execution_authority(self):
        self.now = reducer.parse_time("2026-10-16T02:00:00+00:00")
        with self.assertRaises(guard.RuntimeAuthorizationError):
            self.binding()

    def test_live_predecessor_lease_cannot_be_preempted_by_resume(self):
        # Use the real predecessor envelope at a later synthetic server time,
        # without its historical HANDOFF. The review does not release a lease.
        old = copy.deepcopy(self.events[-3])
        old["at"] = "2026-10-15T23:44:00+00:00"
        old["_github"].update(comment_id=NEW_CLAIM - 1,
            created_at=old["at"], updated_at=old["at"])
        self.events[-1]["continuation"]["expected_previous_comment_id"] = NEW_CLAIM - 1
        self.events = [old, self.events[-1]]
        state = self.reduce()
        self.assertEqual(old["claim_id"], state["claim_id"])
        self.assertEqual(old["claim_id"], self.binding()["claim_id"])
        self.assertIn("RESUME requires a released or expired predecessor claim",
                      str(state["ignored_events"]))

    def test_review_edge_cannot_reopen_a_later_frozen_return(self):
        first = self.events[-1]
        handoff = copy.deepcopy(self.events[-2])
        handoff.update(claim_id=first["claim_id"],
            researcher_id=first["researcher_id"], result_id="RR-NEW-UNREVIEWED",
            at="2026-10-15T23:46:00+00:00")
        handoff["_github"].update(comment_id=NEW_CLAIM + 1,
            created_at=handoff["at"], updated_at=handoff["at"])
        another = copy.deepcopy(first)
        another.update(claim_id="fresh-after-unreviewed",
            at="2026-10-15T23:47:00+00:00")
        another["_github"].update(comment_id=NEW_CLAIM + 2,
            created_at=another["at"], updated_at=another["at"])
        another["continuation"].update(
            expected_previous_claim_id=first["claim_id"],
            expected_previous_comment_id=NEW_CLAIM,
            previous_researcher_id=first["researcher_id"])
        self.events += [handoff, another]
        state = self.assert_new_claim_rejected()
        self.assertEqual("FROZEN_RETURN", state["state"])
        self.assertEqual("RR-NEW-UNREVIEWED", state["result_id"])

    def test_competing_resume_uses_exact_winning_epoch(self):
        second = copy.deepcopy(self.events[-1])
        second.update(claim_id="competing-resume",
            at="2026-10-15T23:46:00+00:00")
        second["_github"].update(comment_id=NEW_CLAIM + 1,
            created_at=second["at"], updated_at=second["at"])
        first_claim = self.events[-1]["claim_id"]
        self.events.append(second)
        state = self.reduce()
        self.assertEqual(first_claim, state["claim_id"])
        self.assertEqual(first_claim, self.binding()["claim_id"])
        self.assertIn("continuation predecessor CLAIM CAS changed",
                      str(state["ignored_events"]))

    def test_caller_flags_cannot_forge_review_authority(self):
        self.result = None
        self.task[scope.REOPEN_KEY] = "2026-10-15T00:00:00+00:00"
        self.task["_handoff_scope_review_reopened_result_id"] = "RR-C428294CF760BD8D99AA"
        self.assert_new_claim_rejected()

    def test_inputs_and_original_failed_native_job_remain_unchanged(self):
        before = copy.deepcopy((self.task, self.events, self.result, self.intents))
        self.reduce()
        self.binding()
        self.assertEqual(before, (self.task, self.events, self.result, self.intents))
        self.assertEqual("FAILED", FIXTURE["actual_failed_claim"]["status"])
        self.assertFalse(FIXTURE["actual_failed_claim"]["receipt"]["execution_started"])


if __name__ == "__main__":
    unittest.main()
