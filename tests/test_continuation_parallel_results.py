"""Continuation projects real parallel Results without opening another scope."""
import hashlib
import json
import tempfile
import unittest
from contextlib import ExitStack
from pathlib import Path
from unittest import mock

import research_driver_authority as driver
from control_plane import research_continuation as continuation
from control_plane import research_source_firewall
from tools import research_dispatch, research_result_records, research_task_records, research_taskbook


class ParallelResultContinuationTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.sha = "a" * 40
        self.task = "RS-TEST"
        self.publication = "TP2-TEST"
        self.book = "research_tasks/current.md"
        self.record = {"task_id": self.task, "publication_id": self.publication, "taskbook_path": self.book}
        self.runtime = {**self.record, "state": "FROZEN_RETURN", "dispatch_state": "AWAITING_REVIEW",
                        "claim_id": None, "next_action": "Review the pending parallel Result."}
        self.manifest = {"schema": "ENTERPRISE_MATH_SOURCE_BLOB_MANIFEST_V1", "source_commit": self.sha, "blobs": {}}
        (self.root / "EM_SNAPSHOT_READY.json").write_text(json.dumps({"sha": self.sha}))
        self.publish(self.book, research_taskbook.render_taskbook({"task_id": self.task}, "Frozen task scope."))
        self.publish(f"research_task_records/{self.task}/{self.publication}.json", json.dumps(self.record))
        self.a = self.result("RR-FIRST")
        self.b = self.result("RR-SECOND")
        self.state = {"state": "AWAITING_DRIVER_REVIEW", "terminal": False,
                      "parallel_result_ids": [self.a["result_id"], self.b["result_id"]],
                      "pending_result_review_ids": [self.b["result_id"]],
                      "result": {"result_id": "PARALLEL-" + self.task, "task_id": self.task,
                                 "publication_id": self.publication, "_record_path": None,
                                 "parallel_result_ids": [self.a["result_id"], self.b["result_id"]]}}

    def publish(self, path, text):
        target = self.root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        data = text.encode()
        target.write_bytes(data)
        self.manifest["blobs"][path] = hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()
        (self.root / "EM_SOURCE_BLOBS.json").write_text(json.dumps(self.manifest))

    def result(self, rid, *, task=None, publication=None):
        task = task or self.task
        publication = publication or self.publication
        row = {"record_schema": "ENTERPRISE_MATH_RESEARCH_RESULT_RECORD_V1", "result_id": rid,
               "task_id": task, "publication_id": publication, "execution_record_id": "ER-" + rid,
               "return_path": f"research_returns/{rid}.md",
               "output_manifest": [{"path": f"research_artifacts/{rid}/proof.txt"}]}
        path = f"research_result_records/{task}/{rid}.json"
        self.publish(path, json.dumps(row))
        self.publish(row["return_path"], rid + " frozen return")
        self.publish(row["output_manifest"][0]["path"], rid + " bounded proof evidence")
        self.publish(f"research_execution_records/{task}/{row['execution_record_id']}.json", json.dumps({"task_id": task}))
        return {**row, "_record_path": path}

    def packet(self, *, mapping=None, firewall=False, driver_session=None):
        with ExitStack() as stack:
            stack.enter_context(mock.patch.object(continuation, "_definition", return_value=self.record))
            stack.enter_context(mock.patch.object(research_task_records, "current_records", return_value={self.task: self.record}))
            stack.enter_context(mock.patch.object(research_dispatch, "reduce_definition", return_value=self.runtime))
            stack.enter_context(mock.patch.object(research_result_records, "task_result_state", return_value=self.state))
            if mapping is not None:
                stack.enter_context(mock.patch.object(research_result_records, "result_map", return_value=mapping))
            if firewall:
                stack.enter_context(mock.patch.object(research_source_firewall, "validate_config", return_value={"allowed_source_pins": []}))
            if driver_session is not None:
                stack.enter_context(mock.patch.object(driver, "require_active_driver", return_value={"source_body": json.dumps({"session_id": "review-session"})}))
            return continuation.continuation_packet(self.task, root=self.root, events=[],
                now=continuation.datetime.fromisoformat("2026-10-02T10:00:00+00:00"), source_commit=self.sha,
                reader_driver_id="EM-DVR-TEST" if driver_session is not None else None,
                reader_session_id=driver_session)

    def paths(self, packet):
        return {pin["path"] for pin in packet["source_artifacts"]}

    def assert_not_exposed(self, packet, row):
        self.assertNotIn(row["_record_path"], self.paths(packet))
        self.assertNotIn(row["return_path"], self.paths(packet))
        self.assertNotIn(row["output_manifest"][0]["path"], self.paths(packet))

    def test_real_current_parallel_records_and_bound_outputs_are_pinned(self):
        packet = self.packet()
        for row in [self.a, self.b]:
            pins = [pin for pin in packet["source_artifacts"] if pin["path"] == row["_record_path"]]
            self.assertEqual(1, len(pins))
            pin = pins[0]
            self.assertEqual((row["result_id"], self.task, self.publication, self.sha),
                             tuple(pin[key] for key in ["result_id", "task_id", "publication_id", "source_commit"]))
            self.assertEqual(self.manifest["blobs"][row["_record_path"]], pin["git_blob_sha1"])
            self.assertEqual(hashlib.sha256((self.root / row["_record_path"]).read_bytes()).hexdigest(), pin["sha256"])
            self.assertIn(row["return_path"], self.paths(packet))
            self.assertIn(row["output_manifest"][0]["path"], self.paths(packet))
            self.assertIn(f"research_execution_records/{self.task}/{row['execution_record_id']}.json", self.paths(packet))
        self.assertEqual([], packet["artifact_errors"])
        self.assertFalse(packet["execution_authorized"])
        self.assertEqual([self.b["result_id"]], packet["result_state"]["pending_result_review_ids"])

    def test_summary_id_never_becomes_a_fictitious_rr_path(self):
        packet = self.packet()
        serialized = json.dumps(packet["source_artifacts"] + packet["artifact_errors"])
        self.assertNotIn("PARALLEL-", serialized)
        self.assertEqual(self.state, packet["result_state"])

    def test_parallel_synthesis_record_keeps_its_real_path(self):
        path = f"research_parallel_syntheses/{self.task}/PS-EXACT.json"
        self.publish(path, json.dumps({"task_id": self.task, "publication_id": self.publication}))
        self.state["result"].update(result_id="PS-EXACT", _record_path=path)
        packet = self.packet()
        self.assertIn(path, self.paths(packet))
        self.assertFalse(any("research_result_records/" in item["path"] and "PS-EXACT" in item["path"]
                             for item in packet["source_artifacts"] + packet["artifact_errors"]))

    def test_duplicate_member_ids_do_not_duplicate_pins(self):
        self.state["parallel_result_ids"].append(self.a["result_id"])
        packet = self.packet()
        self.assertEqual(len(self.paths(packet)), len(packet["source_artifacts"]))

    def test_other_task_or_publication_cannot_expand_the_packet(self):
        for index, (task, publication) in enumerate([("RS-OTHER", self.publication), (self.task, "TP2-OLD")]):
            with self.subTest(task=task, publication=publication):
                foreign = self.result(f"RR-FOREIGN-{index}", task=task, publication=publication)
                self.state["parallel_result_ids"] = [self.a["result_id"], foreign["result_id"]]
                packet = self.packet()
                self.assert_not_exposed(packet, foreign)
                self.assertIn(self.a["_record_path"], self.paths(packet))
                self.assertTrue(any("current task/publication" in row["error"] for row in packet["artifact_errors"]))

    def test_projected_record_path_cannot_point_to_another_record(self):
        aliased = {**self.b, "_record_path": self.a["_record_path"]}
        packet = self.packet(mapping={self.a["result_id"]: self.a, self.b["result_id"]: aliased})
        self.assert_not_exposed(packet, self.b)
        self.assertTrue(any("record path differs" in row["error"] for row in packet["artifact_errors"]))

    def test_immutable_record_scope_must_match_the_operational_row(self):
        raw = {key: value for key, value in self.b.items() if key != "_record_path"}
        raw["publication_id"] = "TP2-OLD"
        self.publish(self.b["_record_path"], json.dumps(raw))
        packet = self.packet(mapping={self.a["result_id"]: self.a, self.b["result_id"]: self.b})
        self.assert_not_exposed(packet, self.b)
        self.assertTrue(any("immutable bytes differ" in row["error"] for row in packet["artifact_errors"]))

    def test_byte_pinned_quarantine_is_not_bypassed_by_a_stale_parallel_id(self):
        from control_plane import research_result_records_compat_runtime as compatibility
        quarantine = {"schema": compatibility.QUARANTINE_SCHEMA, "status": "ACTIVE", "entries": [{
            "result_id": self.b["result_id"], "resolution": "QUARANTINE_INVALID_RECORD", "operational": False,
            "history_preserved": True, "record_path": self.b["_record_path"],
            "record_blob_sha1": self.manifest["blobs"][self.b["_record_path"]], "corrected_result_id": self.a["result_id"],
            "task_id": self.task, "publication_id": self.publication, "reason": ["Exact invalid fixture retained only as history."]}]}
        self.publish(compatibility.QUARANTINE_FILE, json.dumps(quarantine))
        self.assertNotIn(self.b["result_id"], research_result_records.result_map(self.root))
        packet = self.packet()
        self.assert_not_exposed(packet, self.b)
        self.assertIn(self.a["_record_path"], self.paths(packet))
        self.assertEqual(quarantine, json.loads((self.root / compatibility.QUARANTINE_FILE).read_text()))

    def test_missing_member_does_not_open_its_surviving_outputs(self):
        (self.root / self.b["_record_path"]).unlink()
        packet = self.packet()
        self.assert_not_exposed(packet, self.b)
        self.assertTrue(packet["artifact_errors"])

    def test_dirty_or_unmanifested_record_does_not_open_its_outputs(self):
        original = (self.root / self.b["_record_path"]).read_bytes()
        for mode in ["dirty", "unmanifested"]:
            with self.subTest(mode=mode):
                (self.root / self.b["_record_path"]).write_bytes(original + b" " if mode == "dirty" else original)
                if mode == "unmanifested":
                    self.manifest["blobs"].pop(self.b["_record_path"])
                    (self.root / "EM_SOURCE_BLOBS.json").write_text(json.dumps(self.manifest))
                packet = self.packet()
                self.assert_not_exposed(packet, self.b)
                self.assertTrue(any("DRAFT_OR_UNVERIFIED" in row["error"] for row in packet["artifact_errors"]))

    def test_blind_reader_does_not_resolve_or_expose_parallel_results(self):
        with mock.patch.object(research_result_records, "result_map", side_effect=AssertionError("restricted result lookup")):
            packet = self.packet(firewall=True)
        for row in [self.a, self.b]:
            self.assert_not_exposed(packet, row)
        self.assertNotIn("RR-FIRST", json.dumps(packet))
        self.assertTrue(packet["source_access_policy"]["restricted"])

    def test_driver_firewall_access_still_requires_exact_active_session(self):
        packet = self.packet(firewall=True, driver_session="review-session")
        self.assertIn(self.b["_record_path"], self.paths(packet))
        self.assertTrue(packet["source_access_policy"]["verified_driver_review_view"])
        with self.assertRaisesRegex(continuation.ContinuationError, "matching current DA session"):
            self.packet(firewall=True, driver_session="wrong-session")

    def test_single_result_keeps_existing_artifact_projection(self):
        self.state = {"state": "AWAITING_DRIVER_REVIEW", "result": self.a, "terminal": False}
        with mock.patch.object(research_result_records, "result_map", side_effect=AssertionError("unnecessary parallel lookup")):
            packet = self.packet()
        self.assertIn(self.a["_record_path"], self.paths(packet))
        self.assertIn(self.a["return_path"], self.paths(packet))
        self.assert_not_exposed(packet, self.b)
        self.assertEqual([], packet["artifact_errors"])


if __name__ == "__main__":
    unittest.main()
