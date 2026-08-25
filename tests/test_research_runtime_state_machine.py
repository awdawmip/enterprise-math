import json
from pathlib import Path

import pytest

from tools import research_runtime as rt

ROOT = Path(__file__).resolve().parents[1]


def t(value):
    return rt.parse_time(value)


def state(**overrides):
    base = {
        "parent_objective": {"objective_id": "OBJ-1", "status": "OPEN"},
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


def test_runtime_contract_is_canonical_and_has_required_fields():
    data = json.loads((ROOT / "research_runtime_state_machine.json").read_text(encoding="utf-8"))
    assert data["status"] == "ACTIVE_CANONICAL_RUNTIME"
    assert data["schema"] == "ENTERPRISE_MATH_RESEARCH_RUNTIME_STATE_MACHINE_V1"
    assert data["canonical_state_fields"] == [
        "PARENT_OBJECTIVE",
        "TASK",
        "OWNER_CLAIM",
        "SESSION",
        "DURABLE_FRONTIER",
        "CURRENT_UNFINISHED_UNIT",
        "NEXT_ACTION",
        "TERMINAL_SCOPE",
        "FINAL_ALLOWED",
    ]
    assert data["lease_model"]["session_liveness"]["default_minutes"] == 10
    assert data["lease_model"]["session_liveness"]["must_not_inherit_owner_lease_minutes"] is True


def test_pre_final_rejects_open_parent_with_action():
    decision = rt.pre_final_gate(state())
    assert decision["transition"] == "EXECUTE_NEXT_ACTION"
    assert decision["final_allowed"] is False
    assert decision["canonical_final_allowed"] is False


def test_tool_success_parent_open_next_action_rejects_final():
    current = state()
    current["runtime_phase"] = "TOOL_SUCCESS"
    decision = rt.pre_final_gate(current)
    assert decision["canonical_final_allowed"] is False


def test_subflow_complete_reevaluates_parent_instead_of_final():
    out = rt.apply_terminal_event(state(), "SUBFLOW_COMPLETE")
    assert out["terminal_scope"] == "SUBFLOW"
    assert out["runtime_phase"] == "REEVALUATE_PARENT"
    assert out["final_allowed"] is False


def test_task_frozen_reevaluates_parent_instead_of_final():
    out = rt.apply_terminal_event(state(), "TASK_FROZEN")
    assert out["terminal_scope"] == "TASK"
    assert out["task"]["status"] == "FROZEN"
    assert out["runtime_phase"] == "REEVALUATE_PARENT"
    assert out["final_allowed"] is False


def test_parent_objective_complete_runs_pre_final_and_allows_final():
    out = rt.apply_terminal_event(state(), "PARENT_OBJECTIVE_COMPLETE")
    assert out["terminal_scope"] == "PARENT_OBJECTIVE"
    assert out["parent_objective"]["status"] == "COMPLETE"
    assert out["final_allowed"] is True


def test_1440_minute_owner_lease_does_not_keep_session_alive():
    view = rt.classify_session(
        {
            "claim_id": "c",
            "owner_lease_until": "2026-08-26T12:00:00+08:00",
        },
        {"last_activity_at": "2026-08-25T12:00:00+08:00"},
        now=t("2026-08-25T12:11:00+08:00"),
        session_liveness_minutes=10,
    )
    assert view["owner_lease_active"] is True
    assert view["session_state"] == "STALE_RECOVERABLE"
    assert view["adoption_allowed"] is True


def test_legacy_scheduler_lease_is_owner_only_and_stale_is_adoptable():
    scheduler = {
        "state": "IN_PROGRESS",
        "dispatch_state": "LEASED",
        "claim_id": "c",
        "actor": "old",
        "researcher_id": "EM-T1-ABC123",
        "lease_until": "2026-08-26T12:00:00+08:00",
    }
    decision = rt.dispatch_decision(
        scheduler,
        session_last_activity_at="2026-08-25T12:00:00+08:00",
        now=t("2026-08-25T12:11:00+08:00"),
    )
    assert decision["action"] == "ADOPT_OWNER_CLAIM"
    assert decision["owner_claim_preserved"] is True
    assert decision["new_claim_required"] is False


def test_active_session_does_not_get_preempted():
    scheduler = {
        "state": "IN_PROGRESS",
        "dispatch_state": "LEASED",
        "claim_id": "c",
        "researcher_id": "EM-T1-ABC123",
        "lease_until": "2026-08-26T12:00:00+08:00",
    }
    decision = rt.dispatch_decision(
        scheduler,
        session_last_activity_at="2026-08-25T12:05:00+08:00",
        now=t("2026-08-25T12:10:00+08:00"),
    )
    assert decision["action"] == "KEEP_CURRENT_SESSION"


def test_unknown_session_liveness_is_not_treated_as_live_chat():
    scheduler = {
        "state": "IN_PROGRESS",
        "dispatch_state": "LEASED",
        "claim_id": "c",
        "lease_until": "2026-08-26T12:00:00+08:00",
    }
    decision = rt.dispatch_decision(
        scheduler,
        session_last_activity_at=None,
        now=t("2026-08-25T12:10:00+08:00"),
    )
    assert decision["action"] == "VERIFY_SESSION_LIVENESS"
    assert decision["new_claim_required"] is False


def test_stale_adoption_preserves_claim_identity_and_resumes_frontier():
    out = rt.adopt_stale_session(
        state(),
        {
            "taskbook_source": "abc123",
            "owner_branch": "research/t1",
            "claim_id": "claim-1",
            "remote_head": "deadbeef",
            "execution_stamp": "stamp-1",
            "durable_outputs": ["return.md"],
            "durable_frontier_verified": True,
        },
        replacement_session_id="s2",
        now=t("2026-08-25T12:11:00+08:00"),
    )
    assert out["owner_claim"]["claim_id"] == "claim-1"
    assert out["owner_claim"]["researcher_id"] == "EM-T1-ABC123"
    assert out["session"]["session_id"] == "s2"
    assert out["adoption"]["claim_reissued"] is False
    assert out["adoption"]["researcher_id_preserved"] is True
    assert out["adoption"]["completed_units_replayed"] is False
    assert out["adoption"]["resume_unit"] == "prove unit B"
    assert out["adoption"]["required_action"] == "RESUME_CURRENT_UNFINISHED_UNIT"


def test_stale_adoption_rejects_mismatched_claim():
    with pytest.raises(rt.RuntimeStateError, match="claim_id"):
        rt.adopt_stale_session(
            state(),
            {
                "taskbook_source": "abc123",
                "owner_branch": "research/t1",
                "claim_id": "wrong",
                "remote_head": "deadbeef",
                "execution_stamp": "stamp-1",
                "durable_outputs": ["return.md"],
                "durable_frontier_verified": True,
            },
            replacement_session_id="s2",
            now=t("2026-08-25T12:11:00+08:00"),
        )


def test_expired_owner_lease_is_not_adoptable():
    current = state(
        owner_claim={
            "claim_id": "claim-1",
            "researcher_id": "EM-T1-ABC123",
            "owner_lease_until": "2026-08-25T12:05:00+08:00",
        }
    )
    view = rt.classify_session(
        current["owner_claim"],
        current["session"],
        now=t("2026-08-25T12:11:00+08:00"),
    )
    assert view["session_state"] == "STALE_UNOWNED"
    assert view["adoption_allowed"] is False


def test_machine_policies_route_final_permission_to_unified_runtime():
    active = json.loads((ROOT / "active_turn_liveness.json").read_text(encoding="utf-8"))
    final = json.loads((ROOT / "final_response_identity_policy.json").read_text(encoding="utf-8"))
    assert active["runtime_orchestrator"] == "research_runtime_state_machine.json"
    assert active["runtime_evaluator"] == "tools/research_runtime.py"
    assert final["final_permission_authority"] == "research_runtime_state_machine.json"
    assert final["pre_final_permission_gate"]["identity_render_only_after_final_allowed"] is True
    assert final["pre_final_permission_gate"]["rule"] == "RUNTIME_FINAL_ALLOWED_FALSE -> FINAL_CHANNEL_FORBIDDEN"
