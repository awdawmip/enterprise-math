#!/usr/bin/env python3
"""Lane-scoped CLAIM authority for optional parallel execution cohorts.

This module deliberately leaves the ordinary task-level scheduler unchanged.
For an opt-in execution cohort it projects the authenticated Issue #240 event
stream onto exactly one `(task_id, cohort_id, lane_id)` fiber and then reuses the
existing scheduler reducer. Therefore each lane has its own first-valid CLAIM
race while unrelated lanes remain concurrent.
"""
from __future__ import annotations

import copy
import sys
from pathlib import Path
from typing import Any, Mapping

try:
    from tools import research_dispatch
    from tools import research_scheduler
    from tools import research_task_records
except ModuleNotFoundError:
    import research_dispatch  # type: ignore
    import research_scheduler  # type: ignore
    import research_task_records  # type: ignore

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
import research_execution_cohorts  # noqa: E402


class LaneClaimError(ValueError):
    pass


def _publication_record(
    task_id: str, publication_id: str, root: Path = ROOT
) -> dict[str, Any]:
    matches = [
        item
        for item in research_task_records.iter_records(root)
        if item.get("task_id") == task_id and item.get("publication_id") == publication_id
    ]
    if len(matches) != 1:
        raise LaneClaimError("lane publication is unknown or ambiguous for task")
    record = matches[0]
    if record.get("record_state", "ACTIVE") in research_task_records.TERMINAL_RECORD_STATES:
        raise LaneClaimError("lane publication record is terminal")
    if record.get("claimable") is not True:
        raise LaneClaimError("lane publication is not execution-eligible")
    return record


def lane_scope(
    task_id: str, cohort_id: str, lane_id: str, root: Path = ROOT
) -> dict[str, Any]:
    cohort = research_execution_cohorts.cohort_map(root).get(cohort_id)
    if cohort is None or cohort.get("task_id") != task_id:
        raise LaneClaimError("unknown execution cohort for task")
    if cohort.get("record_state") != "ACTIVE":
        raise LaneClaimError("execution cohort is not ACTIVE")
    matches = [
        item
        for item in cohort.get("lanes", [])
        if isinstance(item, dict) and item.get("lane_id") == lane_id
    ]
    if len(matches) != 1:
        raise LaneClaimError("unknown or ambiguous execution lane")
    lane = copy.deepcopy(matches[0])
    publication_id = lane.get("publication_id")
    if not isinstance(publication_id, str) or not publication_id:
        raise LaneClaimError("execution lane has no publication_id")
    prefix = lane.get("output_prefix")
    try:
        output_prefix = research_execution_cohorts._safe_prefix(prefix)
    except Exception as exc:
        raise LaneClaimError(f"execution lane output_prefix invalid: {exc}") from exc
    record = _publication_record(task_id, publication_id, root)
    return {
        "task_id": task_id,
        "execution_cohort_id": cohort_id,
        "execution_lane_id": lane_id,
        "publication_id": publication_id,
        "lane_role": lane.get("lane_role"),
        "purpose": lane.get("purpose"),
        "output_prefix": output_prefix,
        "publication_record": record,
    }


def _safe_output(value: Any) -> str | None:
    if not isinstance(value, str) or not value.strip():
        return None
    text = value.strip().replace("\\", "/")
    path = Path(text)
    if path.is_absolute() or ".." in path.parts:
        return None
    return text


def _outputs_within_prefix(outputs: Any, prefix: str) -> bool:
    if not isinstance(outputs, list) or not outputs:
        return False
    for value in outputs:
        text = _safe_output(value)
        if text is None or not text.startswith(prefix):
            return False
    return True


def _exact_lane_event(
    event: Mapping[str, Any], *, task_id: str, cohort_id: str, lane_id: str
) -> bool:
    return (
        event.get("task_id") == task_id
        and event.get("execution_cohort_id") == cohort_id
        and event.get("execution_lane_id") == lane_id
    )


def project_lane_events(
    events: list[dict[str, Any]], *, task_id: str, cohort_id: str, lane_id: str
) -> list[dict[str, Any]]:
    """Project a global event stream onto one exact execution lane."""
    return [
        copy.deepcopy(event)
        for event in events
        if _exact_lane_event(
            event,
            task_id=task_id,
            cohort_id=cohort_id,
            lane_id=lane_id,
        )
    ]


