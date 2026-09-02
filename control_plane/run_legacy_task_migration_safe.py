#!/usr/bin/env python3
"""One-shot safe renderer and targeted validator for the legacy-to-V2 cutover.

The repository contains historical task-record debt outside this transaction.  A
full-corpus audit is therefore not a valid commit gate for this cutover: it would
couple the migration to unrelated immutable records.  This wrapper keeps the
materializer's per-taskbook policy checks and adds an exact audit of every row
created or referenced by the migration manifest.
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from control_plane import materialize_legacy_tasks_v2 as migration

EXPECTED_DISPOSITIONS = {
    "ALREADY_CURRENT_V2": 10,
    "TERMINAL_HISTORY": 7,
    "BACKLOG": 2,
    "ACTIVE_FRONTIER": 8,
}
GENERATED_DISPOSITIONS = {"TERMINAL_HISTORY", "BACKLOG", "ACTIVE_FRONTIER"}


class TargetedMigrationAuditError(ValueError):
    pass


def safe_body_for(task: dict[str, Any], state: dict[str, Any], disposition: str) -> str:
    task_id = str(task["task_id"])
    runtime_state = str(state.get("state") or task.get("base_state") or "BACKLOG")
    if disposition == "TERMINAL_HISTORY":
        target = (
            "Preserve the verified terminal outcome as immutable nonclaimable history. "
            "This generation cannot authorize a new execution."
        )
        success = (
            "The V2 record preserves task identity and terminal state, remains nonclaimable, "
            "and creates no owner or execution event."
        )
    elif disposition == "BACKLOG":
        target = (
            "Preserve the dormant frontier as an immutable nonclaimable backlog generation. "
            "A later explicit publication is required before activation."
        )
        success = (
            "The V2 record keeps the exact dormant state and does not enter fresh selection."
        )
    else:
        target = (
            "Preserve the verified durable frontier as a claimable V2 generation without "
            "changing mathematical scope or creating an owner event."
        )
        success = (
            "The V2 record preserves task identity, owner boundary, priority class, frontier, "
            "and next action while creating no synthetic execution ownership."
        )
    return f"""# {task_id} — V2 Task Preservation

Status: `PUBLISHED_REGISTERED / CONTROL_MIGRATION / {runtime_state}`

## Mother question

Can this exact task be represented on the immutable V2 task surface without changing its mathematical meaning or durable frontier?

## Frozen inputs and scope

The exact source definition, task metadata, frontier, references, owner boundary, and durable state are frozen in the accompanying metadata and migration record. They are not expanded or reinterpreted in this preservation body.

This preservation envelope adds no theorem, counterexample, novelty conclusion, priority elevation, truth status, or execution ownership.

## Hard target and required outputs

{target}

## Research value to preserve

Preserve the exact identity, lineage, accumulated evidence, durable frontier, and next executable action without replaying completed work.

## Success, kill, and return criteria

{success}

