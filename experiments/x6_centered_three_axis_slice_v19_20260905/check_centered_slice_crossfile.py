from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DEF = ROOT / "definitions"

machine = json.loads((DEF / "ENTERPRISE_X6_CENTERED_THREE_AXIS_SLICE_REBASE_20260905.json").read_text())
assert machine["schema"] == "ENTERPRISE_X6_CENTERED_THREE_AXIS_SLICE_REBASE_V2"
assert machine["status"] == "ACTIVE_FOUNDATION"
assert machine["semantic_authority"]["native_global_distinguished_origin_exists"] is False
assert machine["semantic_authority"]["coordinate_zero_kind"] == "CHOSEN_NATIVE_CELL_ANCHOR"
assert machine["semantic_authority"]["legacy_O_E_current_type"] == "CARRIER_TRIPLE_INCIDENCE_VERTEX"
assert machine["slice"]["coordinate_carrier"] == "Z^3"
assert machine["slice"]["zero"] == "CHOSEN_NATIVE_CELL_ANCHOR"
assert machine["slice"]["zero_is_cell"] is True
assert machine["slice"]["zero_is_global_ontic_origin"] is False
assert machine["slice"]["native_distance_symmetric"] is True
assert machine["slice"]["selected_observation_is_slice_membership"] is False
assert machine["relative_observer"]["min_zero_alone_is_native_identity"] is False
assert machine["relative_observer"]["drop_requires_observer_future_operation_certificate"] is True
assert machine["fcc_star_carrier"]["kernel"] == "Z*(1,1,1)"
assert machine["fcc_star_carrier"]["kernel_is_native_coordinate_equivalence"] is False
assert machine["fcc_star_carrier"]["circle_footprint_is_native_cell_identity"] is False
assert machine["brc"]["triangle_carrier_return_is_native_return"] is False
assert machine["brc"]["signed_native_reversal_preserves_length"] is True
assert machine["brc"]["signed_native_reversal_preserves_shortest_multiplicity"] is True
assert machine["recomputed_witnesses"]["signed_n25_shell"]["endpoint_count"] == 30
assert machine["recomputed_witnesses"]["signed_n25_shell"]["total_shortest_brc_count"] == 846

required_hard_errors = {
    "TREAT_LEGACY_O_E_TRIPLE_INTERSECTION_AS_NATIVE_COORDINATE_ZERO",
    "ASSERT_DISTINGUISHED_GLOBAL_NATIVE_SPATIAL_ORIGIN_FROM_CHART_ZERO",
    "REMOVE_ZERO_CELL_FROM_CENTERED_NATIVE_AXIS",
    "PROMOTE_MIN_ZERO_TRIPLE_TO_NATIVE_CELL_IDENTITY",
    "DROP_CENTERED_SLICE_COMMON_DEPTH_WITHOUT_SCOPE_TYPED_SAFE_QUOTIENT",
    "PROMOTE_FCC_CARRIER_KERNEL_TO_NATIVE_COORDINATE_EQUIVALENCE",
    "PROMOTE_CARRIER_CIRCLE_FOOTPRINT_TO_NATIVE_CELL_IDENTITY",
    "USE_CARRIER_EUCLIDEAN_Q_AS_NATIVE_SIGNED_SLICE_METRIC",
    "TREAT_LEGACY_DIRECTED_MIN_ZERO_GAUGE_AS_NATIVE_SIGNED_DISTANCE",
    "INFER_NATIVE_REVERSAL_FROM_POSITIVE_MIN_ZERO_RECANONICALIZATION",
    "IDENTIFY_CARRIER_TRIANGLE_RETURN_WITH_NATIVE_CELL_RETURN",
    "TREAT_SELECTED_THREE_AXIS_OBSERVER_AS_PROOF_OF_SLICE_MEMBERSHIP",
}
assert required_hard_errors <= set(machine["hard_errors"])

