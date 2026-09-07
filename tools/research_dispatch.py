#!/usr/bin/env python3
"""Canonical immutable-V2 Enterprise Math dispatch compatibility wrapper.

The pre-fix implementation is preserved byte-for-byte in
``tools.research_dispatch_core``. This public entrypoint keeps the same API while
repairing reopen-path compatibility defects:

1. an authorized CLAIM admitted after a nonterminal Driver review must remain the
   live owner when the reducer already reports a valid ``LEASED`` state;
2. once a reducer-applied runtime transition occurs at or after that Driver review,
   the old ``RETURN_TO_EXECUTION`` Result is only the reopen edge, not a permanent
   overlay over the new revision cycle; and
3. legacy/runtime-guard callers of ``_filter_registered_events`` that omit an
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


def _post_review_runtime_transition(
    state: dict[str, Any], result_state: dict[str, Any]
) -> bool:
    """Whether the reducer has applied a transition on/after the reopen boundary.

    GitHub event ingestion overwrites body-declared ``at`` with the immutable
    server ``created_at`` before reduction. Reducer-applied PROGRESS, HANDOFF,
    HARD_BLOCK, UNBLOCK and SUPERSEDE transitions copy that trusted clock into
    ``last_progress_at``; ignored events do not. CLAIM/HEARTBEAT do not advance
    ``last_progress_at`` and are handled separately by the live-LEASED guard.

    Therefore a trusted ``last_progress_at >= reviewed_at`` is the compact state
    witness that the old nonterminal review has already performed its one-time
    reopen role and must no longer overwrite the new revision cycle.
    """
    review = result_state.get("review")
    reviewed_at = review.get("reviewed_at") if isinstance(review, dict) else None
    last_progress_at = state.get("last_progress_at")
    if not isinstance(reviewed_at, str) or not reviewed_at.strip():
        return False
    if not isinstance(last_progress_at, str) or not last_progress_at.strip():
        return False
    try:
        reopened_at = _core._lifecycle_time(reviewed_at, "reviewed_at")
        runtime_at = _core.research_runtime_reducer.parse_time(last_progress_at)
    except Exception:
        return False
    return runtime_at >= reopened_at


def _overlay_result_state(
    task: dict[str, Any],
    state: dict[str, Any],
    root: Path,
    result_state: dict[str, Any] | None,
) -> dict[str, Any]:
    """Treat nonterminal Driver review as a reopen edge, not a permanent overlay.

    ``_claim_result_gate_reason`` rejects CLAIMs inside the frozen interval and
    admits CLAIMs at or after authoritative ``reviewed_at``. A reducer output of
    ``LEASED`` is therefore already a live post-reopen owner and must survive.

    After that owner (or an authorized claimless mutation) causes a reducer-applied
    transition on/after ``reviewed_at``, the reducer state becomes the newer
    authority. This is essential for a second result-bearing HANDOFF, HARD_BLOCK,
    UNBLOCK/plain HANDOFF continuation, or current-generation SUPERSEDE. The old
    Result/REQUEST_REVISION record remains provenance but cannot reopen the task a
    second time. Ignored events cannot acquire precedence because they do not
    advance reducer ``last_progress_at``.
    """
    if (
        _core._is_registered(task)
        and isinstance(result_state, dict)
        and result_state.get("state") == "RETURN_TO_EXECUTION"
    ):
        if (
            state.get("dispatch_state") == "LEASED"
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
        if _post_review_runtime_transition(state, result_state):
            return copy.deepcopy(state)
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
