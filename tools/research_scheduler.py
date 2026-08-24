#!/usr/bin/env python3
"""Validate, inventory and reduce the Enterprise Math research scheduler V2.

V2 makes the scheduler a unified workflow registry rather than a static owner list.
The registry is materialized from three sources:

* the read-only V1 seed during migration;
* all taskbooks discoverable under ``research_tasks``;
* V2 PUBLISH / REGISTER_ORPHAN events from the append-only runtime log.

GitHub Issue #240 remains the append-only runtime coordination surface.  V1
events remain replayable so the migration cannot erase historical workflow state.

The scheduler deliberately does not decide mathematical truth or canonical status.
Research identity is runtime provenance: CLAIMs automatically resolve a stable
Researcher-ID when legacy callers do not supply one explicitly.
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
DEFAULT_TASKBOOK_DIR = ROOT / "research_tasks"
EVENT_SCHEMA_V2 = "ENTERPRISE_MATH_SCHEDULER_EVENT_V2"
EVENT_SCHEMA_V1 = "ENTERPRISE_MATH_SCHEDULER_EVENT_V1"
CONFIG_SCHEMA_V2 = "ENTERPRISE_MATH_RESEARCH_SCHEDULER_V2"
CONFIG_SCHEMA_V1 = "ENTERPRISE_MATH_RESEARCH_SCHEDULER_V1"

HARD_BLOCK_FIELDS = ("missing_object", "owner", "necessity", "unblock_condition")
ACTIVE_OWNER_STATES = {"ACTIVE_OWNER", "ACTIVE_BRIDGE"}
DEPENDENCY_ACTIONS = {"INFORM", "CONSUME", "TEST", "HARD_DEPENDENCY"}
RESEARCHER_ID_RE = re.compile(r"^EM-[A-Z0-9]+-(?:[0-9]{2}|[A-Z0-9]{4,8})$")
DRIVER_ID_RE = re.compile(r"^(?:EM-DRIVER-\d{2}|EM-DVR-[A-Z0-9]+)$")
TASK_LANE_RE = re.compile(r"^RS-((?:R|P)\d{3}[A-Z0-9]*)\b")
LANE_RE = re.compile(r"[^A-Z0-9]+")
TASKBOOK_META_RE = re.compile(r"<!--\s*ENTERPRISE_MATH_TASK_V1\s*(\{.*?\})\s*-->", re.S)
DISPATCHABLE_STATES = {"READY", "HANDOFF_READY"}
TERMINAL_STATES = {"DONE", "REJECTED", "SUPERSEDED"}
REVIEW_KINDS = {"DISPATCH", "RETURN", "ORPHAN_RECOVERY"}
REVIEW_VERDICTS = {"APPROVE", "REVISE", "REJECT"}


class SchedulerError(ValueError):
    pass


def load_json(path: pathlib.Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def load_scheduler_config(path: pathlib.Path = DEFAULT_CONFIG) -> dict[str, Any]:
    config = load_json(path)
    if config.get("schema") != CONFIG_SCHEMA_V2:
        return config
    legacy_path = config.get("legacy_seed_config")
    if not legacy_path:
        return config
    legacy_file = pathlib.Path(legacy_path)
    if not legacy_file.is_absolute():
        legacy_file = path.parent / legacy_file
    if not legacy_file.exists():
        raise SchedulerError(f"legacy seed config does not exist: {legacy_file}")
    legacy = load_json(legacy_file)
    if legacy.get("schema") != CONFIG_SCHEMA_V1:
        raise SchedulerError("legacy_seed_config is not an Enterprise Math scheduler V1 config")
    merged = copy.deepcopy(config)
    migrated_tasks: list[dict[str, Any]] = []
    for item in legacy.get("tasks", []):
        migrated = copy.deepcopy(item)
        migrated.setdefault("registry_source", "LEGACY_STATIC_SEED")
        migrated.setdefault("publication_review_state", "LEGACY_PREAPPROVED")
        migrated_tasks.append(migrated)
    migrated_tasks.extend(copy.deepcopy(config.get("tasks", [])))
    merged["tasks"] = migrated_tasks
    merged["_legacy_seed"] = legacy
    return merged


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


def researcher_id_for_claim(task: dict[str, Any], claim_id: str) -> str:
    lane = identity_lane(task)
    digest = hashlib.sha256(f"{task['task_id']}\0{claim_id}".encode("utf-8")).hexdigest()[:6].upper()
    return f"EM-{lane}-{digest}"


def release_claim_identity(state: dict[str, Any]) -> None:
    if state.get("researcher_id"):
        state["last_researcher_id"] = state["researcher_id"]
    state["researcher_id"] = None
    state["identity_source"] = None


def _validate_task(
    task: dict[str, Any],
    *,
    task_states: set[str],
    priorities: set[str],
    leverage: set[str],
    active_owners: set[str],
    require_active_owner: bool,
    prefix: str,
) -> list[str]:
    errors: list[str] = []
    task_id = task.get("task_id")
    if not isinstance(task_id, str) or not task_id:
        return [f"{prefix}: missing task_id"]

    if "identity_lane" in task:
        try:
            identity_lane(task)
        except SchedulerError as exc:
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
        if require_active_owner and owner not in active_owners:
            errors.append(f"{task_id}: research owner is not ACTIVE_OWNER/ACTIVE_BRIDGE: {owner!r}")
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
    return errors


def validate_scheduler(config: dict[str, Any], owners: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    schema = config.get("schema")
    if schema not in {CONFIG_SCHEMA_V2, CONFIG_SCHEMA_V1}:
        errors.append("unexpected scheduler schema")

    task_states = set(config.get("task_states", []))
    event_types = set(config.get("event_types", []))
    if schema == CONFIG_SCHEMA_V2:
        required_states = {
            "PENDING_REVIEW", "READY", "HANDOFF_READY", "RETURNED", "BLOCKED",
            "ORPHANED", "DONE", "REJECTED", "SUPERSEDED",
        }
        required_events = {
            "PUBLISH", "REGISTER_ORPHAN", "REVIEW", "CLAIM", "HEARTBEAT",
            "PROGRESS", "RETURN", "HANDOFF", "HARD_BLOCK", "UNBLOCK",
            "ORPHAN", "ADOPT", "SUPERSEDE",
        }
    else:
        required_states = {"READY", "HANDOFF_READY", "BLOCKED", "DONE", "SUPERSEDED"}
        required_events = {"CLAIM", "HEARTBEAT", "PROGRESS", "HANDOFF", "HARD_BLOCK", "UNBLOCK", "DONE", "SUPERSEDE"}
    if not required_states <= task_states:
        errors.append("scheduler task_states are incomplete")
    if not required_events <= event_types:
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
        task_id = task.get("task_id")
        if isinstance(task_id, str):
            if task_id in seen:
                errors.append(f"duplicate task_id: {task_id}")
            seen.add(task_id)
        task_errors = _validate_task(
            task,
            task_states=task_states,
            priorities=priorities,
            leverage=leverage,
            active_owners=active_owners,
            require_active_owner=True,
            prefix=f"tasks[{index}]",
        )
        errors.extend(task_errors)
        if task.get("kind") == "RESEARCH" and task.get("owner") in active_owners:
            covered_active.add(task["owner"])

    if config.get("require_static_owner_coverage", True):
        missing_coverage = sorted(active_owners - covered_active)
        if missing_coverage:
            errors.append("active research owners missing scheduler coverage: " + ", ".join(missing_coverage))
    return errors


def active_research_owner_names(owners: dict[str, Any]) -> set[str]:
    return {
        name
        for name, spec in owners.get("branches", {}).items()
        if spec.get("state") in ACTIVE_OWNER_STATES
    }


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


def extract_taskbook_task(path: pathlib.Path) -> tuple[dict[str, Any] | None, str | None]:
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as exc:
        return None, f"cannot read taskbook: {exc}"
    match = TASKBOOK_META_RE.search(text)
    if not match:
        return None, "missing ENTERPRISE_MATH_TASK_V1 metadata"
    try:
        task = json.loads(match.group(1))
    except json.JSONDecodeError as exc:
        return None, f"invalid taskbook JSON: {exc}"
    if not isinstance(task, dict):
        return None, "taskbook metadata is not an object"
    return task, None


def synthetic_orphan_id(path: pathlib.Path, *, prefix: str = "ORPHAN-FILE") -> str:
    digest = hashlib.sha256(str(path).encode("utf-8")).hexdigest()[:12].upper()
    return f"{prefix}-{digest}"


def discover_taskbooks(taskbook_dir: pathlib.Path | None = DEFAULT_TASKBOOK_DIR) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    if taskbook_dir is None or not taskbook_dir.exists():
        return [], []
    tasks: list[dict[str, Any]] = []
    diagnostics: list[dict[str, Any]] = []
    seen_task_ids: set[str] = set()
    for path in sorted(taskbook_dir.glob("*.md")):
        task, error = extract_taskbook_task(path)
        if error or task is None:
            task_id = synthetic_orphan_id(path)
            tasks.append(
                {
                    "task_id": task_id,
                    "title": path.name,
                    "kind": "RESEARCH",
                    "owner": "taskbook/unassigned",
                    "base_state": "ORPHANED",
                    "priority": "P3",
                    "leverage": "LOW",
                    "frontier": "Taskbook-like artifact is not machine-readable by Scheduler V2.",
                    "next_action": "Driver must inspect, register, repair, supersede, or classify this artifact.",
                    "dependencies": [],
                    "source_refs": [str(path.relative_to(ROOT)) if path.is_relative_to(ROOT) else str(path)],
                    "last_progress_ref": str(path),
                    "last_progress_at": "1970-01-01T00:00:00+00:00",
                    "hard_block": None,
                    "registry_source": "TASKBOOK_DISCOVERY_INVALID",
                    "taskbook_path": str(path),
                    "orphan_reason": error,
                }
            )
            diagnostics.append({"path": str(path), "task_id": task_id, "problem": error})
            continue
        task = copy.deepcopy(task)
        task_id = task.get("task_id")
        if not isinstance(task_id, str) or not task_id:
            synthetic = synthetic_orphan_id(path)
            diagnostics.append({"path": str(path), "task_id": synthetic, "problem": "metadata has no task_id"})
            task["task_id"] = synthetic
            task_id = synthetic
        if task_id in seen_task_ids:
            duplicate_id = synthetic_orphan_id(path, prefix="ORPHAN-DUP")
            diagnostics.append({"path": str(path), "task_id": duplicate_id, "problem": f"duplicate task_id {task_id}"})
            task["task_id"] = duplicate_id
            task["title"] = f"Duplicate taskbook registration for {task_id}: {path.name}"
            task["base_state"] = "ORPHANED"
            task["registry_source"] = "TASKBOOK_DISCOVERY_DUPLICATE"
            task["orphan_reason"] = f"duplicate task_id {task_id}"
            task["original_task_id"] = task_id
            task["taskbook_path"] = str(path)
            tasks.append(task)
            continue
        seen_task_ids.add(task_id)
        task.setdefault("registry_source", "TASKBOOK_DISCOVERY")
        task["taskbook_path"] = str(path)
        tasks.append(task)
    return tasks, diagnostics


def publication_task_from_event(event: dict[str, Any]) -> tuple[dict[str, Any] | None, str | None]:
    if event.get("schema") != EVENT_SCHEMA_V2:
        return None, "PUBLISH requires V2 event schema"
    publisher_role = event.get("publisher_role")
    if publisher_role not in {"RESEARCHER", "RESEARCH_DRIVER"}:
        return None, "PUBLISH publisher_role must be RESEARCHER or RESEARCH_DRIVER"
    publisher_id = event.get("publisher_id")
    if publisher_role == "RESEARCHER" and not valid_researcher_id(publisher_id):
        return None, "PUBLISH requires valid Researcher-ID"
    if publisher_role == "RESEARCH_DRIVER" and not valid_driver_id(publisher_id):
        return None, "PUBLISH requires valid Driver-ID"
    task = event.get("task")
    if not isinstance(task, dict):
        return None, "PUBLISH requires task object"
    task = copy.deepcopy(task)
    if task.get("task_id") != event.get("task_id"):
        return None, "PUBLISH task.task_id must equal event.task_id"
    task["base_state"] = "PENDING_REVIEW"
    task["registry_source"] = "PUBLISH_EVENT"
    task["publisher_id"] = str(publisher_id).strip().upper()
    task["publisher_role"] = publisher_role
    task["published_at"] = event.get("at")
    task["publication_review_state"] = "PENDING"
    return task, None


def orphan_task_from_event(event: dict[str, Any]) -> tuple[dict[str, Any] | None, str | None]:
    if event.get("schema") != EVENT_SCHEMA_V2:
        return None, "REGISTER_ORPHAN requires V2 event schema"
    task = event.get("task")
    if not isinstance(task, dict):
        return None, "REGISTER_ORPHAN requires task object"
    task = copy.deepcopy(task)
    if task.get("task_id") != event.get("task_id"):
        return None, "REGISTER_ORPHAN task.task_id must equal event.task_id"
    reason = event.get("orphan_reason")
    if not isinstance(reason, str) or not reason.strip():
        return None, "REGISTER_ORPHAN requires orphan_reason"
    task["base_state"] = "ORPHANED"
    task["registry_source"] = "REGISTER_ORPHAN_EVENT"
    task["orphan_reason"] = reason
    task["orphan_evidence_refs"] = copy.deepcopy(event.get("evidence_refs", []))
    return task, None


def materialize_tasks(
    config: dict[str, Any],
    events: list[dict[str, Any]],
    *,
    taskbook_dir: pathlib.Path | None = DEFAULT_TASKBOOK_DIR,
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    catalog: dict[str, dict[str, Any]] = {}
    diagnostics: list[dict[str, Any]] = []

    for task in config.get("tasks", []):
        item = copy.deepcopy(task)
        item.setdefault("registry_source", "STATIC_CONFIG")
        catalog[item["task_id"]] = item

    taskbooks, taskbook_diagnostics = discover_taskbooks(taskbook_dir)
    diagnostics.extend(taskbook_diagnostics)
    for task in taskbooks:
        task_id = task["task_id"]
        if task_id in catalog:
            catalog[task_id].setdefault("taskbook_path", task.get("taskbook_path"))
            continue
        item = copy.deepcopy(task)
        if item.get("base_state") != "ORPHANED":
            item["base_state"] = "ORPHANED"
            item["registry_source"] = "TASKBOOK_DISCOVERY_ORPHAN"
            item["orphan_reason"] = "TASKBOOK_NOT_REGISTERED_IN_SCHEDULER_V2"
        catalog[task_id] = item

    last_create_index: dict[str, int] = {}
    for index, event in enumerate(events):
        kind = event.get("event")
        if kind not in {"PUBLISH", "REGISTER_ORPHAN"}:
            continue
        task_id = event.get("task_id")
        if not isinstance(task_id, str) or not task_id:
            diagnostics.append({"event_index": index, "problem": f"{kind} missing task_id"})
            continue
        if kind == "PUBLISH":
            item, error = publication_task_from_event(event)
        else:
            item, error = orphan_task_from_event(event)
        if error or item is None:
            diagnostics.append({"event_index": index, "task_id": task_id, "problem": error})
            continue
        prior_index = last_create_index.get(task_id)
        if prior_index is not None:
            diagnostics.append({"event_index": index, "task_id": task_id, "problem": f"duplicate create event; prior index {prior_index}"})
            continue
        last_create_index[task_id] = index
        prior = catalog.get(task_id)
        if prior is not None and prior.get("registry_source") not in {
            "TASKBOOK_DISCOVERY_ORPHAN", "TASKBOOK_DISCOVERY_INVALID", "TASKBOOK_DISCOVERY_DUPLICATE"
        }:
            diagnostics.append({"event_index": index, "task_id": task_id, "problem": "task_id already registered"})
            continue
        if prior is not None and prior.get("taskbook_path") and not item.get("taskbook_path"):
            item["taskbook_path"] = prior["taskbook_path"]
        catalog[task_id] = item
    return [catalog[key] for key in sorted(catalog)], diagnostics


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
        "owner": task.get("owner"),
        "publisher_id": task.get("publisher_id"),
        "publisher_role": task.get("publisher_role"),
        "publication_review_state": task.get("publication_review_state"),
        "dispatch_review": None,
        "return_ref": None,
        "return_review": None,
        "orphan_reason": task.get("orphan_reason"),
        "orphan_evidence_refs": copy.deepcopy(task.get("orphan_evidence_refs", [])),
        "orphan_history": [],
        "orphan_recovery_review": None,
        "ignored_events": [],
    }


def expire_claim(state: dict[str, Any], at: datetime) -> None:
    lease_until = state.get("lease_until")
    if state.get("claim_id") and isinstance(lease_until, datetime) and at >= lease_until:
        orphan = {
            "source": "LEASE_EXPIRY",
            "reason": "CLAIM_LEASE_EXPIRED",
            "at": lease_until.isoformat(),
            "claim_id": state.get("claim_id"),
            "actor": state.get("actor"),
            "researcher_id": state.get("researcher_id"),
            "last_progress_ref": state.get("last_progress_ref"),
            "last_progress_at": state.get("last_progress_at"),
            "next_action": state.get("next_action"),
        }
        state["orphan_history"].append(orphan)
        state["state"] = "ORPHANED"
        state["orphan_reason"] = "CLAIM_LEASE_EXPIRED"
        state["orphan_evidence_refs"] = [state.get("last_progress_ref")] if state.get("last_progress_ref") else []
        state["claim_id"] = None
        state["actor"] = None
        release_claim_identity(state)
        state["lease_until"] = None


def ignore(state: dict[str, Any], index: int, reason: str) -> None:
    state["ignored_events"].append({"index": index, "reason": reason})


def event_actor_identity_matches_claim(state: dict[str, Any], event: dict[str, Any], kind: str) -> str | None:
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


def validate_reviewer(event: dict[str, Any]) -> str | None:
    reviewer_id = event.get("reviewer_id")
    if not valid_driver_id(reviewer_id):
        return "REVIEW requires a valid Driver-ID reviewer_id"
    if event.get("review_kind") not in REVIEW_KINDS:
        return f"invalid review_kind {event.get('review_kind')!r}"
    if event.get("verdict") not in REVIEW_VERDICTS:
        return f"invalid review verdict {event.get('verdict')!r}"
    if not isinstance(event.get("review_ref"), str) or not event["review_ref"].strip():
        return "REVIEW requires review_ref"
    return None


def review_is_independent(state: dict[str, Any], event: dict[str, Any], review_kind: str) -> str | None:
    reviewer = str(event.get("reviewer_id", "")).strip().upper()
    if review_kind == "DISPATCH" and state.get("publisher_role") == "RESEARCH_DRIVER":
        publisher = str(state.get("publisher_id", "")).strip().upper()
        if publisher and reviewer == publisher:
            return "Driver publisher cannot self-review DISPATCH"
    return None


def reduce_task(
    task: dict[str, Any],
    events: Iterable[dict[str, Any]],
    *,
    default_lease_minutes: int,
    now: datetime,
    active_research_owners: set[str] | None = None,
) -> dict[str, Any]:
    state = state_from_task(task)
    matching = [event for event in events if event.get("task_id") == task["task_id"]]

    last_event_time: datetime | None = None
    for index, event in enumerate(matching):
        schema = event.get("schema")
        if schema not in (None, EVENT_SCHEMA_V1, EVENT_SCHEMA_V2):
            ignore(state, index, "wrong event schema")
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

        kind = event.get("event")
        claim_id = event.get("claim_id")
        live_claim = state.get("claim_id")

        if kind in {"PUBLISH", "REGISTER_ORPHAN"}:
            # Creation was already consumed by materialize_tasks().
            continue

        if kind == "REVIEW":
            if schema != EVENT_SCHEMA_V2:
                ignore(state, index, "REVIEW requires V2 event schema")
                continue
            reviewer_error = validate_reviewer(event)
            if reviewer_error:
                ignore(state, index, reviewer_error)
                continue
            review_kind = event["review_kind"]
            verdict = event["verdict"]
            independent_error = review_is_independent(state, event, review_kind)
            if independent_error:
                ignore(state, index, independent_error)
                continue
            review_record = {
                "reviewer_id": event["reviewer_id"],
                "review_ref": event["review_ref"],
                "verdict": verdict,
                "at": event["at"],
                "note": event.get("note"),
            }

            if review_kind == "DISPATCH":
                if state["state"] != "PENDING_REVIEW":
                    ignore(state, index, "DISPATCH review requires PENDING_REVIEW")
                    continue
                state["dispatch_review"] = review_record
                if verdict == "APPROVE":
                    assigned_owner = event.get("assigned_owner") or task.get("owner")
                    if assigned_owner == "taskbook/unassigned" or not isinstance(assigned_owner, str) or not assigned_owner.strip():
                        ignore(state, index, "DISPATCH APPROVE requires a concrete assigned_owner")
                        state["dispatch_review"] = None
                        continue
                    if (
                        task.get("kind") == "RESEARCH"
                        and active_research_owners is not None
                        and assigned_owner not in active_research_owners
                    ):
                        ignore(state, index, f"DISPATCH APPROVE owner is not ACTIVE_OWNER/ACTIVE_BRIDGE: {assigned_owner!r}")
                        state["dispatch_review"] = None
                        continue
                    if task.get("kind") == "GOVERNANCE" and assigned_owner != "governance":
                        ignore(state, index, "GOVERNANCE dispatch must assign owner='governance'")
                        state["dispatch_review"] = None
                        continue
                    task["owner"] = assigned_owner
                    state["owner"] = assigned_owner
                    state["state"] = "READY"
                    state["publication_review_state"] = "APPROVED"
                    state["last_progress_at"] = event["at"]
                elif verdict == "REVISE":
                    state["publication_review_state"] = "REVISION_REQUIRED"
                    if event.get("next_action"):
                        state["next_action"] = event["next_action"]
                else:
                    state["state"] = "REJECTED"
                    state["publication_review_state"] = "REJECTED"
                    state["last_progress_at"] = event["at"]
                continue

            if review_kind == "RETURN":
                if state["state"] != "RETURNED":
                    ignore(state, index, "RETURN review requires RETURNED")
                    continue
                state["return_review"] = review_record
                if verdict == "APPROVE":
                    state["state"] = "DONE"
                    state["last_progress_ref"] = event.get("progress_ref") or state.get("return_ref") or event["review_ref"]
                    state["last_progress_at"] = event["at"]
                elif verdict == "REVISE":
                    if not isinstance(event.get("next_action"), str) or not event["next_action"].strip():
                        ignore(state, index, "RETURN review REVISE requires next_action")
                        state["return_review"] = None
                        continue
                    state["state"] = "HANDOFF_READY"
                    state["next_action"] = event["next_action"]
                    state["last_progress_at"] = event["at"]
                else:
                    state["state"] = "REJECTED"
                    state["last_progress_at"] = event["at"]
                continue

            if review_kind == "ORPHAN_RECOVERY":
                if state["state"] != "ORPHANED":
                    ignore(state, index, "ORPHAN_RECOVERY review requires ORPHANED")
                    continue
                state["orphan_recovery_review"] = review_record
                if verdict == "APPROVE":
                    if (
                        task.get("kind") == "RESEARCH"
                        and active_research_owners is not None
                        and state.get("owner") not in active_research_owners
                    ):
                        ignore(state, index, f"ORPHAN_RECOVERY owner is not ACTIVE_OWNER/ACTIVE_BRIDGE: {state.get('owner')!r}")
                        state["orphan_recovery_review"] = None
                        continue
                    state["state"] = "HANDOFF_READY"
                    state["orphan_reason"] = None
                    if event.get("next_action"):
                        state["next_action"] = event["next_action"]
                    state["last_progress_at"] = event["at"]
                elif verdict == "REVISE":
                    if event.get("next_action"):
                        state["next_action"] = event["next_action"]
                else:
                    state["state"] = "SUPERSEDED"
                    state["last_progress_at"] = event["at"]
                continue

        if kind == "CLAIM":
            if (
                task.get("kind") == "RESEARCH"
                and active_research_owners is not None
                and state.get("owner") not in active_research_owners
            ):
                ignore(state, index, f"CLAIM owner is not ACTIVE_OWNER/ACTIVE_BRIDGE: {state.get('owner')!r}")
                continue
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
            researcher_id = (
                supplied_researcher_id.strip().upper()
                if isinstance(supplied_researcher_id, str)
                else researcher_id_for_claim(task, claim_id)
            )
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
            state["identity_source"] = "EVENT" if supplied_researcher_id is not None else "AUTO_CLAIM_DERIVED"
            state["lease_until"] = at + duration
            continue

        if kind in {"HEARTBEAT", "PROGRESS", "RETURN", "HANDOFF", "HARD_BLOCK"}:
            identity_error = event_actor_identity_matches_claim(state, event, str(kind))
            if identity_error:
                ignore(state, index, identity_error)
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

        if kind == "RETURN":
            if schema != EVENT_SCHEMA_V2:
                ignore(state, index, "RETURN requires V2 event schema")
                continue
            return_ref = event.get("return_ref") or event.get("progress_ref")
            if not isinstance(return_ref, str) or not return_ref.strip():
                ignore(state, index, "RETURN requires return_ref")
                continue
            state["state"] = "RETURNED"
            state["return_ref"] = return_ref
            state["last_progress_ref"] = return_ref
            state["last_progress_at"] = event["at"]
            if event.get("next_action"):
                state["next_action"] = event["next_action"]
            state["claim_id"] = None
            state["actor"] = None
            release_claim_identity(state)
            state["lease_until"] = None
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

        if kind == "ORPHAN":
            if schema != EVENT_SCHEMA_V2:
                ignore(state, index, "ORPHAN requires V2 event schema")
                continue
            if state["state"] in TERMINAL_STATES:
                ignore(state, index, "terminal task cannot be orphaned")
                continue
            reason = event.get("orphan_reason")
            if not isinstance(reason, str) or not reason.strip():
                ignore(state, index, "ORPHAN requires orphan_reason")
                continue
            state["orphan_history"].append(
                {
                    "source": "EVENT",
                    "reason": reason,
                    "at": event["at"],
                    "claim_id": state.get("claim_id"),
                    "actor": state.get("actor"),
                    "researcher_id": state.get("researcher_id"),
                    "evidence_refs": copy.deepcopy(event.get("evidence_refs", [])),
                }
            )
            state["state"] = "ORPHANED"
            state["orphan_reason"] = reason
            state["orphan_evidence_refs"] = copy.deepcopy(event.get("evidence_refs", []))
            state["claim_id"] = None
            state["actor"] = None
            release_claim_identity(state)
            state["lease_until"] = None
            state["last_progress_at"] = event["at"]
            continue

        if kind == "ADOPT":
            if schema != EVENT_SCHEMA_V2:
                ignore(state, index, "ADOPT requires V2 event schema")
                continue
            if state["state"] != "ORPHANED":
                ignore(state, index, "ADOPT requires ORPHANED state")
                continue
            if (
                task.get("kind") == "RESEARCH"
                and active_research_owners is not None
                and state.get("owner") not in active_research_owners
            ):
                ignore(state, index, f"ADOPT owner is not ACTIVE_OWNER/ACTIVE_BRIDGE: {state.get('owner')!r}")
                continue
            reviewer_id = event.get("reviewer_id")
            if not valid_driver_id(reviewer_id):
                ignore(state, index, "ADOPT requires valid Driver-ID reviewer_id")
                continue
            if not isinstance(event.get("review_ref"), str) or not event["review_ref"].strip():
                ignore(state, index, "ADOPT requires review_ref")
                continue
            state["state"] = "HANDOFF_READY"
            state["orphan_reason"] = None
            state["orphan_recovery_review"] = {
                "reviewer_id": reviewer_id,
                "review_ref": event["review_ref"],
                "verdict": "APPROVE",
                "at": event["at"],
                "note": event.get("note"),
            }
            if event.get("next_action"):
                state["next_action"] = event["next_action"]
            state["last_progress_at"] = event["at"]
            continue

        if kind == "DONE":
            if schema == EVENT_SCHEMA_V1:
                # Preserve historical event semantics during migration.
                if not live_claim or claim_id != live_claim:
                    ignore(state, index, "legacy DONE requires current live claim_id")
                    continue
                state["state"] = "DONE"
                state["return_review"] = {"legacy": True, "review_ref": event.get("progress_ref"), "at": event["at"]}
                if event.get("progress_ref"):
                    state["last_progress_ref"] = event["progress_ref"]
                state["last_progress_at"] = event["at"]
                state["claim_id"] = None
                state["actor"] = None
                release_claim_identity(state)
                state["lease_until"] = None
            else:
                ignore(state, index, "V2 forbids unreviewed DONE; use RETURN then REVIEW/RETURN APPROVE")
            continue

        if kind == "SUPERSEDE":
            if schema == EVENT_SCHEMA_V2:
                reviewer_id = event.get("reviewer_id")
                if not valid_driver_id(reviewer_id):
                    ignore(state, index, "V2 SUPERSEDE requires valid Driver-ID reviewer_id")
                    continue
                if not isinstance(event.get("review_ref"), str) or not event["review_ref"].strip():
                    ignore(state, index, "V2 SUPERSEDE requires review_ref")
                    continue
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

    if state["state"] in TERMINAL_STATES:
        state["dispatch_state"] = "COMPLETE"
    elif state["state"] == "BLOCKED" and complete_hard_block(state.get("hard_block")):
        state["dispatch_state"] = "BLOCKED"
    elif state["state"] == "PENDING_REVIEW" or state["state"] == "RETURNED":
        state["dispatch_state"] = "NEEDS_REVIEW"
    elif state["state"] == "ORPHANED":
        state["dispatch_state"] = "ORPHANED"
    elif state.get("claim_id"):
        state["dispatch_state"] = "LEASED"
    elif state["state"] in DISPATCHABLE_STATES:
        state["dispatch_state"] = "NEEDS_DISPATCH"
    else:
        state["dispatch_state"] = "DORMANT"
    return state


def effective_states(
    config: dict[str, Any],
    events: list[dict[str, Any]],
    now: datetime,
    *,
    taskbook_dir: pathlib.Path | None = DEFAULT_TASKBOOK_DIR,
    owners: dict[str, Any] | None = None,
) -> list[dict[str, Any]]:
    default_lease = int(config.get("claim_lease_minutes", 120))
    tasks, catalog_diagnostics = materialize_tasks(config, events, taskbook_dir=taskbook_dir)
    active_owners = active_research_owner_names(owners) if owners is not None else None
    results = []
    for task in tasks:
        reduced = reduce_task(
            task,
            events,
            default_lease_minutes=default_lease,
            now=now,
            active_research_owners=active_owners,
        )
        reduced.update(
            {
                "title": task.get("title"),
                "kind": task.get("kind"),
                "owner": reduced.get("owner", task.get("owner")),
                "priority": task.get("priority"),
                "leverage": task.get("leverage"),
                "frontier": task.get("frontier"),
                "source_refs": task.get("source_refs", []),
                "identity_lane": identity_lane(task),
                "registry_source": task.get("registry_source"),
                "taskbook_path": task.get("taskbook_path"),
            }
        )
        results.append(reduced)
    if catalog_diagnostics:
        for result in results:
            result.setdefault("catalog_diagnostics_count", len(catalog_diagnostics))
    return results


def scheduler_snapshot(
    config: dict[str, Any],
    events: list[dict[str, Any]],
    now: datetime,
    *,
    taskbook_dir: pathlib.Path | None = DEFAULT_TASKBOOK_DIR,
    owners: dict[str, Any] | None = None,
) -> dict[str, Any]:
    tasks, diagnostics = materialize_tasks(config, events, taskbook_dir=taskbook_dir)
    states = effective_states(config, events, now, taskbook_dir=taskbook_dir, owners=owners)
    counts: dict[str, int] = {}
    for state in states:
        counts[state["dispatch_state"]] = counts.get(state["dispatch_state"], 0) + 1
    return {
        "schema": "ENTERPRISE_MATH_RESEARCH_SCHEDULER_SNAPSHOT_V2",
        "at": now.isoformat(),
        "registered_task_count": len(tasks),
        "dispatch_counts": counts,
        "catalog_diagnostics": diagnostics,
        "tasks": states,
    }


def select_task(
    config: dict[str, Any],
    events: list[dict[str, Any]],
    now: datetime,
    *,
    kind: str = "RESEARCH",
    taskbook_dir: pathlib.Path | None = DEFAULT_TASKBOOK_DIR,
    owners: dict[str, Any] | None = None,
) -> dict[str, Any] | None:
    policy = config["selection_policy"]
    states = effective_states(config, events, now, taskbook_dir=taskbook_dir, owners=owners)
    task_by_id, _ = materialize_tasks(config, events, taskbook_dir=taskbook_dir)
    task_lookup = {task["task_id"]: task for task in task_by_id}
    state_rank = {name: index for index, name in enumerate(policy["state_order"])}
    priority_rank = {name: index for index, name in enumerate(policy["priority_order"])}
    leverage_rank = {name: index for index, name in enumerate(policy["leverage_order"])}

    candidates = [
        state for state in states
        if state["dispatch_state"] == "NEEDS_DISPATCH"
        and (kind == "ANY" or state["kind"] == kind)
    ]
    if not candidates:
        return None

    def candidate_key(state: dict[str, Any]) -> tuple[Any, ...]:
        task = task_lookup[state["task_id"]]
        try:
            last_progress = parse_time(state["last_progress_at"])
        except (TypeError, ValueError):
            last_progress = datetime(1970, 1, 1, tzinfo=timezone.utc)
        return (
            state_rank.get(state["state"], len(state_rank)),
            priority_rank.get(task["priority"], len(priority_rank)),
            leverage_rank.get(task["leverage"], len(leverage_rank)),
            last_progress,
            task["task_id"],
        )

    return min(candidates, key=candidate_key)


def registry_audit(
    config: dict[str, Any],
    events: list[dict[str, Any]],
    now: datetime,
    *,
    taskbook_dir: pathlib.Path | None = DEFAULT_TASKBOOK_DIR,
    owners: dict[str, Any] | None = None,
) -> dict[str, Any]:
    snapshot = scheduler_snapshot(config, events, now, taskbook_dir=taskbook_dir, owners=owners)
    orphaned = [task for task in snapshot["tasks"] if task["dispatch_state"] == "ORPHANED"]
    needs_review = [task for task in snapshot["tasks"] if task["dispatch_state"] == "NEEDS_REVIEW"]
    invalid_events = [
        {"task_id": task["task_id"], "ignored_events": task["ignored_events"]}
        for task in snapshot["tasks"]
        if task["ignored_events"]
    ]
    return {
        "schema": "ENTERPRISE_MATH_RESEARCH_REGISTRY_AUDIT_V2",
        "at": now.isoformat(),
        "registered_task_count": snapshot["registered_task_count"],
        "orphaned_count": len(orphaned),
        "needs_review_count": len(needs_review),
        "catalog_diagnostics": snapshot["catalog_diagnostics"],
        "orphaned": orphaned,
        "invalid_event_groups": invalid_events,
    }


def print_json(value: Any) -> None:
    print(json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True))


def load_emit_task_payload(args: argparse.Namespace) -> dict[str, Any]:
    if getattr(args, "task_json", None):
        payload = load_json(args.task_json)
        if not isinstance(payload, dict):
            raise SchedulerError("--task-json must contain one task object")
        return payload
    if getattr(args, "taskbook", None):
        payload, error = extract_taskbook_task(args.taskbook)
        if error or payload is None:
            raise SchedulerError(error or "taskbook metadata unavailable")
        return payload
    raise SchedulerError("publish/orphan registration requires --task-json or --taskbook")


def emit_event(kind: str, args: argparse.Namespace) -> dict[str, Any]:
    event: dict[str, Any] = {
        "schema": EVENT_SCHEMA_V2,
        "event": kind,
        "task_id": args.task_id,
        "actor": getattr(args, "actor", None),
        "at": args.at,
    }
    if kind in {"PUBLISH", "REGISTER_ORPHAN"}:
        event["task"] = load_emit_task_payload(args)
    if kind == "PUBLISH":
        event["publisher_id"] = args.publisher_id
        event["publisher_role"] = args.publisher_role
    elif kind == "REGISTER_ORPHAN":
        event["orphan_reason"] = args.orphan_reason
        event["evidence_refs"] = args.evidence_refs or []
    elif kind in {"CLAIM", "HEARTBEAT", "PROGRESS", "RETURN", "HANDOFF", "HARD_BLOCK"}:
        event["claim_id"] = args.claim_id
        if getattr(args, "researcher_id", None):
            event["researcher_id"] = args.researcher_id
        if getattr(args, "lease_minutes", None):
            event["lease_minutes"] = args.lease_minutes
        if getattr(args, "progress_ref", None):
            event["progress_ref"] = args.progress_ref
        if getattr(args, "return_ref", None):
            event["return_ref"] = args.return_ref
        if getattr(args, "next_action", None):
            event["next_action"] = args.next_action
        if kind == "HARD_BLOCK":
            event["hard_block"] = {
                "missing_object": args.missing_object,
                "owner": args.block_owner,
                "necessity": args.necessity,
                "unblock_condition": args.unblock_condition,
            }
    elif kind == "UNBLOCK":
        event["next_action"] = args.next_action
    elif kind == "REVIEW":
        event.update(
            {
                "review_kind": args.review_kind,
                "verdict": args.verdict,
                "reviewer_id": args.reviewer_id,
                "review_ref": args.review_ref,
            }
        )
        if args.next_action:
            event["next_action"] = args.next_action
        if args.assigned_owner:
            event["assigned_owner"] = args.assigned_owner
        if args.note:
            event["note"] = args.note
    elif kind == "ORPHAN":
        event["orphan_reason"] = args.orphan_reason
        event["evidence_refs"] = args.evidence_refs or []
    elif kind == "ADOPT":
        event["reviewer_id"] = args.reviewer_id
        event["review_ref"] = args.review_ref
        if args.next_action:
            event["next_action"] = args.next_action
        if args.note:
            event["note"] = args.note
    elif kind == "SUPERSEDE":
        event["reviewer_id"] = args.reviewer_id
        event["review_ref"] = args.review_ref
        if args.next_action:
            event["next_action"] = args.next_action
    return event


def select_review(
    config: dict[str, Any],
    events: list[dict[str, Any]],
    now: datetime,
    *,
    reviewer_id: str | None = None,
    taskbook_dir: pathlib.Path | None = DEFAULT_TASKBOOK_DIR,
    owners: dict[str, Any] | None = None,
) -> dict[str, Any] | None:
    states = effective_states(config, events, now, taskbook_dir=taskbook_dir, owners=owners)
    candidates = [state for state in states if state["dispatch_state"] == "NEEDS_REVIEW"]
    reviewer = reviewer_id.strip().upper() if isinstance(reviewer_id, str) else None
    if reviewer:
        candidates = [
            state for state in candidates
            if not (
                state["state"] == "PENDING_REVIEW"
                and state.get("publisher_role") == "RESEARCH_DRIVER"
                and str(state.get("publisher_id", "")).upper() == reviewer
            )
        ]
    if not candidates:
        return None
    priority_rank = {name: i for i, name in enumerate(config["selection_policy"]["priority_order"])}
    review_state_rank = {"RETURNED": 0, "PENDING_REVIEW": 1}
    return min(
        candidates,
        key=lambda state: (
            review_state_rank.get(state["state"], 9),
            priority_rank.get(state.get("priority"), 99),
            parse_time(state["last_progress_at"]) if state.get("last_progress_at") else datetime(1970, 1, 1, tzinfo=timezone.utc),
            state["task_id"],
        ),
    )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Enterprise Math research scheduler V2")
    parser.add_argument("--config", type=pathlib.Path, default=DEFAULT_CONFIG)
    parser.add_argument("--owners", type=pathlib.Path, default=DEFAULT_OWNERS)
    parser.add_argument("--taskbook-dir", type=pathlib.Path, default=DEFAULT_TASKBOOK_DIR)
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("validate")

    status = sub.add_parser("status")
    status.add_argument("--events", type=pathlib.Path)
    status.add_argument("--now")

    snapshot = sub.add_parser("snapshot")
    snapshot.add_argument("--events", type=pathlib.Path)
    snapshot.add_argument("--now")

    audit = sub.add_parser("audit-registry")
    audit.add_argument("--events", type=pathlib.Path)
    audit.add_argument("--now")
    audit.add_argument("--fail-on-invalid-events", action="store_true")

    select = sub.add_parser("select")
    select.add_argument("--events", type=pathlib.Path)
    select.add_argument("--now")
    select.add_argument("--kind", choices=["RESEARCH", "GOVERNANCE", "ANY"], default="RESEARCH")

    select_review_parser = sub.add_parser("select-review")
    select_review_parser.add_argument("--events", type=pathlib.Path)
    select_review_parser.add_argument("--now")
    select_review_parser.add_argument("--reviewer-id")

    identity = sub.add_parser("identity")
    identity.add_argument("--events", type=pathlib.Path)
    identity.add_argument("--task-id", required=True)
    identity.add_argument("--claim-id", required=True)

    emit = sub.add_parser("emit")
    emit_sub = emit.add_subparsers(dest="emit_kind", required=True)

    def add_common(p: argparse.ArgumentParser, *, actor: bool = True) -> None:
        p.add_argument("--task-id", required=True)
        p.add_argument("--at", required=True)
        if actor:
            p.add_argument("--actor", default="agent")

    publish = emit_sub.add_parser("publish")
    add_common(publish)
    source = publish.add_mutually_exclusive_group(required=True)
    source.add_argument("--task-json", type=pathlib.Path)
    source.add_argument("--taskbook", type=pathlib.Path)
    publish.add_argument("--publisher-id", required=True)
    publish.add_argument("--publisher-role", choices=["RESEARCHER", "RESEARCH_DRIVER"], required=True)

    register_orphan = emit_sub.add_parser("register-orphan")
    add_common(register_orphan)
    source = register_orphan.add_mutually_exclusive_group(required=True)
    source.add_argument("--task-json", type=pathlib.Path)
    source.add_argument("--taskbook", type=pathlib.Path)
    register_orphan.add_argument("--orphan-reason", required=True)
    register_orphan.add_argument("--evidence-refs", nargs="*")

    claim = emit_sub.add_parser("claim")
    add_common(claim)
    claim.add_argument("--claim-id", required=True)
    claim.add_argument("--researcher-id")
    claim.add_argument("--lease-minutes", type=int)

    heartbeat = emit_sub.add_parser("heartbeat")
    add_common(heartbeat)
    heartbeat.add_argument("--claim-id", required=True)
    heartbeat.add_argument("--researcher-id")
    heartbeat.add_argument("--lease-minutes", type=int)

    progress = emit_sub.add_parser("progress")
    add_common(progress)
    progress.add_argument("--claim-id", required=True)
    progress.add_argument("--progress-ref", required=True)
    progress.add_argument("--next-action", required=True)
    progress.add_argument("--researcher-id")
    progress.add_argument("--lease-minutes", type=int)

    ret = emit_sub.add_parser("return")
    add_common(ret)
    ret.add_argument("--claim-id", required=True)
    ret.add_argument("--return-ref", required=True)
    ret.add_argument("--next-action")
    ret.add_argument("--researcher-id")

    handoff = emit_sub.add_parser("handoff")
    add_common(handoff)
    handoff.add_argument("--claim-id", required=True)
    handoff.add_argument("--progress-ref")
    handoff.add_argument("--next-action", required=True)
    handoff.add_argument("--researcher-id")

    hard_block = emit_sub.add_parser("hard-block")
    add_common(hard_block)
    hard_block.add_argument("--claim-id", required=True)
    hard_block.add_argument("--researcher-id")
    hard_block.add_argument("--progress-ref")
    hard_block.add_argument("--missing-object", required=True)
    hard_block.add_argument("--block-owner", required=True)
    hard_block.add_argument("--necessity", required=True)
    hard_block.add_argument("--unblock-condition", required=True)

    unblock = emit_sub.add_parser("unblock")
    add_common(unblock)
    unblock.add_argument("--next-action", required=True)

    review = emit_sub.add_parser("review")
    add_common(review)
    review.add_argument("--review-kind", choices=sorted(REVIEW_KINDS), required=True)
    review.add_argument("--verdict", choices=sorted(REVIEW_VERDICTS), required=True)
    review.add_argument("--reviewer-id", required=True)
    review.add_argument("--review-ref", required=True)
    review.add_argument("--next-action")
    review.add_argument("--assigned-owner")
    review.add_argument("--note")

    orphan = emit_sub.add_parser("orphan")
    add_common(orphan)
    orphan.add_argument("--orphan-reason", required=True)
    orphan.add_argument("--evidence-refs", nargs="*")

    adopt = emit_sub.add_parser("adopt")
    add_common(adopt)
    adopt.add_argument("--reviewer-id", required=True)
    adopt.add_argument("--review-ref", required=True)
    adopt.add_argument("--next-action")
    adopt.add_argument("--note")

    supersede = emit_sub.add_parser("supersede")
    add_common(supersede)
    supersede.add_argument("--reviewer-id", required=True)
    supersede.add_argument("--review-ref", required=True)
    supersede.add_argument("--next-action")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    config = load_scheduler_config(args.config)
    owners = load_json(args.owners)
    errors = validate_scheduler(config, owners)

    if args.command == "validate":
        if errors:
            for error in errors:
                print(f"ERROR: {error}")
            return 1
        taskbooks, diagnostics = discover_taskbooks(args.taskbook_dir)
        snapshot = scheduler_snapshot(config, [], now_utc(None), taskbook_dir=args.taskbook_dir, owners=owners)
        print(
            "PASS: scheduler V2 config valid; "
            f"{len(config.get('tasks', []))} migration/static seeds; "
            f"{len(taskbooks)} taskbook artifacts discoverable; "
            f"{snapshot['registered_task_count']} total registry entries; "
            f"{len(diagnostics)} taskbook orphan diagnostics."
        )
        return 0

    if errors:
        raise SchedulerError("invalid scheduler configuration: " + "; ".join(errors))

    if args.command == "emit":
        kind = args.emit_kind.replace("-", "_").upper()
        print_json(emit_event(kind, args))
        return 0

    events = load_events(getattr(args, "events", None))
    current = now_utc(getattr(args, "now", None))

    if args.command == "identity":
        tasks, _ = materialize_tasks(config, events, taskbook_dir=args.taskbook_dir)
        task = next((item for item in tasks if item.get("task_id") == args.task_id), None)
        if task is None:
            raise SchedulerError(f"unknown task_id: {args.task_id}")
        print_json(
            {
                "task_id": args.task_id,
                "claim_id": args.claim_id,
                "identity_lane": identity_lane(task),
                "researcher_id": researcher_id_for_claim(task, args.claim_id),
                "identity_source": "AUTO_CLAIM_DERIVED",
            }
        )
        return 0

    if args.command == "status":
        print_json(effective_states(config, events, current, taskbook_dir=args.taskbook_dir, owners=owners))
        return 0
    if args.command == "snapshot":
        print_json(scheduler_snapshot(config, events, current, taskbook_dir=args.taskbook_dir, owners=owners))
        return 0
    if args.command == "audit-registry":
        audit = registry_audit(config, events, current, taskbook_dir=args.taskbook_dir, owners=owners)
        print_json(audit)
        if args.fail_on_invalid_events and audit["invalid_event_groups"]:
            return 1
        return 0
    if args.command == "select":
        chosen = select_task(config, events, current, kind=args.kind, taskbook_dir=args.taskbook_dir, owners=owners)
        print_json(chosen)
        return 0 if chosen is not None else 2
    if args.command == "select-review":
        chosen = select_review(config, events, current, reviewer_id=args.reviewer_id, taskbook_dir=args.taskbook_dir, owners=owners)
        print_json(chosen)
        return 0 if chosen is not None else 2
    raise AssertionError(args.command)


if __name__ == "__main__":
    sys.exit(main())
