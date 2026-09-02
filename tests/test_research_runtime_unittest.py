import json
import unittest
from pathlib import Path

from tools import research_runtime as rt

ROOT = Path(__file__).resolve().parents[1]


def ts(value):
    return rt.parse_time(value)


def make_state(**overrides):
    base = {
        "parent_objective": {"objective_id": "OBJ-1", "status": "OPEN"},
        "task_registration": {"registry_key": "RS-T1", "state": "CLAIMABLE"},
        "task": {
            "task_id": "RS-T1",
            "status": "ACTIVE",
            "taskbook_source": "abc123",
            "owner_branch": "research/t1",
        },
        "owner_claim": {
            "claim_id": "claim-1",
            "researcher_id": "EM-T1-ABC123",
            "owner_lease_until": "2026-08-26T12:00:00+08:00",
        },
        "session": {
            "session_id": "s1",
            "last_activity_at": "2026-08-25T12:00:00+08:00",
        },
        "durable_frontier": {
            "remote_head": "deadbeef",
            "execution_stamp": "stamp-1",
            "durable_outputs": ["return.md"],
        },
        "current_unfinished_unit": "prove unit B",
        "next_action": {"description": "prove unit B", "executable": True},
        "terminal_scope": None,
        "final_allowed": False,
        "control": {},
    }
    base.update(overrides)
    return base


def make_evidence(**overrides):
    value = {
        "taskbook_source": "abc123",
        "owner_branch": "research/t1",
        "claim_id": "claim-1",
        "remote_head": "deadbeef",
        "execution_stamp": "stamp-1",
        "durable_outputs": ["return.md"],
        "durable_frontier_verified": True,
    }
    value.update(overrides)
    return value


