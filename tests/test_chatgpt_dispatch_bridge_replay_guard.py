import os
import subprocess
import tempfile
import textwrap
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

    def test_persistence_gate_uses_receipt_recovery_decision(self):
        self.assertIn("id: request_change", self.workflow)
        self.assertIn("REQUEST_REPLAY_VALIDATION_ONLY", self.workflow)
        self.assertIn(
            "if: github.event_name == 'push' && steps.request_change.outputs.persist == 'true'",
            self.workflow,
        )

    def detect_request(self, *, changed, receipt_exists):
        # Run the actual workflow detection script with only git diff stubbed.
        # No checkout or remote write is involved in these three routing cases.
        step = self.workflow.split("- name: Detect request-producing push", 1)[1]
        step = step.split("\n      - name:", 1)[0]
        script = textwrap.dedent(step.split("        run: |\n", 1)[1])
        git_stub = 'git() { test "$1" = diff || return 2; return "$REQUEST_DIFF_EXIT"; }\n'
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "output"
            receipt = Path(tmp) / "receipt.json"
            if receipt_exists:
                receipt.write_text("{}", encoding="utf-8")
            result = subprocess.run(
                ["bash", "-c", git_stub + script],
                env={
                    **os.environ,
                    "REQUEST_DIFF_EXIT": "1" if changed else "0",
                    "PUSH_BEFORE": "1" * 40,
                    "GITHUB_SHA": "2" * 40,
                    "GITHUB_OUTPUT": str(output),
                    "REQUEST_PATH": "request.json",
                    "REQUEST_ID": "test-request",
                    "IMMUTABLE_RECEIPT_PATH": str(receipt),
                },
                capture_output=True,
                text=True,
                check=True,
            )
            flags = dict(line.split("=", 1) for line in output.read_text().splitlines())
            return flags, result.stdout

    def test_workflow_only_push_with_existing_receipt_is_validation_only(self):
        flags, log = self.detect_request(changed=False, receipt_exists=True)
        self.assertEqual({"changed": "false", "persist": "false"}, flags)
        self.assertIn("REQUEST_REPLAY_VALIDATION_ONLY", log)

    def test_workflow_only_push_recovers_missing_receipt(self):
        flags, log = self.detect_request(changed=False, receipt_exists=False)
        self.assertEqual({"changed": "false", "persist": "true"}, flags)
        self.assertIn("REQUEST_REPLAY_MISSING_RECEIPT", log)

    def test_changed_request_push_persists(self):
        flags, log = self.detect_request(changed=True, receipt_exists=False)
        self.assertEqual({"changed": "true", "persist": "true"}, flags)
        self.assertIn("REQUEST_PRODUCING_PUSH", log)

    def test_replay_still_runs_live_router_and_compact_builder_before_persistence_gate(self):
        detect = self.workflow.index("- name: Detect request-producing push")
        fetch = self.workflow.index("- name: Fetch authoritative Issue 240 comment stream")
        route = self.workflow.index("- name: Execute canonical recover-before-fresh router")
        compact = self.workflow.index("- name: Build compact researcher startup packet")
        persist = self.workflow.index("- name: Persist request receipt on main")
        self.assertLess(detect, fetch)
        self.assertLess(fetch, route)
        self.assertLess(route, compact)
        self.assertLess(compact, persist)

    def test_real_request_push_has_immutable_receipt_and_startup_packet_contract(self):
        self.assertIn("IMMUTABLE_RECEIPT_PATH", self.workflow)
        self.assertIn("IMMUTABLE_STARTUP_PACKET_PATH", self.workflow)
        self.assertIn("STARTUP_PACKET_DIR: control_plane/chatgpt_startup_packets", self.workflow)
        self.assertIn("control_plane/researcher_startup_packet.py", self.workflow)
        self.assertIn("DUPLICATE_REQUEST_ID_WITH_DIFFERENT_SOURCE", self.workflow)
        self.assertIn("ORPHAN_IMMUTABLE_STARTUP_PACKET", self.workflow)
        self.assertIn("IMMUTABLE_STARTUP_PACKET_MISSING_OR_MISMATCHED_FOR_EXISTING_RECEIPT", self.workflow)
        self.assertIn("LATEST_RECEIPT_SKIPPED", self.workflow)

    def test_compact_packet_is_bounded_and_not_a_latest_mutable_pointer(self):
        self.assertIn("ENTERPRISE_MATH_RESEARCHER_STARTUP_PACKET_V1", self.workflow)
        self.assertIn("(.packet_bytes <= 8192)", self.workflow)
        self.assertNotIn("chatgpt_startup_packet.json", self.workflow)


if __name__ == "__main__":
    unittest.main()
