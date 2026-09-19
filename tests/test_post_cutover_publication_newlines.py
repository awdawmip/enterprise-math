import json
from pathlib import Path
import tempfile
import unittest
from unittest import mock

from control_plane import check_post_cutover_publication_envelope as envelope
from tools import research_taskbook


TASK_ID = "RS-NEWLINE-FIXTURE"
BODY = "\n".join(
    f"## {heading}\n\nFrozen fixture content.\n"
    for heading in (
        "Mother question",
        "Frozen inputs and scope",
        "Hard target and required outputs",
        "Research value to preserve",
        "Success, kill, and return criteria",
    )
)
LF_TASKBOOK = research_taskbook.render_taskbook({"task_id": TASK_ID}, BODY).encode("utf-8")
CRLF_TASKBOOK = LF_TASKBOOK.replace(b"\n", b"\r\n")


class PublicationNewlineTests(unittest.TestCase):
    def audit_bytes(self, data, *, declared_blob=None):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            task_path = root / "research_tasks" / "fixture.md"
            task_path.parent.mkdir()
            task_path.write_bytes(data)
            record_path = root / "research_task_records" / TASK_ID / "TP2-FIXTURE.json"
            record_path.parent.mkdir(parents=True)
            record = {
                "record_schema": envelope.RECORD_SCHEMA,
                "task_id": TASK_ID,
                "taskbook_path": "research_tasks/fixture.md",
                "taskbook_blob_sha1": declared_blob or envelope.git_blob_sha1(data),
            }
            record_path.write_text(json.dumps(record), encoding="utf-8")
            record_bytes = record_path.read_bytes()
            with mock.patch.object(envelope, "ROOT", root), mock.patch.object(
                envelope, "_validated_exception_paths", return_value=(set(), set(), set(), [])
            ):
                errors = envelope.audit(root)
            self.assertEqual(data, task_path.read_bytes())
            self.assertEqual(record_bytes, record_path.read_bytes())
            return errors

    def test_lf_and_crlf_use_the_existing_parser_without_changing_bytes(self):
        self.assertNotEqual(
            envelope.git_blob_sha1(LF_TASKBOOK), envelope.git_blob_sha1(CRLF_TASKBOOK)
        )
        for data in (LF_TASKBOOK, CRLF_TASKBOOK):
            with self.subTest(newline="CRLF" if b"\r\n" in data else "LF"):
                self.assertEqual([], self.audit_bytes(data))

    def test_normalized_pin_cannot_replace_the_actual_raw_byte_pin(self):
        for data, other in ((LF_TASKBOOK, CRLF_TASKBOOK), (CRLF_TASKBOOK, LF_TASKBOOK)):
            with self.subTest(newline="CRLF" if b"\r\n" in data else "LF"):
                errors = self.audit_bytes(data, declared_blob=envelope.git_blob_sha1(other))
                self.assertEqual(1, len(errors))
                self.assertIn("taskbook Git blob drift", errors[0])

    def test_wrong_or_missing_markers_remain_rejected_with_matching_pins(self):
        for source in (LF_TASKBOOK, CRLF_TASKBOOK):
            for data in (
                source.replace(b"ENTERPRISE_MATH_TASK_V1", b"ENTERPRISE_MATH_TASK_V2", 1),
                b" " + source,
                source.split(b"\n", 1)[1],
            ):
                with self.subTest(data=data[:42]):
                    errors = self.audit_bytes(data)
                    self.assertEqual(1, len(errors))
                    self.assertIn("does not use canonical ENTERPRISE_MATH_TASK_V1 envelope", errors[0])

    def test_malformed_json_remains_rejected_after_newline_normalization(self):
        for source in (LF_TASKBOOK, CRLF_TASKBOOK):
            data = source.replace(b'"task_id"', b'broken_key', 1)
            with self.subTest(newline="CRLF" if b"\r\n" in data else "LF"):
                errors = self.audit_bytes(data)
                self.assertEqual(1, len(errors))
                self.assertIn("canonical taskbook parse failed", errors[0])


if __name__ == "__main__":
    unittest.main()
