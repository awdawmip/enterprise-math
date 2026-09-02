#!/usr/bin/env python3
"""Exact task-local isolation for schema-valid semantic-preservation faults.

This layer is deliberately separate from strict task-record audit quarantine.
A publication may satisfy the V2 JSON/taskbook envelope while still replacing
source-backed identity, lineage, parentage, successor-gate, or source provenance
with migration-wrapper metadata.  Such a publication is removed from operational
selection until ordinary publication authority creates a verified superseding
generation.

The registry pins the bad publication, both taskbook byte sequences, and exact
source/observed semantic projections.  This module grants no replacement
publication, Driver review, mathematical truth, Working Truth, Foundation status,
canonical promotion, or successor authority.
"""
from __future__ import annotations

import copy
import json
from collections import defaultdict
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
QUARANTINE_FILE = "research_task_semantic_integrity_quarantines.json"
QUARANTINE_SCHEMA = "ENTERPRISE_MATH_TASK_SEMANTIC_INTEGRITY_QUARANTINE_V1"
FAULT_CLASS = "LEGACY_MIGRATION_SEMANTIC_PRESERVATION_DRIFT"
OPEN_REPAIR_STATE = "AWAITING_AUTHORIZED_SUPERSEDING_PUBLICATION"
RESOLVED_REPAIR_STATE = "RESOLVED_BY_SUPERSEDING_PUBLICATION"
ISOLATION_SCOPE = "CONTROL_PLANE_ONLY"
SUCCESSOR_GATE_FIELDS = {
    "new_information_gap",
    "why_parent_result_does_not_close_it",
    "discriminating_outcomes",
    "kill_condition",
    "alternative_route_or_free_exploration_considered",
    "why_new_stage_or_task_is_better_than_same_task_or_closure",
}


class TaskSemanticIntegrityIsolationError(ValueError):
    pass


