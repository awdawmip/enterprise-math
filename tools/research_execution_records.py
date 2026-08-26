#!/usr/bin/env python3
"""Immutable task-publication -> execution-intent records."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

try:
    from tools import research_identity
    from tools import research_task_records
    from tools import research_taskbook
except ModuleNotFoundError:
    import research_identity  # type: ignore
    import research_task_records  # type: ignore
    import research_taskbook  # type: ignore

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = "ENTERPRISE_MATH_RESEARCH_EXECUTION_RECORD_V1"


class ExecutionRecordError(ValueError):
    pass


def _safe(value: str, label: str) -> str:
    if not re.fullmatch(r"[A-Za-z0-9._-]+", value):
        raise ExecutionRecordError(f"{label} contains unsupported characters")
    return value


def _parse_time(value: str) -> datetime:
    dt = datetime.fromisoformat(value.strip().replace("Z", "+00:00"))
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc)


def _now(value: str | None) -> str:
    return (_parse_time(value) if value else datetime.now(timezone.utc)).isoformat()


def _save_exclusive(path: Path, value: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = json.dumps(value, ensure_ascii=False, indent=2) + "\n"
    try:
        with path.open("x", encoding="utf-8") as handle:
            handle.write(payload)
            handle.flush()
            os.fsync(handle.fileno())
    except FileExistsError as exc:
        raise ExecutionRecordError(f"immutable execution record already exists: {path}") from exc


def execution_record_id(task_id: str, publication_id: str, claim_id: str, researcher_id: str, execution_branch: str) -> str:
    raw = "\0".join((task_id, publication_id, claim_id, researcher_id, execution_branch)).encode("utf-8")
    return "ER-" + hashlib.sha256(raw).hexdigest()[:20].upper()


def iter_records(root: Path = ROOT) -> list[dict[str, Any]]:
    directory = root / "research_execution_records"
    if not directory.exists():
        return []
    out = []
    for path in sorted(directory.glob("*/*.json")):
        value = json.loads(path.read_text(encoding="utf-8"))
        value["_record_path"] = path.relative_to(root).as_posix()
        out.append(value)
    return out


def publication_map(root: Path = ROOT) -> dict[str, dict[str, Any]]:
    """Index every immutable task publication generation, not only the current head."""
    out: dict[str, dict[str, Any]] = {}
    for item in research_task_records.iter_records(root):
        publication_id = item.get("publication_id")
        if not isinstance(publication_id, str) or not publication_id:
            continue
        if publication_id in out:
            raise ExecutionRecordError(f"duplicate task publication_id: {publication_id}")
        out[publication_id] = item
    return out


def intent_for_claim(task_id: str, claim_id: str, root: Path = ROOT) -> dict[str, Any] | None:
    matches = [
        item for item in iter_records(root)
        if item.get("task_id") == task_id and item.get("claim_id") == claim_id
    ]
    if len(matches) > 1:
        raise ExecutionRecordError(f"multiple execution intents for {task_id}/{claim_id}")
    return matches[0] if matches else None


def current_task_record(task_id: str, root: Path = ROOT) -> dict[str, Any]:
    record = research_task_records.current_records(root).get(task_id)
    if record is None:
        raise ExecutionRecordError("execution intents are required only for immutable registered tasks")
    if record.get("claimable") is not True:
        raise ExecutionRecordError("task is not claimable")
    return record


def prepare_intent(
    *,
    task_id: str,
    claim_id: str,
    researcher_id: str | None,
    theorem_owner: str,
    execution_branch: str,
    execution_branch_base: str,
    allowed_outputs: list[str],
    owner_lease_minutes: int,
    prepared_at: str,
    root: Path = ROOT,
) -> dict[str, Any]:
    record = current_task_record(task_id, root)
    if not claim_id.strip():
        raise ExecutionRecordError("claim_id is required")
    taskbook_path = root / record["taskbook_path"]
    meta, _ = research_taskbook.split_taskbook(taskbook_path.read_text(encoding="utf-8"))
    lane = meta.get("identity_lane") if isinstance(meta.get("identity_lane"), str) else None
    resolved_id = (
        researcher_id.strip().upper()
        if isinstance(researcher_id, str) and researcher_id.strip()
        else research_identity.deterministic_claim_id(task_id, claim_id, lane=lane)
    )
    if not research_identity.valid_execution_id(resolved_id):
        raise ExecutionRecordError("invalid researcher_id")
    if not theorem_owner.strip():
        raise ExecutionRecordError("theorem_owner is required as a distinct typed field")
    if not execution_branch.strip():
        raise ExecutionRecordError("execution_branch is required")
    if not re.fullmatch(r"[0-9a-fA-F]{40}", execution_branch_base.strip()):
        raise ExecutionRecordError("execution_branch_base must be a 40-hex commit SHA")
    if type(owner_lease_minutes) is not int or owner_lease_minutes <= 0:
        raise ExecutionRecordError("owner_lease_minutes must be a positive integer")
    if not allowed_outputs or any(not isinstance(item, str) or not item.strip() for item in allowed_outputs):
        raise ExecutionRecordError("allowed_outputs must be a nonempty string list")
    if len(set(allowed_outputs)) != len(allowed_outputs):
        raise ExecutionRecordError("allowed_outputs contains duplicates")
    erid = execution_record_id(task_id, record["publication_id"], claim_id, resolved_id, execution_branch)
    return {
        "record_schema": SCHEMA,
        "record_state": "CLAIM_INTENT",
        "execution_record_id": erid,
        "task_id": task_id,
        "publication_id": record["publication_id"],
        "taskbook_path": record["taskbook_path"],
        "taskbook_blob_sha1": record["taskbook_blob_sha1"],
        "claim_id": claim_id,
        "researcher_id": resolved_id,
        "theorem_owner": theorem_owner,
        "execution_branch": execution_branch,
        "execution_branch_base": execution_branch_base.lower(),
        "allowed_outputs": allowed_outputs,
        "owner_lease_minutes": owner_lease_minutes,
        "prepared_at": prepared_at,
    }


def audit(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    seen_ids: set[str] = set()
    seen_claims: set[tuple[str, str]] = set()
    try:
        publications = publication_map(root)
    except Exception as exc:
        return [str(exc)]
    for item in iter_records(root):
        prefix = item.get("_record_path", "<execution-record>")
        if item.get("record_schema") != SCHEMA:
            errors.append(f"{prefix}: wrong record_schema")
        erid = item.get("execution_record_id")
        if not isinstance(erid, str) or not erid:
            errors.append(f"{prefix}: missing execution_record_id")
        elif erid in seen_ids:
            errors.append(f"{prefix}: duplicate execution_record_id")
        seen_ids.add(str(erid))
        task_id = item.get("task_id")
        claim_id = item.get("claim_id")
        pair = (str(task_id), str(claim_id))
        if pair in seen_claims:
            errors.append(f"{prefix}: duplicate task/claim execution intent")
        seen_claims.add(pair)
        publication_id = item.get("publication_id")
        record = publications.get(str(publication_id))
        if record is None:
            errors.append(f"{prefix}: unknown publication generation: {publication_id}")
            continue
        if record.get("task_id") != task_id:
            errors.append(f"{prefix}: publication generation belongs to a different task")
        if item.get("taskbook_path") != record.get("taskbook_path"):
            errors.append(f"{prefix}: taskbook path differs from referenced publication generation")
        if item.get("taskbook_blob_sha1") != record.get("taskbook_blob_sha1"):
            errors.append(f"{prefix}: taskbook blob differs from referenced publication generation")
        if not research_identity.valid_execution_id(str(item.get("researcher_id", ""))):
            errors.append(f"{prefix}: invalid researcher_id")
        if not isinstance(item.get("theorem_owner"), str) or not item["theorem_owner"].strip():
            errors.append(f"{prefix}: theorem_owner missing")
        if not isinstance(item.get("execution_branch"), str) or not item["execution_branch"].strip():
            errors.append(f"{prefix}: execution_branch missing")
        if not re.fullmatch(r"[0-9a-f]{40}", str(item.get("execution_branch_base", ""))):
            errors.append(f"{prefix}: execution_branch_base invalid")
        outputs = item.get("allowed_outputs")
        if not isinstance(outputs, list) or not outputs or not all(isinstance(x, str) and x.strip() for x in outputs):
            errors.append(f"{prefix}: allowed_outputs invalid")
    return errors


def command_prepare(args: argparse.Namespace) -> int:
    outputs = json.loads(args.allowed_outputs_json)
    if not isinstance(outputs, list):
        raise ExecutionRecordError("--allowed-outputs-json must decode to an array")
    record = prepare_intent(
        task_id=args.task_id,
        claim_id=args.claim_id,
        researcher_id=args.researcher_id,
        theorem_owner=args.theorem_owner,
        execution_branch=args.execution_branch,
        execution_branch_base=args.execution_branch_base,
        allowed_outputs=outputs,
        owner_lease_minutes=args.owner_lease_minutes,
        prepared_at=_now(args.prepared_at),
    )
    path = ROOT / "research_execution_records" / _safe(args.task_id, "task_id") / f"{record['execution_record_id']}.json"
    _save_exclusive(path, record)
    errors = audit()
    if errors:
        raise ExecutionRecordError("execution record created but audit failed: " + "; ".join(errors))
    print(json.dumps({**record, "record_path": path.relative_to(ROOT).as_posix()}, ensure_ascii=False, indent=2))
    return 0


def command_audit(args: argparse.Namespace) -> int:
    errors = audit()
    if errors:
        for error in errors:
            print("ERROR:", error)
        return 1
    print(f"PASS: execution intents valid ({len(iter_records())} record(s)).")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Enterprise Math immutable execution intent records")
    sub = parser.add_subparsers(dest="command", required=True)
    prepare = sub.add_parser("prepare-claim")
    prepare.add_argument("--task-id", required=True)
    prepare.add_argument("--claim-id", required=True)
    prepare.add_argument("--researcher-id")
    prepare.add_argument("--theorem-owner", required=True)
    prepare.add_argument("--execution-branch", required=True)
    prepare.add_argument("--execution-branch-base", required=True)
    prepare.add_argument("--allowed-outputs-json", required=True)
    prepare.add_argument("--owner-lease-minutes", type=int, default=120)
    prepare.add_argument("--prepared-at")
    prepare.set_defaults(func=command_prepare)
    audit_parser = sub.add_parser("audit")
    audit_parser.set_defaults(func=command_audit)
    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except ExecutionRecordError as exc:
        print("ERROR:", exc)
        raise SystemExit(1)
