#!/usr/bin/env python3
"""Enterprise Math research scheduler V2.

V2 makes task publication, Driver review, execution return, and orphan recovery
first-class scheduler states. `research_scheduler.json` remains a legacy seed
registry; `research_scheduler_v2.json` is the canonical control-plane contract.

GitHub Issue #240 remains the append-only runtime event log. This tool is pure:
it validates/reduces exported events and emits canonical event JSON, but it does
not itself perform network I/O.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import pathlib
import re
import sys
from datetime import datetime, timedelta, timezone
from typing import Any, Iterable

ROOT = pathlib.Path(__file__).resolve().parents[1]
DEFAULT_CONFIG = ROOT / "research_scheduler_v2.json"
DEFAULT_OWNERS = ROOT / "branch_governance_overrides.json"

V2_SCHEMA = "ENTERPRISE_MATH_RESEARCH_SCHEDULER_V2"
V1_SCHEMA = "ENTERPRISE_MATH_RESEARCH_SCHEDULER_V1"
V2_EVENT_SCHEMA = "ENTERPRISE_MATH_SCHEDULER_EVENT_V2"
V1_EVENT_SCHEMA = "ENTERPRISE_MATH_SCHEDULER_EVENT_V1"

HARD_BLOCK_FIELDS = ("missing_object", "owner", "necessity", "unblock_condition")
ACTIVE_OWNER_STATES = {"ACTIVE_OWNER", "ACTIVE_BRIDGE"}
DEPENDENCY_ACTIONS = {"INFORM", "CONSUME", "TEST", "HARD_DEPENDENCY"}
RESEARCHER_ID_RE = re.compile(r"^EM-[A-Z0-9]+-(?:[0-9]{2}|[A-Z0-9]{4,8})$")
DRIVER_ID_RE = re.compile(r"^(?:EM-DRIVER-[0-9]{2}|EM-DVR-(?:[0-9]{2}|[A-Z0-9]{4,8}))$")
TASK_LANE_RE = re.compile(r"^RS-((?:R|P)\d{3}[A-Z0-9]*)\b")
LANE_RE = re.compile(r"[^A-Z0-9]+")
TASKBOOK_PREFIX = "<!-- ENTERPRISE_MATH_TASK_V1\n"
TASKBOOK_SUFFIX = "\n-->"
TERMINAL_STATES = {"DONE", "REJECTED", "SUPERSEDED"}
DISPATCHABLE_STATES = {"READY", "HANDOFF_READY", "CHANGES_REQUESTED"}
REVIEW_STATES = {"PUBLISHED", "RETURNED"}
PATCHABLE_TASK_FIELDS = {
    "owner",
    "priority",
    "leverage",
    "frontier",
    "next_action",
    "source_refs",
    "evidence_status",
    "tags",
}


class SchedulerError(ValueError):
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
        raise SchedulerError("identity_lane must contain an alphanumeric character")
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


def valid_driver_id(value: Any) -> bool:
    return isinstance(value, str) and bool(DRIVER_ID_RE.fullmatch(value.strip().upper()))


def valid_publisher_id(role: str, value: Any) -> bool:
    role = role.upper()
    if role == "RESEARCHER":
        return valid_researcher_id(value)
    if role == "RESEARCH_DRIVER":
        return valid_driver_id(value)
    if role == "STEWARD":
        return isinstance(value, str) and value.strip().upper().startswith("EM-")
    if role == "USER":
        return value in (None, "", "USER")
    return False


def researcher_id_for_claim(task: dict[str, Any], claim_id: str) -> str:
    lane = identity_lane(task)
    digest = hashlib.sha256(f"{task['task_id']}\0{claim_id}".encode("utf-8")).hexdigest()[:6].upper()
    return f"EM-{lane}-{digest}"


def release_claim_identity(state: dict[str, Any]) -> None:
    if state.get("researcher_id"):
        state["last_researcher_id"] = state["researcher_id"]
    state["researcher_id"] = None
    state["identity_source"] = None


def load_scheduler_bundle(path: pathlib.Path = DEFAULT_CONFIG) -> dict[str, Any]:
    config = load_json(path)
    if config.get("schema") == V1_SCHEMA:
        legacy = copy.deepcopy(config)
        legacy["_legacy_direct_config"] = True
        return legacy
    if config.get("schema") != V2_SCHEMA:
        return config

    materialized = copy.deepcopy(config)
    tasks: list[dict[str, Any]] = []
    seed_name = materialized.get("seed_registry")
    if isinstance(seed_name, str) and seed_name.strip():
        seed_path = path.parent / seed_name
        seed = load_json(seed_path)
        if seed.get("schema") != V1_SCHEMA:
            raise SchedulerError(f"seed registry {seed_name} is not {V1_SCHEMA}")
        for item in seed.get("tasks", []):
            cloned = copy.deepcopy(item)
            cloned.setdefault("registry_source", "LEGACY_V1_SEED")
            cloned.setdefault("publication_review_exempt", True)
            cloned.setdefault(
                "publication_review_exempt_reason",
                "Task existed in the canonical V1 seed registry before scheduler V2 migration.",
            )
            tasks.append(cloned)
        materialized["_seed_registry_schema"] = seed.get("schema")
    tasks.extend(copy.deepcopy(materialized.get("bootstrap_tasks", [])))
    materialized["tasks"] = tasks
    materialized["_config_path"] = str(path)
    return materialized


def _owner_sets(owners: dict[str, Any]) -> tuple[dict[str, Any], set[str]]:
    owner_entries = owners.get("branches", {})
    active_owners = {
        name
        for name, spec in owner_entries.items()
        if isinstance(spec, dict) and spec.get("state") in ACTIVE_OWNER_STATES
    }
    return owner_entries, active_owners


def validate_scheduler(config: dict[str, Any], owners: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    schema = config.get("schema")
    if schema not in {V2_SCHEMA, V1_SCHEMA}:
        errors.append("unexpected scheduler schema")

    task_states = set(config.get("task_states", []))
    event_types = set(config.get("event_types", []))
    if schema == V2_SCHEMA:
        required_states = {
            "PUBLISHED", "READY", "CLAIMED", "IN_PROGRESS", "RETURNED",
            "HANDOFF_READY", "ORPHANED", "BLOCKED", "DONE", "REJECTED", "SUPERSEDED",
        }
        required_events = {
            "PUBLISH", "REVIEW", "CLAIM", "HEARTBEAT", "PROGRESS", "HANDOFF",
            "RETURN", "HARD_BLOCK", "UNBLOCK", "ORPHAN", "RECOVER", "SUPERSEDE",
        }
    else:
        required_states = {"READY", "HANDOFF_READY", "BLOCKED", "DONE", "SUPERSEDED"}
        required_events = {
            "CLAIM", "HEARTBEAT", "PROGRESS", "HANDOFF", "HARD_BLOCK",
            "UNBLOCK", "DONE", "SUPERSEDE",
        }
    if not required_states <= task_states:
        errors.append("scheduler task_states are incomplete")
    if not required_events <= event_types:
        errors.append("scheduler event_types are incomplete")

    _, active_owners = _owner_sets(owners)
    tasks = config.get("tasks", [])
    seen: set[str] = set()
    covered_active: set[str] = set()
    policy = config.get("selection_policy", {})
    priorities = set(policy.get("priority_order", []))
    leverage_values = set(policy.get("leverage_order", []))

    for index, task in enumerate(tasks):
        prefix = f"tasks[{index}]"
        task_id = task.get("task_id")
        if not isinstance(task_id, str) or not task_id:
            errors.append(f"{prefix}: missing task_id")
            continue
        if task_id in seen:
            errors.append(f"duplicate task_id: {task_id}")
        seen.add(task_id)

        if "identity_lane" in task and task.get("identity_lane"):
            try:
                identity_lane(task)
            except SchedulerError as exc:
                errors.append(f"{task_id}: {exc}")

        state = task.get("base_state")
        if state not in task_states:
            errors.append(f"{task_id}: invalid base_state {state!r}")
        if priorities and task.get("priority") not in priorities:
            errors.append(f"{task_id}: invalid priority {task.get('priority')!r}")
        if leverage_values and task.get("leverage") not in leverage_values:
            errors.append(f"{task_id}: invalid leverage {task.get('leverage')!r}")

        owner = task.get("owner")
        kind = task.get("kind")
        if kind == "RESEARCH":
            if state == "PUBLISHED" and owner == "taskbook/unassigned":
                pass
            elif owner not in active_owners:
                errors.append(f"{task_id}: research owner is not ACTIVE_OWNER/ACTIVE_BRIDGE: {owner!r}")
            else:
                covered_active.add(owner)
        elif kind == "GOVERNANCE":
            if owner != "governance":
                errors.append(f"{task_id}: governance task must use owner='governance'")
        else:
            errors.append(f"{task_id}: invalid task kind {kind!r}")

        hard_block = task.get("hard_block")
        if hard_block is not None and not complete_hard_block(hard_block):
            errors.append(f"{task_id}: partial hard_block is invalid")
        if state == "BLOCKED" and not complete_hard_block(hard_block):
            errors.append(f"{task_id}: BLOCKED requires a complete hard_block")

        for dep_index, dependency in enumerate(task.get("dependencies", [])):
            if not isinstance(dependency, dict):
                errors.append(f"{task_id}: dependency[{dep_index}] is not an object")
                continue
            action = dependency.get("action")
            if action not in DEPENDENCY_ACTIONS:
                errors.append(f"{task_id}: dependency[{dep_index}] has invalid action {action!r}")

        for field in ("frontier", "next_action", "last_progress_at"):
            value = task.get(field)
            if field == "last_progress_at" and state == "PUBLISHED" and not value:
                continue
            if not isinstance(value, str) or not value.strip():
                errors.append(f"{task_id}: missing {field}")
        if isinstance(task.get("last_progress_at"), str):
            try:
                parse_time(task["last_progress_at"])
            except (TypeError, ValueError):
                errors.append(f"{task_id}: invalid last_progress_at")

    missing_coverage = sorted(active_owners - covered_active)
    if missing_coverage:
        errors.append("active research owners missing scheduler coverage: " + ", ".join(missing_coverage))
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
            raise SchedulerError("event JSON must be an array")
        events = data
    else:
        events = [json.loads(line) for line in text.splitlines() if line.strip()]
    for index, event in enumerate(events):
        if not isinstance(event, dict):
            raise SchedulerError(f"event {index} is not an object")
    return events


def event_schema(event: dict[str, Any]) -> str:
    value = event.get("schema")
    return V1_EVENT_SCHEMA if value is None else str(value)


def lease_duration(event: dict[str, Any], default_minutes: int) -> timedelta:
    minutes = event.get("lease_minutes", default_minutes)
    if not isinstance(minutes, int) or minutes <= 0:
        raise SchedulerError("lease_minutes must be a positive integer")
    return timedelta(minutes=minutes)


def event_time(event: dict[str, Any]) -> datetime:
    value = event.get("at")
    if not isinstance(value, str) or not value:
        raise SchedulerError("scheduler event requires ISO-8601 'at'")
    return parse_time(value)


def _publication_task(config: dict[str, Any], event: dict[str, Any]) -> tuple[dict[str, Any] | None, str | None]:
    if event_schema(event) != V2_EVENT_SCHEMA:
        return None, "PUBLISH requires V2 event schema"
    task_id = event.get("task_id")
    if not isinstance(task_id, str) or not task_id.strip():
        return None, "PUBLISH requires task_id"
    role = str(event.get("publisher_role", "")).upper()
    allowed = set(config.get("publish_contract", {}).get("allowed_publisher_roles", []))
    if role not in allowed:
        return None, f"PUBLISH invalid publisher_role {role!r}"
    publisher_id = event.get("publisher_id")
    required_roles = set(config.get("publish_contract", {}).get("publisher_id_required_for_roles", []))
    if role in required_roles and not valid_publisher_id(role, publisher_id):
        return None, f"PUBLISH invalid/missing publisher_id for {role}"
    try:
        published_at = event_time(event)
    except (SchedulerError, ValueError) as exc:
        return None, str(exc)

    payload = event.get("task")
    if not isinstance(payload, dict):
        return None, "PUBLISH requires task object"
    required = config.get("publish_contract", {}).get("required_task_fields", [])
    for field in required:
        value = payload.get(field)
        if not isinstance(value, str) or not value.strip():
            return None, f"PUBLISH task missing {field}"

    priorities = set(config.get("selection_policy", {}).get("priority_order", []))
    leverage = set(config.get("selection_policy", {}).get("leverage_order", []))
    if payload.get("priority") not in priorities:
        return None, f"PUBLISH invalid priority {payload.get('priority')!r}"
    if payload.get("leverage") not in leverage:
        return None, f"PUBLISH invalid leverage {payload.get('leverage')!r}"
    if payload.get("kind") not in {"RESEARCH", "GOVERNANCE"}:
        return None, f"PUBLISH invalid kind {payload.get('kind')!r}"

    task = copy.deepcopy(payload)
    task["task_id"] = task_id
    task["base_state"] = "PUBLISHED"
    task.setdefault("dependencies", [])
    task.setdefault("source_refs", [])
    task.setdefault("evidence_status", "PUBLISHED_PENDING_DRIVER_REVIEW")
    task.setdefault("last_progress_ref", event.get("publish_ref"))
    task.setdefault("last_progress_at", event["at"])
    task.setdefault("hard_block", None)
    task.setdefault("tags", [])
    task["publisher_role"] = role
    task["publisher_id"] = publisher_id.strip().upper() if isinstance(publisher_id, str) else None
    task["publisher_actor"] = event.get("actor")
    task["published_at"] = published_at.isoformat()
    task["publish_ref"] = event.get("publish_ref") or event.get("taskbook_ref")
    task["taskbook_ref"] = event.get("taskbook_ref") or task.get("taskbook_ref")
    task["taskbook_policy_state"] = event.get("taskbook_policy_state")
    task["registry_source"] = "RUNTIME_PUBLISH_EVENT"
    task["publication_review_exempt"] = False
    return task, None


def collect_tasks(config: dict[str, Any], events: list[dict[str, Any]]) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    tasks = [copy.deepcopy(item) for item in config.get("tasks", [])]
    seen = {str(item.get("task_id")) for item in tasks if item.get("task_id")}
    registry_issues: list[dict[str, Any]] = []
    for index, event in enumerate(events):
        if event.get("event") != "PUBLISH":
            continue
        task_id = event.get("task_id")
        if isinstance(task_id, str) and task_id in seen:
            registry_issues.append({"index": index, "task_id": task_id, "reason": "duplicate PUBLISH task_id"})
            continue
        task, error = _publication_task(config, event)
        if error:
            registry_issues.append({"index": index, "task_id": task_id, "reason": error})
            continue
        assert task is not None
        tasks.append(task)
        seen.add(task["task_id"])
    return tasks, registry_issues


def state_from_task(task: dict[str, Any]) -> dict[str, Any]:
    return {
        "task_id": task["task_id"], "state": task["base_state"], "claim_id": None,
        "actor": None, "researcher_id": None, "last_researcher_id": None,
        "last_executor_id": None, "last_executor_actor": None, "identity_source": None,
        "lease_until": None, "hard_block": copy.deepcopy(task.get("hard_block")),
        "last_progress_ref": task.get("last_progress_ref"), "last_progress_at": task.get("last_progress_at"),
        "next_action": task.get("next_action"), "return_ref": None,
        "publisher_role": task.get("publisher_role"), "publisher_id": task.get("publisher_id"),
        "publisher_actor": task.get("publisher_actor"), "published_at": task.get("published_at"),
        "publish_ref": task.get("publish_ref"), "taskbook_ref": task.get("taskbook_ref"),
        "taskbook_policy_state": task.get("taskbook_policy_state"),
        "dispatch_reviewer_id": None, "return_reviewer_id": None,
        "review_history": [], "orphan_history": [],
        "registry_source": task.get("registry_source", "STATIC"),
        "publication_review_exempt": bool(task.get("publication_review_exempt", False)),
        "publication_review_exempt_reason": task.get("publication_review_exempt_reason"),
        "title": task.get("title"), "kind": task.get("kind"), "owner": task.get("owner"),
        "priority": task.get("priority"), "leverage": task.get("leverage"),
        "frontier": task.get("frontier"), "source_refs": copy.deepcopy(task.get("source_refs", [])),
        "evidence_status": task.get("evidence_status"), "tags": copy.deepcopy(task.get("tags", [])),
        "identity_lane": identity_lane(task), "ignored_events": [],
    }


def _orphan_record(state: dict[str, Any], *, orphaned_at: datetime, reason: str, extra: dict[str, Any] | None = None) -> dict[str, Any]:
    record = {
        "orphaned_at": orphaned_at.isoformat(), "reason": reason, "claim_id": state.get("claim_id"),
        "actor": state.get("actor"), "researcher_id": state.get("researcher_id") or state.get("last_researcher_id"),
        "last_progress_ref": state.get("last_progress_ref"), "next_action": state.get("next_action"),
    }
    if extra:
        record.update(copy.deepcopy(extra))
    return record


def expire_claim(state: dict[str, Any], at: datetime) -> None:
    lease_until = state.get("lease_until")
    if state.get("claim_id") and isinstance(lease_until, datetime) and at >= lease_until:
        state["orphan_history"].append(_orphan_record(state, orphaned_at=lease_until, reason="LEASE_EXPIRED", extra={"derived": True}))
        state["state"] = "ORPHANED"
        state["claim_id"] = None
        state["actor"] = None
        release_claim_identity(state)
        state["lease_until"] = None


def ignore(state: dict[str, Any], index: int, reason: str) -> None:
    state["ignored_events"].append({"index": index, "reason": reason})


def _valid_schema_for_kind(kind: Any, schema: str) -> bool:
    if schema == V2_EVENT_SCHEMA:
        return True
    if schema == V1_EVENT_SCHEMA:
        return kind in {"CLAIM", "HEARTBEAT", "PROGRESS", "HANDOFF", "HARD_BLOCK", "UNBLOCK", "DONE", "SUPERSEDE"}
    return False


def _clear_claim(state: dict[str, Any]) -> None:
    state["claim_id"] = None
    state["actor"] = None
    release_claim_identity(state)
    state["lease_until"] = None


def _review_record(event: dict[str, Any]) -> dict[str, Any]:
    return {
        "at": event.get("at"), "stage": event.get("review_stage"), "verdict": event.get("verdict"),
        "reviewer_id": event.get("reviewer_id") or event.get("driver_id"),
        "review_ref": event.get("review_ref"), "note": event.get("review_note"),
    }


def _apply_task_patch(state: dict[str, Any], event: dict[str, Any]) -> str | None:
    patch = event.get("task_patch")
    if patch is None:
        return None
    if not isinstance(patch, dict):
        return "task_patch must be an object"
    unknown = set(patch) - PATCHABLE_TASK_FIELDS
    if unknown:
        return "task_patch contains non-reviewable fields: " + ", ".join(sorted(unknown))
    for field, value in patch.items():
        state[field] = copy.deepcopy(value)
    return None


def _cross_review_error(state: dict[str, Any], stage: str, reviewer_id: str) -> str | None:
    reviewer = reviewer_id.strip().upper()
    if stage == "DISPATCH":
        publisher = state.get("publisher_id")
        if isinstance(publisher, str) and publisher.strip().upper() == reviewer:
            return "DISPATCH review must be independent of publisher_id"
    elif stage == "RETURN":
        executor = state.get("last_executor_id") or state.get("last_researcher_id")
        if isinstance(executor, str) and executor.strip().upper() == reviewer:
            return "RETURN review must be independent of last executor identity"
    return None


def reduce_task(task: dict[str, Any], events: Iterable[dict[str, Any]], *, default_lease_minutes: int, now: datetime) -> dict[str, Any]:
    state = state_from_task(task)
    matching = [event for event in events if event.get("task_id") == task["task_id"]]
    last_event_time: datetime | None = None
    for index, event in enumerate(matching):
        kind = event.get("event")
        schema = event_schema(event)
        if kind == "PUBLISH":
            continue
        if not _valid_schema_for_kind(kind, schema):
            ignore(state, index, f"event {kind!r} not valid under schema {schema!r}")
            continue
        try:
            at = event_time(event)
        except (SchedulerError, ValueError) as exc:
            ignore(state, index, str(exc))
            continue
        if last_event_time is not None and at < last_event_time:
            ignore(state, index, "events must be supplied in GitHub comment order / nondecreasing event time")
            continue
        last_event_time = at
        expire_claim(state, at)
        claim_id = event.get("claim_id")
        live_claim = state.get("claim_id")

        if kind == "CLAIM":
            if state["state"] not in DISPATCHABLE_STATES or live_claim:
                ignore(state, index, "task is not dispatchable")
                continue
            if not isinstance(claim_id, str) or not claim_id:
                ignore(state, index, "CLAIM requires claim_id")
                continue
            supplied_researcher_id = event.get("researcher_id")
            if supplied_researcher_id is not None and not valid_researcher_id(supplied_researcher_id):
                ignore(state, index, "CLAIM researcher_id has invalid format")
                continue
            researcher_id = supplied_researcher_id.strip().upper() if isinstance(supplied_researcher_id, str) else researcher_id_for_claim(task, claim_id)
            try:
                duration = lease_duration(event, default_lease_minutes)
            except SchedulerError as exc:
                ignore(state, index, str(exc))
                continue
            state["state"] = "CLAIMED"
            state["claim_id"] = claim_id
            state["actor"] = event.get("actor")
            state["researcher_id"] = researcher_id
            state["last_researcher_id"] = researcher_id
            state["last_executor_id"] = researcher_id
            state["last_executor_actor"] = event.get("actor")
            state["identity_source"] = "EVENT" if supplied_researcher_id is not None else "AUTO_CLAIM_DERIVED"
            state["lease_until"] = at + duration
            continue

        if kind in {"HEARTBEAT", "PROGRESS", "HANDOFF", "HARD_BLOCK", "RETURN"} or (kind == "DONE" and schema == V1_EVENT_SCHEMA):
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
            except SchedulerError as exc:
                ignore(state, index, str(exc))
            continue

        if kind == "PROGRESS":
            try:
                state["lease_until"] = at + lease_duration(event, default_lease_minutes)
            except SchedulerError as exc:
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
            _clear_claim(state)
            continue

        if kind == "RETURN":
            if schema != V2_EVENT_SCHEMA:
                ignore(state, index, "RETURN requires V2 event schema")
                continue
            return_ref = event.get("return_ref") or event.get("progress_ref")
            if not isinstance(return_ref, str) or not return_ref.strip():
                ignore(state, index, "RETURN requires return_ref or progress_ref")
                continue
            state["state"] = "RETURNED"
            state["return_ref"] = return_ref
            state["last_progress_ref"] = return_ref
            state["last_progress_at"] = event["at"]
            if event.get("next_action"):
                state["next_action"] = event["next_action"]
            _clear_claim(state)
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
            _clear_claim(state)
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

        if kind == "ORPHAN":
            if schema != V2_EVENT_SCHEMA:
                ignore(state, index, "ORPHAN requires V2 event schema")
                continue
            if state["state"] in TERMINAL_STATES:
                ignore(state, index, "terminal task cannot become ORPHANED")
                continue
            required = ("orphan_reason", "discovered_by", "source_ref")
            if any(not isinstance(event.get(field), str) or not event[field].strip() for field in required):
                ignore(state, index, "ORPHAN requires orphan_reason, discovered_by, source_ref")
                continue
            if live_claim and claim_id != live_claim and not valid_driver_id(event.get("driver_id")):
                ignore(state, index, "ORPHAN of a live claim requires current claim_id or Driver override")
                continue
            state["orphan_history"].append(_orphan_record(
                state, orphaned_at=at, reason=event["orphan_reason"],
                extra={"derived": False, "discovered_by": event["discovered_by"], "source_ref": event["source_ref"],
                       "branch": event.get("branch"), "last_commit": event.get("last_commit"), "driver_id": event.get("driver_id")},
            ))
            state["state"] = "ORPHANED"
            state["last_progress_at"] = event["at"]
            _clear_claim(state)
            continue

        if kind == "RECOVER":
            if schema != V2_EVENT_SCHEMA:
                ignore(state, index, "RECOVER requires V2 event schema")
                continue
            if state["state"] != "ORPHANED":
                ignore(state, index, "RECOVER requires ORPHANED state")
                continue
            driver_id = event.get("driver_id")
            if not valid_driver_id(driver_id):
                ignore(state, index, "RECOVER requires valid driver_id")
                continue
            next_action = event.get("next_action")
            review_ref = event.get("review_ref")
            if not isinstance(next_action, str) or not next_action.strip():
                ignore(state, index, "RECOVER requires next_action")
                continue
            if not isinstance(review_ref, str) or not review_ref.strip():
                ignore(state, index, "RECOVER requires review_ref")
                continue
            state["review_history"].append({"at": event.get("at"), "stage": "RECOVERY", "verdict": "ACCEPT",
                                            "reviewer_id": driver_id.strip().upper(), "review_ref": review_ref, "note": event.get("review_note")})
            state["state"] = "HANDOFF_READY"
            state["next_action"] = next_action
            state["last_progress_at"] = event["at"]
            continue

        if kind == "REVIEW":
            if schema != V2_EVENT_SCHEMA:
                ignore(state, index, "REVIEW requires V2 event schema")
                continue
            stage = str(event.get("review_stage", "")).upper()
            verdict = str(event.get("verdict", "")).upper()
            reviewer_id = event.get("reviewer_id")
            review_ref = event.get("review_ref")
            if stage not in {"DISPATCH", "RETURN", "RECOVERY"}:
                ignore(state, index, f"invalid review_stage {stage!r}")
                continue
            if verdict not in {"ACCEPT", "CHANGES_REQUESTED", "REJECT"}:
                ignore(state, index, f"invalid review verdict {verdict!r}")
                continue
            if not valid_driver_id(reviewer_id):
                ignore(state, index, "REVIEW requires valid Driver reviewer_id")
                continue
            if not isinstance(review_ref, str) or not review_ref.strip():
                ignore(state, index, "REVIEW requires review_ref")
                continue
            reviewer = reviewer_id.strip().upper()
            cross_error = _cross_review_error(state, stage, reviewer)
            if cross_error:
                ignore(state, index, cross_error)
                continue
            expected_state = {"DISPATCH": "PUBLISHED", "RETURN": "RETURNED", "RECOVERY": "ORPHANED"}[stage]
            if state["state"] != expected_state:
                ignore(state, index, f"{stage} review requires {expected_state} state")
                continue
            if stage == "RETURN" and verdict == "REJECT":
                ignore(state, index, "RETURN review uses CHANGES_REQUESTED rather than REJECT")
                continue
            if verdict == "ACCEPT":
                patch_error = _apply_task_patch(state, event)
                if patch_error:
                    ignore(state, index, patch_error)
                    continue
            state["review_history"].append({**_review_record(event), "reviewer_id": reviewer})
            if stage == "DISPATCH":
                state["dispatch_reviewer_id"] = reviewer
                if event.get("taskbook_policy_state"):
                    state["taskbook_policy_state"] = event["taskbook_policy_state"]
                if verdict == "ACCEPT":
                    state["state"] = "READY"
                elif verdict == "CHANGES_REQUESTED":
                    state["state"] = "PUBLISHED"
                    if event.get("next_action"):
                        state["next_action"] = event["next_action"]
                else:
                    state["state"] = "REJECTED"
            elif stage == "RETURN":
                state["return_reviewer_id"] = reviewer
                if verdict == "ACCEPT":
                    state["state"] = "DONE"
                else:
                    next_action = event.get("next_action")
                    if not isinstance(next_action, str) or not next_action.strip():
                        state["review_history"].pop()
                        state["return_reviewer_id"] = None
                        ignore(state, index, "RETURN CHANGES_REQUESTED requires next_action")
                        continue
                    state["state"] = "CHANGES_REQUESTED"
                    state["next_action"] = next_action
            else:
                if verdict == "ACCEPT":
                    next_action = event.get("next_action")
                    if not isinstance(next_action, str) or not next_action.strip():
                        state["review_history"].pop()
                        ignore(state, index, "RECOVERY ACCEPT requires next_action")
                        continue
                    state["state"] = "HANDOFF_READY"
                    state["next_action"] = next_action
                elif verdict == "CHANGES_REQUESTED":
                    state["state"] = "ORPHANED"
                    if event.get("next_action"):
                        state["next_action"] = event["next_action"]
                else:
                    state["state"] = "REJECTED"
            state["last_progress_at"] = event["at"]
            continue

        if kind == "DONE":
            if schema != V1_EVENT_SCHEMA:
                ignore(state, index, "V2 forbids worker DONE; use RETURN then REVIEW")
                continue
            state["state"] = "DONE"
            if event.get("progress_ref"):
                state["last_progress_ref"] = event["progress_ref"]
            state["last_progress_at"] = event["at"]
            state["review_history"].append({"at": event.get("at"), "stage": "LEGACY_V1_DONE", "verdict": "GRANDFATHERED",
                                            "reviewer_id": None, "review_ref": event.get("progress_ref"),
                                            "note": "Pre-V2 DONE retained for append-only history compatibility."})
            _clear_claim(state)
            continue

        if kind == "SUPERSEDE":
            if schema == V2_EVENT_SCHEMA and not valid_driver_id(event.get("driver_id")):
                ignore(state, index, "V2 SUPERSEDE requires valid driver_id")
                continue
            state["state"] = "SUPERSEDED"
            _clear_claim(state)
            state["last_progress_at"] = event["at"]
            if event.get("next_action"):
                state["next_action"] = event["next_action"]
            continue

        ignore(state, index, f"unknown event type: {kind!r}")

    expire_claim(state, now)
    state["lease_until"] = state["lease_until"].isoformat() if isinstance(state.get("lease_until"), datetime) else None
    if state["state"] in TERMINAL_STATES:
        state["dispatch_state"] = "COMPLETE"
    elif state["state"] == "BLOCKED" and complete_hard_block(state.get("hard_block")):
        state["dispatch_state"] = "BLOCKED"
    elif state["state"] == "ORPHANED":
        state["dispatch_state"] = "ORPHANED"
    elif state.get("claim_id"):
        state["dispatch_state"] = "LEASED"
    elif state["state"] in REVIEW_STATES:
        state["dispatch_state"] = "NEEDS_REVIEW"
    elif state["state"] in DISPATCHABLE_STATES:
        state["dispatch_state"] = "NEEDS_DISPATCH"
    else:
        state["dispatch_state"] = "DORMANT"
    return state


def effective_states(config: dict[str, Any], events: list[dict[str, Any]], now: datetime) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    default_lease = int(config.get("claim_lease_minutes", 120))
    tasks, registry_issues = collect_tasks(config, events)
    results = [reduce_task(task, events, default_lease_minutes=default_lease, now=now) for task in tasks]
    return results, registry_issues


def select_task(config: dict[str, Any], events: list[dict[str, Any]], now: datetime, *, kind: str = "RESEARCH") -> dict[str, Any] | None:
    policy = config["selection_policy"]
    states, _ = effective_states(config, events, now)
    state_rank = {name: index for index, name in enumerate(policy["state_order"])}
    priority_rank = {name: index for index, name in enumerate(policy["priority_order"])}
    leverage_rank = {name: index for index, name in enumerate(policy["leverage_order"])}
    candidates = [state for state in states if state["dispatch_state"] == "NEEDS_DISPATCH" and (kind == "ANY" or state["kind"] == kind)]
    if not candidates:
        return None
    def candidate_key(state: dict[str, Any]) -> tuple[Any, ...]:
        try:
            last_progress = parse_time(state["last_progress_at"])
        except (TypeError, ValueError):
            last_progress = datetime(1970, 1, 1, tzinfo=timezone.utc)
        return (state_rank.get(state["state"], len(state_rank)), priority_rank.get(state["priority"], len(priority_rank)),
                leverage_rank.get(state["leverage"], len(leverage_rank)), last_progress, state["task_id"])
    return min(candidates, key=candidate_key)


def split_taskbook(text: str) -> tuple[dict[str, Any], str]:
    if not text.startswith(TASKBOOK_PREFIX):
        raise ValueError("missing ENTERPRISE_MATH_TASK_V1 frontmatter")
    end = text.find(TASKBOOK_SUFFIX, len(TASKBOOK_PREFIX))
    if end < 0:
        raise ValueError("unterminated taskbook frontmatter")
    raw = text[len(TASKBOOK_PREFIX):end]
    meta = json.loads(raw)
    body = text[end + len(TASKBOOK_SUFFIX):].lstrip("\n")
    return meta, body


def registry_integrity(config: dict[str, Any], events: list[dict[str, Any]], *, root: pathlib.Path = ROOT) -> list[str]:
    errors: list[str] = []
    tasks, registry_issues = collect_tasks(config, events)
    errors.extend(f"registry event[{item['index']}]: {item['reason']}" for item in registry_issues)
    registered = {task["task_id"] for task in tasks}
    seen_taskbook_ids: dict[str, str] = {}
    policy = config.get("registry_integrity", {})
    must_states = set(policy.get("must_be_registered_taskbook_states", []))
    directory = root / policy.get("taskbook_directory", "research_tasks")
    if directory.exists():
        for path in sorted(directory.glob("*.md")):
            text = path.read_text(encoding="utf-8")
            if not text.startswith(TASKBOOK_PREFIX):
                continue
            try:
                meta, _ = split_taskbook(text)
            except Exception as exc:
                errors.append(f"{path.relative_to(root)}: malformed taskbook: {exc}")
                continue
            task_id = meta.get("task_id")
            if not isinstance(task_id, str) or not task_id:
                errors.append(f"{path.relative_to(root)}: frontmatter missing task_id")
                continue
            prior = seen_taskbook_ids.get(task_id)
            if prior and prior != str(path.relative_to(root)):
                errors.append(f"duplicate taskbook task_id {task_id}: {prior}, {path.relative_to(root)}")
            seen_taskbook_ids[task_id] = str(path.relative_to(root))
            state = meta.get("base_state")
            if state in must_states and task_id not in registered:
                errors.append(f"{path.relative_to(root)}: executable taskbook {task_id} state={state} is absent from scheduler registry")
    for task in tasks:
        taskbook_ref = task.get("taskbook_ref")
        if isinstance(taskbook_ref, str) and taskbook_ref.strip():
            path = root / taskbook_ref
            if not path.exists():
                errors.append(f"{task['task_id']}: registered taskbook_ref does not exist: {taskbook_ref}")
    return errors


def validate_effective_owners(config: dict[str, Any], owners: dict[str, Any], events: list[dict[str, Any]], now: datetime) -> list[str]:
    errors: list[str] = []
    _, active_owners = _owner_sets(owners)
    states, registry_issues = effective_states(config, events, now)
    errors.extend(f"registry event[{item['index']}]: {item['reason']}" for item in registry_issues)
    for state in states:
        if state["kind"] != "RESEARCH" or state["state"] == "PUBLISHED" or state["state"] in TERMINAL_STATES:
            continue
        owner = state.get("owner")
        if owner not in active_owners:
            errors.append(f"{state['task_id']}: effective executable owner is not ACTIVE_OWNER/ACTIVE_BRIDGE: {owner!r}")
    return errors


def print_json(value: Any) -> None:
    print(json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True))


def _iso_now_arg(value: str | None) -> str:
    if value:
        parse_time(value)
        return value
    return datetime.now(timezone.utc).isoformat()


def _base_event(kind: str, args: argparse.Namespace) -> dict[str, Any]:
    return {"schema": V2_EVENT_SCHEMA, "event": kind, "task_id": args.task_id, "actor": args.actor, "at": _iso_now_arg(args.at)}


def _load_taskbook_meta(path_value: str) -> tuple[pathlib.Path, dict[str, Any]]:
    path = pathlib.Path(path_value)
    if not path.is_absolute():
        path = ROOT / path
    meta, _ = split_taskbook(path.read_text(encoding="utf-8"))
    return path, meta


def emit_publish(args: argparse.Namespace) -> int:
    path, meta = _load_taskbook_meta(args.taskbook)
    task_id = meta.get("task_id")
    if not isinstance(task_id, str) or not task_id:
        raise SchedulerError("taskbook missing task_id")
    args.task_id = task_id
    event = _base_event("PUBLISH", args)
    event["publisher_role"] = args.publisher_role
    if args.publisher_id:
        event["publisher_id"] = args.publisher_id
    event["taskbook_ref"] = str(path.relative_to(ROOT))
    review = meta.get("policy_review")
    if isinstance(review, dict):
        event["taskbook_policy_state"] = review.get("review_state")
    event["publish_ref"] = args.publish_ref or event["taskbook_ref"]
    fields = ["title", "kind", "owner", "priority", "leverage", "frontier", "next_action", "dependencies", "source_refs", "evidence_status", "tags", "identity_lane"]
    event["task"] = {field: copy.deepcopy(meta.get(field)) for field in fields if field in meta}
    print_json(event)
    return 0


def emit_review(args: argparse.Namespace) -> int:
    event = _base_event("REVIEW", args)
    event.update({"review_stage": args.review_stage, "verdict": args.verdict, "reviewer_id": args.reviewer_id, "review_ref": args.review_ref})
    if args.review_note:
        event["review_note"] = args.review_note
    if args.next_action:
        event["next_action"] = args.next_action
    if args.taskbook_policy_state:
        event["taskbook_policy_state"] = args.taskbook_policy_state
    print_json(event)
    return 0


def emit_claim(args: argparse.Namespace) -> int:
    event = _base_event("CLAIM", args)
    event["claim_id"] = args.claim_id
    if args.researcher_id:
        event["researcher_id"] = args.researcher_id
    if args.lease_minutes:
        event["lease_minutes"] = args.lease_minutes
    print_json(event)
    return 0


def emit_progress(args: argparse.Namespace) -> int:
    event = _base_event("PROGRESS", args)
    event.update({"claim_id": args.claim_id, "progress_ref": args.progress_ref, "next_action": args.next_action})
    if args.researcher_id:
        event["researcher_id"] = args.researcher_id
    if args.lease_minutes:
        event["lease_minutes"] = args.lease_minutes
    print_json(event)
    return 0


def emit_handoff(args: argparse.Namespace) -> int:
    event = _base_event("HANDOFF", args)
    event.update({"claim_id": args.claim_id, "progress_ref": args.progress_ref, "next_action": args.next_action})
    if args.researcher_id:
        event["researcher_id"] = args.researcher_id
    print_json(event)
    return 0


def emit_return(args: argparse.Namespace) -> int:
    event = _base_event("RETURN", args)
    event.update({"claim_id": args.claim_id, "return_ref": args.return_ref})
    if args.next_action:
        event["next_action"] = args.next_action
    if args.researcher_id:
        event["researcher_id"] = args.researcher_id
    print_json(event)
    return 0


def emit_orphan(args: argparse.Namespace) -> int:
    event = _base_event("ORPHAN", args)
    event.update({"orphan_reason": args.orphan_reason, "discovered_by": args.discovered_by, "source_ref": args.source_ref})
    if args.claim_id:
        event["claim_id"] = args.claim_id
    if args.driver_id:
        event["driver_id"] = args.driver_id
    if args.branch:
        event["branch"] = args.branch
    if args.last_commit:
        event["last_commit"] = args.last_commit
    print_json(event)
    return 0


def emit_recover(args: argparse.Namespace) -> int:
    event = _base_event("RECOVER", args)
    event.update({"driver_id": args.driver_id, "review_ref": args.review_ref, "next_action": args.next_action})
    if args.review_note:
        event["review_note"] = args.review_note
    print_json(event)
    return 0


def _add_common_emit(parser: argparse.ArgumentParser, *, task_required: bool = True) -> None:
    if task_required:
        parser.add_argument("--task-id", required=True)
    parser.add_argument("--actor", required=True)
    parser.add_argument("--at")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Enterprise Math research scheduler V2")
    parser.add_argument("--config", type=pathlib.Path, default=DEFAULT_CONFIG)
    parser.add_argument("--owners", type=pathlib.Path, default=DEFAULT_OWNERS)
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("validate")
    integrity = sub.add_parser("registry-integrity")
    integrity.add_argument("--events", type=pathlib.Path)
    integrity.add_argument("--now")
    status = sub.add_parser("status")
    status.add_argument("--events", type=pathlib.Path)
    status.add_argument("--now")
    select = sub.add_parser("select")
    select.add_argument("--events", type=pathlib.Path)
    select.add_argument("--now")
    select.add_argument("--kind", choices=["RESEARCH", "GOVERNANCE", "ANY"], default="RESEARCH")
    identity = sub.add_parser("identity")
    identity.add_argument("--task-id", required=True)
    identity.add_argument("--claim-id", required=True)

    publish = sub.add_parser("emit-publish")
    publish.add_argument("--taskbook", required=True)
    publish.add_argument("--publisher-role", choices=["RESEARCHER", "RESEARCH_DRIVER", "STEWARD", "USER"], required=True)
    publish.add_argument("--publisher-id")
    publish.add_argument("--publish-ref")
    _add_common_emit(publish, task_required=False)
    publish.set_defaults(func=emit_publish)

    review = sub.add_parser("emit-review")
    review.add_argument("--review-stage", choices=["DISPATCH", "RETURN", "RECOVERY"], required=True)
    review.add_argument("--verdict", choices=["ACCEPT", "CHANGES_REQUESTED", "REJECT"], required=True)
    review.add_argument("--reviewer-id", required=True)
    review.add_argument("--review-ref", required=True)
    review.add_argument("--review-note")
    review.add_argument("--next-action")
    review.add_argument("--taskbook-policy-state")
    _add_common_emit(review)
    review.set_defaults(func=emit_review)

    claim = sub.add_parser("emit-claim")
    claim.add_argument("--claim-id", required=True)
    claim.add_argument("--researcher-id")
    claim.add_argument("--lease-minutes", type=int)
    _add_common_emit(claim)
    claim.set_defaults(func=emit_claim)

    progress = sub.add_parser("emit-progress")
    progress.add_argument("--claim-id", required=True)
    progress.add_argument("--researcher-id")
    progress.add_argument("--progress-ref", required=True)
    progress.add_argument("--next-action", required=True)
    progress.add_argument("--lease-minutes", type=int)
    _add_common_emit(progress)
    progress.set_defaults(func=emit_progress)

    handoff = sub.add_parser("emit-handoff")
    handoff.add_argument("--claim-id", required=True)
    handoff.add_argument("--researcher-id")
    handoff.add_argument("--progress-ref", required=True)
    handoff.add_argument("--next-action", required=True)
    _add_common_emit(handoff)
    handoff.set_defaults(func=emit_handoff)

    returned = sub.add_parser("emit-return")
    returned.add_argument("--claim-id", required=True)
    returned.add_argument("--researcher-id")
    returned.add_argument("--return-ref", required=True)
    returned.add_argument("--next-action")
    _add_common_emit(returned)
    returned.set_defaults(func=emit_return)

    orphan = sub.add_parser("emit-orphan")
    orphan.add_argument("--orphan-reason", required=True)
    orphan.add_argument("--discovered-by", required=True)
    orphan.add_argument("--source-ref", required=True)
    orphan.add_argument("--claim-id")
    orphan.add_argument("--driver-id")
    orphan.add_argument("--branch")
    orphan.add_argument("--last-commit")
    _add_common_emit(orphan)
    orphan.set_defaults(func=emit_orphan)

    recover = sub.add_parser("emit-recover")
    recover.add_argument("--driver-id", required=True)
    recover.add_argument("--review-ref", required=True)
    recover.add_argument("--next-action", required=True)
    recover.add_argument("--review-note")
    _add_common_emit(recover)
    recover.set_defaults(func=emit_recover)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if hasattr(args, "func"):
        return args.func(args)
    config = load_scheduler_bundle(args.config)
    owners = load_json(args.owners)
    errors = validate_scheduler(config, owners)
    if args.command == "validate":
        if errors:
            for error in errors:
                print(f"ERROR: {error}")
            return 1
        print(f"PASS: scheduler V2 config valid; {len(config.get('tasks', []))} static/bootstrap tasks cover all active research owners/bridges.")
        return 0
    if errors:
        raise SchedulerError("invalid scheduler configuration: " + "; ".join(errors))
    if args.command == "identity":
        tasks, _ = collect_tasks(config, [])
        task = next((item for item in tasks if item.get("task_id") == args.task_id), None)
        if task is None:
            raise SchedulerError(f"unknown static task_id: {args.task_id}")
        print_json({"task_id": args.task_id, "claim_id": args.claim_id, "identity_lane": identity_lane(task),
                    "researcher_id": researcher_id_for_claim(task, args.claim_id), "identity_source": "AUTO_CLAIM_DERIVED"})
        return 0
    events = load_events(args.events)
    current = now_utc(args.now)
    if args.command == "registry-integrity":
        issues = registry_integrity(config, events)
        issues.extend(validate_effective_owners(config, owners, events, current))
        if issues:
            for issue in issues:
                print(f"ERROR: {issue}")
            return 1
        print("PASS: scheduler registry integrity valid; no executable taskbook is invisible to the V2 registry.")
        return 0
    if args.command == "status":
        states, registry_issues = effective_states(config, events, current)
        print_json({"schema": V2_SCHEMA, "at": current.isoformat(), "registry_issues": registry_issues, "tasks": states})
        return 0
    if args.command == "select":
        chosen = select_task(config, events, current, kind=args.kind)
        print_json(chosen)
        return 0 if chosen is not None else 2
    raise AssertionError(args.command)


if __name__ == "__main__":
    try:
        sys.exit(main())
    except SchedulerError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        sys.exit(1)
