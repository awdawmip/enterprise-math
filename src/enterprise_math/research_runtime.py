"""Executable liveness guards for Enterprise Math research conversations.

This module turns the repository's active-turn continuation contract into a
small deterministic runtime surface. It deliberately fails closed: a caller
may emit a terminal/final response only after the parent objective is known to
be complete, the user explicitly requested a stop/pause, or a genuine terminal
block has been classified.

Local terminal events are scoped. SUBFLOW and TASK completion return to the
parent objective for re-evaluation; they are not aliases for parent completion.
The runtime snapshot then binds parent objective, task, owner claim, session,
durable frontier, unfinished unit, next action, terminal scope, and final gate
into one inspectable object.
"""

from __future__ import annotations

from typing import Any


RUNTIME_SCHEMA = "ENTERPRISE_MATH_RESEARCH_RUNTIME_STATE_V1"

TERMINAL_BLOCK_REASONS = {
    "SAFETY",
    "AUTHORIZATION",
    "MISSING_USER_DATA",
    "UNAVOIDABLE_EXTERNAL_EVENT",
    "PLATFORM_OR_TOOL_LIMIT",
}

TERMINAL_SCOPES = {
    "NONE",
    "SUBFLOW",
    "TASK",
    "PARENT_OBJECTIVE",
}


class RuntimeStateError(ValueError):
    """Raised when a runtime state declaration is internally invalid."""


def _clean_action(value: Any) -> str | None:
    if value is None:
        return None
    if not isinstance(value, str):
        raise RuntimeStateError("next_executable_action must be a string or null")
    value = value.strip()
    return value or None


def _clean_optional_text(value: Any, field: str) -> str | None:
    if value is None:
        return None
    if not isinstance(value, str):
        raise RuntimeStateError(f"{field} must be a string or null")
    value = value.strip()
    return value or None


def _required_text(value: Any, field: str) -> str:
    cleaned = _clean_optional_text(value, field)
    if cleaned is None:
        raise RuntimeStateError(f"{field} must be a non-empty string")
    return cleaned


def _clean_terminal_scope(value: str) -> str:
    if not isinstance(value, str):
        raise RuntimeStateError("terminal_scope must be a string")
    scope = value.strip().upper()
    if scope not in TERMINAL_SCOPES:
        raise RuntimeStateError(
            "terminal_scope must be one of: " + ", ".join(sorted(TERMINAL_SCOPES))
        )
    return scope


def pre_final_gate(
    *,
    parent_objective_complete: bool,
    next_executable_action: str | None = None,
    terminal_scope: str = "NONE",
    user_requested_stop: bool = False,
    terminal_block_reason: str | None = None,
) -> dict[str, Any]:
    """Classify whether the current turn is allowed to emit a final response.

    The gate is intentionally stricter than a prose reminder. An open parent
    objective never becomes final merely because a subflow/task ended or
    because the caller currently lacks a next-action string.
    """

    action = _clean_action(next_executable_action)
    scope = _clean_terminal_scope(terminal_scope)

    if terminal_block_reason is not None:
        if not isinstance(terminal_block_reason, str):
            raise RuntimeStateError("terminal_block_reason must be a string or null")
        terminal_block_reason = terminal_block_reason.strip().upper()
        if terminal_block_reason not in TERMINAL_BLOCK_REASONS:
            raise RuntimeStateError(
                "terminal_block_reason must be one of: "
                + ", ".join(sorted(TERMINAL_BLOCK_REASONS))
            )

    if scope == "PARENT_OBJECTIVE" and not parent_objective_complete:
        raise RuntimeStateError(
            "terminal_scope=PARENT_OBJECTIVE requires parent_objective_complete=true"
        )

    if parent_objective_complete:
        return {
            "final_allowed": True,
            "required_transition": "EMIT_PARENT_TERMINAL_FINAL",
            "reason": "PARENT_USER_OBJECTIVE_COMPLETE",
            "terminal_scope": "PARENT_OBJECTIVE",
            "next_executable_action": None,
            "recovery_record_required": False,
        }

    if user_requested_stop:
        return {
            "final_allowed": True,
            "required_transition": "EMIT_USER_REQUESTED_STOP_FINAL",
            "reason": "USER_EXPLICIT_STOP_PAUSE_REVIEW_ONLY_OR_WAIT",
            "terminal_scope": scope,
            "next_executable_action": action,
            "recovery_record_required": bool(action) or scope in {"SUBFLOW", "TASK"},
        }

    if terminal_block_reason is not None:
        return {
            "final_allowed": True,
            "required_transition": "EMIT_BLOCKED_FINAL_WITH_RECOVERY_RECORD",
            "reason": terminal_block_reason,
            "terminal_scope": scope,
            "next_executable_action": action,
            "recovery_record_required": True,
        }

    if scope in {"SUBFLOW", "TASK"}:
        return {
            "final_allowed": False,
            "required_transition": "REEVALUATE_PARENT_OBJECTIVE",
            "reason": f"{scope}_TERMINAL_IS_LOCAL_NOT_PARENT_TERMINAL",
            "terminal_scope": scope,
            "next_executable_action": action,
            "recovery_record_required": False,
        }

    if action is not None:
        return {
            "final_allowed": False,
            "required_transition": "EXECUTE_NEXT_ACTION_IN_SAME_TURN",
            "reason": "PARENT_OPEN_AND_EXECUTABLE_NEXT_ACTION_EXISTS",
            "terminal_scope": scope,
            "next_executable_action": action,
            "recovery_record_required": False,
        }

    return {
        "final_allowed": False,
        "required_transition": "RESOLVE_NEXT_ACTION_OR_TERMINAL_BLOCK",
        "reason": "PARENT_OPEN_WITHOUT_PROVED_TERMINAL_CONDITION",
        "terminal_scope": scope,
        "next_executable_action": None,
        "recovery_record_required": False,
    }