def _load(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise TaskSemanticIntegrityIsolationError(f"{path}: JSON root must be object")
    return value


def _require_text(row: dict[str, Any], field: str, prefix: str) -> str:
    value = row.get(field)
    if not isinstance(value, str) or not value:
        raise TaskSemanticIntegrityIsolationError(f"{prefix}: missing {field}")
    return value


def quarantine_rows(root: Path = ROOT) -> dict[str, dict[str, Any]]:
    path = root / QUARANTINE_FILE
    if not path.exists():
        raise TaskSemanticIntegrityIsolationError(f"{QUARANTINE_FILE}: missing")
    payload = _load(path)
    if payload.get("schema") != QUARANTINE_SCHEMA:
        raise TaskSemanticIntegrityIsolationError(f"{QUARANTINE_FILE}: wrong schema")
    if payload.get("status") != "ACTIVE":
        raise TaskSemanticIntegrityIsolationError(f"{QUARANTINE_FILE}: status must be ACTIVE")
    rows = payload.get("quarantines")
    if not isinstance(rows, list) or not rows:
        raise TaskSemanticIntegrityIsolationError(
            f"{QUARANTINE_FILE}: quarantines must be a nonempty list"
        )

    out: dict[str, dict[str, Any]] = {}
    seen_publications: set[str] = set()
    for index, row in enumerate(rows):
        if not isinstance(row, dict):
            raise TaskSemanticIntegrityIsolationError(
                f"{QUARANTINE_FILE}: row {index} must be object"
            )
        task_id = _require_text(row, "task_id", f"row {index}")
        publication_id = _require_text(row, "publication_id", task_id)
        if task_id in out:
            raise TaskSemanticIntegrityIsolationError(
                f"{QUARANTINE_FILE}: duplicate task {task_id}"
            )
        if publication_id in seen_publications:
            raise TaskSemanticIntegrityIsolationError(
                f"{QUARANTINE_FILE}: duplicate publication {publication_id}"
            )
        for field in (
            "record_path",
            "record_blob_sha1",
            "taskbook_path",
            "taskbook_blob_sha1",
            "source_taskbook_path",
            "source_taskbook_blob_sha1",
            "migration_provenance_field",
            "migration_archive_branch",
            "migration_source_commit",
            "reason",
        ):
            _require_text(row, field, task_id)
        if row.get("fault_class") != FAULT_CLASS:
            raise TaskSemanticIntegrityIsolationError(f"{task_id}: wrong fault_class")
        if row.get("isolation_scope") != ISOLATION_SCOPE:
            raise TaskSemanticIntegrityIsolationError(f"{task_id}: wrong isolation_scope")

        fields = row.get("semantic_fields")
        expected = row.get("expected_semantics")
        observed = row.get("observed_semantics")
        if (
            not isinstance(fields, list)
            or not fields
            or any(not isinstance(item, str) or not item for item in fields)
            or len(set(fields)) != len(fields)
        ):
            raise TaskSemanticIntegrityIsolationError(f"{task_id}: semantic_fields invalid")
        if not isinstance(expected, dict) or set(expected) != set(fields):
            raise TaskSemanticIntegrityIsolationError(
                f"{task_id}: expected_semantics must exactly cover semantic_fields"
            )
        if not isinstance(observed, dict) or set(observed) != set(fields):
            raise TaskSemanticIntegrityIsolationError(
                f"{task_id}: observed_semantics must exactly cover semantic_fields"
            )
        if expected == observed:
            raise TaskSemanticIntegrityIsolationError(
                f"{task_id}: quarantine does not describe a semantic difference"
            )
        if expected.get("task_lineage") == "CONTINUATION":
            if not isinstance(expected.get("parent_task_id"), str) or not expected["parent_task_id"]:
                raise TaskSemanticIntegrityIsolationError(
                    f"{task_id}: CONTINUATION requires expected parent_task_id"
                )
            gate = expected.get("successor_gate")
            if not isinstance(gate, dict) or set(gate) != SUCCESSOR_GATE_FIELDS:
                raise TaskSemanticIntegrityIsolationError(
                    f"{task_id}: expected continuation successor_gate is incomplete"
                )
            if any(value in (None, "", []) for value in gate.values()):
                raise TaskSemanticIntegrityIsolationError(
                    f"{task_id}: expected continuation successor_gate contains empty payload"
                )

        missing_refs = row.get("required_missing_source_refs")
        if (
            not isinstance(missing_refs, list)
            or not missing_refs
            or any(not isinstance(item, str) or not item for item in missing_refs)
            or len(set(missing_refs)) != len(missing_refs)
        ):
            raise TaskSemanticIntegrityIsolationError(
                f"{task_id}: required_missing_source_refs invalid"
            )

        repair_state = row.get("repair_state")
        operational = row.get("operational_publication_id")
        if repair_state == OPEN_REPAIR_STATE:
            if operational is not None:
                raise TaskSemanticIntegrityIsolationError(
                    f"{task_id}: open quarantine cannot select an operational publication"
                )
        elif repair_state == RESOLVED_REPAIR_STATE:
            if not isinstance(operational, str) or not operational or operational == publication_id:
                raise TaskSemanticIntegrityIsolationError(
                    f"{task_id}: resolved quarantine requires a distinct operational publication"
                )
        else:
            raise TaskSemanticIntegrityIsolationError(
                f"{task_id}: unsupported repair_state {repair_state!r}"
            )

        for flag in (
            "working_truth_granted",
            "foundation_authority_granted",
            "canonical_promotion_granted",
            "successor_triggered",
            "review_disposition_granted",
            "replacement_publication_granted",
        ):
            if row.get(flag) is not False:
                raise TaskSemanticIntegrityIsolationError(
                    f"{task_id}: quarantine cannot grant {flag}"
                )
        out[task_id] = row
        seen_publications.add(publication_id)
    return out


def _active_heads(
    records: list[dict[str, Any]], terminal_states: set[str]
) -> dict[str, list[dict[str, Any]]]:
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


def _taskbook_meta(path: Path) -> dict[str, Any]:
    from tools import research_taskbook

    meta, _ = research_taskbook.split_taskbook(path.read_text(encoding="utf-8"))
    if not isinstance(meta, dict):
        raise TaskSemanticIntegrityIsolationError(f"{path}: taskbook metadata must be object")
    return meta


def _projection(meta: dict[str, Any], fields: list[str]) -> dict[str, Any]:
    return {field: copy.deepcopy(meta.get(field)) for field in fields}


def _verify_migration_provenance(
    task_id: str, row: dict[str, Any], meta: dict[str, Any], record: dict[str, Any]
) -> None:
    field = row["migration_provenance_field"]
    meta_source = meta.get(field)
    record_source = record.get(field)
    if not isinstance(meta_source, dict):
        raise TaskSemanticIntegrityIsolationError(
            f"{task_id}: taskbook migration provenance is not separate object {field!r}"
        )
    if not isinstance(record_source, dict):
        raise TaskSemanticIntegrityIsolationError(
            f"{task_id}: publication migration provenance is not separate object {field!r}"
        )
    for source in (meta_source, record_source):
        if source.get("archive_branch") != row["migration_archive_branch"]:
            raise TaskSemanticIntegrityIsolationError(
                f"{task_id}: migration archive branch drift"
            )
        if source.get("source_commit") != row["migration_source_commit"]:
            raise TaskSemanticIntegrityIsolationError(
                f"{task_id}: migration source commit drift"
            )


def validated_quarantines(root: Path = ROOT) -> dict[str, dict[str, Any]]:
    """Validate source/current bytes, semantic projections, and repair state."""
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
        if record is None or record.get("task_id") != task_id:
            raise TaskSemanticIntegrityIsolationError(
                f"{task_id}: unknown or foreign quarantined publication {publication_id}"
            )
        if record.get("_record_path") != row["record_path"]:
            raise TaskSemanticIntegrityIsolationError(f"{task_id}: record_path drift")
        record_path = root / row["record_path"]
        taskbook_path = root / row["taskbook_path"]
        source_path = root / row["source_taskbook_path"]
        for path, field in (
            (record_path, "record_path"),
            (taskbook_path, "taskbook_path"),
            (source_path, "source_taskbook_path"),
        ):
            if not path.exists():
                raise TaskSemanticIntegrityIsolationError(f"{task_id}: {field} missing")
        actual_record_blob = core.git_blob_sha1_bytes(record_path.read_bytes())
        actual_taskbook_blob = core.git_blob_sha1_bytes(taskbook_path.read_bytes())
        actual_source_blob = core.git_blob_sha1_bytes(source_path.read_bytes())
        if actual_record_blob != row["record_blob_sha1"]:
            raise TaskSemanticIntegrityIsolationError(f"{task_id}: record blob drift")
        if actual_taskbook_blob != row["taskbook_blob_sha1"]:
            raise TaskSemanticIntegrityIsolationError(f"{task_id}: taskbook blob drift")
        if actual_source_blob != row["source_taskbook_blob_sha1"]:
            raise TaskSemanticIntegrityIsolationError(f"{task_id}: source taskbook blob drift")
        if record.get("taskbook_path") != row["taskbook_path"]:
            raise TaskSemanticIntegrityIsolationError(f"{task_id}: record taskbook_path drift")

        source_meta = _taskbook_meta(source_path)
        observed_meta = _taskbook_meta(taskbook_path)
        if source_meta.get("task_id") != task_id or observed_meta.get("task_id") != task_id:
            raise TaskSemanticIntegrityIsolationError(f"{task_id}: taskbook task_id mismatch")
        fields = list(row["semantic_fields"])
        if _projection(source_meta, fields) != row["expected_semantics"]:
            raise TaskSemanticIntegrityIsolationError(
                f"{task_id}: source semantic projection drifted from pinned expectation"
            )
        if _projection(observed_meta, fields) != row["observed_semantics"]:
            raise TaskSemanticIntegrityIsolationError(
                f"{task_id}: migrated semantic projection drifted from pinned observation"
            )
        source_refs = set(source_meta.get("source_refs") or [])
        observed_refs = set(observed_meta.get("source_refs") or [])
        for ref in row["required_missing_source_refs"]:
            if ref not in source_refs or ref in observed_refs:
                raise TaskSemanticIntegrityIsolationError(
                    f"{task_id}: pinned missing source-ref witness no longer matches"
                )
        _verify_migration_provenance(task_id, row, observed_meta, record)

        active_ids = {
            str(item.get("publication_id"))
            for item in heads.get(task_id, [])
            if item.get("publication_id")
        }
        if row["repair_state"] == OPEN_REPAIR_STATE:
            if active_ids != {publication_id}:
                raise TaskSemanticIntegrityIsolationError(
                    f"{task_id}: open semantic quarantine requires exactly the pinned bad head; "
                    f"actual={sorted(active_ids)!r}"
                )
            continue

        operational_id = row["operational_publication_id"]
        if active_ids != {operational_id}:
            raise TaskSemanticIntegrityIsolationError(
                f"{task_id}: resolved semantic quarantine operational head mismatch; "
                f"expected={[operational_id]!r} actual={sorted(active_ids)!r}"
            )
        successor = by_publication.get(str(operational_id))
        if successor is None or successor.get("supersedes_publication_id") != publication_id:
            raise TaskSemanticIntegrityIsolationError(
                f"{task_id}: resolved repair must directly supersede the pinned bad publication"
            )
        successor_path_value = successor.get("taskbook_path")
        if not isinstance(successor_path_value, str):
            raise TaskSemanticIntegrityIsolationError(f"{task_id}: repaired taskbook path missing")
        successor_path = root / successor_path_value
        if not successor_path.exists():
            raise TaskSemanticIntegrityIsolationError(f"{task_id}: repaired taskbook missing")
        successor_meta = _taskbook_meta(successor_path)
        if _projection(successor_meta, fields) != row["expected_semantics"]:
            raise TaskSemanticIntegrityIsolationError(
                f"{task_id}: repaired generation does not restore source semantics"
            )
        _verify_migration_provenance(task_id, row, successor_meta, successor)
        for field in fields:
            if successor.get(field) != row["expected_semantics"][field]:
                raise TaskSemanticIntegrityIsolationError(
                    f"{task_id}: repaired publication record does not carry restored {field}"
                )
    return rows


def open_quarantines(root: Path = ROOT) -> dict[str, dict[str, Any]]:
    return {
        task_id: row
        for task_id, row in validated_quarantines(root).items()
        if row["repair_state"] == OPEN_REPAIR_STATE
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
            "owner": value.get("owner", "control-plane/task-semantic-integrity-quarantine"),
            "base_state": "BLOCKED",
            "priority": value.get("priority", "P2"),
            "leverage": value.get("leverage", "MEDIUM"),
            "frontier": "INVALID_CURRENT_TASK_SEMANTIC_PRESERVATION",
            "next_action": (
                "DRIVER_REVIEW_NEGATIVE_BOUNDARY_AND_PUBLISH_SEMANTICALLY_"
                "PRESERVING_SUPERSEDING_GENERATION"
            ),
            "dependencies": copy.deepcopy(value.get("dependencies", [])),
            "source_refs": sorted(
                set(value.get("source_refs", []))
                | {
                    row["record_path"],
                    row["taskbook_path"],
                    row["source_taskbook_path"],
                    row["publication_id"],
                }
            ),
            "evidence_status": "CONTROL_PLANE_QUARANTINED_SEMANTIC_PRESERVATION_DRIFT",
            "last_progress_ref": QUARANTINE_FILE,
            "last_progress_at": value.get("last_progress_at", "1970-01-01T00:00:00+00:00"),
            "hard_block": {
                "code": "INVALID_CURRENT_TASK_SEMANTIC_PRESERVATION",
                "publication_id": row["publication_id"],
                "record_path": row["record_path"],
                "record_blob_sha1": row["record_blob_sha1"],
                "taskbook_path": row["taskbook_path"],
                "taskbook_blob_sha1": row["taskbook_blob_sha1"],
                "source_taskbook_path": row["source_taskbook_path"],
                "source_taskbook_blob_sha1": row["source_taskbook_blob_sha1"],
                "operational_publication_id": None,
            },
            "tags": sorted(
                set(value.get("tags", [])) | {"CONTROL_PLANE_SEMANTIC_INTEGRITY_QUARANTINE"}
            ),
            "claim_lease_minutes": int(value.get("claim_lease_minutes") or 120),
            "publication_id": None,
            "publication_ids": [row["publication_id"]],
            "registration_source": "TASK_SEMANTIC_INTEGRITY_QUARANTINE",
        }
    )
    return value


