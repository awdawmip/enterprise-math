"""Explicit GOV delegation routes; no CLAIM, DA, or research is published here."""
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
from control_plane import researcher_startup_packet as startup
from tests.test_research_driver_authority import contract, policy, record, DRIVER, write_json
from tests.test_research_task_record_compatibility import _write_current_record, _write_semantic_fixture
from tools import research_taskbook

NOW = datetime(2026, 9, 9, 6, 0, tzinfo=timezone.utc)
TASK = "GV-ASSIGNED-FIXTURE"
PUB = "TP2-ASSIGNED-FIXTURE"
PARENT = "OBJ-ASSIGNED-FIXTURE"


class AssignedGovernanceDriverDispatchTests(unittest.TestCase):
    def setUp(self):
        directory = tempfile.TemporaryDirectory(prefix="em-assigned-gov-")
        self.addCleanup(directory.cleanup)
        self.root = Path(directory.name)
        _write_semantic_fixture(self.root)
        self.publication = _write_current_record(
            self.root, task_id=TASK, publication_id=PUB, parent_objective_id=PARENT,
            claimable=True, kind="GOVERNANCE", owner="governance",
            published_at="2026-09-09T01:00:00Z")
        self.publication_path = self.root.joinpath("research_task_records", TASK, PUB + ".json")
        self.book = self.root.joinpath(self.publication["taskbook_path"])
        write_json(self.root.joinpath("research_driver_authority_contract.json"), contract())
        write_json(self.root.joinpath("research_control_event_authorization.json"), policy())
        self.authority = record()
        body = json.loads(self.authority["source_body"])
        body["assigned_governance_task"] = {"task_id": TASK, "publication_id": PUB,
                                            "parent_objective_id": PARENT}
        self.authority["source_body"] = json.dumps(body)
        self.authority["source_body_sha256"] = "sha256:" + hashlib.sha256(json.dumps(body).encode()).hexdigest()
        self.authority_path = self.root.joinpath("research_driver_authority_records", DRIVER,
                                               self.authority["authority_record_id"] + ".json")
        write_json(self.authority_path, self.authority)
        self.request = {
            "schema": router.ASSIGNED_DRIVER_SCHEMA, "driver_id": DRIVER,
            "task_id": TASK, "publication_id": PUB, "parent_objective_id": PARENT,
            "driver_authority_record_id": self.authority["authority_record_id"],
            "driver_authority_record_sha256": self.authority_hash(),
            "session_id": "fixture-session-A", "expected_claim_id": None,
        }
        self.state = {"task_id": TASK, "publication_id": PUB, "kind": "GOVERNANCE",
                      "state": "READY", "dispatch_state": "NEEDS_DISPATCH",
                      "claim_id": None, "owner": "governance", "hard_block": None}
        write_json(self.root.joinpath("research_context_budget.json"), {
            "researcher_cold_start_envelope": {"compact_packet_hard_max_bytes": 8192,
                                               "normal_remote_source_reads_before_math_max": 2}})
        self.root.joinpath("research_runtime_policy_v2.json").write_bytes(
            router.ROOT.joinpath("research_runtime_policy_v2.json").read_bytes())

    def authority_hash(self):
        return "sha256:" + hashlib.sha256(self.authority_path.read_bytes()).hexdigest()

    def route(self, *, request=None, states=None, observations=None, kind="GOVERNANCE"):
        # The full canonical overlay is independently tested by its owning tests.
        # This fixture isolates selection while exercising actual current-record,
        # taskbook byte pin, DA source validation and runtime session primitives.
        chosen = self.state if states is None else next(s for s in states if s['task_id'] == TASK)
        with mock.patch.object(router.research_dispatch, "reduce_definition", return_value=chosen) as derive, \
             mock.patch.object(router.research_dispatch, "_dispatch_result_read_snapshot", return_value=nullcontext()), \
             mock.patch.object(router.research_dispatch, "effective_states", side_effect=AssertionError("global scan")):
            result = router.route_control([], now=NOW, root=self.root, kind=kind,
                                          observations=observations,
                                          assigned_driver_task=self.request if request is None else request)
        derive.assert_called_once()
        self.assertEqual(derive.call_args.args[0]['task_id'], TASK)
        self.assertEqual(derive.call_args.args[0]['parent_objective_id'], PARENT)
        self.assertEqual(derive.call_args.args[1], [])
        return result

    def leased(self):
        self.state.update(state="CLAIMED", dispatch_state="LEASED", claim_id="fixture-existing-claim",
                          researcher_id=DRIVER, lease_until="2026-09-09T07:00:00Z")
        self.request["expected_claim_id"] = self.state["claim_id"]

    def observation(self, at="2026-09-09T05:59:00Z", **changes):
        row = {"task_id": TASK, "claim_id": self.state["claim_id"],
               "activity_evidence_kind": "DURABLE_EXECUTION_PROGRESS",
               "last_verified_activity_at": at, "session_id": "fixture-session-A", **changes}
        return router.parse_session_observations({"schema": router.SESSION_OBSERVATION_SCHEMA,
                                                  "observations": [row]})

    def test_exact_assigned_gov_does_not_select_unrelated_higher_priority(self):
        other = dict(self.state, task_id="GV-UNASSIGNED-P0", publication_id="TP2-OTHER", priority="P0")
        result = self.route(states=[other, self.state])
        self.assertEqual(result["action"], "CLAIM_NEW_OWNER")
        self.assertEqual(result["target"]["task_id"], TASK)
        self.assertTrue(result["new_claim_required"])
        self.assertFalse(result["assigned_driver_selection"]["execution_authorized"])

    def test_existing_claim_and_live_exact_session_are_preserved(self):
        self.leased()
        result = self.route(observations=self.observation())
        self.assertEqual(result["action"], "KEEP_CURRENT_SESSION")
        self.assertEqual(result["claim_id"], self.state["claim_id"])
        self.assertTrue(result["owner_claim_preserved"])
        self.assertFalse(result["new_claim_required"])
        self.assertEqual(result["assigned_driver_selection"]["mode"], "CURRENT_FORWARD_REVALIDATION")
        self.assertFalse(result["assigned_driver_selection"]["preclaim_selection_reconstructed"])

    def test_unknown_or_foreign_session_cannot_borrow_owner_activity(self):
        self.leased()
        for observations in (None, self.observation(session_id="fixture-session-B"),
                             self.observation(claim_id="foreign-claim")):
            with self.subTest(observations=observations):
                result = self.route(observations=observations)
                self.assertEqual(result["action"], "VERIFY_SESSION_LIVENESS")
                self.assertFalse(result["new_claim_required"])
        result = self.route(observations=self.observation(at="2026-09-09T05:40:00Z"))
        self.assertEqual(result["action"], "ADOPT_OWNER_CLAIM")
        self.assertEqual(result["required_guard"], "tools/research_runtime_guard.py adopt")

    def test_owner_race_foreign_owner_and_expired_revalidation_refuse(self):
        self.leased()
        for changes in ({"claim_id": "changed-claim"}, {"researcher_id": "EM-OTHER-ABC123"},
                        {"claim_id": None, "dispatch_state": "NEEDS_DISPATCH"}):
            with self.subTest(changes=changes), self.assertRaises(router.ControlDispatchError):
                self.route(states=[dict(self.state, **changes)])

    def test_scope_is_exact_not_prose_or_bare_manual_assignment(self):
        for key, value in (("task_id", "GV-OTHER"), ("publication_id", "TP2-OTHER"),
                           ("parent_objective_id", "OBJ-OTHER"), ("driver_id", "EM-DVR-OTHER")):
            with self.subTest(key=key), self.assertRaises(router.ControlDispatchError):
                self.route(request=dict(self.request, **{key: value}))
        body = json.loads(self.authority["source_body"])
        body["reason"] = "Assign " + TASK
        body.pop("assigned_governance_task")
        self.authority["source_body"] = json.dumps(body)
        self.authority["source_body_sha256"] = "sha256:" + hashlib.sha256(json.dumps(body).encode()).hexdigest()
        write_json(self.authority_path, self.authority)
        self.request["driver_authority_record_sha256"] = self.authority_hash()
        with self.assertRaisesRegex(router.ControlDispatchError, "typed GOV delegation"):
            self.route()

    def test_revoked_authority_unauthorized_source_and_da_pin_drift_refuse(self):
        revoked = record("REVOKE", 9002, "2026-09-09T05:00:00Z")
        rev_path = self.authority_path.with_name(revoked["authority_record_id"] + ".json")
        write_json(rev_path, revoked)
        with self.assertRaisesRegex(router.ControlDispatchError, "ACTIVE"):
            self.route()
        rev_path.unlink()
        self.authority_path.write_bytes(self.authority_path.read_bytes() + b"\n")
        with self.assertRaisesRegex(router.ControlDispatchError, "bytes changed"):
            self.route()
        self.authority["source_server_author"]["login"] = "outsider"
        write_json(self.authority_path, self.authority)
        self.request["driver_authority_record_sha256"] = self.authority_hash()
        with self.assertRaisesRegex(router.ControlDispatchError, "not control-authorized"):
            self.route()

    def test_research_and_noncurrent_or_unclaimable_publication_refuse(self):
        with self.assertRaisesRegex(router.ControlDispatchError, "GOVERNANCE only"):
            self.route(kind="RESEARCH")
        for changes in ({"claimable": False}, {"kind": "RESEARCH"},
                        {"parent_objective_id": "OTHER"}, {"publication_id": "TP2-NEW"}):
            with self.subTest(changes=changes):
                write_json(self.publication_path, dict(self.publication, **changes))
                with self.assertRaises(router.ControlDispatchError):
                    self.route()

    def test_closed_result_cohort_parent_and_hard_block_are_not_bypassed(self):
        for dispatch_state in ("BLOCKED", "AWAITING_REVIEW", "COMPLETE", "COHORT_ACTIVE",
                               "PARENT_OBJECTIVE_CLOSED", "PARENT_OBJECTIVE_PARKED"):
            with self.subTest(state=dispatch_state), self.assertRaisesRegex(router.ControlDispatchError, "not executable"):
                self.route(states=[dict(self.state, dispatch_state=dispatch_state)])
        with self.assertRaisesRegex(router.ControlDispatchError, "hard block"):
            self.route(states=[dict(self.state, hard_block={"reason": "pending prerequisite"})])
        with self.assertRaises(router.ControlDispatchError):
            self.route(states=[dict(self.state, execution_cohort_id="COH-FIXTURE")])

    def test_changed_book_and_unresolved_dependency_are_not_bypassed(self):
        original = self.book.read_bytes()
        self.book.write_bytes(original + b"changed\n")
        with self.assertRaisesRegex(router.ControlDispatchError, "frozen publication"):
            self.route()
        self.book.write_bytes(original)
        meta, body = research_taskbook.split_taskbook(self.book.read_text(encoding="utf-8"))
        meta["dependencies"] = [{"target": "GV-PREREQUISITE", "action": "WAIT"}]
        self.book.write_text(research_taskbook.render_taskbook(meta, body), encoding="utf-8")
        self.publication["taskbook_blob_sha1"] = router.research_task_records.taskbook_blob(self.book)
        write_json(self.publication_path, self.publication)
        with self.assertRaisesRegex(router.ControlDispatchError, "dependencies"):
            self.route()

    def test_malformed_request_fields_fail_closed(self):
        for request in ([], {}, dict(self.request, session_id=""), dict(self.request, expected_claim_id=False),
                        dict(self.request, execution_scope=None), dict(self.request, driver_authority_record_id="old")):
            with self.subTest(request=request), self.assertRaises(router.ControlDispatchError):
                self.route(request=request)

    def test_public_cli_forwards_typed_input_and_requires_raw_event_file(self):
        request = json.dumps(self.request)
        with mock.patch("sys.argv", ["research_control_dispatch.py", "--kind", "GOVERNANCE",
                                     "--assigned-driver-task-json", request]):
            with self.assertRaisesRegex(router.ControlDispatchError, "actual Issue 240"):
                router.main()
        events_path = self.root.joinpath("raw-events.json")
        write_json(events_path, [])
        with mock.patch("sys.argv", ["research_control_dispatch.py", "--events", str(events_path),
                                     "--kind", "GOVERNANCE", "--assigned-driver-task-json", request]), \
             mock.patch.object(router, "route_control", return_value={"action": "CLAIM_NEW_OWNER"}) as route, \
             redirect_stdout(io.StringIO()):
            self.assertEqual(router.main(), 0)
        self.assertEqual(route.call_args.kwargs["assigned_driver_task"], self.request)

    def test_bridge_and_compact_packet_preserve_revalidation_without_new_authority(self):
        self.leased()
        route = self.route(observations=self.observation())
        packet = startup.build_packet({"route": route, "request_id": "assigned-fixture",
                                       "source_sha": "a" * 40, "kind": "GOVERNANCE"}, self.root)
        self.assertEqual(packet["assigned_driver_selection"], route["assigned_driver_selection"])
        self.assertFalse(packet["new_claim_required"])
        self.assertEqual(packet["action"], "KEEP_CURRENT_SESSION")
        self.assertEqual(packet["packet_bytes"], len(startup._serialized_packet(packet)))
        self.assertLessEqual(packet["packet_bytes"], 8192)
        workflow = router.ROOT.joinpath(".github/workflows/chatgpt-control-dispatch-bridge.yml").read_text()
        self.assertIn("--assigned-driver-task-json", workflow)
        self.assertEqual(workflow.count('"${assigned_args[@]}"'), 2)
        self.assertIn("Fetch authoritative Issue 240 comment stream", workflow)


if __name__ == "__main__":
    unittest.main()
