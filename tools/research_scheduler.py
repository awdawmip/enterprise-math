#!/usr/bin/env python3
"""Validate and reduce the Enterprise Math research scheduler state machine.

The repository config defines durable task frontiers. GitHub Issue #240 is the
append-only runtime coordination surface; callers may export its valid event
objects in GitHub comment order to JSON/JSONL and pass them with --events.

This tool deliberately does not decide mathematical truth or canonical status.
Research identity is runtime provenance: CLAIMs automatically resolve a stable
Researcher-ID even when legacy callers do not supply one explicitly.

Owner/resource ownership and conversation/session liveness are intentionally
separate.  A stale session does not release the owner claim; it becomes
STALE_RECOVERABLE and may be adopted by a replacement conversation using the
same claim after durable-frontier reconciliation.
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

HARD_BLOCK_FIELDS = ("missing_object", "owner", "necessity", "unblock_condition")
ACTIVE_OWNER_STATES = {"ACTIVE_OWNER", "ACTIVE_BRIDGE"}
DEPENDENCY_ACTIONS = {"INFORM", "CONSUME", "TEST", "HARD_DEPENDENCY"}
RESEARCHER_ID_RE = re.compile(r"^EM-[A-Z0-9]+-(?:[0-9]{2}|[A-Z0-9]{4,8})$")
TASK_LANE_RE = re.compile(r"^RS-((?:R|P)\d{3}[A-Z]?)\b")
LANE_RE = re.compile(r"[^A-Z0-9]+")
DEFAULT_SESSION_LIVENESS_MINUTES = 10


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

    session_minutes = config.get("session_liveness_minutes", DEFAULT_SESSION_LIVENESS_MINUTES)
    if not isinstance(session_minutes, int) or session_minutes <= 0:
        errors.append("session_liveness_minutes must be a positive integer when present")
    claim_minutes = config.get("claim_lease_minutes", 120)
    if not isinstance(claim_minutes, int) or claim_minutes <= 0:
        errors.append("claim_lease_minutes must be a positive integer")
    elif isinstance(session_minutes, int) and session_minutes >= claim_minutes:
        errors.append("session_liveness_minutes must be shorter than claim_lease_minutes")

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


def session_duration(event: dict[str, Any], default_minutes: int) -> timedelta:
    minutes = event.get("session_liveness_minutes", default_minutes)
    if not isinstance(minutes, int) or minutes <= 0:
        raise SchedulerError("session_liveness_minutes must be a positive integer")
    return timedelta(minutes=minutes)


def event_time(event: dict[str, Any]) -> datetime:
    value = event.get("at")
    if not isinstance(value, str) or not value:
        raise SchedulerError("scheduler event requires ISO-8601 'at'")
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
        "owner_lease_until": None,
        "session_lease_until": None,
        "session_state": "NONE",
        "last_session_activity_at": None,
        "last_session_adopt_at": None,
        "last_recovery_ref": None,
        "current_unfinished_unit": None,
        "hard_block": copy.deepcopy(task.get("hard_block")),
        "last_progress_ref": task.get("last_progress_ref"),
        "last_progress_at": task.get("last_progress_at"),
        "next_action": task.get("next_action"),
        "ignored_events": [],
    }


def release_claim(state: dict[str, Any]) -> None:
    state["claim_id"] = None
    state["actor"] = None
    release_claim_identity(state)
    state["owner_lease_until"] = None
    state["session_lease_until"] = None
    state["session_state"] = "NONE"


def expire_owner_claim(state: dict[str, Any], at: datetime) -> None:
    lease_until = state.get("owner_lease_until")
    if state.get("claim_id") and isinstance(lease_until, datetime) and at >= lease_until:
        state["state"] = "HANDOFF_READY"
        release_claim(state)


def refresh_session_state(state: dict[str, Any], at: datetime) -> None:
    if not state.get("claim_id"):
        state["session_state"] = "NONE"
        return
    session_until = state.get("session_lease_until")
    if isinstance(session_until, datetime) and at >= session_until:
        state["session_state"] = "STALE"
    else:
        state["session_state"] = "LIVE"


def touch_session(
    state: dict[str, Any],
    *,
    at: datetime,
    at_text: str,
    default_session_minutes: int,
    event: dict[str, Any],
) -> None:
    state["session_lease_until"] = at + session_duration(event, default_session_minutes)
    state["session_state"] = "LIVE"
    state["last_session_activity_at"] = at_text


def renew_owner(
    state: dict[str, Any],
    *,
    at: datetime,
    default_lease_minutes: int,
    event: dict[str, Any],
) -> None:
    state["owner_lease_until"] = at + lease_duration(event, default_lease_minutes)


def ignore(state: dict[str, Any], index: int, reason: str) -> None:
    state["ignored_events"].append({"index": index, "reason": reason})


def _event_actor_matches(state: dict[str, Any], event: dict[str, Any]) -> bool:
    event_actor = event.get("actor")
    current_actor = state.get("actor")
    if event_actor is None or current_actor is None:
        return True
    return event_actor == current_actor


def reduce_task(
    task: dict[str, Any],
    events: Iterable[dict[str, Any]],
    *,
    default_lease_minutes: int,
    now: datetime,
    session_liveness_minutes: int = DEFAULT_SESSION_LIVENESS_MINUTES,
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
        except (SchedulerError, ValueError) as exc:
            ignore(state, index, str(exc))
            continue
        if last_event_time is not None and at < last_event_time:
            ignore(state, index, "events must be supplied in GitHub comment order / nondecreasing event time")
            continue
        last_event_time = at
        expire_owner_claim(state, at)
        refresh_session_state(state, at)

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
                renew_owner(state, at=at, default_lease_minutes=default_lease_minutes, event=event)
                touch_session(
                    state,
                    at=at,
                    at_text=event["at"],
                    default_session_minutes=session_liveness_minutes,
                    event=event,
                )
            except SchedulerError as exc:
                ignore(state, index, str(exc))
                state["owner_lease_until"] = None
                state["session_lease_until"] = None
                state["session_state"] = "NONE"
                continue
            state["state"] = "CLAIMED"
            state["claim_id"] = claim_id
            state["actor"] = event.get("actor")
            state["researcher_id"] = researcher_id
            state["last_researcher_id"] = researcher_id
            state["identity_source"] = "EVENT" if supplied_researcher_id is not None else "AUTO_CLAIM_DERIVED"
            continue

        claim_scoped = {"HEARTBEAT", "PROGRESS", "SESSION_ADOPT", "HANDOFF", "HARD_BLOCK", "DONE"}
        if kind in claim_scoped:
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
            if kind != "SESSION_ADOPT" and not _event_actor_matches(state, event):
                ignore(state, index, f"{kind} actor does not match current session actor")
                continue

        if kind == "HEARTBEAT":
            if state.get("session_state") == "STALE":
                ignore(state, index, "stale session requires SESSION_ADOPT or durable PROGRESS")
                continue
            try:
                renew_owner(state, at=at, default_lease_minutes=default_lease_minutes, event=event)
                touch_session(
                    state,
                    at=at,
                    at_text=event["at"],
                    default_session_minutes=session_liveness_minutes,
                    event=event,
                )
            except SchedulerError as exc:
                ignore(state, index, str(exc))
            continue

        if kind == "PROGRESS":
            try:
                renew_owner(state, at=at, default_lease_minutes=default_lease_minutes, event=event)
                touch_session(
                    state,
                    at=at,
                    at_text=event["at"],
                    default_session_minutes=session_liveness_minutes,
                    event=event,
                )
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

        if kind == "SESSION_ADOPT":
            if state.get("session_state") != "STALE":
                ignore(state, index, "SESSION_ADOPT requires a stale session on a still-live owner claim")
                continue
            actor = event.get("actor")
            recovery_ref = event.get("recovery_ref")
            unfinished_unit = event.get("unfinished_unit")
            next_action = event.get("next_action")
            required = {
                "actor": actor,
                "recovery_ref": recovery_ref,
                "unfinished_unit": unfinished_unit,
                "next_action": next_action,
            }
            if not all(isinstance(value, str) and value.strip() for value in required.values()):
                ignore(state, index, "SESSION_ADOPT requires actor, recovery_ref, unfinished_unit, and next_action")
                continue
            try:
                renew_owner(state, at=at, default_lease_minutes=default_lease_minutes, event=event)
                touch_session(
                    state,
                    at=at,
                    at_text=event["at"],
                    default_session_minutes=session_liveness_minutes,
                    event=event,
                )
            except SchedulerError as exc:
                ignore(state, index, str(exc))
                continue
            state["state"] = "IN_PROGRESS"
            state["actor"] = actor
            state["last_session_adopt_at"] = event["at"]
            state["last_recovery_ref"] = recovery_ref
            state["current_unfinished_unit"] = unfinished_unit
            state["next_action"] = next_action
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
            release_claim(state)
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
            release_claim(state)
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
            release_claim(state)
            continue

        if kind == "SUPERSEDE":
            state["state"] = "SUPERSEDED"
            release_claim(state)
            state["last_progress_at"] = event["at"]
            if event.get("next_action"):
                state["next_action"] = event["next_action"]
            continue

        ignore(state, index, f"unknown event type: {kind!r}")

    expire_owner_claim(state, now)
    refresh_session_state(state, now)

    owner_lease_until = state.get("owner_lease_until")
    session_lease_until = state.get("session_lease_until")
    state["owner_lease_until"] = owner_lease_until.isoformat() if isinstance(owner_lease_until, datetime) else None
    state["session_lease_until"] = session_lease_until.isoformat() if isinstance(session_lease_until, datetime) else None
    # Compatibility alias for callers that previously interpreted lease_until as
    # the only lease.  It now explicitly mirrors the owner/resource lease.
    state["lease_until"] = state["owner_lease_until"]

    if state["state"] in {"DONE", "SUPERSEDED"}:
        state["dispatch_state"] = "COMPLETE"
    elif state["state"] == "BLOCKED" and complete_hard_block(state.get("hard_block")):
        state["dispatch_state"] = "BLOCKED"
    elif state.get("claim_id") and state.get("session_state") == "STALE":
        state["dispatch_state"] = "STALE_RECOVERABLE"
    elif state.get("claim_id"):
        state["dispatch_state"] = "LEASED"
    elif state["state"] in {"READY", "HANDOFF_READY"}:
        state["dispatch_state"] = "NEEDS_DISPATCH"
    else:
        state["dispatch_state"] = "DORMANT"
    return state


def effective_states(config: dict[str, Any], events: list[dict[str, Any]], now: datetime) -> list[dict[str, Any]]:
    default_lease = int(config.get("claim_lease_minutes", 120))
    session_liveness = int(config.get("session_liveness_minutes", DEFAULT_SESSION_LIVENESS_MINUTES))
    results = []
    for task in config.get("tasks", []):
        reduced = reduce_task(
            task,
            events,
            default_lease_minutes=default_lease,
            now=now,
            session_liveness_minutes=session_liveness,
        )
        reduced.update({
            "title": task.get("title"),
            "kind": task.get("kind"),
            "owner": task.get("owner"),
            "priority": task.get("priority"),
            "leverage": task.get("leverage"),
            "frontier": task.get("frontier"),
            "source_refs": task.get("source_refs", []),
            "identity_lane": identity_lane(task),
        })
        results.append(reduced)
    return results


def select_task(
    config: dict[str, Any],
    events: list[dict[str, Any]],
    now: datetime,
    *,
    kind: str = "RESEARCH",
) -> dict[str, Any] | None:
    policy = config["selection_policy"]
    states = effective_states(config, events, now)
    task_by_id = {task["task_id"]: task for task in config["tasks"]}
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
        task = task_by_id[state["task_id"]]
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

    chosen = min(candidates, key=candidate_key)
    return chosen


def print_json(value: Any) -> None:
    print(json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Enterprise Math research scheduler")
    parser.add_argument("--config", type=pathlib.Path, default=DEFAULT_CONFIG)
    parser.add_argument("--owners", type=pathlib.Path, default=DEFAULT_OWNERS)
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("validate")

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
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    config = load_json(args.config)
    owners = load_json(args.owners)
    errors = validate_scheduler(config, owners)

    if args.command == "validate":
        if errors:
            for error in errors:
                print(f"ERROR: {error}")
            return 1
        print(f"PASS: scheduler config valid; {len(config.get('tasks', []))} tasks cover all active research owners/bridges.")
        return 0

    if errors:
        raise SchedulerError("invalid scheduler configuration: " + "; ".join(errors))

    if args.command == "identity":
        task = next((item for item in config.get("tasks", []) if item.get("task_id") == args.task_id), None)
        if task is None:
            raise SchedulerError(f"unknown task_id: {args.task_id}")
        print_json({
            "task_id": args.task_id,
            "claim_id": args.claim_id,
            "identity_lane": identity_lane(task),
            "researcher_id": researcher_id_for_claim(task, args.claim_id),
            "identity_source": "AUTO_CLAIM_DERIVED",
        })
        return 0

    events = load_events(args.events)
    current = now_utc(args.now)
    if args.command == "status":
        print_json(effective_states(config, events, current))
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
