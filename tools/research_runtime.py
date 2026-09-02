#!/usr/bin/env python3
"""Unified Enterprise Math research runtime control state machine.

The runtime composes task registration, active-turn PRE_FINAL liveness, durable
owner claims, independent conversation liveness, stale adoption and terminal
scope. It governs control flow only; it does not promote mathematical truth.
"""
from __future__ import annotations

import argparse
import copy
import json
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Mapping

try:
    from tools import active_turn_liveness
except ModuleNotFoundError:  # direct script execution from tools/
    import active_turn_liveness  # type: ignore

TERMINAL_SCOPES = ("SUBFLOW", "TASK", "PARENT_OBJECTIVE")
TASK_REGISTRATION_STATES = {
    "REGISTERED",
    "CLAIMABLE",
    "CLAIMED",
    "IN_PROGRESS",
    "HANDOFF_READY",
    "BLOCKED",
    "FROZEN",
    "DONE",
    "PARKED",
    "SUPERSEDED",
}
SESSION_ACTIVE = "ACTIVE"
SESSION_STALE_RECOVERABLE = "STALE_RECOVERABLE"
SESSION_STALE_UNOWNED = "STALE_UNOWNED"
SESSION_TERMINATED = "TERMINATED"
REEVALUATE_PARENT = "REEVALUATE_PARENT"
ADOPT_OWNER_CLAIM = "ADOPT_OWNER_CLAIM"
CLAIM_NEW_OWNER = "CLAIM_NEW_OWNER"
KEEP_CURRENT_SESSION = "KEEP_CURRENT_SESSION"
NO_DISPATCH = "NO_DISPATCH"
DEFAULT_SESSION_LIVENESS_MINUTES = 10

REQUIRED_CANONICAL_FIELDS = (
    "parent_objective",
    "task_registration",
    "task",
    "owner_claim",
    "session",
    "durable_frontier",
    "current_unfinished_unit",
    "next_action",
    "terminal_scope",
    "final_allowed",
)
ADOPTION_EVIDENCE_FIELDS = (
    "taskbook_source",
    "owner_branch",
    "claim_id",
    "remote_head",
    "execution_stamp",
    "durable_outputs",
    "durable_frontier_verified",
)


class RuntimeStateError(ValueError):
    pass


def parse_time(value: str) -> datetime:
    if not isinstance(value, str) or not value.strip():
        raise RuntimeStateError("timestamp must be a non-empty ISO-8601 string")
    normalized = value.strip().replace("Z", "+00:00")
    try:
        dt = datetime.fromisoformat(normalized)
    except ValueError as exc:
        raise RuntimeStateError(f"invalid ISO-8601 timestamp: {value!r}") from exc
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc)


def iso(dt: datetime) -> str:
    return dt.astimezone(timezone.utc).isoformat()


def require_task_registration(state: Mapping[str, Any]) -> None:
    registration = state.get("task_registration")
    task = state.get("task")
    if not isinstance(registration, Mapping):
        raise RuntimeStateError("task_registration must be an object; unregistered tasks cannot execute")
    if not isinstance(task, Mapping):
        raise RuntimeStateError("task must be an object")
    registration_state = str(registration.get("state", "")).upper()
    if registration_state not in TASK_REGISTRATION_STATES:
        raise RuntimeStateError(
            "task registration is not executable: "
            f"{registration_state or 'MISSING'}; register the task by publishing its immutable V2 record before READY/CLAIM/execution"
        )
    task_id = task.get("task_id")
    registry_key = registration.get("registry_key")
    if not isinstance(registry_key, str) or not registry_key.strip():
        raise RuntimeStateError("registered task requires nonempty task_registration.registry_key")
    if registry_key != task_id:
        raise RuntimeStateError("task_registration.registry_key must equal task.task_id")


