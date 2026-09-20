import copy
import json
import subprocess
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path
from types import SimpleNamespace
from unittest import mock

import research_driver_authority as driver
from control_plane import research_continuation as continuation
from tools import research_runtime_reducer as reducer


NOW = reducer.parse_time("2026-09-20T09:21:00Z")
SOURCE = "a" * 40


class ContinuationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / "EM_SNAPSHOT_READY.json").write_text(json.dumps({"sha": SOURCE}))
        (self.root / "frontier.md").write_text("Verified control handoff; mathematical parent remains open.\n")
        self.publish_fixture("frontier.md")
        self.pin = continuation.artifact_pin(self.root, "frontier.md", SOURCE)
        self.frontier = {"source_commit": SOURCE, "artifacts": [self.pin],
                         "current_unfinished_unit": "next lemma", "next_action": "inspect saved lemma",
                         "completed_units": ["saved bounded computation"], "do_not_repeat": ["saved computation"],
                         "contributor_ids": ["EM-TEST-OLD1"]}
        self.task = {"task_id": "RS-TEST", "publication_id": "TP2-TEST", "base_state": "READY"}
        self.old = self.claim("old", "EM-TEST-OLD1", 101, "2026-09-20T09:00:00Z")

    def publish_fixture(self, *paths):
        import hashlib
        manifest_path = self.root / "EM_SOURCE_BLOBS.json"
        manifest = json.loads(manifest_path.read_text()) if manifest_path.exists() else {"schema": "ENTERPRISE_MATH_SOURCE_BLOB_MANIFEST_V1", "source_commit": SOURCE, "blobs": {}}
        for path in paths:
            raw = (self.root / path).read_bytes()
            manifest["blobs"][path] = hashlib.sha1(f"blob {len(raw)}\0".encode() + raw).hexdigest()
        manifest_path.write_text(json.dumps(manifest))

    def claim(self, claim_id, researcher, cid, at):
        return {"schema": "ENTERPRISE_MATH_SCHEDULER_EVENT_V1", "event": "CLAIM",
                "task_id": "RS-TEST", "publication_id": "TP2-TEST", "claim_id": claim_id,
                "researcher_id": researcher, "at": at, "lease_minutes": 120,
                "_github": {"server_authenticated": True, "control_authorized": True,
                            "edited": False, "comment_id": cid, "issue_number": 240}}

    def successor(self, mode="TAKEOVER"):
        event = self.claim("new", "EM-TEST-NEW1", 102, "2026-09-20T09:20:00Z")
        event["session_id"] = "new-conversation"
        event["continuation"] = {"schema": continuation.SCHEMA, "mode": mode,
            "expected_previous_claim_id": "old", "expected_previous_comment_id": 101,
            "previous_researcher_id": "EM-TEST-OLD1", "session_id": "new-conversation",
            "reason": "Owner authorized replacement after terminated predecessor",
            "frontier": copy.deepcopy(self.frontier),
            "recovery_evidence": {"basis": "STALE_SESSION", "previous_session_id": "old-conversation",
                "observed_at": "2026-09-20T09:19:00Z", "last_activity_at": "2026-09-20T09:00:00Z",
                "source_ref": self.pin, "active_session_confirmed": False}}
        return event

    def reduce(self, *events, now=NOW):
        return reducer.reduce_task(self.task, events, now=now, default_lease_minutes=120)

    def test_successor_fences_old_progress_without_rewriting_old_claim(self):
        old_bytes = json.dumps(self.old, sort_keys=True)
        new = self.successor()
        progress = {**self.old, "event": "PROGRESS", "at": "2026-09-20T09:20:30Z", "progress_ref": "unauthorized"}
        state = self.reduce(self.old, new, progress)
        self.assertEqual("new", state["claim_id"])
        self.assertEqual("EM-TEST-NEW1", state["researcher_id"])
        self.assertEqual(["old"], state["fenced_claim_ids"])
        self.assertEqual("new-conversation", state["session_id"])
        self.assertEqual(102, state["ownership_epoch"])
        self.assertNotEqual("unauthorized", state.get("last_progress_ref"))
        self.assertEqual(old_bytes, json.dumps(self.old, sort_keys=True))

    def test_competing_takeovers_have_one_winner(self):
        rival = self.successor()
        rival.update(claim_id="rival", researcher_id="EM-TEST-RIVL", at="2026-09-20T09:20:01Z")
        rival["_github"]["comment_id"] = 103
        state = self.reduce(self.old, self.successor(), rival)
        self.assertEqual("new", state["claim_id"])
        self.assertIn("CAS changed", state["ignored_events"][-1]["reason"])

    def test_retry_is_idempotent_and_does_not_extend_lease(self):
        first = self.reduce(self.old, self.successor())
        retry = self.successor()
        retry["at"] = "2026-09-20T09:20:30Z"
        retry["_github"]["comment_id"] = 103
        second = self.reduce(self.old, self.successor(), retry)
        self.assertEqual(first["lease_until"], second["lease_until"])
        self.assertEqual(first["ownership_epoch"], second["ownership_epoch"])

    def test_active_or_recent_session_cannot_be_preempted(self):
        for evidence_change in ({"active_session_confirmed": True}, {"last_activity_at": "2026-09-20T09:18:00Z"}):
            event = self.successor()
            event["continuation"]["recovery_evidence"].update(evidence_change)
            self.assertEqual("old", self.reduce(self.old, event)["claim_id"])

    def test_real_recent_progress_overrides_callers_old_activity_time(self):
        progress = {**self.old, "event": "PROGRESS", "at": "2026-09-20T09:19:30Z", "progress_ref": "real-recent-source"}
        progress["_github"] = {**progress["_github"], "comment_id": 102}
        successor = self.successor()
        successor["_github"]["comment_id"] = 103
        self.assertEqual("old", self.reduce(self.old, progress, successor)["claim_id"])

    def test_taskbook_pin_cannot_impersonate_explicit_owner_release(self):
        event = self.successor()
        event["continuation"]["recovery_evidence"]["basis"] = "OWNER_CONFIRMED_TERMINATED"
        self.assertEqual("old", self.reduce(self.old, event)["claim_id"])

    def test_prepared_takeover_is_invalidated_by_new_real_heartbeat(self):
        from tools import research_dispatch
        event = self.successor()
        intent = {key: event.get(key) for key in ("task_id", "publication_id", "claim_id", "researcher_id", "execution_branch", "execution_branch_base", "allowed_outputs", "theorem_owner", "continuation")}
        intent["execution_record_id"] = "ER-FIXTURE"
        path = self.root / "research_execution_records/RS-TEST/ER-FIXTURE.json"
        path.parent.mkdir(parents=True)
        path.write_text(json.dumps(intent))
        heartbeat = {**self.old, "event": "HEARTBEAT", "at": "2026-09-20T09:20:30Z"}
        state = self.reduce(self.old, heartbeat)
        with mock.patch.object(continuation, "_definition", return_value=self.task), mock.patch.object(research_dispatch, "reduce_definition", return_value=state):
            with self.assertRaisesRegex(continuation.ContinuationError, "canonical owner activity"):
                continuation.validate_prepared_claim(root=self.root, events=[], now=NOW, source_commit=SOURCE, claim_event=event, intent=intent)

    def test_control_source_must_match_real_loader_snapshot(self):
        with self.assertRaisesRegex(continuation.ContinuationError, "loader snapshot"):
            continuation.verify_source_snapshot(self.root, "b" * 40)

    def test_global_continuation_explicitly_refuses_active_cohort_scope(self):
        from tools import research_dispatch
        with mock.patch.object(continuation, "_definition", return_value=self.task), mock.patch.object(research_dispatch, "reduce_definition", return_value={"dispatch_state": "COHORT_ACTIVE"}):
            with self.assertRaisesRegex(continuation.ContinuationError, "SUPPORTED_NATIVE_LANE_ADAPTER_REQUIRED"):
                continuation.prepare_takeover("RS-TEST", root=self.root, events=[], now=NOW, source_commit=SOURCE,
                    new_researcher_id="EM-TEST-NEW1", new_session_id="new-session", new_claim_id="new",
                    execution_branch="new", execution_branch_base=SOURCE, allowed_outputs=["output/"],
                    expected_previous_claim_id="old", expected_previous_comment_id=101, frontier=self.frontier, reason="fixture")

    def git(self, *args):
        result = subprocess.run(["git", "-c", "user.name=Control Fixture", "-c", "user.email=fixture@example.invalid",
            "-c", "commit.gpgsign=false", "-c", "core.autocrlf=false", "-c", f"core.hooksPath={self.root / 'empty-hooks'}",
            "-C", str(self.root), *args], capture_output=True, text=True, check=True)
        return result.stdout.strip()

    def test_dirty_or_untracked_bytes_cannot_be_pinned_as_immutable_head(self):
        self.git("init", "-q")
        (self.root / "proof.md").write_text("published source")
        self.git("add", "proof.md")
        self.git("commit", "-qm", "Control fixture Alpha")
        alpha = self.git("rev-parse", "HEAD")
        continuation.artifact_pin(self.root, "proof.md", alpha)
        (self.root / "proof.md").write_text("dirty unpublished source")
        with self.assertRaisesRegex(continuation.ContinuationError, "DRAFT_OR_UNVERIFIED"):
            continuation.artifact_pin(self.root, "proof.md", alpha)
        (self.root / "untracked.md").write_text("unpublished")
        with self.assertRaisesRegex(continuation.ContinuationError, "DRAFT_OR_UNVERIFIED"):
            continuation.artifact_pin(self.root, "untracked.md", alpha)

    def test_alpha_artifact_and_beta_control_are_legitimate_distinct_sources(self):
        self.git("init", "-q")
        (self.root / "proof.md").write_text("Alpha proof")
        self.git("add", "proof.md")
        self.git("commit", "-qm", "Control fixture Alpha")
        alpha = self.git("rev-parse", "HEAD")
        alpha_pin = continuation.artifact_pin(self.root, "proof.md", alpha)
        (self.root / "proof.md").write_text("Beta different source")
        self.git("add", "proof.md")
        self.git("commit", "-qm", "Control fixture Beta")
        beta = self.git("rev-parse", "HEAD")
        frontier = {**self.frontier, "source_commit": alpha, "artifacts": [alpha_pin]}
        continuation.validate_frontier(frontier, root=self.root, source_commit=beta)
        self.assertEqual(alpha, frontier["artifacts"][0]["source_commit"])
        self.assertNotEqual(alpha_pin["sha256"], continuation.artifact_pin(self.root, "proof.md", beta)["sha256"])

    def test_verified_external_partial_root_keeps_its_own_commit(self):
        import hashlib
        external = self.root / "external-evidence"
        external.mkdir()
        raw = b"Verified external branch bytes"
        (external / "proof.md").write_bytes(raw)
        alpha = "b" * 40
        manifest = {"schema": "ENTERPRISE_MATH_SOURCE_BLOB_MANIFEST_V1", "source_commit": alpha,
                    "blobs": {"proof.md": hashlib.sha1(f"blob {len(raw)}\0".encode() + raw).hexdigest()}}
        (external / "EM_SOURCE_BLOBS.json").write_text(json.dumps(manifest))
        pin = continuation.artifact_pin(self.root, "proof.md", alpha, evidence_roots={alpha: external})
        frontier = {**self.frontier, "artifacts": [pin]}
        continuation.validate_frontier(frontier, root=self.root, source_commit=SOURCE, evidence_roots={alpha: external})
        self.assertEqual(alpha, pin["source_commit"])
        with self.assertRaises(continuation.ContinuationError):
            continuation.validate_frontier(frontier, root=self.root, source_commit=SOURCE)

    def test_lost_progress_comment_does_not_hide_persisted_checkpoint(self):
        from tools import research_dispatch
        checkpoint_path = "research_artifacts/mcp/RS-TEST/old-conversation/write-one/_checkpoint.json"
        checkpoint = {"schema": "ENTERPRISE_MATH_MCP_EXECUTION_CHECKPOINT_V1", "task_id": "RS-TEST", "publication_id": "TP2-TEST",
                      "claim_id": "old", "ownership_epoch": 101, "session_id": "old-conversation", "researcher_id": "EM-TEST-OLD1", "output_manifest": []}
        path = self.root / checkpoint_path
        path.parent.mkdir(parents=True)
        path.write_text(json.dumps(checkpoint))
        self.publish_fixture(checkpoint_path)
        pointer = {**checkpoint, "schema": "ENTERPRISE_MATH_MCP_CHECKPOINT_POINTER_V1", "authority_granted": False,
                   "checkpoint_path": checkpoint_path, "checkpoint_sha256": continuation.artifact_pin(self.root, checkpoint_path, SOURCE)["sha256"],
                   "created_at": "2026-09-20T09:05:00Z"}
        pointer_path = self.root / "research_artifacts/mcp/RS-TEST/latest_checkpoint.json"
        pointer_path.write_text(json.dumps(pointer))
        self.publish_fixture(pointer_path.relative_to(self.root).as_posix())
        old = {**self.old, "session_id": "old-conversation"}
        with mock.patch.object(continuation, "_definition", return_value=self.task):
            result = continuation.checkpoint_frontier("RS-TEST", "TP2-TEST", root=self.root, events=[old], source_commit=SOURCE)
            self.assertEqual("SOURCE_BYTES_AND_RECORDED_CLAIM_VERIFIED", result["state"])
            self.assertFalse(result["execution_authorized"])
            self.assertIn("AUTHOR_REPORTED", result["semantic_status"])
            path.write_text("changed")
            changed = continuation.checkpoint_frontier("RS-TEST", "TP2-TEST", root=self.root, events=[old], source_commit=SOURCE)
            self.assertEqual("UNKNOWN", changed["state"])

    def test_missing_stale_evidence_cannot_replace_live_owner(self):
        event = self.successor()
        del event["continuation"]["recovery_evidence"]
        self.assertEqual("old", self.reduce(self.old, event)["claim_id"])

    def test_unauthenticated_takeover_is_rejected_by_reducer_too(self):
        event = self.successor()
        event["_github"]["control_authorized"] = False
        self.assertEqual("old", self.reduce(self.old, event)["claim_id"])

    def test_expired_claim_resumes_same_task_with_new_owner(self):
        event = self.successor("RESUME")
        event["at"] = "2026-09-20T12:00:00Z"
        state = self.reduce(self.old, event, now=reducer.parse_time("2026-09-20T12:01:00Z"))
        self.assertEqual("new", state["claim_id"])
        self.assertEqual("RS-TEST", state["task_id"])

    def test_publication_or_authorship_drift_is_rejected(self):
        event = self.successor()
        event["publication_id"] = "TP2-OTHER"
        with self.assertRaisesRegex(continuation.ContinuationError, "publication"):
            continuation.validate_claim_continuation(self.task, event, root=self.root)
        event = self.successor()
        event["continuation"]["frontier"]["contributor_ids"] = ["EM-TEST-OTHER"]
        with self.assertRaisesRegex(continuation.ContinuationError, "provenance"):
            continuation.validate_claim_continuation(self.task, event, root=self.root)

    def test_fresh_frontier_checks_bytes_but_history_keeps_immutable_pin(self):
        continuation.validate_frontier(self.frontier, root=self.root, source_commit=SOURCE)
        (self.root / "frontier.md").write_text("changed")
        with self.assertRaisesRegex(continuation.ContinuationError, "bytes"):
            continuation.validate_frontier(self.frontier, root=self.root, source_commit=SOURCE)
        # The old exact commit is provenance; present-tree file drift must not
        # retrospectively erase an authenticated historical owner transition.
        continuation.validate_claim_continuation(self.task, self.successor(), root=self.root)

    def enable_gate(self):
        path = self.root / continuation.POLICY
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps({"canonical_freeze_requires_current_runtime_authorization": True}))

    def test_freeze_without_current_ownership_evidence_fails_closed(self):
        self.enable_gate()
        with self.assertRaisesRegex(continuation.ContinuationError, "--runtime-state-file"):
            continuation.require_freeze_authority({}, SimpleNamespace(), root=self.root)

    def test_fenced_execution_cannot_freeze_against_new_winner(self):
        from tools import research_dispatch, research_runtime_guard
        self.enable_gate()
        state_file = self.root / "runtime.json"
        state_file.write_text("{}")
        args = SimpleNamespace(runtime_state_file=str(state_file), events="events.json")
        binding = {"claim_id": "new", "publication_id": "TP2-TEST", "researcher_id": "EM-TEST-NEW1",
                   "execution_branch": "new-branch", "taskbook_blob_sha1": "b" * 40}
        record = {**binding, "task_id": "RS-TEST", "claim_id": "old"}
        with mock.patch.object(research_dispatch, "load_events", return_value=[]), mock.patch.object(research_runtime_guard, "authorize_execution", return_value={"authorized": True, "task_id": "RS-TEST", "execution_binding": binding}) as authorize:
            with self.assertRaisesRegex(continuation.ContinuationError, "fenced"):
                continuation.require_freeze_authority(record, args, root=self.root)
            self.assertLess(abs((datetime.now(timezone.utc) - authorize.call_args.kwargs["now"]).total_seconds()), 5)

    def test_inventory_cursor_is_bound_to_current_source_and_events(self):
        from tools import research_dispatch
        rows = [{"task_id": "A", "dispatch_state": "NEEDS_DISPATCH"}, {"task_id": "B", "dispatch_state": "AWAITING_REVIEW"}]
        with mock.patch.object(research_dispatch, "effective_states", return_value=rows):
            first = continuation.inventory(root=self.root, events=[], now=NOW, source_commit=SOURCE, limit=1)
            second = continuation.inventory(root=self.root, events=[], now=NOW, source_commit=SOURCE, limit=1, cursor=first["next_cursor"])
            self.assertEqual("B", second["tasks"][0]["task_id"])
            with self.assertRaisesRegex(continuation.ContinuationError, "CURSOR_STALE"):
                continuation.inventory(root=self.root, events=[{"new": True}], now=NOW, source_commit=SOURCE, cursor=first["next_cursor"])

    def test_awaiting_current_generation_does_not_borrow_an_old_result(self):
        from tools import research_dispatch, research_result_records
        rows = [{"task_id": "RS-TEST", "publication_id": "TP2-NEW", "dispatch_state": "AWAITING_REVIEW"}]
        with mock.patch.object(research_dispatch, "effective_states", return_value=rows), mock.patch.object(research_result_records, "iter_results", return_value=[{"task_id": "RS-TEST", "publication_id": "TP2-OLD"}]):
            result = continuation.inventory_projection(root=self.root, events=[], now=NOW, source_commit=SOURCE)
            self.assertEqual("LEGACY_BRANCH_RESULT_INTAKE_REQUIRED", result["tasks"][0]["continuation"]["action"])
            self.assertFalse(result["tasks"][0]["continuation"]["execution_authorized"])
        with mock.patch.object(research_dispatch, "effective_states", return_value=rows), mock.patch.object(research_result_records, "iter_results", return_value=[{"task_id": "RS-TEST", "publication_id": "TP2-NEW"}]):
            result = continuation.inventory_projection(root=self.root, events=[], now=NOW, source_commit=SOURCE)
            self.assertEqual("ACTIVATE_NEW_DRIVER_AND_REVIEW_FROZEN_RESULT", result["tasks"][0]["continuation"]["action"])

    def test_legacy_intake_packet_distinguishes_exact_result_from_prose_hint(self):
        from tools import research_dispatch, research_task_records, research_result_records, research_taskbook
        taskbook = "research_tasks/fixture.md"
        book = self.root / taskbook
        book.parent.mkdir(parents=True)
        book.write_text(research_taskbook.render_taskbook({"task_id": "RS-TEST"}, "Control fixture only."))
        publication = {"task_id": "RS-TEST", "publication_id": "TP2-TEST", "taskbook_path": taskbook}
        pub_path = self.root / "research_task_records/RS-TEST/TP2-TEST.json"
        pub_path.parent.mkdir(parents=True)
        pub_path.write_text(json.dumps(publication))
        self.publish_fixture(taskbook, pub_path.relative_to(self.root).as_posix())
        runtime = {"task_id": "RS-TEST", "state": "FROZEN_RETURN", "dispatch_state": "AWAITING_REVIEW",
                   "next_action": "Resolve PR #123 then review", "last_progress_ref": "PR #123"}
        with mock.patch.object(continuation, "_definition", return_value=self.task), mock.patch.object(research_task_records, "current_records", return_value={"RS-TEST": publication}), mock.patch.object(research_dispatch, "reduce_definition", return_value=runtime), mock.patch.object(research_result_records, "task_result_state", return_value=None):
            packet = continuation.continuation_packet("RS-TEST", root=self.root, events=[], now=NOW, source_commit=SOURCE)
            self.assertEqual("FROZEN_RETURN", packet["runtime"]["state"])
            self.assertEqual("LEGACY_BRANCH_RESULT_INTAKE_REQUIRED", packet["route"]["action"])
            self.assertEqual("NEEDS_EXACT_SOURCE_LOOKUP", packet["legacy_result_intake"]["candidate_status"])
            self.assertFalse(packet["legacy_result_intake"]["research_reclaim_allowed"])
            runtime["last_progress_ref"] = f"https://github.com/awdawmip/enterprise-math/blob/{SOURCE}/research_result_records/RS-TEST/RR-OLD.json"
            exact = continuation.continuation_packet("RS-TEST", root=self.root, events=[], now=NOW, source_commit=SOURCE)
            self.assertEqual("EXACT_FROZEN_RESULT_CANDIDATE_PENDING_READBACK", exact["legacy_result_intake"]["candidate_status"])
            self.assertFalse(exact["legacy_result_intake"]["native_review_ready"])

    def test_explicit_file_commit_is_candidate_but_branch_or_blob_is_only_hint(self):
        candidate = continuation._fixed_source_candidate(f"research_returns/return.md@{SOURCE}", "CURRENT_TASKBOOK_DECLARED_INPUT")
        self.assertEqual("research_returns/return.md", candidate["path"])
        self.assertEqual(SOURCE, candidate["source_commit"])
        self.assertEqual("PENDING_IMMUTABLE_READBACK", candidate["verification"])
        self.assertIsNone(continuation._fixed_source_candidate(f"research/some-branch@{SOURCE}", "hint"))
        self.assertIsNone(continuation._fixed_source_candidate(f"research_returns/return.md@blob:{SOURCE}", "hint"))

    def test_path_traversal_cannot_become_verified_frontier(self):
        with self.assertRaises(continuation.ContinuationError):
            continuation.artifact_pin(self.root, "../outside", SOURCE)

    def test_driver_review_cannot_erase_declared_contribution(self):
        self.enable_gate()
        active = {"source_body": json.dumps({"session_id": "review-session"}), "authority_record_id": "DA-NEW"}
        args = SimpleNamespace(driver_id="EM-DVR-NEW1", reviewer_session_id="review-session",
                               reviewer_contribution_ids_json='["EM-TEST-OLD1"]')
        with mock.patch.object(driver, "require_active_driver", return_value=active):
            with self.assertRaisesRegex(continuation.ContinuationError, "contributed"):
                continuation.require_review_authority({"researcher_id": "EM-TEST-NEW1", "contributor_ids": ["EM-TEST-OLD1"]}, args, root=self.root)
            args.reviewer_contribution_ids_json = "[]"
            self.assertEqual(active, continuation.require_review_authority({"researcher_id": "EM-TEST-NEW1"}, args, root=self.root))

    def test_old_sessionless_da_cannot_be_borrowed_for_new_review(self):
        self.enable_gate()
        old = {"source_body": "{}", "authority_record_id": "DA-OLD"}
        args = SimpleNamespace(driver_id="EM-DVR-OLD1", reviewer_session_id="arbitrary-new-session", reviewer_contribution_ids_json="[]")
        with mock.patch.object(driver, "require_active_driver", return_value=old):
            with self.assertRaisesRegex(continuation.ContinuationError, "explicitly session-bound"):
                continuation.require_review_authority({"researcher_id": "EM-TEST-NEW1"}, args, root=self.root)


