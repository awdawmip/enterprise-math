#!/usr/bin/env python3
"""Repository-derived PRE_FINAL authority for Enterprise Math.

This module composes three existing layers without letting any caller-supplied
parent-objective status become authority:

1. ``tools.research_runtime_guard`` authenticates task registration;
2. ``research_parent_closure`` derives whether the canonical parent Objective is
   actually complete from repository state, including cohort/two-pass synthesis;
3. ``tools.research_runtime`` remains the pure active-turn liveness primitive.

The module governs final-interaction permission only.  It grants no mathematical
truth, Foundation authority, or canonical theorem promotion.
"""
from __future__ import annotations

import argparse
import copy
import json
from pathlib import Path
from typing import Any, Mapping

import research_parent_closure
from tools import research_runtime
from tools import research_runtime_guard
from tools import research_task_records

ROOT = Path(__file__).resolve().parent
PARENT_STATUS_AUTHORITY = "REPOSITORY_DERIVED_PARENT_CLOSURE"


class PreFinalAuthorityError(ValueError):
    pass


def _registered_parent_projection(
    safe: Mapping[str, Any], *, root: Path
) -> dict[str, Any]:
    task = safe.get("task")
    if not isinstance(task, Mapping):
        raise PreFinalAuthorityError("task must be an object")
    task_id = task.get("task_id")
    if not isinstance(task_id, str) or not task_id:
        raise PreFinalAuthorityError("task.task_id is required")

    registration = safe.get("task_registration")
    if not isinstance(registration, Mapping):
        raise PreFinalAuthorityError("task_registration must be an object")
    if registration.get("state") == "LEGACY_BASELINE_REGISTERED":
        return {
            "objective_id": None,
            "objective_generation_id": None,
            "derived_parent_complete": False,
            "state": "LEGACY_PARENT_OBJECTIVE_AUTHORITY_UNBOUND",
            "final_permission_granted": False,
            "next_control_action": "MIGRATE_PARENT_OBJECTIVE_AUTHORITY_OR_CONTINUE_WITH_PARENT_OPEN",
        }

    try:
        record = research_task_records.current_records(root).get(task_id)
    except Exception as exc:
        return {
            "objective_id": None,
            "objective_generation_id": None,
            "derived_parent_complete": False,
            "state": "TASK_PUBLICATION_AUTHORITY_INVALID",
            "authority_error": str(exc),
            "final_permission_granted": False,
            "next_control_action": "REPAIR_TASK_PUBLICATION_AUTHORITY",
        }
    if record is None:
        return {
            "objective_id": None,
            "objective_generation_id": None,
            "derived_parent_complete": False,
            "state": "CURRENT_TASK_PUBLICATION_MISSING",
            "final_permission_granted": False,
            "next_control_action": "REPAIR_TASK_PUBLICATION_AUTHORITY",
        }
    objective_id = record.get("parent_objective_id")
    if not isinstance(objective_id, str) or not objective_id:
        return {
            "objective_id": None,
            "objective_generation_id": None,
            "derived_parent_complete": False,
            "state": "CURRENT_TASK_PARENT_OBJECTIVE_MISSING",
            "final_permission_granted": False,
            "next_control_action": "REPAIR_TASK_OBJECTIVE_BINDING",
        }
    return research_parent_closure.derive_objective_closure(objective_id, root)


def canonical_pre_final_state(
    state: Mapping[str, Any], *, root: Path = ROOT
) -> tuple[dict[str, Any], dict[str, Any]]:
    """Authenticate registration, derive parent closure, and sanitize parent status."""
    safe = research_runtime_guard.canonicalize_registration(
        state, purpose="pre_final", root=root
    )
    if safe["task_registration"]["state"] == "IMMUTABLE_REGISTERED":
        # The pure V1 liveness primitive understands the compatibility execution
        # state vocabulary; immutable registration has already been authenticated.
        safe["task_registration"]["state"] = "CLAIMABLE"

    closure = _registered_parent_projection(safe, root=root)
    supplied_parent = state.get("parent_objective")
    supplied_status = (
        supplied_parent.get("status")
        if isinstance(supplied_parent, Mapping)
        else None
    )
    existing_parent = safe.get("parent_objective")
    parent = dict(existing_parent) if isinstance(existing_parent, Mapping) else {}
    canonical_objective_id = closure.get("objective_id")
    if isinstance(canonical_objective_id, str) and canonical_objective_id:
        parent["objective_id"] = canonical_objective_id
    parent["status"] = (
        "COMPLETE" if closure.get("derived_parent_complete") is True else "OPEN"
    )
    parent["status_authority"] = PARENT_STATUS_AUTHORITY
    parent["caller_supplied_status"] = supplied_status
    parent["caller_supplied_status_is_authority"] = False
    safe["parent_objective"] = parent
    return safe, closure


