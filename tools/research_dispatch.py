#!/usr/bin/env python3
"""Canonical registered-plus-legacy Enterprise Math dispatch view.

Post-cutover task definitions come from immutable task publication records.
The frozen research_scheduler.json remains a compatibility baseline only.
Issue #240 events are still reduced by tools/research_scheduler.py, but the
canonical selector consumes the merged definition view and result/review state.
"""
from __future__ import annotations

import argparse
import copy
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

try:
    from tools import research_result_records
    from tools import research_scheduler
    from tools import research_task_records
    from tools import research_taskbook
except ModuleNotFoundError:
    import research_result_records  # type: ignore
    import research_scheduler  # type: ignore
    import research_task_records  # type: ignore
    import research_taskbook  # type: ignore

ROOT = Path(__file__).resolve().parents[1]
LEGACY = ROOT / "research_scheduler.json"
OWNERS = ROOT / "branch_governance_overrides.json"


class DispatchError(ValueError):
    pass


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _parse_taskbook(record: dict[str, Any], root: Path) -> dict[str, Any]:
    path_value = record.get("taskbook_path")
    if not isinstance(path_value, str) or not path_value:
        raise DispatchError(f"{record.get('task_id')}: task record missing taskbook_path")
    path = root / path_value
    if not path.exists():
        raise DispatchError(f"{record.get('task_id')}: taskbook does not exist")
    meta, _ = research_taskbook.split_taskbook(path.read_text(encoding="utf-8"))
    if meta.get("task_id") != record.get("task_id"):
        raise DispatchError(f"{record.get('task_id')}: taskbook task_id mismatch")
    return meta


def registered_definition(record: dict[str, Any], root: Path = ROOT) -> dict[str, Any]:
    meta = _parse_taskbook(record, root)
    state = str(meta.get("base_state") or "READY")
    if record.get("claimable") is True and state in {"DRAFT", "BACKLOG"}:
        state = "READY"
    if state not in {"BACKLOG", "READY", "HANDOFF_READY", "BLOCKED", "DONE", "SUPERSEDED"}:
        state = "READY" if record.get("claimable") is True else "BACKLOG"
    last_progress_at = meta.get("last_progress_at") or record.get("published_at")
    if not isinstance(last_progress_at, str) or not last_progress_at:
        last_progress_at = "1970-01-01T00:00:00+00:00"
    return {
        "task_id": record["task_id"],
        "title": meta.get("title", record["task_id"]),
        "kind": record.get("kind", meta.get("kind", "RESEARCH")),
        "owner": record.get("owner", meta.get("owner", "taskbook/unassigned")),
        "base_state": state,
        "priority": record.get("effective_priority", meta.get("priority", "P2")),
        "leverage": record.get("effective_leverage", meta.get("leverage", "MEDIUM")),
        "frontier": record.get("frontier", meta.get("frontier", "")),
        "next_action": record.get("next_action", meta.get("next_action", "")),
        "dependencies": copy.deepcopy(meta.get("dependencies", [])),
        "source_refs": copy.deepcopy(meta.get("source_refs", [])),
        "evidence_status": meta.get("evidence_status", "REGISTERED_TASK"),
        "last_progress_ref": meta.get("last_progress_ref") or record.get("publication_id"),
        "last_progress_at": last_progress_at,
        "hard_block": copy.deepcopy(meta.get("hard_block")),
        "tags": copy.deepcopy(meta.get("tags", [])),
        "claim_lease_minutes": int(meta.get("claim_lease_minutes") or 120),
        "identity_lane": meta.get("identity_lane"),
        "publication_id": record.get("publication_id"),
        "registration_source": "IMMUTABLE_TASK_RECORD",
    }


def merged_definitions(root: Path = ROOT) -> list[dict[str, Any]]:
    legacy = load_json(root / "research_scheduler.json")
    by_id: dict[str, dict[str, Any]] = {}
    for task in legacy.get("tasks", []):
        if isinstance(task, dict) and isinstance(task.get("task_id"), str):
            value = copy.deepcopy(task)
            value["registration_source"] = "FROZEN_LEGACY_BASELINE"
            by_id[task["task_id"]] = value
    for task_id, record in research_task_records.current_records(root).items():
        by_id[task_id] = registered_definition(record, root)
    return [by_id[key] for key in sorted(by_id)]


