#!/usr/bin/env python3
"""Derive repository-backed parent Objective closure for Enterprise Math.

This reducer does not grant PRE_FINAL permission.  It answers the narrower
control question that PRE_FINAL needs: whether the current operational Objective
head is CLOSED *and* every currently active child task under that Objective has
repository-proven terminal control state.

Child terminality reuses existing authorities:

* an active execution-cohort overlay has precedence over an older task-global
  result and is terminal only when the cohort reducer says all active cohorts are
  terminal after exact-set intake, reference pass 1, reference pass 2 and
  synthesis;
* without an active cohort overlay, the generation-aware task result/review
  reducer decides terminality;
* task/objective membership must pass ``research_objective_authority`` so a
  caller string, an unselected OPEN proposal, or an unproven legacy sidecar
  cannot make a child participate in parent-final authority.

Inactive publication families are retained as history but do not count as live
child work.  Any active unbound/ambiguous child fails closed.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any, Mapping

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import research_objective_records as objective_records  # noqa: E402
from tools import research_cohort_runtime  # noqa: E402
from tools import research_objective_authority  # noqa: E402
from tools import research_result_records  # noqa: E402
from tools import research_task_records  # noqa: E402


class ParentClosureError(ValueError):
    pass


def _sha256(path: Path) -> str:
    return "sha256:" + hashlib.sha256(path.read_bytes()).hexdigest()


def _current_head_proof(objective_id: str, root: Path) -> dict[str, Any]:
    head = objective_records.current_head(objective_id, root)
    if head is None:
        raise ParentClosureError("objective has no operational head")
    gid = head.get("objective_generation_id")
    if not isinstance(gid, str) or not gid:
        raise ParentClosureError("objective operational head has no generation id")
    objective = objective_records.objective_record_map(root).get(gid)
    if objective is None or objective.get("objective_id") != objective_id:
        raise ParentClosureError("objective operational head references missing generation")
    receipt = research_objective_authority.selection_receipt_map(root).get(gid)
    if receipt is None or receipt.get("objective_id") != objective_id:
        raise ParentClosureError("objective operational head lacks immutable selection receipt")
    objective_path = objective_records.objective_generation_path(objective_id, gid, root)
    digest = _sha256(objective_path)
    if head.get("objective_record_sha256") != digest:
        raise ParentClosureError("objective operational head digest drift")
    if receipt.get("objective_record_sha256") != digest:
        raise ParentClosureError("objective selection receipt digest drift")
    if receipt.get("record_schema") != research_objective_authority.SELECTION_SCHEMA:
        raise ParentClosureError("objective selection receipt schema mismatch")
    if receipt.get("selection_authority") != research_objective_authority.SELECTION_AUTHORITY:
        raise ParentClosureError("objective selection receipt authority mismatch")
    for head_field, receipt_field in (
        ("objective_generation_id", "objective_generation_id"),
        ("generation", "generation"),
        ("objective_status", "objective_status"),
        ("updated_by", "selected_by"),
        ("updated_at", "selected_at"),
    ):
        if head.get(head_field) != receipt.get(receipt_field):
            raise ParentClosureError(
                f"objective head/selection receipt mismatch for {head_field}"
            )
    return {"head": head, "objective": objective, "selection_receipt": receipt}


def _publication_families(root: Path) -> tuple[dict[str, list[dict[str, Any]]], dict[str, dict[str, Any]]]:
    families: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for item in research_task_records.iter_records(root):
        task_id = item.get("task_id")
        if isinstance(task_id, str) and task_id:
            families[task_id].append(item)
    try:
        current = research_task_records.current_records(root)
    except Exception as exc:
        raise ParentClosureError(f"cannot resolve current task publications: {exc}") from exc
    return dict(families), current


def _task_control_state(task: Mapping[str, Any], root: Path) -> dict[str, Any]:
    task_id = str(task["task_id"])
    publication_id = task.get("publication_id")
    cohort = research_cohort_runtime.task_active_cohort_state(task_id, root)
    if cohort is not None:
        terminal = cohort.get("terminal") is True
        return {
            "task_id": task_id,
            "publication_id": publication_id,
            "terminal": terminal,
            "authority": "ACTIVE_EXECUTION_COHORT_OVERLAY",
            "state": cohort.get("state"),
            "control": cohort,
        }
    result = research_result_records.task_result_state(
        task_id,
        root,
        publication_id=str(publication_id) if isinstance(publication_id, str) else None,
    )
    if result is None:
        return {
            "task_id": task_id,
            "publication_id": publication_id,
            "terminal": False,
            "authority": "TASK_RESULT_REVIEW_STATE",
            "state": "NO_RESULT",
            "control": None,
        }
    return {
        "task_id": task_id,
        "publication_id": publication_id,
        "terminal": result.get("terminal") is True,
        "authority": "TASK_RESULT_REVIEW_STATE",
        "state": result.get("state"),
        "control": result,
    }


def derive_objective_closure(objective_id: str, root: Path = ROOT) -> dict[str, Any]:
    """Return a fail-closed repository projection for one parent Objective."""
    if not isinstance(objective_id, str) or not objective_id.strip():
        raise ParentClosureError("objective_id is required")
    oid = objective_id.strip()
    try:
        proof = _current_head_proof(oid, root)
    except Exception as exc:
        return {
            "objective_id": oid,
            "derived_parent_complete": False,
            "state": "OBJECTIVE_AUTHORITY_INVALID",
            "authority_error": str(exc),
            "final_permission_granted": False,
            "next_control_action": "REPAIR_OR_ESTABLISH_OBJECTIVE_AUTHORITY",
        }

    head = proof["head"]
    objective = proof["objective"]
    head_closed = head.get("objective_status") == "CLOSED"

    try:
        families, current = _publication_families(root)
    except Exception as exc:
        return {
            "objective_id": oid,
            "objective_generation_id": head.get("objective_generation_id"),
            "objective_head_status": head.get("objective_status"),
            "derived_parent_complete": False,
            "state": "TASK_PUBLICATION_AUTHORITY_INVALID",
            "authority_error": str(exc),
            "final_permission_granted": False,
            "next_control_action": "REPAIR_TASK_PUBLICATION_AUTHORITY",
        }

    family_ids = sorted(
        task_id
        for task_id, records in families.items()
        if any(item.get("parent_objective_id") == oid for item in records)
    )
    active_children = sorted(
        task_id
        for task_id, item in current.items()
        if item.get("parent_objective_id") == oid
    )
    inactive_or_detached = sorted(set(family_ids) - set(active_children))

    terminal_children: list[str] = []
    unbound_children: list[dict[str, Any]] = []
    nonterminal_children: list[dict[str, Any]] = []
    child_states: list[dict[str, Any]] = []

    for task_id in active_children:
        task = current[task_id]
        try:
            binding = research_objective_authority.resolve_authoritative_task_parent_binding(
                task, root
            )
        except Exception as exc:
            unbound_children.append(
                {
                    "task_id": task_id,
                    "publication_id": task.get("publication_id"),
                    "reason": str(exc),
                }
            )
            continue
        if binding.get("objective_authority_verified") is not True:
            unbound_children.append(
                {
                    "task_id": task_id,
                    "publication_id": task.get("publication_id"),
                    "reason": "task has no canonical objective-generation authority",
                }
            )
            continue
        if binding.get("objective_id") != oid:
            unbound_children.append(
                {
                    "task_id": task_id,
                    "publication_id": task.get("publication_id"),
                    "reason": "resolved objective binding differs from current parent objective",
                }
            )
            continue
        try:
            control = _task_control_state(task, root)
        except Exception as exc:
            control = {
                "task_id": task_id,
                "publication_id": task.get("publication_id"),
                "terminal": False,
                "authority": "CHILD_CONTROL_ERROR",
                "state": "CONTROL_ERROR",
                "error": str(exc),
            }
        control["objective_generation_id"] = binding.get("objective_generation_id")
        control["binding_source"] = binding.get("binding_source")
        child_states.append(control)
        if control.get("terminal") is True:
            terminal_children.append(task_id)
        else:
            nonterminal_children.append(control)

    derived_complete = bool(
        head_closed
        and not unbound_children
        and not nonterminal_children
        and len(terminal_children) == len(active_children)
    )
    if not head_closed:
        state = "OBJECTIVE_HEAD_NOT_CLOSED"
        next_action = "CONTINUE_OBJECTIVE_WORK"
    elif unbound_children:
        state = "ACTIVE_CHILD_OBJECTIVE_BINDING_UNPROVEN"
        next_action = "BIND_OR_MIGRATE_ACTIVE_CHILD_OBJECTIVE_AUTHORITY"
    elif nonterminal_children:
        state = "ACTIVE_CHILD_CONTROL_NOT_TERMINAL"
        next_action = "RESOLVE_CHILD_RESULTS_COHORTS_AND_SYNTHESIS"
    else:
        state = "DERIVED_PARENT_COMPLETE"
        next_action = "PRE_FINAL_LIVENESS_RECHECK"

    return {
        "objective_id": oid,
        "objective_generation_id": head.get("objective_generation_id"),
        "objective_head_status": head.get("objective_status"),
        "objective_selection_receipt_verified": True,
        "closure_evidence_refs": objective.get("closure_evidence_refs", []),
        "child_task_family_ids": family_ids,
        "active_child_task_ids": active_children,
        "inactive_or_detached_task_ids": inactive_or_detached,
        "terminal_active_child_task_ids": sorted(terminal_children),
        "unbound_active_children": unbound_children,
        "nonterminal_active_children": nonterminal_children,
        "child_control_states": child_states,
        "derived_parent_complete": derived_complete,
        "state": state,
        "final_permission_granted": False,
        "working_truth_granted": False,
        "foundation_authority_granted": False,
        "canonical_promotion_granted": False,
        "next_control_action": next_action,
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Derive Enterprise Math parent Objective closure from repository state"
    )
    parser.add_argument("--objective-id", required=True)
    args = parser.parse_args()
    result = derive_objective_closure(args.objective_id, ROOT)
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
    return 0 if result.get("derived_parent_complete") is True else 1


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except ParentClosureError as exc:
        print("ERROR:", exc)
        raise SystemExit(1)
