#!/usr/bin/env python3
"""Pure V2 runtime event reducer.

Task definitions come from immutable V2 publication records.  This module only
reduces already-authenticated Issue #240 events and derives stable execution
identity.  It owns no task table, legacy baseline, publication authority, or
mathematical status.
"""
from __future__ import annotations

import copy
import hashlib
import json
import pathlib
import re
from datetime import datetime, timedelta, timezone
from typing import Any, Iterable

ROOT = pathlib.Path(__file__).resolve().parents[1]
POLICY_PATH = ROOT / "research_runtime_policy_v2.json"
HARD_BLOCK_FIELDS = ("missing_object", "owner", "necessity", "unblock_condition")
RESEARCHER_ID_RE = re.compile(r"^EM-[A-Z0-9]+-(?:[0-9]{2}|[A-Z0-9]{4,8})$")
TASK_LANE_RE = re.compile(r"^RS-((?:R|P)\d{3}[A-Z]?)\b")
LANE_RE = re.compile(r"[^A-Z0-9]+")
EVENT_SCHEMA = "ENTERPRISE_MATH_SCHEDULER_EVENT_V1"
POLICY_SCHEMA = "ENTERPRISE_MATH_RESEARCH_RUNTIME_POLICY_V2"
DRIVER_REVIEW_TERMINAL_SCOPE = "RESEARCH_RETURN_FROZEN_AWAITING_DRIVER_REVIEW"
HANDOFF_SCOPE_CONTINUATION = "CONTINUATION"
HANDOFF_SCOPE_FROZEN_RETURN = "FROZEN_RETURN_AWAITING_DRIVER_REVIEW"
# Forward enforcement clock; historical owner races before this remain replayable.
LEGACY_HANDOFF_SCOPE_CUTOVER = datetime(2026, 9, 17, 4, 0, tzinfo=timezone.utc)
HANDOFF_SCOPE_RECONCILIATION = "RECONCILE_HANDOFF_SCOPE"
LEGACY_DRIVER_REVIEW_TERMINAL_CANDIDATES = {
    "SUCCESS_REVIEW_COMPLETE_AWAITING_DRIVER_DECISION",
}

class RuntimeReducerError(ValueError):
    pass


def load_json(path: pathlib.Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def parse_time(value: str) -> datetime:
    normalized = value.strip().replace("Z", "+00:00")
    dt = datetime.fromisoformat(normalized)
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc)


def now_utc(value: str | None) -> datetime:
    return parse_time(value) if value else datetime.now(timezone.utc)


def complete_hard_block(value: Any) -> bool:
    return isinstance(value, dict) and all(
        isinstance(value.get(field), str) and value[field].strip()
        for field in HARD_BLOCK_FIELDS
    )


def normalize_lane(value: str) -> str:
    lane = LANE_RE.sub("", value.strip().upper())
    if not lane:
        raise RuntimeReducerError("identity_lane must contain an alphanumeric character")
    return lane[:16]


def identity_lane(task: dict[str, Any]) -> str:
    explicit = task.get("identity_lane")
    if isinstance(explicit, str) and explicit.strip():
        return normalize_lane(explicit)
    task_id = str(task.get("task_id", "")).strip().upper()
    match = TASK_LANE_RE.match(task_id)
    if match:
        return normalize_lane(match.group(1))
    if task_id.startswith("RS-"):
        task_id = task_id[3:]
    first = task_id.split("-", 1)[0]
    return normalize_lane(first or "DIRECT")


def valid_researcher_id(value: Any) -> bool:
    return isinstance(value, str) and bool(RESEARCHER_ID_RE.fullmatch(value.strip().upper()))


def researcher_id_for_claim(task: dict[str, Any], claim_id: str) -> str:
    lane = identity_lane(task)
    digest = hashlib.sha256(f"{task['task_id']}\0{claim_id}".encode("utf-8")).hexdigest()[:6].upper()
    return f"EM-{lane}-{digest}"


def release_claim_identity(state: dict[str, Any]) -> None:
    if state.get("researcher_id"):
        state["last_researcher_id"] = state["researcher_id"]
    state["researcher_id"] = None
    state["identity_source"] = None


