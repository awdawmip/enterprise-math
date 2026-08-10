#!/usr/bin/env python3
"""Enterprise Math scheduler with append-only Markdown taskbook discovery.

The stable reducer remains in ``research_tasks/_research_scheduler_legacy.py``.
This thin layer merges scout-created ``research_tasks/*.md`` taskbooks into the
legacy static scheduler config before validation/status/selection. New taskbooks
therefore become dispatchable without editing ``research_scheduler.json``.

Research tasks are context-isolated by default. Memory and undeclared cross-task
material are hints only; they do not become premises unless resolved to allowed
sources or imported explicitly with provenance.
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
CONTEXT_POLICY_PATH = ROOT / "research_context_policy.json"
TASKBOOK_MARKER = "<!-- ENTERPRISE_MATH_TASK_V1"
TASKBOOK_END = "-->"
TASKBOOK_UNASSIGNED_OWNER = "taskbook/unassigned"

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
    return apply_research_context_defaults(task, source=task["_taskbook_path"])


def load_taskbooks(taskbook_dir: pathlib.Path = DEFAULT_TASKBOOK_DIR) -> list[dict[str, Any]]:
    if not taskbook_dir.exists():
        return []
    tasks: list[dict[str, Any]] = []
    for path in sorted(taskbook_dir.glob("*.md")):
        if path.name.lower() in {"readme.md", "agents.md"}:
            continue
        tasks.append(parse_taskbook(path))
    return tasks


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
    """Run legacy validation while enforcing isolated research context.

    ``taskbook/unassigned`` is a routing placeholder only. It does not grant
    theorem ownership. A researcher claiming the task remains an execution actor;
    any reusable theorem is routed to the real owner before promotion.
    """
    try:
        config = normalize_research_context(config)
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


def _attach_context_fields(
    value: dict[str, Any] | None,
    task_by_id: dict[str, dict[str, Any]],
) -> dict[str, Any] | None:
    if value is None:
        return None
    result = copy.deepcopy(value)
    task = task_by_id.get(result.get("task_id"), {})
    for field in ("context_mode", "memory_policy", "cross_task_import_policy"):
        if field in task:
            result[field] = task[field]
    return result


def effective_states(
    config: dict[str, Any],
    events: list[dict[str, Any]],
    now: Any,
) -> list[dict[str, Any]]:
    config = normalize_research_context(config)
    states = legacy.effective_states(config, events, now)
    task_by_id = {task["task_id"]: task for task in config.get("tasks", [])}
    return [
        _attach_context_fields(state, task_by_id) or state
        for state in states
    ]


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
    return _attach_context_fields(chosen, task_by_id)


def build_parser() -> argparse.ArgumentParser:
    parser = legacy.build_parser()
    parser.add_argument(
        "--taskbooks",
        type=pathlib.Path,
        default=DEFAULT_TASKBOOK_DIR,
        help="append-only Markdown taskbook directory",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    config = load_scheduler_config(args.config, args.taskbooks)
    owners = load_json(args.owners)
    errors = validate_scheduler(config, owners)

    if args.command == "validate":
        if errors:
            for error in errors:
                print(f"ERROR: {error}")
            return 1
        taskbook_count = sum(bool(task.get("_taskbook_path")) for task in config.get("tasks", []))
        print(
            f"PASS: scheduler config valid; {len(config.get('tasks', []))} tasks "
            f"({taskbook_count} append-only taskbooks) are discoverable and TASK_ISOLATED."
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
