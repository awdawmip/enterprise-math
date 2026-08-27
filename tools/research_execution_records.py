#!/usr/bin/env python3
"""Immutable task-publication -> execution-intent records."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
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
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
import research_execution_cohorts  # noqa: E402

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


def execution_record_id(
    task_id: str,
    publication_id: str,
    claim_id: str,
    researcher_id: str,
    execution_branch: str,
    execution_cohort_id: str | None = None,
    execution_lane_id: str | None = None,
) -> str:
    fields = [task_id, publication_id, claim_id, researcher_id, execution_branch]
    if execution_cohort_id is not None or execution_lane_id is not None:
        if not execution_cohort_id or not execution_lane_id:
            raise ExecutionRecordError("execution cohort and lane must be supplied together")
        fields.extend((execution_cohort_id, execution_lane_id))
    raw = "\0".join(fields).encode("utf-8")
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


def _scope_pair(
    execution_cohort_id: str | None, execution_lane_id: str | None
) -> tuple[str | None, str | None]:
    cohort = execution_cohort_id.strip() if isinstance(execution_cohort_id, str) and execution_cohort_id.strip() else None
    lane = execution_lane_id.strip() if isinstance(execution_lane_id, str) and execution_lane_id.strip() else None
    if (cohort is None) != (lane is None):
        raise ExecutionRecordError("execution_cohort_id and execution_lane_id must be supplied together")
    return cohort, lane


def intent_for_claim(
    task_id: str,
    claim_id: str,
    root: Path = ROOT,
    *,
    execution_cohort_id: str | None = None,
    execution_lane_id: str | None = None,
) -> dict[str, Any] | None:
    cohort, lane = _scope_pair(execution_cohort_id, execution_lane_id)
    matches = []
    for item in iter_records(root):
        if item.get("task_id") != task_id or item.get("claim_id") != claim_id:
            continue
        item_cohort = item.get("execution_cohort_id")
        item_lane = item.get("execution_lane_id")
        if cohort is None:
            if item_cohort is None and item_lane is None:
                matches.append(item)
        elif item_cohort == cohort and item_lane == lane:
            matches.append(item)
    if len(matches) > 1:
        scope = f"/{cohort}/{lane}" if cohort is not None else ""
        raise ExecutionRecordError(f"multiple execution intents for {task_id}{scope}/{claim_id}")
    return matches[0] if matches else None


def current_task_record(task_id: str, root: Path = ROOT) -> dict[str, Any]:
    record = research_task_records.current_records(root).get(task_id)
    if record is None:
        raise ExecutionRecordError("execution intents are required only for immutable registered tasks")
    if record.get("claimable") is not True:
        raise ExecutionRecordError("task is not claimable")
    return record


def _safe_output(value: str) -> str | None:
    text = value.strip().replace("\\", "/")
    path = Path(text)
    if not text or path.is_absolute() or ".." in path.parts:
        return None
    return text


def _lane_publication(
    task_id: str,
    cohort_id: str,
    lane_id: str,
    allowed_outputs: list[str],
    root: Path,
) -> tuple[dict[str, Any], str]:
    cohort = research_execution_cohorts.cohort_map(root).get(cohort_id)
    if cohort is None or cohort.get("task_id") != task_id:
        raise ExecutionRecordError("unknown execution cohort for task")
    if cohort.get("record_state") != "ACTIVE":
        raise ExecutionRecordError("execution cohort must be ACTIVE when execution provenance is prepared")
    lanes = [
        item for item in cohort.get("lanes", [])
        if isinstance(item, dict) and item.get("lane_id") == lane_id
    ]
    if len(lanes) != 1:
        raise ExecutionRecordError("unknown or ambiguous execution lane")
    lane = lanes[0]
    publication_id = lane.get("publication_id")
    record = publication_map(root).get(str(publication_id))
    if record is None or record.get("task_id") != task_id:
        raise ExecutionRecordError("lane publication is unknown for task")
    if record.get("claimable") is not True:
        raise ExecutionRecordError("lane publication is not claimable")
    try:
        prefix = research_execution_cohorts._safe_prefix(lane.get("output_prefix"))
    except Exception as exc:
        raise ExecutionRecordError(f"lane output_prefix invalid: {exc}") from exc
    for output in allowed_outputs:
        text = _safe_output(output)
        if text is None or not text.startswith(prefix):
            raise ExecutionRecordError("allowed_outputs escape execution lane output_prefix")
    return record, prefix


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
    execution_cohort_id: str | None = None,
    execution_lane_id: str | None = None,
    root: Path = ROOT,
) -> dict[str, Any]:
    cohort, lane_id = _scope_pair(execution_cohort_id, execution_lane_id)
    if not claim_id.strip():
        raise ExecutionRecordError("claim_id is required")
    if not allowed_outputs or any(not isinstance(item, str) or not item.strip() for item in allowed_outputs):
        raise ExecutionRecordError("allowed_outputs must be a nonempty string list")
    if len(set(allowed_outputs)) != len(allowed_outputs):
        raise ExecutionRecordError("allowed_outputs contains duplicates")
    if cohort is None:
        record = current_task_record(task_id, root)
        lane_output_prefix = None
    else:
        record, lane_output_prefix = _lane_publication(task_id, cohort, str(lane_id), allowed_outputs, root)
    taskbook_path = root / record["taskbook_path"]
    meta, _ = research_taskbook.split_taskbook(taskbook_path.read_text(encoding="utf-8"))
    identity_lane = meta.get("identity_lane") if isinstance(meta.get("identity_lane"), str) else None
    resolved_id = (
        researcher_id.strip().upper()
        if isinstance(researcher_id, str) and researcher_id.strip()
        else research_identity.deterministic_claim_id(task_id, claim_id, lane=identity_lane)
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
    erid = execution_record_id(
        task_id,
        record["publication_id"],
        claim_id,
        resolved_id,
        execution_branch,
        cohort,
        lane_id,
    )
    value: dict[str, Any] = {
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
    if cohort is not None:
        value.update(
            {
                "execution_cohort_id": cohort,
                "execution_lane_id": lane_id,
                "lane_output_prefix": lane_output_prefix,
            }
        )
    return value


def audit(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    seen_ids: set[str] = set()
    seen_claims: set[tuple[str, str, str, str]] = set()
    try:
        publications = publication_map(root)
        cohort_map = research_execution_cohorts.cohort_map(root)
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
        cohort_id = item.get("execution_cohort_id")
        lane_id = item.get("execution_lane_id")
        if (cohort_id is None) != (lane_id is None):
            errors.append(f"{prefix}: cohort/lane identity must be both present or both absent")
        scope_key = (
            str(task_id),
            str(cohort_id or "NONCOHORT"),
            str(lane_id or "NONCOHORT"),
            str(claim_id),
        )
        if scope_key in seen_claims:
            errors.append(f"{prefix}: duplicate execution claim within owner scope")
        seen_claims.add(scope_key)
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
        outputs = item.get("allowed_outputs")
        if not isinstance(outputs, list) or not outputs or not all(isinstance(x, str) and x.strip() for x in outputs):
            errors.append(f"{prefix}: allowed_outputs invalid")
            outputs = []
        if cohort_id is not None and lane_id is not None:
            cohort = cohort_map.get(str(cohort_id))
            if cohort is None or cohort.get("task_id") != task_id:
                errors.append(f"{prefix}: unknown execution cohort for task")
            else:
                lanes = [
                    row for row in cohort.get("lanes", [])
                    if isinstance(row, dict) and row.get("lane_id") == lane_id
                ]
                if len(lanes) != 1:
                    errors.append(f"{prefix}: unknown or ambiguous execution lane")
                else:
                    lane = lanes[0]
                    if lane.get("publication_id") != publication_id:
                        errors.append(f"{prefix}: execution publication differs from lane publication pin")
                    try:
                        lane_prefix = research_execution_cohorts._safe_prefix(lane.get("output_prefix"))
                    except Exception as exc:
                        errors.append(f"{prefix}: invalid lane output_prefix: {exc}")
                    else:
                        if item.get("lane_output_prefix") != lane_prefix:
                            errors.append(f"{prefix}: lane_output_prefix differs from cohort lane")
                        for output in outputs:
                            text = _safe_output(output)
                            if text is None or not text.startswith(lane_prefix):
                                errors.append(f"{prefix}: allowed output escapes cohort lane: {output}")
        if not research_identity.valid_execution_id(str(item.get("researcher_id", ""))):
            errors.append(f"{prefix}: invalid researcher_id")
        if not isinstance(item.get("theorem_owner"), str) or not item["theorem_owner"].strip():
            errors.append(f"{prefix}: theorem_owner missing")
        if not isinstance(item.get("execution_branch"), str) or not item["execution_branch"].strip():
            errors.append(f"{prefix}: execution_branch missing")
        if not re.fullmatch(r"[0-9a-f]{40}", str(item.get("execution_branch_base", ""))):
            errors.append(f"{prefix}: execution_branch_base invalid")
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
        execution_cohort_id=args.execution_cohort_id,
        execution_lane_id=args.execution_lane_id,
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
    prepare.add_argument("--execution-cohort-id")
    prepare.add_argument("--execution-lane-id")
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
