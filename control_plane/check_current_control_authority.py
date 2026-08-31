#!/usr/bin/env python3
"""Audit current Enterprise Math control-authority routing across active surfaces.

This checker is deliberately narrow and non-mathematical. It verifies only the
post-cutover control facts owned by ``current_control_authority.json``:

* immutable V2 task publication;
* recovery-aware live dispatch versus subordinate fresh selectors;
* exact owner-scope liveness rather than generic chat activity;
* deterministic external liveness/recovery bookkeeping without CLAIM authority;
* one-shot Researcher durable handoff;
* toolbox coverage versus actual reuse resolution;
* typed role transitions that preserve provenance without leaking authority;
* Foundation Steward V2 execution handoff;
* chat-only control-plane maintenance boundaries;
* V1 task-registry write commands remain fail-closed compatibility only.

It does not audit theorem truth, Driver mathematical verdicts, Foundation truth,
research-task mathematics, or discovery candidate content.
"""
from __future__ import annotations

import json
import re
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


def require_version_at_least(text: str, label: str, major: int, minor: int) -> None:
    match = re.search(r"Status: `[^`]* / V(\d+)\.(\d+)`", text)
    if match is None:
        raise ControlAuthorityError(f"{label}: cannot parse status version")
    current = (int(match.group(1)), int(match.group(2)))
    required = (major, minor)
    if current < required:
        raise ControlAuthorityError(
            f"{label}: version V{current[0]}.{current[1]} is below required V{major}.{minor}"
        )