def install(root: Path = ROOT) -> None:
    """Remove open semantic-fault heads from operational publication/dispatch views."""
    rows = open_quarantines(root)
    from control_plane import research_task_records_impl as core
    from tools import research_dispatch, research_task_records

    if not getattr(core, "_task_semantic_integrity_fault_isolation_installed", False):
        base_current = research_task_records.current_records

        def current_records(local_root: Path = root) -> dict[str, dict[str, Any]]:
            current = dict(base_current(local_root))
            for task_id in open_quarantines(local_root):
                current.pop(task_id, None)
            return current

        core.current_records = current_records
        research_task_records.current_records = current_records
        core._task_semantic_integrity_fault_isolation_installed = True

    if not getattr(research_dispatch, "_task_semantic_integrity_fault_isolation_installed", False):
        base_merged = research_dispatch.merged_definitions

        def merged_definitions(
            local_root: Path = research_dispatch.ROOT,
        ) -> list[dict[str, Any]]:
            values = base_merged(local_root)
            by_id = {
                item["task_id"]: item
                for item in values
                if isinstance(item, dict) and isinstance(item.get("task_id"), str)
            }
            for task_id, row in open_quarantines(local_root).items():
                by_id[task_id] = blocked_definition(task_id, row, by_id.get(task_id))
            return [by_id[key] for key in sorted(by_id)]

        research_dispatch.merged_definitions = merged_definitions
        research_dispatch._task_semantic_integrity_fault_isolation_installed = True

    if set(rows) != set(open_quarantines(root)):
        raise TaskSemanticIntegrityIsolationError(
            "task semantic-integrity quarantine changed during install"
        )


