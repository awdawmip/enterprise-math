import json
from pathlib import Path

import pytest

from tools import research_runtime as rt

ROOT = Path(__file__).resolve().parents[1]


def t(value):
    return rt.parse_time(value)


def runtime_state():
    return {
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


def evidence(**overrides):
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


def test_stale_adoption_requires_exact_durable_frontier_evidence():
    for bad, marker in (
        (evidence(remote_head="other"), "remote_head"),
        (evidence(execution_stamp="other"), "execution_stamp"),
        (evidence(durable_outputs=["other.md"]), "durable_outputs"),
    ):
        with pytest.raises(rt.RuntimeStateError, match=marker):
            rt.adopt_stale_session(
                runtime_state(),
                bad,
                replacement_session_id="s2",
                now=t("2026-08-25T12:11:00+08:00"),
            )


def test_stale_adoption_preserves_owner_and_skips_replay():
    out = rt.adopt_stale_session(
        runtime_state(),
        evidence(),
        replacement_session_id="s2",
        now=t("2026-08-25T12:11:00+08:00"),
    )
    assert out["owner_claim"]["claim_id"] == "claim-1"
    assert out["owner_claim"]["researcher_id"] == "EM-T1-ABC123"
    assert out["adoption"]["claim_reissued"] is False
    assert out["adoption"]["completed_units_replayed"] is False
    assert out["adoption"]["resume_unit"] == "prove unit B"


def test_runtime_policy_is_visible_from_universal_and_taskbook_routes():
    agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
    taskbook = json.loads((ROOT / "research_taskbook_contract.json").read_text(encoding="utf-8"))
    policy = json.loads((ROOT / "research_taskbook_policy.json").read_text(encoding="utf-8"))
    for marker in (
        "research_runtime_state_machine.json",
        "OWNER_LEASE != SESSION_LIVENESS",
        "SESSION_STALE + OWNER_LEASE_ACTIVE -> STALE_RECOVERABLE",
        "TASK_FROZEN -> REEVALUATE_PARENT",
        "RUNTIME_FINAL_ALLOWED_FALSE -> FINAL_CHANNEL_FORBIDDEN",
    ):
        assert marker in agents
    assert taskbook["runtime_state_machine"] == "research_runtime_state_machine.json"
    assert taskbook["runtime_terminal_contract"]["default_taskbook_stop_scope"] == "TASK"
    assert taskbook["runtime_lease_contract"]["taskbook_claim_lease_scope"] == "OWNER_CLAIM"
    assert "research_runtime_state_machine.json" in policy["policy_inputs"]
    assert "docs/RESEARCH_RUNTIME_STATE_MACHINE.md" in policy["policy_inputs"]


def test_legacy_long_owner_lease_cannot_mask_dead_session():
    scheduler = {
        "state": "IN_PROGRESS",
        "dispatch_state": "LEASED",
        "claim_id": "c",
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
