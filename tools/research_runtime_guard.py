#!/usr/bin/env python3
"""Repository-backed authorization guard for the Enterprise Math runtime.

The historical tools/research_runtime.py remains the pure liveness/terminal
primitive. This wrapper authenticates TASK_REGISTRATION against immutable task
records or the frozen legacy baseline before delegating. It also owns the
optional blind/independent PRE_MATH source-firewall gate so no second control
utility or GitHub hot path is introduced.
"""
from __future__ import annotations

import argparse
import copy
import json
import os
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping

try:
    from tools import research_result_records
    from tools import research_runtime
    from tools import research_task_records
    from tools import research_taskbook
except ModuleNotFoundError:
    import research_result_records  # type: ignore
    import research_runtime  # type: ignore
    import research_task_records  # type: ignore
    import research_taskbook  # type: ignore

ROOT = Path(__file__).resolve().parents[1]
SOURCE_FIREWALL_CONTRACT = "research_source_firewall_contract.json"
STAMP_SCHEMA = "ENTERPRISE_MATH_BLIND_EXECUTION_STAMP_V1"
STAMP_PHASE = "STARTED_BEFORE_MATH"
HEX40 = re.compile(r"^[0-9a-fA-F]{40}$")


class RuntimeAuthorizationError(ValueError):
    pass


def _load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _parse_time(value: str | None) -> str:
    if value:
        dt = datetime.fromisoformat(value.strip().replace("Z", "+00:00"))
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
    else:
        dt = datetime.now(timezone.utc)
    return dt.astimezone(timezone.utc).isoformat()