class DriverSuccessionTests(unittest.TestCase):
    def row(self, driver_id, cid, at, succession=None):
        body = {"event": "AUTHORIZE", "driver_id": driver_id}
        if succession:
            body["succession"] = succession
        return {"driver_id": driver_id, "source_comment_id": cid, "authority_record_id": f"DA-{cid}",
                "event": "AUTHORIZE", "source_created_at": at, "source_body": json.dumps(body)}

    def test_driver_succession_is_cas_and_preserves_prior_authority_time(self):
        old = self.row("EM-DVR-OLD1", 1, "2026-09-20T08:00:00Z")
        predecessor = {"previous_driver_id": old["driver_id"], "previous_authority_record_id": "DA-1", "previous_source_comment_id": 1}
        new = self.row("EM-DVR-NEW1", 2, "2026-09-20T09:00:00Z", predecessor)
        rival = self.row("EM-DVR-RIVL", 3, "2026-09-20T09:00:01Z", predecessor)
        with mock.patch.object(driver, "contract_enabled", return_value=True), mock.patch.object(driver, "contract"), mock.patch.object(driver, "valid_records", return_value=[old, new, rival]):
            self.assertEqual(old, driver.active_authority_at(old["driver_id"], "2026-09-20T08:59:59Z"))
            self.assertIsNone(driver.active_authority_at(old["driver_id"], "2026-09-20T09:01:00Z"))
            self.assertEqual(new, driver.active_authority_at(new["driver_id"], "2026-09-20T09:01:00Z"))
            self.assertIsNone(driver.active_authority_at(rival["driver_id"], "2026-09-20T09:01:00Z"))

    def test_later_same_second_revocation_does_not_rewrite_observed_review_history(self):
        old = self.row("EM-DVR-OLD1", 1, "2026-09-20T08:00:00Z")
        revoke = {**self.row("EM-DVR-OLD1", 2, "2026-09-20T09:00:00Z"), "event": "REVOKE"}
        with mock.patch.object(driver, "contract_enabled", return_value=True), mock.patch.object(driver, "contract"), mock.patch.object(driver, "valid_records", return_value=[old, revoke]):
            self.assertIsNone(driver.active_authority_at(old["driver_id"], "2026-09-20T09:00:00.500Z"))
            self.assertEqual(old, driver.active_authority_at(old["driver_id"], "2026-09-20T09:00:00.500Z", through_comment_id=1))

    def test_governance_role_is_driver_without_researcher_activity(self):
        authority = {"source_body": json.dumps({"session_id": "driver-session"}), "authority_record_id": "DA-1", "source_comment_id": 1}
        with mock.patch.object(continuation, "_definition", return_value={"kind": "GOVERNANCE"}), mock.patch.object(driver, "require_active_driver", return_value=authority):
            result = continuation.authorize_executor_role("GOV-TEST", executor_id="EM-DVR-NEW1", session_id="driver-session", executor_role="RESEARCH_DRIVER", now=NOW, root=Path.cwd())
            self.assertEqual("RESEARCH_DRIVER", result["executor_role"])
            self.assertNotIn("activity_id", result)
            with self.assertRaisesRegex(continuation.ContinuationError, "actual RESEARCH_DRIVER"):
                continuation.authorize_executor_role("GOV-TEST", executor_id="EM-DVR-NEW1", session_id="driver-session", executor_role="RESEARCHER", now=NOW, root=Path.cwd())
            authority["source_body"] = "{}"
            with self.assertRaisesRegex(continuation.ContinuationError, "explicitly session-bound"):
                continuation.authorize_executor_role("GOV-TEST", executor_id="EM-DVR-NEW1", session_id="driver-session", executor_role="RESEARCH_DRIVER", now=NOW, root=Path.cwd())


if __name__ == "__main__":
    unittest.main()
