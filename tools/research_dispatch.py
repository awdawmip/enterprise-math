#!/usr/bin/env python3
"""Canonical immutable-V2 Enterprise Math dispatch compatibility wrapper.

The pre-fix implementation is preserved byte-for-byte in
``tools.research_dispatch_core``. This public entrypoint keeps the same API while
repairing narrow compatibility defects:

1. an authorized CLAIM admitted after a nonterminal Driver review must remain the
   live owner when the reducer already reports a valid ``LEASED`` state;
2. once a reducer-applied runtime transition occurs at or after that Driver review,
   the old ``RETURN_TO_EXECUTION`` Result is only the reopen edge, not a permanent
   overlay over the new revision cycle;
3. legacy/runtime-guard callers of ``_filter_registered_events`` that omit an
   explicit Result lifecycle view receive the same canonical lifecycle gate; and
4. an immutable execution intent may authorize only the exact task-publication
   generation it was prepared for.  Intent-backed CLAIMs are normalized to that
   current publication and cannot use an old intent to cross a V2 generation.

The preserved core remains fail-closed: runtime input must be raw authenticated
Issue #240 comment objects. No priority, lease duration, Driver disposition,
terminalization, or task-selection policy is changed here.
"""
from __future__ import annotations

import copy
from contextlib import contextmanager
from control_plane import research_result_authority_fault_isolation as _result_authority
from pathlib import Path
from typing import Any

from tools import research_dispatch_core as _core

ROOT = _core.ROOT
DispatchError = _core.DispatchError

_ORIGINAL_OVERLAY_RESULT_STATE = _core._overlay_result_state
_ORIGINAL_OVERLAY_ACTIVE_COHORT = _core._overlay_active_cohort
_ORIGINAL_RESULT_SNAPSHOT = _core._dispatch_result_read_snapshot
_ORIGINAL_FILTER_REGISTERED_EVENTS = _core._filter_registered_events
_AUTO_RESULT_STATE = object()


def _event_source_index(
    event: dict[str, Any], events: list[dict[str, Any]]
) -> int | None:
    """Recover the authenticated-stream index after core normalization copies."""
    meta = event.get(_core.GITHUB_META_KEY)
    comment_id = meta.get("comment_id") if isinstance(meta, dict) else None
    if type(comment_id) is not int:
        return None
    for index, source in enumerate(events):
        source_meta = source.get(_core.GITHUB_META_KEY)
        if isinstance(source_meta, dict) and source_meta.get("comment_id") == comment_id:
            return index
    return None


