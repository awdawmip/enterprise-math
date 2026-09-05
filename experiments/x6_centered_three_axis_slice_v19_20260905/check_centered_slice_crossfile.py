from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DEF = ROOT / "definitions"

machine = json.loads((DEF / "ENTERPRISE_X6_CENTERED_THREE_AXIS_SLICE_REBASE_20260905.json").read_text())
assert machine["status"] == "ACTIVE_FOUNDATION"
assert machine["slice"]["coordinate_carrier"] == "Z^3"
assert machine["slice"]["zero"] == "CHOSEN_NATIVE_CELL_ANCHOR"
assert machine["slice"]["zero_is_cell"] is True
assert machine["slice"]["native_distance_symmetric"] is True
assert machine["relative_observer"]["min_zero_alone_is_native_identity"] is False
assert machine["fcc_star_carrier"]["kernel"] == "Z*(1,1,1)"
assert machine["brc"]["triangle_carrier_return_is_native_return"] is False
assert machine["recomputed_witnesses"]["signed_n25_shell"]["endpoint_count"] == 30
assert machine["recomputed_witnesses"]["signed_n25_shell"]["total_shortest_brc_count"] == 846

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
assert p000["derived_foundation_state"]["X6_NATIVE_SPATIAL_TRANSLATION_GROUP"] == "Z^6"

print("centered-slice cross-file consistency: PASS")
