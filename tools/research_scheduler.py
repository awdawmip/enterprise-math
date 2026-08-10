#!/usr/bin/env python3
"""Enterprise Math scheduler with taskbooks, role authority, and proposal discovery.

The stable task reducer remains in ``research_tasks/_research_scheduler_legacy.py``.
This wrapper adds three narrow control-plane features without changing ordinary
research execution:

1. append-only ``research_tasks/*.md`` discovery;
2. non-weakenable task-local context isolation;
3. Driver authority for dispatchable taskbooks plus a non-dispatchable compact
   proposal queue under ``research_proposals/*.json``.

Research remains the hot path. Proposal capture is optional bookkeeping at a
semantic checkpoint, never a startup gate or HARD_BLOCK.
"""

from __future__ import annotations

import argparse
import copy
import importlib.util
import json
import pathlib
import sys
from typing import Any

ROOT = pathlib.Path(__file__).resolve().parents[1]
LEGACY_PATH = ROOT / "research_tasks" / "_research_scheduler_legacy.py"
DEFAULT_TASKBOOK_DIR = ROOT / "research_tasks"
DEFAULT_PROPOSAL_DIR = ROOT / "research_proposals"
CONTEXT_POLICY_PATH = ROOT / "research_context_policy.json"
ROLE_POLICY_PATH = ROOT / "research_role_policy.json"
TASKBOOK_MARKER = "<!-- ENTERPRISE_MATH_TASK_V1"
TASKBOOK_END = "-->"
TASKBOOK_UNASSIGNED_OWNER = "taskbook/unassigned"
PROPOSAL_SCHEMA = "ENTERPRISE_MATH_PROPOSAL_BUNDLE_V1"

_spec = importlib.util.spec_from_file_location("enterprise_math_research_scheduler_legacy", LEGACY_PATH)
if _spec is None or _spec.loader is None:
    raise RuntimeError(f"cannot load scheduler core from {LEGACY_PATH}")
legacy = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(legacy)

SchedulerError = legacy.SchedulerError
load_json = legacy.load_json
parse_time = legacy.parse_time
now_utc = legacy.now_utc
complete_hard_block = legacy.complete_hard_block
load_events = legacy.load_events
lease_duration = legacy.lease_duration
event_time = legacy.event_time
state_from_task = legacy.state_from_task
expire_claim = legacy.expire_claim
ignore = legacy.ignore
reduce_task = legacy.reduce_task
print_json = legacy.print_json


def load_context_policy(path: pathlib.Path = CONTEXT_POLICY_PATH) -> dict[str, Any]:
    policy = load_json(path)
    if policy.get("schema") != "ENTERPRISE_MATH_RESEARCH_CONTEXT_ISOLATION_V1":
        raise SchedulerError(f"{path}: unexpected research context policy schema")
    defaults = policy.get("default_research_context")
    if not isinstance(defaults, dict) or not defaults:
        raise SchedulerError(f"{path}: missing default_research_context")
    return policy


def load_role_policy(path: pathlib.Path = ROLE_POLICY_PATH) -> dict[str, Any]:
    policy = load_json(path)
    if policy.get("schema") != "ENTERPRISE_MATH_RESEARCH_ROLE_POLICY_V1":
        raise SchedulerError(f"{path}: unexpected research role policy schema")
    if policy.get("default_role") != "RESEARCHER":
        raise SchedulerError(f"{path}: default_role must remain RESEARCHER")
    authority = policy.get("official_taskbook_authority")
    proposal = policy.get("proposal_capture")
    if not isinstance(authority, dict) or not isinstance(proposal, dict):
        raise SchedulerError(f"{path}: missing taskbook authority/proposal policy")
    return policy