def check() -> None:
    authority = load_json("control_plane/current_control_authority.json")
    publication = load_json("research_task_publication_contract_v2.json")
    dispatch = load_json("research_dispatch_contract.json")
    tools = load_json("tool_invocation_policy.json")
    transitions = load_json("control_plane/role_transition_matrix.json")

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
    handoff_auth = authority.get("researcher_durable_handoff", {})
    tool_auth = authority.get("tool_reuse", {})
    role_auth = authority.get("role_transitions", {})
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
        dispatch.get("schema") == "ENTERPRISE_MATH_RESEARCH_DISPATCH_CONTRACT_V5",
        "dispatch contract must be exact-owner-scope V5",
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
    session = dispatch.get("session_liveness_routing", {})
    require(session.get("owner_lease_is_session_liveness") is False, "owner lease must not imply session liveness")
    require(session.get("conversation_activity_is_owner_scope_liveness") is False, "generic conversation activity must not imply owner-scope liveness")
    require(
        session.get("observation_schema") == "ENTERPRISE_MATH_SESSION_LIVENESS_OBSERVATIONS_V2",
        "session observation schema must be owner-scope V2",
    )
    require(
        set(session.get("allowed_activity_evidence_kinds", []))
        == {"TASK_RESEARCH_RESPONSE", "DURABLE_EXECUTION_PROGRESS"},
        "owner-scope liveness evidence kinds must be exact and closed",
    )
    excluded = set(session.get("does_not_count_as_owner_scope_activity", []))
    require("CONTROL_PLANE_MAINTENANCE response" in excluded, "control responses must not refresh task owner liveness")
    require("FREE_AXIOM_DISCOVERY response" in excluded, "FREE responses must not refresh task owner liveness")
    require(
        session.get("valid_owner_plus_stale_session")
        == "ADOPT_EXISTING_WINNING_CLAIM_WITHOUT_NEW_CLAIM",
        "stale valid owner must adopt same winning CLAIM",
    )
    require(
        session.get("claim_mismatch_observation", "").startswith("IGNORE_AS_LIVENESS_EVIDENCE"),
        "foreign/stale claim activity must not keep current owner active",
    )
    require(
        live_auth.get("external_supervisor") == "infrastructure/cloudflare-supervisor/",
        "live dispatch precedence must name the external Supervisor",
    )
    require(
        live_auth.get("external_supervisor_creates_claims") is False,
        "external Supervisor must not create CLAIM authority",
    )

    require(
        handoff_auth.get("protocol") == "docs/RESEARCHER_DURABLE_HANDOFF_PROTOCOL.md",
        "durable handoff precedence must name its protocol",
    )
    require(
        set(handoff_auth.get("accepted_durable_surfaces", [])) == {"GITHUB", "GOOGLE_DRIVE"},
        "durable handoff surfaces must be exact and closed",
    )
    require(
        handoff_auth.get("researcher_id_is_addressable_mailbox") is False,
        "Researcher-ID must remain provenance rather than an addressable mailbox",
    )
    require(
        handoff_auth.get("github_ref_must_be_immutable_commit") is True,
        "GitHub durable handoff must require an immutable commit",
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
    require(control_auth.get("owner_state_alarm_atomic") is True, "Supervisor state and alarm updates must be atomic")
    require(control_auth.get("no_op_progress_refreshes_lease") is False, "no-op progress must not refresh a turn lease")
    require(control_auth.get("recovery_workflow_start_idempotent") is True, "recovery Workflow start must be idempotent")
    require(control_auth.get("recovery_retry_alarm_required") is True, "failed recovery Workflow start must re-arm recovery")
    require(
        control_auth.get("external_supervisor_has_mathematical_or_claim_authority") is False,
        "external Supervisor must have no mathematical or CLAIM authority",
    )

    require(
        transitions.get("schema") == "ENTERPRISE_MATH_ROLE_TRANSITION_MATRIX_V1",
        "role transition matrix: wrong schema",
    )
    require(
        transitions.get("status") == "ACTIVE_CANONICAL_CONTROL_TRANSITIONS",
        "role transition matrix: not active canonical transitions",
    )
    require(
        role_auth.get("matrix") == "control_plane/role_transition_matrix.json",
        "control precedence does not point to role transition matrix",
    )
    require(role_auth.get("mode") == "TYPED_SELECTIVE_MERGE", "role transitions must use typed selective merge")
    require(role_auth.get("role_switch_is_context_reset") is False, "role switch must not pretend context reset")
    require(role_auth.get("source_role_authority_persists_implicitly") is False, "source role authority must not leak across role switch")
    require(role_auth.get("role_switch_releases_or_duplicates_claim") is False, "role switch must not release/duplicate CLAIM by itself")
    require(role_auth.get("free_clean_blindness_recoverable_after_agenda_exposure") is False, "FREE CLEAN blindness must be monotone after exposure")
    require(role_auth.get("working_truth_follows_role_label") is False, "Working Truth must not follow role label")
    require("OWNER_SCOPE_LIVENESS" in transitions.get("state_dimensions", []), "role transition matrix missing owner-scope liveness dimension")
    require(
        "ONLY_EXACT_CLAIM_BOUND_TASK_RESPONSE_OR_DURABLE_PROGRESS_REFRESHES_OWNER_SCOPE_LIVENESS"
        in transitions.get("core_invariants", []),
        "role transition matrix missing exact owner-scope liveness invariant",
    )

    transition_rows = transitions.get("transitions", {})
    required_transition_rows = {
        "CONTROL_PLANE_MAINTENANCE->TASK_RESEARCH",
        "CONTROL_PLANE_MAINTENANCE->RESEARCH_DRIVER",
        "CONTROL_PLANE_MAINTENANCE->FOUNDATION_STEWARD",
        "CONTROL_PLANE_MAINTENANCE->FREE_AXIOM_DISCOVERY",
        "TASK_RESEARCH->CONTROL_PLANE_MAINTENANCE",
        "RESEARCH_DRIVER->CONTROL_PLANE_MAINTENANCE",
        "FOUNDATION_STEWARD->CONTROL_PLANE_MAINTENANCE",
        "FREE_AXIOM_DISCOVERY->CONTROL_PLANE_MAINTENANCE",
        "TASK_RESEARCH->FREE_AXIOM_DISCOVERY",
        "FREE_AXIOM_DISCOVERY->TASK_RESEARCH",
        "TASK_RESEARCH->RESEARCH_DRIVER",
        "RESEARCH_DRIVER->TASK_RESEARCH",
        "FOUNDATION_STEWARD->TASK_RESEARCH",
        "TASK_RESEARCH->FOUNDATION_STEWARD",
    }
    require(required_transition_rows <= set(transition_rows), "role transition matrix missing required cross-role transitions")
    require(
        transition_rows["CONTROL_PLANE_MAINTENANCE->FREE_AXIOM_DISCOVERY"].get("blindness", "").startswith("ANCHOR_EXPOSED"),
        "control-maintenance to FREE must disclose anchor exposure when current context was inspected",
    )
    require(
        transition_rows["TASK_RESEARCH->CONTROL_PLANE_MAINTENANCE"].get("research_authority") == "SUSPEND",
        "TASK to control transition must suspend research authority",
    )
    require(
        transition_rows["TASK_RESEARCH->CONTROL_PLANE_MAINTENANCE"].get("owner_scope_liveness", "").startswith("DO_NOT_REFRESH_OWNER_LIVENESS"),
        "TASK to control transition must stop refreshing task owner liveness",
    )
    require(
        transition_rows["TASK_RESEARCH->RESEARCH_DRIVER"].get("owner_scope_liveness", "").startswith("DO_NOT_REFRESH_OWNER_LIVENESS"),
        "TASK to Driver transition must stop refreshing task owner liveness",
    )
    require(
        transition_rows["TASK_RESEARCH->FOUNDATION_STEWARD"].get("owner_scope_liveness", "").startswith("DO_NOT_REFRESH_OWNER_LIVENESS"),
        "TASK to Steward transition must stop refreshing task owner liveness",
    )
    require(
        transition_rows["RESEARCH_DRIVER->CONTROL_PLANE_MAINTENANCE"].get("driver_authority") == "CLEAR_AUTHORITY",
        "Driver to control transition must clear Driver authority",
    )
    require(
        transition_rows["FOUNDATION_STEWARD->CONTROL_PLANE_MAINTENANCE"].get("steward_authority") == "CLEAR_AUTHORITY",
        "Steward to control transition must clear Steward authority",
    )

    publication_protocol = read("docs/RESEARCH_TASK_PUBLICATION_PROTOCOL.md")
    require("CANONICAL TASK PUBLICATION / V2" in publication_protocol, "human task publication protocol must be V2")
    require("python tools/research_task_records.py publish" in publication_protocol, "human publication protocol missing V2 publish command")
    require("python tools/research_task_registry.py publish" not in publication_protocol, "human publication protocol still instructs V1 publish")
    require("python tools/research_task_registry.py new" not in publication_protocol, "human publication protocol still instructs V1 new")

    driver = read("docs/RESEARCH_DRIVER_OPERATING_CONTRACT.md")
    require_version_at_least(driver, "Driver contract", 5, 3)
    require("Task publication: `research_task_publication_contract_v2.json`" in driver, "Driver contract must use V2 publication")
    require("Canonical live dispatch: `research_control_dispatch.py`" in driver, "Driver contract must use recovery-aware live dispatch")
    require("COVERAGE_LOOKUP != TOOL_USE" in driver, "Driver contract must distinguish coverage from use")
    require("Review write authority: `research_review_write_authority.json`" in driver, "Driver contract missing review write authority")
    require("READ_SNAPSHOT != REVIEW_WRITE_AUTHORITY" in driver, "Driver contract missing review write-boundary invariant")

    handoff = read("docs/RESEARCHER_DURABLE_HANDOFF_PROTOCOL.md")
    require("RESEARCHER_ID != ADDRESSABLE_MAILBOX" in handoff, "handoff protocol must freeze one-shot Researcher identity")
    require("immutable commit SHA" in handoff, "handoff protocol must require immutable GitHub locators")

    supervisor = read("infrastructure/cloudflare-supervisor/README.md")
    require("no mathematical authority" in supervisor, "external Supervisor boundary must remain non-mathematical")
    require("OWNER_STATE_AND_ALARM_UPDATE -> ONE STORAGE TRANSACTION" in supervisor, "Supervisor docs missing atomic alarm invariant")

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
    require("ENTERPRISE_MATH_SESSION_LIVENESS_OBSERVATIONS_V2" in router, "live control router missing owner-scope observation V2")
    require("TASK_RESEARCH_RESPONSE" in router, "live control router missing task-response liveness kind")
    require("DURABLE_EXECUTION_PROGRESS" in router, "live control router missing durable-progress liveness kind")
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
    print("PASS: current control authority, owner-scope liveness, role transitions, publication, dispatch, and tool-reuse surfaces are consistent.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
