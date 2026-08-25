#!/usr/bin/env python3
"""Executable liveness guards for Enterprise Math research conversations.

This module turns the repository's active-turn continuation contract into a
small deterministic runtime surface.  It deliberately fails closed: a caller
may emit a terminal/final response only after the parent objective is known to
be complete, the user explicitly requested a stop/pause, or a genuine terminal
block has been classified.

A missing next action is therefore not evidence of completion.  When the parent
objective remains open, the caller must either execute the known next action or
resolve the next action/blocker before finalizing.
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


class RuntimeStateError(ValueError):
    """Raised when a runtime state declaration is internally invalid."""


def _clean_action(value: Any) -> str | None:
    if value is None:
        return None
    if not isinstance(value, str):
        raise RuntimeStateError("next_executable_action must be a string or null")
    value = value.strip()
    return value or None


def pre_final_gate(
    *,
    parent_objective_complete: bool,
    next_executable_action: str | None = None,
    user_requested_stop: bool = False,
    terminal_block_reason: str | None = None,
) -> dict[str, Any]:
    """Classify whether the current turn is allowed to emit a final response.

    The gate is intentionally stricter than a prose reminder.  An open parent
    objective never becomes final merely because a subflow ended or because the
    caller currently lacks a next-action string.
    """

    action = _clean_action(next_executable_action)

    if terminal_block_reason is not None:
        if not isinstance(terminal_block_reason, str):
            raise RuntimeStateError("terminal_block_reason must be a string or null")
        terminal_block_reason = terminal_block_reason.strip().upper()
        if terminal_block_reason not in TERMINAL_BLOCK_REASONS:
            raise RuntimeStateError(
                "terminal_block_reason must be one of: "
                + ", ".join(sorted(TERMINAL_BLOCK_REASONS))
            )

    if parent_objective_complete:
        return {
            "final_allowed": True,
            "required_transition": "EMIT_PARENT_TERMINAL_FINAL",
            "reason": "PARENT_USER_OBJECTIVE_COMPLETE",
            "next_executable_action": None,
            "recovery_record_required": False,
        }

    if user_requested_stop:
        return {
            "final_allowed": True,
            "required_transition": "EMIT_USER_REQUESTED_STOP_FINAL",
            "reason": "USER_EXPLICIT_STOP_PAUSE_REVIEW_ONLY_OR_WAIT",
            "next_executable_action": action,
            "recovery_record_required": bool(action),
        }

    if terminal_block_reason is not None:
        return {
            "final_allowed": True,
            "required_transition": "EMIT_BLOCKED_FINAL_WITH_RECOVERY_RECORD",
            "reason": terminal_block_reason,
            "next_executable_action": action,
            "recovery_record_required": True,
        }

    if action is not None:
        return {
            "final_allowed": False,
            "required_transition": "EXECUTE_NEXT_ACTION_IN_SAME_TURN",
            "reason": "PARENT_OPEN_AND_EXECUTABLE_NEXT_ACTION_EXISTS",
            "next_executable_action": action,
            "recovery_record_required": False,
        }

    return {
        "final_allowed": False,
        "required_transition": "RESOLVE_NEXT_ACTION_OR_TERMINAL_BLOCK",
        "reason": "PARENT_OPEN_WITHOUT_PROVED_TERMINAL_CONDITION",
        "next_executable_action": None,
        "recovery_record_required": False,
    }
