import unittest
from pathlib import Path


class ChatGPTDispatchBridgeReplayGuardTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.workflow = Path(
            ".github/workflows/chatgpt-control-dispatch-bridge.yml"
        ).read_text()

    def test_push_range_not_only_first_parent_detects_request_changes(self):
        self.assertIn("PUSH_BEFORE: ${{ github.event.before }}", self.workflow)
        self.assertIn('before="$PUSH_BEFORE"', self.workflow)
        self.assertIn(
            'git diff --quiet "$before" "$GITHUB_SHA" -- "$REQUEST_PATH"',
            self.workflow,
        )

    def test_zero_before_has_safe_first_parent_fallback(self):
        self.assertIn(
            'before="$(git rev-parse "${GITHUB_SHA}^1")"',
            self.workflow,
        )

    def test_workflow_only_push_is_validation_replay_not_new_request(self):
        self.assertIn("id: request_change", self.workflow)
        self.assertIn("REQUEST_REPLAY_VALIDATION_ONLY", self.workflow)
        self.assertIn(
            "if: github.event_name == 'push' && steps.request_change.outputs.changed == 'true'",
            self.workflow,
        )

    def test_replay_still_runs_live_router_before_persistence_gate(self):
        detect = self.workflow.index("- name: Detect request-producing push")
        fetch = self.workflow.index("- name: Fetch authoritative Issue 240 comment stream")
        route = self.workflow.index("- name: Execute canonical recover-before-fresh router")
        persist = self.workflow.index("- name: Persist request receipt on main")
        self.assertLess(detect, fetch)
        self.assertLess(fetch, route)
        self.assertLess(route, persist)

    def test_real_request_push_still_has_immutable_receipt_contract(self):
        self.assertIn("IMMUTABLE_RECEIPT_PATH", self.workflow)
        self.assertIn("DUPLICATE_REQUEST_ID_WITH_DIFFERENT_SOURCE", self.workflow)
        self.assertIn("LATEST_RECEIPT_SKIPPED", self.workflow)


if __name__ == "__main__":
    unittest.main()
