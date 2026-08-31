import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


DOWNSTREAM_NAMES = (
    "ENTERPRISE_NATIVE_LINE_TRACE_FORMULA_20260821.md",
    "ENTERPRISE_ARBITRARY_POINT_DIRECTED_LINE_GAUGE_20260821.md",
    "ENTERPRISE_UNORIENTED_BIDIRECTIONAL_SEGMENT_SPECTRUM_20260821.md",
    "ENTERPRISE_BRC_MULTIPATH_ENRICHMENT_BRIDGE_20260821.md",
    "ENTERPRISE_PATH_VALUED_SQUARE_ROOT_OPERATOR_20260821.md",
)


def test_free_substrate_router_is_primitive_only_and_does_not_name_withheld_achievements():
    text = read("definitions/00_FREE_AXIOM_DISCOVERY_SUBSTRATE.md")
    assert "FOUNDATION_FOR_DISCOVERY != CATALOG_OF_CURRENT_ACHIEVEMENTS" in text
    assert "NO_DEFAULT_DISCOVERY_LENS_MENU" in text
    assert "ENTERPRISE_THREE_POSITIVE_AXIS_OVERLAPPING_CIRCLE_CELL_PLANE_20260820.md" in text
    assert "DO_NOT_PRELOAD = definitions/00_CURRENT_NATIVE_FOUNDATION.md" in text
    assert "Do not enumerate or preload the project's current downstream achievements" in text
    for downstream in DOWNSTREAM_NAMES:
        assert downstream not in text


def test_machine_architecture_routes_free_phase_a_to_primitive_substrate_without_prompt_menu():
    arch = json.loads(read("research_architecture.json"))
    free = arch["research_modes"]["FREE_AXIOM_DISCOVERY"]
    assert free["phase_a_substrate_router"] == "definitions/00_FREE_AXIOM_DISCOVERY_SUBSTRATE.md"
    assert free["general_current_router_before_candidate_freeze"] is False
    assert free["general_current_router_phase_b"] == "definitions/00_CURRENT_NATIVE_FOUNDATION.md"
    assert free["agenda_visibility_before_candidate_freeze"] == "PRIMITIVE_SUBSTRATE_ONLY"
    assert free["default_discovery_lens_menu"] is None
    assert free["default_suggested_question_menu"] is None
    assert free["phase_a_forbidden_object_enumeration"] is False
    visibility = arch["context_visibility"]["free_phase_a"]
    assert "definitions/00_FREE_AXIOM_DISCOVERY_SUBSTRATE.md" in visibility["allow"]
    assert any("general current-result router" in item for item in visibility["withhold_as_discovery_prior"])
    assert visibility["negative_instruction_style"].startswith("GENERIC_CATEGORIES_ONLY")
    assert visibility["candidate_generation_prompt_style"] == "NO_DEFAULT_QUESTION_OR_LENS_MENU"
    assert arch["read_performance"]["free_phase_a_general_current_router_preload"] is False
    assert arch["read_performance"]["free_phase_a_default_discovery_prompt_menu"] is False


def test_role_policy_matches_primitive_zero_suggestion_machine_contract():
    policy = json.loads(read("research_role_policy.json"))
    free = policy["research_modes"]["FREE_AXIOM_DISCOVERY"]
    assert free["phase_a_substrate_router"] == "definitions/00_FREE_AXIOM_DISCOVERY_SUBSTRATE.md"
    assert free["agenda_visibility_before_candidate_freeze"] == "PRIMITIVE_SUBSTRATE_ONLY"
    assert free["general_current_router_before_candidate_freeze"] is False
    assert free["default_suggested_question_menu"] is None
    assert free["default_discovery_lens_menu"] is None
    assert free["negative_instruction_style"] == "GENERIC_CATEGORIES_ONLY"
    assert free["negative_instruction_style"] == "GENERIC_CATEGORIES_ONLY"
    assert free["generic_no_user_task_scheduler_rule_applies"] is False


def test_free_role_and_anti_anchor_do_not_name_specific_downstream_achievements_or_seed_lens_menu():
    role = read("research_roles/EM_FREE_RESEARCHER_ROLE.md")
    anti = read("research_roles/EM_FREE_RESEARCHER_ANTI_ANCHORING_PROTOCOL.md")
    for text in (role, anti):
        assert "definitions/00_FREE_AXIOM_DISCOVERY_SUBSTRATE.md" in text
        assert "definitions/00_CURRENT_NATIVE_FOUNDATION.md" in text
        assert "Do **not** preload" in text
        for downstream in DOWNSTREAM_NAMES:
            assert downstream not in text
    assert "NO_DEFAULT_DISCOVERY_LENS_MENU" in role
    assert "The first substantive question is authored by the researcher" in role
    assert "NO_SUGGESTED_DISCOVERY_LENS_LIST" in anti
    assert "NEGATIVE_INSTRUCTION_MUST_NOT_ENUMERATE_SALIENT_FORBIDDEN_OBJECTS" in anti


def test_human_architecture_matches_primitive_zero_suggestion_contract():
    text = read("docs/RESEARCH_ARCHITECTURE.md")
    assert "definitions/00_FREE_AXIOM_DISCOVERY_SUBSTRATE.md" in text
    assert "FOUNDATION_FOR_DISCOVERY != CATALOG_OF_CURRENT_ACHIEVEMENTS" in text
    assert "NO_DEFAULT_DISCOVERY_LENS_MENU" in text
    assert "current task/route/history" in text.lower()
    assert "suggestion menu" in text.lower()
    for downstream in DOWNSTREAM_NAMES:
        assert downstream not in text


def test_general_current_router_remains_available_only_after_free_candidate_freeze():
    substrate = read("definitions/00_FREE_AXIOM_DISCOVERY_SUBSTRATE.md")
    role = read("research_roles/EM_FREE_RESEARCHER_ROLE.md")
    assert "The full current router becomes available in Phase B" in substrate
    assert "Only after freeze may current/prior project research context be opened for Phase-B audit." in role
    current = read("definitions/00_CURRENT_NATIVE_FOUNDATION.md")
    # The richer router still owns current-result lookup; only its Phase-A visibility changed.
    assert "ENTERPRISE_NATIVE_LINE_TRACE_FORMULA_20260821.md" in current
    assert "ENTERPRISE_BRC_MULTIPATH_ENRICHMENT_BRIDGE_20260821.md" in current