def validate_scheduler(config: dict[str, Any], owners: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if config.get("schema") != "ENTERPRISE_MATH_RESEARCH_SCHEDULER_V1":
        errors.append("unexpected scheduler schema")

    task_states = set(config.get("task_states", []))
    event_types = set(config.get("event_types", []))
    if not {"READY", "HANDOFF_READY", "BLOCKED", "DONE", "SUPERSEDED"} <= task_states:
        errors.append("scheduler task_states are incomplete")
    if not {"CLAIM", "HEARTBEAT", "PROGRESS", "HANDOFF", "HARD_BLOCK", "UNBLOCK", "DONE", "SUPERSEDE"} <= event_types:
        errors.append("scheduler event_types are incomplete")

    owner_entries = owners.get("branches", {})
    active_owners = {
        name for name, spec in owner_entries.items()
        if spec.get("state") in ACTIVE_OWNER_STATES
    }

    tasks = config.get("tasks", [])
    seen: set[str] = set()
    covered_active: set[str] = set()
    priorities = set(config.get("selection_policy", {}).get("priority_order", []))
    leverage = set(config.get("selection_policy", {}).get("leverage_order", []))

    for index, task in enumerate(tasks):
        prefix = f"tasks[{index}]"
        task_id = task.get("task_id")
        if not isinstance(task_id, str) or not task_id:
            errors.append(f"{prefix}: missing task_id")
            continue
        if task_id in seen:
            errors.append(f"duplicate task_id: {task_id}")
        seen.add(task_id)

        if "identity_lane" in task:
            try:
                identity_lane(task)
            except RuntimeReducerError as exc:
                errors.append(f"{task_id}: {exc}")

        state = task.get("base_state")
        if state not in task_states:
            errors.append(f"{task_id}: invalid base_state {state!r}")
        if task.get("priority") not in priorities:
            errors.append(f"{task_id}: invalid priority {task.get('priority')!r}")
        if task.get("leverage") not in leverage:
            errors.append(f"{task_id}: invalid leverage {task.get('leverage')!r}")

        owner = task.get("owner")
        if task.get("kind") == "RESEARCH":
            if owner not in active_owners:
                errors.append(f"{task_id}: research owner is not ACTIVE_OWNER/ACTIVE_BRIDGE: {owner!r}")
            else:
                covered_active.add(owner)
        elif task.get("kind") == "GOVERNANCE":
            if owner != "governance":
                errors.append(f"{task_id}: governance task must use owner='governance'")
        else:
            errors.append(f"{task_id}: invalid task kind {task.get('kind')!r}")

        hard_block = task.get("hard_block")
        if hard_block is not None and not complete_hard_block(hard_block):
            errors.append(f"{task_id}: partial hard_block is invalid")
        if state == "BLOCKED" and not complete_hard_block(hard_block):
            errors.append(f"{task_id}: BLOCKED requires a complete hard_block")

        for dep_index, dependency in enumerate(task.get("dependencies", [])):
            action = dependency.get("action")
            if action not in DEPENDENCY_ACTIONS:
                errors.append(f"{task_id}: dependency[{dep_index}] has invalid action {action!r}")

        for field in ("frontier", "next_action", "last_progress_at"):
            if not isinstance(task.get(field), str) or not task[field].strip():
                errors.append(f"{task_id}: missing {field}")

        if isinstance(task.get("last_progress_at"), str):
            try:
                parse_time(task["last_progress_at"])
            except (TypeError, ValueError):
                errors.append(f"{task_id}: invalid last_progress_at")

    missing_coverage = sorted(active_owners - covered_active)
    if missing_coverage:
        errors.append("active research owners missing scheduler coverage: " + ", ".join(missing_coverage))

    unknown_covered = sorted(covered_active - active_owners)
    if unknown_covered:
        errors.append("scheduler covers non-active owners: " + ", ".join(unknown_covered))

    return errors


def load_events(path: pathlib.Path | None) -> list[dict[str, Any]]:
    if path is None:
        return []
    text = path.read_text(encoding="utf-8").strip()
    if not text:
        return []
    if text.startswith("["):
        data = json.loads(text)
        if not isinstance(data, list):
            raise RuntimeReducerError("event JSON must be an array")
        events = data
    else:
        events = [json.loads(line) for line in text.splitlines() if line.strip()]
    for index, event in enumerate(events):
        if not isinstance(event, dict):
            raise RuntimeReducerError(f"event {index} is not an object")
    return events


def lease_duration(event: dict[str, Any], default_minutes: int) -> timedelta:
    minutes = event.get("lease_minutes", default_minutes)
    if not isinstance(minutes, int) or minutes <= 0:
        raise RuntimeReducerError("lease_minutes must be a positive integer")
    return timedelta(minutes=minutes)


def event_time(event: dict[str, Any]) -> datetime:
    value = event.get("at")
    if not isinstance(value, str) or not value:
        raise RuntimeReducerError("scheduler event requires ISO-8601 'at'")
    return parse_time(value)


def state_from_task(task: dict[str, Any]) -> dict[str, Any]:
    return {
        "task_id": task["task_id"],
        "state": task["base_state"],
        "claim_id": None,
        "actor": None,
        "researcher_id": None,
        "last_researcher_id": None,
        "identity_source": None,
        "lease_until": None,
        "hard_block": copy.deepcopy(task.get("hard_block")),
        "last_progress_ref": task.get("last_progress_ref"),
        "last_progress_at": task.get("last_progress_at"),
        "next_action": task.get("next_action"),
        "ignored_events": [],
    }


def expire_claim(state: dict[str, Any], at: datetime) -> None:
    lease_until = state.get("lease_until")
    if state.get("claim_id") and isinstance(lease_until, datetime) and at >= lease_until:
        state["state"] = "HANDOFF_READY"
        state["claim_id"] = None
        state["actor"] = None
        release_claim_identity(state)
        state["lease_until"] = None


def ignore(state: dict[str, Any], index: int, reason: str) -> None:
    state["ignored_events"].append({"index": index, "reason": reason})


def live_claim_event_reason(state: dict[str, Any], event: dict[str, Any]) -> str | None:
    """Share the reducer's claim and optional researcher identity boundary."""
    kind = event.get("event")
    live_claim = state.get("claim_id")
    if not live_claim or event.get("claim_id") != live_claim:
        return f"{kind} requires the current live claim_id"
    event_researcher_id = event.get("researcher_id")
    if event_researcher_id is not None:
        if not valid_researcher_id(event_researcher_id):
            return f"{kind} researcher_id has invalid format"
        if event_researcher_id.strip().upper() != state.get("researcher_id"):
            return f"{kind} researcher_id does not match live claim identity"
    return None



def _handoff_obligation(
    task: dict[str, Any], state: dict[str, Any], event: dict[str, Any] | None = None,
) -> dict[str, Any] | None:
    """Retain scope uncertainty, not a prose-inferred review/terminal verdict."""
    if task.get("registration_source") != "IMMUTABLE_TASK_RECORD":
        return None
    if event is None and not (
        task.get("base_state") == "HANDOFF_READY"
        and task.get("evidence_status") == "LEGACY_CONTROL_MIGRATED_HANDOFF_READY"
    ):
        return None
    meta = event.get("_github", {}) if event is not None else {}
    return {
        "progress_ref": state.get("last_progress_ref"),
        "progress_at": state.get("last_progress_at"),
        "server_comment_id": meta.get("comment_id"),
    }


def _handoff_reconciliation_reason(
    task: dict[str, Any], state: dict[str, Any], event: dict[str, Any],
    obligation: dict[str, Any] | None, at: datetime,
) -> str | None:
    """Validate a claimless, exact-frontier annotation; never grant Result authority.

    The authorized source author attests the evidence binding. This pure reducer
    checks its shape and immutable address, not remote bytes or mathematics.
    """
    prefix = "RECONCILE_HANDOFF_SCOPE: "
    meta = event.get("_github")
    if not isinstance(meta, dict) or not (
        meta.get("server_authenticated") is True
        and meta.get("control_authorized") is True
        and meta.get("issue_number") == 240
        and type(meta.get("comment_id")) is int
        and meta["comment_id"] > 0
        and meta.get("edited") is False
    ):
        return prefix + "requires the authorized unedited Issue 240 server envelope"
    if task.get("registration_source") != "IMMUTABLE_TASK_RECORD":
        return prefix + "requires an operational immutable task publication"
    if event.get("publication_id") != task.get("publication_id") or not task.get("publication_id"):
        return prefix + "publication_id mismatch"
    if event.get("taskbook_blob_sha1") != task.get("taskbook_blob_sha1") or not task.get("taskbook_blob_sha1"):
        return prefix + "taskbook blob mismatch"
    try:
        published = parse_time(task["publication_published_at"])
        server_at = parse_time(meta["created_at"])
    except (KeyError, TypeError, AttributeError, ValueError):
        return prefix + "requires current publication and server clocks"
    if at != server_at or at < published:
        return prefix + "server time precedes current publication or differs from reducer clock"
    if state.get("claim_id") or state.get("state") != "HANDOFF_READY" or state.get("hard_block"):
        return prefix + "cannot replace a live owner, hard block or terminal/frozen state"
    if obligation is None or event.get("source_handoff") != obligation:
        return prefix + "source frontier mismatch or scope already resolved"
    if event.get("handoff_scope") not in {HANDOFF_SCOPE_CONTINUATION, HANDOFF_SCOPE_FROZEN_RETURN}:
        return prefix + "requires explicit continuation or frozen-return scope"
    forbidden = {"result_id", "review_id", "driver_disposition", "terminal_verdict",
                 "claim_id", "researcher_id", "execution_cohort_id", "execution_lane_id",
                 "terminal_scope", "terminal_candidate"}
    if forbidden.intersection(event):
        return prefix + "must not create execution, review, Result or terminal authority"
    evidence = event.get("source_evidence")
    if not isinstance(evidence, dict) or set(evidence) != {
        "repository", "commit", "path", "git_blob_sha1", "sha256"
    }:
        return prefix + "requires exact immutable source evidence"
    if evidence["repository"] != "awdawmip/enterprise-math":
        return prefix + "wrong source repository"
    for key, size in (("commit", 40), ("git_blob_sha1", 40), ("sha256", 64)):
        if not isinstance(evidence[key], str) or not re.fullmatch("[0-9a-f]{%d}" % size, evidence[key]):
            return prefix + "invalid source " + key
    path = evidence["path"]
    if not isinstance(path, str) or not path or any(
        part in {"", ".", ".."} for part in path.split("/")
    ) or any(c in path for c in "\\:#?%"):
        return prefix + "invalid source path"
    url = "https://github.com/awdawmip/enterprise-math/blob/" + evidence["commit"] + "/" + path
    if event.get("progress_ref") != url:
        return prefix + "progress_ref must equal the exact immutable source URL"
    if not isinstance(event.get("next_action"), str) or not event["next_action"].strip():
        return prefix + "requires next_action"
    return None


def _project_unresolved_handoff(
    task: dict[str, Any], state: dict[str, Any], obligation: dict[str, Any] | None,
) -> None:
    if obligation is None or state["state"] != "HANDOFF_READY" or state.get("claim_id"):
        return
    state["state"] = "BLOCKED"
    state["hard_block"] = {
        "code": "LEGACY_HANDOFF_SCOPE_UNRESOLVED",
        "publication_id": task.get("publication_id"),
        "taskbook_blob_sha1": task.get("taskbook_blob_sha1"),
        "source_handoff": copy.deepcopy(obligation),
        "missing_object": "an explicit continuation versus frozen-return scope for this exact frontier",
        "owner": "control-plane/handoff-scope-reconciliation",
        "necessity": "An untyped old handoff must not silently redispatch completed research.",
        "unblock_condition": "Append an authorized exact-frontier RECONCILE_HANDOFF_SCOPE event with verified immutable source evidence, or consume the ordinary Result/review lifecycle.",
    }
    state["next_action"] = (
        "Reconcile the exact legacy handoff scope without a new research CLAIM; "
        "do not infer completion or review acceptance from prose."
    )


def reduce_task(
    task: dict[str, Any],
    events: Iterable[dict[str, Any]],
    *,
    default_lease_minutes: int,
    now: datetime,
) -> dict[str, Any]:
    state = state_from_task(task)
    scope_obligation = _handoff_obligation(task, state)
    # Supplied only by the canonical operational Result adapter, never task JSON.
    review_reopen = task.get("_handoff_scope_review_reopened_at")
    review_reopen_at = parse_time(review_reopen) if isinstance(review_reopen, str) else None
    review_reopen_consumed = False
    matching = [event for event in events if event.get("task_id") == task["task_id"]]

    last_event_time: datetime | None = None
    for index, event in enumerate(matching):
        if event.get("schema") not in (None, "ENTERPRISE_MATH_SCHEDULER_EVENT_V1"):
            ignore(state, index, "wrong event schema")
            continue
        try:
            at = event_time(event)
        except (RuntimeReducerError, ValueError) as exc:
            ignore(state, index, str(exc))
            continue
        if last_event_time is not None and at < last_event_time:
            ignore(state, index, "events must be supplied in GitHub comment order / nondecreasing event time")
            continue
        last_event_time = at
        expire_claim(state, at)
        if review_reopen_at is not None and not review_reopen_consumed and at >= review_reopen_at:
            scope_obligation = None
            review_reopen_consumed = True

        kind = event.get("event")
        claim_id = event.get("claim_id")
        live_claim = state.get("claim_id")

        if kind == HANDOFF_SCOPE_RECONCILIATION:
            reason = _handoff_reconciliation_reason(task, state, event, scope_obligation, at)
            if reason is not None:
                ignore(state, index, reason)
                continue
            state["handoff_scope_reconciliation"] = {
                "server_comment_id": event["_github"]["comment_id"],
                "source_handoff": copy.deepcopy(scope_obligation),
                "source_evidence": copy.deepcopy(event["source_evidence"]),
            }
            state["handoff_scope"] = event["handoff_scope"]
            state["state"] = (
                "FROZEN_RETURN" if event["handoff_scope"] == HANDOFF_SCOPE_FROZEN_RETURN
                else "HANDOFF_READY"
            )
            state["last_progress_ref"] = event["progress_ref"]
            state["last_progress_at"] = event["at"]
            state["next_action"] = event["next_action"]
            scope_obligation = None
            continue

        if kind == "CLAIM":
            if scope_obligation is not None and at >= LEGACY_HANDOFF_SCOPE_CUTOVER:
                ignore(state, index, "CLAIM requires reconciliation of the unresolved legacy handoff scope")
                continue
            if state["state"] not in {"READY", "HANDOFF_READY"} or live_claim:
                ignore(state, index, "task is not dispatchable")
                continue
            if not isinstance(claim_id, str) or not claim_id:
                ignore(state, index, "CLAIM requires claim_id")
                continue
            supplied_researcher_id = event.get("researcher_id")
            if supplied_researcher_id is not None and not valid_researcher_id(supplied_researcher_id):
                ignore(state, index, "CLAIM researcher_id has invalid format")
                continue
            researcher_id = (
                supplied_researcher_id.strip().upper()
                if isinstance(supplied_researcher_id, str)
                else researcher_id_for_claim(task, claim_id)
            )
            try:
                duration = lease_duration(event, default_lease_minutes)
            except RuntimeReducerError as exc:
                ignore(state, index, str(exc))
                continue
            state["state"] = "CLAIMED"
            state["claim_id"] = claim_id
            state["actor"] = event.get("actor")
            state["researcher_id"] = researcher_id
            state["last_researcher_id"] = researcher_id
            state["identity_source"] = "EVENT" if supplied_researcher_id is not None else "AUTO_CLAIM_DERIVED"
            state["lease_until"] = at + duration
            continue

        if kind in {"HEARTBEAT", "PROGRESS", "HANDOFF", "HARD_BLOCK", "DONE"}:
            reason = live_claim_event_reason(state, event)
            if reason is not None:
                ignore(state, index, reason)
                continue

        if kind == "HEARTBEAT":
            try:
                state["lease_until"] = at + lease_duration(event, default_lease_minutes)
            except RuntimeReducerError as exc:
                ignore(state, index, str(exc))
            continue

        if kind == "PROGRESS":
            try:
                state["lease_until"] = at + lease_duration(event, default_lease_minutes)
            except RuntimeReducerError as exc:
                ignore(state, index, str(exc))
                continue
            if event.get("progress_ref") and event["progress_ref"] != state.get("last_progress_ref"):
                scope_obligation = None
            state["state"] = "IN_PROGRESS"
            if event.get("progress_ref"):
                state["last_progress_ref"] = event["progress_ref"]
            state["last_progress_at"] = event["at"]
            if event.get("next_action"):
                state["next_action"] = event["next_action"]
            continue

        if kind == "HANDOFF":
            next_action = event.get("next_action")
            if not isinstance(next_action, str) or not next_action.strip():
                ignore(state, index, "HANDOFF requires next_action")
                continue
            result_id = event.get("result_id")
            if result_id is not None and (not isinstance(result_id, str) or not result_id.strip()):
                ignore(state, index, "HANDOFF result_id must be a nonempty string when supplied")
                continue
            terminal_scope = event.get("terminal_scope")
            if terminal_scope is not None and not isinstance(terminal_scope, str):
                ignore(state, index, "HANDOFF terminal_scope must be a string when supplied")
                continue
            handoff_scope = event.get("handoff_scope")
            if handoff_scope is not None and (
                not isinstance(handoff_scope, str)
                or handoff_scope not in {HANDOFF_SCOPE_CONTINUATION, HANDOFF_SCOPE_FROZEN_RETURN}
            ):
                ignore(state, index, "HANDOFF handoff_scope is invalid")
                continue
            legacy_terminal_candidate = event.get("terminal_candidate")
            if legacy_terminal_candidate is not None and not isinstance(legacy_terminal_candidate, str):
                ignore(state, index, "HANDOFF terminal_candidate must be a string when supplied")
                continue
            driver_review_terminal = (
                terminal_scope == DRIVER_REVIEW_TERMINAL_SCOPE
                or handoff_scope == HANDOFF_SCOPE_FROZEN_RETURN
                or legacy_terminal_candidate in LEGACY_DRIVER_REVIEW_TERMINAL_CANDIDATES
            )
            if handoff_scope == HANDOFF_SCOPE_CONTINUATION and (
                result_id is not None or driver_review_terminal
            ):
                ignore(state, index, "HANDOFF CONTINUATION scope contradicts frozen-return marker")
                continue
            # Terminality is machine-explicit. Natural-language fields never decide it.
            state["state"] = (
                "FROZEN_RETURN"
                if result_id is not None or driver_review_terminal
                else "HANDOFF_READY"
            )
            if isinstance(result_id, str):
                state["result_id"] = result_id.strip()
            else:
                state.pop("result_id", None)
            if terminal_scope == DRIVER_REVIEW_TERMINAL_SCOPE:
                state["terminal_scope"] = DRIVER_REVIEW_TERMINAL_SCOPE
            else:
                state.pop("terminal_scope", None)
            if handoff_scope in {HANDOFF_SCOPE_CONTINUATION, HANDOFF_SCOPE_FROZEN_RETURN}:
                state["handoff_scope"] = handoff_scope
            else:
                state.pop("handoff_scope", None)
            if legacy_terminal_candidate in LEGACY_DRIVER_REVIEW_TERMINAL_CANDIDATES:
                state["terminal_candidate"] = legacy_terminal_candidate
            else:
                state.pop("terminal_candidate", None)
            if event.get("progress_ref"):
                state["last_progress_ref"] = event["progress_ref"]
            state["last_progress_at"] = event["at"]
            state["next_action"] = next_action
            scope_obligation = (
                _handoff_obligation(task, state, event)
                if state["state"] == "HANDOFF_READY" and handoff_scope is None
                else None
            )
            state["claim_id"] = None
            state["actor"] = None
            release_claim_identity(state)
            state["lease_until"] = None
            continue

        if kind == "HARD_BLOCK":
            hard_block = event.get("hard_block")
            if not complete_hard_block(hard_block):
                ignore(state, index, "HARD_BLOCK requires all four hard-block fields")
                continue
            scope_obligation = None
            state["state"] = "BLOCKED"
            state["hard_block"] = copy.deepcopy(hard_block)
            state["last_progress_at"] = event["at"]
            if event.get("progress_ref"):
                state["last_progress_ref"] = event["progress_ref"]
            state["claim_id"] = None
            state["actor"] = None
            release_claim_identity(state)
            state["lease_until"] = None
            continue

        if kind == "UNBLOCK":
            if state["state"] != "BLOCKED":
                ignore(state, index, "UNBLOCK requires BLOCKED state")
                continue
            state["state"] = "HANDOFF_READY"
            state["hard_block"] = None
            state["last_progress_at"] = event["at"]
            if event.get("next_action"):
                state["next_action"] = event["next_action"]
            continue

        if kind == "DONE":
            state["state"] = "DONE"
            if event.get("progress_ref"):
                state["last_progress_ref"] = event["progress_ref"]
            state["last_progress_at"] = event["at"]
            state["claim_id"] = None
            state["actor"] = None
            release_claim_identity(state)
            state["lease_until"] = None
            continue

        if kind == "SUPERSEDE":
            state["state"] = "SUPERSEDED"
            state["hard_block"] = None
            state["claim_id"] = None
            state["actor"] = None
            release_claim_identity(state)
            state["lease_until"] = None
            if event.get("progress_ref"):
                state["last_progress_ref"] = event["progress_ref"]
            state["last_progress_at"] = event["at"]
            if event.get("next_action"):
                state["next_action"] = event["next_action"]
            continue

        ignore(state, index, f"unknown event type: {kind!r}")

    expire_claim(state, now)
    _project_unresolved_handoff(task, state, scope_obligation)
    state["lease_until"] = state["lease_until"].isoformat() if isinstance(state.get("lease_until"), datetime) else None

    if state["state"] in {"DONE", "SUPERSEDED"}:
        state["dispatch_state"] = "COMPLETE"
    elif state["state"] == "BLOCKED" and complete_hard_block(state.get("hard_block")):
        state["dispatch_state"] = "BLOCKED"
    elif state["state"] == "FROZEN_RETURN":
        state["dispatch_state"] = "AWAITING_REVIEW"
    elif state.get("claim_id"):
        state["dispatch_state"] = "LEASED"
    elif state["state"] in {"READY", "HANDOFF_READY"}:
        state["dispatch_state"] = "NEEDS_DISPATCH"
    else:
        state["dispatch_state"] = "DORMANT"
    return state



def validate_policy(policy: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if policy.get("schema") != POLICY_SCHEMA:
        errors.append("unexpected V2 runtime-policy schema")
    if policy.get("status") != "ACTIVE_CANONICAL":
        errors.append("V2 runtime policy must be ACTIVE_CANONICAL")
    if policy.get("task_definition_source") != "IMMUTABLE_V2_TASK_PUBLICATIONS":
        errors.append("runtime policy task source must be immutable V2 publications")
    if policy.get("event_schema") != EVENT_SCHEMA:
        errors.append("runtime policy event schema mismatch")
    lease = policy.get("default_claim_lease_minutes")
    if type(lease) is not int or lease <= 0:
        errors.append("default_claim_lease_minutes must be positive integer")
    selection = policy.get("selection_policy")
    if not isinstance(selection, dict):
        errors.append("selection_policy must be an object")
    else:
        for field in ("state_order", "priority_order", "leverage_order"):
            value = selection.get(field)
            if not isinstance(value, list) or not value or any(not isinstance(x, str) for x in value):
                errors.append(f"selection_policy.{field} must be a nonempty string list")
    if policy.get("legacy_task_definition_source") is not None:
        errors.append("legacy task-definition source must be null after cutover")
    return errors


def load_policy(root: pathlib.Path = ROOT) -> dict[str, Any]:
    policy = load_json(root / "research_runtime_policy_v2.json")
    errors = validate_policy(policy)
    if errors:
        raise RuntimeReducerError("invalid V2 runtime policy: " + "; ".join(errors))
    return policy


def select_state(
    states: Iterable[dict[str, Any]],
    policy: dict[str, Any],
    *,
    kind: str = "RESEARCH",
) -> dict[str, Any] | None:
    selection = policy["selection_policy"]
    state_rank = {name: index for index, name in enumerate(selection["state_order"])}
    priority_rank = {name: index for index, name in enumerate(selection["priority_order"])}
    leverage_rank = {name: index for index, name in enumerate(selection["leverage_order"])}
    candidates = [
        value for value in states
        if value.get("dispatch_state") == "NEEDS_DISPATCH"
        and (kind == "ANY" or value.get("kind") == kind)
    ]
    if not candidates:
        return None

    def key(value: dict[str, Any]) -> tuple[Any, ...]:
        try:
            last = parse_time(str(value.get("last_progress_at") or ""))
        except Exception:
            last = datetime(1970, 1, 1, tzinfo=timezone.utc)
        return (
            state_rank.get(value.get("state"), len(state_rank)),
            priority_rank.get(value.get("priority"), len(priority_rank)),
            leverage_rank.get(value.get("leverage"), len(leverage_rank)),
            last,
            value.get("task_id", ""),
        )

    return min(candidates, key=key)
