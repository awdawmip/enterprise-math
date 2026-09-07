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
   generation it was prepared for. Intent-backed CLAIMs are normalized to that
   current publication and cannot use an old intent to cross a V2 generation; and
5. registered terminal/HANDOFF fail-closed guards obtain blocking authority only
   from the claim that was actually live at the authenticated event time.

The preserved core remains fail-closed: runtime input must be raw authenticated
Issue #240 comment objects. No priority, lease duration, Driver disposition,
terminalization, or task-selection policy is changed here.
"""
from __future__ import annotations

import copy
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from tools import research_dispatch_core as _core

ROOT = _core.ROOT
DispatchError = _core.DispatchError

_ORIGINAL_OVERLAY_RESULT_STATE = _core._overlay_result_state
_ORIGINAL_FILTER_REGISTERED_EVENTS = _core._filter_registered_events
_ORIGINAL_BLOCK_UNREVIEWED_REGISTERED_DONE = _core._block_unreviewed_registered_done
_AUTO_RESULT_STATE = object()

# Audited compatibility boundary.  Between this GitHub-server timestamp and
# deployment, the complete Issue #240 stream contained exactly two HANDOFFs: one
# structurally ambiguous PCF return and one already-structured P021 frozen return;
# there was no plain researcher-to-researcher continuation in that interval.
HANDOFF_SCOPE_CUTOVER = datetime(2026, 9, 7, 2, 20, tzinfo=timezone.utc)
HANDOFF_SCOPE_CONTINUATION = "CONTINUATION"
HANDOFF_SCOPE_FROZEN_RETURN = "FROZEN_RETURN_AWAITING_DRIVER_REVIEW"
DRIVER_REVIEW_TERMINAL_SCOPE = "RESEARCH_RETURN_FROZEN_AWAITING_DRIVER_REVIEW"
HANDOFF_SCOPE_REASON_PREFIX = "registered HANDOFF scope contract:"


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
    intents by task/claim owner scope so old generations remain auditable. That
    lookup is intentionally not a current-publication selector. Therefore an
    intent-backed CLAIM must prove that the returned intent belongs to the current
    task publication before it can carry execution authority.

    When the event omits ``publication_id``, a current immutable intent supplies
    the generation binding and the normalized event receives it explicitly. A
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


def _registered_handoff_scope_reason(event: dict[str, Any]) -> str | None:
    """Return a post-cutover structural HANDOFF defect, never a prose inference."""
    if event.get("event") != "HANDOFF":
        return None
    meta = event.get(_core.GITHUB_META_KEY)
    created_at = meta.get("created_at") if isinstance(meta, dict) else None
    try:
        created = _core.research_runtime_reducer.parse_time(created_at)
    except Exception:
        return f"{HANDOFF_SCOPE_REASON_PREFIX} invalid authenticated created_at"
    if created < HANDOFF_SCOPE_CUTOVER:
        return None

    result_id = event.get("result_id")
    if result_id is not None and (
        not isinstance(result_id, str) or not result_id.strip()
    ):
        return f"{HANDOFF_SCOPE_REASON_PREFIX} result_id must be a nonempty string when supplied"

    handoff_scope = event.get("handoff_scope")
    if handoff_scope is not None and handoff_scope not in {
        HANDOFF_SCOPE_CONTINUATION,
        HANDOFF_SCOPE_FROZEN_RETURN,
    }:
        return f"{HANDOFF_SCOPE_REASON_PREFIX} invalid handoff_scope"

    terminal_scope = event.get("terminal_scope")
    if terminal_scope is not None and terminal_scope != DRIVER_REVIEW_TERMINAL_SCOPE:
        return f"{HANDOFF_SCOPE_REASON_PREFIX} invalid terminal_scope"

    # ``terminal_candidate`` remains reducer compatibility for historical events,
    # but new registered producers must use the typed HANDOFF contract.
    if event.get("terminal_candidate") is not None:
        return f"{HANDOFF_SCOPE_REASON_PREFIX} terminal_candidate is legacy-only after cutover"

    frozen_marker = (
        isinstance(result_id, str) and bool(result_id.strip())
    ) or terminal_scope == DRIVER_REVIEW_TERMINAL_SCOPE or (
        handoff_scope == HANDOFF_SCOPE_FROZEN_RETURN
    )

    if handoff_scope == HANDOFF_SCOPE_CONTINUATION and frozen_marker:
        return f"{HANDOFF_SCOPE_REASON_PREFIX} CONTINUATION contradicts frozen-return marker"
    if handoff_scope == HANDOFF_SCOPE_CONTINUATION or frozen_marker:
        return None
    return f"{HANDOFF_SCOPE_REASON_PREFIX} explicit machine scope required after cutover"


def _enforce_registered_handoff_scopes(
    events: list[dict[str, Any]],
    accepted: list[dict[str, Any]],
    rejected: list[dict[str, Any]],
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    kept: list[dict[str, Any]] = []
    extra_rejected = list(rejected)
    for event in accepted:
        reason = _registered_handoff_scope_reason(event)
        if reason is None:
            kept.append(event)
            continue
        index = _event_source_index(event, events)
        extra_rejected.append(
            {"index": index if index is not None else 0, "reason": reason}
        )
    return kept, extra_rejected


def _filter_registered_events(
    task: dict[str, Any],
    events: list[dict[str, Any]],
    root: Path,
    result_state: dict[str, Any] | None | object = _AUTO_RESULT_STATE,
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    """Apply lifecycle, generation, and typed-HANDOFF gates."""
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
    return _enforce_registered_handoff_scopes(events, accepted, rejected)


def _event_had_live_claim(
    task: dict[str, Any],
    event: dict[str, Any],
    reduced_task_events: list[dict[str, Any]] | None,
) -> bool:
    """Whether a rejected terminal event belonged to the live claim at event time."""
    if reduced_task_events is None:
        # Direct legacy callers lack replay context; preserve conservative behavior.
        return True
    claim_id = event.get("claim_id")
    if not isinstance(claim_id, str) or not claim_id:
        return False
    meta = event.get(_core.GITHUB_META_KEY)
    comment_id = meta.get("comment_id") if isinstance(meta, dict) else None
    created_at = meta.get("created_at") if isinstance(meta, dict) else None
    if type(comment_id) is not int or not isinstance(created_at, str):
        return False
    try:
        event_at = _core.research_runtime_reducer.parse_time(created_at)
    except Exception:
        return False

    prior: list[dict[str, Any]] = []
    for candidate in reduced_task_events:
        candidate_meta = candidate.get(_core.GITHUB_META_KEY)
        candidate_id = (
            candidate_meta.get("comment_id") if isinstance(candidate_meta, dict) else None
        )
        if type(candidate_id) is int and candidate_id < comment_id:
            prior.append(candidate)
    try:
        prior_state = _core.research_runtime_reducer.reduce_task(
            task,
            prior,
            default_lease_minutes=90,
            now=event_at,
        )
    except Exception:
        return False
    return (
        prior_state.get("dispatch_state") == "LEASED"
        and prior_state.get("claim_id") == claim_id
    )


def _later_applied_event_exists(
    event: dict[str, Any],
    reduced_task_events: list[dict[str, Any]] | None,
    reducer_ignored_indices: set[int] | None,
) -> bool:
    if reduced_task_events is None:
        return False
    meta = event.get(_core.GITHUB_META_KEY)
    comment_id = meta.get("comment_id") if isinstance(meta, dict) else None
    if type(comment_id) is not int:
        return False
    ignored = reducer_ignored_indices or set()
    for reduced_index, reduced_event in enumerate(reduced_task_events):
        if reduced_index in ignored:
            continue
        reduced_meta = reduced_event.get(_core.GITHUB_META_KEY)
        reduced_comment_id = (
            reduced_meta.get("comment_id") if isinstance(reduced_meta, dict) else None
        )
        if type(reduced_comment_id) is int and reduced_comment_id > comment_id:
            return True
    return False


def _block_ambiguous_registered_handoff(
    task: dict[str, Any],
    state: dict[str, Any],
    authenticated: list[dict[str, Any]],
    registered_rejected: list[dict[str, Any]],
    result_state: dict[str, Any] | None,
    reduced_task_events: list[dict[str, Any]] | None = None,
    reducer_ignored_indices: set[int] | None = None,
) -> dict[str, Any]:
    if result_state is not None or state.get("dispatch_state") != "NEEDS_DISPATCH":
        return state
    for rejected in registered_rejected:
        reason = rejected.get("reason")
        if not isinstance(reason, str) or not reason.startswith(HANDOFF_SCOPE_REASON_PREFIX):
            continue
        index = rejected.get("index")
        if type(index) is not int or index < 0 or index >= len(authenticated):
            continue
        event = authenticated[index]
        if event.get("task_id") != task.get("task_id") or event.get("event") != "HANDOFF":
            continue
        if not _event_had_live_claim(task, event, reduced_task_events):
            continue
        if _later_applied_event_exists(
            event, reduced_task_events, reducer_ignored_indices
        ):
            continue
        meta = event.get(_core.GITHUB_META_KEY)
        value = copy.deepcopy(state)
        value["state"] = "BLOCKED"
        value["dispatch_state"] = "BLOCKED"
        value["hard_block"] = {
            "code": "REGISTERED_HANDOFF_SCOPE_REQUIRED",
            "publication_id": task.get("publication_id"),
            "claim_id": event.get("claim_id"),
            "server_comment_id": meta.get("comment_id") if isinstance(meta, dict) else None,
            "reason": reason,
        }
        value["next_action"] = (
            "Append a structurally scoped HANDOFF correction while the original owner "
            "lease is valid, or append an authorized lifecycle correction; do not "
            "redispatch this ambiguous handoff."
        )
        return value
    return state


def _block_unreviewed_registered_done(
    task: dict[str, Any],
    state: dict[str, Any],
    authenticated: list[dict[str, Any]],
    registered_rejected: list[dict[str, Any]],
    result_state: dict[str, Any] | None,
    reduced_task_events: list[dict[str, Any]] | None = None,
    reducer_ignored_indices: set[int] | None = None,
) -> dict[str, Any]:
    """Strengthen provisional terminal barriers with live-claim provenance."""
    terminal_reason = "registered DONE requires a frozen result with terminal Driver review"
    eligible_rejected: list[dict[str, Any]] = []
    for rejected in registered_rejected:
        if rejected.get("reason") != terminal_reason:
            eligible_rejected.append(rejected)
            continue
        index = rejected.get("index")
        if type(index) is not int or index < 0 or index >= len(authenticated):
            continue
        event = authenticated[index]
        if _event_had_live_claim(task, event, reduced_task_events):
            eligible_rejected.append(rejected)

    value = _ORIGINAL_BLOCK_UNREVIEWED_REGISTERED_DONE(
        task,
        state,
        authenticated,
        eligible_rejected,
        result_state,
        reduced_task_events,
        reducer_ignored_indices,
    )
    return _block_ambiguous_registered_handoff(
        task,
        value,
        authenticated,
        registered_rejected,
        result_state,
        reduced_task_events,
        reducer_ignored_indices,
    )


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


# Patch the preserved core because functions such as effective_states() resolve
# these helpers in the core module's global namespace. Then re-export the complete
# historical surface, including private helpers used by repository runtime guards.
_core._filter_registered_events = _filter_registered_events
_core._overlay_result_state = _overlay_result_state
_core._block_unreviewed_registered_done = _block_unreviewed_registered_done

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
