import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def test_root_project_definition_routes_current_routers_only():
    zh = read("PROJECT_DEFINITION.zh-CN.md")
    en = read("PROJECT_DEFINITION.md")
    machine = json.loads(read("project_definition.json"))

    for text in (zh, en):
        assert "definitions/00_CURRENT_NATIVE_FOUNDATION.md" in text
        assert "definitions/00_FREE_AXIOM_DISCOVERY_SUBSTRATE.md" in text
        assert "120" in text
        assert not re.search(r"\bR0\d{2}\b", text)
        assert "SUPERSEDED_BY_USER" not in text
        assert "six native" not in text.lower()

    assert machine["schema"] == "ENTERPRISE_MATH_PROJECT_DEFINITION_V4"
    assert machine["authority_chain"]["current_native_router"] == "definitions/00_CURRENT_NATIVE_FOUNDATION.md"
    assert machine["authority_chain"]["free_discovery_substrate_router"] == "definitions/00_FREE_AXIOM_DISCOVERY_SUBSTRATE.md"
    dumped = json.dumps(machine, ensure_ascii=False)
    assert "SUPERSEDED" not in dumped
    assert "historical_carrier_typing" not in dumped


def test_current_native_router_preserves_p000_x6_and_typed_observers():
    text = read("definitions/00_CURRENT_NATIVE_FOUNDATION.md")
    for token in (
        "../p000_reality_foundation.json",
        "ENTERPRISE_SPACE_DIMENSION=6",
        "ENTERPRISE_TIME_DIMENSION=1",
        "ENTERPRISE_RIGHT_ANGLE=120_DEGREES",
        "X6_NATIVE_SPATIAL = AFFINE_TORSOR(Z^6)",
        "THREE_AXIS_NATIVE_SLICE_ZERO = CHOSEN_CELL_CENTER",
        "MIN_ZERO_THREE_AXIS_ADDRESS != NATIVE_CELL_IDENTITY",
        "MIN_ZERO_ADDRESS + INTEGER_COMMON_DEPTH = LOSSLESS_RAW_SLICE_COORDINATE",
        "ENTERPRISE_JOINT_RELATION_OBSERVER_PRESERVATION_20260905.json",
        "ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md",
        "ENTERPRISE_X6_CENTERED_THREE_AXIS_SLICE_REBASE_20260905.md",
        "ENTERPRISE_NATIVE_LINE_TRACE_FORMULA_20260821.md",
        "ENTERPRISE_ARBITRARY_POINT_DIRECTED_LINE_GAUGE_20260821.md",
        "ENTERPRISE_UNORIENTED_BIDIRECTIONAL_SEGMENT_SPECTRUM_20260821.md",
        "ENTERPRISE_BRC_MULTIPATH_ENRICHMENT_BRIDGE_20260821.md",
        "ENTERPRISE_BRC_WEIGHTED_GLOBAL_SUBSTRATE_20260902.json",
        "Positive Weighted-BRC remains distinct from signed/phase cancellation",
        "Exact current canonical definitions control over this router summary",
        "FREE Phase A",
    ):
        assert token in text

    assert "now retyped composite-path combinatorics" in text
    assert "now relative-observer gauge only" in text
    assert "now observer diagnostic only" in text
    assert "O_E=0" not in text
    assert "CANONICAL_BRC_BASE_LAYER=BOOLEAN_RESULT_SUPPORT_SEMANTICS" not in text
    assert "Historical / superseded family" not in text
    assert "signed-origin" not in text


def test_free_and_general_current_router_are_separate():
    current = read("definitions/00_CURRENT_NATIVE_FOUNDATION.md")
    free = read("definitions/00_FREE_AXIOM_DISCOVERY_SUBSTRATE.md")
    routes = json.loads(read("project_definition.json"))["authority_chain"]
    assert routes["free_discovery_substrate_router"] == "definitions/00_FREE_AXIOM_DISCOVERY_SUBSTRATE.md"
    assert routes["current_native_router"] == "definitions/00_CURRENT_NATIVE_FOUNDATION.md"
    assert "FREE Phase A uses only its governing primitive substrate" in current
    assert "DO_NOT_PRELOAD = definitions/00_CURRENT_NATIVE_FOUNDATION.md" in free
    assert "NO_DEFAULT_DISCOVERY_LENS_MENU" in free


def test_tool_surface_is_connector_first_and_exact_task_first():
    text = read("docs/EM_RESEARCH_TOOL_SURFACE.md")
    assert "CONNECTED_GITHUB_PLUGIN = PRIMARY_REMOTE_GITHUB_PATH" in text
    assert "chat/container networking" in text
    assert "MAX_ROUTINE_SOURCE_READS_BEFORE_SUBSTANTIVE_WORK = 3" in text
    assert "exact task entry" in text
    assert "first exact dependency required to begin" in text
    assert "Do not poll CI" in text


def test_agents_is_connector_first_and_current_only():
    text = read("AGENTS.md")
    assert "CONNECTED_GITHUB_PLUGIN = PRIMARY_REMOTE_GITHUB_PATH" in text
    assert "Current-only hot path" in text
    assert "current execution router" in text.lower()
    assert not re.search(r"\bR0\d{2}\b", text)


def test_github_budget_does_not_fallback_to_chat_container_for_remote_github():
    text = read("docs/GITHUB_INTERACTION_BUDGET.md")
    assert "CONNECTED_GITHUB_PLUGIN = PRIMARY_REMOTE_GITHUB_PATH" in text
    assert "Do not use ChatGPT/container networking" in text
    assert "do not retry it later" in text
    assert "0 routine workflow-status queries" in text
