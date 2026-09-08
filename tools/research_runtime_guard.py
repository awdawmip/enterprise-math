#!/usr/bin/env python3
"""Canonical Enterprise Math repository-backed runtime guard.

The pre-firewall runtime implementation is preserved byte-for-byte in
``control_plane.research_runtime_guard_core``.  This public entrypoint keeps the
same API while composing the opt-in claim-scoped blind source firewall around
registered execution authorization and exposing the three local lifecycle
transactions PRE_MATH -> RAW_FREEZE -> SOURCE_EXPOSED.
"""
from __future__ import annotations

import argparse
import json
import sys as _sys
from pathlib import Path
from typing import Any, Mapping

_BOOT_ROOT = Path(__file__).resolve().parents[1]
if str(_BOOT_ROOT) not in _sys.path:
    _sys.path.insert(0, str(_BOOT_ROOT))

from control_plane.research_runtime_guard_core import *  # noqa: F401,F403
from control_plane import research_runtime_guard_core as _core
from control_plane import research_source_firewall as _firewall
from control_plane import research_startup_transport as _startup
from tools import research_activity as _activity

ROOT = _core.ROOT
RuntimeAuthorizationError = _core.RuntimeAuthorizationError


def _is_activity_state(state: Mapping[str, Any]) -> bool:
    # Activity metadata cannot opt a task/claim out of its original authority checks.
    if any(key in state for key in (
        "task", "task_id", "publication_id", "task_registration", "owner_claim",
        "execution_scope", "execution_binding", "execution_record_id"
    )):
        return False
    return state.get("research_mode", state.get("mode")) not in (
        "CONTROL_PLANE_MAINTENANCE", "RESEARCH_DRIVER", "FOUNDATION_STEWARD"
    )


def _activity_gate(state: Mapping[str, Any], boundary: str, root: Path) -> dict[str, Any]:
    try:
        result = _activity.guard(activity_id=state.get("activity_id"), boundary=boundary,
            event_id=state.get("research_checkpoint_event_id"), session_id=state.get("session_id"),
            registration_source=state.get("activity_registration_source"),
            new_semantic_progress=state.get("new_semantic_progress", True), root=root)
        result["authorized"] = False
        result["authorization_authority"] = "ACTIVITY_BOOKKEEPING_ONLY_NO_TASK_AUTHORITY"
        return result
    except (ValueError, OSError) as exc:
        raise RuntimeAuthorizationError(f"research activity guard: {exc}") from exc


def _is_control_only_pre_final_state(state: Mapping[str, Any]) -> bool:
    if state.get("research_mode", state.get("mode")) not in (
        "CONTROL_PLANE_MAINTENANCE", "RESEARCH_DRIVER", "FOUNDATION_STEWARD"
    ):
        return False
    # Even empty formal/activity bindings retain the original routing checks.
    return not any(key in state for key in (
        "task", "task_id", "publication_id", "task_registration", "owner_claim",
        "claim_id", "execution_scope", "execution_binding", "execution_record_id",
        "execution_cohort_id", "execution_lane_id",
        "activity_id", "activity_registration_source", "research_checkpoint_event_id"
    ))


def _control_only_pre_final_gate(state: Mapping[str, Any]) -> dict[str, Any]:
    result = {
        "authorized": False,
        "authorization_authority": "CONTROL_ONLY_PRE_FINAL_NO_TASK_AUTHORITY",
        "final_allowed": False,
        "required_action": "EVALUATE_PARENT_LIVENESS",
    }
    liveness = state.get("parent_liveness")
    if liveness is None:
        return result
    if not isinstance(liveness, Mapping):
        raise RuntimeAuthorizationError("control-only PRE_FINAL: parent_liveness must be an object")
    from tools import active_turn_liveness
    try:
        decision = active_turn_liveness.evaluate(liveness)
    except ValueError as exc:
        raise RuntimeAuthorizationError(f"control-only PRE_FINAL: {exc}") from exc
    if liveness["parent_objective_complete"] and liveness["executable_next_actions"] > 0:
        decision.update(
            transition=active_turn_liveness.CONTROL_STATE_INCONSISTENT,
            final_allowed=False,
            required_action=active_turn_liveness.REQUIRED_ACTIONS[active_turn_liveness.CONTROL_STATE_INCONSISTENT],
            reason="parent is marked complete while executable work remains",
            continuation_lease_preserved=liveness.get("continuation_lease_active", False),
        )
    result.update(
        parent_liveness=decision,
        final_allowed=decision["final_allowed"],
        required_action=decision["required_action"],
    )
    return result