router = (DEF / "00_CURRENT_NATIVE_FOUNDATION.md").read_text()
required_router = [
    "THREE_AXIS_NATIVE_SLICE_ZERO = CHOSEN_CELL_CENTER",
    "THREE_AXIS_NATIVE_SLICE_ZERO_IS_CELL = TRUE",
    "THREE_AXIS_NATIVE_SLICE_COORDINATES = Z^3_SIGNED",
    "MIN_ZERO_THREE_AXIS_ADDRESS != NATIVE_CELL_IDENTITY",
    "CARRIER_TRIANGLE_RETURN != NATIVE_CELL_RETURN",
    "FULL_SIGNED_THREE_AXIS_N25_ENDPOINT_COUNT=30",
]
for token in required_router:
    assert token in router, token

x6_human = (DEF / "ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md").read_text()
required_x6 = [
    "P000-V5-BOUND",
    "NATIVE_SPATIAL_DISTINGUISHED_GLOBAL_ORIGIN_EXISTS = FALSE",
    "CELL_COORDINATE_ZERO = CHOSEN_NATIVE_CELL_ANCHOR",
    "CELL_COORDINATE_ZERO_IS_CHART_RELATIVE = TRUE",
    "LEGACY_O_E_TRIPLE_BOUNDARY_INTERSECTION = CARRIER_INCIDENCE_VERTEX_NOT_NATIVE_ORIGIN",
    "SELECTED_THREE_AXIS_OBSERVATION != CENTERED_THREE_AXIS_SLICE_MEMBERSHIP",
    "CARRIER_TRIANGLE_RETURN != NATIVE_CELL_RETURN",
]
for token in required_x6:
    assert token in x6_human, token
assert "CELL_COORDINATE_ZERO = CHOSEN_CELL_ANCHOR != GEOMETRIC_ORIGIN_O_E" not in x6_human

legacy_slice = (DEF / "ENTERPRISE_THREE_POSITIVE_AXIS_OVERLAPPING_CIRCLE_CELL_PLANE_20260820.md").read_text()
assert "SUPERSEDED_AS_NATIVE_SLICE" in legacy_slice
assert "NATIVE_SLICE_ZERO = CHOSEN_CELL_CENTER" in legacy_slice

legacy_gauge = (DEF / "ENTERPRISE_ARBITRARY_POINT_DIRECTED_LINE_GAUGE_20260821.md").read_text()
assert "RELATIVE-OBSERVER GAUGE ONLY" in legacy_gauge
assert "NATIVE_POINT_TO_POINT_DISTANCE_IS_SYMMETRIC = TRUE" in legacy_gauge
assert "REVERSAL_LENGTH_SYMMETRY = false" not in legacy_gauge

legacy_spectrum = (DEF / "ENTERPRISE_UNORIENTED_BIDIRECTIONAL_SEGMENT_SPECTRUM_20260821.md").read_text()
assert "SUPERSEDED AS NATIVE LENGTH REPAIR" in legacy_spectrum
assert "NATIVE_SIGNED_SLICE_DISTANCE_IS_REVERSAL_SYMMETRIC=true" in legacy_spectrum

brc_bridge = (DEF / "ENTERPRISE_BRC_MULTIPATH_ENRICHMENT_BRIDGE_20260821.md").read_text()
assert "SIGNED_NATIVE_REVERSAL_PRESERVES_N_BRC_MULTIPLICITY" in brc_bridge
assert "CARRIER_ENDPOINT_RECOALESCENCE != NATIVE_ENDPOINT_RECOALESCENCE" in brc_bridge

fcc = (DEF / "P000_FCC_PRIMARY_COORDINATE_CARRIER_20260829.md").read_text()
assert "STAR_CARRIER_CENTER_READOUT = Z3/Z(1,1,1)" in fcc
assert "NATIVE_SLICE_ZERO = CHOSEN_CELL_CENTER" in fcc

g1 = (DEF / "ENTERPRISE_DERIVED_DIAGONAL_DISPLACEMENT_QUOTIENT_20260826.md").read_text()
assert "G_REL3 = THREE_AXIS_RELATIVE/CARRIER_ENDPOINT_QUOTIENT" in g1
assert "G_REL3 != NATIVE_SIGNED_SLICE_DISPLACEMENT" in g1

