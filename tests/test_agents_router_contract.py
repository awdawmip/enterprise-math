from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def test_agents_is_small_execution_router_not_research_catalog():
    text = read("AGENTS.md")
    assert "STABLE EXECUTION ROUTER" in text
    assert "V2.7" in text
    assert "not** a theorem catalog" in text
    assert len(text.splitlines()) < 340
    assert len(text) < 18000
    for stale_or_agenda_token in (
        "Issue #240",
        "Issue #164",
        "Research Relay #82",
        "classical pi",
        "root choice",
        "random-walk",
        "graph distance",
        "State Pair",
        "A4 correspondence",
    ):
        assert stale_or_agenda_token not in text


def test_agents_routes_free_to_primitive_substrate_without_menu():
    text = read("AGENTS.md")
    assert "definitions/00_FREE_AXIOM_DISCOVERY_SUBSTRATE.md" in text
    assert "FOUNDATION_FOR_DISCOVERY != CATALOG_OF_CURRENT_ACHIEVEMENTS" in text
    assert "NO_DEFAULT_DISCOVERY_LENS_MENU" in text
    assert "do not preload the general current-result router" in text
    assert "do not supply suggested questions or discovery-lens menus" in text
    assert "generic exclusion categories" in text


def test_agents_task_start_is_exact_task_first_not_common_surface_first():
    text = read("AGENTS.md")
    assert "**the exact task entry**" in text
    assert "the first exact dependency required to begin" in text
    assert "Soft routine source-read budget before substantive work: `<= 3`" in text
    assert "Common Surface is a lookup" in text


def test_agents_uses_current_candidate_successor_and_promotion_boundaries():
    text = read("AGENTS.md")
    for marker in (
        "RAW_AXIOM_CANDIDATE != WORKING_TRUTH != CANONICAL_FOUNDATION",
        "PASS_IS_NOT_A_SUCCESSOR_TRIGGER",
        "READY_PR != PROMOTION_LANE_LEASE",
        "docs/GOVERNANCE_MAINTENANCE_LIVENESS.md",
    ):
        assert marker in text


def test_agents_routes_all_task_coordination_through_scheduler_v2():
    text = read("AGENTS.md")
    for marker in (
        "research_scheduler_v2.json",
        "docs/RESEARCH_SCHEDULER_V2_QUICKSTART.md",
        "PUBLISH != READY",
        "RETURN != DONE",
        "LEASE_EXPIRY -> ORPHANED",
        "EXECUTABLE_TASKBOOK -> REGISTERED_TASK_ID",
    ):
        assert marker in text


def test_agents_preserves_tool_reuse_gate_after_identity_merge():
    text = read("AGENTS.md")
    for marker in (
        "tool_invocation_policy.json",
        "docs/ENTERPRISE_TOOL_INVOCATION_PROTOCOL.md",
        "enterprise_toolbox_registry.json",
        "research_method_inventory.json",
        "tools/enterprise_toolbox.py",
        "UNDERSTAND_TASK_FIRST -> TOOL_LOOKUP_SECOND",
        "NEW_TOOL_DIRECTION_REQUIRES_CONFIRMED_CAPABILITY_GAP",
        "Discovery-firewall timing exception",
    ):
        assert marker in text


def test_agents_makes_final_role_identity_footer_unconditional():
    text = read("AGENTS.md")
    assert "final_response_identity_policy.json" in text
    assert (
        "ACTIVE_ENTERPRISE_MATH_ROLE -> "
        "EVERY_ASSISTANT_FINAL_RESPONSE_ENDS_WITH_EXACTLY_ONE_ROLE_IDENTITY_MARKER"
        in text
    )
    assert "Driver-ID: <ID> / CONTROL_PLANE" in text
    assert "Researcher-ID: <ID> / <TASK_ID>" in text
    assert "Researcher-ID: <ID> / FREE_AXIOM_DISCOVERY" in text
    assert "Researcher-ID: <ID> / TASK_RESEARCH" in text
    assert "Do not use `DIRECT` as a visible researcher scope" in text


def test_tool_surface_matches_agents_role_routing_without_transition_guard():
    text = read("docs/EM_RESEARCH_TOOL_SURFACE.md")
    assert "HOT-PATH V4" in text
    assert "definitions/00_FREE_AXIOM_DISCOVERY_SUBSTRATE.md" in text
    assert "definitions/00_CURRENT_NATIVE_FOUNDATION.md" in text
    assert "the exact task entry" in text
    assert "Do **not** make Common Surface an automatic second read" in text
    assert "Until that source governance is promoted" not in text
    assert "suggested question/discovery-lens menu" in text


def test_free_role_preserves_blind_tool_timing_and_can_publish_mature_work():
    text = read("research_roles/EM_FREE_RESEARCHER_ROLE.md")
    assert "V7.0" in text
    assert "NO_DEFAULT_DISCOVERY_LENS_MENU" in text
    assert "Phase B" in text
    assert "tool_invocation_policy.json" in text
    assert "PUBLISHED / NEEDS_REVIEW" in text
    assert "FREE researcher may author the derived taskbook itself" in text
    assert "Researcher-ID: <ID> / FREE_AXIOM_DISCOVERY" in text
    assert "Every final response" in text
    for seeded_example in (
        "invariance / locality",
        "composition / cancellation",
        "symmetry breaking",
        "minimal sufficient state",
    ):
        assert seeded_example not in text
