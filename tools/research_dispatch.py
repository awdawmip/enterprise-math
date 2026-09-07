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
   explicit Result lifecycle view receive the same canonical lifecycle gate;
4. an immutable execution intent may authorize only the exact task-publication
   generation it was prepared for; and
5. a runtime event explicitly bound to the current V2 publication cannot predate
   the immutable publication record that makes that task generation exist.

The preserved core remains fail-closed: runtime input must be raw authenticated
Issue #240 comment objects. No priority, lease duration, Driver disposition,
terminalization, or task-selection policy is changed here.
"""
from __future__ import annotations

import copy
from pathlib import Path
from typing import Any

from tools import research_dispatch_core as _core

ROOT = _core.ROOT
DispatchError = _core.DispatchError

_ORIGINAL_REGISTERED_DEFINITION = _core.registered_definition
_ORIGINAL_OVERLAY_RESULT_STATE = _core._overlay_result_state
_ORIGINAL_FILTER_REGISTERED_EVENTS = _core._filter_registered_events
_AUTO_RESULT_STATE = object()


def registered_definition(
    record: dict[str, Any], root: Path = ROOT
) -> dict[str, Any]:
    """Expose the immutable publication clock to the runtime compatibility layer."""
    value = _ORIGINAL_REGISTERED_DEFINITION(record, root)
    published_at = record.get("published_at")
    if not isinstance(published_at, str) or not published_at.strip():
        raise DispatchError(f"{record.get('task_id')}: task publication published_at is required")
    try:
        _core._lifecycle_time(published_at, "task publication published_at")
    except DispatchError:
        raise
    value["publication_published_at"] = published_at.strip()
    return value


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
    """Fail closed when an execution intent belongs to another publication."""
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


def _enforce_publication_event_causality(
    task: dict[str, Any],
    events: list[dict[str, Any]],
    accepted: list[dict[str, Any]],
    rejected: list[dict[str, Any]],
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    """Reject current-generation authority that predates task existence.

    Canonical production definitions carry ``publication_published_at`` from the
    immutable V2 task record.  Synthetic/direct compatibility definitions that do
    not carry that field retain historical test/library behavior; they are not the
    production task-definition source.

    The time gate is deliberately narrow.  CLAIMs normalized to the current
    publication are checked.  Claimless UNBLOCK/SUPERSEDE are checked only when
    they explicitly name the current publication.  Therefore pre-cutover
    publicationless legacy replay remains available to the migration path.
    """
    if not _core._is_registered(task):
        return accepted, rejected
    published_raw = task.get("publication_published_at")
    if published_raw is None:
        return accepted, rejected
    try:
        published_at = _core._lifecycle_time(
            published_raw, "task publication published_at"
        )
    except DispatchError:
        raise
    expected = task.get("publication_id")
    kept: list[dict[str, Any]] = []
    extra_rejected = list(rejected)
    for event in accepted:
        if event.get("task_id") != task.get("task_id"):
            kept.append(event)
            continue
        kind = event.get("event")
        bound_to_current = (
            kind == "CLAIM" and event.get("publication_id") == expected
        ) or (
            kind in {"UNBLOCK", "SUPERSEDE"}
            and event.get("publication_id") == expected
        )
        if not bound_to_current:
            kept.append(event)
            continue
        meta = event.get(_core.GITHUB_META_KEY)
        created_raw = meta.get("created_at") if isinstance(meta, dict) else None
        index = _event_source_index(event, events)
        try:
            created_at = _core._lifecycle_time(created_raw, "GitHub created_at")
        except DispatchError as exc:
            extra_rejected.append(
                {
                    "index": index if index is not None else 0,
                    "reason": f"registered {kind} current-publication clock is invalid: {exc}",
                }
            )
            continue
        if created_at < published_at:
            extra_rejected.append(
                {
                    "index": index if index is not None else 0,
                    "reason": f"registered {kind} predates current task publication",
                }
            )
            continue
        kept.append(event)
    return kept, extra_rejected


def _filter_registered_events(
    task: dict[str, Any],
    events: list[dict[str, Any]],
    root: Path,
    result_state: dict[str, Any] | None | object = _AUTO_RESULT_STATE,
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    """Apply lifecycle, generation, and publication-time gates."""
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
    accepted, rejected = _ORIGINAL_FILTER_REGISTERED_EVENTS(
        task,
        events,
        root,
        result_state if isinstance(result_state, dict) else None,
    )
    accepted, rejected = _bind_intent_claim_publications(
        task, events, accepted, rejected, root
    )
    return _enforce_publication_event_causality(task, events, accepted, rejected)


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


# Patch the preserved core because functions such as merged_definitions() and
# effective_states() resolve these helpers in the core module's global namespace.
_core.registered_definition = registered_definition
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
