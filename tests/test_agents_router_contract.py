from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_agents_is_small_execution_router_not_research_catalog():
    text = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
    assert "STABLE EXECUTION ROUTER" in text
    assert "not** a theorem catalog" in text
    assert len(text.splitlines()) < 260
    assert len(text) < 12000
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
    text = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
    assert "definitions/00_FREE_AXIOM_DISCOVERY_SUBSTRATE.md" in text
    assert "FOUNDATION_FOR_DISCOVERY != CATALOG_OF_CURRENT_ACHIEVEMENTS" in text
    assert "NO_DEFAULT_DISCOVERY_LENS_MENU" in text
    assert "do not preload `definitions/00_CURRENT_NATIVE_FOUNDATION.md`" in text
    assert "do not supply a suggested-question or discovery-lens menu" in text
    assert "generic exclusion categories" in text


def test_agents_task_start_is_exact_task_first_not_common_surface_first():
    text = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
    assert "**the exact task entry**" in text
    assert "**the first exact dependency actually required to begin**" in text
    assert "Soft routine source-read budget before substantive work: `<= 3`" in text
    assert "Common Surface is an ownership/tool/conflict **lookup**" in text
    assert "automatic second read" in text


def test_agents_uses_current_candidate_successor_and_promotion_boundaries():
    text = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
    for marker in (
        "RAW_AXIOM_CANDIDATE != WORKING_TRUTH != CANONICAL_FOUNDATION",
        "PASS_IS_NOT_A_SUCCESSOR_TRIGGER",
        "READY_PR != PROMOTION_LANE_LEASE",
        "docs/GOVERNANCE_MAINTENANCE_LIVENESS.md",
    ):
        assert marker in text


def test_tool_surface_matches_agents_role_routing_without_transition_guard():
    text = (ROOT / "docs" / "EM_RESEARCH_TOOL_SURFACE.md").read_text(encoding="utf-8")
    assert "HOT-PATH V4" in text
    assert "definitions/00_FREE_AXIOM_DISCOVERY_SUBSTRATE.md" in text
    assert "definitions/00_CURRENT_NATIVE_FOUNDATION.md" in text
    assert "the exact task entry" in text
    assert "Do **not** make Common Surface an automatic second read" in text
    assert "Until that source governance is promoted" not in text
    assert "suggested question/discovery-lens menu" in text


def test_free_role_has_no_residual_concrete_lens_examples():
    text = (ROOT / "research_roles" / "EM_FREE_RESEARCHER_ROLE.md").read_text(encoding="utf-8")
    assert "V6.1" in text
    assert "NO_DEFAULT_DISCOVERY_LENS_MENU" in text
    for seeded_example in (
        "invariance / locality",
        "composition / cancellation",
        "symmetry breaking",
        "minimal sufficient state",
    ):
        assert seeded_example not in text