def pre_final_gate(
    state: Mapping[str, Any], *, root: Path = ROOT
) -> dict[str, Any]:
    safe, closure = canonical_pre_final_state(state, root=root)
    decision = research_runtime.pre_final_gate(safe)
    return {
        **decision,
        "registration_authenticated": True,
        "registration_authority": (
            "FROZEN_LEGACY_BASELINE"
            if safe["task_registration"]["state"] == "LEGACY_BASELINE_REGISTERED"
            else "IMMUTABLE_TASK_RECORD"
        ),
        "parent_status_authority": PARENT_STATUS_AUTHORITY,
        "caller_supplied_parent_status_is_authority": False,
        "parent_closure": closure,
    }


def apply_terminal_event(
    state: Mapping[str, Any], event: str, *, root: Path = ROOT
) -> dict[str, Any]:
    """Apply terminal events, refusing caller-forged parent completion."""
    if event != "PARENT_OBJECTIVE_COMPLETE":
        value = research_runtime_guard.apply_terminal_event(state, event, root=root)
        value["parent_status_authority"] = PARENT_STATUS_AUTHORITY
        return value

    safe, closure = canonical_pre_final_state(state, root=root)
    if closure.get("derived_parent_complete") is not True:
        decision = research_runtime.pre_final_gate(safe)
        value = copy.deepcopy(safe)
        value["runtime_phase"] = "REEVALUATE_PARENT"
        value["final_allowed"] = bool(decision["final_allowed"])
        value["pre_final_decision"] = {
            **decision,
            "parent_closure": closure,
            "caller_supplied_parent_status_is_authority": False,
        }
        value["registration_authenticated"] = True
        value["parent_terminal_event_authorized"] = False
        value["parent_terminal_event_rejected_reason"] = closure.get("state")
        value["parent_status_authority"] = PARENT_STATUS_AUTHORITY
        value["parent_closure"] = closure
        return value

    value = research_runtime.apply_terminal_event(
        safe, "PARENT_OBJECTIVE_COMPLETE"
    )
    value["registration_authenticated"] = True
    value["parent_terminal_event_authorized"] = True
    value["parent_status_authority"] = PARENT_STATUS_AUTHORITY
    value["parent_closure"] = closure
    if isinstance(value.get("pre_final_decision"), dict):
        value["pre_final_decision"]["parent_closure"] = closure
        value["pre_final_decision"]["caller_supplied_parent_status_is_authority"] = False
    return value


def _load_state(args: argparse.Namespace) -> dict[str, Any]:
    if args.state_json is not None:
        value = json.loads(args.state_json)
    else:
        value = json.loads(Path(args.state_file).read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise PreFinalAuthorityError("state must decode to an object")
    return value


def _add_state(parser: argparse.ArgumentParser) -> None:
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--state-json")
    source.add_argument("--state-file")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Enterprise Math repository-derived PRE_FINAL authority"
    )
    sub = parser.add_subparsers(dest="command", required=True)
    pre = sub.add_parser("pre-final")
    _add_state(pre)
    terminal = sub.add_parser("terminal")
    _add_state(terminal)
    terminal.add_argument(
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
    args = parser.parse_args()
    state = _load_state(args)
    result = (
        pre_final_gate(state)
        if args.command == "pre-final"
        else apply_terminal_event(state, args.event)
    )
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (PreFinalAuthorityError, research_runtime_guard.RuntimeAuthorizationError) as exc:
        print("ERROR:", exc)
        raise SystemExit(1)