def _git(root: Path, *args: str) -> str:
    try:
        proc = subprocess.run(
            ["git", *args],
            cwd=root,
            check=False,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
    except OSError as exc:
        raise RuntimeAuthorizationError(f"git is unavailable for source-firewall validation: {exc}") from exc
    if proc.returncode != 0:
        detail = proc.stderr.strip() or proc.stdout.strip() or "git command failed"
        raise RuntimeAuthorizationError(detail)
    return proc.stdout.strip()


def _normalize_blob(value: Any) -> str:
    if not isinstance(value, str):
        raise RuntimeAuthorizationError("source pin blob_sha1 must be a string")
    text = value.strip().lower()
    if text.startswith("sha1:"):
        text = text[5:]
    if not HEX40.fullmatch(text):
        raise RuntimeAuthorizationError("source pin blob_sha1 must be a 40-hex Git blob SHA-1")
    return text


def validate_source_firewall_config(value: Any) -> dict[str, Any] | None:
    """Validate the optional taskbook source_firewall object.

    None/NONE means no extra blind gate. BLIND_INDEPENDENT is deliberately strict:
    every allowed mathematical source is path+commit+blob pinned and the stamp is
    created before route-specific source exposure.
    """
    if value in (None, {}, "NONE"):
        return None
    if not isinstance(value, Mapping):
        raise RuntimeAuthorizationError("source_firewall must be an object")
    mode = value.get("mode")
    if mode == "NONE":
        return None
    if mode != "BLIND_INDEPENDENT":
        raise RuntimeAuthorizationError("source_firewall.mode must be NONE or BLIND_INDEPENDENT")
    if value.get("pre_math_stamp_required") is not True:
        raise RuntimeAuthorizationError("BLIND_INDEPENDENT requires pre_math_stamp_required=true")
    if type(value.get("remote_stamp_before_math_required")) is not bool:
        raise RuntimeAuthorizationError("source_firewall.remote_stamp_before_math_required must be boolean")
    pins = value.get("allowed_source_pins")
    if not isinstance(pins, list) or not pins:
        raise RuntimeAuthorizationError("BLIND_INDEPENDENT requires nonempty allowed_source_pins")
    normalized_pins: list[dict[str, str]] = []
    seen: set[tuple[str, str]] = set()
    for index, pin in enumerate(pins):
        if not isinstance(pin, Mapping):
            raise RuntimeAuthorizationError(f"allowed_source_pins[{index}] must be an object")
        path = pin.get("path")
        commit = pin.get("commit")
        if not isinstance(path, str) or not path.strip() or path.startswith("/") or ".." in Path(path).parts:
            raise RuntimeAuthorizationError(f"allowed_source_pins[{index}].path must be a safe repository-relative path")
        if not isinstance(commit, str) or not HEX40.fullmatch(commit.strip()):
            raise RuntimeAuthorizationError(f"allowed_source_pins[{index}].commit must be a 40-hex commit SHA")
        blob = _normalize_blob(pin.get("blob_sha1"))
        key = (commit.lower(), path)
        if key in seen:
            raise RuntimeAuthorizationError("allowed_source_pins contains duplicate commit/path pin")
        seen.add(key)
        normalized_pins.append({"path": path, "commit": commit.lower(), "blob_sha1": blob})
    withheld = value.get("withheld_until_raw_freeze")
    if not isinstance(withheld, list) or any(not isinstance(item, str) or not item.strip() for item in withheld):
        raise RuntimeAuthorizationError("withheld_until_raw_freeze must be a string list")
    raw = value.get("raw_freeze_path")
    if not isinstance(raw, str) or not raw.strip() or raw.startswith("/") or ".." in Path(raw).parts:
        raise RuntimeAuthorizationError("raw_freeze_path must be a safe repository-relative path")
    return {
        "mode": mode,
        "pre_math_stamp_required": True,
        "remote_stamp_before_math_required": value["remote_stamp_before_math_required"],
        "allowed_source_pins": normalized_pins,
        "withheld_until_raw_freeze": list(withheld),
        "raw_freeze_path": raw,
    }


def _current_task_record(task_id: str, root: Path) -> dict[str, Any]:
    try:
        record = research_task_records.current_records(root).get(task_id)
    except Exception as exc:
        raise RuntimeAuthorizationError(f"cannot resolve current task publication: {exc}") from exc
    if record is None:
        raise RuntimeAuthorizationError("source-firewall PRE_MATH gate requires an immutable registered task")
    return record


def source_firewall_for_task(task_id: str, root: Path = ROOT) -> tuple[dict[str, Any] | None, dict[str, Any]]:
    record = _current_task_record(task_id, root)
    path = root / record["taskbook_path"]
    try:
        meta, _ = research_taskbook.split_taskbook(path.read_text(encoding="utf-8"))
    except Exception as exc:
        raise RuntimeAuthorizationError(f"cannot parse taskbook source_firewall: {exc}") from exc
    return validate_source_firewall_config(meta.get("source_firewall")), record


def validate_source_pins(firewall: Mapping[str, Any], root: Path = ROOT) -> list[dict[str, str]]:
    """Validate exact source pins using only the local Git object database."""
    results: list[dict[str, str]] = []
    for pin in firewall["allowed_source_pins"]:
        commit = pin["commit"]
        path = pin["path"]
        declared_blob = pin["blob_sha1"]
        resolved_commit = _git(root, "rev-parse", "--verify", f"{commit}^{{commit}}")
        if resolved_commit.lower() != commit:
            raise RuntimeAuthorizationError(f"source pin commit did not resolve exactly: {commit}")
        actual_blob = _git(root, "rev-parse", f"{commit}:{path}").lower()
        if not HEX40.fullmatch(actual_blob):
            raise RuntimeAuthorizationError(f"source pin did not resolve to a Git object: {path}@{commit}")
        if actual_blob != declared_blob:
            raise RuntimeAuthorizationError(
                f"source pin blob mismatch for {path}@{commit}: declared {declared_blob}, actual {actual_blob}"
            )
        results.append({
            "path": path,
            "commit": commit,
            "declared_blob_sha1": declared_blob,
            "actual_blob_sha1": actual_blob,
            "status": "PASS",
        })
    return results


def default_stamp_path(task_id: str, root: Path = ROOT) -> Path:
    safe = re.sub(r"[^A-Za-z0-9._-]+", "_", task_id)
    return root / "evidence" / safe / "execution_stamp.json"


def build_pre_math_stamp(
    *,
    task_id: str,
    researcher_id: str,
    created_at: str | None = None,
    root: Path = ROOT,
) -> dict[str, Any]:
    firewall, record = source_firewall_for_task(task_id, root)
    if firewall is None:
        raise RuntimeAuthorizationError("task does not declare a BLIND_INDEPENDENT source_firewall")
    if not isinstance(researcher_id, str) or not researcher_id.strip():
        raise RuntimeAuthorizationError("researcher_id is required for PRE_MATH stamp")
    source_validation = validate_source_pins(firewall, root)
    return {
        "schema": STAMP_SCHEMA,
        "phase": STAMP_PHASE,
        "task_id": task_id,
        "publication_id": record["publication_id"],
        "taskbook_path": record["taskbook_path"],
        "taskbook_blob_sha1": record["taskbook_blob_sha1"],
        "researcher_id": researcher_id.strip().upper(),
        "created_at": _parse_time(created_at),
        "math_source_read_before_stamp": False,
        "source_validation": source_validation,
        "allowed_source_pins": copy.deepcopy(firewall["allowed_source_pins"]),
        "withheld_until_raw_freeze": copy.deepcopy(firewall["withheld_until_raw_freeze"]),
        "raw_freeze_path": firewall["raw_freeze_path"],
        "remote_stamp_before_math_required": firewall["remote_stamp_before_math_required"],
        "remote_stamp_verification": "TASK_SPECIFIC_EXTERNAL_ORCHESTRATOR_REQUIRED" if firewall["remote_stamp_before_math_required"] else "NOT_REQUIRED_BEFORE_MATH",
    }


def write_pre_math_stamp(
    *,
    task_id: str,
    researcher_id: str,
    output: Path | None = None,
    created_at: str | None = None,
    root: Path = ROOT,
) -> tuple[dict[str, Any], Path]:
    stamp = build_pre_math_stamp(
        task_id=task_id,
        researcher_id=researcher_id,
        created_at=created_at,
        root=root,
    )
    path = output or default_stamp_path(task_id, root)
    if not path.is_absolute():
        path = root / path
    try:
        path.resolve().relative_to(root.resolve())
    except ValueError as exc:
        raise RuntimeAuthorizationError("execution stamp must be inside repository root") from exc
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = json.dumps(stamp, ensure_ascii=False, indent=2) + "\n"
    try:
        with path.open("x", encoding="utf-8") as handle:
            handle.write(payload)
            handle.flush()
            os.fsync(handle.fileno())
    except FileExistsError as exc:
        raise RuntimeAuthorizationError(f"refusing to overwrite existing PRE_MATH stamp: {path}") from exc
    return stamp, path


def verify_pre_math_stamp(
    task_id: str,
    stamp_path: Path,
    *,
    root: Path = ROOT,
) -> dict[str, Any]:
    firewall, record = source_firewall_for_task(task_id, root)
    if firewall is None:
        raise RuntimeAuthorizationError("task does not declare a source_firewall")
    path = stamp_path if stamp_path.is_absolute() else root / stamp_path
    if not path.exists():
        raise RuntimeAuthorizationError(f"PRE_MATH stamp does not exist: {path}")
    stamp = _load_json(path)
    if stamp.get("schema") != STAMP_SCHEMA or stamp.get("phase") != STAMP_PHASE:
        raise RuntimeAuthorizationError("invalid PRE_MATH stamp schema/phase")
    if stamp.get("task_id") != task_id:
        raise RuntimeAuthorizationError("PRE_MATH stamp task_id mismatch")
    if stamp.get("publication_id") != record.get("publication_id"):
        raise RuntimeAuthorizationError("PRE_MATH stamp publication_id is stale")
    if stamp.get("taskbook_path") != record.get("taskbook_path") or stamp.get("taskbook_blob_sha1") != record.get("taskbook_blob_sha1"):
        raise RuntimeAuthorizationError("PRE_MATH stamp taskbook pin mismatch")
    if stamp.get("math_source_read_before_stamp") is not False:
        raise RuntimeAuthorizationError("PRE_MATH stamp must state math_source_read_before_stamp=false")
    if stamp.get("allowed_source_pins") != firewall.get("allowed_source_pins"):
        raise RuntimeAuthorizationError("PRE_MATH stamp allowed_source_pins differ from current taskbook firewall")
    if stamp.get("withheld_until_raw_freeze") != firewall.get("withheld_until_raw_freeze"):
        raise RuntimeAuthorizationError("PRE_MATH stamp withheld-source list differs from current taskbook firewall")
    if stamp.get("raw_freeze_path") != firewall.get("raw_freeze_path"):
        raise RuntimeAuthorizationError("PRE_MATH stamp raw_freeze_path mismatch")
    expected = validate_source_pins(firewall, root)
    if stamp.get("source_validation") != expected:
        raise RuntimeAuthorizationError("PRE_MATH stamp source_validation is stale or inconsistent")
    return stamp


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
    task_id = safe["task"]["task_id"]
    firewall = None
    if safe["task_registration"]["state"] == "IMMUTABLE_REGISTERED":
        firewall, _ = source_firewall_for_task(task_id, root)
    stamp_ref = None
    if firewall is not None and firewall.get("pre_math_stamp_required") is True:
        frontier = safe.get("durable_frontier")
        stamp_ref = frontier.get("execution_stamp") if isinstance(frontier, Mapping) else None
        if not isinstance(stamp_ref, str) or not stamp_ref.strip():
            raise RuntimeAuthorizationError("BLIND_INDEPENDENT execution requires PRE_MATH execution_stamp before source exposure")
        verify_pre_math_stamp(task_id, Path(stamp_ref), root=root)
        if firewall.get("remote_stamp_before_math_required") is True:
            remote = frontier.get("remote_stamp_verification") if isinstance(frontier, Mapping) else None
            if not isinstance(remote, Mapping) or remote.get("verified") is not True:
                raise RuntimeAuthorizationError(
                    "task-specific remote_stamp_before_math_required=true; external orchestrator must verify the remote stamp before mathematics"
                )
    return {
        "authorized": True,
        "task_id": task_id,
        "task_registration": safe["task_registration"],
        "source_firewall": "BLIND_INDEPENDENT_PRE_MATH_VERIFIED" if firewall is not None else "NOT_APPLICABLE",
        "execution_stamp": stamp_ref,
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

    pre_math = sub.add_parser("pre-math-stamp")
    pre_math.add_argument("--task-id", required=True)
    pre_math.add_argument("--researcher-id", required=True)
    pre_math.add_argument("--output", type=Path)
    pre_math.add_argument("--created-at")

    verify_stamp = sub.add_parser("verify-pre-math-stamp")
    verify_stamp.add_argument("--task-id", required=True)
    verify_stamp.add_argument("--stamp", type=Path, required=True)

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
    if args.command == "pre-math-stamp":
        stamp, path = write_pre_math_stamp(
            task_id=args.task_id,
            researcher_id=args.researcher_id,
            output=args.output,
            created_at=args.created_at,
        )
        result = {**stamp, "stamp_path": path.relative_to(ROOT).as_posix()}
    elif args.command == "verify-pre-math-stamp":
        result = verify_pre_math_stamp(args.task_id, args.stamp)
    else:
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
