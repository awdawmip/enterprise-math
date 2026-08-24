#!/usr/bin/env python3
"""Unified Enterprise Math task + Driver review state reducer.

The legacy research scheduler remains the task-state engine. This wrapper adds:
- dynamic TASK_PUBLISH events for Driver-approved taskbooks;
- a Driver cross-review queue on the same append-only Issue #240 event log;
- generic task/review selection without requiring the user to name an ID.

The tool does not decide theorem truth or canonical status.
"""
from __future__ import annotations

import argparse
import copy
import json
import pathlib
from datetime import datetime, timedelta, timezone
from typing import Any

from tools import research_scheduler as legacy

ROOT = pathlib.Path(__file__).resolve().parents[1]
DEFAULT_MACHINE = ROOT / "research_work_state_machine.json"
DEFAULT_SCHEDULER = ROOT / "research_scheduler.json"
WORK_SCHEMA = "ENTERPRISE_MATH_WORK_EVENT_V1"
LEGACY_SCHEMA = "ENTERPRISE_MATH_SCHEDULER_EVENT_V1"

REVIEW_EVENTS = {
    "REVIEW_REQUEST",
    "REVIEW_CLAIM",
    "REVIEW_PROGRESS",
    "REVIEW_HANDOFF",
    "REVIEW_DONE",
    "REVIEW_SUPERSEDE",
}
TASK_RUNTIME_EVENTS = {
    "CLAIM",
    "HEARTBEAT",
    "PROGRESS",
    "HANDOFF",
    "HARD_BLOCK",
    "UNBLOCK",
    "DONE",
    "SUPERSEDE",
}


class WorkStateError(ValueError):
    pass


