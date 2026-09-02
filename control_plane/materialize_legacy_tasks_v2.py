#!/usr/bin/env python3
"""Materialize every legacy task into immutable V2 task records.

This one-shot cutover preserves task identity, frontier, owner, ordering metadata,
and the highest authenticated Issue #240 runtime state. It does not create a new
mathematical claim, reopen terminal work, promote truth, or mint a replacement
execution claim.
"""
from __future__ import annotations

import argparse
import copy
import json
import os
import re
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from control_plane import research_task_records_impl as records_impl
from tools import research_dispatch, research_scheduler, research_task_records, research_taskbook

SOURCE_COMMIT = "ce629e24e5af59128e25af87075c6622413684e0"
ARCHIVE_BRANCH = "archive/legacy-control-plane-pre-v2-20260902"
MIGRATION_EFFECTIVE = "2026-09-02T00:00:00+00:00"
PUBLISHER_ROLE = "RESEARCH_DRIVER"
PUBLISHER_ID = "EM-DVR-CUTOVER"
TASKBOOK_PREFIX = "LEGACY_CONTROL_MIGRATION_"
MANIFEST_PATH = ROOT / "control_plane" / "legacy_control_migration_manifest.json"
TERMINAL_STATES = {"DONE", "SUPERSEDED"}


class MigrationError(ValueError):
    pass


def load(path: Path, default: Any = None) -> Any:
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def flatten_comments(value: Any) -> list[dict[str, Any]]:
    if isinstance(value, list) and value and all(isinstance(page, list) for page in value):
        value = [item for page in value for item in page]
    return [item for item in value if isinstance(item, dict)] if isinstance(value, list) else []


def task_map(payload: Any) -> dict[str, dict[str, Any]]:
    out: dict[str, dict[str, Any]] = {}
    if not isinstance(payload, dict):
        return out
    for row in payload.get("tasks", []):
        if isinstance(row, dict) and isinstance(row.get("task_id"), str):
            if row["task_id"] in out:
                raise MigrationError(f"duplicate legacy task: {row['task_id']}")
            out[row["task_id"]] = copy.deepcopy(row)
    return out


def reduce_scheduler_tasks(
    scheduler_payload: dict[str, Any], comments: list[dict[str, Any]]
) -> dict[str, dict[str, Any]]:
    events = research_dispatch.events_from_github_comments(comments, root=ROOT)
    now = datetime.now(timezone.utc)
    default_lease = int(scheduler_payload.get("claim_lease_minutes", 120))
    out: dict[str, dict[str, Any]] = {}
    for task in scheduler_payload.get("tasks", []):
        if not isinstance(task, dict) or not isinstance(task.get("task_id"), str):
            continue
        state = research_scheduler.reduce_task(
            task,
            events,
            default_lease_minutes=int(task.get("claim_lease_minutes") or default_lease),
            now=now,
        )
        if state.get("claim_id"):
            raise MigrationError(
                f"{task['task_id']}: live legacy claim exists; cutover must preserve it explicitly"
            )
        out[task["task_id"]] = state
    return out


def safe_name(task_id: str) -> str:
    return TASKBOOK_PREFIX + re.sub(r"[^A-Z0-9]+", "_", task_id.upper()).strip("_") + "_20260902.md"


def lane(task_id: str) -> str:
    text = task_id[3:] if task_id.startswith("RS-") else task_id
    first = text.split("-", 1)[0]
    value = re.sub(r"[^A-Z0-9]+", "", first.upper())
    return (value or "MIGRATION")[:16]