def require_canonical_state(state: Mapping[str, Any]) -> None:
    missing = [field for field in REQUIRED_CANONICAL_FIELDS if field not in state]
    if missing:
        raise RuntimeStateError("missing canonical runtime fields: " + ", ".join(missing))
    if not isinstance(state["parent_objective"], Mapping):
        raise RuntimeStateError("parent_objective must be an object")
    if not isinstance(state["task"], Mapping):
        raise RuntimeStateError("task must be an object")
    if not isinstance(state["owner_claim"], Mapping):
        raise RuntimeStateError("owner_claim must be an object")
    if not isinstance(state["session"], Mapping):
        raise RuntimeStateError("session must be an object")
    if not isinstance(state["durable_frontier"], Mapping):
        raise RuntimeStateError("durable_frontier must be an object")
    if state["terminal_scope"] not in (None, *TERMINAL_SCOPES):
        raise RuntimeStateError("terminal_scope must be null, SUBFLOW, TASK, or PARENT_OBJECTIVE")
    if type(state["final_allowed"]) is not bool:
        raise RuntimeStateError("final_allowed must be boolean")
    require_task_registration(state)


def _owner_lease_until(owner_claim: Mapping[str, Any]) -> datetime | None:
    raw = owner_claim.get("owner_lease_until", owner_claim.get("lease_until"))
    if raw in (None, ""):
        return None
    return parse_time(raw)


def owner_lease_active(owner_claim: Mapping[str, Any], now: datetime) -> bool:
    claim_id = owner_claim.get("claim_id")
    lease_until = _owner_lease_until(owner_claim)
    return bool(isinstance(claim_id, str) and claim_id and lease_until and now < lease_until)


def classify_session(
    owner_claim: Mapping[str, Any],
    session: Mapping[str, Any],
    *,
    now: datetime,
    session_liveness_minutes: int = DEFAULT_SESSION_LIVENESS_MINUTES,
) -> dict[str, Any]:
    """Classify chat/session liveness independently from the owner lease."""
    if type(session_liveness_minutes) is not int or session_liveness_minutes <= 0:
        raise RuntimeStateError("session_liveness_minutes must be a positive integer")
    if session.get("terminated") is True:
        return {
            "session_state": SESSION_TERMINATED,
            "owner_lease_active": owner_lease_active(owner_claim, now),
            "adoption_allowed": False,
        }
    last_activity = session.get("last_activity_at")
    if not isinstance(last_activity, str) or not last_activity.strip():
        raise RuntimeStateError("session.last_activity_at is required")
    stale_at = parse_time(last_activity) + timedelta(minutes=session_liveness_minutes)
    is_stale = now >= stale_at
    owner_active = owner_lease_active(owner_claim, now)
    if not is_stale:
        session_state = SESSION_ACTIVE
    elif owner_active:
        session_state = SESSION_STALE_RECOVERABLE
    else:
        session_state = SESSION_STALE_UNOWNED
    return {
        "session_state": session_state,
        "owner_lease_active": owner_active,
        "adoption_allowed": session_state == SESSION_STALE_RECOVERABLE,
        "stale_at": iso(stale_at),
    }


def owner_claim_from_scheduler(scheduler_state: Mapping[str, Any]) -> dict[str, Any]:
    """Map reduced runtime claim fields to the owner-lease layer only."""
    return {
        "claim_id": scheduler_state.get("claim_id"),
        "actor": scheduler_state.get("actor"),
        "researcher_id": scheduler_state.get("researcher_id"),
        "owner_lease_until": scheduler_state.get("owner_lease_until", scheduler_state.get("lease_until")),
        "scheduler_state": scheduler_state.get("state"),
        "dispatch_state": scheduler_state.get("dispatch_state"),
    }


def dispatch_decision(
    scheduler_state: Mapping[str, Any],
    *,
    session_last_activity_at: str | None,
    now: datetime,
    session_liveness_minutes: int = DEFAULT_SESSION_LIVENESS_MINUTES,
) -> dict[str, Any]:
    """Derive conversation dispatch from reduced runtime state."""
    owner_claim = owner_claim_from_scheduler(scheduler_state)
    dispatch_state = scheduler_state.get("dispatch_state")
    if dispatch_state == "LEASED" and owner_claim.get("claim_id"):
        if session_last_activity_at is None:
            return {
                "action": "VERIFY_SESSION_LIVENESS",
                "owner_claim_preserved": True,
                "new_claim_required": False,
            }
        session_view = classify_session(
            owner_claim,
            {"last_activity_at": session_last_activity_at},
            now=now,
            session_liveness_minutes=session_liveness_minutes,
        )
        if session_view["session_state"] == SESSION_STALE_RECOVERABLE:
            return {
                "action": ADOPT_OWNER_CLAIM,
                "owner_claim_preserved": True,
                "new_claim_required": False,
                **session_view,
            }
        if session_view["session_state"] == SESSION_ACTIVE:
            return {
                "action": KEEP_CURRENT_SESSION,
                "owner_claim_preserved": True,
                "new_claim_required": False,
                **session_view,
            }
        return {
            "action": CLAIM_NEW_OWNER,
            "owner_claim_preserved": False,
            "new_claim_required": True,
            **session_view,
        }
    if dispatch_state == "NEEDS_DISPATCH":
        return {
            "action": CLAIM_NEW_OWNER,
            "owner_claim_preserved": False,
            "new_claim_required": True,
            "registration_gate_required": True,
        }
    return {
        "action": NO_DISPATCH,
        "owner_claim_preserved": bool(owner_claim.get("claim_id")),
        "new_claim_required": False,
    }