def load_json(path: pathlib.Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def parse_time(value: str) -> datetime:
    return legacy.parse_time(value)


def load_events(path: pathlib.Path | None) -> list[dict[str, Any]]:
    if path is None:
        return []
    text = path.read_text(encoding="utf-8").strip()
    if not text:
        return []
    if text.startswith("["):
        data = json.loads(text)
        if not isinstance(data, list):
            raise WorkStateError("event JSON must be an array")
        events = data
    else:
        events = [json.loads(line) for line in text.splitlines() if line.strip()]
    if not all(isinstance(item, dict) for item in events):
        raise WorkStateError("every event must be an object")
    return events


def work_events(events: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return [e for e in events if e.get("schema") == WORK_SCHEMA]


def _required_nonempty(obj: dict[str, Any], fields: list[str]) -> list[str]:
    missing: list[str] = []
    for field in fields:
        value = obj.get(field)
        if value is None or value == "" or value == [] or value == {}:
            missing.append(field)
    return missing


def validate_task_publish(event: dict[str, Any], machine: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    required_event = machine["task_publication"]["required_event_fields"]
    missing = _required_nonempty(event, required_event)
    if missing:
        errors.append("TASK_PUBLISH missing event fields: " + ", ".join(missing))
        return errors
    try:
        parse_time(str(event["at"]))
    except (TypeError, ValueError):
        errors.append("TASK_PUBLISH has invalid at timestamp")
    ref = event.get("taskbook_ref")
    if not isinstance(ref, str) or "@" not in ref:
        errors.append("TASK_PUBLISH taskbook_ref must be immutable path@commit")
    task = event.get("task")
    if not isinstance(task, dict):
        errors.append("TASK_PUBLISH task must be an object")
        return errors
    missing_task = _required_nonempty(task, machine["task_publication"]["required_task_fields"])
    if "hard_block" in missing_task and "hard_block" in task:
        missing_task.remove("hard_block")
    if missing_task:
        errors.append("TASK_PUBLISH task missing fields: " + ", ".join(missing_task))
    if task.get("base_state") not in {"READY", "HANDOFF_READY"}:
        errors.append("TASK_PUBLISH task base_state must be READY or HANDOFF_READY")
    return errors


def composed_scheduler(
    legacy_config: dict[str, Any],
    events: list[dict[str, Any]],
    machine: dict[str, Any],
) -> dict[str, Any]:
    """Overlay latest valid TASK_PUBLISH definitions on legacy static tasks."""
    cfg = copy.deepcopy(legacy_config)
    by_id = {task["task_id"]: copy.deepcopy(task) for task in cfg.get("tasks", [])}
    order = [task["task_id"] for task in cfg.get("tasks", [])]

    for event in work_events(events):
        if event.get("event") != "TASK_PUBLISH":
            continue
        if validate_task_publish(event, machine):
            continue
        task = copy.deepcopy(event["task"])
        task_id = task["task_id"]
        if task_id not in by_id:
            order.append(task_id)
        by_id[task_id] = task

    cfg["tasks"] = [by_id[task_id] for task_id in order]
    return cfg


def normalized_task_events(events: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Return legacy-compatible task runtime events in board comment order."""
    out: list[dict[str, Any]] = []
    for event in events:
        if event.get("schema") == LEGACY_SCHEMA and event.get("event") in TASK_RUNTIME_EVENTS:
            out.append(event)
            continue
        if event.get("schema") == WORK_SCHEMA and event.get("event") in TASK_RUNTIME_EVENTS:
            clone = copy.deepcopy(event)
            clone["schema"] = LEGACY_SCHEMA
            out.append(clone)
    return out


def effective_task_states(
    legacy_config: dict[str, Any],
    events: list[dict[str, Any]],
    machine: dict[str, Any],
    now: datetime,
) -> list[dict[str, Any]]:
    cfg = composed_scheduler(legacy_config, events, machine)
    return legacy.effective_states(cfg, normalized_task_events(events), now)


def select_task(
    legacy_config: dict[str, Any],
    events: list[dict[str, Any]],
    machine: dict[str, Any],
    now: datetime,
    *,
    kind: str = "RESEARCH",
) -> dict[str, Any] | None:
    cfg = composed_scheduler(legacy_config, events, machine)
    return legacy.select_task(cfg, normalized_task_events(events), now, kind=kind)


def _review_base(event: dict[str, Any], machine: dict[str, Any]) -> dict[str, Any]:
    required = machine["review"]["required_review_request_fields"]
    missing = _required_nonempty(event, required)
    if missing:
        raise WorkStateError("REVIEW_REQUEST missing fields: " + ", ".join(missing))
    parse_time(str(event["at"]))
    return {
        "review_id": event["review_id"],
        "task_id": event["task_id"],
        "state": "READY",
        "priority": event["priority"],
        "originating_researcher_id": event["originating_researcher_id"],
        "issuer_driver_id": event.get("issuer_driver_id"),
        "review_objective": event["review_objective"],
        "target_refs": copy.deepcopy(event["target_refs"]),
        "evidence_refs": copy.deepcopy(event["evidence_refs"]),
        "execution_log_refs": copy.deepcopy(event["execution_log_refs"]),
        "requested_checks": copy.deepcopy(event["requested_checks"]),
        "requested_at": event["at"],
        "claim_id": None,
        "reviewer_driver_id": None,
        "lease_until": None,
        "last_progress_at": event["at"],
        "findings": None,
        "verdict": None,
        "next_action": None,
        "method_harvest": None,
        "successor_disposition": None,
        "ignored_events": [],
    }


def _expire_review(state: dict[str, Any], at: datetime) -> None:
    lease = state.get("lease_until")
    if state.get("claim_id") and isinstance(lease, datetime) and at >= lease:
        state["state"] = "HANDOFF_READY"
        state["claim_id"] = None
        state["reviewer_driver_id"] = None
        state["lease_until"] = None


def _review_ignore(state: dict[str, Any], index: int, reason: str) -> None:
    state["ignored_events"].append({"index": index, "reason": reason})


def reduce_reviews(
    events: list[dict[str, Any]],
    machine: dict[str, Any],
    now: datetime,
) -> list[dict[str, Any]]:
    states: dict[str, dict[str, Any]] = {}
    default_lease = int(machine["review"].get("claim_lease_minutes", 1440))
    allowed_verdicts = set(machine["review"]["review_done_verdicts"])
    done_required = machine["review"]["review_done_required_fields"]

    for index, event in enumerate(work_events(events)):
        kind = event.get("event")
        if kind not in REVIEW_EVENTS:
            continue

        review_id = event.get("review_id")
        if not isinstance(review_id, str) or not review_id:
            continue

        if kind == "REVIEW_REQUEST":
            if review_id in states:
                _review_ignore(states[review_id], index, "duplicate REVIEW_REQUEST")
                continue
            try:
                states[review_id] = _review_base(event, machine)
            except (WorkStateError, TypeError, ValueError):
                continue
            continue

        state = states.get(review_id)
        if state is None:
            continue

        try:
            at = parse_time(str(event.get("at", "")))
        except (TypeError, ValueError):
            _review_ignore(state, index, "invalid at timestamp")
            continue
        _expire_review(state, at)

        if kind == "REVIEW_CLAIM":
            if state["state"] not in {"READY", "HANDOFF_READY"} or state.get("claim_id"):
                _review_ignore(state, index, "review is not claimable")
                continue
            claim_id = event.get("claim_id")
            driver_id = event.get("reviewer_driver_id")
            if not isinstance(claim_id, str) or not claim_id:
                _review_ignore(state, index, "REVIEW_CLAIM requires claim_id")
                continue
            if not isinstance(driver_id, str) or not driver_id:
                _review_ignore(state, index, "REVIEW_CLAIM requires reviewer_driver_id")
                continue
            minutes = event.get("lease_minutes", default_lease)
            if not isinstance(minutes, int) or minutes <= 0:
                _review_ignore(state, index, "lease_minutes must be positive")
                continue
            state["state"] = "CLAIMED"
            state["claim_id"] = claim_id
            state["reviewer_driver_id"] = driver_id
            state["lease_until"] = at + timedelta(minutes=minutes)
            state["last_progress_at"] = event["at"]
            continue

        if kind in {"REVIEW_PROGRESS", "REVIEW_HANDOFF", "REVIEW_DONE"}:
            if (
                not state.get("claim_id")
                or event.get("claim_id") != state.get("claim_id")
                or event.get("reviewer_driver_id") != state.get("reviewer_driver_id")
            ):
                _review_ignore(state, index, f"{kind} requires current review claim and Driver-ID")
                continue

        if kind == "REVIEW_PROGRESS":
            minutes = event.get("lease_minutes", default_lease)
            if not isinstance(minutes, int) or minutes <= 0:
                _review_ignore(state, index, "lease_minutes must be positive")
                continue
            state["state"] = "IN_PROGRESS"
            state["lease_until"] = at + timedelta(minutes=minutes)
            state["last_progress_at"] = event["at"]
            if event.get("findings"):
                state["findings"] = event["findings"]
            if event.get("next_action"):
                state["next_action"] = event["next_action"]
            continue

        if kind == "REVIEW_HANDOFF":
            next_action = event.get("next_action")
            if not isinstance(next_action, str) or not next_action.strip():
                _review_ignore(state, index, "REVIEW_HANDOFF requires next_action")
                continue
            state["state"] = "HANDOFF_READY"
            state["next_action"] = next_action
            state["last_progress_at"] = event["at"]
            state["claim_id"] = None
            state["reviewer_driver_id"] = None
            state["lease_until"] = None
            continue

        if kind == "REVIEW_DONE":
            missing = _required_nonempty(event, done_required)
            if missing:
                _review_ignore(state, index, "REVIEW_DONE missing fields: " + ", ".join(missing))
                continue
            if event.get("verdict") not in allowed_verdicts:
                _review_ignore(state, index, "REVIEW_DONE verdict is not allowed")
                continue
            state["state"] = "DONE"
            state["verdict"] = event["verdict"]
            state["findings"] = copy.deepcopy(event["findings"])
            state["evidence_refs"] = copy.deepcopy(event["evidence_refs"])
            state["next_action"] = event["next_action"]
            state["method_harvest"] = copy.deepcopy(event["method_harvest"])
            state["successor_disposition"] = copy.deepcopy(event["successor_disposition"])
            state["same_driver_review"] = (
                bool(state.get("issuer_driver_id"))
                and state.get("issuer_driver_id") == state.get("reviewer_driver_id")
            )
            state["last_progress_at"] = event["at"]
            state["claim_id"] = None
            state["reviewer_driver_id"] = None
            state["lease_until"] = None
            continue

        if kind == "REVIEW_SUPERSEDE":
            state["state"] = "SUPERSEDED"
            state["last_progress_at"] = event["at"]
            state["claim_id"] = None
            state["reviewer_driver_id"] = None
            state["lease_until"] = None
            if event.get("next_action"):
                state["next_action"] = event["next_action"]

    out = []
    for state in states.values():
        _expire_review(state, now)
        lease = state.get("lease_until")
        state["lease_until"] = lease.isoformat() if isinstance(lease, datetime) else None
        if state["state"] in {"DONE", "SUPERSEDED"}:
            state["dispatch_state"] = "COMPLETE"
        elif state.get("claim_id"):
            state["dispatch_state"] = "LEASED"
        elif state["state"] in {"READY", "HANDOFF_READY"}:
            state["dispatch_state"] = "NEEDS_REVIEW"
        else:
            state["dispatch_state"] = "DORMANT"
        out.append(state)
    return out


def select_review(
    events: list[dict[str, Any]],
    machine: dict[str, Any],
    now: datetime,
    *,
    driver_id: str | None = None,
) -> dict[str, Any] | None:
    candidates = [
        state for state in reduce_reviews(events, machine, now)
        if state["dispatch_state"] == "NEEDS_REVIEW"
    ]
    if not candidates:
        return None

    state_order = {"HANDOFF_READY": 0, "READY": 1}
    priority_order = {"P0": 0, "P1": 1, "P2": 2, "P3": 3}

    def key(state: dict[str, Any]) -> tuple[Any, ...]:
        same_issuer = (
            1
            if driver_id
            and machine["review"].get("prefer_reviewer_different_from_issuer", True)
            and state.get("issuer_driver_id") == driver_id
            else 0
        )
        return (
            same_issuer,
            state_order.get(state["state"], 9),
            priority_order.get(state.get("priority"), 9),
            parse_time(state["requested_at"]),
            state["review_id"],
        )

    return min(candidates, key=key)


def validate_machine(machine: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if machine.get("schema") != "ENTERPRISE_MATH_WORK_STATE_MACHINE_V1":
        errors.append("unexpected work-state schema")
    if machine.get("board", {}).get("issue") != 240:
        errors.append("work-state board must be Issue #240")
    review = machine.get("review", {})
    if review.get("issuer_lock") is not False:
        errors.append("cross-review requires issuer_lock=false")
    if "REVIEW_DONE" not in set(review.get("events", [])):
        errors.append("review event set is incomplete")
    if machine.get("task_claim", {}).get("task_id_required_from_user") is not False:
        errors.append("generic task claim must not require a task id")
    return errors


def print_json(value: Any) -> None:
    print(json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True))


def main() -> int:
    parser = argparse.ArgumentParser(description="Enterprise Math unified task/review state")
    parser.add_argument("--machine", type=pathlib.Path, default=DEFAULT_MACHINE)
    parser.add_argument("--scheduler", type=pathlib.Path, default=DEFAULT_SCHEDULER)
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("validate")

    task_status = sub.add_parser("task-status")
    task_status.add_argument("--events", type=pathlib.Path)
    task_status.add_argument("--now")

    task_select = sub.add_parser("select-task")
    task_select.add_argument("--events", type=pathlib.Path)
    task_select.add_argument("--now")
    task_select.add_argument("--kind", choices=["RESEARCH", "GOVERNANCE", "ANY"], default="RESEARCH")

    review_status = sub.add_parser("review-status")
    review_status.add_argument("--events", type=pathlib.Path)
    review_status.add_argument("--now")

    review_select = sub.add_parser("select-review")
    review_select.add_argument("--events", type=pathlib.Path)
    review_select.add_argument("--now")
    review_select.add_argument("--driver-id")

    args = parser.parse_args()
    machine = load_json(args.machine)
    legacy_config = load_json(args.scheduler)

    if args.command == "validate":
        errors = validate_machine(machine)
        if errors:
            for error in errors:
                print(error)
            return 1
        print("PASS")
        return 0

    events = load_events(args.events)
    now = parse_time(args.now) if args.now else datetime.now(timezone.utc)

    if args.command == "task-status":
        print_json(effective_task_states(legacy_config, events, machine, now))
        return 0
    if args.command == "select-task":
        print_json(select_task(legacy_config, events, machine, now, kind=args.kind))
        return 0
    if args.command == "review-status":
        print_json(reduce_reviews(events, machine, now))
        return 0
    if args.command == "select-review":
        print_json(select_review(events, machine, now, driver_id=args.driver_id))
        return 0
    raise AssertionError(args.command)


if __name__ == "__main__":
    raise SystemExit(main())