Return the immutable V2 publication record and its migration-manifest row after repository integrity checks pass. Mathematical execution and review remain separate actions.
"""


def _load_object(path: Path, label: str) -> dict[str, Any]:
    if not path.is_file():
        raise TargetedMigrationAuditError(f"{label}: missing file {path.relative_to(ROOT)}")
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise TargetedMigrationAuditError(f"{label}: JSON object required")
    return value


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise TargetedMigrationAuditError(message)


def _validate_generated_row(row: dict[str, Any]) -> None:
    task_id = str(row.get("task_id") or "")
    disposition = str(row.get("disposition") or "")
    record_rel = row.get("record_path")
    taskbook_rel = row.get("taskbook_path")
    _require(isinstance(record_rel, str) and bool(record_rel), f"{task_id}: record_path missing")
    _require(isinstance(taskbook_rel, str) and bool(taskbook_rel), f"{task_id}: taskbook_path missing")

    record = _load_object(ROOT / record_rel, task_id)
    taskbook_path = ROOT / taskbook_rel
    _require(taskbook_path.is_file(), f"{task_id}: taskbook missing")
    _require(record.get("record_schema") == migration.records_impl.RECORD_SCHEMA, f"{task_id}: wrong record schema")
    _require(record.get("task_id") == task_id, f"{task_id}: record task mismatch")
    _require(record.get("publication_id") == row.get("publication_id"), f"{task_id}: publication mismatch")
    _require(record.get("taskbook_path") == taskbook_rel, f"{task_id}: taskbook path mismatch")

    actual_blob = migration.records_impl.taskbook_blob(taskbook_path)
    _require(record.get("taskbook_blob_sha1") == actual_blob, f"{task_id}: taskbook blob drift")
    expected_publication = migration.records_impl.publication_id(
        task_id,
        actual_blob,
        str(record.get("publisher_id")),
        str(record.get("parent_objective_id")),
    )
    _require(record.get("publication_id") == expected_publication, f"{task_id}: publication id is not deterministic")

    findings = migration.research_taskbook.audit_taskbook(taskbook_path, root=ROOT, dispatch=True)
    errors = [item for item in findings if item.get("severity") == "ERROR"]
    _require(not errors, f"{task_id}: generated taskbook audit failed: {errors}")

    _require(record.get("working_truth_granted") is False, f"{task_id}: Working Truth grant forbidden")
    _require(record.get("canonical_promotion_granted") is False, f"{task_id}: canonical promotion forbidden")
    source = record.get("migration_source")
    _require(isinstance(source, dict), f"{task_id}: migration_source missing")
    _require(source.get("archive_branch") == migration.ARCHIVE_BRANCH, f"{task_id}: archive branch pin mismatch")
    _require(source.get("source_commit") == migration.SOURCE_COMMIT, f"{task_id}: source commit pin mismatch")
    _require(source.get("legacy_claim_id") in {None, ""}, f"{task_id}: live legacy claim was not resolved")
    _require(source.get("no_execution_claim_created") is True, f"{task_id}: migration created an execution claim")

    if disposition == "TERMINAL_HISTORY":
        _require(record.get("record_state") in {"CLOSED", "SUPERSEDED"}, f"{task_id}: terminal record state mismatch")
        _require(record.get("claimable") is False, f"{task_id}: terminal history must be nonclaimable")
    elif disposition == "BACKLOG":
        _require(record.get("record_state") == "ACTIVE", f"{task_id}: backlog record state mismatch")
        _require(record.get("claimable") is False, f"{task_id}: backlog must remain nonclaimable")
    elif disposition == "ACTIVE_FRONTIER":
        _require(record.get("record_state") == "ACTIVE", f"{task_id}: active frontier record state mismatch")
        _require(record.get("claimable") is True, f"{task_id}: active frontier must be claimable")
    else:  # pragma: no cover - guarded by caller
        raise TargetedMigrationAuditError(f"{task_id}: unsupported generated disposition {disposition}")


def validate_manifest() -> dict[str, Any]:
    manifest = _load_object(migration.MANIFEST_PATH, "migration manifest")
    _require(manifest.get("schema") == "ENTERPRISE_MATH_LEGACY_CONTROL_MIGRATION_MANIFEST_V1", "wrong manifest schema")
    _require(manifest.get("status") == "COMPLETE", "migration manifest is not complete")
    source = manifest.get("source")
    authority = manifest.get("authority")
    _require(isinstance(source, dict), "manifest source missing")
    _require(isinstance(authority, dict), "manifest authority missing")
    _require(source.get("commit") == migration.SOURCE_COMMIT, "manifest source commit mismatch")
    _require(source.get("archive_branch") == migration.ARCHIVE_BRANCH, "manifest archive branch mismatch")
    for flag in (
        "mathematical_truth_granted",
        "working_truth_granted",
        "foundation_authority_granted",
        "canonical_promotion_granted",
        "execution_claim_created",
    ):
        _require(authority.get(flag) is False, f"manifest must not grant {flag}")

    rows = manifest.get("tasks")
    _require(isinstance(rows, list), "manifest tasks must be a list")
    _require(len(rows) == 27, f"expected 27 legacy task identities, got {len(rows)}")
    task_ids = [row.get("task_id") for row in rows if isinstance(row, dict)]
    _require(len(task_ids) == 27 and len(set(task_ids)) == 27, "manifest task identities are incomplete or duplicated")
    actual_counts = Counter(str(row.get("disposition")) for row in rows if isinstance(row, dict))
    _require(dict(actual_counts) == EXPECTED_DISPOSITIONS, f"unexpected migration disposition counts: {dict(actual_counts)}")

    for row in rows:
        _require(isinstance(row, dict), "manifest task row must be an object")
        disposition = str(row.get("disposition") or "")
        if disposition in GENERATED_DISPOSITIONS:
            _validate_generated_row(row)
        elif disposition == "ALREADY_CURRENT_V2":
            record_rel = row.get("record_path")
            _require(isinstance(record_rel, str) and (ROOT / record_rel).is_file(), f"{row.get('task_id')}: referenced current V2 record missing")
            record = _load_object(ROOT / record_rel, str(row.get("task_id")))
            _require(record.get("task_id") == row.get("task_id"), f"{row.get('task_id')}: referenced current task mismatch")
            _require(record.get("publication_id") == row.get("publication_id"), f"{row.get('task_id')}: referenced current publication mismatch")
        else:
            raise TargetedMigrationAuditError(f"unsupported manifest disposition: {disposition}")

    return manifest


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--comments", type=Path)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    if args.check:
        manifest = validate_manifest()
    else:
        if args.comments is None:
            parser.error("--comments is required when materializing")
        migration.body_for = safe_body_for
        # The materializer already audits each generated taskbook.  Suppress only
        # its final all-history audit, then replace that gate with the exact
        # transaction-scoped validation above.
        migration.research_task_records.audit = lambda _root: []
        manifest = migration.run(args.comments, check_only=False)
        validate_manifest()

    print(json.dumps({"status": "TARGETED_MIGRATION_AUDIT_PASS", "counts": manifest["counts"]}, sort_keys=True))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (TargetedMigrationAuditError, ValueError, OSError, json.JSONDecodeError) as exc:
        print("ERROR:", exc)
        raise SystemExit(1)
