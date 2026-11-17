"""Prior authenticated progress remains discoverable when late writes narrow latest."""
import hashlib
import json
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from control_plane import research_continuation as continuation
from tools import research_dispatch


SOURCE = "a" * 40
TASK = "RS-TEST"
PUB = "TP2-TEST"
CLAIM = "claim-one"
SESSION = "session-one"
AUTHOR = "EM-TEST-OWNER"


class CheckpointHistoryTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.blobs = {}
        self.definition = {"task_id": TASK, "publication_id": PUB, "base_state": "READY"}
        self.write("EM_SNAPSHOT_READY.json", {"sha": SOURCE})

    def write(self, path, value):
        raw = json.dumps(value).encode("utf-8")
        file = self.root / path
        file.parent.mkdir(parents=True, exist_ok=True)
        file.write_bytes(raw)
        self.blobs[path] = hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()
        (self.root / "EM_SOURCE_BLOBS.json").write_text(json.dumps({
            "schema": "ENTERPRISE_MATH_SOURCE_BLOB_MANIFEST_V1",
            "source_commit": SOURCE, "blobs": self.blobs}))

    def run_case(self, first_units, last_units, corrupt_prior=False):
        prefix = f"research_artifacts/mcp/{TASK}/{SESSION}"
        first_path = f"{prefix}/first/_checkpoint.json"
        last_path = f"{prefix}/last/_checkpoint.json"
        fields = {"task_id": TASK, "publication_id": PUB, "claim_id": CLAIM,
                  "ownership_epoch": 101, "session_id": SESSION,
                  "researcher_id": AUTHOR}
        for path, units in ((first_path, first_units), (last_path, last_units)):
            self.write(path, {**fields,
                "schema": "ENTERPRISE_MATH_MCP_EXECUTION_CHECKPOINT_V1",
                "completed_units": units, "output_manifest": []})
        self.write(f"research_artifacts/mcp/{TASK}/latest_checkpoint.json", {
            **fields, "schema": "ENTERPRISE_MATH_MCP_CHECKPOINT_POINTER_V1",
            "authority_granted": False, "checkpoint_path": last_path,
            "checkpoint_sha256": continuation.artifact_pin(self.root, last_path, SOURCE)["sha256"],
            "created_at": "2026-11-16T22:46:34Z"})
        def event(kind, at, cid, ref=None, claim=CLAIM):
            value = {"schema": "ENTERPRISE_MATH_SCHEDULER_EVENT_V1",
                     "event": kind, "task_id": TASK, "publication_id": PUB,
                     "claim_id": claim, "researcher_id": AUTHOR, "session_id": SESSION,
                     "at": at, "lease_minutes": 120,
                     "_github": {"server_authenticated": True, "control_authorized": True,
                                 "comment_id": cid, "edited": False}}
            if ref:
                value["progress_ref"] = f"https://github.com/awdawmip/enterprise-math/blob/{'b'*40}/{ref}"
            return value
        events = [
            event("CLAIM", "2026-11-16T22:00:00Z", 101),
            event("PROGRESS", "2026-11-16T22:32:53Z", 102, first_path),
            event("PROGRESS", "2026-11-16T23:00:12Z", 103, last_path)]
        if corrupt_prior:
            # Authenticity filtering and reduction must never let this
            # unrelated claimant's artifact become a verified prior checkpoint.
            events.insert(2, event("PROGRESS", "2026-11-16T22:37:00Z", 104,
                                   last_path, claim="other-claim"))
        with mock.patch.object(continuation, "_definition", return_value=self.definition), \
             mock.patch.object(research_dispatch, "_event_authentication_filter",
                               side_effect=lambda _definition, rows: (rows, [])), \
             mock.patch.object(research_dispatch, "_filter_registered_events",
                               side_effect=lambda _definition, rows, _root, result_state: (rows, [])):
            return continuation.checkpoint_frontier(TASK, PUB, root=self.root,
                                                   events=events, source_commit=SOURCE)

    def test_late_narrower_and_late_broader_both_preserve_earlier_source(self):
        for first, last in ((["U75", "U76"], ["U75"]),
                            (["U75"], ["U75", "U76"])):
            with self.subTest(first=first, last=last):
                result = self.run_case(first, last)
                self.assertEqual("SOURCE_BYTES_AND_RECORDED_CLAIM_VERIFIED", result["state"])
                self.assertEqual(last, result["checkpoint"]["completed_units"])
                prior = result["prior_authenticated_checkpoints"]
                self.assertEqual(1, len(prior))
                self.assertEqual(first, prior[0]["completed_units"])
                self.assertEqual(102, prior[0]["original_progress_comment_id"])
                self.assertEqual(SOURCE, prior[0]["source_artifact"]["source_commit"])
                self.assertFalse(prior[0]["execution_authorized"])
                self.assertFalse(result["execution_authorized"])

    def test_unauthorized_foreign_claim_is_not_promoted(self):
        result = self.run_case(["U75", "U76"], ["U75"], corrupt_prior=True)
        self.assertEqual("SOURCE_BYTES_AND_RECORDED_CLAIM_VERIFIED", result["state"])
        self.assertEqual([102], [p["original_progress_comment_id"]
                                 for p in result["prior_authenticated_checkpoints"]])


if __name__ == "__main__":
    unittest.main()