def apply_research_context_defaults(
    task: dict[str, Any],
    *,
    source: str,
    policy: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Apply the non-weakenable task-isolation defaults to one research task."""
    if task.get("kind") != "RESEARCH":
        return task
    policy = policy or load_context_policy()
    defaults = policy["default_research_context"]
    normalized = copy.deepcopy(task)
    for field, required in defaults.items():
        existing = normalized.get(field)
        if existing is not None and existing != required:
            raise SchedulerError(
                f"{source}: research task cannot weaken {field}; "
                f"expected {required!r}, got {existing!r}"
            )
        normalized[field] = required
    return normalized


def apply_taskbook_authority(
    task: dict[str, Any],
    *,
    source: str,
    policy: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Require Driver approval for new dispatchable append-only taskbooks.

    Central legacy scheduler tasks are unaffected. Taskbooks created before this
    policy are explicitly grandfathered by stable task_id so the new gate does not
    interrupt ongoing research.
    """
    if not task.get("_taskbook_path"):
        return task
    policy = policy or load_role_policy()
    authority = policy["official_taskbook_authority"]
    normalized = copy.deepcopy(task)
    task_id = normalized.get("task_id")
    grandfathered = set(authority.get("grandfathered_task_ids", []))
    if task_id in grandfathered:
        normalized.setdefault("created_by_role", "RESEARCH_DRIVER")
        normalized.setdefault("task_authority", "GRANDFATHERED_DRIVER_APPROVED")
        return normalized

    required_role = authority.get("created_by_role", "RESEARCH_DRIVER")
    required_authority = authority.get("task_authority", "DRIVER_APPROVED")
    if normalized.get("created_by_role") != required_role:
        raise SchedulerError(
            f"{source}: new taskbook is not dispatchable without "
            f"created_by_role={required_role!r}"
        )
    if normalized.get("task_authority") != required_authority:
        raise SchedulerError(
            f"{source}: new taskbook is not dispatchable without "
            f"task_authority={required_authority!r}"
        )
    return normalized


def normalize_research_context(
    config: dict[str, Any],
    *,
    policy: dict[str, Any] | None = None,
) -> dict[str, Any]:
    policy = policy or load_context_policy()
    normalized = copy.deepcopy(config)
    normalized["tasks"] = [
        apply_research_context_defaults(
            task,
            source=task.get("_taskbook_path") or task.get("task_id") or "scheduler task",
            policy=policy,
        )
        for task in normalized.get("tasks", [])
    ]
    return normalized


def parse_taskbook(path: pathlib.Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith(TASKBOOK_MARKER):
        raise SchedulerError(f"{path}: missing ENTERPRISE_MATH_TASK_V1 metadata block")
    end = text.find(TASKBOOK_END, len(TASKBOOK_MARKER))
    if end < 0:
        raise SchedulerError(f"{path}: unterminated taskbook metadata block")
    payload = text[len(TASKBOOK_MARKER):end].strip()
    try:
        task = json.loads(payload)
    except json.JSONDecodeError as exc:
        raise SchedulerError(f"{path}: invalid taskbook JSON: {exc}") from exc
    if not isinstance(task, dict):
        raise SchedulerError(f"{path}: taskbook metadata must be an object")
    task = copy.deepcopy(task)
    try:
        task["_taskbook_path"] = path.relative_to(ROOT).as_posix()
    except ValueError:
        task["_taskbook_path"] = path.as_posix()
    task = apply_research_context_defaults(task, source=task["_taskbook_path"])
    return apply_taskbook_authority(task, source=task["_taskbook_path"])


def load_taskbooks(taskbook_dir: pathlib.Path = DEFAULT_TASKBOOK_DIR) -> list[dict[str, Any]]:
    if not taskbook_dir.exists():
        return []
    tasks: list[dict[str, Any]] = []
    for path in sorted(taskbook_dir.glob("*.md")):
        if path.name.lower() in {"readme.md", "agents.md"}:
            continue
        tasks.append(parse_taskbook(path))
    return tasks


def parse_proposal_bundle(
    path: pathlib.Path,
    *,
    policy: dict[str, Any] | None = None,
) -> list[dict[str, Any]]:
    """Parse one compact researcher proposal bundle into non-dispatchable rows."""
    policy = policy or load_role_policy()
    proposal_policy = policy["proposal_capture"]
    data = load_json(path)
    if not isinstance(data, dict) or data.get("schema") != PROPOSAL_SCHEMA:
        raise SchedulerError(f"{path}: unexpected proposal bundle schema")
    if data.get("created_by_role") != "RESEARCHER":
        raise SchedulerError(f"{path}: proposal bundle must use created_by_role='RESEARCHER'")
    parent = data.get("parent_task_id")
    if not isinstance(parent, str) or not parent.strip():
        raise SchedulerError(f"{path}: proposal bundle requires parent_task_id")
    at = data.get("at")
    if not isinstance(at, str) or not at.strip():
        raise SchedulerError(f"{path}: proposal bundle requires at")
    try:
        parse_time(at)
    except (TypeError, ValueError) as exc:
        raise SchedulerError(f"{path}: invalid proposal timestamp") from exc
    candidates = data.get("candidates")
    if not isinstance(candidates, list) or not candidates:
        raise SchedulerError(f"{path}: proposal bundle requires non-empty candidates")

    required = proposal_policy.get("candidate_required_fields", [])
    leverage_values = set(proposal_policy.get("expected_leverage", []))
    rows: list[dict[str, Any]] = []
    seen: set[str] = set()
    for index, candidate in enumerate(candidates):
        if not isinstance(candidate, dict):
            raise SchedulerError(f"{path}: candidate[{index}] must be an object")
        missing = [field for field in required if not candidate.get(field)]
        if missing:
            raise SchedulerError(f"{path}: candidate[{index}] missing {', '.join(missing)}")
        proposal_id = candidate["proposal_id"]
        if proposal_id in seen:
            raise SchedulerError(f"{path}: duplicate proposal_id {proposal_id!r}")
        seen.add(proposal_id)
        if candidate.get("expected_leverage") not in leverage_values:
            raise SchedulerError(
                f"{path}: candidate[{index}] invalid expected_leverage "
                f"{candidate.get('expected_leverage')!r}"
            )
        if not isinstance(candidate.get("evidence_refs"), list):
            raise SchedulerError(f"{path}: candidate[{index}] evidence_refs must be a list")
        row = copy.deepcopy(candidate)
        row.update({
            "parent_task_id": parent,
            "at": at,
            "created_by_role": "RESEARCHER",
            "review_state": proposal_policy.get("default_review_state", "PENDING_DRIVER_REVIEW"),
            "dispatchable": False,
            "_proposal_bundle_path": path.as_posix(),
        })
        rows.append(row)
    return rows


def load_proposal_queue(
    proposal_dir: pathlib.Path = DEFAULT_PROPOSAL_DIR,
) -> list[dict[str, Any]]:
    if not proposal_dir.exists():
        return []
    policy = load_role_policy()
    rows: list[dict[str, Any]] = []
    for path in sorted(proposal_dir.glob("*.json")):
        rows.extend(parse_proposal_bundle(path, policy=policy))
    return rows


def merge_taskbooks(config: dict[str, Any], taskbooks: list[dict[str, Any]]) -> dict[str, Any]:
    merged = copy.deepcopy(config)
    merged.setdefault("tasks", [])
    merged["tasks"].extend(copy.deepcopy(taskbooks))
    return merged


def load_scheduler_config(
    config_path: pathlib.Path = legacy.DEFAULT_CONFIG,
    taskbook_dir: pathlib.Path = DEFAULT_TASKBOOK_DIR,
) -> dict[str, Any]:
    merged = merge_taskbooks(load_json(config_path), load_taskbooks(taskbook_dir))
    return normalize_research_context(merged)


def validate_scheduler(config: dict[str, Any], owners: dict[str, Any]) -> list[str]:
    """Run legacy validation while enforcing isolated context and task authority."""
    try:
        config = normalize_research_context(config)
        load_role_policy()
    except SchedulerError as exc:
        return [str(exc)]

    has_unassigned_taskbook = any(
        task.get("_taskbook_path") and task.get("owner") == TASKBOOK_UNASSIGNED_OWNER
        for task in config.get("tasks", [])
    )
    if not has_unassigned_taskbook:
        return legacy.validate_scheduler(config, owners)

    owners_for_validation = copy.deepcopy(owners)
    owners_for_validation.setdefault("branches", {})[TASKBOOK_UNASSIGNED_OWNER] = {
        "state": "ACTIVE_OWNER",
        "scope": "scheduler routing placeholder only",
    }
    return legacy.validate_scheduler(config, owners_for_validation)


def _attach_control_fields(
    value: dict[str, Any] | None,
    task_by_id: dict[str, dict[str, Any]],
) -> dict[str, Any] | None:
    if value is None:
        return None
    result = copy.deepcopy(value)
    task = task_by_id.get(result.get("task_id"), {})
    for field in (
        "context_mode",
        "memory_policy",
        "cross_task_import_policy",
        "created_by_role",
        "task_authority",
    ):
        if field in task:
            result[field] = task[field]
    result["session_role"] = "RESEARCHER"
    result["driver_activation"] = "EXPLICIT_CURRENT_CONVERSATION_ONLY"
    return result


def effective_states(
    config: dict[str, Any],
    events: list[dict[str, Any]],
    now: Any,
) -> list[dict[str, Any]]:
    config = normalize_research_context(config)
    states = legacy.effective_states(config, events, now)
    task_by_id = {task["task_id"]: task for task in config.get("tasks", [])}
    return [_attach_control_fields(state, task_by_id) or state for state in states]


def select_task(
    config: dict[str, Any],
    events: list[dict[str, Any]],
    now: Any,
    *,
    kind: str = "RESEARCH",
) -> dict[str, Any] | None:
    config = normalize_research_context(config)
    chosen = legacy.select_task(config, events, now, kind=kind)
    task_by_id = {task["task_id"]: task for task in config.get("tasks", [])}
    return _attach_control_fields(chosen, task_by_id)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Enterprise Math research scheduler")
    parser.add_argument("--config", type=pathlib.Path, default=legacy.DEFAULT_CONFIG)
    parser.add_argument("--owners", type=pathlib.Path, default=legacy.DEFAULT_OWNERS)
    parser.add_argument("--taskbooks", type=pathlib.Path, default=DEFAULT_TASKBOOK_DIR)
    parser.add_argument("--proposals", type=pathlib.Path, default=DEFAULT_PROPOSAL_DIR)
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("validate")

    status = sub.add_parser("status")
    status.add_argument("--events", type=pathlib.Path)
    status.add_argument("--now")

    select = sub.add_parser("select")
    select.add_argument("--events", type=pathlib.Path)
    select.add_argument("--now")
    select.add_argument("--kind", choices=["RESEARCH", "GOVERNANCE", "ANY"], default="RESEARCH")

    proposals = sub.add_parser("proposal-queue")
    proposals.add_argument("--parent-task-id")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)

    if args.command == "proposal-queue":
        rows = load_proposal_queue(args.proposals)
        if args.parent_task_id:
            rows = [row for row in rows if row.get("parent_task_id") == args.parent_task_id]
        print_json(rows)
        return 0

    config = load_scheduler_config(args.config, args.taskbooks)
    owners = load_json(args.owners)
    errors = validate_scheduler(config, owners)

    if args.command == "validate":
        if errors:
            for error in errors:
                print(f"ERROR: {error}")
            return 1
        taskbook_count = sum(bool(task.get("_taskbook_path")) for task in config.get("tasks", []))
        proposal_count = len(load_proposal_queue(args.proposals))
        print(
            f"PASS: scheduler config valid; {len(config.get('tasks', []))} tasks "
            f"({taskbook_count} append-only taskbooks) are discoverable, TASK_ISOLATED, "
            f"and role-governed; {proposal_count} proposal candidates are non-dispatchable."
        )
        return 0

    if errors:
        raise SchedulerError("invalid scheduler configuration: " + "; ".join(errors))

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