def body_for(task: dict[str, Any], state: dict[str, Any], disposition: str) -> str:
    task_id = task["task_id"]
    title = task.get("title") or task_id
    frontier = str(task.get("frontier") or "The exact legacy frontier is preserved in metadata.")
    source_refs = task.get("source_refs") if isinstance(task.get("source_refs"), list) else []
    source_text = ", ".join(str(item) for item in source_refs) or "the exact archived legacy definition"
    if disposition == "TERMINAL_HISTORY":
        target = (
            "Preserve the terminal control outcome without making the task claimable or "
            "authorizing a fresh execution."
        )
        success = (
            "Success is an immutable nonclaimable V2 history record whose task identity and "
            "terminal state match the authenticated durable outcome. Any attempt to redispatch "
            "this generation is a cutover failure."
        )
    elif disposition == "BACKLOG":
        target = (
            "Preserve the dormant frontier as an immutable, nonclaimable V2 backlog generation. "
            "Activation requires a later explicit superseding publication."
        )
        success = (
            "Success is a nonclaimable ACTIVE V2 record with base state BACKLOG. It must not "
            "appear in fresh task selection until a later authority publishes a new generation."
        )
    else:
        target = (
            "Preserve the exact durable handoff or ready frontier as a claimable V2 generation, "
            "without changing its mathematical scope or creating an execution claim."
        )
        success = (
            "Success is one claimable V2 task record with the same task identity, owner, frontier, "
            "priority class and durable next action. Failure includes scope widening, loss of the "
            "handoff, or creation of a synthetic owner claim."
        )
    return f"""# {title} — V2 Control Migration

Status: `PUBLISHED_REGISTERED / CONTROL_MIGRATION / {state.get('state')}`

## Mother question

Can `{task_id}` be transferred from the archived control definition into the immutable V2 task surface while preserving its exact durable research or governance frontier and without changing mathematical meaning?

## Frozen inputs and scope

The source is the exact archived snapshot `{ARCHIVE_BRANCH}` at `{SOURCE_COMMIT}`. The preserved frontier is:

{frontier}

The preserved source references are: {source_text}.

This taskbook is a control migration envelope. It adds no theorem, counterexample, novelty claim, priority promotion, Working Truth, Foundation status, or execution ownership.

## Hard target and required outputs

{target}

The authoritative next action is stored in the task metadata so it remains byte-exact and is not restated as generic repository policy in this body.

## Research value to preserve

The task identity, owner-local boundary, source lineage, accumulated evidence, durable frontier and next executable action remain valuable even when the task is terminal or not currently selected. The migration preserves those objects without replaying completed work.

## Success, kill, and return criteria

{success}

Return the immutable V2 publication record and the migration-manifest row. Stop this migration subflow after repository integrity checks pass; task execution, review and mathematical promotion remain separate control actions.
"""


def record_state(runtime_state: str) -> tuple[str, bool, str]:
    if runtime_state == "SUPERSEDED":
        return "SUPERSEDED", False, "TERMINAL_HISTORY"
    if runtime_state == "DONE":
        return "CLOSED", False, "TERMINAL_HISTORY"
    if runtime_state == "BACKLOG":
        return "ACTIVE", False, "BACKLOG"
    return "ACTIVE", True, "ACTIVE_FRONTIER"


def record_map() -> dict[str, list[dict[str, Any]]]:
    out: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in research_task_records.iter_records(ROOT):
        task_id = row.get("task_id")
        if isinstance(task_id, str):
            out[task_id].append(row)
    return out


def exact_write(path: Path, content: str) -> None:
    if path.exists():
        if path.read_text(encoding="utf-8") != content:
            raise MigrationError(f"idempotency drift at {path.relative_to(ROOT)}")
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def exact_write_json(path: Path, payload: dict[str, Any]) -> None:
    exact_write(path, json.dumps(payload, ensure_ascii=False, indent=2) + "\n")


def build_taskbook(
    task: dict[str, Any], state: dict[str, Any], disposition: str
) -> tuple[Path, dict[str, Any]]:
    task_id = task["task_id"]
    runtime_state = str(state.get("state") or task.get("base_state") or "BACKLOG")
    base_state = runtime_state if runtime_state in {
        "BACKLOG", "READY", "HANDOFF_READY", "BLOCKED", "DONE", "SUPERSEDED"
    } else "HANDOFF_READY"
    meta = {
        "task_id": task_id,
        "title": task.get("title") or task_id,
        "kind": task.get("kind", "RESEARCH"),
        "owner": task.get("owner", "taskbook/unassigned"),
        "base_state": base_state,
        "priority": task.get("priority", "P2"),
        "leverage": task.get("leverage", "MEDIUM"),
        "frontier": task.get("frontier") or "Legacy frontier preserved by exact migration.",
        "next_action": state.get("next_action") or task.get("next_action") or "No executable action recorded.",
        "dependencies": copy.deepcopy(task.get("dependencies", [])),
        "source_refs": copy.deepcopy(task.get("source_refs", [])),
        "evidence_status": f"LEGACY_CONTROL_MIGRATED_{runtime_state}",
        "last_progress_ref": state.get("last_progress_ref") or task.get("last_progress_ref"),
        "last_progress_at": state.get("last_progress_at") or task.get("last_progress_at") or MIGRATION_EFFECTIVE,
        "hard_block": copy.deepcopy(state.get("hard_block") or task.get("hard_block")),
        "tags": sorted(set([*(task.get("tags") or []), "legacy-control-migration", "v2-cutover"])),
        "claim_lease_minutes": int(task.get("claim_lease_minutes") or 120),
        "created_by_role": PUBLISHER_ROLE,
        "task_authority": "PUBLISHED_REGISTERED",
        "publication_contract": records_impl.TASKBOOK_PUBLICATION_CONTRACT,
        "publication_template": records_impl.TASKBOOK_TEMPLATE,
        "registry_key": task_id,
        "parent_objective_id": "LEGACY_CONTROL_CUTOVER_" + re.sub(r"[^A-Z0-9]+", "_", task_id.upper()).strip("_"),
        "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
        "final_response_identity_policy": "INHERIT_GLOBAL",
        "identity_lane": lane(task_id),
        "origin_kind": "MAINTENANCE",
        "task_lineage": "MAINTENANCE",
        "parent_task_id": None,
        "successor_gate": None,
        "policy_review": {
            "policy_set": "research_taskbook_policy.json",
            "policy_digest": research_taskbook.policy_digest(ROOT),
            "review_state": "PASS",
            "temporary_overrides": [],
        },
        "migration_source": {
            "archive_branch": ARCHIVE_BRANCH,
            "source_commit": SOURCE_COMMIT,
            "legacy_runtime_state": runtime_state,
            "legacy_dispatch_state": state.get("dispatch_state"),
            "legacy_claim_id": state.get("claim_id"),
        },
    }
    path = ROOT / "research_tasks" / safe_name(task_id)
    text = research_taskbook.render_taskbook(meta, body_for(task, state, disposition))
    exact_write(path, text)
    findings = research_taskbook.audit_taskbook(path, root=ROOT, dispatch=True)
    errors = [item for item in findings if item.get("severity") == "ERROR"]
    if errors:
        raise MigrationError(
            f"{path.relative_to(ROOT)}: taskbook audit failed: "
            + "; ".join(f"{item['code']}:{item['message']}" for item in errors)
        )
    return path, meta