def pre_final_gate(state: Mapping[str, Any], *, root: Path = ROOT) -> dict[str, Any]:
    if _is_control_only_pre_final_state(state):
        return _control_only_pre_final_gate(state)
    if not _is_activity_state(state):
        return _core.pre_final_gate(state, root=root)
    result = _activity_gate(state, "pre-final", root)
    result["final_allowed"] = False
    if result["activity_allowed"] and result["persistence_allowed"]:
        liveness = state.get("parent_liveness")
        if not isinstance(liveness, Mapping):
            result["required_action"] = "EVALUATE_PARENT_LIVENESS"
        else:
            from tools import active_turn_liveness
            result["parent_liveness"] = active_turn_liveness.evaluate(liveness)
            if liveness["parent_objective_complete"] and liveness["executable_next_actions"] > 0:
                result["parent_liveness"].update(
                    transition=active_turn_liveness.CONTROL_STATE_INCONSISTENT,
                    final_allowed=False,
                    required_action=active_turn_liveness.REQUIRED_ACTIONS[active_turn_liveness.CONTROL_STATE_INCONSISTENT],
                    reason="parent is marked complete while executable work remains")
            result["final_allowed"] = result["parent_liveness"]["final_allowed"]
            result["required_action"] = result["parent_liveness"]["required_action"]
    return result


def _raise_firewall(exc: Exception) -> None:
    raise RuntimeAuthorizationError(f"source-firewall authorization failed: {exc}") from exc


def authorize_execution(
    state: Mapping[str, Any],
    *,
    events: list[dict[str, Any]] | None = None,
    now=None,
    root: Path = ROOT,
) -> dict[str, Any]:
    """Authorize the existing winning CLAIM, then enforce opt-in PRE_MATH."""
    if _is_activity_state(state):
        return _activity_gate(state, "startup", root)
    result = _startup.attach(
        _core.authorize_execution(state, events=events, now=now, root=root)
    )
    binding = result.get("execution_binding")
    if not isinstance(binding, Mapping):
        return result

    # The core obtains record_path only from canonical repository state. Real
    # immutable records therefore exist at this path. Focused unit tests may
    # mock current_records() with in-memory publications and fake record paths;
    # the optional firewall must stay transparent to those synthetic fixtures.
    registration = result.get("task_registration")
    record_ref = registration.get("record_path") if isinstance(registration, Mapping) else None
    if isinstance(record_ref, str):
        record_path = Path(record_ref)
        if not record_path.is_absolute():
            record_path = root / record_path
        if not record_path.is_file():
            return result

        # Strict opt-in boundary: ordinary and historical taskbooks retain the
        # exact pre-firewall authorization path. Only a frontmatter declaration
        # enters the new parser/validator. This prevents an optional blind mode
        # from making legacy taskbook syntax a new execution dependency.
        try:
            record_payload = json.loads(record_path.read_text(encoding="utf-8"))
            taskbook_ref = record_payload.get("taskbook_path")
            taskbook_path = root / str(taskbook_ref or "")
            taskbook_text = taskbook_path.read_text(encoding="utf-8")
        except (OSError, ValueError, TypeError):
            return result
        frontmatter_text = taskbook_text.split("-->", 1)[0]
        if "source_firewall" not in frontmatter_text:
            return result

    try:
        gate = _firewall.execution_gate(
            task_id=str(result["task_id"]),
            binding=binding,
            state=state,
            root=root,
        )
    except _firewall.SourceFirewallError as exc:
        _raise_firewall(exc)
    if gate is not None:
        result["source_firewall"] = gate
        result["authorization_authority"] = (
            str(result["authorization_authority"]) + "+BLIND_PRE_MATH_VERIFIED"
        )
    return result


