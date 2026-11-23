import json
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

    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.root = Path(tmp.name)
        self.git("init", "-q")
        self.git("config", "user.email", "test@example.invalid")
        self.git("config", "user.name", "Test")
        self.first = self.commit("request.json", '{"request_id":"first"}')
        self.request = self.commit("request.json", '{"request_id":"second"}')
        self.maintenance = self.commit("rule.txt", "maintenance")

    def git(self, *args):
        return subprocess.check_output(["git", *args], cwd=self.root, text=True).strip()

    def commit(self, path, content):
        (self.root / path).write_text(content)
        self.git("add", path)
        self.git("commit", "-qm", path)
        return self.git("rev-parse", "HEAD")

    def detect(self, event, *, before=None, recovery=None, ref="refs/heads/main", ok=True):
        validation = self.workflow.split("\n  canonical-dispatch:", 1)[0]
        step = validation.split("- name: Detect request authority", 1)[1]
        step = step.split("\n      - name:", 1)[0]
        script = textwrap.dedent(step.split("        run: |\n", 1)[1])
        output = self.root / "output"
        output.write_text("")
        result = subprocess.run(
            ["bash", "-c", script], cwd=self.root, capture_output=True, text=True,
            env={**os.environ, "GITHUB_EVENT_NAME": event, "GITHUB_SHA": self.maintenance,
                 "GITHUB_REF": ref, "PUSH_BEFORE": before or self.request,
                 "ORIGINAL_REQUEST_COMMIT": recovery or "", "GITHUB_OUTPUT": str(output),
                 "REQUEST_PATH": "request.json", "IMMUTABLE_RECEIPT_PATH": "receipt.json",
                 "IMMUTABLE_STARTUP_PACKET_PATH": "packet.json"},
        )
        if ok:
            self.assertEqual(0, result.returncode, result.stderr)
        else:
            self.assertNotEqual(0, result.returncode)
        return dict(line.split("=", 1) for line in output.read_text().splitlines())

    def test_push_range_including_request_change_before_tip(self):
        self.assertEqual({"execute": "true", "request_source_commit": self.request},
                         self.detect("push", before=self.first))

    def test_validation_never_persists_missing_or_existing_receipt(self):
        for event in ("push", "pull_request"):
            with self.subTest(event=event):
                self.assertEqual({"execute": "false"}, self.detect(event))
                (self.root / "receipt.json").touch()
                self.assertEqual({"execute": "false"}, self.detect(event))
                (self.root / "receipt.json").unlink()

    def test_zero_before_falls_back_to_first_parent(self):
        self.assertEqual({"execute": "false"}, self.detect("push", before="0" * 40))

    def test_missing_diff_base_cannot_authorize_request(self):
        self.assertEqual({}, self.detect("push", before="f" * 40, ok=False))

    def test_explicit_recovery_binds_latest_request_change_on_main(self):
        self.assertEqual({"execute": "true", "request_source_commit": self.request},
                         self.detect("workflow_dispatch", recovery=self.request))
        for commit in (self.first, self.maintenance):
            self.assertEqual({}, self.detect("workflow_dispatch", recovery=commit, ok=False))
        self.assertEqual({}, self.detect("workflow_dispatch", recovery=self.request,
                                        ref="refs/heads/other", ok=False))

    def test_explicit_recovery_respects_existing_pair_or_orphan(self):
        (self.root / "packet.json").touch()
        self.assertEqual({}, self.detect("workflow_dispatch", recovery=self.request, ok=False))
        (self.root / "receipt.json").touch()
        self.assertEqual({"execute": "false"}, self.detect("workflow_dispatch", recovery=self.request))
        (self.root / "packet.json").unlink()
        self.assertEqual({}, self.detect("workflow_dispatch", recovery=self.request, ok=False))

    def test_concurrent_recovery_reuses_only_the_original_request_and_packet(self):
        step = self.workflow.split("- name: Persist request receipt on main", 1)[1]
        script = textwrap.dedent(step.split("        run: |\n", 1)[1])
        # The race is at the freshly fetched tree. No network or write is required.
        no_remote = 'git() { case "$1" in config|fetch|reset) return 0 ;; *) return 99 ;; esac; }\n'
        receipt = self.root / "receipt.json"
        packet = self.root / "packet.json"
        env = {**os.environ, "GITHUB_SHA": self.maintenance, "REQUEST_ID": "second",
               "REQUEST_SOURCE_COMMIT": self.request, "IMMUTABLE_RECEIPT_PATH": str(receipt),
               "IMMUTABLE_STARTUP_PACKET_PATH": str(packet)}
        for original, packet_source, expected in [
                (self.request, self.first, 0), (self.first, self.first, 1),
                (self.request, self.maintenance, 1)]:
            with self.subTest(original=original, packet=packet_source):
                receipt.write_text(json.dumps({"request_id": "second", "source_sha": self.first,
                                               "request_source_commit": original}))
                packet.write_text(json.dumps({"request_id": "second", "source_sha": packet_source}))
                result = subprocess.run(["bash", "-c", no_remote + script], cwd=self.root,
                                        env=env, capture_output=True, text=True)
                self.assertEqual(expected, result.returncode, result.stderr)

    def test_only_authorized_job_fetches_live_events_and_writes(self):
        validation, execution = self.workflow.split("  canonical-dispatch:", 1)
        self.assertIn("contents: read", validation)
        self.assertNotIn("contents: write", validation)
        self.assertNotIn("GH_TOKEN", validation)
        self.assertIn("needs: inspect-request", execution)
        self.assertIn("if: needs.inspect-request.outputs.execute == 'true'", execution)
        self.assertIn("Fetch authoritative Issue 240 comment stream", execution)
        self.assertIn("Persist request receipt on main", execution)
        self.assertIn("request_source_commit: $request_source_commit", execution)
        self.assertIn('explicit_receipt_recovery: ($event == "workflow_dispatch")', execution)

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
