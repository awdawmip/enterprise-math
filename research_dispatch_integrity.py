#!/usr/bin/env python3
"""Canonical dispatch integrity using lossless immutable-history compatibility.

Dispatch reduction itself remains ``tools.research_dispatch``. This audit mirrors
its validation graph but composes the current task/result integrity wrappers so
resolved retained history is not rejected merely for historical field/body
spellings. Operational task selection and runtime dispatch semantics are unchanged.
"""
from __future__ import annotations

import argparse
from pathlib import Path

import research_result_record_audit
import research_task_record_audit
from tools import research_dispatch as dispatch

ROOT = Path(__file__).resolve().parent


def audit(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    legacy = dispatch.load_json(root / "research_scheduler.json")
    owners = dispatch.load_json(root / "branch_governance_overrides.json")
    try:
        dispatch.control_authorization_policy(root)
    except Exception as exc:
        errors.append(f"control-event authorization policy failure: {exc}")
    errors.extend(dispatch.research_scheduler.validate_scheduler(legacy, owners))
    errors.extend(research_task_record_audit.audit(root))
    errors.extend(dispatch.research_execution_records.audit(root))
    errors.extend(research_result_record_audit.audit(root))
    errors.extend(dispatch.research_cohort_runtime.audit(root))
    try:
        definitions = dispatch.merged_definitions(root)
    except Exception as exc:
        errors.append(f"merged dispatch definition failure: {exc}")
        return errors
    ids = [item.get("task_id") for item in definitions]
    if len(ids) != len(set(ids)):
        errors.append("canonical merged dispatch view contains duplicate task IDs")
    current = dispatch.research_task_records.current_records(root)
    for task_id in current:
        matches = [item for item in definitions if item.get("task_id") == task_id]
        if (
            len(matches) != 1
            or matches[0].get("registration_source") != "IMMUTABLE_TASK_RECORD"
        ):
            errors.append(
                f"{task_id}: registered task is not canonical in merged dispatch view"
            )
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Enterprise Math canonical dispatch integrity with immutable-history compatibility"
    )
    parser.add_argument("command", choices=["audit"])
    args = parser.parse_args()
    if args.command != "audit":
        raise AssertionError(args.command)
    errors = audit()
    if errors:
        for error in errors:
            print("ERROR:", error)
        return 1
    print(
        f"PASS: canonical dispatch integrity valid; {len(dispatch.merged_definitions())} "
        f"merged task definition(s), {len(dispatch.research_task_records.current_records())} "
        "immutable registered task(s)."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
