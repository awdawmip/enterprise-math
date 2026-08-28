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
from pathlib import Path
from typing import Any, Mapping

from control_plane.research_runtime_guard_core import *  # noqa: F401,F403
from control_plane import research_runtime_guard_core as _core
from control_plane import research_source_firewall as _firewall

ROOT = _core.ROOT
RuntimeAuthorizationError = _core.RuntimeAuthorizationError


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
    result = _core.authorize_execution(state, events=events, now=now, root=root)
    binding = result.get("execution_binding")
    if not isinstance(binding, Mapping):
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
    resolved_now = now if now is not None else _core.research_scheduler.now_utc(None)
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
        _core.research_scheduler.now_utc(args.now)
        if getattr(args, "now", None) is not None
        else None
    )

    if args.command == "authorize":
        result = authorize_execution(state, events=events, now=parsed_now)
    elif args.command == "pre-final":
        result = _core.pre_final_gate(state)
    elif args.command == "terminal":
        result = _core.apply_terminal_event(state, args.event)
    elif args.command == "adopt":
        evidence = json.loads(args.evidence_json)
        if not isinstance(evidence, dict):
            raise RuntimeAuthorizationError("evidence must decode to an object")
        result = _core.adopt_stale_session(
            state,
            evidence,
            replacement_session_id=args.replacement_session_id,
            now=_core.research_runtime.parse_time(args.now),
            events=events,
            session_liveness_minutes=args.session_liveness_minutes,
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
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except RuntimeAuthorizationError as exc:
        print("ERROR:", exc)
        raise SystemExit(1)