def _blind_binding(
    state: Mapping[str, Any],
    *,
    events: list[dict[str, Any]] | None,
    now,
    root: Path,
) -> tuple[str, dict[str, Any]]:
    """Resolve the exact winning ordinary/lane CLAIM without authorizing math yet."""
    safe = _core.canonicalize_registration(state, purpose="execution", root=root)
    if safe["task_registration"]["state"] != "IMMUTABLE_REGISTERED":
        raise RuntimeAuthorizationError("blind source firewall requires an immutable registered task")
    if events is None:
        raise RuntimeAuthorizationError(
            "blind source firewall requires canonical Issue #240 event evidence"
        )
    task_id = str(safe["task"]["task_id"])
    resolved_now = now if now is not None else _core.research_runtime_reducer.now_utc(None)
    scope = _core._execution_scope(state)
    binding = _core._binding_for_scope(
        task_id, scope, events, now=resolved_now, root=root
    )
    _core._reconcile_caller_owner_claim(state, binding)
    return task_id, binding


def write_pre_math_stamp(
    state: Mapping[str, Any],
    *,
    events: list[dict[str, Any]] | None,
    now=None,
    output: Path | None = None,
    created_at: str | None = None,
    root: Path = ROOT,
) -> dict[str, Any]:
    task_id, binding = _blind_binding(state, events=events, now=now, root=root)
    try:
        stamp, path = _firewall.write_pre_math_stamp(
            task_id=task_id,
            binding=binding,
            output=output,
            created_at=created_at,
            root=root,
        )
    except _firewall.SourceFirewallError as exc:
        _raise_firewall(exc)
    return {
        "task_id": task_id,
        "phase": "PRE_MATH",
        "record_path": path.resolve().relative_to(root.resolve()).as_posix(),
        "record": stamp,
    }


def write_raw_freeze(
    state: Mapping[str, Any],
    *,
    events: list[dict[str, Any]] | None,
    pre_math_stamp: Path,
    now=None,
    output: Path | None = None,
    created_at: str | None = None,
    root: Path = ROOT,
) -> dict[str, Any]:
    task_id, binding = _blind_binding(state, events=events, now=now, root=root)
    try:
        record, path = _firewall.write_raw_freeze_record(
            task_id=task_id,
            binding=binding,
            pre_math_stamp_path=pre_math_stamp,
            output=output,
            created_at=created_at,
            root=root,
        )
    except _firewall.SourceFirewallError as exc:
        _raise_firewall(exc)
    return {
        "task_id": task_id,
        "phase": "RAW_FREEZE",
        "record_path": path.resolve().relative_to(root.resolve()).as_posix(),
        "record": record,
    }


def write_source_exposure(
    state: Mapping[str, Any],
    *,
    events: list[dict[str, Any]] | None,
    raw_freeze_record: Path,
    now=None,
    output: Path | None = None,
    created_at: str | None = None,
    root: Path = ROOT,
) -> dict[str, Any]:
    task_id, binding = _blind_binding(state, events=events, now=now, root=root)
    try:
        record, path = _firewall.write_source_exposure_record(
            task_id=task_id,
            binding=binding,
            raw_record_path=raw_freeze_record,
            output=output,
            created_at=created_at,
            root=root,
        )
    except _firewall.SourceFirewallError as exc:
        _raise_firewall(exc)
    return {
        "task_id": task_id,
        "phase": "SOURCE_EXPOSED",
        "record_path": path.resolve().relative_to(root.resolve()).as_posix(),
        "record": record,
    }


def _load_state(args: argparse.Namespace) -> dict[str, Any]:
    return _core._load_state(args)