def _bool(control: Mapping[str, Any], key: str, default: bool = False) -> bool:
    value = control.get(key, default)
    if type(value) is not bool:
        raise RuntimeStateError(f"control.{key} must be boolean")
    return value


def _next_action_count(next_action: Any) -> int:
    if next_action is None:
        return 0
    if isinstance(next_action, str):
        return 1 if next_action.strip() else 0
    if isinstance(next_action, Mapping):
        if next_action.get("executable") is False:
            return 0
        description = next_action.get("description", next_action.get("action"))
        if description is None:
            return 1
        return 1 if isinstance(description, str) and description.strip() else 0
    raise RuntimeStateError("next_action must be null, string, or object")


def _unfinished_unit_present(value: Any) -> bool:
    if value is None:
        return False
    if isinstance(value, str):
        return bool(value.strip())
    return True


def pre_final_gate(state: Mapping[str, Any]) -> dict[str, Any]:
    """Evaluate final permission from a registered canonical runtime object."""
    require_canonical_state(state)
    control = state.get("control", {})
    if not isinstance(control, Mapping):
        raise RuntimeStateError("control must be an object when present")
    parent_complete = str(state["parent_objective"].get("status", "OPEN")).upper() == "COMPLETE"
    next_action_count = _next_action_count(state.get("next_action"))
    if parent_complete and (
        next_action_count > 0 or _unfinished_unit_present(state.get("current_unfinished_unit"))
    ):
        transition = active_turn_liveness.CONTROL_STATE_INCONSISTENT
        continuation_lease_active = _bool(control, "continuation_lease_active")
        return {
            "transition": transition,
            "final_allowed": False,
            "reason": "parent objective is marked complete while runtime still records unfinished work",
            "required_action": active_turn_liveness.REQUIRED_ACTIONS[transition],
            "continuation_lease_preserved": continuation_lease_active,
            "terminal_scope": state.get("terminal_scope"),
            "canonical_final_allowed": False,
        }
    primitive = {
        "parent_objective_complete": parent_complete,
        "user_requested_stop_pause_review_or_wait": _bool(control, "user_requested_stop_pause_review_or_wait"),
        "parent_hard_blocker": _bool(control, "parent_hard_blocker"),
        "platform_or_tool_hard_limit": _bool(control, "platform_or_tool_hard_limit"),
        "independent_safe_work_exhausted": _bool(control, "independent_safe_work_exhausted"),
        "same_action_repeated_without_state_change": _bool(control, "same_action_repeated_without_state_change"),
        "supported_alternative_available": _bool(control, "supported_alternative_available"),
        "parent_state_recomputed_without_change": _bool(control, "parent_state_recomputed_without_change"),
        "executable_next_actions": next_action_count,
        "continuation_lease_active": _bool(control, "continuation_lease_active"),
    }
    decision = active_turn_liveness.evaluate(primitive)
    return {
        **decision,
        "terminal_scope": state.get("terminal_scope"),
        "canonical_final_allowed": bool(decision["final_allowed"]),
    }


