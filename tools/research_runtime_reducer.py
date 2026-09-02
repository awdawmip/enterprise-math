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


def reduce_task(
    task: dict[str, Any],
    events: Iterable[dict[str, Any]],
    *,
    default_lease_minutes: int,
    now: datetime,
) -> dict[str, Any]:
    state = state_from_task(task)
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

        kind = event.get("event")
        claim_id = event.get("claim_id")
        live_claim = state.get("claim_id")

        if kind == "CLAIM":
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
            if not live_claim or claim_id != live_claim:
                ignore(state, index, f"{kind} requires the current live claim_id")
                continue
            event_researcher_id = event.get("researcher_id")
            if event_researcher_id is not None:
                if not valid_researcher_id(event_researcher_id):
                    ignore(state, index, f"{kind} researcher_id has invalid format")
                    continue
                if event_researcher_id.strip().upper() != state.get("researcher_id"):
                    ignore(state, index, f"{kind} researcher_id does not match live claim identity")
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
            state["state"] = "HANDOFF_READY"
            if event.get("progress_ref"):
                state["last_progress_ref"] = event["progress_ref"]
            state["last_progress_at"] = event["at"]
            state["next_action"] = next_action
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
            state["claim_id"] = None
            state["actor"] = None
            release_claim_identity(state)
            state["lease_until"] = None
            state["last_progress_at"] = event["at"]
            if event.get("next_action"):
                state["next_action"] = event["next_action"]
            continue

        ignore(state, index, f"unknown event type: {kind!r}")

    expire_claim(state, now)
    state["lease_until"] = state["lease_until"].isoformat() if isinstance(state.get("lease_until"), datetime) else None

    if state["state"] in {"DONE", "SUPERSEDED"}:
        state["dispatch_state"] = "COMPLETE"
    elif state["state"] == "BLOCKED" and complete_hard_block(state.get("hard_block")):
        state["dispatch_state"] = "BLOCKED"
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
