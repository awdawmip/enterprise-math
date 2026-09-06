#!/usr/bin/env python3
"""Canonical immutable-V2 Enterprise Math dispatch compatibility wrapper.

The pre-fix implementation is preserved byte-for-byte in
``tools.research_dispatch_core``. This public entrypoint keeps the same API while
repairing two reopen-path compatibility defects:

1. an authorized CLAIM admitted after a nonterminal Driver review must remain the
   live owner when the reducer already reports a valid ``LEASED`` state; and
2. legacy/runtime-guard callers of ``_filter_registered_events`` that omit an
   explicit Result lifecycle view must receive the same canonical lifecycle gate,
   rather than failing by arity or bypassing the frozen-result interval.

The preserved core remains fail-closed: runtime input must be raw authenticated Issue #240 comment objects.
No priority, lease duration, Driver disposition, terminalization, or task-selection
policy is changed here. The wrapper only preserves authority that the core reducer
and Result lifecycle gate have already accepted.
"""
from __future__ import annotations

import copy
from pathlib import Path
from typing import Any

from tools import research_dispatch_core as _core

ROOT = _core.ROOT
DispatchError = _core.DispatchError

_ORIGINAL_OVERLAY_RESULT_STATE = _core._overlay_result_state
_ORIGINAL_FILTER_REGISTERED_EVENTS = _core._filter_registered_events
_AUTO_RESULT_STATE = object()


def _filter_registered_events(
    task: dict[str, Any],
    events: list[dict[str, Any]],
    root: Path,
    result_state: dict[str, Any] | None | object = _AUTO_RESULT_STATE,
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    """Apply the registered-event lifecycle gate with backward-compatible arity.

    Canonical dispatch already supplies ``result_state`` explicitly. Older runtime
    guard callers supplied only ``task, events, root``. For those callers, resolve
    the same immutable Result/Driver state here so execution authorization cannot
    bypass a frozen-result interval and cannot fail merely because the helper grew
    a lifecycle parameter.
    """
    if result_state is _AUTO_RESULT_STATE:
        resolved: dict[str, Any] | None = None
        if _core._is_registered(task):
            publication_id = task.get("publication_id")
            resolved = _core.research_result_records.task_result_state(
                task["task_id"],
                root,
                publication_id if isinstance(publication_id, str) else None,
            )
        result_state = resolved
    return _ORIGINAL_FILTER_REGISTERED_EVENTS(
        task,
        events,
        root,
        result_state if isinstance(result_state, dict) else None,
    )


def _overlay_result_state(
    task: dict[str, Any],
    state: dict[str, Any],
    root: Path,
    result_state: dict[str, Any] | None,
) -> dict[str, Any]:
    """Preserve a reducer-accepted live owner across a nonterminal reopen.

    ``_claim_result_gate_reason`` already rejects CLAIMs created inside the frozen
    interval and admits CLAIMs at or after the authoritative ``reviewed_at`` of a
    nonterminal Driver review. Therefore a reducer output of ``LEASED`` here is
    already a live, post-reopen owner. Clearing it in the Result overlay creates a
    permanent CLAIM_NEW_OWNER loop and contradicts that lifecycle gate.
    """
    if (
        _core._is_registered(task)
        and isinstance(result_state, dict)
        and result_state.get("state") == "RETURN_TO_EXECUTION"
        and state.get("dispatch_state") == "LEASED"
        and isinstance(state.get("claim_id"), str)
        and bool(state.get("claim_id"))
    ):
        value = copy.deepcopy(state)
        result = result_state.get("result")
        review = result_state.get("review")
        if isinstance(result, dict):
            value["result_id"] = result.get("result_id")
            value["result_record_path"] = result.get("_record_path")
        value["driver_disposition"] = (
            review.get("disposition") if isinstance(review, dict) else None
        )
        value["next_action"] = "Resume task under Driver disposition"
        return value
    return _ORIGINAL_OVERLAY_RESULT_STATE(task, state, root, result_state)


# Patch the preserved core because functions such as effective_states() resolve
# these helpers in the core module's global namespace. Then re-export the complete
# historical surface, including private helpers used by repository runtime guards.
_core._filter_registered_events = _filter_registered_events
_core._overlay_result_state = _overlay_result_state

for _name in dir(_core):
    if _name.startswith("__"):
        continue
    globals().setdefault(_name, getattr(_core, _name))


if __name__ == "__main__":
    try:
        raise SystemExit(_core.main())
    except _core.DispatchError as exc:
        print("ERROR:", exc)
        raise SystemExit(1)
