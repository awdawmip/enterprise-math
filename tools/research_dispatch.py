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
   generation it was prepared for.  Intent-backed CLAIMs are normalized to that
   current publication and cannot use an old intent to cross a V2 generation;
5. current-publication authority cannot predate its immutable publication; and
6. typed HANDOFF and provisional terminal barriers require the appropriate live claim.

The preserved core remains fail-closed: runtime input must be raw authenticated
Issue #240 comment objects. No priority, lease duration, Driver disposition,
terminalization, or task-selection policy is changed here.
"""
from __future__ import annotations

import copy
from datetime import datetime, timezone
from contextlib import contextmanager
from control_plane import research_result_authority_fault_isolation as _result_authority
from pathlib import Path
from typing import Any

from tools import research_dispatch_core as _core

ROOT = _core.ROOT
DispatchError = _core.DispatchError

_ORIGINAL_REGISTERED_DEFINITION = _core.registered_definition
_ORIGINAL_OVERLAY_RESULT_STATE = _core._overlay_result_state
_ORIGINAL_OVERLAY_ACTIVE_COHORT = _core._overlay_active_cohort
_ORIGINAL_RESULT_SNAPSHOT = _core._dispatch_result_read_snapshot
_ORIGINAL_FILTER_REGISTERED_EVENTS = _core._filter_registered_events
_ORIGINAL_BLOCK_UNREVIEWED_REGISTERED_DONE = _core._block_unreviewed_registered_done
_AUTO_RESULT_STATE = object()

# PR1360 froze this compatibility boundary from its recorded pre-deployment audit.
HANDOFF_SCOPE_CUTOVER = datetime(2026, 9, 7, 2, 20, tzinfo=timezone.utc)
HANDOFF_SCOPE_CONTINUATION = "CONTINUATION"
HANDOFF_SCOPE_FROZEN_RETURN = "FROZEN_RETURN_AWAITING_DRIVER_REVIEW"
DRIVER_REVIEW_TERMINAL_SCOPE = "RESEARCH_RETURN_FROZEN_AWAITING_DRIVER_REVIEW"
HANDOFF_SCOPE_REASON_PREFIX = "registered HANDOFF scope contract:"


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
    if handoff_scope is not None and (
        not isinstance(handoff_scope, str)
        or handoff_scope not in {HANDOFF_SCOPE_CONTINUATION, HANDOFF_SCOPE_FROZEN_RETURN}
    ):
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
    task: dict[str, Any],
    events: list[dict[str, Any]],
    accepted: list[dict[str, Any]],
    rejected: list[dict[str, Any]],
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    if not _core._is_registered(task):
        return accepted, rejected
    kept: list[dict[str, Any]] = []
    extra_rejected = list(rejected)
    for event in accepted:
        if event.get("task_id") != task["task_id"]:
            kept.append(event)
            continue
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
    """Compose lifecycle, intent, publication time, typed HANDOFF and held gates."""
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
    accepted, rejected = _enforce_publication_event_causality(task, events, accepted, rejected)
    accepted, rejected = _enforce_registered_handoff_scopes(task, events, accepted, rejected)
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


def _event_had_live_claim(
    task: dict[str, Any],
    event: dict[str, Any],
    reduced_task_events: list[dict[str, Any]] | None,
    *,
    resolved_lease_minutes: int | None = None,
) -> bool:
    """Whether a rejected terminal event belonged to the live claim at event time."""
    if reduced_task_events is None:
        # Direct legacy callers lack replay context; preserve conservative behavior.
        return True
    if resolved_lease_minutes is None:
        raise DispatchError("live-claim replay requires the dispatch resolved lease")
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
            default_lease_minutes=resolved_lease_minutes,
            now=event_at,
        )
    except Exception:
        return False
    return (
        prior_state.get("dispatch_state") == "LEASED"
        and _core.research_runtime_reducer.live_claim_event_reason(prior_state, event) is None
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
    *,
    resolved_lease_minutes: int | None = None,
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
        if not _event_had_live_claim(
            task, event, reduced_task_events, resolved_lease_minutes=resolved_lease_minutes
        ):
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
    *,
    resolved_lease_minutes: int | None = None,
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
        if _event_had_live_claim(
            task, event, reduced_task_events, resolved_lease_minutes=resolved_lease_minutes
        ):
            eligible_rejected.append(rejected)

    value = _ORIGINAL_BLOCK_UNREVIEWED_REGISTERED_DONE(
        task,
        state,
        authenticated,
        eligible_rejected,
        result_state,
        reduced_task_events,
        reducer_ignored_indices,
        resolved_lease_minutes=resolved_lease_minutes,
    )
    return _block_ambiguous_registered_handoff(
        task,
        value,
        authenticated,
        registered_rejected,
        result_state,
        reduced_task_events,
        reducer_ignored_indices,
        resolved_lease_minutes=resolved_lease_minutes,
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
_core.registered_definition = registered_definition
_core._filter_registered_events = _filter_registered_events
_core._block_unreviewed_registered_done = _block_unreviewed_registered_done
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
