#!/usr/bin/env python3
"""Fail-closed dispatch gate for non-open parent Objectives.

A current immutable task publication is necessary but not sufficient authority for
fresh execution.  If the task's current parent Objective head is PARKED or CLOSED,
that later Objective authority wins over historical READY/HANDOFF_READY/CLAIM
state.  The task remains immutable history and any frozen Result remains
reviewable; only fresh operational selection is withheld.

This layer grants no Objective, task, review, or mathematical authority.  It only
consumes the current immutable Objective head and is therefore automatically
reversible if ordinary Driver authority later publishes an OPEN Objective head.
"""
from __future__ import annotations

import copy
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
NONOPEN_STATUSES = {"PARKED", "CLOSED"}


class ParentObjectiveDispatchGateError(ValueError):
    pass


def apply_parent_objective_gate(
    task: dict[str, Any], state: dict[str, Any], root: Path = ROOT
) -> dict[str, Any]:
    parent = task.get("parent_objective_id")
    if not isinstance(parent, str) or not parent.strip():
        return state

    import research_objective_records

    head = research_objective_records.current_head(parent.strip(), root)
    if head is None:
        return state
    status = str(head.get("objective_status") or "").upper()
    if status == "OPEN":
        return state
    if status not in NONOPEN_STATUSES:
        raise ParentObjectiveDispatchGateError(
            f"{task.get('task_id')}: unsupported parent Objective status {status!r}"
        )

    value = copy.deepcopy(state)
    suppressed = {
        key: value.get(key)
        for key in (
            "state",
            "dispatch_state",
            "claim_id",
            "actor",
            "researcher_id",
            "lease_until",
            "result_id",
            "review_id",
        )
        if value.get(key) is not None
    }
    if suppressed:
        value["suppressed_operational_state_due_to_parent_objective"] = suppressed

    value["state"] = "BLOCKED"
    value["dispatch_state"] = f"PARENT_OBJECTIVE_{status}"
    value["claim_id"] = None
    value["actor"] = None
    value["researcher_id"] = None
    value["identity_source"] = None
    value["lease_until"] = None
    value["next_action"] = (
        "Return to Objective/Driver control. Fresh task execution is disabled while "
        f"parent Objective {parent} is {status}."
    )
    value["hard_block"] = {
        "code": "PARENT_OBJECTIVE_NOT_OPEN",
        "parent_objective_id": parent,
        "objective_generation_id": head.get("objective_generation_id"),
        "objective_status": status,
        "missing_object": "one authority-valid OPEN operational parent Objective generation",
        "owner": "research-driver/objective-control",
        "necessity": (
            "A child task cannot acquire or resume fresh execution authority after its "
            "operational parent Objective has been parked or closed."
        ),
        "unblock_condition": (
            "Ordinary Driver authority publishes an OPEN parent Objective head, or an "
            "authorized successor task is published under another OPEN Objective; then "
            "canonical dispatch is recomputed from immutable records."
        ),
    }
    return value


def install(root: Path = ROOT) -> None:
    """Install the Objective gate after all ordinary task/result/cohort overlays."""
    from tools import research_dispatch, research_task_records

    if not getattr(research_dispatch, "_parent_objective_definition_enrichment_installed", False):
        base_merged = research_dispatch.merged_definitions

        def merged_definitions(
            local_root: Path = research_dispatch.ROOT,
        ) -> list[dict[str, Any]]:
            values = base_merged(local_root)
            current = research_task_records.current_records(local_root)
            out: list[dict[str, Any]] = []
            for raw in values:
                item = copy.deepcopy(raw)
                task_id = item.get("task_id") if isinstance(item, dict) else None
                record = current.get(task_id) if isinstance(task_id, str) else None
                if isinstance(record, dict):
                    parent = record.get("parent_objective_id")
                    if isinstance(parent, str) and parent:
                        item["parent_objective_id"] = parent
                out.append(item)
            return out

        research_dispatch.merged_definitions = merged_definitions
        research_dispatch._parent_objective_definition_enrichment_installed = True

    if not getattr(research_dispatch, "_parent_objective_dispatch_gate_installed", False):
        base_reduce = research_dispatch.reduce_definition

        def reduce_definition(
            task: dict[str, Any],
            events: list[dict[str, Any]],
            *,
            now,
            default_lease_minutes: int = 120,
            root: Path = research_dispatch.ROOT,
        ) -> dict[str, Any]:
            reduced = base_reduce(
                task,
                events,
                now=now,
                default_lease_minutes=default_lease_minutes,
                root=root,
            )
            return apply_parent_objective_gate(task, reduced, root)

        research_dispatch.reduce_definition = reduce_definition
        research_dispatch._parent_objective_dispatch_gate_installed = True


def audit(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    try:
        install(root)
        from tools import research_dispatch
        import research_objective_records

        for task in research_dispatch.merged_definitions(root):
            parent = task.get("parent_objective_id")
            if not isinstance(parent, str) or not parent:
                continue
            head = research_objective_records.current_head(parent, root)
            if head is None:
                continue
            status = str(head.get("objective_status") or "").upper()
            if status not in NONOPEN_STATUSES:
                continue
            probe = apply_parent_objective_gate(
                task,
                {
                    "task_id": task.get("task_id"),
                    "state": task.get("base_state", "READY"),
                    "dispatch_state": "NEEDS_DISPATCH",
                },
                root,
            )
            if probe.get("state") != "BLOCKED":
                errors.append(f"{task.get('task_id')}: non-open parent Objective is not BLOCKED")
            block = probe.get("hard_block")
            if not isinstance(block, dict) or block.get("parent_objective_id") != parent:
                errors.append(f"{task.get('task_id')}: parent Objective hard block is incomplete")
    except Exception as exc:
        errors.append(str(exc))
    return errors


if __name__ == "__main__":
    found = audit()
    if found:
        for item in found:
            print("ERROR:", item)
        raise SystemExit(1)
    print("PASS: non-open parent Objectives cannot dispatch child tasks.")