def build_record(
    task: dict[str, Any], state: dict[str, Any], existing: list[dict[str, Any]]
) -> tuple[dict[str, Any], Path, str]:
    runtime_state = str(state.get("state") or task.get("base_state") or "BACKLOG")
    rec_state, claimable, disposition = record_state(runtime_state)
    taskbook_path, meta = build_taskbook(task, state, disposition)
    blob = records_impl.taskbook_blob(taskbook_path)
    parent = meta["parent_objective_id"]
    publication_id = records_impl.publication_id(task["task_id"], blob, PUBLISHER_ID, parent)
    prior_ids = [str(row.get("publication_id")) for row in existing if row.get("publication_id")]
    generation = max([int(row.get("publication_generation", 1)) for row in existing] or [0]) + 1
    supersedes = prior_ids[-1] if prior_ids else None
    record = {
        "record_schema": records_impl.RECORD_SCHEMA,
        "record_state": rec_state,
        "task_id": task["task_id"],
        "registry_key": task["task_id"],
        "publication_id": publication_id,
        "publication_generation": generation,
        "supersedes_publication_id": supersedes,
        "publication_contract": records_impl.TASKBOOK_PUBLICATION_CONTRACT,
        "template_version": records_impl.TASKBOOK_TEMPLATE,
        "publication_transaction": records_impl.PUBLICATION_TRANSACTION_V2,
        "taskbook_path": taskbook_path.relative_to(ROOT).as_posix(),
        "taskbook_blob_sha1": blob,
        "publisher_role": PUBLISHER_ROLE,
        "publisher_id": PUBLISHER_ID,
        "published_at": MIGRATION_EFFECTIVE,
        "parent_objective_id": parent,
        "origin_kind": "MAINTENANCE",
        "origin_candidate_id": None,
        "origin_candidate_state": None,
        "kind": task.get("kind", "RESEARCH"),
        "task_lineage": "MAINTENANCE",
        "parent_task_id": None,
        "claimable": claimable,
        "effective_priority": task.get("priority", "P2"),
        "effective_leverage": task.get("leverage", "MEDIUM"),
        "priority_source": "LEGACY_CONTROL_EXACT_PRESERVATION",
        "publisher_priority_request": task.get("priority"),
        "publisher_leverage_request": task.get("leverage"),
        "owner": task.get("owner"),
        "frontier": task.get("frontier"),
        "next_action": state.get("next_action") or task.get("next_action"),
        "research_value": task.get("frontier") or "Preserve exact legacy task value and durable frontier.",
        "terminal_scope": "TASK",
        "working_truth_granted": False,
        "canonical_promotion_granted": False,
        "migration_source": {
            "schema": "ENTERPRISE_MATH_LEGACY_TASK_CUTOVER_SOURCE_V1",
            "archive_branch": ARCHIVE_BRANCH,
            "source_commit": SOURCE_COMMIT,
            "source_definition": "research_scheduler.json" if task.get("_from_scheduler") else "research_task_registry.json",
            "legacy_runtime_state": runtime_state,
            "legacy_dispatch_state": state.get("dispatch_state"),
            "legacy_claim_id": state.get("claim_id"),
            "legacy_lease_until": state.get("lease_until"),
            "legacy_last_progress_ref": state.get("last_progress_ref"),
            "legacy_last_progress_at": state.get("last_progress_at"),
            "migration_disposition": disposition,
            "no_execution_claim_created": True,
        },
    }
    out = records_impl.record_path(ROOT, task["task_id"], publication_id)
    exact_write_json(out, record)
    return record, out, disposition


