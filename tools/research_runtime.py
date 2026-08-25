#!/usr/bin/env python3
"""Executable liveness guards for Enterprise Math research conversations.

This module turns the repository's active-turn continuation contract into a
small deterministic runtime surface. It deliberately fails closed: a caller
may emit a terminal/final response only after the parent objective is known to
be complete, the user explicitly requested a stop/pause, or a genuine terminal
block has been classified.

Local terminal events are scoped. SUBFLOW and TASK completion return to the
parent objective for re-evaluation; they are not aliases for parent completion.
"""

from __future__ import annotations

from typing import Any


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
