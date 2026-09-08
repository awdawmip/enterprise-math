"""Freeze prepared taskbooks consistently across platform newline writes."""
from __future__ import annotations

import copy
from pathlib import Path
from types import SimpleNamespace
import unittest
from unittest import mock

from control_plane import research_driver_followup_transaction as transaction
from tools import research_task_records, research_taskbook


ROOT = Path(__file__).resolve().parents[1]
META = {"task_id": "RS-NEWLINE-FIXTURE", "title": "Prepared boundary fixture"}
BODY = """# Prepared boundary fixture

## 0. Mother question

Preserve UTF-8 text: 进取数论; literal escape \\r\\n remains literal.

## 1. Frozen inputs and scope

Only temporary prepared bytes are involved.

## 2. Hard target and required outputs

Freeze the validated text with LF line endings.

## 3. Research value to preserve

Keep the complete metadata and body.

## 4. Success, kill, and return criteria

Malformed metadata or body must still be rejected.
"""
LF_BYTES = research_taskbook.render_taskbook(META, BODY).encode("utf-8")


class PreparedTaskbookNewlineTests(unittest.TestCase):
    def prepare(self, content, returned_meta=None):
        # The actual prepare-only pipeline is covered by the captured real-spec
        # receipt. These fixtures isolate its successful-return byte boundary.
        def prepared(path, **kwargs):
            self.assertEqual(kwargs["publisher_role"], "RESEARCH_DRIVER")
            self.assertEqual(kwargs["parent_objective_id"], "FIXTURE_PARENT")
            self.assertEqual(kwargs["root"], ROOT)
            path.write_bytes(content)
            return copy.deepcopy(META if returned_meta is None else returned_meta)

        source = SimpleNamespace(_taskbook_text=lambda spec, parent: LF_BYTES.decode("utf-8"))
        with mock.patch.object(research_task_records, "prepare_taskbook", side_effect=prepared):
            return transaction._prepared_taskbook_bytes(source, {}, "FIXTURE_PARENT", ROOT)

    def test_lf_bytes_are_unchanged(self):
        meta, content = self.prepare(LF_BYTES)
        self.assertEqual(meta, META)
        self.assertEqual(content, LF_BYTES)

    def test_crlf_bytes_freeze_as_the_same_complete_lf_text(self):
        crlf = LF_BYTES.replace(b"\n", b"\r\n")
        with self.assertRaisesRegex(ValueError, "missing ENTERPRISE_MATH_TASK_V1"):
            research_taskbook.split_taskbook(crlf.decode("utf-8"))
        meta, content = self.prepare(crlf)
        self.assertEqual(meta, META)
        self.assertEqual(content, LF_BYTES)
        self.assertNotIn(b"\r", content)
        self.assertEqual(research_taskbook.split_taskbook(content.decode("utf-8")),
                         research_taskbook.split_taskbook(LF_BYTES.decode("utf-8")))

    def test_missing_frontmatter_is_still_rejected(self):
        with self.assertRaisesRegex(ValueError, "missing ENTERPRISE_MATH_TASK_V1"):
            self.prepare(BODY.encode("utf-8"))

    def test_metadata_mismatch_is_still_rejected(self):
        with self.assertRaisesRegex(transaction.DriverFollowupTransactionError, "metadata differs"):
            self.prepare(LF_BYTES, {**META, "task_id": "RS-DIFFERENT"})

    def test_invalid_body_is_still_rejected(self):
        content = research_taskbook.render_taskbook(META, "# Incomplete body\n").encode("utf-8")
        with self.assertRaises(transaction.DriverFollowupTransactionError):
            self.prepare(content)

    def test_invalid_utf8_is_still_rejected(self):
        with self.assertRaises(UnicodeDecodeError):
            self.prepare(LF_BYTES + b"\xff")


if __name__ == "__main__":
    unittest.main()
