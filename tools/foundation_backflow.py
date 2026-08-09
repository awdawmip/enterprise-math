#!/usr/bin/env python3
"""Validate the research-to-Foundation closed-loop router.

This is a governance validator. It checks cross-surface links among the static
Foundation backflow router and research scheduler. It deliberately does not try
to infer live FQ or scheduler runtime state from GitHub; Issue #164 and #240
remain the authorities for those mutable states.
"""

from __future__ import annotations

import argparse
import json
import pathlib
import re
import sys
from typing import Any

ROOT = pathlib.Path(__file__).resolve().parents[1]
DEFAULT_BACKFLOW = ROOT / "foundation_backflow.json"
DEFAULT_SCHEDULER = ROOT / "research_scheduler.json"

FQ_RE = re.compile(r"^FQ-\d{8}-\d{3}$")
ROLE_TO_KIND = {
    "RESEARCH": "RESEARCH",
    "STEWARD_VERIFICATION": "GOVERNANCE",
    "INTEGRATION": "GOVERNANCE",
}


class BackflowError(ValueError):
    pass


def load_json(path: pathlib.Path) -> dict[str, Any]:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise BackflowError(f"cannot load {path}: {exc}") from exc


def validate_backflow(backflow: dict[str, Any], scheduler: dict[str, Any]) -> list[str]:
    errors: list[str] = []

    if backflow.get("schema") != "ENTERPRISE_MATH_FOUNDATION_BACKFLOW_V1":
        errors.append("unexpected foundation backflow schema")
    if backflow.get("status") != "ACTIVE":
        errors.append("foundation backflow router must be ACTIVE")

    surfaces = backflow.get("surfaces", {})
    authority = scheduler.get("authority", {})
    expected_surface_pairs = [
        ("research_relay_issue", "research_relay_issue"),
        ("foundation_problem_issue", "foundation_problem_issue"),
    ]
    for backflow_key, scheduler_key in expected_surface_pairs:
        if surfaces.get(backflow_key) != authority.get(scheduler_key):
            errors.append(
                f"surface mismatch: backflow {backflow_key}={surfaces.get(backflow_key)!r} "
                f"!= scheduler {scheduler_key}={authority.get(scheduler_key)!r}"
            )
    if surfaces.get("research_dispatch_issue") != scheduler.get("scheduler_issue"):
        errors.append("research dispatch issue does not match scheduler_issue")
    if surfaces.get("scheduler_config") != "research_scheduler.json":
        errors.append("backflow scheduler_config must be research_scheduler.json")

    required_packet = {
        "candidate_object_or_tool",
        "weakest_scope_hypotheses",
        "minimal_state",
        "minimal_repair_or_extension",
        "negative_boundary",
        "cross_route_evidence",
        "proof_status",
        "tool_surface",
        "prior_art_and_owner",
        "foundation_destination",
    }
    packet = backflow.get("feedback_packet_fields", [])
    if set(packet) != required_packet or len(packet) != len(required_packet):
        errors.append("Foundation Feedback Packet fields drifted from the canonical contract")

    handling = set(backflow.get("handling_classes", []))
    required_handling = {
        "DIRECT_FOUNDATION_MAINTENANCE",
        "FOUNDATION_QUESTION",
        "APPLICATION_LOCAL_OR_NOT_READY",
    }
    if handling != required_handling:
        errors.append("foundation handling classes drifted from the three-way classification")

    task_by_id = {task.get("task_id"): task for task in scheduler.get("tasks", [])}
    seen_questions: set[str] = set()
    for index, link in enumerate(backflow.get("question_scheduler_links", [])):
        prefix = f"question_scheduler_links[{index}]"
        question_id = link.get("question_id")
        if not isinstance(question_id, str) or not FQ_RE.fullmatch(question_id):
            errors.append(f"{prefix}: invalid question_id {question_id!r}")
            continue
        if question_id in seen_questions:
            errors.append(f"{prefix}: duplicate question link for {question_id}")
        seen_questions.add(question_id)

        task_id = link.get("scheduler_task_id")
        task = task_by_id.get(task_id)
        if task is None:
            errors.append(f"{prefix}: unknown scheduler task {task_id!r}")
            continue

        role = link.get("scheduler_role")
        expected_kind = ROLE_TO_KIND.get(role)
        if expected_kind is None:
            errors.append(f"{prefix}: invalid scheduler_role {role!r}")
        elif task.get("kind") != expected_kind:
            errors.append(
                f"{prefix}: role {role} requires task kind {expected_kind}, "
                f"got {task.get('kind')!r}"
            )

        if role == "RESEARCH":
            owner = link.get("research_owner")
            if owner != task.get("owner"):
                errors.append(
                    f"{prefix}: research_owner {owner!r} must match task owner {task.get('owner')!r}"
                )

        refs = link.get("source_refs")
        if not isinstance(refs, list) or not refs or not all(isinstance(ref, str) and ref for ref in refs):
            errors.append(f"{prefix}: source_refs must be a nonempty string list")

    if backflow.get("authority_boundaries", {}).get("canonical_truth") != "gated source-repository main":
        errors.append("canonical truth boundary must remain gated source-repository main")

    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Enterprise Math foundation backflow validator")
    parser.add_argument("--backflow", type=pathlib.Path, default=DEFAULT_BACKFLOW)
    parser.add_argument("--scheduler", type=pathlib.Path, default=DEFAULT_SCHEDULER)
    args = parser.parse_args(argv)

    try:
        backflow = load_json(args.backflow)
        scheduler = load_json(args.scheduler)
    except BackflowError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    errors = validate_backflow(backflow, scheduler)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print(
        "PASS: foundation backflow router valid; "
        f"{len(backflow.get('question_scheduler_links', []))} FQ scheduler links checked."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