def run(comments_path: Path, *, check_only: bool) -> dict[str, Any]:
    scheduler_payload = load(ROOT / "research_scheduler.json", {})
    registry_payload = load(ROOT / "research_task_registry.json", {})
    scheduler = task_map(scheduler_payload)
    registry = task_map(registry_payload)
    comments = flatten_comments(load(comments_path, []))
    runtime = reduce_scheduler_tasks(scheduler_payload, comments)
    all_existing = record_map()
    current = research_task_records.current_records(ROOT)

    union = sorted(set(scheduler) | set(registry))
    rows: list[dict[str, Any]] = []
    for task_id in union:
        old = copy.deepcopy(scheduler.get(task_id) or registry[task_id])
        old["_from_scheduler"] = task_id in scheduler
        if task_id in current:
            rows.append(
                {
                    "task_id": task_id,
                    "disposition": "ALREADY_CURRENT_V2",
                    "publication_id": current[task_id].get("publication_id"),
                    "record_path": current[task_id].get("_record_path"),
                }
            )
            continue
        state = copy.deepcopy(runtime.get(task_id) or {
            "state": old.get("base_state", "BACKLOG"),
            "dispatch_state": "DORMANT",
            "claim_id": None,
            "lease_until": None,
            "last_progress_ref": old.get("last_progress_ref"),
            "last_progress_at": old.get("last_progress_at"),
            "next_action": old.get("next_action"),
            "hard_block": old.get("hard_block"),
        })
        existing = all_existing.get(task_id, [])
        if existing and state.get("dispatch_state") == "COMPLETE":
            latest = max(existing, key=lambda item: int(item.get("publication_generation", 1)))
            rows.append(
                {
                    "task_id": task_id,
                    "disposition": "ALREADY_V2_TERMINAL_HISTORY",
                    "publication_id": latest.get("publication_id"),
                    "record_path": latest.get("_record_path"),
                }
            )
            continue
        record, out, disposition = build_record(old, state, existing)
        rows.append(
            {
                "task_id": task_id,
                "disposition": disposition,
                "publication_id": record["publication_id"],
                "record_path": out.relative_to(ROOT).as_posix(),
                "taskbook_path": record["taskbook_path"],
                "record_state": record["record_state"],
                "claimable": record["claimable"],
                "legacy_runtime_state": record["migration_source"]["legacy_runtime_state"],
            }
        )

    counts: dict[str, int] = defaultdict(int)
    for row in rows:
        counts[str(row["disposition"])] += 1
    manifest = {
        "schema": "ENTERPRISE_MATH_LEGACY_CONTROL_MIGRATION_MANIFEST_V1",
        "status": "COMPLETE",
        "effective": MIGRATION_EFFECTIVE,
        "source": {
            "repository": "awdawmip/enterprise-math",
            "commit": SOURCE_COMMIT,
            "archive_branch": ARCHIVE_BRANCH,
            "legacy_definition_files": ["research_scheduler.json", "research_task_registry.json"],
            "authenticated_issue_240_comment_count": len(comments),
        },
        "authority": {
            "basis": "EXPLICIT_CURRENT_USER_DIRECTION_TO_MIGRATE_AND_PHYSICALLY_ISOLATE_THE_LEGACY_CONTROL_PLANE",
            "publisher_role": PUBLISHER_ROLE,
            "publisher_id": PUBLISHER_ID,
            "mathematical_truth_granted": False,
            "working_truth_granted": False,
            "foundation_authority_granted": False,
            "canonical_promotion_granted": False,
            "execution_claim_created": False,
        },
        "counts": {"legacy_union": len(union), **dict(sorted(counts.items()))},
        "tasks": rows,
    }
    exact_write_json(MANIFEST_PATH, manifest)

    errors = research_task_records.audit(ROOT)
    if errors:
        raise MigrationError("V2 task-record audit failed: " + "; ".join(errors))
    if check_only:
        print(json.dumps(manifest["counts"], sort_keys=True))
    else:
        print(json.dumps(manifest, ensure_ascii=False, indent=2))
    return manifest


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--comments", type=Path, required=True)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    run(args.comments, check_only=args.check)
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except MigrationError as exc:
        print("ERROR:", exc)
        raise SystemExit(1)
