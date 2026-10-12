"""Isolated synthetic control events over exact frozen PCF scientific bytes.

No event in these fixtures is a real claim, review, or mathematical acceptance.
Server-envelope authentication, registered intent filter, reducer, DA validation,
old-byte pins, local transaction and public task-state consumption remain real.
"""
import base64
import copy
import hashlib
import json
import shutil
import tempfile
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path
from unittest import mock

from control_plane import research_historical_result_intake as h
from control_plane import research_continuation_write_authority as writes
from tests.test_research_driver_authority import contract, policy, record as da_fixture
from tools import research_dispatch, research_execution_records, research_result_records

REPO = Path(__file__).resolve().parents[1]
SOURCE = "a" * 40


class HistoricalIntakeTests(unittest.TestCase):
    def setUp(self):
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        self.root = Path(directory.name)
        self.write("EM_SNAPSHOT_READY.json", {"sha": SOURCE})
        # Other ordinary tests install the canonical bootstrap globally. Supply
        # its real unrelated semantic-quarantine fixture in either test order.
        from tests.test_research_task_record_compatibility import _write_semantic_fixture
        _write_semantic_fixture(self.root)
        target = json.loads((REPO / h.CONTRACT).read_text())["targets"][0]
        self.target = target
        paths = [h.CONTRACT, "research_runtime_policy_v2.json", "research_task_publication_contract_v2.json"]
        old = json.loads((REPO / target["result_pin"]["path"]).read_text())
        quarantine = json.loads((REPO / "research_result_authority_quarantines.json").read_text())
        quarantine["entries"] = [row for row in quarantine["entries"] if row["result_id"] == target["historical_result_id"]]
        paths += [row["path"] for row in quarantine["entries"][0]["dependency_pins"]]
        paths += [row["path"] for row in old["output_manifest"]]
        paths += [target[field]["path"] for field in ("result_pin", "execution_pin", "publication_pin", "taskbook_pin")]
        self.gov = target["authorizing_governance_task_id"]
        gov_path = next((REPO / "research_task_records" / self.gov).glob("*.json"))
        pub = json.loads(gov_path.read_text())
        self.gov_pub = pub
        paths += [gov_path.relative_to(REPO).as_posix(), pub["taskbook_path"]]
        for path in set(paths):
            dst = self.root / path
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(REPO / path, dst)
        self.write("research_result_authority_quarantines.json", quarantine)
        cutover = json.loads((REPO / writes.CUTOVER).read_text())
        cutover["records"] = {key: value for key, value in cutover["records"].items() if (self.root / key).exists()}
        self.write(writes.CUTOVER, cutover)
        self.write("research_driver_authority_contract.json", contract())
        self.write("research_control_event_authorization.json", policy())
        self.now = datetime.now(timezone.utc)
        self.driver, self.session = "EM-DVR-FIXHRI", "fixture-intake-session"
        self.da = self.authority(self.driver, self.session, 9900000001)
        intent = research_execution_records.prepare_intent(task_id=self.gov, claim_id="fixture-hri-claim",
            researcher_id=self.driver, theorem_owner=pub["owner"], execution_branch="research/fixture-hri",
            execution_branch_base=SOURCE, allowed_outputs=["research_artifacts/fixture-hri/"],
            owner_lease_minutes=120, prepared_at=(self.now - timedelta(minutes=1)).isoformat(), root=self.root)
        intent["executor_role"] = "RESEARCH_DRIVER"
        self.write(f"research_execution_records/{self.gov}/{intent['execution_record_id']}.json", intent)
        event = {"schema": research_dispatch.EVENT_SCHEMA, "event": "CLAIM", "task_id": self.gov,
            "publication_id": pub["publication_id"], "claim_id": intent["claim_id"], "researcher_id": self.driver,
            "session_id": self.session, "executor_role": "RESEARCH_DRIVER", "lease_minutes": 120}
        comment = {"id": 9900000002, "body": json.dumps(event), "created_at": self.now.isoformat(), "updated_at": self.now.isoformat(),
            "issue_url": "https://api.github.com/repos/awdawmip/enterprise-math/issues/240",
            "user": {"login": "owner", "id": 7}, "author_association": "OWNER"}
        encoded = base64.b64encode((self.root / pub["taskbook_path"]).read_bytes()).decode()
        self.context = {"source_commit": SOURCE, "authorized_at": self.now.isoformat(), "principal": {
            "driver_id": self.driver, "session_id": self.session, "authority_record_id": self.da["authority_record_id"],
            "governance_task_id": self.gov, "governance_publication_id": pub["publication_id"], "claim_id": intent["claim_id"],
            "ownership_epoch": 9900000002, "execution_record_id": intent["execution_record_id"], "run_request_id": "fixture-hri-open"},
            "authority_observed_through_comment_id": 9900000002, "server_comments": [comment], "taskbook_content_base64": encoded,
            "task_definition": writes._canonical_frozen_definition(pub, {"taskbook_content_base64": encoded})}
        self.spec = {"run_request_id": "fixture-hri-open", "target_task_id": target["task_id"], "publication_id": target["publication_id"],
            "historical_result_id": target["historical_result_id"], "expected_result_sha256": target["result_pin"]["sha256"],
            "expected_result_blob_sha1": target["result_pin"]["git_blob_sha1"], "expected_execution_sha256": target["execution_pin"]["sha256"],
            "expected_execution_blob_sha1": target["execution_pin"]["git_blob_sha1"], "expected_publication_blob_sha1": target["publication_pin"]["git_blob_sha1"],
            "expected_taskbook_blob_sha1": target["taskbook_pin"]["git_blob_sha1"], "reason": "isolated fixture only"}

    def write(self, path, value):
        p = self.root / path
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(json.dumps(value) + "\n")

    def authority(self, driver, session, cid):
        import research_driver_authority as da
        value = da_fixture(comment_id=cid, created=(self.now - timedelta(minutes=2)).isoformat())
        body = json.dumps({"schema": da.EVENT_SCHEMA, "event": "AUTHORIZE", "driver_id": driver,
            "scope": "CONTROL_PLANE", "authority": "RESEARCH_DRIVER", "session_id": session})
        value.update(driver_id=driver, authority_record_id=da._record_id(driver, "AUTHORIZE", cid),
            source_body=body, source_body_sha256="sha256:" + hashlib.sha256(body.encode()).hexdigest())
        self.write(f"research_driver_authority_records/{driver}/{value['authority_record_id']}.json", value)
        return value

    def intake(self):
        return h.freeze_intake(self.spec, self.context, root=self.root)

    def mark_published(self):
        self.write("EM_SOURCE_BLOBS.json", {"schema": "ENTERPRISE_MATH_SOURCE_BLOB_MANIFEST_V1", "source_commit": SOURCE,
            "blobs": {path.relative_to(self.root).as_posix(): h.pin(self.root, path.relative_to(self.root).as_posix())["git_blob_sha1"]
                      for path in self.root.rglob("*") if path.is_file() and path.name != "EM_SOURCE_BLOBS.json"}})

    def review(self, intake, disposition="ACCEPTED", contributors=None):
        driver, session = "EM-DVR-FIXHRV", "fixture-review-session"
        da = self.authority(driver, session, 9900000003)
        self.write("driver_reviews/fixture-hri.md", {"fixture": "synthetic review disposition; no real acceptance"})
        artifact = h.pin(self.root, "driver_reviews/fixture-hri.md")
        record_pin = h.pin(self.root, intake["record_path"])
        spec = {"target_task_id": self.target["task_id"], "publication_id": self.target["publication_id"], "intake_id": intake["record"]["intake_id"],
            "expected_intake_sha256": record_pin["sha256"], "expected_intake_blob_sha1": record_pin["git_blob_sha1"],
            "review_path": artifact["path"], "expected_review_sha256": artifact["sha256"], "expected_review_blob_sha1": artifact["git_blob_sha1"],
            "disposition": disposition, "reviewer_contribution_ids": contributors or [driver], "reason": "synthetic fixture review only",
            "portfolio_continuation": {"parent_objective_status": "OPEN", "next_action": "continue the existing parent", "next_task_id": None}}
        context = {"source_commit": SOURCE, "authorized_at": self.now.isoformat(), "authority_observed_through_comment_id": 9900000003,
            "principal": {"driver_id": driver, "session_id": session, "authority_record_id": da["authority_record_id"]}}
        _, heads = h.review_heads(intake["record"]["intake_id"], root=self.root)
        previous = [{"review_id": row["review_id"], **h.pin(self.root, f"{h.REVIEW_ROOT}/{intake['record']['intake_id']}/{row['review_id']}.json")} for row in heads]
        spec.update(supersedes_review_ids=sorted(row["review_id"] for row in heads), expected_previous_review_set_sha256=h.review_set_digest(previous))
        context["authorized_at"] = datetime.now(timezone.utc).isoformat()
        self.last_review_spec, self.last_review_context = spec, context
        return h.freeze_review(spec, context, root=self.root)

    def test_intake_preserves_every_old_byte_and_unknown_auth_never_inherits_acceptance(self):
        before = {p: (self.root / p).read_bytes() for p in [self.target["result_pin"]["path"], self.target["execution_pin"]["path"]]}
        frozen = self.intake()
        self.assertTrue(frozen["created"])
        self.assertFalse(h.freeze_intake(self.spec, self.context, root=self.root)["created"])
        state = research_result_records.task_result_state(self.target["task_id"], self.root, self.target["publication_id"])
        self.assertEqual("AWAITING_DRIVER_REVIEW", state["state"])
        self.assertFalse(state["terminal"])
        self.assertFalse(state["execution_authorized"])
        self.assertEqual("historical_result_review", state["review_write_operation"])
        self.assertIn("UNKNOWN", state["historical_authentication_status"])
        for path, raw in before.items():
            self.assertEqual(raw, (self.root / path).read_bytes())
        self.assertFalse((self.root / "research_execution_records" / self.target["task_id"] / "ER-E90FEF513B0AEE96C73E.json").exists())

    def test_fresh_independent_review_and_explicit_open_parent_complete_only_task(self):
        intake = self.intake()
        reviewed = self.review(intake)
        state = h.task_state(self.target["task_id"], self.target["publication_id"], root=self.root)
        self.assertTrue(state["terminal"])
        self.assertFalse(state["parent_completion_granted"])
        self.assertEqual("OPEN", state["portfolio_continuation"]["parent_objective_status"])
        self.assertEqual(reviewed["record"]["review_id"], state["review"]["review_id"])
        self.assertEqual([], h.audit(self.root))

    def test_revision_has_no_execution_authority(self):
        self.review(self.intake(), "REQUEST_REVISION")
        state = h.task_state(self.target["task_id"], self.target["publication_id"], root=self.root)
        self.assertEqual("RETURN_TO_EXECUTION", state["state"])
        self.assertFalse(state["terminal"])
        self.assertFalse(state["execution_authorized"])

    def test_exact_target_pins_unknown_fields_and_run_binding_reject_before_write(self):
        for field, value in (("expected_result_sha256", "b" * 64), ("publication_id", "TP2-FOREIGN"),
                             ("unexpected", True), ("run_request_id", "foreign-open")):
            spec = dict(self.spec, **{field: value})
            with self.subTest(field=field), self.assertRaises(h.HistoricalIntakeError):
                h.freeze_intake(spec, self.context, root=self.root)
        self.assertFalse((self.root / h.INTAKE_ROOT).exists())

    def test_scientific_output_drift_cannot_be_intaken(self):
        old = json.loads((self.root / self.target["result_pin"]["path"]).read_text())
        scientific_paths = [row["path"] for row in old["output_manifest"]]
        scientific_paths += [self.target[key]["path"] for key in ("result_pin", "execution_pin")]
        expected_bytes = {relative: (self.root / relative).read_bytes() for relative in scientific_paths}
        path = self.root / old["return_path"]
        expected_bytes[old["return_path"]] += b"drift"
        path.write_bytes(expected_bytes[old["return_path"]])
        self.assertNotEqual(old["return_sha256"].removeprefix("sha256:"), hashlib.sha256(path.read_bytes()).hexdigest())
        result_bytes = {p.relative_to(self.root): p.read_bytes() for p in (self.root / "research_result_records").rglob("*.json")}
        with mock.patch.object(h.tx, "commit") as commit, self.assertRaisesRegex(h.HistoricalIntakeError, "byte drift"):
            self.intake()
        commit.assert_not_called()
        for relative, raw in expected_bytes.items():
            self.assertEqual(raw, (self.root / relative).read_bytes())
        self.assertEqual(result_bytes, {p.relative_to(self.root): p.read_bytes() for p in (self.root / "research_result_records").rglob("*.json")})
        self.assertFalse((self.root / h.INTAKE_ROOT).exists())
        self.assertFalse((self.root / h.REVIEW_ROOT).exists())

    def test_canonical_result_authority_rejection_keeps_intake_error_and_cause(self):
        from control_plane.research_result_authority_fault_isolation import ResultAuthorityIsolationError
        from tools import research_task_records
        cause = ResultAuthorityIsolationError("exact dependency byte drift: fixture")
        with mock.patch.object(research_task_records, "current_records", side_effect=cause), \
             mock.patch.object(h, "_authority") as authority, mock.patch.object(h.tx, "commit") as commit:
            with self.assertRaisesRegex(h.HistoricalIntakeError, "exact dependency byte drift") as caught:
                self.intake()
        self.assertIs(caught.exception.__cause__, cause)
        authority.assert_not_called()
        commit.assert_not_called()
        self.assertFalse((self.root / h.INTAKE_ROOT).exists())

    def test_unrelated_current_view_error_is_not_reclassified(self):
        from tools import research_task_records
        cause = ValueError("unrelated current-view failure")
        with mock.patch.object(research_task_records, "current_records", side_effect=cause), \
             mock.patch.object(h.tx, "commit") as commit:
            with self.assertRaises(ValueError) as caught:
                self.intake()
        self.assertIs(caught.exception, cause)
        self.assertNotIsInstance(caught.exception, h.HistoricalIntakeError)
        commit.assert_not_called()
        self.assertFalse((self.root / h.INTAKE_ROOT).exists())

    def test_foreign_session_epoch_gov_scope_and_stale_authorization_reject(self):
        for field, value in (("session_id", "other-chat"), ("ownership_epoch", 42), ("governance_task_id", "GV-OTHER")):
            context = copy.deepcopy(self.context)
            context["principal"][field] = value
            with self.subTest(field=field), self.assertRaises(h.HistoricalIntakeError):
                h.freeze_intake(self.spec, context, root=self.root)
        context = copy.deepcopy(self.context)
        context["authorized_at"] = (self.now - timedelta(minutes=10)).isoformat()
        with self.assertRaisesRegex(h.HistoricalIntakeError, "fresh"):
            h.freeze_intake(self.spec, context, root=self.root)

    def test_untrusted_or_edited_server_claim_is_not_current_principal(self):
        for change in ({"author_association": "NONE"}, {"updated_at": (self.now + timedelta(seconds=1)).isoformat()}):
            context = copy.deepcopy(self.context)
            context["server_comments"][0].update(change)
            with self.subTest(change=change), self.assertRaises(h.HistoricalIntakeError):
                h.freeze_intake(self.spec, context, root=self.root)

    def test_contribution_overlap_cannot_accept_historical_author_even_new_identity(self):
        with self.assertRaisesRegex(h.HistoricalIntakeError, "contributed"):
            self.review(self.intake(), contributors=["EM-PCF7FIX-B603FA", "EM-DVR-FIXHRV"])
        self.assertFalse((self.root / h.REVIEW_ROOT).exists())

    def test_payload_change_and_review_artifact_drift_invalidate_read_view(self):
        intake = self.intake()
        reviewed = self.review(intake)
        path = self.root / reviewed["record"]["review_artifact_pin"]["path"]
        path.write_bytes(path.read_bytes() + b"drift")
        with self.assertRaisesRegex(h.HistoricalIntakeError, "byte drift"):
            h.task_state(self.target["task_id"], self.target["publication_id"], root=self.root)

    def test_unknown_ordinary_receipt_kind_cannot_borrow_review_authority(self):
        with self.assertRaisesRegex(ValueError, "unknown"):
            writes.build_receipt({}, "HISTORICAL_RESULT_INTAKE", {})
        self.assertIn("unknown", writes.receipt_error({}, "HISTORICAL_RESULT_INTAKE", self.root))

    def test_current_target_claim_is_preserved_when_intake_becomes_reviewable(self):
        state = {"dispatch_state": "LEASED", "state": "IN_PROGRESS", "claim_id": "other-live-claim", "session_id": "other-chat"}
        result_state = h.task_state(self.target["task_id"], self.target["publication_id"], root=self.root) if self.intake() else None
        reduced = research_dispatch._overlay_result_state({}, state, self.root, result_state)
        self.assertEqual("other-live-claim", reduced["claim_id"])
        self.assertEqual("other-chat", reduced["session_id"])
        self.assertEqual("LEASED", reduced["dispatch_state"])

    def test_actual_existing_target_claim_survives_filter_and_reduce_after_intake(self):
        from tools import research_task_records
        target = research_task_records.current_records(self.root)[self.target["task_id"]]
        actor, session, claim = "EM-HRI-FIXAAA", "another-active-chat", "fixture-target-existing"
        at = self.now - timedelta(seconds=10)
        intent = research_execution_records.prepare_intent(task_id=target["task_id"], claim_id=claim, researcher_id=actor,
            theorem_owner=target["owner"], execution_branch="research/fixture-target-existing", execution_branch_base=SOURCE,
            allowed_outputs=["research_artifacts/fixture-existing/"], owner_lease_minutes=120, prepared_at=at.isoformat(), root=self.root)
        self.write(f"research_execution_records/{target['task_id']}/{intent['execution_record_id']}.json", intent)
        body = {"schema": research_dispatch.EVENT_SCHEMA, "event": "CLAIM", "task_id": target["task_id"],
            "publication_id": target["publication_id"], "claim_id": claim, "researcher_id": actor, "session_id": session, "lease_minutes": 120}
        raw = {"id": 9900000000, "body": json.dumps(body), "created_at": at.isoformat(), "updated_at": at.isoformat(),
            "issue_url": "https://api.github.com/repos/awdawmip/enterprise-math/issues/240", "user": {"login": "owner", "id": 7}, "author_association": "OWNER"}
        events = research_dispatch.events_from_github_comments([raw], root=self.root)
        intake = self.intake()
        definition = research_dispatch.registered_definition(target, self.root)
        actual = research_dispatch.reduce_definition(definition, events, now=self.now + timedelta(seconds=1), root=self.root)
        self.assertEqual(claim, actual["claim_id"])
        self.assertEqual(session, actual["session_id"])
        self.assertEqual("LEASED", actual["dispatch_state"])
        self.review(intake)
        after_review = research_dispatch.reduce_definition(definition, events, now=datetime.now(timezone.utc), root=self.root)
        self.assertEqual(claim, after_review["claim_id"])
        self.assertEqual(session, after_review["session_id"])
        self.assertEqual("LEASED", after_review["dispatch_state"])

    def test_historical_acceptance_does_not_accept_or_stall_later_ordinary_result(self):
        from contextlib import contextmanager
        self.review(self.intake())
        ordinary = {"task_id": self.target["task_id"], "publication_id": self.target["publication_id"], "result_id": "RR-LATER-ORDINARY"}
        ordinary_state = {"state": "AWAITING_DRIVER_REVIEW", "result": ordinary, "review": None, "terminal": False}
        @contextmanager
        def no_hold(_root):
            yield {}
        # Isolate the existing ordinary reducer/Result admission, exercised by
        # its own tests. This boundary test keeps actual HRI/DA/science/review
        # validation and proves its accepted verdict cannot override that flow.
        with mock.patch.object(research_result_records, "iter_results", return_value=[ordinary]), \
             mock.patch.object(research_result_records._result_authority, "authority_snapshot", no_hold), \
             mock.patch.object(research_result_records, "_task_result_state_operational", return_value=copy.deepcopy(ordinary_state)):
            actual = research_result_records.task_result_state(self.target["task_id"], self.root, self.target["publication_id"])
        self.assertEqual("RR-LATER-ORDINARY", actual["result"]["result_id"])
        self.assertEqual("AWAITING_DRIVER_REVIEW", actual["state"])
        self.assertFalse(actual["terminal"])
        self.assertFalse(actual["historical_review_inherited"])
        self.assertEqual("TERMINAL", actual["historical_intake_review_state"])

    def test_revision_then_exact_set_fresh_review_retry_never_latest_wins(self):
        intake = self.intake()
        first = self.review(intake, "REQUEST_REVISION")
        before = (self.root / first["record_path"]).read_bytes()
        second = self.review(intake, "ACCEPTED")
        self.assertEqual([first["record"]["review_id"]], [row["review_id"] for row in second["record"]["previous_review_set"]])
        self.assertEqual(before, (self.root / first["record_path"]).read_bytes())
        latest_bytes = (self.root / second["record_path"]).read_bytes()
        retry = h.freeze_review(self.last_review_spec, self.last_review_context, root=self.root)
        self.assertFalse(retry["created"])
        self.assertEqual(latest_bytes, (self.root / second["record_path"]).read_bytes())
        self.assertTrue(h.task_state(self.target["task_id"], self.target["publication_id"], root=self.root)["terminal"])
        stale = dict(self.last_review_spec, supersedes_review_ids=[], expected_previous_review_set_sha256=h.review_set_digest([]), disposition="REJECTED")
        with self.assertRaisesRegex(h.HistoricalIntakeError, "complete current head set"):
            h.freeze_review(stale, self.last_review_context, root=self.root)

    def test_real_continuation_packet_reads_typed_handle_without_er_alias_or_old_review(self):
        from control_plane import research_continuation as continuation
        self.intake()
        self.mark_published()
        packet = continuation.continuation_packet(self.target["task_id"], root=self.root, events=[],
            now=datetime.now(timezone.utc), source_commit=SOURCE, reader_driver_id=self.driver, reader_session_id=self.session)
        self.assertEqual("AWAITING_DRIVER_REVIEW", packet["result_state"]["state"])
        self.assertEqual("RESEARCH_DRIVER", packet["route"]["required_role"])
        paths = {row["path"] for row in packet["source_artifacts"]}
        self.assertTrue(any(path.startswith(h.INTAKE_ROOT + "/") for path in paths))
        self.assertIn(self.target["execution_pin"]["path"], paths)
        self.assertFalse(any("research_result_records/" in row["path"] and "/HRI-" in row["path"] for row in packet["artifact_errors"]))
        self.assertFalse(any("research_execution_records/" + self.target["task_id"] + "/ER-E90" in row["path"] for row in packet["artifact_errors"]))

    def test_real_released_gov_same_session_prepare_resume_preserves_frontier(self):
        from control_plane import research_continuation as continuation
        comments = copy.deepcopy(self.context["server_comments"])
        handoff = json.loads(comments[0]["body"])
        handoff.update(event="HANDOFF", handoff_scope="CONTINUATION", progress_ref=self.gov_pub["publication_id"], next_action="resume saved governance")
        at = datetime.now(timezone.utc)
        comments.append({**comments[0], "id": 9900000004, "body": json.dumps(handoff), "created_at": at.isoformat(), "updated_at": at.isoformat()})
        self.mark_published()
        pin = continuation.artifact_pin(self.root, self.gov_pub["taskbook_path"], SOURCE)
        frontier = {"source_commit": SOURCE, "artifacts": [pin], "completed_units": ["saved scoped driver checkpoint"],
            "do_not_repeat": ["old scientific correction"], "contributor_ids": [self.driver],
            "current_unfinished_unit": "prospective intake", "next_action": "continue current driver governance"}
        events = research_dispatch.events_from_github_comments(comments, root=self.root)
        prepared = continuation.prepare_takeover(self.gov, root=self.root, events=events, now=at + timedelta(seconds=1), source_commit=SOURCE,
            new_researcher_id=self.driver, new_session_id=self.session, new_claim_id="fixture-hri-resumed",
            execution_branch="research/fixture-hri-resumed", execution_branch_base=SOURCE, allowed_outputs=["research_artifacts/fixture-hri/"],
            expected_previous_claim_id="fixture-hri-claim", expected_previous_comment_id=9900000002, frontier=frontier, reason="same active authenticated chat resumes released work")
        self.assertEqual("RESUME", prepared["claim_event"]["continuation"]["mode"])
        self.assertEqual(self.session, prepared["claim_event"]["continuation"]["previous_session_id"])
        self.assertEqual(frontier, prepared["claim_event"]["continuation"]["frontier"])
        with self.assertRaisesRegex(continuation.ContinuationError, "session"):
            continuation.prepare_takeover(self.gov, root=self.root, events=events, now=at + timedelta(seconds=1), source_commit=SOURCE,
                new_researcher_id=self.driver, new_session_id="other-chat", new_claim_id="fixture-foreign",
                execution_branch="research/fixture-foreign", execution_branch_base=SOURCE, allowed_outputs=["research_artifacts/fixture-hri/"],
                expected_previous_claim_id="fixture-hri-claim", expected_previous_comment_id=9900000002, frontier=frontier, reason="foreign chat")


if __name__ == "__main__":
    unittest.main()