def _add_state(parser: argparse.ArgumentParser) -> None:
    _core._add_state(parser)


def _events(args: argparse.Namespace):
    return _core.research_dispatch.load_events(args.events) if getattr(args, "events", None) else None


def _add_events_now(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--events", type=Path, required=True)
    parser.add_argument("--now")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Enterprise Math repository-backed runtime guard"
    )
    sub = parser.add_subparsers(dest="command", required=True)

    authorize = sub.add_parser("authorize")
    _add_state(authorize)
    authorize.add_argument("--events", type=Path)
    authorize.add_argument("--now")

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

    adopt = sub.add_parser("adopt")
    _add_state(adopt)
    adopt.add_argument("--events", type=Path)
    adopt.add_argument("--evidence-json", required=True)
    adopt.add_argument("--replacement-session-id", required=True)
    adopt.add_argument("--now", required=True)
    adopt.add_argument(
        "--session-liveness-minutes",
        type=int,
        default=_core.research_runtime.DEFAULT_SESSION_LIVENESS_MINUTES,
    )

    stamp = sub.add_parser("pre-math-stamp")
    _add_state(stamp)
    _add_events_now(stamp)
    stamp.add_argument("--output", type=Path)
    stamp.add_argument("--created-at")

    raw = sub.add_parser("raw-freeze")
    _add_state(raw)
    _add_events_now(raw)
    raw.add_argument("--pre-math-stamp", type=Path, required=True)
    raw.add_argument("--output", type=Path)
    raw.add_argument("--created-at")

    expose = sub.add_parser("source-expose")
    _add_state(expose)
    _add_events_now(expose)
    expose.add_argument("--raw-freeze-record", type=Path, required=True)
    expose.add_argument("--output", type=Path)
    expose.add_argument("--created-at")

    args = parser.parse_args()
    state = _load_state(args)
    events = _events(args)
    parsed_now = (
        _core.research_runtime_reducer.now_utc(args.now)
        if getattr(args, "now", None) is not None
        else None
    )

    if args.command == "authorize":
        result = authorize_execution(state, events=events, now=parsed_now)
    elif args.command == "pre-final":
        result = pre_final_gate(state)
    elif args.command == "terminal":
        result = _core.apply_terminal_event(state, args.event)
    elif args.command == "adopt":
        evidence = json.loads(args.evidence_json)
        if not isinstance(evidence, dict):
            raise RuntimeAuthorizationError("evidence must decode to an object")
        result = _startup.attach(
            _core.adopt_stale_session(
                state,
                evidence,
                replacement_session_id=args.replacement_session_id,
                now=_core.research_runtime.parse_time(args.now),
                events=events,
                session_liveness_minutes=args.session_liveness_minutes,
            )
        )
    elif args.command == "pre-math-stamp":
        result = write_pre_math_stamp(
            state,
            events=events,
            now=parsed_now,
            output=args.output,
            created_at=args.created_at,
        )
    elif args.command == "raw-freeze":
        result = write_raw_freeze(
            state,
            events=events,
            pre_math_stamp=args.pre_math_stamp,
            now=parsed_now,
            output=args.output,
            created_at=args.created_at,
        )
    elif args.command == "source-expose":
        result = write_source_exposure(
            state,
            events=events,
            raw_freeze_record=args.raw_freeze_record,
            now=parsed_now,
            output=args.output,
            created_at=args.created_at,
        )
    else:
        raise AssertionError(args.command)

    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
    if args.command == "pre-final" and _is_control_only_pre_final_state(state):
        return 0 if result["final_allowed"] else 2
    if _is_activity_state(state) and args.command in ("authorize", "pre-final"):
        allowed = (result["activity_allowed"] and result["persistence_allowed"]) if args.command == "authorize" else result["final_allowed"]
        return 0 if allowed else 2
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except RuntimeAuthorizationError as exc:
        print("ERROR:", exc)
        raise SystemExit(1)
