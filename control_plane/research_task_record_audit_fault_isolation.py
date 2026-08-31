#!/usr/bin/env python3
"""Exact audit-only isolation for nonoperational immutable task-record defects.

This layer is deliberately separate from current-task integrity quarantine:

* current sole-head defects must be handled by ``research_task_integrity_quarantines.json``
  and project the task to BLOCKED;
* this module may suppress strict-audit errors only for records that are already
  nonoperational for an independently verified reason: a directly superseded
  same-task generation, or an active head inside an unresolved publication fork
  that is itself locally BLOCKED by publication-fork quarantine.

Every suppression pins exact record bytes, exact taskbook bytes and exact error
suffixes. Full immutable-record audit errors and earliest publication-envelope
errors are tracked separately so one checker's vocabulary cannot become a stale
or overbroad waiver in another. A malformed immutable record may itself omit or
drift its taskbook blob pin only when ``allowed_publication_envelope_errors`` is
exactly that one record-side pin defect; the quarantine still pins the actual
taskbook Git blob independently. It grants no dispatch, publication selection,
Working Truth, Foundation, canonical-promotion or successor authority.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

QUARANTINE_FILE = "research_task_record_audit_quarantines.json"
SCHEMA = "ENTERPRISE_MATH_TASK_RECORD_AUDIT_QUARANTINE_V1"
STATE = "NONOPERATIONAL_IMMUTABLE_RECORD_INTEGRITY_FAULT"
BASIS_SUPERSEDED = "DIRECTLY_SUPERSEDED_SAME_TASK"
BASIS_FORK_BLOCKED = "TASK_BLOCKED_BY_PUBLICATION_FORK_QUARANTINE"
BASES = {BASIS_SUPERSEDED, BASIS_FORK_BLOCKED}
SHA1 = re.compile(r"^sha1:[0-9a-f]{40}$")


class TaskRecordAuditIsolationError(ValueError):
    pass


def _load(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise TaskRecordAuditIsolationError(f"{path}: JSON root must be object")
    return value


def _validate_error_list(row: dict[str, Any], qid: str, field: str, *, required: bool) -> list[str]:
    value = row.get(field)
    if value is None and not required:
        return []
    if (
        not isinstance(value, list)
        or (required and not value)
        or any(not isinstance(item, str) or not item for item in value)
        or len(set(value)) != len(value)
    ):
        raise TaskRecordAuditIsolationError(f"{qid}: {field} invalid")
    return value


def quarantine_rows(root: Path = ROOT) -> list[dict[str, Any]]:
    path = root / QUARANTINE_FILE
    if not path.exists():
        return []
    payload = _load(path)
    if payload.get("schema") != SCHEMA or payload.get("status") != "ACTIVE":
        raise TaskRecordAuditIsolationError(f"{QUARANTINE_FILE}: wrong schema/status")
    rows = payload.get("quarantines")
    if not isinstance(rows, list):
        raise TaskRecordAuditIsolationError(f"{QUARANTINE_FILE}: quarantines must be list")

    seen_ids: set[str] = set()
    seen_publications: set[str] = set()
    out: list[dict[str, Any]] = []
    for index, row in enumerate(rows):
        if not isinstance(row, dict):
            raise TaskRecordAuditIsolationError(f"{QUARANTINE_FILE}: row {index} must be object")
        quarantine_id = row.get("quarantine_id")
        task_id = row.get("task_id")
        publication_id = row.get("publication_id")
        if not isinstance(quarantine_id, str) or not quarantine_id or quarantine_id in seen_ids:
            raise TaskRecordAuditIsolationError(
                f"{QUARANTINE_FILE}: invalid/duplicate quarantine_id {quarantine_id!r}"
            )
        if not isinstance(task_id, str) or not task_id:
            raise TaskRecordAuditIsolationError(f"{quarantine_id}: missing task_id")
        if (
            not isinstance(publication_id, str)
            or not publication_id
            or publication_id in seen_publications
        ):
            raise TaskRecordAuditIsolationError(
                f"{quarantine_id}: invalid/duplicate publication_id {publication_id!r}"
            )
        if row.get("state") != STATE:
            raise TaskRecordAuditIsolationError(f"{quarantine_id}: wrong state")
        if row.get("nonoperational_basis") not in BASES:
            raise TaskRecordAuditIsolationError(f"{quarantine_id}: unsupported nonoperational_basis")
        if row.get("operational") is not False or row.get("history_preserved") is not True:
            raise TaskRecordAuditIsolationError(
                f"{quarantine_id}: record-audit quarantine must be nonoperational retained history"
            )
        for field in (
            "record_path",
            "record_blob_sha1",
            "taskbook_path",
            "taskbook_blob_sha1",
        ):
            if not isinstance(row.get(field), str) or not row[field]:
                raise TaskRecordAuditIsolationError(f"{quarantine_id}: missing {field}")
        _validate_error_list(row, quarantine_id, "allowed_task_record_audit_errors", required=True)
        _validate_error_list(row, quarantine_id, "allowed_publication_envelope_errors", required=False)
        for flag in (
            "working_truth_granted",
            "foundation_authority_granted",
            "canonical_promotion_granted",
            "successor_triggered",
            "operational_publication_selected",
        ):
            if row.get(flag) is not False:
                raise TaskRecordAuditIsolationError(f"{quarantine_id}: cannot grant {flag}")
        seen_ids.add(quarantine_id)
        seen_publications.add(publication_id)
        out.append(row)
    return out


def _declared_taskbook_pin_defect(record: dict[str, Any], actual_pin: str) -> str | None:
    """Return the exact envelope suffix represented by a bad record-side pin."""
    declared = record.get("taskbook_blob_sha1")
    if not isinstance(declared, str) or not SHA1.fullmatch(declared):
        return "missing/invalid taskbook_blob_sha1"
    if declared != actual_pin:
        return f"taskbook Git blob drift: declared {declared}, actual {actual_pin}"
    return None


def validated_rows(root: Path = ROOT) -> list[dict[str, Any]]:
    from control_plane import research_publication_fault_isolation as fork_isolation
    from control_plane import research_task_records_impl as core

    rows = quarantine_rows(root)
    records = core.iter_records(root)
    by_publication = {
        str(record.get("publication_id")): record
        for record in records
        if isinstance(record.get("publication_id"), str)
    }
    fork_rows: dict[str, dict[str, Any]] | None = None

    for row in rows:
        qid = row["quarantine_id"]
        task_id = row["task_id"]
        publication_id = row["publication_id"]
        record = by_publication.get(publication_id)
        if record is None:
            raise TaskRecordAuditIsolationError(
                f"{qid}: unknown publication_id {publication_id}"
            )
        if record.get("task_id") != task_id:
            raise TaskRecordAuditIsolationError(f"{qid}: publication belongs to another task")
        if record.get("_record_path") != row["record_path"]:
            raise TaskRecordAuditIsolationError(f"{qid}: record_path drift")
        record_path = root / row["record_path"]
        if not record_path.is_file():
            raise TaskRecordAuditIsolationError(f"{qid}: record path missing")
        actual_record_blob = core.git_blob_sha1_bytes(record_path.read_bytes())
        if actual_record_blob != row["record_blob_sha1"]:
            raise TaskRecordAuditIsolationError(
                f"{qid}: record blob drift; declared={row['record_blob_sha1']} "
                f"actual={actual_record_blob}"
            )
        if record.get("taskbook_path") != row["taskbook_path"]:
            raise TaskRecordAuditIsolationError(f"{qid}: taskbook_path drift")
        taskbook_path = root / row["taskbook_path"]
        if not taskbook_path.is_file():
            raise TaskRecordAuditIsolationError(f"{qid}: taskbook path missing")
        actual_taskbook_blob = core.taskbook_blob(taskbook_path)
        if actual_taskbook_blob != row["taskbook_blob_sha1"]:
            raise TaskRecordAuditIsolationError(
                f"{qid}: taskbook blob drift; declared={row['taskbook_blob_sha1']} "
                f"actual={actual_taskbook_blob}"
            )

        record_pin_defect = _declared_taskbook_pin_defect(record, actual_taskbook_blob)
        envelope_allowed = _validate_error_list(
            row,
            qid,
            "allowed_publication_envelope_errors",
            required=False,
        )
        expected_envelope = [] if record_pin_defect is None else [record_pin_defect]
        if envelope_allowed != expected_envelope:
            raise TaskRecordAuditIsolationError(
                f"{qid}: allowed_publication_envelope_errors must equal the exact "
                f"record-side taskbook pin defect; expected={expected_envelope!r} "
                f"actual={envelope_allowed!r}"
            )

        basis = row["nonoperational_basis"]
        if basis == BASIS_SUPERSEDED:
            generation = record.get("publication_generation")
            successors = [
                candidate
                for candidate in records
                if candidate.get("task_id") == task_id
                and candidate.get("supersedes_publication_id") == publication_id
            ]
            if not successors:
                raise TaskRecordAuditIsolationError(
                    f"{qid}: publication is not directly superseded by same-task history"
                )
            if not isinstance(generation, int) or any(
                not isinstance(candidate.get("publication_generation"), int)
                or candidate["publication_generation"] <= generation
                for candidate in successors
            ):
                raise TaskRecordAuditIsolationError(
                    f"{qid}: direct successor generation is not strictly newer"
                )
        elif basis == BASIS_FORK_BLOCKED:
            if fork_rows is None:
                fork_rows = fork_isolation.validated_quarantines(root)
            fork = fork_rows.get(task_id)
            if fork is None:
                raise TaskRecordAuditIsolationError(
                    f"{qid}: task is not currently blocked by publication-fork quarantine"
                )
            effective = set(fork.get("_effective_publication_ids", fork.get("publication_ids", [])))
            if publication_id not in effective:
                raise TaskRecordAuditIsolationError(
                    f"{qid}: publication is not a current blocked fork head; "
                    f"effective_heads={sorted(effective)}"
                )
    return rows


def suppression_strings(root: Path = ROOT) -> set[str]:
    """Exact suppressions for the full immutable task-record audit only."""
    return {
        f"{row['record_path']}: {suffix}"
        for row in validated_rows(root)
        for suffix in row["allowed_task_record_audit_errors"]
    }


def envelope_suppression_strings(root: Path = ROOT) -> set[str]:
    """Exact suppressions for the earliest publication-envelope checker only."""
    return {
        f"{row['record_path']}: {suffix}"
        for row in validated_rows(root)
        for suffix in row.get("allowed_publication_envelope_errors", [])
    }


def audit_against(raw_errors: list[str], root: Path = ROOT) -> list[str]:
    try:
        suppressions = suppression_strings(root)
    except Exception as exc:
        return [str(exc)]
    raw_set = set(raw_errors)
    errors = [
        f"{QUARANTINE_FILE}: stale or unused suppression: {item}"
        for item in sorted(suppressions - raw_set)
    ]
    errors.extend(item for item in raw_errors if item not in suppressions)
    return errors


def main() -> int:
    try:
        rows = validated_rows(ROOT)
    except Exception as exc:
        print("ERROR:", exc)
        return 1
    print(
        "PASS: exact nonoperational task-record audit quarantine valid "
        f"({len(rows)} immutable record(s)); no runtime authority granted."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
