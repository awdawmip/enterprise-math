#!/usr/bin/env python3
"""Audit current Enterprise Math control-authority routing across active surfaces.

This checker is deliberately narrow and non-mathematical.  It verifies only the
post-cutover control facts owned by ``current_control_authority.json``:

* immutable V2 task publication;
* recovery-aware live dispatch versus subordinate fresh selectors;
* toolbox coverage versus actual reuse resolution;
* Foundation Steward V2 execution handoff;
* chat-only control-plane maintenance boundaries;
* V1 task-registry write commands remain fail-closed compatibility only.

It does not audit theorem truth, Driver mathematical verdicts, Foundation truth,
research-task mathematics, or discovery candidate content.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ControlAuthorityError(ValueError):
    pass


def load_json(path: str) -> dict:
    value = json.loads((ROOT / path).read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ControlAuthorityError(f"{path}: expected JSON object")
    return value


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ControlAuthorityError(message)


def check() -> None:
    authority = load_json("control_plane/current_control_authority.json")
    publication = load_json("research_task_publication_contract_v2.json")
    dispatch = load_json("research_dispatch_contract.json")
    tools = load_json("tool_invocation_policy.json")

    require(
        authority.get("schema") == "ENTERPRISE_MATH_CURRENT_CONTROL_AUTHORITY_V1",
        "current control authority: wrong schema",
    )
    require(
        authority.get("status") == "ACTIVE_CANONICAL_CONTROL_PRECEDENCE",
        "current control authority: not active canonical precedence",
    )

    task_auth = authority.get("task_publication", {})
    live_auth = authority.get("live_dispatch", {})
    tool_auth = authority.get("tool_reuse", {})
    control_auth = authority.get("control_liveness", {})

    require(
        task_auth.get("contract") == "research_task_publication_contract_v2.json",
        "task publication precedence must name V2 contract",
    )
    require(
        task_auth.get("tool") == "tools/research_task_records.py",
        "task publication precedence must use immutable V2 tool",
    )
    require(
        task_auth.get("legacy_role") == "READ_ONLY_COMPATIBILITY_AND_AUDIT_ONLY",
        "V1 registry must be read-only compatibility",
    )

    require(
        publication.get("control_dispatch_tool") == "research_control_dispatch.py",
        "V2 publication contract must name recovery-aware control dispatch",
    )
    require(
        publication.get("fresh_dispatch_selector") == "tools/research_dispatch.py",
        "V2 publication contract must distinguish ordinary fresh selector",
    )
    require(
        publication.get("control_dispatch_tool") == live_auth.get("canonical_entrypoint"),
        "publication and precedence disagree on live dispatch entrypoint",
    )
    require(
        publication.get("fresh_dispatch_selector") == live_auth.get("ordinary_fresh_selector"),
        "publication and precedence disagree on ordinary fresh selector",
    )
    require(
        dispatch.get("canonical_tool") == live_auth.get("canonical_entrypoint"),
        "dispatch contract and precedence disagree on canonical live entrypoint",
    )
    require(
        dispatch.get("fresh_task_dispatch_tool") == live_auth.get("ordinary_fresh_selector"),
        "dispatch contract and precedence disagree on fresh task selector",
    )
    require(
        dispatch.get("session_adoption_tool") == live_auth.get("stale_adoption_guard"),
        "dispatch contract and precedence disagree on stale-adoption guard",
    )
    require(
        dispatch.get("session_liveness_routing", {}).get("valid_owner_plus_stale_session")
        == "ADOPT_EXISTING_WINNING_CLAIM_WITHOUT_NEW_CLAIM",
        "stale valid owner must adopt same winning CLAIM",
    )

    require(
        tools.get("schema") == "ENTERPRISE_MATH_TOOL_INVOCATION_POLICY_V2",
        "tool invocation policy must be V2",
    )
    reuse = tools.get("reuse_resolution", {})
    require(reuse.get("coverage_hit_is_tool_use") is False, "coverage hit must not count as tool use")
    require(reuse.get("required_after_any_relevant_match") is True, "relevant tool match must require reuse resolution")
    require(
        "REUSE_IDENTIFIED_EXECUTION_UNAVAILABLE" in set(reuse.get("states", [])),
        "reuse resolution must represent execution unavailability separately",
    )
    require(tool_auth.get("coverage_lookup_is_tool_use") is False, "precedence must agree coverage lookup is not tool use")
    require(tool_auth.get("execution_unavailability_is_capability_gap") is False, "environment execution unavailability must not become capability gap")

    control_tools = tools.get("role_timing", {}).get("CONTROL_PLANE_MAINTENANCE", {})
    require(control_tools.get("mandatory") is False, "control maintenance must not inherit research toolbox mandate")
    require(control_tools.get("mathematical_toolbox_default") == "DO_NOT_OPEN", "control maintenance mathematical toolbox must default closed")
    require(control_auth.get("mode") == "CONTROL_PLANE_MAINTENANCE", "control liveness precedence missing maintenance mode")
    require(control_auth.get("watchdog") == "COOPERATIVE_SOFT_WATCHDOG", "control maintenance must use cooperative soft watchdog")

    publication_protocol = read("docs/RESEARCH_TASK_PUBLICATION_PROTOCOL.md")
    require("CANONICAL TASK PUBLICATION / V2" in publication_protocol, "human task publication protocol must be V2")
    require("python tools/research_task_records.py publish" in publication_protocol, "human publication protocol missing V2 publish command")
    require("python tools/research_task_registry.py publish" not in publication_protocol, "human publication protocol still instructs V1 publish")
    require("python tools/research_task_registry.py new" not in publication_protocol, "human publication protocol still instructs V1 new")

    driver = read("docs/RESEARCH_DRIVER_OPERATING_CONTRACT.md")
    require("V5.3" in driver, "Driver contract must be V5.3 or newer current control version")
    require("Task publication: `research_task_publication_contract_v2.json`" in driver, "Driver contract must use V2 publication")
    require("Canonical live dispatch: `research_control_dispatch.py`" in driver, "Driver contract must use recovery-aware live dispatch")
    require("COVERAGE_LOOKUP != TOOL_USE" in driver, "Driver contract must distinguish coverage from use")

    free_role = read("research_roles/EM_FREE_RESEARCHER_ROLE.md")
    require("ROLE-SPECIFIC CONTRACT V6.4" in free_role, "FREE role must be current V6.4 control version")
    require("Task publication: `research_task_publication_contract_v2.json`" in free_role, "FREE role must use V2 publication")
    require("Phase B — mandatory tool dedup and reuse resolution" in free_role, "FREE Phase B must require tool reuse resolution")

    architecture = read("docs/RESEARCH_ARCHITECTURE.md")
    require("ACTIVE / CANONICAL GOVERNANCE / V2.6" in architecture, "human research architecture must be V2.6")
    require("control_plane/current_control_authority.json" in architecture, "human architecture must route through narrow control precedence")
    require("research_control_dispatch.py" in architecture, "human architecture must name recovery-aware live dispatch")
    require("TOOL_COVERAGE_LOOKUP != TOOL_USE" in architecture, "human architecture must distinguish coverage from use")

    steward = read("docs/FOUNDATION_STEWARD_CONTROL_PLANE_ADDENDUM.md")
    require("tools/research_task_records.py prepare" in steward, "Steward addendum missing V2 prepare path")
    require("research_control_dispatch.py" in steward, "Steward addendum missing recovery-aware dispatch")
    require("COVERAGE_LOOKUP != TOOL_USE" in steward, "Steward addendum must distinguish coverage from use")

    agents = read("AGENTS.md")
    require("CONTROL_PLANE_MAINTENANCE" in agents, "AGENTS missing control-plane maintenance mode")
    require("research_control_dispatch.py" in agents, "AGENTS missing recovery-aware control dispatch")
    require("READ_SNAPSHOT != WRITE_AUTHORITY" in agents, "AGENTS missing mutation-authority boundary")

    legacy_tool = read("tools/research_task_registry.py")
    require("Read-only V1 task-registry compatibility surface" in legacy_tool, "V1 registry tool not explicitly read-only")
    require('for name in ("new", "publish", "select")' in legacy_tool, "V1 registry write/select commands are not all fail-closed")
    require("_forbid(command)" in legacy_tool, "V1 registry commands do not route through fail-closed guard")

    router = read("research_control_dispatch.py")
    require("research_control_bootstrap.install(ROOT)" in router, "live control router must install canonical bootstrap")
    require("research_dispatch.select_task" in router, "live control router must subordinate ordinary fresh selector")
    require("research_runtime.ADOPT_OWNER_CLAIM" in router, "live control router missing same-CLAIM adoption path")
    require('"VERIFY_SESSION_LIVENESS"' in router, "live control router missing unknown-liveness route")


def main() -> int:
    try:
        check()
    except (ControlAuthorityError, OSError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}")
        return 1
    print("PASS: current control authority, role routing, publication, dispatch, and tool-reuse surfaces are consistent.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