def reduce_lane(
    task_id: str,
    cohort_id: str,
    lane_id: str,
    events: list[dict[str, Any]],
    *,
    now,
    root: Path = ROOT,
) -> dict[str, Any]:
    """Reduce one lane independently from every other lane of the same task."""
    scope = lane_scope(task_id, cohort_id, lane_id, root)
    try:
        task = research_dispatch.registered_definition(scope["publication_record"], root)
    except Exception as exc:
        raise LaneClaimError(f"cannot construct lane task definition: {exc}") from exc

    projected = project_lane_events(
        events,
        task_id=task_id,
        cohort_id=cohort_id,
        lane_id=lane_id,
    )
    authenticated, auth_rejected = research_dispatch._event_authentication_filter(task, projected)
    accepted: list[dict[str, Any]] = []
    rejected: list[dict[str, Any]] = list(auth_rejected)
    for index, event in enumerate(authenticated):
        if event.get("event") == "CLAIM":
            normalized, reason = research_dispatch._inline_claim_envelope(task, event)
            if normalized is None:
                rejected.append(
                    {
                        "index": index,
                        "reason": reason or "lane CLAIM execution envelope is invalid",
                    }
                )
                continue
            if not _outputs_within_prefix(
                normalized.get("allowed_outputs"), scope["output_prefix"]
            ):
                rejected.append(
                    {
                        "index": index,
                        "reason": "lane CLAIM allowed_outputs escape lane output_prefix",
                    }
                )
                continue
            normalized["execution_cohort_id"] = cohort_id
            normalized["execution_lane_id"] = lane_id
            accepted.append(normalized)
            continue
        accepted.append(event)

    state = research_scheduler.reduce_task(
        task,
        accepted,
        default_lease_minutes=int(task.get("claim_lease_minutes") or 120),
        now=now,
    )
    state["ignored_events"].extend(rejected)
    state.update(
        {
            "execution_cohort_id": cohort_id,
            "execution_lane_id": lane_id,
            "lane_role": scope["lane_role"],
            "lane_publication_id": scope["publication_id"],
            "lane_output_prefix": scope["output_prefix"],
        }
    )
    return state


def winning_lane_claim_binding(
    task_id: str,
    cohort_id: str,
    lane_id: str,
    events: list[dict[str, Any]],
    *,
    now,
    root: Path = ROOT,
) -> dict[str, Any]:
    """Return the exact currently winning authorized CLAIM for one lane."""
    scope = lane_scope(task_id, cohort_id, lane_id, root)
    try:
        task = research_dispatch.registered_definition(scope["publication_record"], root)
    except Exception as exc:
        raise LaneClaimError(f"cannot construct lane task definition: {exc}") from exc
    projected = project_lane_events(
        events,
        task_id=task_id,
        cohort_id=cohort_id,
        lane_id=lane_id,
    )
    authenticated, _ = research_dispatch._event_authentication_filter(task, projected)
    valid_claims: list[dict[str, Any]] = []
    reducer_events: list[dict[str, Any]] = []
    for event in authenticated:
        if event.get("event") == "CLAIM":
            normalized, _ = research_dispatch._inline_claim_envelope(task, event)
            if normalized is None:
                continue
            if not _outputs_within_prefix(
                normalized.get("allowed_outputs"), scope["output_prefix"]
            ):
                continue
            normalized["execution_cohort_id"] = cohort_id
            normalized["execution_lane_id"] = lane_id
            valid_claims.append(normalized)
            reducer_events.append(normalized)
        else:
            reducer_events.append(event)
    reduced = research_scheduler.reduce_task(
        task,
        reducer_events,
        default_lease_minutes=int(task.get("claim_lease_minutes") or 120),
        now=now,
    )
    claim_id = reduced.get("claim_id")
    if reduced.get("dispatch_state") != "LEASED" or not isinstance(claim_id, str):
        raise LaneClaimError("execution lane requires a current winning live CLAIM")
    matches = [event for event in valid_claims if event.get("claim_id") == claim_id]
    if not matches:
        raise LaneClaimError("lane owner state has no accepted CLAIM provenance")
    claim = matches[-1]
    meta = claim.get(research_dispatch.GITHUB_META_KEY)
    if not isinstance(meta, Mapping) or meta.get("control_authorized") is not True:
        raise LaneClaimError("winning lane CLAIM lacks authorized GitHub control provenance")
    return {
        "task_id": task_id,
        "publication_id": scope["publication_id"],
        "taskbook_blob_sha1": task.get("taskbook_blob_sha1"),
        "execution_cohort_id": cohort_id,
        "execution_lane_id": lane_id,
        "lane_role": scope["lane_role"],
        "lane_output_prefix": scope["output_prefix"],
        "claim_id": claim_id,
        "researcher_id": reduced.get("researcher_id"),
        "theorem_owner": claim.get("theorem_owner"),
        "execution_branch": claim.get("execution_branch"),
        "execution_branch_base": claim.get("execution_branch_base"),
        "allowed_outputs": copy.deepcopy(claim.get("allowed_outputs")),
        "owner_lease_until": reduced.get("lease_until"),
        "server_comment_id": meta.get("comment_id"),
        "server_author_login": meta.get("author_login"),
        "server_author_user_id": meta.get("author_user_id"),
        "binding_source": "CURRENT_AUTHORIZED_WINNING_ISSUE_240_LANE_CLAIM",
    }