def build_runtime_snapshot(
    *,
    parent_objective: str,
    parent_objective_complete: bool,
    current_subflow: str | None = None,
    task_id: str | None = None,
    scheduler_state: dict[str, Any] | None = None,
    durable_frontier: str | None = None,
    current_unfinished_unit: str | None = None,
    next_executable_action: str | None = None,
    terminal_scope: str = "NONE",
    user_requested_stop: bool = False,
    terminal_block_reason: str | None = None,
) -> dict[str, Any]:
    """Build the canonical cross-control-plane runtime snapshot.

    Scheduler state is optional so the same runtime can cover direct/free work.
    When it is present, task/claim/session/frontier fields are derived from that
    durable reducer state unless an explicit current-turn field is supplied.
    """

    parent = _required_text(parent_objective, "parent_objective")
    if scheduler_state is not None and not isinstance(scheduler_state, dict):
        raise RuntimeStateError("scheduler_state must be an object or null")

    scheduler_state = scheduler_state or {}
    resolved_task_id = _clean_optional_text(
        task_id if task_id is not None else scheduler_state.get("task_id"),
        "task_id",
    )
    subflow = _clean_optional_text(current_subflow, "current_subflow")

    frontier = _clean_optional_text(
        durable_frontier if durable_frontier is not None else scheduler_state.get("last_progress_ref"),
        "durable_frontier",
    )
    recovery_ref = _clean_optional_text(scheduler_state.get("last_recovery_ref"), "last_recovery_ref")
    unfinished = _clean_optional_text(
        current_unfinished_unit
        if current_unfinished_unit is not None
        else scheduler_state.get("current_unfinished_unit"),
        "current_unfinished_unit",
    )
    action = _clean_action(
        next_executable_action
        if next_executable_action is not None
        else scheduler_state.get("next_action")
    )

    claim_id = _clean_optional_text(scheduler_state.get("claim_id"), "claim_id")
    owner_claim = None
    if claim_id is not None:
        owner_claim = {
            "claim_id": claim_id,
            "actor": _clean_optional_text(scheduler_state.get("actor"), "actor"),
            "researcher_id": _clean_optional_text(
                scheduler_state.get("researcher_id"), "researcher_id"
            ),
            "owner_lease_until": _clean_optional_text(
                scheduler_state.get("owner_lease_until") or scheduler_state.get("lease_until"),
                "owner_lease_until",
            ),
        }

    session_state = _clean_optional_text(scheduler_state.get("session_state"), "session_state")
    session = {
        "state": session_state or ("NONE" if claim_id is None else "UNKNOWN"),
        "session_lease_until": _clean_optional_text(
            scheduler_state.get("session_lease_until"), "session_lease_until"
        ),
        "last_session_activity_at": _clean_optional_text(
            scheduler_state.get("last_session_activity_at"), "last_session_activity_at"
        ),
        "last_session_adopt_at": _clean_optional_text(
            scheduler_state.get("last_session_adopt_at"), "last_session_adopt_at"
        ),
    }

    gate = pre_final_gate(
        parent_objective_complete=parent_objective_complete,
        next_executable_action=action,
        terminal_scope=terminal_scope,
        user_requested_stop=user_requested_stop,
        terminal_block_reason=terminal_block_reason,
    )

    return {
        "schema": RUNTIME_SCHEMA,
        "parent_objective": {
            "id": parent,
            "complete": bool(parent_objective_complete),
        },
        "current_subflow": subflow,
        "task": {
            "task_id": resolved_task_id,
            "scheduler_state": _clean_optional_text(scheduler_state.get("state"), "scheduler_state"),
            "dispatch_state": _clean_optional_text(
                scheduler_state.get("dispatch_state"), "dispatch_state"
            ),
        },
        "owner_claim": owner_claim,
        "session": session,
        "durable_frontier": {
            "progress_ref": frontier,
            "recovery_ref": recovery_ref,
        },
        "current_unfinished_unit": unfinished,
        "next_executable_action": action,
        "terminal_scope": gate["terminal_scope"],
        "final_gate": gate,
    }
