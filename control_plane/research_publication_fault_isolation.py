#!/usr/bin/env python3
"""Task-local fault isolation for unresolved immutable publication forks.

An unresolved publication fork must remain fail-closed for the affected task, but
it must not turn one malformed/ambiguous task definition into a denial of service
for the entire canonical dispatch view.  This module provides a narrow overlay:

* the exact head set must be declared in ``research_task_publication_quarantines.json``;
* no operational publication is selected;
* no Working Truth, promotion, successor, or Foundation authority is granted;
* the quarantined task projects to BLOCKED in dispatch;
* every non-quarantined task keeps the existing strict publication semantics.

This is not a semantic resolution.  A real operational selection still goes
through the existing parallel-publication resolution + two-reference-pass
synthesis contract.
"""
from __future__ import annotations

import copy
import json
from collections import defaultdict
from pathlib import Path
from typing import Any, Callable

ROOT = Path(__file__).resolve().parents[1]
QUARANTINE_FILE = "research_task_publication_quarantines.json"
QUARANTINE_SCHEMA = "ENTERPRISE_MATH_TASK_PUBLICATION_FORK_QUARANTINE_V1"
QUARANTINE_STATE = "UNRESOLVED_PUBLICATION_FORK"


class PublicationFaultIsolationError(ValueError):
    pass


def _load(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise PublicationFaultIsolationError(f"{path}: JSON root must be object")
    return value


def quarantine_rows(root: Path = ROOT) -> dict[str, dict[str, Any]]:
    path = root / QUARANTINE_FILE
    if not path.exists():
        return {}
    payload = _load(path)
    if payload.get("schema") != QUARANTINE_SCHEMA:
        raise PublicationFaultIsolationError(f"{QUARANTINE_FILE}: wrong schema")
    if payload.get("status") != "ACTIVE":
        raise PublicationFaultIsolationError(f"{QUARANTINE_FILE}: status must be ACTIVE")
    rows = payload.get("quarantines")
    if not isinstance(rows, list):
        raise PublicationFaultIsolationError(f"{QUARANTINE_FILE}: quarantines must be list")
    out: dict[str, dict[str, Any]] = {}
    for index, row in enumerate(rows):
        if not isinstance(row, dict):
            raise PublicationFaultIsolationError(f"{QUARANTINE_FILE}: row {index} must be object")
        task_id = row.get("task_id")
        pubs = row.get("publication_ids")
        if not isinstance(task_id, str) or not task_id:
            raise PublicationFaultIsolationError(f"{QUARANTINE_FILE}: row {index} missing task_id")
        if task_id in out:
            raise PublicationFaultIsolationError(f"{QUARANTINE_FILE}: duplicate task {task_id}")
        if row.get("state") != QUARANTINE_STATE:
            raise PublicationFaultIsolationError(f"{QUARANTINE_FILE}: {task_id} wrong state")
        if (
            not isinstance(pubs, list)
            or len(pubs) < 2
            or any(not isinstance(item, str) or not item for item in pubs)
            or len(set(pubs)) != len(pubs)
        ):
            raise PublicationFaultIsolationError(f"{QUARANTINE_FILE}: {task_id} publication_ids invalid")
        if row.get("operational_publication_id") is not None:
            raise PublicationFaultIsolationError(
                f"{QUARANTINE_FILE}: {task_id} quarantine cannot select an operational publication"
            )
        if row.get("isolation_scope") != "CONTROL_PLANE_ONLY":
            raise PublicationFaultIsolationError(f"{QUARANTINE_FILE}: {task_id} wrong isolation_scope")
        for flag in (
            "working_truth_granted",
            "foundation_authority_granted",
            "canonical_promotion_granted",
            "successor_triggered",
        ):
            if row.get(flag) is not False:
                raise PublicationFaultIsolationError(
                    f"{QUARANTINE_FILE}: {task_id} cannot grant {flag}"
                )
        out[task_id] = row
    return out


def _heads(records: list[dict[str, Any]], terminal_states: set[str]) -> dict[str, list[dict[str, Any]]]:
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
            if item.get("supersedes_publication_id")
        }
        active = [
            item
            for item in values
            if item.get("publication_id") not in superseded
            and item.get("record_state", "ACTIVE") not in terminal_states
        ]
        if active:
            out[task_id] = active
    return out