def apply_terminal_event(state: Mapping[str, Any], event: str) -> dict[str, Any]:
    """Apply publication/subflow/task/parent terminal events at exact scope."""
    require_canonical_state(state)
    updated = copy.deepcopy(dict(state))
    if event == "TASK_PUBLISHED":
        updated["terminal_scope"] = "SUBFLOW"
        updated["runtime_phase"] = REEVALUATE_PARENT
        updated["final_allowed"] = False
        return updated
    if event == "SUBFLOW_COMPLETE":
        updated["terminal_scope"] = "SUBFLOW"
        updated["current_unfinished_unit"] = None
        updated["next_action"] = None
        updated["runtime_phase"] = REEVALUATE_PARENT
        updated["final_allowed"] = False
        return updated
    if event in {"TASK_FROZEN", "TASK_COMPLETE"}:
        updated["terminal_scope"] = "TASK"
        updated["task"]["status"] = "FROZEN" if event == "TASK_FROZEN" else "COMPLETE"
        updated["current_unfinished_unit"] = None
        updated["next_action"] = None
        updated["runtime_phase"] = REEVALUATE_PARENT
        updated["final_allowed"] = False
        return updated
    if event == "PARENT_OBJECTIVE_COMPLETE":
        updated["terminal_scope"] = "PARENT_OBJECTIVE"
        updated["parent_objective"]["status"] = "COMPLETE"
        updated["runtime_phase"] = "PRE_FINAL"
        decision = pre_final_gate(updated)
        updated["final_allowed"] = bool(decision["final_allowed"])
        updated["pre_final_decision"] = decision
        return updated
    raise RuntimeStateError(f"unknown terminal event: {event}")


def _match(evidence: Mapping[str, Any], expected: Any, field: str) -> None:
    if evidence.get(field) != expected:
        raise RuntimeStateError(f"adoption evidence mismatch for {field}")


def adopt_stale_session(
    state: Mapping[str, Any],
    evidence: Mapping[str, Any],
    *,
    replacement_session_id: str,
    now: datetime,
    session_liveness_minutes: int = DEFAULT_SESSION_LIVENESS_MINUTES,
) -> dict[str, Any]:
    """Adopt an existing owner claim after the previous chat goes stale."""
    require_canonical_state(state)
    missing = [field for field in ADOPTION_EVIDENCE_FIELDS if field not in evidence]
    if missing:
        raise RuntimeStateError("missing adoption evidence: " + ", ".join(missing))
    if not replacement_session_id.strip():
        raise RuntimeStateError("replacement_session_id is required")
    session_view = classify_session(
        state["owner_claim"],
        state["session"],
        now=now,
        session_liveness_minutes=session_liveness_minutes,
    )
    if session_view["session_state"] != SESSION_STALE_RECOVERABLE:
        raise RuntimeStateError("session is not STALE_RECOVERABLE")

    task = state["task"]
    claim = state["owner_claim"]
    frontier = state["durable_frontier"]
    _match(evidence, task.get("taskbook_source"), "taskbook_source")
    _match(evidence, task.get("owner_branch"), "owner_branch")
    _match(evidence, claim.get("claim_id"), "claim_id")
    if evidence.get("durable_frontier_verified") is not True:
        raise RuntimeStateError("durable_frontier_verified must be true")
    if not isinstance(evidence.get("remote_head"), str) or not evidence["remote_head"].strip():
        raise RuntimeStateError("remote_head must be non-empty")
    if not isinstance(evidence.get("execution_stamp"), str) or not evidence["execution_stamp"].strip():
        raise RuntimeStateError("execution_stamp must be non-empty")
    if not isinstance(evidence.get("durable_outputs"), list):
        raise RuntimeStateError("durable_outputs must be an array")
    expected_head = frontier.get("remote_head")
    if expected_head and evidence["remote_head"] != expected_head:
        raise RuntimeStateError("remote_head does not match refreshed durable frontier")
    expected_stamp = frontier.get("execution_stamp")
    if expected_stamp and evidence["execution_stamp"] != expected_stamp:
        raise RuntimeStateError("execution_stamp does not match refreshed durable frontier")
    expected_outputs = frontier.get("durable_outputs")
    if expected_outputs is not None and evidence["durable_outputs"] != expected_outputs:
        raise RuntimeStateError("durable_outputs do not match refreshed durable frontier")

    updated = copy.deepcopy(dict(state))
    updated["session"] = {
        **dict(updated["session"]),
        "session_id": replacement_session_id,
        "last_activity_at": iso(now),
        "state": SESSION_ACTIVE,
        "adopted_from_stale_session": True,
    }
    updated["durable_frontier"] = {
        **dict(updated["durable_frontier"]),
        "remote_head": evidence["remote_head"],
        "execution_stamp": evidence["execution_stamp"],
        "durable_outputs": copy.deepcopy(evidence["durable_outputs"]),
        "verified_at": iso(now),
    }
    updated["runtime_phase"] = "RESUME_FROM_DURABLE_FRONTIER"
    updated["final_allowed"] = False
    updated["adoption"] = {
        "claim_reissued": False,
        "owner_claim_preserved": True,
        "researcher_id_preserved": True,
        "completed_units_replayed": False,
        "resume_unit": updated.get("current_unfinished_unit"),
        "required_action": (
            "RESUME_CURRENT_UNFINISHED_UNIT"
            if updated.get("current_unfinished_unit")
            else REEVALUATE_PARENT
        ),
    }
    return updated


