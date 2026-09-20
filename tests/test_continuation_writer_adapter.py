import json
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest import mock

from control_plane import research_continuation_writer as writer
from control_plane.research_continuation import ContinuationError


class RestrictedWriterAdapterTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / "tools").mkdir()
        (self.root / "tools/research_result_records.py").write_text("# fixed admitted native entrypoint fixture\n")
        self.source = "a" * 40

    def mark(self):
        (self.root / writer.MARKER).write_text(json.dumps({"schema": "ENTERPRISE_MATH_ISOLATED_WRITE_SANDBOX_V1", "source_commit": self.source, "isolated": True}))

    def test_unmarked_real_workspace_is_not_a_write_sandbox(self):
        with self.assertRaises(FileNotFoundError):
            writer.prepare_freeze(root=self.root, source_commit=self.source, runtime_state={}, raw_comments=[], payload={})

    def test_payload_cannot_add_arbitrary_commands(self):
        self.mark()
        with self.assertRaisesRegex(ContinuationError, "exactly"):
            writer.prepare_freeze(root=self.root, source_commit=self.source, runtime_state={}, raw_comments=[], payload={"command": "arbitrary"})

    def test_invocation_is_fixed_argv_without_shell(self):
        with mock.patch.object(writer.subprocess, "run", return_value=SimpleNamespace(returncode=0, stdout='{"ok": true}', stderr="")) as run:
            self.assertTrue(writer._invoke(self.root, "freeze", ["--return-path", "name with spaces.md"])["ok"])
            argv = run.call_args.args[0]
            self.assertEqual("-I", argv[1])
            self.assertEqual(str(self.root / "tools/research_result_records.py"), argv[2])
            self.assertEqual(["freeze", "--return-path", "name with spaces.md"], argv[3:])
            self.assertNotIn("shell", run.call_args.kwargs)
        with self.assertRaises(ContinuationError):
            writer._invoke(self.root, "exec", [])

    def test_unexpected_code_change_is_never_published(self):
        before = writer._capture(self.root)
        (self.root / "tools/research_result_records.py").write_text("changed")
        with self.assertRaisesRegex(ContinuationError, "outside"):
            writer._changes(self.root, before)

    def test_immutable_record_rewrite_is_never_published(self):
        path = self.root / "research_result_records/RS-TEST/RR-OLD.json"
        path.parent.mkdir(parents=True)
        path.write_text("{}")
        before = writer._capture(self.root)
        path.write_text('{"changed":true}')
        with self.assertRaisesRegex(ContinuationError, "immutable"):
            writer._changes(self.root, before)

    def test_freeze_returns_unsubmitted_handoff_only_after_native_result(self):
        self.mark()
        artifact = self.root / "research_artifacts/mcp/RS-TEST/session/return.md"
        artifact.parent.mkdir(parents=True)
        artifact.write_text("fixture-only submitted mathematical text")
        path = artifact.relative_to(self.root).as_posix()
        payload = {field: "fixture" for field in writer.FREEZE_FIELDS}
        payload.update(return_path=path, output_paths=[path])
        record = {"task_id": "RS-TEST", "publication_id": "TP2-TEST", "result_id": "RR-TEST",
                  "claim_id": "new", "researcher_id": "EM-TEST-NEW1", "next_control_plane_recommendation": "independent review"}

        def native_fixture(root, command, arguments):
            target = root / "research_result_records/RS-TEST/RR-TEST.json"
            target.parent.mkdir(parents=True)
            target.write_text(json.dumps(record))
            return record

        with mock.patch.object(writer, "_invoke", side_effect=native_fixture):
            result = writer.prepare_freeze(root=self.root, source_commit=self.source, runtime_state={}, raw_comments=[], payload=payload)
        self.assertEqual(1, len(result["files"]))
        self.assertTrue(result["requires_publication_before_handoff"])
        self.assertNotIn("progress_ref", result["handoff_event_template"])
        self.assertFalse(result["mathematical_acceptance_granted"])


if __name__ == "__main__":
    unittest.main()
