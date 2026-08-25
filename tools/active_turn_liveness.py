#!/usr/bin/env python3
"""Canonical PRE_FINAL liveness evaluator for Enterprise Math.

This helper turns the repository liveness contract into an executable decision.
It intentionally governs control flow only; it does not make mathematical truth,
safety, authorization, or product-runtime decisions on behalf of their owners.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Mapping

FINAL_ALLOWED = "FINAL_ALLOWED"
FINAL_ALLOWED_WITH_BLOCKER = "FINAL_ALLOWED_WITH_BLOCKER"
FINAL_ALLOWED_WITH_LIMIT = "FINAL_ALLOWED_WITH_LIMIT"
EXECUTE_NEXT_ACTION = "EXECUTE_NEXT_ACTION"
SWITCH_STRATEGY = "SWITCH_STRATEGY"
RECOMPUTE_PARENT_STATE = "RECOMPUTE_PARENT_STATE"
CONTROL_STATE_INCONSISTENT = "CONTROL_STATE_INCONSISTENT"

TRANSITIONS = (
    FINAL_ALLOWED,
    FINAL_ALLOWED_WITH_BLOCKER,
    FINAL_ALLOWED_WITH_LIMIT,
    EXECUTE_NEXT_ACTION,
    SWITCH_STRATEGY,
    RECOMPUTE_PARENT_STATE,
    CONTROL_STATE_INCONSISTENT,
)

_BOOL_FIELDS = (
    "parent_objective_complete",
    "user_requested_stop_pause_review_or_wait",
    "parent_hard_blocker",
    "platform_or_tool_hard_limit",
    "independent_safe_work_exhausted",
    "same_action_repeated_without_state_change",
    "supported_alternative_available",
    "parent_state_recomputed_without_change",
)


def _require_bool(state: Mapping[str, Any], key: str) -> bool:
    if key not in state:
        raise ValueError(f"missing required boolean field: {key}")
    value = state[key]
    if type(value) is not bool:
        raise ValueError(f"{key} must be a boolean")
    return value


def _require_nonnegative_int(state: Mapping[str, Any], key: str) -> int:
    if key not in state:
        raise ValueError(f"missing required integer field: {key}")
    value = state[key]
    if type(value) is not int or value < 0:
        raise ValueError(f"{key} must be a nonnegative integer")
    return value


def _optional_bool(state: Mapping[str, Any], key: str, default: bool = False) -> bool:
    value = state.get(key, default)
    if type(value) is not bool:
        raise ValueError(f"{key} must be a boolean when present")
    return value


def _decision(
    transition: str,
    reason: str,
    *,
    continuation_lease_active: bool,
    lease_terminates: bool = False,
) -> dict[str, Any]:
    final_allowed = transition in {
        FINAL_ALLOWED,
        FINAL_ALLOWED_WITH_BLOCKER,
        FINAL_ALLOWED_WITH_LIMIT,
    }
    return {
        "transition": transition,
        "final_allowed": final_allowed,
        "reason": reason,
        "continuation_lease_preserved": continuation_lease_active and not lease_terminates,
    }


def evaluate(state: Mapping[str, Any]) -> dict[str, Any]:
    """Evaluate the canonical PRE_FINAL transition.

    The continuation lease is deliberately *not* a prerequisite for continuing.
    If the parent objective is incomplete and executable work exists, final is
    forbidden whether or not the user previously said "continue".
    """

    values = {key: _require_bool(state, key) for key in _BOOL_FIELDS}
    executable_next_actions = _require_nonnegative_int(state, "executable_next_actions")
    continuation_lease_active = _optional_bool(state, "continuation_lease_active", False)

    if values["parent_objective_complete"]:
        return _decision(
            FINAL_ALLOWED,
            "parent user objective is complete",
            continuation_lease_active=continuation_lease_active,
            lease_terminates=True,
        )

    if values["user_requested_stop_pause_review_or_wait"]:
        return _decision(
            FINAL_ALLOWED,
            "user explicitly requested a terminal interaction boundary",
            continuation_lease_active=continuation_lease_active,
            lease_terminates=True,
        )

    if executable_next_actions > 0:
        if values["same_action_repeated_without_state_change"]:
            if values["supported_alternative_available"]:
                return _decision(
                    SWITCH_STRATEGY,
                    "same action made no state progress; a supported alternative exists",
                    continuation_lease_active=continuation_lease_active,
                )
            if values["parent_state_recomputed_without_change"]:
                return _decision(
                    CONTROL_STATE_INCONSISTENT,
                    "same no-progress action has no alternative and parent-state recomputation changed nothing",
                    continuation_lease_active=continuation_lease_active,
                )
            return _decision(
                RECOMPUTE_PARENT_STATE,
                "same action made no state progress and no alternative is currently selected",
                continuation_lease_active=continuation_lease_active,
            )

        return _decision(
            EXECUTE_NEXT_ACTION,
            "parent objective is incomplete and at least one executable next action exists",
            continuation_lease_active=continuation_lease_active,
        )

    if not values["independent_safe_work_exhausted"]:
        if values["parent_state_recomputed_without_change"]:
            return _decision(
                CONTROL_STATE_INCONSISTENT,
                "safe work is claimed to remain, but parent-state recomputation produced no executable action",
                continuation_lease_active=continuation_lease_active,
            )
        return _decision(
            RECOMPUTE_PARENT_STATE,
            "no next action is selected but independent/downstream-safe work has not been exhausted",
            continuation_lease_active=continuation_lease_active,
        )

    if values["platform_or_tool_hard_limit"]:
        return _decision(
            FINAL_ALLOWED_WITH_LIMIT,
            "a platform/tool hard limit blocks all remaining executable work this turn",
            continuation_lease_active=continuation_lease_active,
        )

    if values["parent_hard_blocker"]:
        return _decision(
            FINAL_ALLOWED_WITH_BLOCKER,
            "a genuine parent-level blocker remains after safe independent work is exhausted",
            continuation_lease_active=continuation_lease_active,
        )

    if values["parent_state_recomputed_without_change"]:
        return _decision(
            CONTROL_STATE_INCONSISTENT,
            "parent is incomplete, no executable work or terminal blocker exists, and recomputation changed nothing",
            continuation_lease_active=continuation_lease_active,
        )

    return _decision(
        RECOMPUTE_PARENT_STATE,
        "parent is incomplete with no selected executable action and no terminal blocker; recompute routing once",
        continuation_lease_active=continuation_lease_active,
    )


def _load_state(args: argparse.Namespace) -> Mapping[str, Any]:
    if args.state_json is not None:
        state = json.loads(args.state_json)
    else:
        state = json.loads(Path(args.state_file).read_text(encoding="utf-8"))
    if not isinstance(state, dict):
        raise ValueError("state input must decode to a JSON object")
    return state


def main() -> int:
    parser = argparse.ArgumentParser(description="Evaluate Enterprise Math PRE_FINAL liveness state")
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--state-json", help="inline JSON object")
    source.add_argument("--state-file", help="path to a JSON object")
    args = parser.parse_args()
    decision = evaluate(_load_state(args))
    print(json.dumps(decision, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
