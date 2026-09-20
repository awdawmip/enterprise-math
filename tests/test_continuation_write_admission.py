import copy
import base64
import hashlib
import json
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from control_plane import research_continuation_write_authority as admission


class WriteAdmissionTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.cutover = self.root / admission.CUTOVER
        self.cutover.parent.mkdir(parents=True)
        self.cutover.write_text(json.dumps({"schema": "ENTERPRISE_MATH_CONTINUATION_RECORD_CUTOVER_V1", "records": {}}))
        self.result = {"task_id": "RS-TEST", "publication_id": "TP2-TEST", "result_id": "RR-TEST",
                       "researcher_id": "EM-TEST-OLD1", "claim_id": "old", "taskbook_blob_sha1": "b" * 40}

    def test_old_format_new_result_and_review_are_nonoperational(self):
        self.assertIn("requires", admission.receipt_error(self.result, "RESULT", self.root))
        self.assertEqual([], admission.operational([self.result], "RESULT", self.root))
        review = {**self.result, "review_id": "DR-NEW"}
        self.assertEqual([], admission.operational([review], "REVIEW", self.root))
        self.assertEqual("RR-TEST", admission.diagnostics([self.result], "RESULT", self.root)[0]["result_id"])

    def test_direct_git_style_old_format_record_holds_exact_task_generation(self):
        from tools import research_result_records
        path = self.root / admission.record_path(self.result, "RESULT")
        path.parent.mkdir(parents=True)
        path.write_text(json.dumps(self.result))
        state = research_result_records.task_result_state("RS-TEST", self.root, "TP2-TEST")
        self.assertEqual("RESULT_CONTROL_AUTHORITY_WITHHELD", state["state"])
        self.assertFalse(state["terminal"])
        self.assertEqual(["RR-TEST"], state["withheld_result_ids"])
        self.assertIn("write_authorization", state["write_authority_holds"][0]["reason"])

    def test_exact_legacy_pin_retains_original_audit_not_mutation_permission(self):
        relative = admission.record_path(self.result, "RESULT")
        path = self.root / relative
        path.parent.mkdir(parents=True)
        raw = json.dumps(self.result).encode()
        path.write_bytes(raw)
        pins = {relative: {"git_blob_sha1": hashlib.sha1(f"blob {len(raw)}\0".encode() + raw).hexdigest(), "sha256": hashlib.sha256(raw).hexdigest()}}
        self.cutover.write_text(json.dumps({"schema": "ENTERPRISE_MATH_CONTINUATION_RECORD_CUTOVER_V1", "records": pins}))
        self.assertIsNone(admission.receipt_error(self.result, "RESULT", self.root))
        path.write_bytes(raw + b"\n")
        self.assertIn("immutable", admission.receipt_error(self.result, "RESULT", self.root))

    def test_receipt_cannot_be_copied_to_changed_result_payload(self):
        record = copy.deepcopy(self.result)
        record["write_authorization"] = admission.build_receipt(record, "RESULT", {})
        record["claim_id"] = "different"
        self.assertIn("payload", admission.receipt_error(record, "RESULT", self.root))

    def test_receipt_replays_server_stream_and_rejects_fenced_writer(self):
        from tools import research_dispatch
        from tests.test_research_continuation import ContinuationTests, NOW
        fixture = ContinuationTests()
        fixture.setUp()
        self.addCleanup(fixture.doCleanups)
        new = fixture.successor()
        publication = self.root / "research_task_records/RS-TEST/TP2-TEST.json"
        publication.parent.mkdir(parents=True)
        from tools import research_taskbook
        taskbook = research_taskbook.render_taskbook({"task_id": "RS-TEST", "base_state": "READY", "claim_lease_minutes": 120}, "Control fixture only.").encode()
        blob = "sha1:" + hashlib.sha1(f"blob {len(taskbook)}\0".encode() + taskbook).hexdigest()
        pub = {"task_id": "RS-TEST", "publication_id": "TP2-TEST", "claimable": True,
               "taskbook_blob_sha1": blob, "taskbook_path": "research_tasks/fixture.md", "published_at": "2026-09-19T00:00:00Z"}
        publication.write_text(json.dumps(pub))
        record = copy.deepcopy(self.result)
        record["taskbook_blob_sha1"] = blob
        book_receipt = {"taskbook_content_base64": base64.b64encode(taskbook).decode()}
        definition = admission._canonical_frozen_definition(pub, book_receipt)
        context = {"source_commit": "a" * 40, "authorized_at": NOW.isoformat(), "server_comments": [],
                   "task_definition": definition, **book_receipt,
                   "principal": {"claim_id": "old", "researcher_id": "EM-TEST-OLD1", "session_id": "old-session", "ownership_epoch": 101}}
        record["write_authorization"] = admission.build_receipt(record, "RESULT", context)
        events = [fixture.old, new]
        with mock.patch.object(research_dispatch, "events_from_github_comments", return_value=events), mock.patch.object(research_dispatch, "_event_authentication_filter", return_value=(events, [])), mock.patch.object(research_dispatch, "_filter_registered_events", return_value=(events, [])):
            self.assertIn("fenced", admission.receipt_error(record, "RESULT", self.root))
            record["claim_id"] = "new"
            record["researcher_id"] = "EM-TEST-NEW1"
            context["principal"].update(claim_id="new", researcher_id="EM-TEST-NEW1", session_id="new-conversation", ownership_epoch=102)
            record["write_authorization"] = admission.build_receipt(record, "RESULT", context)
            self.assertIsNone(admission.receipt_error(record, "RESULT", self.root))
            record["write_authorization"]["task_definition"]["claim_lease_minutes"] = 99999
            self.assertIn("immutable publication/taskbook", admission.receipt_error(record, "RESULT", self.root))


if __name__ == "__main__":
    unittest.main()
