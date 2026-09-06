import unittest

from tools import research_dispatch as rd
from tools import research_runtime_reducer as rr


class RegisteredDoneDispatchGuardTests(unittest.TestCase):
    def setUp(self):
        self.task = {
            "task_id": "RS-T1",
            "publication_id": "TP2-TEST",
            "kind": "RESEARCH",
            "priority": "P0",
            "leverage": "HIGH",
        }
        self.done = {
            "schema": rr.EVENT_SCHEMA,
            "event": "DONE",
            "task_id": "RS-T1",
            "claim_id": "c1",
            "progress_ref": "return.md",
            rd.GITHUB_META_KEY: {"comment_id": 123, "server_authenticated": True},
        }
        self.rejected = [{
            "index": 0,
            "reason": "registered DONE requires a frozen result with terminal Driver review",
        }]

    def fresh_state(self):
        return {
            "task_id": "RS-T1",
            "kind": "RESEARCH",
            "priority": "P0",
            "leverage": "HIGH",
            "state": "HANDOFF_READY",
            "dispatch_state": "NEEDS_DISPATCH",
        }

    def test_unreviewed_done_blocks_fresh_redispatch_without_promoting_completion(self):
        state = rd._block_unreviewed_registered_done(
            self.task, self.fresh_state(), [self.done], self.rejected, None
        )
        self.assertEqual("BLOCKED", state["state"])
        self.assertEqual("BLOCKED", state["dispatch_state"])
        self.assertEqual(
            "REGISTERED_DONE_REQUIRES_TERMINAL_DRIVER_REVIEW",
            state["hard_block"]["code"],
        )
        self.assertEqual(123, state["hard_block"]["server_comment_id"])
        self.assertIsNone(rr.select_state([state], rr.load_policy(), kind="RESEARCH"))

    def test_existing_result_lifecycle_remains_authoritative(self):
        original = self.fresh_state()
        result_state = {"state": "AWAITING_DRIVER_REVIEW"}
        state = rd._block_unreviewed_registered_done(
            self.task, original, [self.done], self.rejected, result_state
        )
        self.assertEqual(original, state)

    def test_active_lease_is_not_replaced_by_provisional_block(self):
        original = self.fresh_state()
        original["state"] = "CLAIMED"
        original["dispatch_state"] = "LEASED"
        state = rd._block_unreviewed_registered_done(
            self.task, original, [self.done], self.rejected, None
        )
        self.assertEqual(original, state)

    def test_other_rejection_reason_does_not_trigger_terminal_guard(self):
        original = self.fresh_state()
        state = rd._block_unreviewed_registered_done(
            self.task,
            original,
            [self.done],
            [{"index": 0, "reason": "registered DONE result_id mismatch"}],
            None,
        )
        self.assertEqual(original, state)


if __name__ == "__main__":
    unittest.main()