p000 = json.loads((ROOT / "p000_reality_foundation.json").read_text())
assert p000["axioms"]["NATIVE_PRIMITIVE_DIRECTION_DOMAIN"] == "SIGNED_NATIVE_SPATIAL_AXES"
assert p000["axioms"]["CURRENT_THREE_AXIS_MODEL"] == "RESEARCH_SLICE_OF_6D_SPACE"
derived = p000["derived_foundation_state"]
assert derived["X6_NATIVE_SPATIAL_TRANSLATION_GROUP"] == "Z^6"
assert derived["X6_NATIVE_SPATIAL_DISTINGUISHED_GLOBAL_ORIGIN"] == "NONE"
assert derived["X6_NATIVE_SPATIAL_COORDINATE_ZERO_KIND"] == "CHOSEN_NATIVE_CELL_ANCHOR"
assert derived["X6_NATIVE_SPATIAL_COORDINATE_ZERO_IS_CHART_RELATIVE"] is True
assert derived["X6_CENTERED_THREE_AXIS_SLICE_FOUNDATION"] == "ACTIVE"
assert derived["X6_CENTERED_THREE_AXIS_SLICE_ZERO_IS_CELL"] is True
assert derived["X6_CENTERED_THREE_AXIS_SLICE_ZERO_IS_GLOBAL_ONTIC_ORIGIN"] is False
assert derived["X6_CENTERED_THREE_AXIS_SLICE_NATIVE_REVERSAL_SYMMETRIC"] is True
assert derived["X6_CARRIER_TRIANGLE_RETURN_IS_NATIVE_RETURN"] is False

p000_machine = set(p000["machine_invariants"])
required_p000_invariants = {
    "NATIVE_SPATIAL_DISTINGUISHED_GLOBAL_ORIGIN_EXISTS=false",
    "CELL_COORDINATE_ZERO=CHOSEN_NATIVE_CELL_ANCHOR",
    "CELL_COORDINATE_ZERO_IS_CHART_RELATIVE=true",
    "CENTERED_THREE_AXIS_NATIVE_SLICE=AFFINE_SUBTORSOR_OF_X6",
    "CENTERED_THREE_AXIS_SLICE_ZERO_IS_CELL=true",
    "SELECTED_THREE_AXIS_OBSERVATION != CENTERED_THREE_AXIS_SLICE_MEMBERSHIP",
    "MIN_ZERO_THREE_AXIS_ADDRESS!=NATIVE_CELL_IDENTITY",
    "CARRIER_TRIANGLE_RETURN!=NATIVE_CELL_RETURN",
    "CENTERED_THREE_AXIS_NATIVE_REVERSAL_SYMMETRIC=true",
    "LEGACY_DIRECTED_MIN_ZERO_GAUGE!=NATIVE_SIGNED_METRIC",
}
assert required_p000_invariants <= p000_machine

required_p000_hard_errors = {
    "TREAT_LEGACY_O_E_TRIPLE_INTERSECTION_AS_NATIVE_COORDINATE_ZERO",
    "ASSERT_DISTINGUISHED_GLOBAL_NATIVE_SPATIAL_ORIGIN_FROM_CHART_ZERO",
    "REMOVE_ZERO_CELL_FROM_CENTERED_NATIVE_AXIS",
    "PROMOTE_MIN_ZERO_THREE_AXIS_ADDRESS_TO_NATIVE_CELL_IDENTITY",
    "DROP_CENTERED_SLICE_COMMON_DEPTH_WITHOUT_SCOPE_TYPED_SAFE_QUOTIENT",
    "PROMOTE_FCC_STAR_CARRIER_KERNEL_TO_NATIVE_COORDINATE_EQUIVALENCE",
    "USE_CARRIER_EUCLIDEAN_Q_AS_NATIVE_SIGNED_SLICE_METRIC",
    "TREAT_LEGACY_DIRECTED_MIN_ZERO_GAUGE_AS_NATIVE_SIGNED_DISTANCE",
    "INFER_NATIVE_REVERSAL_FROM_POSITIVE_MIN_ZERO_RECANONICALIZATION",
    "IDENTIFY_CARRIER_TRIANGLE_RETURN_WITH_NATIVE_CELL_RETURN",
}
assert required_p000_hard_errors <= set(p000["hard_errors"])

print("centered-slice cross-file consistency: PASS")
