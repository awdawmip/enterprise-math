import json
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

    parsed = json.loads(machine)
    dumped = json.dumps(parsed, ensure_ascii=False).upper()
    assert "THREE_POSITIVE" in dumped or "THREE-POSITIVE" in dumped


def test_stable_current_router_freezes_current_plane_and_is_lazy():
    text = read("definitions/00_CURRENT_NATIVE_FOUNDATION.md")
    required = [
        "O_E=0",
        "three positive rays",
        "ENTERPRISE_RIGHT_ANGLE=120_DEGREES",
        "min(a,b,c)=0",
        "No native common diagonal-shift quotient",
        "ENTERPRISE_NATIVE_LINE_TRACE_FORMULA_20260821.md",
        "ENTERPRISE_ARBITRARY_POINT_DIRECTED_LINE_GAUGE_20260821.md",
        "ENTERPRISE_UNORIENTED_BIDIRECTIONAL_SEGMENT_SPECTRUM_20260821.md",
        "ENTERPRISE_BRC_MULTIPATH_ENRICHMENT_BRIDGE_20260821.md",
        "CANONICAL_BRC_BASE_LAYER=BOOLEAN_RESULT_SUPPORT_SEMANTICS",
        "Load by dependency",
        "Do not read all six",
    ]
    for token in required:
        assert token in text


def test_current_router_uses_two_stage_authority_resolution():
    text = read("definitions/00_CURRENT_NATIVE_FOUNDATION.md")
    assert "Two-stage authority rule" in text
    assert "Stage 1 — generation selection" in text
    assert "Stage 2 — exact content inside the selected current generation" in text
    assert "EXACT CURRENT CANONICAL DEFINITION -> CURRENT ROUTER SUMMARY" in text


def test_all_reconciled_obsolete_ontology_files_are_explicitly_noncurrent():
    historical = [
        "definitions/ENTERPRISE_CHAMBER_LOCAL_ALGEBRAIC_VECTOR_OPERATIONS_20260817.md",
        "definitions/ENTERPRISE_COORDINATE_ORIGIN_ONE_NO_ZERO_20260817.md",
        "definitions/ENTERPRISE_COORDINATE_SYSTEM_AND_BRC_BRIDGE_20260816.md",
        "definitions/ENTERPRISE_INITIAL_CIRCLE_ALL_UNIT_INVARIANTS_20260817.md",
        "definitions/ENTERPRISE_ORIGIN_IS_DIAMETER_ONE_CIRCLE_20260817.md",
        "definitions/ENTERPRISE_POINT_ORIGIN_AND_DISPLACEMENT_ZERO_20260817.md",
        "definitions/ENTERPRISE_SEGMENT_ALL_SHORTEST_PATHS_20260817.md",
        "definitions/ENTERPRISE_SIGNED_ORIGIN_ONE_COORDINATE_20260817.md",
        "definitions/ENTERPRISE_SQUARE_AND_ROOT_20260816.md",
        "definitions/ENTERPRISE_SQUARE_AND_ROOT_ORIGIN_ONE_20260817.md",
        "definitions/ENTERPRISE_SQUARE_AND_ROOT_SIGNED_ORIGIN_ONE_20260817.md",
        "definitions/ENTERPRISE_VECTOR_NORM_ENDPOINT_REVERSE_GEODESIC_SEGMENT_20260817.md",
        "definitions/ENTERPRISE_VECTOR_RADIUS_DISCRETE_ROTATION_THEORY_20260817.md",
        "definitions/ENTERPRISE_VOID_ORIGIN_EXISTENCE_GEODESIC_20260817.md",
    ]
    noncurrent_markers = (
        "SUPERSEDED",
        "HISTORICAL",
        "PARTIALLY_SUPERSEDED",
        "DOWNSTREAM_ONLY",
        "AUXILIARY",
    )
    for path in historical:
        head = read(path)[:1400].upper()
        assert any(marker in head for marker in noncurrent_markers), path
        if "STATUS:" in head and "ACTIVE / CANONICAL / FOUNDATIONAL" in head:
            assert "SUPERSEDED" in head or "HISTORICAL" in head, path


def test_historical_machine_records_cannot_restore_old_ontology():
    for path in (
        "definitions/enterprise_coordinate_system_and_brc_bridge.json",
        "definitions/enterprise_square_root_origin_one.json",
    ):
        data = json.loads(read(path))
        status = str(data.get("status", "")).upper()
        assert "SUPERSEDED" in status or "HISTORICAL" in status
        dumped = json.dumps(data, ensure_ascii=False)
        assert "THREE_POSITIVE_NATIVE_RAYS" in dumped
        assert '"right_angle_degrees": 120' in dumped


def test_research_tool_surface_matches_three_read_exact_task_first_hot_path():
    text = read("docs/EM_RESEARCH_TOOL_SURFACE.md")
    assert "MAX_ROUTINE_SOURCE_READS_BEFORE_SUBSTANTIVE_WORK = 3" in text
    assert "AGENTS.md" in text
    assert "the exact task entry" in text
    assert "the first exact dependency actually needed to begin" in text
    assert "Do **not** make `research_common_surface.json`" in text
    assert "triggered ownership/theorem/tool/conflict lookup surfaces" in text
    assert "definitions/00_CURRENT_NATIVE_FOUNDATION.md" in text
    assert "Do not poll CI" in text
    assert "Re-reading unchanged routers/PR metadata" in text
    assert "FREE_AXIOM_DISCOVERY" in text
    assert "ANCHOR_EXPOSED" in text
