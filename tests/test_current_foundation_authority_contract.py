from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def test_root_project_definition_routes_three_positive_axis_foundation():
    zh = read("PROJECT_DEFINITION.zh-CN.md")
    en = read("PROJECT_DEFINITION.md")
    machine = read("project_definition.json")
    for text in (zh, en, machine):
        upper = text.upper()
        assert (
            "THREE_POSITIVE" in upper
            or "THREE-POSITIVE" in upper
            or "THREE POSITIVE" in upper
            or "三条正" in text
        )
        assert "120" in text
        assert "ENTERPRISE_THREE_POSITIVE_AXIS_OVERLAPPING_CIRCLE_CELL_PLANE_20260820.md" in text


def test_stable_current_router_freezes_current_plane():
    text = read("definitions/00_CURRENT_NATIVE_FOUNDATION.md")
    required = [
        "O_E=0",
        "three positive rays",
        "ENTERPRISE_RIGHT_ANGLE=120_DEGREES",
        "min(a,b,c)=0",
        "ENTERPRISE_NATIVE_LINE_TRACE_FORMULA_20260821.md",
        "ENTERPRISE_ARBITRARY_POINT_DIRECTED_LINE_GAUGE_20260821.md",
        "ENTERPRISE_UNORIENTED_BIDIRECTIONAL_SEGMENT_SPECTRUM_20260821.md",
        "ENTERPRISE_BRC_MULTIPATH_ENRICHMENT_BRIDGE_20260821.md",
    ]
    for token in required:
        assert token in text


def test_obsolete_ontology_files_are_not_active_canonical():
    historical = [
        "definitions/ENTERPRISE_COORDINATE_SYSTEM_AND_BRC_BRIDGE_20260816.md",
        "definitions/ENTERPRISE_SIGNED_ORIGIN_ONE_COORDINATE_20260817.md",
        "definitions/ENTERPRISE_COORDINATE_ORIGIN_ONE_NO_ZERO_20260817.md",
        "definitions/ENTERPRISE_ORIGIN_IS_DIAMETER_ONE_CIRCLE_20260817.md",
        "definitions/ENTERPRISE_INITIAL_CIRCLE_ALL_UNIT_INVARIANTS_20260817.md",
        "definitions/ENTERPRISE_CHAMBER_LOCAL_ALGEBRAIC_VECTOR_OPERATIONS_20260817.md",
    ]
    for path in historical:
        head = read(path)[:600]
        assert "SUPERSEDED" in head or "HISTORICAL" in head


def test_research_tool_surface_requires_current_router():
    text = read("docs/EM_RESEARCH_TOOL_SURFACE.md")
    assert "definitions/00_CURRENT_NATIVE_FOUNDATION.md" in text