def audit_runtime_projection(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    try:
        install(root)
        from tools import research_dispatch, research_task_records

        rows = validated_quarantines(root)
        open_rows = {
            task_id: row
            for task_id, row in rows.items()
            if row["repair_state"] == OPEN_REPAIR_STATE
        }
        current = research_task_records.current_records(root)
        definitions = {
            item["task_id"]: item for item in research_dispatch.merged_definitions(root)
        }
        for task_id, row in open_rows.items():
            if task_id in current:
                errors.append(f"{task_id}: semantic-quarantined task remains current")
            item = definitions.get(task_id)
            if item is None:
                errors.append(f"{task_id}: semantic quarantine missing from dispatch view")
                continue
            if item.get("base_state") != "BLOCKED":
                errors.append(f"{task_id}: semantic quarantine is not BLOCKED")
            if item.get("publication_id") is not None:
                errors.append(f"{task_id}: semantic quarantine selected a publication")
            if item.get("registration_source") != "TASK_SEMANTIC_INTEGRITY_QUARANTINE":
                errors.append(f"{task_id}: semantic quarantine registration source drifted")
            if item.get("hard_block", {}).get("publication_id") != row["publication_id"]:
                errors.append(f"{task_id}: semantic quarantine publication pin drifted")
        for task_id, row in rows.items():
            if row["repair_state"] != RESOLVED_REPAIR_STATE:
                continue
            current_item = current.get(task_id)
            if current_item is None or current_item.get("publication_id") != row["operational_publication_id"]:
                errors.append(f"{task_id}: resolved semantic repair is not operational")
    except Exception as exc:
        errors.append(str(exc))
    return errors


def audit(root: Path = ROOT) -> list[str]:
    return audit_runtime_projection(root)


def main() -> int:
    errors = audit()
    if errors:
        for error in errors:
            print("ERROR:", error)
        return 1
    rows = validated_quarantines()
    open_count = sum(row["repair_state"] == OPEN_REPAIR_STATE for row in rows.values())
    resolved_count = sum(row["repair_state"] == RESOLVED_REPAIR_STATE for row in rows.values())
    print(
        "PASS: exact task semantic-integrity quarantine valid "
        f"({open_count} blocked, {resolved_count} resolved)."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
