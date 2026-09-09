"""Driver assignment selects a registered researcher scope, never a CLAIM."""
from __future__ import annotations

import copy
import hashlib
import io
import json
from contextlib import nullcontext, redirect_stdout
from datetime import datetime, timezone
from pathlib import Path
import tempfile
import unittest
from unittest import mock

import research_control_dispatch as router
from control_plane import research_task_assignment as assignment
from control_plane import researcher_startup_packet as startup
from tests.test_research_driver_authority import DRIVER, contract, policy, record, write_json
from tests.test_research_task_record_compatibility import _write_current_record, _write_semantic_fixture
from tools import research_execution_records, research_taskbook

NOW = datetime(2026, 9, 9, 13, 0, tzinfo=timezone.utc)
TASK = "RS-DRIVER-ASSIGNED-FIXTURE"
PUB = "TP2-DRIVER-ASSIGNED-FIXTURE"
PARENT = "OBJ-DRIVER-ASSIGNED-FIXTURE"
RESEARCHER = "EM-TYPED-ABC123"
SESSION = "fixture-research-session-A"


class AssignedResearchTaskDispatchTests(unittest.TestCase):
    def setUp(self):
        directory = tempfile.TemporaryDirectory(prefix="em-assigned-research-")
        self.addCleanup(directory.cleanup)
        self.root = Path(directory.name)
        _write_semantic_fixture(self.root)
        self.publication = _write_current_record(
            self.root, task_id=TASK, publication_id=PUB, parent_objective_id=PARENT,
            kind="RESEARCH", owner="taskbook/unassigned", claimable=True,
            published_at="2026-09-09T11:00:00Z")
        self.publication_path = self.root / "research_task_records" / TASK / (PUB + ".json")
        self.book = self.root / self.publication["taskbook_path"]
        write_json(self.root / "research_driver_authority_contract.json", contract())
        write_json(self.root / "research_control_event_authorization.json", policy())
        self.authority = record()
        self.authority_path = self.root / "research_driver_authority_records" / DRIVER / (self.authority["authority_record_id"] + ".json")
        body = json.loads(self.authority["source_body"])
        body[assignment.SCOPE_FIELD] = {"parent_objective_ids": [PARENT]}
        self.set_authority_body(body)
        self.raw_assignment = self.comment()
        self.request = {
            "schema": assignment.SCHEMA, "driver_id": DRIVER,
            "driver_authority_record_id": self.authority["authority_record_id"],
            "driver_authority_record_sha256": self.authority_hash(),
            "task_id": TASK, "publication_id": PUB, "parent_objective_id": PARENT,
            "researcher_id": RESEARCHER, "session_id": SESSION, "executor_role": "RESEARCHER",
            "assignment_comment_id": self.raw_assignment["id"],
            "assignment_body_sha256": self.body_hash(self.raw_assignment),
            "expected_claim_id": None,
        }
        self.state = {"task_id": TASK, "publication_id": PUB, "kind": "RESEARCH",
                      "owner": "taskbook/unassigned", "state": "READY", "dispatch_state": "NEEDS_DISPATCH",
                      "priority": "P2", "claim_id": None, "hard_block": None}
        write_json(self.root / "research_context_budget.json", {
            "researcher_cold_start_envelope": {"compact_packet_hard_max_bytes": 8192,
                                               "normal_remote_source_reads_before_math_max": 2}})
        (self.root / "research_runtime_policy_v2.json").write_bytes(
            (router.ROOT / "research_runtime_policy_v2.json").read_bytes())

    @staticmethod
    def body_hash(comment):
        return "sha256:" + hashlib.sha256(comment["body"].encode()).hexdigest()

    def authority_hash(self):
        return "sha256:" + hashlib.sha256(self.authority_path.read_bytes()).hexdigest()

    def set_authority_body(self, body):
        self.authority["source_body"] = json.dumps(body)
        self.authority["source_body_sha256"] = "sha256:" + hashlib.sha256(self.authority["source_body"].encode()).hexdigest()
        write_json(self.authority_path, self.authority)
        if hasattr(self, "request"):
            self.request["driver_authority_record_sha256"] = self.authority_hash()

    def comment(self, cid=9100, *, event=assignment.ASSIGN, at="2026-09-09T12:00:00Z", **changes):
        body = {"schema": "ENTERPRISE_MATH_SCHEDULER_EVENT_V1", "event": event,
                "driver_id": DRIVER, "driver_authority_record_id": self.authority["authority_record_id"],
                "driver_authority_source_comment_id": self.authority["source_comment_id"],
                "task_id": TASK, "publication_id": PUB, "parent_objective_id": PARENT,
                "researcher_id": RESEARCHER, "session_id": SESSION, "executor_role": "RESEARCHER", **changes}
        return {"id": cid, "issue_url": "https://api.github.com/repos/awdawmip/enterprise-math/issues/240",
                "user": {"login": "owner", "id": 7}, "author_association": "OWNER",
                "created_at": at, "updated_at": at, "body": json.dumps(body)}

    def events(self, comments=None):
        return router.research_dispatch.events_from_github_comments(
            [self.raw_assignment] if comments is None else comments, root=self.root)

    def route(self, *, request=None, comments=None, state=None, observations=None, kind="RESEARCH", real_reducer=False):
        chosen = self.state if state is None else state
        reducer = nullcontext() if real_reducer else mock.patch.object(router.research_dispatch, "reduce_definition", return_value=chosen)
        with reducer, \
             mock.patch.object(router.research_dispatch, "_dispatch_result_read_snapshot", return_value=nullcontext()), \
             mock.patch.object(router.research_dispatch, "effective_states", side_effect=AssertionError("unrelated global scan")):
            return router.route_control(self.events(comments), now=NOW, observations=observations,
                                        kind=kind, root=self.root,
                                        assigned_research_task=self.request if request is None else request)

    def leased(self, owner=RESEARCHER):
        self.state.update(state="CLAIMED", dispatch_state="LEASED", claim_id="fixture-winning-claim",
                          researcher_id=owner, lease_until="2026-09-09T14:00:00Z")
        self.request["expected_claim_id"] = self.state["claim_id"]

    def observation(self, *, at="2026-09-09T12:59:00Z", **changes):
        row = {"task_id": TASK, "claim_id": self.state["claim_id"], "session_id": SESSION,
               "activity_evidence_kind": "DURABLE_EXECUTION_PROGRESS", "last_verified_activity_at": at, **changes}
        return router.parse_session_observations({"schema": router.SESSION_OBSERVATION_SCHEMA, "observations": [row]})

    def test_fresh_assignment_selects_exact_researcher_without_global_priority_or_authority_grant(self):
        route = self.route()
        self.assertEqual(route["action"], "CLAIM_NEW_OWNER")
        self.assertEqual(route["target"]["task_id"], TASK)
        self.assertEqual(route["researcher_id"], RESEARCHER)
        self.assertNotEqual(route["researcher_id"], DRIVER)
        self.assertEqual(route["assigned_research_selection"]["assignment_comment_id"], 9100)
        self.assertTrue(route["assigned_research_selection"]["eligible"])
        self.assertFalse(route["assigned_research_selection"]["execution_authorized"])
        self.assertFalse(route["assigned_research_selection"]["preclaim_selection_reconstructed"])
        self.assertEqual(route["next_control_steps"][0], "tools/research_execution_records.py prepare")

    def test_real_reducer_ignores_assignment_as_claim_or_progress(self):
        route = self.route(real_reducer=True)
        self.assertEqual(route["action"], "CLAIM_NEW_OWNER")
        self.assertIsNone(route["target"]["claim_id"])
        self.assertIsNone(route["target"]["lease_until"])
        self.assertTrue(any("unknown event type" in row["reason"] for row in route["target"]["ignored_events"]))

    def test_current_prepare_remains_a_separate_non_authorizing_intent(self):
        selected = self.route()
        intent = research_execution_records.prepare_intent(
            task_id=selected["target"]["task_id"], claim_id="future-actual-claim-id",
            researcher_id=selected["researcher_id"], theorem_owner=PARENT,
            execution_branch="research/assigned-fixture", execution_branch_base="a" * 40,
            allowed_outputs=["research_artifacts/assigned-fixture/**"], owner_lease_minutes=120,
            prepared_at=NOW.isoformat(), root=self.root)
        self.assertEqual(intent["publication_id"], PUB)
        self.assertEqual(intent["researcher_id"], RESEARCHER)
        self.assertEqual(intent["record_state"], "CLAIM_INTENT")
        self.assertFalse((self.root / "research_execution_records").exists())

    def test_untyped_authority_reason_and_gov_binding_do_not_grant_research_scope(self):
        body = json.loads(self.authority["source_body"])
        body.pop(assignment.SCOPE_FIELD)
        body["reason"] = "Delegate research within " + PARENT
        body["assigned_governance_task"] = {"task_id": "GV-FIXTURE", "publication_id": "TP2-GOV", "parent_objective_id": PARENT}
        self.set_authority_body(body)
        with self.assertRaisesRegex(router.ControlDispatchError, "typed research parent"):
            self.route()

    def test_parent_scope_is_exact_and_wildcards_or_duplicate_lists_are_rejected(self):
        for scope in ({"parent_objective_ids": ["OBJ-OTHER"]}, {"parent_objective_ids": ["*"]},
                      {"parent_objective_ids": [PARENT, PARENT]}, {"parent_objective_ids": PARENT},
                      {"parent_objective_ids": [PARENT], "all_tasks": True}):
            with self.subTest(scope=scope):
                body = json.loads(self.authority["source_body"])
                body[assignment.SCOPE_FIELD] = scope
                self.set_authority_body(body)
                with self.assertRaisesRegex(router.ControlDispatchError, "typed research parent"):
                    self.route()

    def test_request_and_event_must_match_receiver_session_and_exact_task_generation(self):
        for field, value in (("task_id", "RS-OTHER"), ("publication_id", "TP2-OTHER"),
                             ("parent_objective_id", "OBJ-OTHER"), ("researcher_id", "EM-TYPED-DEF456"),
                             ("session_id", "other-session"), ("assignment_body_sha256", "sha256:" + "0" * 64)):
            with self.subTest(field=field), self.assertRaises(router.ControlDispatchError):
                self.route(request={**self.request, field: value})

    def test_nonobject_authority_body_has_no_research_scope(self):
        self.set_authority_body([])
        with self.assertRaisesRegex(router.ControlDispatchError, "typed research parent"):
            self.route()

    def test_driver_and_steward_identities_are_not_research_recipients(self):
        for recipient in (DRIVER, "EM-DVR-DEF456", "EM-STW-ABC123", "EM-DRIVER-01"):
            with self.subTest(recipient=recipient), self.assertRaisesRegex(router.ControlDispatchError, "RESEARCHER identity"):
                self.route(request={**self.request, "researcher_id": recipient})
        with self.assertRaisesRegex(router.ControlDispatchError, "RESEARCHER identity"):
            self.route(request={**self.request, "executor_role": "RESEARCH_DRIVER"})

    def test_malformed_request_fields_and_cross_kind_cannot_turn_into_arbitrary_filter(self):
        for request in ({}, {**self.request, "task_filter": TASK}, {**self.request, "assignment_comment_id": True},
                        {**self.request, "expected_claim_id": False}, {**self.request, "session_id": ""}):
            with self.subTest(request=request), self.assertRaises(router.ControlDispatchError):
                self.route(request=request)
        for kind in ("GOVERNANCE", "ANY"):
            with self.subTest(kind=kind), self.assertRaisesRegex(router.ControlDispatchError, "kind RESEARCH"):
                self.route(kind=kind)
        with self.assertRaisesRegex(router.ControlDispatchError, "exclusive entries"):
            router.route_control([], now=NOW, root=self.root, assigned_driver_task={}, assigned_research_task=self.request)

    def test_source_envelope_author_edit_and_server_time_are_enforced(self):
        variants = [dict(self.raw_assignment, user={"login": "outsider", "id": 8}),
                    dict(self.raw_assignment, updated_at="2026-09-09T12:01:00Z"),
                    dict(self.raw_assignment, created_at="2026-09-10T12:00:00Z", updated_at="2026-09-10T12:00:00Z"),
                    dict(self.raw_assignment, created_at="2020-01-01T00:00:00Z", updated_at="2020-01-01T00:00:00Z")]
        for raw in variants:
            with self.subTest(raw=raw), self.assertRaises(router.ControlDispatchError):
                self.route(comments=[raw])
        raw = self.comment(at="2026-09-09T12:00:00Z", actor="owner")
        payload = json.loads(raw["body"])
        payload["at"] = "1900-01-01T00:00:00Z"
        raw["body"] = json.dumps(payload)
        route = self.route(comments=[raw], request={**self.request, "assignment_body_sha256": self.body_hash(raw)})
        self.assertEqual(route["assigned_research_selection"]["assignment_created_at"], "2026-09-09T12:00:00+00:00")

    def test_missing_authenticated_metadata_is_not_assignment_evidence(self):
        raw_event = json.loads(self.raw_assignment["body"])
        with self.assertRaisesRegex(assignment.AssignmentError, "absent"):
            assignment.resolve(self.request, [raw_event], now=NOW, root=self.root)

    def test_da_bytes_drift_revoke_and_replacement_do_not_reauthorize_old_assignment(self):
        original = self.authority_path.read_bytes()
        self.authority_path.write_bytes(original + b"\n")
        with self.assertRaisesRegex(router.ControlDispatchError, "bytes changed"):
            self.route()
        self.authority_path.write_bytes(original)
        revoked = record("REVOKE", 9200, "2026-09-09T12:30:00Z")
        rev_path = self.authority_path.with_name(revoked["authority_record_id"] + ".json")
        write_json(rev_path, revoked)
        with self.assertRaisesRegex(router.ControlDispatchError, "current ACTIVE"):
            self.route()

    def test_publication_supersession_and_changed_taskbook_cannot_inherit_selection(self):
        self.book.write_bytes(self.book.read_bytes() + b"\nchanged\n")
        with self.assertRaisesRegex(router.ControlDispatchError, "frozen publication"):
            self.route()
        self.publication["taskbook_blob_sha1"] = router.research_task_records.taskbook_blob(self.book)
        write_json(self.publication_path, self.publication)
        newer = _write_current_record(self.root, task_id=TASK, publication_id="TP2-NEXT-FIXTURE",
            parent_objective_id=PARENT, kind="RESEARCH", claimable=True, owner="taskbook/unassigned",
            publication_generation=2, supersedes_publication_id=PUB)
        with self.assertRaisesRegex(router.ControlDispatchError, "exact current"):
            self.route()
        self.assertNotEqual(newer["publication_id"], self.request["publication_id"])

    def test_replaced_da_needs_a_new_source_assignment_without_relabeling_old_one(self):
        old_assignment = copy.deepcopy(self.raw_assignment)
        self.authority = record("AUTHORIZE", 9200, "2026-09-09T12:30:00Z")
        self.authority_path = self.authority_path.with_name(self.authority["authority_record_id"] + ".json")
        body = json.loads(self.authority["source_body"])
        body[assignment.SCOPE_FIELD] = {"parent_objective_ids": [PARENT]}
        self.set_authority_body(body)
        with self.assertRaisesRegex(router.ControlDispatchError, "current ACTIVE"):
            self.route()
        self.request["driver_authority_record_id"] = self.authority["authority_record_id"]
        with self.assertRaisesRegex(router.ControlDispatchError, "authority/time|absent"):
            self.route()
        fresh = self.comment(9300, at="2026-09-09T12:40:00Z")
        fresh_request = {**self.request, "assignment_comment_id": 9300,
                         "assignment_body_sha256": self.body_hash(fresh)}
        self.assertEqual(self.route(request=fresh_request, comments=[old_assignment, fresh])["action"], "CLAIM_NEW_OWNER")
        self.assertEqual(self.raw_assignment, old_assignment)

    def test_canonical_publication_result_parent_cohort_and_hard_blocks_are_not_bypassed(self):
        for state in ("BLOCKED", "AWAITING_REVIEW", "COMPLETE", "DORMANT", "COHORT_ACTIVE",
                      "PARENT_OBJECTIVE_CLOSED", "PARENT_OBJECTIVE_PARKED"):
            with self.subTest(state=state):
                result = self.route(state={**self.state, "dispatch_state": state})
                self.assertEqual(result["selection_status"], "BLOCKED")
                self.assertEqual(result["target"]["dispatch_state"], "BLOCKED")
                self.assertFalse(result["new_claim_required"])
        for changes in ({"hard_block": {"reason": "prerequisite"}}, {"execution_cohort_id": "COH-FIXTURE"}):
            self.assertEqual(self.route(state={**self.state, **changes})["selection_status"], "BLOCKED")
        for change in ({"claimable": False}, {"kind": "GOVERNANCE"}):
            write_json(self.publication_path, {**self.publication, **change})
            with self.assertRaisesRegex(router.ControlDispatchError, "claimable RESEARCH"):
                self.route()

    def test_nonempty_or_malformed_dependencies_stay_blocked_without_rewriting_task(self):
        original = self.book.read_text(encoding="utf-8")
        for dependencies in ([{"target": "RS-DEPENDENCY", "action": "WAIT"}], ["TP2-REFERENCE"], None):
            meta, body = research_taskbook.split_taskbook(original)
            meta["dependencies"] = dependencies
            self.book.write_text(research_taskbook.render_taskbook(meta, body), encoding="utf-8")
            self.publication["taskbook_blob_sha1"] = router.research_task_records.taskbook_blob(self.book)
            write_json(self.publication_path, self.publication)
            before = self.book.read_bytes()
            result = self.route()
            self.assertEqual(result["selection_status"], "BLOCKED")
            self.assertIn("dependencies", result["reason"])
            self.assertEqual(self.book.read_bytes(), before)

    def test_foreign_owner_and_expected_claim_race_preserve_claim(self):
        self.leased("EM-OTHER-ABC123")
        result = self.route(observations=self.observation(at="2026-09-09T12:00:00Z"))
        self.assertEqual(result["selection_status"], "BLOCKED")
        self.assertTrue(result["owner_claim_preserved"])
        self.assertEqual(result["claim_id"], "fixture-winning-claim")
        self.assertFalse(result["new_claim_required"])
        result = self.route(request={**self.request, "expected_claim_id": None})
        self.assertEqual(result["selection_status"], "BLOCKED")

    def test_exact_owner_session_liveness_drives_keep_verify_or_adopt(self):
        self.leased()
        self.assertEqual(self.route()["action"], "VERIFY_SESSION_LIVENESS")
        self.assertEqual(self.route(observations=self.observation())["action"], "KEEP_CURRENT_SESSION")
        for observations in (self.observation(claim_id="foreign-claim"), self.observation(session_id="foreign-session")):
            self.assertEqual(self.route(observations=observations)["action"], "VERIFY_SESSION_LIVENESS")
        result = self.route(observations=self.observation(at="2026-09-09T12:40:00Z"))
        self.assertEqual(result["action"], "ADOPT_OWNER_CLAIM")
        self.assertEqual(result["required_guard"], "tools/research_runtime_guard.py adopt")
        self.assertEqual(result["claim_id"], self.state["claim_id"])
        self.assertFalse(result["new_claim_required"])
        self.assertFalse(result["assigned_research_selection"]["preclaim_selection_reconstructed"])

    def test_assignment_is_not_session_activity_and_scoped_block_keeps_owner(self):
        self.leased()
        result = self.route()
        self.assertEqual(result["action"], "VERIFY_SESSION_LIVENESS")
        result = self.route(state={**self.state, "dispatch_state": "BLOCKED"})
        self.assertTrue(result["owner_claim_preserved"])
        self.assertFalse(result["assigned_research_selection"]["eligible"])

    def test_competing_assignments_require_explicit_same_driver_revocation(self):
        second = self.comment(9101, researcher_id="EM-TYPED-DEF456", session_id="second-session")
        with self.assertRaisesRegex(router.ControlDispatchError, "multiple active"):
            self.route(comments=[self.raw_assignment, second])
        revoke = self.comment(9102, event=assignment.REVOKE, assignment_comment_id=9100)
        with self.assertRaisesRegex(router.ControlDispatchError, "revoked"):
            self.route(comments=[self.raw_assignment, revoke])
        second_request = {**self.request, "assignment_comment_id": 9101,
                          "assignment_body_sha256": self.body_hash(second),
                          "researcher_id": "EM-TYPED-DEF456", "session_id": "second-session"}
        self.assertEqual(self.route(request=second_request, comments=[self.raw_assignment, second, revoke])["action"], "CLAIM_NEW_OWNER")
        wrong_driver = self.comment(9102, event=assignment.REVOKE, assignment_comment_id=9100, driver_id="EM-DVR-DEF456")
        self.assertEqual(self.route(comments=[self.raw_assignment, wrong_driver])["action"], "CLAIM_NEW_OWNER")

    def test_cli_bridge_and_compact_packet_preserve_typed_selection(self):
        request = json.dumps(self.request)
        with mock.patch("sys.argv", ["research_control_dispatch.py", "--kind", "RESEARCH", "--assigned-research-task-json", request]):
            with self.assertRaisesRegex(router.ControlDispatchError, "actual Issue 240"):
                router.main()
        events_path = self.root / "raw-events.json"
        write_json(events_path, [self.raw_assignment])
        with mock.patch("sys.argv", ["research_control_dispatch.py", "--events", str(events_path),
                                     "--kind", "RESEARCH", "--assigned-research-task-json", request]), \
             mock.patch.object(router, "route_control", return_value={"action": "CLAIM_NEW_OWNER"}) as route, redirect_stdout(io.StringIO()):
            self.assertEqual(router.main(), 0)
        self.assertEqual(route.call_args.kwargs["assigned_research_task"], self.request)
        selected = self.route()
        packet = startup.build_packet({"route": selected, "request_id": "assigned-research-fixture",
                                       "source_sha": "a" * 40, "kind": "RESEARCH"}, self.root)
        self.assertEqual(packet["assigned_research_selection"], selected["assigned_research_selection"])
        self.assertEqual(packet["packet_bytes"], len(startup._serialized_packet(packet)))
        self.assertLessEqual(packet["packet_bytes"], 8192)
        workflow = (router.ROOT / ".github/workflows/chatgpt-control-dispatch-bridge.yml").read_text()
        self.assertIn("--assigned-research-task-json", workflow)
        self.assertIn('has("assigned_driver_task") | not', workflow)


if __name__ == "__main__":
    unittest.main()
