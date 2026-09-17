"""Compose legacy scope repair with the existing operational Result reopen edge.

No new Result, review or publication is created. The current Result reader is
already fault-isolated by the canonical bootstrap. Never trust a task/body flag
as proof of a Driver's reopen decision.
"""
from __future__ import annotations

import copy
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
REOPEN_KEY = "_handoff_scope_review_reopened_at"


def definition_for_result(task: dict[str, Any], result_state: Any) -> dict[str, Any]:
    value = copy.deepcopy(task)
    value.pop(REOPEN_KEY, None)
    if isinstance(result_state, dict) and result_state.get("state") == "RETURN_TO_EXECUTION":
        review = result_state.get("review")
        reopened_at = review.get("reviewed_at") if isinstance(review, dict) else None
        if isinstance(reopened_at, str) and reopened_at.strip():
            value[REOPEN_KEY] = reopened_at
    return value


def install(root: Path = ROOT) -> None:
    from tools import research_dispatch
    from tools import research_result_records

    if getattr(research_dispatch, "_legacy_handoff_scope_runtime_installed", False):
        return
    original = research_dispatch.reduce_definition

    def reduce_definition(task, events, *, now, default_lease_minutes=120,
                          root=research_dispatch.ROOT):
        result = None
        if task.get("registration_source") == "IMMUTABLE_TASK_RECORD":
            result = research_result_records.task_result_state(
                task["task_id"], root, task.get("publication_id")
            )
        return original(definition_for_result(task, result), events, now=now,
                        default_lease_minutes=default_lease_minutes, root=root)

    research_dispatch._core.reduce_definition = reduce_definition
    research_dispatch.reduce_definition = reduce_definition
    research_dispatch._legacy_handoff_scope_runtime_installed = True
