#!/usr/bin/env python3
"""Exact task-local isolation for known current publication integrity faults.

Runtime availability and governance strictness are deliberately separated:

* exact, durably pinned known-bad current publications are locally BLOCKED and
  removed from operational current-record selection;
* unrelated tasks remain dispatchable;
* strict task-record audit errors are suppressible only when the exact record
  blob, taskbook blob, and exact error suffix are pinned in the quarantine file;
* every declared suppression must be used, so a repaired/drifted publication
  makes the quarantine stale and fails CI until the control record is updated;
* no quarantine grants Working Truth, Foundation authority, canonical promotion,
  successor authority, or an operational publication selection.

This module does not rewrite taskbooks or decide research semantics.
"""
from __future__ import annotations

import copy
import json
from collections import defaultdict
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
QUARANTINE_FILE = "research_task_integrity_quarantines.json"
QUARANTINE_SCHEMA = "ENTERPRISE_MATH_TASK_INTEGRITY_QUARANTINE_V1"
QUARANTINE_STATE = "INVALID_CURRENT_TASK_PUBLICATION"


class TaskIntegrityIsolationError(ValueError):
    pass


def _load(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise TaskIntegrityIsolationError(f"{path}: JSON root must be object")
    return value


def quarantine_rows(root: Path = ROOT) -> dict[str, dict[str, Any]]:
    path = root / QUARANTINE_FILE
    if not path.exists():
        return {}
    payload = _load(path)
    if payload.get("schema") != QUARANTINE_SCHEMA:
        raise TaskIntegrityIsolationError(f"{QUARANTINE_FILE}: wrong schema")
    if payload.get("status") != "ACTIVE":
        raise TaskIntegrityIsolationError(f"{QUARANTINE_FILE}: status must be ACTIVE")
    rows = payload.get("quarantines")
    if not isinstance(rows, list):
        raise TaskIntegrityIsolationError(f"{QUARANTINE_FILE}: quarantines must be list")

    out: dict[str, dict[str, Any]] = {}
    seen_publications: set[str] = set()
    for index, row in enumerate(rows):
        if not isinstance(row, dict):
            raise TaskIntegrityIsolationError(f"{QUARANTINE_FILE}: row {index} must be object")
        task_id = row.get("task_id")
        publication_id = row.get("publication_id")
        if not isinstance(task_id, str) or not task_id:
            raise TaskIntegrityIsolationError(f"{QUARANTINE_FILE}: row {index} missing task_id")
        if task_id in out:
            raise TaskIntegrityIsolationError(f"{QUARANTINE_FILE}: duplicate task {task_id}")
        if not isinstance(publication_id, str) or not publication_id:
            raise TaskIntegrityIsolationError(f"{QUARANTINE_FILE}: {task_id} missing publication_id")
        if publication_id in seen_publications:
            raise TaskIntegrityIsolationError(
                f"{QUARANTINE_FILE}: duplicate publication {publication_id}"
            )
        if row.get("state") != QUARANTINE_STATE:
            raise TaskIntegrityIsolationError(f"{QUARANTINE_FILE}: {task_id} wrong state")
        if row.get("operational_publication_id") is not None:
            raise TaskIntegrityIsolationError(
                f"{QUARANTINE_FILE}: {task_id} quarantine cannot select an operational publication"
            )
        if row.get("isolation_scope") != "CONTROL_PLANE_ONLY":
            raise TaskIntegrityIsolationError(f"{QUARANTINE_FILE}: {task_id} wrong isolation_scope")
        for field in ("record_path", "record_blob_sha1", "taskbook_path", "taskbook_blob_sha1"):
            value = row.get(field)
            if not isinstance(value, str) or not value:
                raise TaskIntegrityIsolationError(
                    f"{QUARANTINE_FILE}: {task_id} missing {field}"
                )
        allowed = row.get("allowed_task_record_audit_errors")
        if (
            not isinstance(allowed, list)
            or not allowed
            or any(not isinstance(item, str) or not item for item in allowed)
            or len(set(allowed)) != len(allowed)
        ):
            raise TaskIntegrityIsolationError(
                f"{QUARANTINE_FILE}: {task_id} allowed_task_record_audit_errors invalid"
            )
        for flag in (
            "working_truth_granted",
            "foundation_authority_granted",
            "canonical_promotion_granted",
            "successor_triggered",
        ):
            if row.get(flag) is not False:
                raise TaskIntegrityIsolationError(
                    f"{QUARANTINE_FILE}: {task_id} cannot grant {flag}"
                )
        out[task_id] = row
        seen_publications.add(publication_id)
    return out


def _active_heads(records: list[dict[str, Any]], terminal_states: set[str]) -> dict[str, list[dict[str, Any]]]:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for record in records:
        task_id = record.get("task_id")
        if isinstance(task_id, str) and task_id:
            grouped[task_id].append(record)
    out: dict[str, list[dict[str, Any]]] = {}
    for task_id, values in grouped.items():
        superseded = {
            item.get("supersedes_publication_id")
            for item in values
            if isinstance(item.get("supersedes_publication_id"), str)
            and item.get("supersedes_publication_id")
        }
        heads = [
            item
            for item in values
            if item.get("publication_id") not in superseded
            and item.get("record_state", "ACTIVE") not in terminal_states
        ]
        if heads:
            out[task_id] = heads
    return out


def validated_quarantines(root: Path = ROOT) -> dict[str, dict[str, Any]]:
    """Validate exact current head, record blob, taskbook blob, and authority nulls."""
    from control_plane import research_task_records_impl as core

    rows = quarantine_rows(root)
    records = core.iter_records(root)
    heads = _active_heads(records, core.TERMINAL_RECORD_STATES)
    by_publication = {
        str(record.get("publication_id")): record
        for record in records
        if isinstance(record.get("publication_id"), str)
    }

    for task_id, row in rows.items():
        publication_id = row["publication_id"]
        record = by_publication.get(publication_id)
        if record is None:
            raise TaskIntegrityIsolationError(
                f"{task_id}: quarantine references unknown publication {publication_id}"
            )
        if record.get("task_id") != task_id:
            raise TaskIntegrityIsolationError(f"{task_id}: publication belongs to another task")
        active_ids = {
            str(item.get("publication_id"))
            for item in heads.get(task_id, [])
            if item.get("publication_id")
        }
        if active_ids != {publication_id}:
            raise TaskIntegrityIsolationError(
                f"{task_id}: integrity quarantine requires exactly one pinned active head; "
                f"expected={[publication_id]!r} actual={sorted(active_ids)!r}"
            )
        if record.get("_record_path") != row["record_path"]:
            raise TaskIntegrityIsolationError(f"{task_id}: record_path drift")
        record_path = root / row["record_path"]
        if not record_path.exists():
            raise TaskIntegrityIsolationError(f"{task_id}: quarantined record path missing")
        actual_record_blob = core.git_blob_sha1_bytes(record_path.read_bytes())
        if actual_record_blob != row["record_blob_sha1"]:
            raise TaskIntegrityIsolationError(
                f"{task_id}: quarantined record blob drift; "
                f"declared={row['record_blob_sha1']} actual={actual_record_blob}"
            )
        if record.get("taskbook_path") != row["taskbook_path"]:
            raise TaskIntegrityIsolationError(f"{task_id}: taskbook_path drift")
        taskbook_path = root / row["taskbook_path"]
        if not taskbook_path.exists():
            raise TaskIntegrityIsolationError(f"{task_id}: quarantined taskbook path missing")
        actual_taskbook_blob = core.git_blob_sha1_bytes(taskbook_path.read_bytes())
        if actual_taskbook_blob != row["taskbook_blob_sha1"]:
            raise TaskIntegrityIsolationError(
                f"{task_id}: quarantined taskbook blob drift; "
                f"declared={row['taskbook_blob_sha1']} actual={actual_taskbook_blob}"
            )
    return rows


def suppression_strings(root: Path = ROOT) -> set[str]:
    rows = validated_quarantines(root)
    return {
        f"{row['record_path']}: {suffix}"
        for row in rows.values()
        for suffix in row["allowed_task_record_audit_errors"]
    }


def blocked_definition(
    task_id: str, row: dict[str, Any], prior: dict[str, Any] | None = None
) -> dict[str, Any]:
    value = copy.deepcopy(prior or {})
    value.update(
        {
            "task_id": task_id,
            "title": value.get("title", task_id),
            "kind": value.get("kind", "RESEARCH"),
            "owner": value.get("owner", "control-plane/task-integrity-quarantine"),
            "base_state": "BLOCKED",
            "priority": value.get("priority", "P2"),
            "leverage": value.get("leverage", "MEDIUM"),
            "frontier": "INVALID_CURRENT_TASK_PUBLICATION",
            "next_action": "REPAIR_OR_REPUBLISH_CURRENT_TASK_UNDER_ORDINARY_AUTHORITY",
            "dependencies": copy.deepcopy(value.get("dependencies", [])),
            "source_refs": sorted(
                set(value.get("source_refs", []))
                | {row["record_path"], row["taskbook_path"], row["publication_id"]}
            ),
            "evidence_status": "CONTROL_PLANE_QUARANTINED_INVALID_CURRENT_TASK_PUBLICATION",
            "last_progress_ref": QUARANTINE_FILE,
            "last_progress_at": value.get("last_progress_at", "1970-01-01T00:00:00+00:00"),
            "hard_block": {
                "code": "INVALID_CURRENT_TASK_PUBLICATION",
                "publication_id": row["publication_id"],
                "record_path": row["record_path"],
                "record_blob_sha1": row["record_blob_sha1"],
                "taskbook_path": row["taskbook_path"],
                "taskbook_blob_sha1": row["taskbook_blob_sha1"],
                "operational_publication_id": None,
            },
            "tags": sorted(set(value.get("tags", [])) | {"CONTROL_PLANE_INTEGRITY_QUARANTINE"}),
            "claim_lease_minutes": int(value.get("claim_lease_minutes") or 120),
            "publication_id": None,
            "publication_ids": [row["publication_id"]],
            "registration_source": "TASK_INTEGRITY_QUARANTINE",
        }
    )
    return value


def install(root: Path = ROOT) -> None:
    """Layer exact integrity quarantine on top of publication-fork isolation."""
    from control_plane import research_publication_fault_isolation as publication_isolation

    publication_isolation.install(root)
    rows = validated_quarantines(root)

    from control_plane import research_task_records_impl as core
    from tools import research_dispatch, research_task_records

    if not getattr(core, "_task_integrity_fault_isolation_installed", False):
        base_current = research_task_records.current_records

        def current_records(local_root: Path = root) -> dict[str, dict[str, Any]]:
            current = dict(base_current(local_root))
            for task_id in validated_quarantines(local_root):
                current.pop(task_id, None)
            return current

        core.current_records = current_records
        research_task_records.current_records = current_records
        core._task_integrity_fault_isolation_installed = True

    if not getattr(research_dispatch, "_task_integrity_fault_isolation_installed", False):
        base_merged = research_dispatch.merged_definitions

        def merged_definitions(local_root: Path = research_dispatch.ROOT) -> list[dict[str, Any]]:
            values = base_merged(local_root)
            by_id = {
                item["task_id"]: item
                for item in values
                if isinstance(item, dict) and isinstance(item.get("task_id"), str)
            }
            for task_id, row in validated_quarantines(local_root).items():
                by_id[task_id] = blocked_definition(task_id, row, by_id.get(task_id))
            return [by_id[key] for key in sorted(by_id)]

        research_dispatch.merged_definitions = merged_definitions
        research_dispatch._task_integrity_fault_isolation_installed = True

    # Force exact validation even on repeated installs where monkeypatches are
    # already resident in this interpreter.
    if set(rows) != set(validated_quarantines(root)):
        raise TaskIntegrityIsolationError("task integrity quarantine changed during install")


def audit_task_records(root: Path = ROOT) -> list[str]:
    """Run strict audit and subtract only exact pinned, currently-used errors."""
    try:
        install(root)
        from tools import research_task_records

        strict_audit = getattr(research_task_records, "strict_audit", research_task_records.audit)
        raw_errors = list(strict_audit(root))
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


def audit_runtime_projection(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    try:
        install(root)
        from tools import research_dispatch, research_task_records

        rows = validated_quarantines(root)
        current = research_task_records.current_records(root)
        definitions = {
            item["task_id"]: item for item in research_dispatch.merged_definitions(root)
        }
        for task_id, row in rows.items():
            if task_id in current:
                errors.append(f"{task_id}: integrity-quarantined task remains current")
            item = definitions.get(task_id)
            if item is None:
                errors.append(f"{task_id}: integrity quarantine missing from dispatch view")
                continue
            if item.get("base_state") != "BLOCKED":
                errors.append(f"{task_id}: integrity quarantine is not BLOCKED")
            if item.get("publication_id") is not None:
                errors.append(f"{task_id}: integrity quarantine selected a publication")
            if item.get("registration_source") != "TASK_INTEGRITY_QUARANTINE":
                errors.append(f"{task_id}: integrity quarantine registration source drifted")
            if item.get("hard_block", {}).get("publication_id") != row["publication_id"]:
                errors.append(f"{task_id}: integrity quarantine publication pin drifted")
    except Exception as exc:
        errors.append(str(exc))
    return errors


def audit(root: Path = ROOT) -> list[str]:
    return [*audit_task_records(root), *audit_runtime_projection(root)]


def main() -> int:
    errors = audit()
    if errors:
        for error in errors:
            print("ERROR:", error)
        return 1
    print(
        "PASS: exact task-integrity quarantine valid "
        f"({len(quarantine_rows())} locally blocked publication(s))."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