def _bind_intent_claim_publications(
    task: dict[str, Any],
    events: list[dict[str, Any]],
    accepted: list[dict[str, Any]],
    rejected: list[dict[str, Any]],
    root: Path,
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    """Fail closed when an execution intent belongs to another publication.

    ``research_execution_records.intent_for_claim`` indexes historical immutable
    intents by task/claim owner scope so old generations remain auditable.  That
    lookup is intentionally not a current-publication selector.  Therefore an
    intent-backed CLAIM must prove that the returned intent belongs to the current
    task publication before it can carry execution authority.

    When the event omits ``publication_id``, a current immutable intent supplies
    the generation binding and the normalized event receives it explicitly.  A
    supplied event publication must also equal the current generation.
    """
    if not _core._is_registered(task):
        return accepted, rejected
    expected = task.get("publication_id")
    kept: list[dict[str, Any]] = []
    extra_rejected = list(rejected)
    for event in accepted:
        if event.get("task_id") != task.get("task_id") or event.get("event") != "CLAIM":
            kept.append(event)
            continue
        claim_id = event.get("claim_id")
        if not isinstance(claim_id, str) or not claim_id:
            kept.append(event)
            continue
        try:
            intent = _core.research_execution_records.intent_for_claim(
                task["task_id"], claim_id, root
            )
        except Exception as exc:
            index = _event_source_index(event, events)
            extra_rejected.append(
                {
                    "index": index if index is not None else 0,
                    "reason": f"execution intent lookup failed during publication binding: {exc}",
                }
            )
            continue
        if intent is None:
            # Inline/no-intent CLAIMs were already publication-checked by the core.
            kept.append(event)
            continue
        index = _event_source_index(event, events)
        intent_publication = intent.get("publication_id")
        if (
            not isinstance(expected, str)
            or not expected
            or intent_publication != expected
        ):
            extra_rejected.append(
                {
                    "index": index if index is not None else 0,
                    "reason": "registered CLAIM execution intent publication_id does not match current task publication",
                }
            )
            continue
        supplied = event.get("publication_id")
        if supplied is not None and supplied != expected:
            extra_rejected.append(
                {
                    "index": index if index is not None else 0,
                    "reason": "registered CLAIM publication_id does not match current task publication",
                }
            )
            continue
        normalized = copy.deepcopy(event)
        normalized["publication_id"] = expected
        kept.append(normalized)
    return kept, extra_rejected


def _filter_registered_events(
    task: dict[str, Any],
    events: list[dict[str, Any]],
    root: Path,
    result_state: dict[str, Any] | None | object = _AUTO_RESULT_STATE,
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    """Apply lifecycle and generation gates with backward-compatible arity."""
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
    held = isinstance(result_state, dict) and result_state.get("state") == _result_authority.STATE
    accepted, rejected = _ORIGINAL_FILTER_REGISTERED_EVENTS(
        task,
        events,
        root,
        result_state if isinstance(result_state, dict) and not held else None,
    )
    accepted, rejected = _bind_intent_claim_publications(task, events, accepted, rejected, root)
    if held and _core._is_registered(task):
        kept = []
        for event in accepted:
            if event.get("task_id") != task.get("task_id"):
                kept.append(event)
                continue
            kind = event.get("event")
            blocked = kind in {"CLAIM", "HANDOFF", "DONE", "UNBLOCK", "SUPERSEDE"}
            if kind == "CLAIM":
                # Keep authenticated pre-freeze ownership as historical source;
                # live execution is separately denied by the repository guard.
                meta = event.get(_core.GITHUB_META_KEY)
                try:
                    blocked = not (isinstance(meta, dict) and
                        _core._lifecycle_time(meta.get("created_at"), "GitHub created_at") <
                        _core._lifecycle_time(result_state.get("withheld_frozen_at"), "withheld freeze"))
                except Exception:
                    blocked = True
            if blocked:
                index = _event_source_index(event, events)
                rejected.append({"index": index if index is not None else 0,
                                 "reason": _result_authority.STATE + ": control recovery required"})
            else:
                kept.append(event)
        accepted = kept
    return accepted, rejected


def _post_review_runtime_transition(
    state: dict[str, Any], result_state: dict[str, Any]
) -> bool:
    """Whether the reducer has applied a transition on/after the reopen boundary."""
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
    """Treat nonterminal Driver review as a reopen edge, not a permanent overlay."""
    if (_core._is_registered(task) and isinstance(result_state, dict)
            and result_state.get("state") == _result_authority.STATE):
        value = copy.deepcopy(state)
        value.update({"state": "BLOCKED", "dispatch_state": "BLOCKED", "terminal": False,
                      "result_authority_state": _result_authority.STATE,
                      "result_id": None, "review_id": None, "driver_disposition": None,
                      "historical_execution_claims": copy.deepcopy(result_state.get("historical_execution_claims", [])),
                      "hard_block": {
                          "code": _result_authority.STATE,
                          "publication_id": result_state.get("publication_id"),
                          "withheld_result_ids": list(result_state.get("withheld_result_ids", [])),
                          "owner": "control-plane/result-authority-recovery",
                          "missing_object": "a valid frozen Result under the ordinary Result/replacement contract",
                          "necessity": "Invalid frozen Result evidence cannot authorize execution, completion, review or follow-up.",
                          "unblock_condition": "Obtain a valid Result through the existing contract and re-run strict control gates.",
                      },
                      "next_action": "Wait for Result control authority recovery under the ordinary Result/replacement contract"})
        return value
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


def _overlay_active_cohort(task: dict[str, Any], state: dict[str, Any], root: Path) -> dict[str, Any]:
    value = _ORIGINAL_OVERLAY_ACTIVE_COHORT(task, state, root)
    if state.get("result_authority_state") != _result_authority.STATE:
        return value
    if value.get("dispatch_state") == "COHORT_ACTIVE":
        # A separately published lane remains independent. Withheld source
        # generation lanes cannot erase the exact-generation control block.
        cohorts = _core.research_cohort_runtime.active_cohorts(task["task_id"], root)
        lane_publications = {lane.get("publication_id") for cohort in cohorts
                             for lane in cohort.get("lanes", []) if isinstance(lane, dict)}
        withheld_publications = set()
        for publication_id in lane_publications:
            if not isinstance(publication_id, str):
                continue
            lane_result = _core.research_result_records.task_result_state(
                task["task_id"], root, publication_id,
            )
            if isinstance(lane_result, dict) and lane_result.get("state") == _result_authority.STATE:
                withheld_publications.add(publication_id)
        if lane_publications - withheld_publications - {None}:
            value["withheld_lane_publication_ids"] = sorted(withheld_publications)
            value["task_global_result_authority_withheld"] = copy.deepcopy(state.get("hard_block"))
            value.pop("hard_block", None)
            value.pop("result_authority_state", None)
            return value
    return state


@contextmanager
def _dispatch_result_read_snapshot(root: Path = _core.ROOT):
    with _result_authority.authority_snapshot(root):
        with _ORIGINAL_RESULT_SNAPSHOT(root):
            yield


# Patch the preserved core because functions such as effective_states() resolve
# these helpers in the core module's global namespace. Then re-export the complete
# historical surface, including private helpers used by repository runtime guards.
_core._filter_registered_events = _filter_registered_events
_core._overlay_result_state = _overlay_result_state
_core._overlay_active_cohort = _overlay_active_cohort
_core._dispatch_result_read_snapshot = _dispatch_result_read_snapshot

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
