#!/usr/bin/env python3
"""Repository-backed authorization guard for the Enterprise Math runtime.

The historical tools/research_runtime.py remains the pure liveness/terminal
primitive. This wrapper is canonical because it authenticates TASK_REGISTRATION
against immutable task records or the frozen legacy baseline before delegating.
"""
from __future__ import annotations

import argparse
import copy
import json
from pathlib import Path
from typing import Any, Mapping

try:
    from tools import research_result_records
    from tools import research_runtime
    from tools import research_task_records
except ModuleNotFoundError:
    import research_result_records  # type: ignore
    import research_runtime  # type: ignore
    import research_task_records  # type: ignore

ROOT = Path(__file__).resolve().parents[1]


class RuntimeAuthorizationError(ValueError):
    pass


def _load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def legacy_task_ids(root: Path = ROOT) -> set[str]:
    scheduler = _load_json(root / "research_scheduler.json")
    return {
        task["task_id"]
        for task in scheduler.get("tasks", [])
        if isinstance(task, dict) and isinstance(task.get("task_id"), str)
    }


def canonicalize_registration(
    state: Mapping[str, Any], *, purpose: str, root: Path = ROOT
) -> dict[str, Any]:
    task = state.get("task")
    if not isinstance(task, Mapping):
        raise RuntimeAuthorizationError("task must be an object")
    task_id = task.get("task_id")
    if not isinstance(task_id, str) or not task_id:
        raise RuntimeAuthorizationError("task.task_id is required")

    try:
        current = research_task_records.current_records(root)
    except Exception as exc:
        raise RuntimeAuthorizationError(
            f"cannot resolve canonical task records: {exc}"
        ) from exc

    updated = copy.deepcopy(dict(state))
    if task_id in current:
        record = current[task_id]
        if record.get("claimable") is not True and purpose in {"execution", "adopt"}:
            raise RuntimeAuthorizationError("registered task is not execution-eligible")
        if record.get("record_state", "ACTIVE") != "ACTIVE" and purpose in {"execution", "adopt"}:
            raise RuntimeAuthorizationError("registered task publication generation is not ACTIVE")
        result_state = research_result_records.task_result_state(task_id, root)
        if (
            purpose in {"execution", "adopt"}
            and result_state is not None
            and result_state.get("state") in {"AWAITING_DRIVER_REVIEW", "TERMINAL"}
        ):
            raise RuntimeAuthorizationError(
                f"task execution is closed by result state {result_state.get('state')}"
            )
        updated["task_registration"] = {
            "state": "IMMUTABLE_REGISTERED",
            "registry_key": task_id,
            "publication_id": record.get("publication_id"),
            "record_path": record.get("_record_path"),
            "claimable": record.get("claimable"),
        }
        return updated

    if task_id in legacy_task_ids(root):
        supplied = state.get("task_registration")
        fresh = isinstance(supplied, Mapping) and supplied.get("fresh_redispatch") is True
        if fresh:
            raise RuntimeAuthorizationError(
                "legacy baseline cannot authorize fresh redispatch; publish an immutable task record"
            )
        if purpose in {"execution", "adopt"}:
            claim = state.get("owner_claim")
            if not isinstance(claim, Mapping) or not claim.get("claim_id"):
                raise RuntimeAuthorizationError(
                    "legacy baseline permits only already-owned continuation; fresh claim requires migration"
                )
        updated["task_registration"] = {
            "state": "LEGACY_BASELINE_REGISTERED",
            "registry_key": None,
            "fresh_redispatch": False,
        }
        return updated

    raise RuntimeAuthorizationError(
        f"task {task_id!r} is neither immutably registered nor in the frozen legacy baseline"
    )


def _delegate_safe_state(
    state: Mapping[str, Any], *, purpose: str, root: Path = ROOT
) -> dict[str, Any]:
    safe = canonicalize_registration(state, purpose=purpose, root=root)
    if safe["task_registration"]["state"] == "IMMUTABLE_REGISTERED":
        safe["task_registration"]["state"] = "CLAIMABLE"
    return safe


def pre_final_gate(state: Mapping[str, Any], *, root: Path = ROOT) -> dict[str, Any]:
    safe = _delegate_safe_state(state, purpose="pre_final", root=root)
    decision = research_runtime.pre_final_gate(safe)
    decision["registration_authenticated"] = True
    decision["registration_authority"] = (
        "FROZEN_LEGACY_BASELINE"
        if safe["task_registration"]["state"] == "LEGACY_BASELINE_REGISTERED"
        else "IMMUTABLE_TASK_RECORD"
    )
    return decision


def apply_terminal_event(
    state: Mapping[str, Any], event: str, *, root: Path = ROOT
) -> dict[str, Any]:
    safe = _delegate_safe_state(state, purpose="terminal", root=root)
    value = research_runtime.apply_terminal_event(safe, event)
    value["registration_authenticated"] = True
    return value


def adopt_stale_session(
    state: Mapping[str, Any],
    evidence: Mapping[str, Any],
    *,
    replacement_session_id: str,
    now,
    session_liveness_minutes: int = research_runtime.DEFAULT_SESSION_LIVENESS_MINUTES,
    root: Path = ROOT,
) -> dict[str, Any]:
    safe = _delegate_safe_state(state, purpose="adopt", root=root)
    return research_runtime.adopt_stale_session(
        safe,
        evidence,
        replacement_session_id=replacement_session_id,
        now=now,
        session_liveness_minutes=session_liveness_minutes,
    )


def authorize_execution(
    state: Mapping[str, Any], *, root: Path = ROOT
) -> dict[str, Any]:
    safe = canonicalize_registration(state, purpose="execution", root=root)
    return {
        "authorized": True,
        "task_id": safe["task"]["task_id"],
        "task_registration": safe["task_registration"],
    }


def _load_state(args: argparse.Namespace) -> dict[str, Any]:
    if args.state_json:
        value = json.loads(args.state_json)
    else:
        value = json.loads(Path(args.state_file).read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise RuntimeAuthorizationError("state must decode to an object")
    return value


def _add_state(parser: argparse.ArgumentParser) -> None:
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--state-json")
    group.add_argument("--state-file")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Enterprise Math repository-backed runtime guard"
    )
    sub = parser.add_subparsers(dest="command", required=True)

    authorize = sub.add_parser("authorize")
    _add_state(authorize)

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
    adopt.add_argument("--evidence-json", required=True)
    adopt.add_argument("--replacement-session-id", required=True)
    adopt.add_argument("--now", required=True)
    adopt.add_argument(
        "--session-liveness-minutes",
        type=int,
        default=research_runtime.DEFAULT_SESSION_LIVENESS_MINUTES,
    )

    args = parser.parse_args()
    state = _load_state(args)
    if args.command == "authorize":
        result = authorize_execution(state)
    elif args.command == "pre-final":
        result = pre_final_gate(state)
    elif args.command == "terminal":
        result = apply_terminal_event(state, args.event)
    elif args.command == "adopt":
        evidence = json.loads(args.evidence_json)
        if not isinstance(evidence, dict):
            raise RuntimeAuthorizationError("evidence must decode to an object")
        result = adopt_stale_session(
            state,
            evidence,
            replacement_session_id=args.replacement_session_id,
            now=research_runtime.parse_time(args.now),
            session_liveness_minutes=args.session_liveness_minutes,
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
