"""Exact-session resume is distinct from cross-conversation takeover."""
import copy
import unittest
from control_plane import research_continuation as c
from tests import test_research_continuation as _resume_fixture


class SameSessionResumeTests(unittest.TestCase):
    def setUp(self):
        self.fixture = _resume_fixture.ContinuationTests()
        self.fixture.setUp()
        self.addCleanup(self.fixture.doCleanups)
        self.old = copy.deepcopy(self.fixture.old)
        self.old["session_id"] = "active-own-session"
        self.release = {**self.old, "event": "HANDOFF", "at": "2026-09-20T09:19:00Z", "handoff_scope": "CONTINUATION",
            "next_action": "resume bounded work", "progress_ref": "published-frontier", "_github": {**self.old["_github"], "comment_id": 102}}
        self.resume = self.fixture.successor("RESUME")
        self.resume.update(researcher_id=self.old["researcher_id"], session_id="active-own-session")
        self.resume["_github"]["comment_id"] = 103
        self.resume["continuation"].update(session_id="active-own-session", previous_session_id="active-own-session")

    def reduce(self, *events):
        return self.fixture.reduce(*events)

    def test_released_exact_session_resume_wins_fresh_epoch_and_fences_old_progress(self):
        c.validate_claim_continuation(self.fixture.task, self.resume, root=self.fixture.root)
        progress = {**self.old, "event": "PROGRESS", "at": "2026-09-20T09:20:30Z", "progress_ref": "old-writer"}
        progress["_github"] = {**self.old["_github"], "comment_id": 104}
        state = self.reduce(self.old, self.release, self.resume, progress)
        self.assertEqual("new", state["claim_id"])
        self.assertEqual(103, state["ownership_epoch"])
        self.assertEqual("active-own-session", state["session_id"])
        self.assertEqual(self.fixture.frontier, state["continuation_frontier"])
        self.assertNotEqual("old-writer", state["last_progress_ref"])
        self.assertIn("old", state["fenced_claim_ids"])

    def test_live_same_identity_takeover_and_resume_are_rejected(self):
        for mode in ("TAKEOVER", "RESUME"):
            event = copy.deepcopy(self.resume)
            event["continuation"]["mode"] = mode
            self.assertEqual("old", self.reduce(self.old, event)["claim_id"])

    def test_foreign_unknown_mismatched_and_noncanonical_identity_cannot_bypass_session_gate(self):
        for identity in (self.old["researcher_id"], "  " + self.old["researcher_id"].lower() + "  "):
            for session in ("other-chat", None, ""):
                event = copy.deepcopy(self.resume)
                event.update(researcher_id=identity, session_id=session)
                event["continuation"]["session_id"] = session
                self.assertIsNone(self.reduce(self.old, self.release, event)["claim_id"])
        old = {**self.old, "session_id": None}
        self.assertIsNone(self.reduce(old, self.release, self.resume)["claim_id"])

    def test_predecessor_epoch_and_new_claim_identity_are_required(self):
        for field, value in (("expected_previous_comment_id", 99), ("expected_previous_claim_id", "other")):
            event = copy.deepcopy(self.resume)
            event["continuation"][field] = value
            self.assertIsNone(self.reduce(self.old, self.release, event)["claim_id"])
        event = {**self.resume, "claim_id": "old"}
        self.assertIsNone(self.reduce(self.old, self.release, event)["claim_id"])

    def test_static_resume_preserves_predecessor_contribution(self):
        event = copy.deepcopy(self.resume)
        event["continuation"]["frontier"]["contributor_ids"] = ["EM-OTHER-XXXX"]
        with self.assertRaisesRegex(c.ContinuationError, "provenance"):
            c.validate_claim_continuation(self.fixture.task, event, root=self.fixture.root)


if __name__ == "__main__":
    unittest.main()
