#!/usr/bin/env python3
"""Enterprise Math Research Scheduler V2.

V2 is the canonical control plane for task publication, execution, return review,
and orphan recovery. Historical V1 events are accepted only before the V2
cutover timestamp. New work must use ENTERPRISE_MATH_SCHEDULER_EVENT_V2.

The scheduler coordinates work. It does not decide mathematical truth or
canonical promotion.
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
DEFAULT_CONFIG = ROOT / "research_scheduler.json"
DEFAULT_OWNERS = ROOT / "branch_governance_overrides.json"

V1_SCHEMA = "ENTERPRISE_MATH_SCHEDULER_EVENT_V1"
V2_SCHEMA = "ENTERPRISE_MATH_SCHEDULER_EVENT_V2"
TASKBOOK_PREFIX = "<!-- ENTERPRISE_MATH_TASK_V1\n"
TASKBOOK_SUFFIX = "\n-->"
HARD_BLOCK_FIELDS = ("missing_object", "owner", "necessity", "unblock_condition")
ACTIVE_OWNER_STATES = {"ACTIVE_OWNER", "ACTIVE_BRIDGE"}
DEPENDENCY_ACTIONS = {"INFORM", "CONSUME", "TEST", "HARD_DEPENDENCY"}
EXECUTION_ID_RE = re.compile(r"^EM-[A-Z0-9]+-(?:[0-9]{2}|[A-Z0-9]{4,8})$")
TASK_LANE_RE = re.compile(r"^RS-((?:R|P)\d{3}[A-Z0-9]*)\b")
LANE_RE = re.compile(r"[^A-Z0-9]+")
TASK_ID_TEXT_RE = re.compile(r"(?im)^\s*(?:Task-ID|Task-ID：|Task-ID:)\s*`?([A-Z0-9][A-Z0-9_-]+)`?\s*$")
IMMUTABLE_REF_RE = re.compile(r"^.+@[0-9a-fA-F]{7,64}$")


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


def nonempty(value: Any) -> bool:
    if isinstance(value, str):
        return bool(value.strip())
    if isinstance(value, (list, tuple, dict, set)):
        return bool(value)
    return value is not None


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
    return normalize_lane(task_id.split("-", 1)[0] or "DIRECT")


def valid_execution_id(value: Any) -> bool:
    return isinstance(value, str) and bool(EXECUTION_ID_RE.fullmatch(value.strip().upper()))


def valid_driver_id(value: Any) -> bool:
    if not valid_execution_id(value):
        return False
    normalized = str(value).strip().upper()
    return normalized == "EM-DRIVER-01" or normalized.startswith("EM-DVR-")


def researcher_id_for_claim(task: dict[str, Any], claim_id: str) -> str:
    lane = identity_lane(task)
    digest = hashlib.sha256(f"{task['task_id']}\0{claim_id}".encode("utf-8")).hexdigest()[:6].upper()
    return f"EM-{lane}-{digest}"


def event_time(event: dict[str, Any]) -> datetime:
    value = event.get("at")
    if not isinstance(value, str) or not value:
        raise SchedulerError("scheduler event requires ISO-8601 'at'")
    return parse_time(value)


def lease_duration(event: dict[str, Any], default_minutes: int) -> timedelta:
    minutes = event.get("lease_minutes", default_minutes)
    if not isinstance(minutes, int) or minutes <= 0:
        raise SchedulerError("lease_minutes must be a positive integer")
    return timedelta(minutes=minutes)


def review_lease_duration(event: dict[str, Any], default_minutes: int) -> timedelta:
    minutes = event.get("lease_minutes", default_minutes)
    if not isinstance(minutes, int) or minutes <= 0:
        raise SchedulerError("review lease_minutes must be a positive integer")
    return timedelta(minutes=minutes)


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
    if not all(isinstance(item, dict) for item in events):
        raise SchedulerError("every scheduler event must be an object")
    return events


def split_taskbook_metadata(text: str) -> dict[str, Any] | None:
    if not text.startswith(TASKBOOK_PREFIX):
        return None
    end = text.find(TASKBOOK_SUFFIX, len(TASKBOOK_PREFIX))
    if end < 0:
        return None
    try:
        value = json.loads(text[len(TASKBOOK_PREFIX):end])
    except json.JSONDecodeError:
        return None
    return value if isinstance(value, dict) else None


def _task_time(task: dict[str, Any]) -> datetime:
    raw = task.get("last_progress_at")
    if isinstance(raw, str):
        try:
            return parse_time(raw)
        except ValueError:
            pass
    return datetime(1970, 1, 1, tzinfo=timezone.utc)


def _normalize_task(task: dict[str, Any], *, source: str) -> dict[str, Any]:
    item = copy.deepcopy(task)
    item.setdefault("title", item.get("task_id", "unnamed task"))
    item.setdefault("kind", "RESEARCH")
    item.setdefault("owner", "unregistered")
    item.setdefault("priority", "P3")
    item.setdefault("leverage", "LOW")
    item.setdefault("frontier", "Recovered task requires control-plane reconciliation.")
    item.setdefault("next_action", "Inspect recovered task evidence and choose adopt, supersede, or close.")
    item.setdefault("dependencies", [])
    item.setdefault("source_refs", [])
    item.setdefault("evidence_status", "UNRECONCILED")
    item.setdefault("last_progress_ref", source)
    item.setdefault("last_progress_at", "1970-01-01T00:00:00+00:00")
    item.setdefault("hard_block", None)
    item.setdefault("tags", [])
    item["registry_source"] = source
    return item


def _load_legacy_config(config: dict[str, Any], root: pathlib.Path) -> dict[str, Any]:
    if config.get("schema") == "ENTERPRISE_MATH_RESEARCH_SCHEDULER_V1":
        return config
    rel = config.get("legacy_static_registry")
    if not isinstance(rel, str) or not rel.strip():
        return {"schema": "ENTERPRISE_MATH_RESEARCH_SCHEDULER_V1", "tasks": []}
    path = root / rel
    if not path.exists():
        raise SchedulerError(f"legacy_static_registry does not exist: {rel}")
    legacy = load_json(path)
    if legacy.get("schema") != "ENTERPRISE_MATH_RESEARCH_SCHEDULER_V1":
        raise SchedulerError("legacy_static_registry must use ENTERPRISE_MATH_RESEARCH_SCHEDULER_V1")
    return legacy


def _pre_v2_runtime_ids(config: dict[str, Any], events: list[dict[str, Any]]) -> set[str]:
    cutoff = parse_time(config["effective_at"])
    out: set[str] = set()
    for event in events:
        if event.get("schema") != V1_SCHEMA or not isinstance(event.get("task_id"), str):
            continue
        try:
            at = event_time(event)
        except (SchedulerError, ValueError):
            continue
        if at < cutoff:
            out.add(event["task_id"])
    return out


def discover_taskbooks(
    config: dict[str, Any], events: list[dict[str, Any]], *, root: pathlib.Path
) -> dict[str, dict[str, Any]]:
    """Discover every task-like Markdown artifact and give it a registry state.

    A structured taskbook that is already represented by the legacy static registry
    is left to that registry. A pre-V2 taskbook with valid historical runtime
    events may replay from its own base state. Every other pre-V2 taskbook is
    registered as ORPHANED rather than silently becoming dispatchable. A V2-aware
    taskbook is registered DRAFT until a PUBLISH event occurs.
    """
    task_dir = root / str(config.get("taskbook_root", "research_tasks"))
    if not task_dir.exists():
        return {}
    runtime_ids = _pre_v2_runtime_ids(config, events)
    grouped: dict[str, list[dict[str, Any]]] = {}
    for path in sorted(task_dir.glob("*.md")):
        try:
            text = path.read_text(encoding="utf-8")
        except OSError:
            continue
        meta = split_taskbook_metadata(text)
        if meta is not None and isinstance(meta.get("task_id"), str) and meta["task_id"].strip():
            task_id = meta["task_id"].strip()
            item = _normalize_task(meta, source=f"taskbook:{path.relative_to(root)}")
            item["taskbook_path"] = str(path.relative_to(root))
            marker = item.get("scheduler_registration")
            marker_v2 = marker == "PUBLISH_AND_CROSS_REVIEW_REQUIRED" or (
                isinstance(marker, dict) and marker.get("schema") == "ENTERPRISE_MATH_SCHEDULER_TASK_REGISTRATION_V2"
            )
            if marker_v2:
                item["base_state"] = "DRAFT"
                item["registry_status"] = "REGISTERED_AWAITING_PUBLISH"
            elif task_id in runtime_ids:
                state = item.get("base_state")
                if state not in set(config.get("task_states", [])):
                    item["base_state"] = "READY"
                item["registry_status"] = "MIGRATED_RUNTIME_TOUCHED"
            else:
                item["pre_orphan_state"] = item.get("base_state")
                item["base_state"] = "ORPHANED"
                item["orphan_seed"] = {
                    "reason": "UNREGISTERED_TASKBOOK_DISCOVERED",
                    "taskbook_ref": str(path.relative_to(root)),
                }
                item["registry_status"] = "ORPHAN_REGISTERED"
            grouped.setdefault(task_id, []).append(item)
            continue
        match = TASK_ID_TEXT_RE.search(text)
        if match:
            task_id = match.group(1)
            synthetic = _normalize_task({
                "task_id": task_id,
                "title": path.stem.replace("_", " "),
                "base_state": "ORPHANED",
                "last_progress_ref": str(path.relative_to(root)),
                "last_progress_at": "1970-01-01T00:00:00+00:00",
                "source_refs": [str(path.relative_to(root))],
            }, source=f"legacy-task-artifact:{path.relative_to(root)}")
            synthetic["taskbook_path"] = str(path.relative_to(root))
            synthetic["orphan_seed"] = {
                "reason": "LEGACY_TASK_ARTIFACT_WITHOUT_STRUCTURED_REGISTRATION",
                "taskbook_ref": str(path.relative_to(root)),
            }
            synthetic["registry_status"] = "ORPHAN_REGISTERED"
            grouped.setdefault(task_id, []).append(synthetic)

    out: dict[str, dict[str, Any]] = {}
    for task_id, items in grouped.items():
        primary = max(items, key=_task_time)
        primary = copy.deepcopy(primary)
        primary["taskbook_aliases"] = sorted({str(item.get("taskbook_path")) for item in items if item.get("taskbook_path")})
        out[task_id] = primary
    return out


def _valid_publish_envelope(event: dict[str, Any]) -> bool:
    task = event.get("task")
    return (
        event.get("schema") == V2_SCHEMA
        and event.get("event") in {"PUBLISH", "MIGRATE", "ORPHAN"}
        and isinstance(event.get("task_id"), str)
        and isinstance(task, dict)
        and task.get("task_id") == event.get("task_id")
    )


def materialize_tasks(
    config: dict[str, Any], events: list[dict[str, Any]], *, root: pathlib.Path = ROOT
) -> list[dict[str, Any]]:
    legacy = _load_legacy_config(config, root)
    by_id: dict[str, dict[str, Any]] = {}
    order: list[str] = []
    for task in legacy.get("tasks", []):
        if not isinstance(task, dict) or not isinstance(task.get("task_id"), str):
            continue
        task_id = task["task_id"]
        by_id[task_id] = _normalize_task(task, source="legacy-static-registry")
        order.append(task_id)

    discovered = discover_taskbooks(config, events, root=root)
    for task_id, task in discovered.items():
        if task_id in by_id:
            merged = by_id[task_id]
            merged["taskbook_aliases"] = task.get("taskbook_aliases", [])
            if task.get("taskbook_path"):
                merged["taskbook_path"] = task["taskbook_path"]
            continue
        by_id[task_id] = task
        order.append(task_id)

    for event in events:
        if not _valid_publish_envelope(event):
            continue
        task_id = event["task_id"]
        payload = _normalize_task(event["task"], source=f"event:{event['event']}")
        if task_id not in by_id:
            order.append(task_id)
        existing = by_id.get(task_id, {})
        aliases = existing.get("taskbook_aliases", [])
        by_id[task_id] = payload
        if aliases:
            by_id[task_id]["taskbook_aliases"] = aliases

    return [by_id[task_id] for task_id in order]


def validate_scheduler(
    config: dict[str, Any], owners: dict[str, Any], *, root: pathlib.Path = ROOT
) -> list[str]:
    errors: list[str] = []
    if config.get("schema") != "ENTERPRISE_MATH_RESEARCH_SCHEDULER_V2":
        errors.append("unexpected scheduler schema")
        return errors
    try:
        parse_time(str(config.get("effective_at", "")))
    except ValueError:
        errors.append("invalid effective_at")
    task_states = set(config.get("task_states", []))
    required_states = {
        "DRAFT", "REVIEW_PENDING", "READY", "CLAIMED", "IN_PROGRESS",
        "HANDOFF_READY", "RETURN_REVIEW", "ORPHANED", "BLOCKED", "BACKLOG",
        "DONE", "REJECTED", "SUPERSEDED",
    }
    if not required_states <= task_states:
        errors.append("scheduler task_states are incomplete")
    event_types = set(config.get("event_types", []))
    required_events = {
        "PUBLISH", "REVIEW_CLAIM", "REVIEW_HEARTBEAT", "REVIEW_HANDOFF",
        "APPROVE", "REJECT", "CLAIM", "ADOPT", "HEARTBEAT", "PROGRESS",
        "HANDOFF", "SUBMIT", "REVIEW", "ORPHAN", "HARD_BLOCK", "UNBLOCK",
        "MIGRATE", "SUPERSEDE",
    }
    if not required_events <= event_types:
        errors.append("scheduler event_types are incomplete")
    if config.get("direct_done_allowed") is not False:
        errors.append("V2 must forbid direct DONE")
    if config.get("orphan_contract", {}).get("lease_expiry_state") != "ORPHANED":
        errors.append("lease expiry must produce ORPHANED")
    if config.get("review_contract", {}).get("cross_driver_required") is not True:
        errors.append("cross-driver review must be required")
    if config.get("publication_contract", {}).get("free_researcher_may_publish_pending") is not True:
        errors.append("free researchers must be able to publish pending tasks")

    try:
        legacy = _load_legacy_config(config, root)
    except (SchedulerError, OSError, json.JSONDecodeError) as exc:
        errors.append(str(exc))
        return errors
    owner_entries = owners.get("branches", {})
    active_owners = {
        name for name, spec in owner_entries.items()
        if isinstance(spec, dict) and spec.get("state") in ACTIVE_OWNER_STATES
    }
    covered_active: set[str] = set()
    seen: set[str] = set()
    priorities = set(config.get("selection_policy", {}).get("priority_order", []))
    leverage = set(config.get("selection_policy", {}).get("leverage_order", []))
    for index, task in enumerate(legacy.get("tasks", [])):
        if not isinstance(task, dict):
            errors.append(f"legacy tasks[{index}] is not an object")
            continue
        task_id = task.get("task_id")
        if not isinstance(task_id, str) or not task_id:
            errors.append(f"legacy tasks[{index}]: missing task_id")
            continue
        if task_id in seen:
            errors.append(f"duplicate legacy task_id: {task_id}")
        seen.add(task_id)
        owner = task.get("owner")
        if task.get("kind") == "RESEARCH" and owner in active_owners:
            covered_active.add(owner)
        if task.get("priority") not in priorities:
            errors.append(f"{task_id}: invalid priority {task.get('priority')!r}")
        if task.get("leverage") not in leverage:
            errors.append(f"{task_id}: invalid leverage {task.get('leverage')!r}")
        if task.get("hard_block") is not None and not complete_hard_block(task.get("hard_block")):
            errors.append(f"{task_id}: partial hard_block is invalid")
        for dep_index, dependency in enumerate(task.get("dependencies", [])):
            if isinstance(dependency, dict) and dependency.get("action") not in DEPENDENCY_ACTIONS:
                errors.append(f"{task_id}: dependency[{dep_index}] has invalid action {dependency.get('action')!r}")
    missing = sorted(active_owners - covered_active)
    if missing:
        errors.append("active research owners missing legacy scheduler coverage: " + ", ".join(missing))
    return errors


def release_claim_identity(state: dict[str, Any]) -> None:
    if state.get("execution_id"):
        state["last_execution_id"] = state["execution_id"]
    state["execution_id"] = None
    state["researcher_id"] = None
    state["actor"] = None


def release_review_claim(state: dict[str, Any]) -> None:
    state["review_claim_id"] = None
    state["reviewer_id"] = None
    state["review_lease_until"] = None


def state_from_task(task: dict[str, Any]) -> dict[str, Any]:
    state = {
        "task_id": task["task_id"],
        "state": task.get("base_state", "ORPHANED"),
        "generation": 0,
        "claim_id": None,
        "actor": None,
        "execution_id": None,
        "researcher_id": None,
        "last_execution_id": None,
        "lease_until": None,
        "review_claim_id": None,
        "reviewer_id": None,
        "review_lease_until": None,
        "publisher_id": None,
        "publisher_role": None,
        "published_at": None,
        "publication_ref": None,
        "approval": None,
        "submission": None,
        "review": None,
        "hard_block": copy.deepcopy(task.get("hard_block")),
        "last_progress_ref": task.get("last_progress_ref"),
        "last_progress_at": task.get("last_progress_at"),
        "next_action": task.get("next_action"),
        "orphan_records": [],
        "review_abandonments": [],
        "migration": None,
        "ignored_events": [],
    }
    seed = task.get("orphan_seed")
    if state["state"] == "ORPHANED" and isinstance(seed, dict):
        state["orphan_records"].append(copy.deepcopy(seed))
    for key in ("title", "kind", "owner", "priority", "leverage", "frontier", "source_refs", "registry_source", "registry_status", "taskbook_path", "taskbook_aliases"):
        if key in task:
            state[key] = copy.deepcopy(task[key])
    return state


def _orphan(state: dict[str, Any], at: datetime, *, reason: str, ref: Any = None) -> None:
    record = {
        "reason": reason,
        "orphaned_at": at.isoformat(),
        "claim_id": state.get("claim_id"),
        "execution_id": state.get("execution_id"),
        "actor": state.get("actor"),
        "last_progress_ref": state.get("last_progress_ref"),
        "next_action": state.get("next_action"),
    }
    if ref:
        record["recovery_ref"] = ref
    state["orphan_records"].append(record)
    state["state"] = "ORPHANED"
    state["claim_id"] = None
    release_claim_identity(state)
    state["lease_until"] = None
    release_review_claim(state)


def expire_claim(state: dict[str, Any], at: datetime) -> None:
    lease = state.get("lease_until")
    if state.get("claim_id") and isinstance(lease, datetime) and at >= lease:
        _orphan(state, at, reason="LEASE_EXPIRED")


def expire_review_claim(state: dict[str, Any], at: datetime) -> None:
    lease = state.get("review_lease_until")
    if state.get("review_claim_id") and isinstance(lease, datetime) and at >= lease:
        state["review_abandonments"].append({
            "reason": "REVIEW_LEASE_EXPIRED",
            "at": at.isoformat(),
            "review_claim_id": state.get("review_claim_id"),
            "reviewer_id": state.get("reviewer_id"),
        })
        release_review_claim(state)


def ignore(state: dict[str, Any], index: int, reason: str) -> None:
    state["ignored_events"].append({"index": index, "reason": reason})


def _event_execution_id(event: dict[str, Any], task: dict[str, Any], claim_id: str) -> str | None:
    for field in ("execution_id", "researcher_id", "driver_id", "actor_id"):
        value = event.get(field)
        if valid_execution_id(value):
            return str(value).strip().upper()
    if event.get("actor_role") == "RESEARCHER":
        return researcher_id_for_claim(task, claim_id)
    return None


def _driver_for_event(event: dict[str, Any]) -> str | None:
    for field in ("driver_id", "reviewer_id", "actor_id"):
        value = event.get(field)
        if valid_driver_id(value):
            return str(value).strip().upper()
    return None


def _immutable_ref(value: Any) -> bool:
    return isinstance(value, str) and bool(IMMUTABLE_REF_RE.fullmatch(value.strip()))


def _claim_matches(state: dict[str, Any], event: dict[str, Any]) -> bool:
    if not state.get("claim_id") or event.get("claim_id") != state.get("claim_id"):
        return False
    supplied = event.get("execution_id") or event.get("researcher_id") or event.get("driver_id") or event.get("actor_id")
    if supplied is None:
        return True
    return valid_execution_id(supplied) and str(supplied).strip().upper() == state.get("execution_id")


def _review_claim_matches(state: dict[str, Any], event: dict[str, Any]) -> bool:
    driver = _driver_for_event(event)
    return (
        bool(state.get("review_claim_id"))
        and event.get("review_claim_id") == state.get("review_claim_id")
        and driver == state.get("reviewer_id")
    )


def _update_task_metadata(state: dict[str, Any], payload: dict[str, Any]) -> None:
    for key in ("title", "kind", "owner", "priority", "leverage", "frontier", "source_refs"):
        if key in payload:
            state[key] = copy.deepcopy(payload[key])
    if payload.get("next_action"):
        state["next_action"] = payload["next_action"]
    if payload.get("last_progress_at"):
        state["last_progress_at"] = payload["last_progress_at"]
    if payload.get("last_progress_ref"):
        state["last_progress_ref"] = payload["last_progress_ref"]


def _handle_v1_event(
    state: dict[str, Any], task: dict[str, Any], event: dict[str, Any], index: int,
    *, at: datetime, default_lease_minutes: int
) -> None:
    kind = event.get("event")
    claim_id = event.get("claim_id")
    if kind == "CLAIM":
        if state["state"] not in {"READY", "HANDOFF_READY"} or state.get("claim_id"):
            ignore(state, index, "legacy task is not dispatchable")
            return
        if not isinstance(claim_id, str) or not claim_id:
            ignore(state, index, "legacy CLAIM requires claim_id")
            return
        execution_id = event.get("researcher_id")
        if execution_id is not None and not valid_execution_id(execution_id):
            ignore(state, index, "legacy CLAIM researcher_id invalid")
            return
        execution_id = str(execution_id).strip().upper() if execution_id else researcher_id_for_claim(task, claim_id)
        try:
            duration = lease_duration(event, default_lease_minutes)
        except SchedulerError as exc:
            ignore(state, index, str(exc))
            return
        state.update({"state": "CLAIMED", "claim_id": claim_id, "actor": event.get("actor"), "execution_id": execution_id, "researcher_id": execution_id, "lease_until": at + duration})
        return
    if kind in {"HEARTBEAT", "PROGRESS", "HANDOFF", "HARD_BLOCK", "DONE"} and not _claim_matches(state, event):
        ignore(state, index, f"legacy {kind} requires current live claim")
        return
    if kind == "HEARTBEAT":
        try:
            state["lease_until"] = at + lease_duration(event, default_lease_minutes)
        except SchedulerError as exc:
            ignore(state, index, str(exc))
    elif kind == "PROGRESS":
        try:
            state["lease_until"] = at + lease_duration(event, default_lease_minutes)
        except SchedulerError as exc:
            ignore(state, index, str(exc))
            return
        state["state"] = "IN_PROGRESS"
        state["last_progress_at"] = event["at"]
        if event.get("progress_ref"):
            state["last_progress_ref"] = event["progress_ref"]
        if event.get("next_action"):
            state["next_action"] = event["next_action"]
    elif kind == "HANDOFF":
        if not nonempty(event.get("next_action")):
            ignore(state, index, "legacy HANDOFF requires next_action")
            return
        state["state"] = "HANDOFF_READY"
        state["last_progress_at"] = event["at"]
        state["next_action"] = event["next_action"]
        if event.get("progress_ref"):
            state["last_progress_ref"] = event["progress_ref"]
        state["claim_id"] = None
        release_claim_identity(state)
        state["lease_until"] = None
    elif kind == "HARD_BLOCK":
        if not complete_hard_block(event.get("hard_block")):
            ignore(state, index, "legacy HARD_BLOCK incomplete")
            return
        state["state"] = "BLOCKED"
        state["hard_block"] = copy.deepcopy(event["hard_block"])
        state["claim_id"] = None
        release_claim_identity(state)
        state["lease_until"] = None
    elif kind == "UNBLOCK":
        if state["state"] != "BLOCKED":
            ignore(state, index, "legacy UNBLOCK requires BLOCKED")
            return
        state["state"] = "HANDOFF_READY"
        state["hard_block"] = None
    elif kind == "DONE":
        state["state"] = "DONE"
        state["review"] = {"authority": "LEGACY_V1_PRE_CUTOVER", "at": event["at"]}
        if event.get("progress_ref"):
            state["last_progress_ref"] = event["progress_ref"]
        state["claim_id"] = None
        release_claim_identity(state)
        state["lease_until"] = None
    elif kind == "SUPERSEDE":
        state["state"] = "SUPERSEDED"
        state["claim_id"] = None
        release_claim_identity(state)
        state["lease_until"] = None
    else:
        ignore(state, index, f"unknown legacy event type: {kind!r}")


def reduce_task(
    task: dict[str, Any], events: Iterable[dict[str, Any]], *, config: dict[str, Any], now: datetime
) -> dict[str, Any]:
    state = state_from_task(task)
    matching = [event for event in events if event.get("task_id") == task["task_id"]]
    cutoff = parse_time(config["effective_at"])
    default_lease = int(config.get("claim_lease_minutes", 120))
    default_review_lease = int(config.get("review_lease_minutes", 120))
    last_event_time: datetime | None = None

    for index, event in enumerate(matching):
        try:
            at = event_time(event)
        except (SchedulerError, ValueError) as exc:
            ignore(state, index, str(exc))
            continue
        if last_event_time is not None and at < last_event_time:
            ignore(state, index, "events must be supplied in append-only comment order with nondecreasing event time")
            continue
        last_event_time = at
        expire_claim(state, at)
        expire_review_claim(state, at)
        schema = event.get("schema")
        if schema == V1_SCHEMA:
            if at >= cutoff:
                ignore(state, index, "V1 event schema retired at V2 cutover")
                continue
            _handle_v1_event(state, task, event, index, at=at, default_lease_minutes=default_lease)
            continue
        if schema != V2_SCHEMA:
            ignore(state, index, "wrong event schema")
            continue

        kind = event.get("event")
        if kind == "PUBLISH":
            payload = event.get("task")
            publisher_id = event.get("publisher_id") or event.get("actor_id")
            role = event.get("publisher_role") or event.get("actor_role")
            if not isinstance(payload, dict) or payload.get("task_id") != task["task_id"]:
                ignore(state, index, "PUBLISH requires matching task payload")
                continue
            if role not in {"RESEARCHER", "RESEARCH_DRIVER", "FOUNDATION_STEWARD", "USER"}:
                ignore(state, index, "PUBLISH requires allowed publisher_role")
                continue
            if role != "USER" and not valid_execution_id(publisher_id):
                ignore(state, index, "PUBLISH requires valid publisher identity")
                continue
            state["generation"] += 1
            state["state"] = "REVIEW_PENDING"
            state["publisher_id"] = str(publisher_id).strip().upper() if isinstance(publisher_id, str) else "USER"
            state["publisher_role"] = role
            state["published_at"] = event["at"]
            state["publication_ref"] = event.get("publication_ref") or event.get("taskbook_ref")
            state["claim_id"] = None
            release_claim_identity(state)
            state["lease_until"] = None
            release_review_claim(state)
            state["hard_block"] = None
            state["submission"] = None
            state["review"] = None
            _update_task_metadata(state, payload)
            continue

        if kind == "REVIEW_CLAIM":
            if state["state"] not in {"REVIEW_PENDING", "RETURN_REVIEW"} or state.get("review_claim_id"):
                ignore(state, index, "task is not awaiting an unclaimed review")
                continue
            driver = _driver_for_event(event)
            claim = event.get("review_claim_id")
            if driver is None or not isinstance(claim, str) or not claim:
                ignore(state, index, "REVIEW_CLAIM requires Driver-ID and review_claim_id")
                continue
            if driver == state.get("publisher_id") or driver == (state.get("submission") or {}).get("submitted_by"):
                ignore(state, index, "cross-driver review forbids publisher/submitter self-review")
                continue
            try:
                duration = review_lease_duration(event, default_review_lease)
            except SchedulerError as exc:
                ignore(state, index, str(exc))
                continue
            state["review_claim_id"] = claim
            state["reviewer_id"] = driver
            state["review_lease_until"] = at + duration
            continue

        if kind in {"REVIEW_HEARTBEAT", "REVIEW_HANDOFF", "APPROVE", "REJECT", "REVIEW"} and not _review_claim_matches(state, event):
            ignore(state, index, f"{kind} requires current cross-driver review claim")
            continue

        if kind == "REVIEW_HEARTBEAT":
            try:
                state["review_lease_until"] = at + review_lease_duration(event, default_review_lease)
            except SchedulerError as exc:
                ignore(state, index, str(exc))
            continue
        if kind == "REVIEW_HANDOFF":
            if event.get("next_action"):
                state["next_action"] = event["next_action"]
            release_review_claim(state)
            continue

        if kind == "APPROVE":
            if state["state"] != "REVIEW_PENDING":
                ignore(state, index, "APPROVE requires REVIEW_PENDING")
                continue
            ref = event.get("taskbook_ref")
            if not _immutable_ref(ref):
                ignore(state, index, "APPROVE requires immutable taskbook_ref path@sha")
                continue
            state["approval"] = {"reviewer_id": state.get("reviewer_id"), "review_ref": event.get("review_ref"), "taskbook_ref": ref, "at": event["at"]}
            state["state"] = "READY"
            release_review_claim(state)
            continue
        if kind == "REJECT":
            if state["state"] != "REVIEW_PENDING":
                ignore(state, index, "REJECT requires REVIEW_PENDING")
                continue
            state["review"] = {"reviewer_id": state.get("reviewer_id"), "verdict": "REJECT", "review_ref": event.get("review_ref"), "at": event["at"]}
            state["state"] = "REJECTED"
            release_review_claim(state)
            continue

        if kind == "CLAIM":
            if state["state"] not in {"READY", "HANDOFF_READY"} or state.get("claim_id"):
                ignore(state, index, "task is not dispatchable")
                continue
            claim_id = event.get("claim_id")
            if not isinstance(claim_id, str) or not claim_id:
                ignore(state, index, "CLAIM requires claim_id")
                continue
            execution_id = _event_execution_id(event, task, claim_id)
            if execution_id is None:
                ignore(state, index, "CLAIM requires or derives a valid execution identity")
                continue
            try:
                duration = lease_duration(event, default_lease)
            except SchedulerError as exc:
                ignore(state, index, str(exc))
                continue
            state.update({"state": "CLAIMED", "claim_id": claim_id, "actor": event.get("actor"), "execution_id": execution_id, "researcher_id": execution_id if not execution_id.startswith("EM-DVR-") else None, "lease_until": at + duration})
            continue

        if kind == "ADOPT":
            if state["state"] != "ORPHANED" or state.get("claim_id"):
                ignore(state, index, "ADOPT requires ORPHANED task")
                continue
            claim_id = event.get("claim_id")
            if not isinstance(claim_id, str) or not claim_id or not nonempty(event.get("recovery_ref")):
                ignore(state, index, "ADOPT requires claim_id and recovery_ref")
                continue
            execution_id = _event_execution_id(event, task, claim_id)
            if execution_id is None:
                ignore(state, index, "ADOPT requires valid execution identity")
                continue
            try:
                duration = lease_duration(event, default_lease)
            except SchedulerError as exc:
                ignore(state, index, str(exc))
                continue
            state.update({"state": "CLAIMED", "claim_id": claim_id, "actor": event.get("actor"), "execution_id": execution_id, "researcher_id": execution_id if not execution_id.startswith("EM-DVR-") else None, "lease_until": at + duration})
            state["orphan_records"].append({"reason": "ADOPTED", "at": event["at"], "adopted_by": execution_id, "recovery_ref": event["recovery_ref"]})
            continue

        if kind in {"HEARTBEAT", "PROGRESS", "HANDOFF", "SUBMIT", "HARD_BLOCK"} and not _claim_matches(state, event):
            ignore(state, index, f"{kind} requires current live claim")
            continue
        if kind == "HEARTBEAT":
            try:
                state["lease_until"] = at + lease_duration(event, default_lease)
            except SchedulerError as exc:
                ignore(state, index, str(exc))
            continue
        if kind == "PROGRESS":
            try:
                state["lease_until"] = at + lease_duration(event, default_lease)
            except SchedulerError as exc:
                ignore(state, index, str(exc))
                continue
            state["state"] = "IN_PROGRESS"
            state["last_progress_at"] = event["at"]
            if event.get("progress_ref"):
                state["last_progress_ref"] = event["progress_ref"]
            if event.get("next_action"):
                state["next_action"] = event["next_action"]
            continue
        if kind == "HANDOFF":
            if not nonempty(event.get("next_action")):
                ignore(state, index, "HANDOFF requires next_action")
                continue
            state["state"] = "HANDOFF_READY"
            state["last_progress_at"] = event["at"]
            state["next_action"] = event["next_action"]
            if event.get("progress_ref"):
                state["last_progress_ref"] = event["progress_ref"]
            state["claim_id"] = None
            release_claim_identity(state)
            state["lease_until"] = None
            continue
        if kind == "SUBMIT":
            if not nonempty(event.get("return_ref")):
                ignore(state, index, "SUBMIT requires return_ref")
                continue
            submitted_by = state.get("execution_id")
            state["submission"] = {"submitted_by": submitted_by, "return_ref": event["return_ref"], "evidence_refs": copy.deepcopy(event.get("evidence_refs", [])), "at": event["at"]}
            state["state"] = "RETURN_REVIEW"
            state["last_progress_at"] = event["at"]
            state["last_progress_ref"] = event["return_ref"]
            state["claim_id"] = None
            release_claim_identity(state)
            state["lease_until"] = None
            continue
        if kind == "HARD_BLOCK":
            if not complete_hard_block(event.get("hard_block")):
                ignore(state, index, "HARD_BLOCK requires all four fields")
                continue
            state["state"] = "BLOCKED"
            state["hard_block"] = copy.deepcopy(event["hard_block"])
            state["claim_id"] = None
            release_claim_identity(state)
            state["lease_until"] = None
            continue

        if kind == "REVIEW":
            if state["state"] != "RETURN_REVIEW":
                ignore(state, index, "REVIEW requires RETURN_REVIEW")
                continue
            verdict = event.get("verdict")
            allowed = set(config.get("review_contract", {}).get("verdicts", []))
            if verdict not in allowed or not nonempty(event.get("review_ref")):
                ignore(state, index, "REVIEW requires allowed verdict and review_ref")
                continue
            reviewer = state.get("reviewer_id")
            state["review"] = {"reviewer_id": reviewer, "verdict": verdict, "review_ref": event["review_ref"], "findings": copy.deepcopy(event.get("findings", [])), "at": event["at"]}
            release_review_claim(state)
            if verdict in {"ACCEPT", "ACCEPT_WITH_NARROWING", "ROUTE_TO_FOUNDATION", "PROMOTION_READY"}:
                state["state"] = "DONE"
            elif verdict in {"RETURN_TO_RESEARCH", "REQUEST_INDEPENDENT_REPLICATION"}:
                if not nonempty(event.get("next_action")):
                    ignore(state, index, "return/replication verdict requires next_action")
                    state["review"] = None
                    continue
                state["state"] = "HANDOFF_READY"
                state["next_action"] = event["next_action"]
            elif verdict == "PARK":
                state["state"] = "BACKLOG"
                state["next_action"] = event.get("next_action") or state.get("next_action")
            else:
                state["state"] = "REJECTED"
            continue

        if kind == "ORPHAN":
            reason = event.get("reason")
            if not isinstance(reason, str) or not reason.strip():
                ignore(state, index, "ORPHAN requires reason")
                continue
            driver = _driver_for_event(event)
            if driver is None and event.get("actor_role") != "SYSTEM":
                ignore(state, index, "ORPHAN requires Driver or SYSTEM authority")
                continue
            _orphan(state, at, reason=reason, ref=event.get("recovery_ref") or event.get("evidence_ref"))
            continue

        if kind == "UNBLOCK":
            if state["state"] != "BLOCKED":
                ignore(state, index, "UNBLOCK requires BLOCKED")
                continue
            driver = _driver_for_event(event)
            if driver is None:
                ignore(state, index, "UNBLOCK requires Driver-ID")
                continue
            state["state"] = "HANDOFF_READY"
            state["hard_block"] = None
            if event.get("next_action"):
                state["next_action"] = event["next_action"]
            continue

        if kind == "MIGRATE":
            driver = _driver_for_event(event)
            target = event.get("target_state")
            if driver is None or not nonempty(event.get("migration_ref")):
                ignore(state, index, "MIGRATE requires Driver-ID and migration_ref")
                continue
            allowed_targets = {"READY", "HANDOFF_READY", "IN_PROGRESS", "RETURN_REVIEW", "ORPHANED", "BACKLOG", "DONE", "SUPERSEDED"}
            if target not in allowed_targets:
                ignore(state, index, "MIGRATE target_state invalid")
                continue
            payload = event.get("task")
            if isinstance(payload, dict):
                _update_task_metadata(state, payload)
            state["migration"] = {"driver_id": driver, "migration_ref": event["migration_ref"], "at": event["at"], "target_state": target}
            state["state"] = target
            release_review_claim(state)
            state["claim_id"] = None
            release_claim_identity(state)
            state["lease_until"] = None
            if target == "IN_PROGRESS":
                claim_id = event.get("claim_id")
                execution_id = event.get("execution_id") or event.get("researcher_id")
                if not isinstance(claim_id, str) or not claim_id or not valid_execution_id(execution_id):
                    state["state"] = "ORPHANED"
                    state["orphan_records"].append({"reason": "INVALID_ACTIVE_MIGRATION", "at": event["at"], "migration_ref": event["migration_ref"]})
                    continue
                try:
                    duration = lease_duration(event, default_lease)
                except SchedulerError:
                    duration = timedelta(minutes=default_lease)
                state["claim_id"] = claim_id
                state["execution_id"] = str(execution_id).strip().upper()
                state["researcher_id"] = state["execution_id"] if not state["execution_id"].startswith("EM-DVR-") else None
                state["actor"] = event.get("actor")
                state["lease_until"] = at + duration
            elif target == "RETURN_REVIEW":
                submitted = event.get("submitted_by")
                if not valid_execution_id(submitted) or not nonempty(event.get("return_ref")):
                    state["state"] = "ORPHANED"
                    state["orphan_records"].append({"reason": "INVALID_RETURN_MIGRATION", "at": event["at"], "migration_ref": event["migration_ref"]})
                    continue
                state["submission"] = {"submitted_by": str(submitted).strip().upper(), "return_ref": event["return_ref"], "evidence_refs": copy.deepcopy(event.get("evidence_refs", [])), "at": event["at"]}
            continue

        if kind == "SUPERSEDE":
            driver = _driver_for_event(event)
            if driver is None:
                ignore(state, index, "SUPERSEDE requires Driver-ID")
                continue
            state["state"] = "SUPERSEDED"
            state["claim_id"] = None
            release_claim_identity(state)
            state["lease_until"] = None
            release_review_claim(state)
            if event.get("next_action"):
                state["next_action"] = event["next_action"]
            continue

        if kind == "DONE":
            ignore(state, index, "direct DONE is forbidden in V2; use SUBMIT -> cross-driver REVIEW")
            continue
        ignore(state, index, f"unknown V2 event type: {kind!r}")

    expire_claim(state, now)
    expire_review_claim(state, now)
    for key in ("lease_until", "review_lease_until"):
        if isinstance(state.get(key), datetime):
            state[key] = state[key].isoformat()
    if state["state"] in {"DONE", "REJECTED", "SUPERSEDED"}:
        state["dispatch_state"] = "COMPLETE"
    elif state["state"] == "BLOCKED":
        state["dispatch_state"] = "BLOCKED"
    elif state.get("claim_id"):
        state["dispatch_state"] = "LEASED"
    elif state.get("review_claim_id"):
        state["dispatch_state"] = "REVIEW_LEASED"
    elif state["state"] in {"REVIEW_PENDING", "RETURN_REVIEW"}:
        state["dispatch_state"] = "NEEDS_REVIEW"
    elif state["state"] == "ORPHANED":
        state["dispatch_state"] = "ORPHAN_RECOVERY"
    elif state["state"] in {"READY", "HANDOFF_READY"}:
        state["dispatch_state"] = "NEEDS_DISPATCH"
    else:
        state["dispatch_state"] = "DORMANT"
    return state


def effective_states(
    config: dict[str, Any], events: list[dict[str, Any]], now: datetime, *, root: pathlib.Path = ROOT
) -> list[dict[str, Any]]:
    return [reduce_task(task, events, config=config, now=now) for task in materialize_tasks(config, events, root=root)]


def select_task(
    config: dict[str, Any], events: list[dict[str, Any]], now: datetime, *, kind: str = "ANY", root: pathlib.Path = ROOT
) -> dict[str, Any] | None:
    policy = config["selection_policy"]
    states = [s for s in effective_states(config, events, now, root=root) if s["dispatch_state"] == "NEEDS_DISPATCH" and (kind == "ANY" or s.get("kind") == kind)]
    if not states:
        return None
    state_rank = {name: i for i, name in enumerate(policy["state_order"])}
    priority_rank = {name: i for i, name in enumerate(policy["priority_order"])}
    leverage_rank = {name: i for i, name in enumerate(policy["leverage_order"])}

    def key(state: dict[str, Any]) -> tuple[Any, ...]:
        try:
            last = parse_time(state.get("last_progress_at") or "1970-01-01T00:00:00+00:00")
        except ValueError:
            last = datetime(1970, 1, 1, tzinfo=timezone.utc)
        return (state_rank.get(state["state"], 99), priority_rank.get(state.get("priority"), 99), leverage_rank.get(state.get("leverage"), 99), last, state["task_id"])

    return min(states, key=key)


def select_review(
    config: dict[str, Any], events: list[dict[str, Any]], now: datetime, *, reviewer_id: str, root: pathlib.Path = ROOT
) -> dict[str, Any] | None:
    if not valid_driver_id(reviewer_id):
        raise SchedulerError("select-review requires a valid Driver-ID")
    reviewer = reviewer_id.strip().upper()
    states = []
    for state in effective_states(config, events, now, root=root):
        if state["dispatch_state"] != "NEEDS_REVIEW":
            continue
        if state.get("publisher_id") == reviewer:
            continue
        if (state.get("submission") or {}).get("submitted_by") == reviewer:
            continue
        states.append(state)
    if not states:
        return None
    priority_rank = {name: i for i, name in enumerate(config["selection_policy"]["priority_order"])}
    phase_rank = {"RETURN_REVIEW": 0, "REVIEW_PENDING": 1}

    def key(state: dict[str, Any]) -> tuple[Any, ...]:
        raw = (state.get("submission") or {}).get("at") or state.get("published_at") or state.get("last_progress_at") or "1970-01-01T00:00:00+00:00"
        try:
            when = parse_time(raw)
        except ValueError:
            when = datetime(1970, 1, 1, tzinfo=timezone.utc)
        return (phase_rank.get(state["state"], 9), priority_rank.get(state.get("priority"), 9), when, state["task_id"])

    return min(states, key=key)


def registry_report(config: dict[str, Any], events: list[dict[str, Any]], now: datetime, *, root: pathlib.Path = ROOT) -> dict[str, Any]:
    states = effective_states(config, events, now, root=root)
    counts: dict[str, int] = {}
    for state in states:
        counts[state["dispatch_state"]] = counts.get(state["dispatch_state"], 0) + 1
    return {
        "schema": "ENTERPRISE_MATH_RESEARCH_REGISTRY_REPORT_V2",
        "task_count": len(states),
        "dispatch_counts": dict(sorted(counts.items())),
        "orphans": [s["task_id"] for s in states if s["dispatch_state"] == "ORPHAN_RECOVERY"],
        "reviews": [s["task_id"] for s in states if s["dispatch_state"] == "NEEDS_REVIEW"],
        "active": [s["task_id"] for s in states if s["dispatch_state"] in {"LEASED", "REVIEW_LEASED"}],
        "dispatchable": [s["task_id"] for s in states if s["dispatch_state"] == "NEEDS_DISPATCH"],
    }


def print_json(value: Any) -> None:
    print(json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Enterprise Math Research Scheduler V2")
    parser.add_argument("--config", type=pathlib.Path, default=DEFAULT_CONFIG)
    parser.add_argument("--owners", type=pathlib.Path, default=DEFAULT_OWNERS)
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("validate")
    for name in ("status", "registry"):
        p = sub.add_parser(name)
        p.add_argument("--events", type=pathlib.Path)
        p.add_argument("--now")
    select = sub.add_parser("select")
    select.add_argument("--events", type=pathlib.Path)
    select.add_argument("--now")
    select.add_argument("--kind", default="ANY")
    review = sub.add_parser("select-review")
    review.add_argument("--events", type=pathlib.Path)
    review.add_argument("--now")
    review.add_argument("--reviewer-id", required=True)
    identity = sub.add_parser("identity")
    identity.add_argument("--task-id", required=True)
    identity.add_argument("--claim-id", required=True)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    config = load_json(args.config)
    owners = load_json(args.owners)
    root = args.config.resolve().parent
    errors = validate_scheduler(config, owners, root=root)
    if args.command == "validate":
        if errors:
            for error in errors:
                print(f"ERROR: {error}")
            return 1
        report = registry_report(config, [], now_utc(None), root=root)
        print(f"PASS: V2 scheduler valid; {report['task_count']} task identities are registered/discoverable; orphaned historical taskbooks are visible, not dispatchable.")
        return 0
    if errors:
        raise SchedulerError("invalid scheduler configuration: " + "; ".join(errors))
    if args.command == "identity":
        task = next((t for t in materialize_tasks(config, [], root=root) if t["task_id"] == args.task_id), None)
        if task is None:
            raise SchedulerError(f"unknown task_id: {args.task_id}")
        print_json({"task_id": args.task_id, "claim_id": args.claim_id, "identity_lane": identity_lane(task), "researcher_id": researcher_id_for_claim(task, args.claim_id)})
        return 0
    events = load_events(args.events)
    current = now_utc(args.now)
    if args.command == "status":
        print_json(effective_states(config, events, current, root=root))
        return 0
    if args.command == "registry":
        print_json(registry_report(config, events, current, root=root))
        return 0
    if args.command == "select":
        chosen = select_task(config, events, current, kind=args.kind, root=root)
        print_json(chosen)
        return 0 if chosen else 2
    if args.command == "select-review":
        chosen = select_review(config, events, current, reviewer_id=args.reviewer_id, root=root)
        print_json(chosen)
        return 0 if chosen else 2
    raise AssertionError(args.command)


if __name__ == "__main__":
    try:
        sys.exit(main())
    except SchedulerError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        sys.exit(1)