class ResearchRuntimeTransitionTests(unittest.TestCase):
    def test_unregistered_new_task_cannot_materialize_runtime(self):
        state = make_state(task_registration={"registry_key": "RS-T1", "state": "UNREGISTERED"})
        with self.assertRaisesRegex(rt.RuntimeStateError, "register the task"):
            rt.pre_final_gate(state)

    def test_missing_task_registration_cannot_materialize_runtime(self):
        state = make_state()
        state.pop("task_registration")
        with self.assertRaisesRegex(rt.RuntimeStateError, "task_registration"):
            rt.pre_final_gate(state)

    def test_registry_key_must_match_task_id(self):
        state = make_state(task_registration={"registry_key": "RS-OTHER", "state": "CLAIMABLE"})
        with self.assertRaisesRegex(rt.RuntimeStateError, "registry_key"):
            rt.pre_final_gate(state)

    def test_non_v2_registration_cannot_execute(self):
        state = make_state(task_registration={"state": "LEGACY_BASELINE_REGISTERED"})
        with self.assertRaisesRegex(rt.RuntimeStateError, "not executable"):
            rt.pre_final_gate(state)

    def test_tool_success_parent_open_next_action_physically_rejects_final_decision(self):
        state = make_state()
        state["runtime_phase"] = "TOOL_SUCCESS"
        decision = rt.pre_final_gate(state)
        self.assertEqual(decision["transition"], "EXECUTE_NEXT_ACTION")
        self.assertFalse(decision["canonical_final_allowed"])

    def test_task_publication_is_subflow_and_preserves_current_frontier(self):
        out = rt.apply_terminal_event(make_state(), "TASK_PUBLISHED")
        self.assertEqual(out["terminal_scope"], "SUBFLOW")
        self.assertEqual(out["runtime_phase"], "REEVALUATE_PARENT")
        self.assertEqual(out["current_unfinished_unit"], "prove unit B")
        self.assertEqual(out["next_action"]["description"], "prove unit B")
        self.assertFalse(out["final_allowed"])

    def test_subflow_complete_returns_to_parent(self):
        out = rt.apply_terminal_event(make_state(), "SUBFLOW_COMPLETE")
        self.assertEqual(out["terminal_scope"], "SUBFLOW")
        self.assertEqual(out["runtime_phase"], "REEVALUATE_PARENT")
        self.assertFalse(out["final_allowed"])

    def test_task_frozen_returns_to_parent(self):
        out = rt.apply_terminal_event(make_state(), "TASK_FROZEN")
        self.assertEqual(out["terminal_scope"], "TASK")
        self.assertEqual(out["task"]["status"], "FROZEN")
        self.assertEqual(out["runtime_phase"], "REEVALUATE_PARENT")
        self.assertFalse(out["final_allowed"])

    def test_consistent_parent_complete_passes_pre_final(self):
        state = make_state(
            current_unfinished_unit=None,
            next_action=None,
            task={"task_id": "RS-T1", "status": "COMPLETE", "taskbook_source": "abc123", "owner_branch": "research/t1"},
        )
        out = rt.apply_terminal_event(state, "PARENT_OBJECTIVE_COMPLETE")
        self.assertEqual(out["terminal_scope"], "PARENT_OBJECTIVE")
        self.assertEqual(out["runtime_phase"], "PRE_FINAL")
        self.assertTrue(out["final_allowed"])
        self.assertEqual(out["pre_final_decision"]["transition"], "FINAL_ALLOWED")

    def test_contradictory_parent_complete_with_unfinished_work_fails_closed(self):
        out = rt.apply_terminal_event(make_state(), "PARENT_OBJECTIVE_COMPLETE")
        self.assertFalse(out["final_allowed"])
        self.assertEqual(out["pre_final_decision"]["transition"], "CONTROL_STATE_INCONSISTENT")

    def test_long_owner_lease_does_not_extend_ten_minute_session(self):
        view = rt.classify_session(
            {"claim_id": "claim-1", "owner_lease_until": "2026-08-26T12:00:00+08:00"},
            {"last_activity_at": "2026-08-25T12:00:00+08:00"},
            now=ts("2026-08-25T12:11:00+08:00"),
        )
        self.assertTrue(view["owner_lease_active"])
        self.assertEqual(view["session_state"], "STALE_RECOVERABLE")
        self.assertTrue(view["adoption_allowed"])

    def test_scheduler_lease_is_owner_only_and_stale_dispatch_adopts(self):
        decision = rt.dispatch_decision(
            {"state": "IN_PROGRESS", "dispatch_state": "LEASED", "claim_id": "claim-1", "researcher_id": "EM-T1-ABC123", "lease_until": "2026-08-26T12:00:00+08:00"},
            session_last_activity_at="2026-08-25T12:00:00+08:00",
            now=ts("2026-08-25T12:11:00+08:00"),
        )
        self.assertEqual(decision["action"], "ADOPT_OWNER_CLAIM")
        self.assertTrue(decision["owner_claim_preserved"])
        self.assertFalse(decision["new_claim_required"])

    def test_unknown_session_liveness_never_counts_as_live_chat(self):
        decision = rt.dispatch_decision(
            {"state": "IN_PROGRESS", "dispatch_state": "LEASED", "claim_id": "claim-1", "lease_until": "2026-08-26T12:00:00+08:00"},
            session_last_activity_at=None,
            now=ts("2026-08-25T12:11:00+08:00"),
        )
        self.assertEqual(decision["action"], "VERIFY_SESSION_LIVENESS")
        self.assertFalse(decision["new_claim_required"])

    def test_stale_adoption_preserves_claim_identity_and_does_not_replay(self):
        out = rt.adopt_stale_session(make_state(), make_evidence(), replacement_session_id="replacement", now=ts("2026-08-25T12:11:00+08:00"))
        self.assertEqual(out["owner_claim"]["claim_id"], "claim-1")
        self.assertEqual(out["owner_claim"]["researcher_id"], "EM-T1-ABC123")
        self.assertFalse(out["adoption"]["claim_reissued"])
        self.assertFalse(out["adoption"]["completed_units_replayed"])
        self.assertEqual(out["adoption"]["resume_unit"], "prove unit B")

    def test_stale_adoption_rejects_every_durable_frontier_mismatch(self):
        for bad, marker in (
            (make_evidence(remote_head="other"), "remote_head"),
            (make_evidence(execution_stamp="other"), "execution_stamp"),
            (make_evidence(durable_outputs=["other.md"]), "durable_outputs"),
        ):
            with self.subTest(marker=marker):
                with self.assertRaisesRegex(rt.RuntimeStateError, marker):
                    rt.adopt_stale_session(make_state(), bad, replacement_session_id="replacement", now=ts("2026-08-25T12:11:00+08:00"))

    def test_expired_owner_claim_cannot_be_adopted(self):
        state = make_state(owner_claim={"claim_id": "claim-1", "researcher_id": "EM-T1-ABC123", "owner_lease_until": "2026-08-25T12:05:00+08:00"})
        view = rt.classify_session(state["owner_claim"], state["session"], now=ts("2026-08-25T12:11:00+08:00"))
        self.assertEqual(view["session_state"], "STALE_UNOWNED")
        self.assertFalse(view["adoption_allowed"])

    def test_universal_router_and_taskbook_inheritance_expose_runtime_and_registry(self):
        agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
        contract = json.loads((ROOT / "research_taskbook_contract.json").read_text(encoding="utf-8"))
        policy = json.loads((ROOT / "research_taskbook_policy.json").read_text(encoding="utf-8"))
        final = json.loads((ROOT / "final_response_identity_policy.json").read_text(encoding="utf-8"))
        for marker in (
            "OWNER_LEASE != SESSION_LIVENESS",
            "SESSION_STALE + OWNER_LEASE_ACTIVE -> STALE_RECOVERABLE",
            "TASK_FROZEN -> REEVALUATE_PARENT",
            "RUNTIME_FINAL_ALLOWED_FALSE -> FINAL_CHANNEL_FORBIDDEN",
            "OFFICIAL_NEW_TASK -> IMMUTABLE_V2_TASK_PUBLICATION_RECORD",
            "UNPUBLISHED_TASK -> NO READY / NO CLAIM / NO EXECUTION",
        ):
            self.assertIn(marker, agents)
        self.assertEqual(contract["runtime_state_machine"], "research_runtime_state_machine.json")
        self.assertEqual(contract["task_record_store"], "research_task_records/<task-id>/<publication-id>.json")
        self.assertEqual(contract["publication_contract"]["researcher_driver_approval_required"], False)
        self.assertIn("research_task_publication_contract_v2.json", policy["policy_inputs"])
        self.assertEqual(final["final_permission_authority"], "research_runtime_state_machine.json")
        self.assertEqual(final["pre_final_permission_gate"]["evaluator"], "research_pre_final_authority.py")
        self.assertEqual(final["pre_final_permission_gate"]["registration_guard"], "tools/research_runtime_guard.py")
        self.assertEqual(final["pre_final_permission_gate"]["parent_closure_authority"], "research_parent_closure.py")
        self.assertFalse(final["pre_final_permission_gate"]["caller_supplied_registration_is_authority"])
        self.assertFalse(final["pre_final_permission_gate"]["caller_supplied_parent_status_is_authority"])

    def test_runtime_owns_control_tools_in_exact_owner_surface(self):
        runtime = json.loads((ROOT / "research_runtime_state_machine.json").read_text(encoding="utf-8"))
        self.assertEqual(
            set(runtime["repository_tool_paths"]),
            {
                "tools/active_turn_liveness.py",
                "tools/research_cohort_runtime.py",
                "tools/research_dispatch.py",
                "tools/research_execution_records.py",
                "tools/research_lane_claims.py",
                "tools/research_lane_dispatch.py",
                "tools/research_result_records.py",
                "tools/research_runtime.py",
                "tools/research_runtime_guard.py",
                "tools/research_task_records.py",
                "tools/research_runtime_reducer.py",
            },
        )
        self.assertEqual(runtime["executable_runtime"], "tools/research_runtime_guard.py")
        text = (ROOT / "docs/RESEARCH_RUNTIME_STATE_MACHINE.md").read_text(encoding="utf-8")
        for path in runtime["repository_tool_paths"]:
            self.assertIn(path, text)


if __name__ == "__main__":
    unittest.main()