def _load_json_arg(value: str | None, path: str | None) -> dict[str, Any]:
    if value is not None:
        data = json.loads(value)
    elif path is not None:
        data = json.loads(Path(path).read_text(encoding="utf-8"))
    else:
        raise RuntimeStateError("JSON input is required")
    if not isinstance(data, dict):
        raise RuntimeStateError("input must decode to an object")
    return data


def _add_state_source(parser: argparse.ArgumentParser) -> None:
    src = parser.add_mutually_exclusive_group(required=True)
    src.add_argument("--state-json")
    src.add_argument("--state-file")


def main() -> int:
    parser = argparse.ArgumentParser(description="Enterprise Math unified research runtime")
    sub = parser.add_subparsers(dest="command", required=True)

    pf = sub.add_parser("pre-final")
    _add_state_source(pf)

    term = sub.add_parser("terminal")
    _add_state_source(term)
    term.add_argument(
        "--event",
        choices=[
            "TASK_PUBLISHED",
            "SUBFLOW_COMPLETE",
            "TASK_FROZEN",
            "TASK_COMPLETE",
            "PARENT_OBJECTIVE_COMPLETE",
        ],
        required=True,
    )

    session = sub.add_parser("session")
    session.add_argument("--owner-claim-json", required=True)
    session.add_argument("--last-activity-at", required=True)
    session.add_argument("--now", required=True)
    session.add_argument("--session-liveness-minutes", type=int, default=DEFAULT_SESSION_LIVENESS_MINUTES)

    dispatch = sub.add_parser("dispatch")
    dispatch.add_argument("--scheduler-state-json", required=True)
    dispatch.add_argument("--session-last-activity-at")
    dispatch.add_argument("--now", required=True)
    dispatch.add_argument("--session-liveness-minutes", type=int, default=DEFAULT_SESSION_LIVENESS_MINUTES)

    adopt = sub.add_parser("adopt")
    _add_state_source(adopt)
    adopt.add_argument("--evidence-json", required=True)
    adopt.add_argument("--replacement-session-id", required=True)
    adopt.add_argument("--now", required=True)
    adopt.add_argument("--session-liveness-minutes", type=int, default=DEFAULT_SESSION_LIVENESS_MINUTES)

    args = parser.parse_args()
    if args.command == "session":
        owner_claim = json.loads(args.owner_claim_json)
        if not isinstance(owner_claim, dict):
            raise RuntimeStateError("owner claim must decode to an object")
        result = classify_session(
            owner_claim,
            {"last_activity_at": args.last_activity_at},
            now=parse_time(args.now),
            session_liveness_minutes=args.session_liveness_minutes,
        )
    elif args.command == "dispatch":
        scheduler_state = json.loads(args.scheduler_state_json)
        if not isinstance(scheduler_state, dict):
            raise RuntimeStateError("scheduler state must decode to an object")
        result = dispatch_decision(
            scheduler_state,
            session_last_activity_at=args.session_last_activity_at,
            now=parse_time(args.now),
            session_liveness_minutes=args.session_liveness_minutes,
        )
    else:
        state = _load_json_arg(args.state_json, args.state_file)
        if args.command == "pre-final":
            result = pre_final_gate(state)
        elif args.command == "terminal":
            result = apply_terminal_event(state, args.event)
        elif args.command == "adopt":
            evidence = json.loads(args.evidence_json)
            if not isinstance(evidence, dict):
                raise RuntimeStateError("adoption evidence must decode to an object")
            result = adopt_stale_session(
                state,
                evidence,
                replacement_session_id=args.replacement_session_id,
                now=parse_time(args.now),
                session_liveness_minutes=args.session_liveness_minutes,
            )
        else:
            raise AssertionError(args.command)
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