def validated_quarantines(root: Path = ROOT) -> dict[str, dict[str, Any]]:
    from control_plane import research_task_records_impl as core

    rows = quarantine_rows(root)
    heads = _heads(core.iter_records(root), core.TERMINAL_RECORD_STATES)
    resolutions = core.publication_resolutions(root)
    for task_id, row in rows.items():
        if task_id in resolutions:
            raise PublicationFaultIsolationError(
                f"{task_id}: unresolved quarantine cannot coexist with operational resolution"
            )
        actual = {str(item.get("publication_id")) for item in heads.get(task_id, [])}
        declared = set(row["publication_ids"])
        if actual != declared:
            raise PublicationFaultIsolationError(
                f"{task_id}: quarantine head set drift; declared={sorted(declared)} actual={sorted(actual)}"
            )
    return rows


def isolated_current_records(root: Path = ROOT) -> dict[str, dict[str, Any]]:
    """Strict current-record reducer with exact quarantined forks omitted locally."""
    from control_plane import research_task_records_impl as core

    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for record in core.iter_records(root):
        task_id = record.get("task_id")
        if isinstance(task_id, str):
            grouped[task_id].append(record)
    resolutions = core.publication_resolutions(root)
    quarantines = validated_quarantines(root)
    unknown_resolutions = sorted(set(resolutions) - set(grouped))
    if unknown_resolutions:
        raise core.TaskRecordError(
            f"publication resolution references unknown task(s): {unknown_resolutions}"
        )
    unknown_quarantines = sorted(set(quarantines) - set(grouped))
    if unknown_quarantines:
        raise core.TaskRecordError(
            f"publication quarantine references unknown task(s): {unknown_quarantines}"
        )

    current: dict[str, dict[str, Any]] = {}
    for task_id, values in grouped.items():
        superseded = {
            item.get("supersedes_publication_id")
            for item in values
            if item.get("supersedes_publication_id")
        }
        heads = [
            item
            for item in values
            if item.get("publication_id") not in superseded
            and item.get("record_state", "ACTIVE") not in core.TERMINAL_RECORD_STATES
        ]
        resolution = resolutions.get(task_id)
        quarantine = quarantines.get(task_id)
        if len(heads) > 1:
            if quarantine is not None:
                # Exact-set validation already proved that every active head is
                # retained and none is selected.  This task is projected to
                # BLOCKED later; all other tasks remain reducible.
                continue
            if resolution is None:
                raise core.TaskRecordError(
                    f"publication fork for {task_id}: "
                    f"{[item.get('publication_id') for item in heads]}"
                )
            head_by_id = {str(item.get("publication_id")): item for item in heads}
            canonical = str(resolution["canonical_publication_id"])
            quarantined = set(resolution["quarantined_publication_ids"])
            if canonical not in head_by_id:
                raise core.TaskRecordError(
                    f"publication resolution for {task_id} selects non-head {canonical}"
                )
            unresolved = set(head_by_id) - {canonical} - quarantined
            missing_quarantine = quarantined - set(head_by_id)
            if unresolved:
                raise core.TaskRecordError(
                    f"publication resolution for {task_id} leaves unresolved heads: {sorted(unresolved)}"
                )
            if missing_quarantine:
                raise core.TaskRecordError(
                    f"publication resolution for {task_id} quarantines non-heads: {sorted(missing_quarantine)}"
                )
            current[task_id] = head_by_id[canonical]
            continue
        if heads:
            if quarantine is not None:
                raise core.TaskRecordError(
                    f"stale publication quarantine for {task_id}: fork no longer exists"
                )
            if resolution is not None and resolution.get("canonical_publication_id") != heads[0].get("publication_id"):
                raise core.TaskRecordError(
                    f"stale publication resolution for {task_id}: canonical head no longer matches"
                )
            current[task_id] = heads[0]
    return current


