#!/usr/bin/env python3
"""Mechanical audit for Scheduler V2 control-plane wiring.

This does not inspect mathematical truth. It verifies that the current hot-path
routers, role policy, taskbook contract, identity state machine and CI all point
to the same V2 workflow rather than leaving a mixed V1/V2 operational surface.
"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_json(path: str):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def text(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def audit() -> list[str]:
    errors: list[str] = []
    scheduler = load_json("research_scheduler_v2.json")
    role = load_json("research_role_policy.json")
    identity = load_json("research_identity_state_machine.json")
    taskbook = load_json("research_taskbook_contract.json")
    architecture = load_json("research_architecture.json")
    agents = text("AGENTS.md")
    toolsurface = text("docs/EM_RESEARCH_TOOL_SURFACE.md")
    scheduling = text("docs/RESEARCH_SCHEDULING_PROTOCOL.en.md")
    quickstart = text("docs/RESEARCH_SCHEDULER_V2_QUICKSTART.md")
    nonblocking = text("docs/RESEARCH_SCHEDULER_NONBLOCKING_STARTUP.md")
    quality = text(".github/workflows/quality.yml")

    if scheduler.get("schema") != "ENTERPRISE_MATH_RESEARCH_SCHEDULER_V2":
        errors.append("canonical scheduler schema is not V2")
    for required in ("PUBLISHED", "RETURNED", "ORPHANED", "DONE"):
        if required not in scheduler.get("task_states", []):
            errors.append(f"scheduler missing state {required}")
    for required in ("PUBLISH", "REVIEW", "RETURN", "ORPHAN", "RECOVER"):
        if required not in scheduler.get("event_types", []):
            errors.append(f"scheduler missing event {required}")

    free = role.get("research_modes", {}).get("FREE_AXIOM_DISCOVERY", {})
    if free.get("scheduler_eligible") is not False:
        errors.append("FREE must remain excluded from automatic scheduler work")
    if free.get("scheduler_publish_eligible") is not True:
        errors.append("FREE must be allowed to publish mature tasks")
    if free.get("scheduler_auto_claim_eligible") is not False:
        errors.append("FREE must not auto-claim scheduler tasks")

    authority = role.get("official_taskbook_authority", {})
    if authority.get("task_authority") != "SCHEDULER_REVIEW_REQUIRED":
        errors.append("new taskbooks do not require scheduler review")
    if authority.get("scheduler_ready_state_requires_driver_review") is not True:
        errors.append("READY is not Driver-review gated")

    gate = taskbook.get("scheduler_gate", {})
    expected_gate = {
        "publication_state": "PUBLISHED",
        "dispatch_accept_state": "READY",
        "worker_completion_event": "RETURN",
        "return_state": "RETURNED",
        "completion_accept_state": "DONE",
    }
    for key, expected in expected_gate.items():
        if gate.get(key) != expected:
            errors.append(f"taskbook scheduler gate {key}={gate.get(key)!r}, expected {expected!r}")

    if identity.get("scheduler") != "research_scheduler_v2.json":
        errors.append("identity state machine does not point to scheduler V2")
    if identity.get("scheduler_publish", {}).get("publication_grants_ready_authority") is not False:
        errors.append("identity policy incorrectly lets publication grant READY")

    boundary = architecture.get("scheduler_boundary", {})
    if boundary.get("contract") != "research_scheduler_v2.json":
        errors.append("research architecture does not point to scheduler V2")
    if boundary.get("all_official_tasks_registered") is not True:
        errors.append("architecture does not require all official tasks registered")

    for path, body in (
        ("AGENTS.md", agents),
        ("docs/EM_RESEARCH_TOOL_SURFACE.md", toolsurface),
        ("docs/RESEARCH_SCHEDULING_PROTOCOL.en.md", scheduling),
        ("docs/RESEARCH_SCHEDULER_V2_QUICKSTART.md", quickstart),
    ):
        if "research_scheduler_v2.json" not in body:
            errors.append(f"{path} does not route to scheduler V2")
        if "PUBLISH != READY" not in body:
            errors.append(f"{path} lacks PUBLISH != READY guard")
        if "RETURN != DONE" not in body:
            errors.append(f"{path} lacks RETURN != DONE guard")

    if "old V1 allowance" not in nonblocking or "superseded" not in nonblocking:
        errors.append("nonblocking addendum does not explicitly supersede V1 unleased execution")
    if "UNLEASED_EXPLORATION != CLAIMED_EXECUTION" not in nonblocking:
        errors.append("nonblocking addendum lacks unleased/claimed distinction")

    if "python tools/research_scheduler.py validate" not in quality:
        errors.append("quality workflow does not validate scheduler V2")
    if "python tools/research_scheduler.py registry-integrity" not in quality:
        errors.append("quality workflow does not enforce registry integrity")

    registry = scheduler.get("registry_integrity", {})
    if registry.get("auto_register_untracked_taskbooks_as_orphaned") is not True:
        errors.append("untracked taskbooks are not auto-registered as orphans")
    if registry.get("untracked_taskbook_dispatchable") is not False:
        errors.append("untracked taskbook orphan is dispatchable")

    return errors


def main() -> int:
    errors = audit()
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("PASS: Scheduler V2 control-plane wiring is internally consistent across router, roles, taskbooks, identities and CI.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