def _is_registered(task: dict[str, Any]) -> bool:
    return task.get("registration_source") == "IMMUTABLE_TASK_RECORD"


def _filter_registered_done_events(
    task: dict[str, Any], events: list[dict[str, Any]], root: Path
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    if not _is_registered(task):
        return events, []
    result_state = research_result_records.task_result_state(task["task_id"], root)
    terminal_result_id = None
    if result_state is not None and result_state.get("terminal") is True:
        terminal_result_id = result_state["result"].get("result_id")
    accepted: list[dict[str, Any]] = []
    rejected: list[dict[str, Any]] = []
    for index, event in enumerate(events):
        if event.get("task_id") != task["task_id"] or event.get("event") != "DONE":
            accepted.append(event)
            continue
        if not terminal_result_id:
            rejected.append({
                "index": index,
                "reason": "registered DONE requires a frozen result with terminal Driver review",
            })
            continue
        if event.get("result_id") != terminal_result_id:
            rejected.append({
                "index": index,
                "reason": "registered DONE result_id does not match terminal reviewed result",
            })
            continue
        accepted.append(event)
    return accepted, rejected


def _overlay_result_state(
    task: dict[str, Any], state: dict[str, Any], root: Path
) -> dict[str, Any]:
    if not _is_registered(task):
        return state
    result_state = research_result_records.task_result_state(task["task_id"], root)
    if result_state is None:
        return state
    value = copy.deepcopy(state)
    result = result_state["result"]
    review = result_state.get("review")
    value["result_id"] = result.get("result_id")
    value["result_record_path"] = result.get("_record_path")
    if result_state["state"] == "AWAITING_DRIVER_REVIEW":
        value["state"] = "FROZEN_RETURN"
        value["dispatch_state"] = "AWAITING_REVIEW"
        value["next_action"] = "Driver review required before terminal closure or researcher redispatch"
        return value
    if result_state["state"] == "RETURN_TO_EXECUTION":
        value["state"] = "HANDOFF_READY"
        value["dispatch_state"] = "NEEDS_DISPATCH"
        value["claim_id"] = None
        value["actor"] = None
        value["researcher_id"] = None
        value["identity_source"] = None
        value["lease_until"] = None
        value["driver_disposition"] = review.get("disposition") if review else None
        value["next_action"] = "Resume task under Driver disposition"
        return value
    if result_state["state"] == "TERMINAL":
        value["state"] = "DONE"
        value["dispatch_state"] = "COMPLETE"
        value["claim_id"] = None
        value["actor"] = None
        value["researcher_id"] = None
        value["identity_source"] = None
        value["lease_until"] = None
        value["driver_disposition"] = review.get("disposition") if review else None
        value["review_id"] = review.get("review_id") if review else None
        return value
    return value


def reduce_definition(
    task: dict[str, Any],
    events: list[dict[str, Any]],
    *,
    now: datetime,
    default_lease_minutes: int = 120,
    root: Path = ROOT,
) -> dict[str, Any]:
    filtered, rejected = _filter_registered_done_events(task, events, root)
    lease = int(task.get("claim_lease_minutes") or default_lease_minutes)
    state = research_scheduler.reduce_task(
        task,
        filtered,
        default_lease_minutes=lease,
        now=now,
    )
    state["ignored_events"].extend(rejected)
    state.update({
        "title": task.get("title"),
        "kind": task.get("kind"),
        "owner": task.get("owner"),
        "priority": task.get("priority"),
        "leverage": task.get("leverage"),
        "frontier": task.get("frontier"),
        "source_refs": task.get("source_refs", []),
        "registration_source": task.get("registration_source"),
        "publication_id": task.get("publication_id"),
    })
    try:
        state["identity_lane"] = research_scheduler.identity_lane(task)
    except Exception:
        state["identity_lane"] = task.get("identity_lane")
    return _overlay_result_state(task, state, root)


def effective_states(
    events: list[dict[str, Any]], *, now: datetime, root: Path = ROOT
) -> list[dict[str, Any]]:
    return [
        reduce_definition(task, events, now=now, root=root)
        for task in merged_definitions(root)
    ]


def select_task(
    events: list[dict[str, Any]],
    *,
    now: datetime,
    kind: str = "RESEARCH",
    root: Path = ROOT,
) -> dict[str, Any] | None:
    legacy = load_json(root / "research_scheduler.json")
    policy = legacy["selection_policy"]
    states = effective_states(events, now=now, root=root)
    state_rank = {name: index for index, name in enumerate(policy["state_order"])}
    priority_rank = {name: index for index, name in enumerate(policy["priority_order"])}
    leverage_rank = {name: index for index, name in enumerate(policy["leverage_order"])}
    candidates = [
        item for item in states
        if item.get("dispatch_state") == "NEEDS_DISPATCH"
        and (kind == "ANY" or item.get("kind") == kind)
    ]
    if not candidates:
        return None

    def key(item: dict[str, Any]):
        try:
            last = research_scheduler.parse_time(item.get("last_progress_at", ""))
        except Exception:
            last = datetime(1970, 1, 1, tzinfo=timezone.utc)
        return (
            state_rank.get(item.get("state"), len(state_rank)),
            priority_rank.get(item.get("priority"), len(priority_rank)),
            leverage_rank.get(item.get("leverage"), len(leverage_rank)),
            last,
            item.get("task_id", ""),
        )

    return min(candidates, key=key)


def validate(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    legacy = load_json(root / "research_scheduler.json")
    owners = load_json(root / "branch_governance_overrides.json")
    errors.extend(research_scheduler.validate_scheduler(legacy, owners))
    errors.extend(research_task_records.audit(root))
    errors.extend(research_result_records.audit(root))
    try:
        definitions = merged_definitions(root)
    except Exception as exc:
        errors.append(f"merged dispatch definition failure: {exc}")
        return errors
    ids = [item.get("task_id") for item in definitions]
    if len(ids) != len(set(ids)):
        errors.append("canonical merged dispatch view contains duplicate task IDs")
    current = research_task_records.current_records(root)
    for task_id in current:
        matches = [item for item in definitions if item.get("task_id") == task_id]
        if len(matches) != 1 or matches[0].get("registration_source") != "IMMUTABLE_TASK_RECORD":
            errors.append(f"{task_id}: registered task is not canonical in merged dispatch view")
    return errors


def load_events(path: Path | None) -> list[dict[str, Any]]:
    return research_scheduler.load_events(path)


def main() -> int:
    parser = argparse.ArgumentParser(description="Enterprise Math canonical registered-plus-legacy dispatch")
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("validate")
    status = sub.add_parser("status")
    status.add_argument("--events", type=Path)
    status.add_argument("--now")
    select = sub.add_parser("select")
    select.add_argument("--events", type=Path)
    select.add_argument("--now")
    select.add_argument("--kind", choices=["RESEARCH", "GOVERNANCE", "ANY"], default="RESEARCH")
    args = parser.parse_args()
    if args.command == "validate":
        errors = validate()
        if errors:
            for error in errors:
                print("ERROR:", error)
            return 1
        print(
            f"PASS: canonical dispatch valid; {len(merged_definitions())} merged task definition(s), "
            f"{len(research_task_records.current_records())} immutable registered task(s)."
        )
        return 0
    events = load_events(args.events)
    now = research_scheduler.now_utc(args.now)
    if args.command == "status":
        print(json.dumps(effective_states(events, now=now), ensure_ascii=False, indent=2, sort_keys=True))
        return 0
    chosen = select_task(events, now=now, kind=args.kind)
    print(json.dumps(chosen, ensure_ascii=False, indent=2, sort_keys=True))
    return 0 if chosen is not None else 2


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except DispatchError as exc:
        print("ERROR:", exc)
        raise SystemExit(1)