def blocked_definition(task_id: str, row: dict[str, Any], prior: dict[str, Any] | None = None) -> dict[str, Any]:
    value = copy.deepcopy(prior or {})
    value.update(
        {
            "task_id": task_id,
            "title": value.get("title", task_id),
            "kind": value.get("kind", "RESEARCH"),
            "owner": value.get("owner", "control-plane/publication-fork-quarantine"),
            "base_state": "BLOCKED",
            "priority": value.get("priority", "P2"),
            "leverage": value.get("leverage", "MEDIUM"),
            "frontier": "UNRESOLVED_PUBLICATION_FORK",
            "next_action": "RESOLVE_PUBLICATION_FORK_UNDER_EXISTING_PARALLEL_PUBLICATION_CONTRACT",
            "dependencies": copy.deepcopy(value.get("dependencies", [])),
            "source_refs": sorted(row["publication_ids"]),
            "evidence_status": "CONTROL_PLANE_QUARANTINED_UNRESOLVED_PUBLICATION_FORK",
            "last_progress_ref": QUARANTINE_FILE,
            "last_progress_at": value.get("last_progress_at", "1970-01-01T00:00:00+00:00"),
            "hard_block": {
                "code": "UNRESOLVED_PUBLICATION_FORK",
                "publication_ids": sorted(row["publication_ids"]),
                "operational_publication_id": None,
            },
            "tags": sorted(set(value.get("tags", [])) | {"CONTROL_PLANE_QUARANTINE"}),
            "claim_lease_minutes": int(value.get("claim_lease_minutes") or 120),
            "publication_id": None,
            "publication_ids": sorted(row["publication_ids"]),
            "registration_source": "PUBLICATION_FORK_QUARANTINE",
        }
    )
    return value


def install(root: Path = ROOT) -> None:
    """Install the narrow reducer overlay into already-established public modules."""
    from control_plane import research_task_records_impl as core
    from tools import research_task_records

    validated_quarantines(root)
    if not getattr(core, "_publication_fault_isolation_installed", False):
        core.current_records = isolated_current_records
        research_task_records.current_records = isolated_current_records
        core._publication_fault_isolation_installed = True

    from tools import research_dispatch
    if not getattr(research_dispatch, "_publication_fault_isolation_installed", False):
        original_merged: Callable[..., list[dict[str, Any]]] = research_dispatch.merged_definitions

        def merged_definitions(local_root: Path = research_dispatch.ROOT) -> list[dict[str, Any]]:
            values = original_merged(local_root)
            by_id = {
                item["task_id"]: item
                for item in values
                if isinstance(item, dict) and isinstance(item.get("task_id"), str)
            }
            for task_id, row in validated_quarantines(local_root).items():
                by_id[task_id] = blocked_definition(task_id, row, by_id.get(task_id))
            return [by_id[key] for key in sorted(by_id)]

        research_dispatch.merged_definitions = merged_definitions
        research_dispatch._publication_fault_isolation_installed = True


def audit(root: Path = ROOT) -> list[str]:
    """Validate the overlay and prove that quarantined tasks are locally BLOCKED."""
    errors: list[str] = []
    try:
        rows = validated_quarantines(root)
        install(root)
        from tools import research_dispatch, research_task_records
        task_errors = research_task_records.audit(root)
        errors.extend(task_errors)
        definitions = {item["task_id"]: item for item in research_dispatch.merged_definitions(root)}
        for task_id, row in rows.items():
            item = definitions.get(task_id)
            if item is None:
                errors.append(f"{task_id}: quarantine missing from dispatch view")
                continue
            if item.get("base_state") != "BLOCKED":
                errors.append(f"{task_id}: quarantine is not BLOCKED in dispatch view")
            if item.get("publication_id") is not None:
                errors.append(f"{task_id}: quarantine unexpectedly selected publication_id")
            if set(item.get("publication_ids", [])) != set(row["publication_ids"]):
                errors.append(f"{task_id}: dispatch quarantine head set mismatch")
    except Exception as exc:
        errors.append(str(exc))
    return errors


def main() -> int:
    errors = audit()
    if errors:
        for error in errors:
            print("ERROR:", error)
        return 1
    print(f"PASS: publication-fork fault isolation valid ({len(quarantine_rows())} quarantined task(s)).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
