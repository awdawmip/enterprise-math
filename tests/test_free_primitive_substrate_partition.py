import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def test_free_substrate_router_is_primitive_only_partition():
    text = read("definitions/00_FREE_AXIOM_DISCOVERY_SUBSTRATE.md")
    assert "FOUNDATION_FOR_DISCOVERY != CATALOG_OF_CURRENT_ACHIEVEMENTS" in text
    assert "ENTERPRISE_THREE_POSITIVE_AXIS_OVERLAPPING_CIRCLE_CELL_PLANE_20260820.md" in text
    for downstream in (
        "ENTERPRISE_NATIVE_LINE_TRACE_FORMULA_20260821.md",
        "ENTERPRISE_ARBITRARY_POINT_DIRECTED_LINE_GAUGE_20260821.md",
        "ENTERPRISE_UNORIENTED_BIDIRECTIONAL_SEGMENT_SPECTRUM_20260821.md",
        "ENTERPRISE_BRC_MULTIPATH_ENRICHMENT_BRIDGE_20260821.md",
        "ENTERPRISE_PATH_VALUED_SQUARE_ROOT_OPERATOR_20260821.md",
    ):
        assert downstream in text
    assert "DO_NOT_PRELOAD = definitions/00_CURRENT_NATIVE_FOUNDATION.md" in text


def test_machine_architecture_routes_free_phase_a_to_primitive_substrate():
    arch = json.loads(read("research_architecture.json"))
    free = arch["research_modes"]["FREE_AXIOM_DISCOVERY"]
    assert free["phase_a_substrate_router"] == "definitions/00_FREE_AXIOM_DISCOVERY_SUBSTRATE.md"
    assert free["general_current_router_before_candidate_freeze"] is False
    assert free["general_current_router_phase_b"] == "definitions/00_CURRENT_NATIVE_FOUNDATION.md"
    assert free["agenda_visibility_before_candidate_freeze"] == "PRIMITIVE_SUBSTRATE_ONLY"
    visibility = arch["context_visibility"]["free_phase_a"]
    assert "definitions/00_FREE_AXIOM_DISCOVERY_SUBSTRATE.md" in visibility["allow"]
    assert any("00_CURRENT_NATIVE_FOUNDATION.md" in item for item in visibility["withhold_as_discovery_prior"])
    assert arch["read_performance"]["free_phase_a_general_current_router_preload"] is False


def test_free_role_and_anti_anchor_do_not_preload_general_current_router():
    role = read("research_roles/EM_FREE_RESEARCHER_ROLE.md")
    anti = read("research_roles/EM_FREE_RESEARCHER_ANTI_ANCHORING_PROTOCOL.md")
    for text in (role, anti):
        assert "definitions/00_FREE_AXIOM_DISCOVERY_SUBSTRATE.md" in text
        assert "definitions/00_CURRENT_NATIVE_FOUNDATION.md" in text
        assert "Do **not** preload" in text
    assert "current line/gauge/bidirectional/BRC/path-root canonical result files" in role
    assert "DOWNSTREAM_CANONICAL_SUCCESS_IS_NOT_PHASE_A_SUBSTRATE" in anti


def test_general_current_router_remains_available_for_phase_b_and_task_research():
    substrate = read("definitions/00_FREE_AXIOM_DISCOVERY_SUBSTRATE.md")
    assert "The full current router becomes available in Phase B" in substrate
    current = read("definitions/00_CURRENT_NATIVE_FOUNDATION.md")
    assert "ENTERPRISE_NATIVE_LINE_TRACE_FORMULA_20260821.md" in current
    assert "ENTERPRISE_BRC_MULTIPATH_ENRICHMENT_BRIDGE_20260821.md" in current
