#!/usr/bin/env python3
"""Cross-file consistency checks for the admitted X6 signed spatial foundation."""
from __future__ import annotations

import json
import pathlib
import sys

ROOT=pathlib.Path(__file__).resolve().parents[1]

p000=json.loads((ROOT/"p000_reality_foundation.json").read_text())
router=(ROOT/"definitions/00_CURRENT_NATIVE_FOUNDATION.md").read_text()
canonical=(ROOT/"definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md").read_text()

assert p000["schema"]=="ENTERPRISE_MATH_P000_REALITY_FOUNDATION_V5"
assert p000["derived_foundation_state"]["X6_NATIVE_SPATIAL_TRANSLATION_GROUP"]=="Z^6"
assert p000["derived_foundation_state"]["X6_NATIVE_SPATIAL_CELL_CENTER_FOUNDATION"]=="ACTIVE"
assert p000["derived_foundation_state"]["X6_JOINT_POSITIVE_SLICE_RELATIVE_OBSERVER"]=="Z^6 / Z(1,1,1,1,1,1)"
assert p000["axioms"]["NATIVE_PRIMITIVE_DIRECTION_DOMAIN"]=="SIGNED_NATIVE_SPATIAL_AXES"
assert p000["axioms"]["ENTERPRISE_NATIVE_RIGHT_ANGLE_DEGREES"]==120
assert p000["axioms"]["NATIVE_SPATIAL_AXIS_COUNT"]==6

required_router=(
    "ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md",
    "X6_NATIVE_SPATIAL = AFFINE_TORSOR(Z^6)",
    "G6_REL=Z^6/Delta",
    "X6_AXIS_PERMUTATION_ROTATION_SKELETON=S6",
    "COMMON_DEPTH != SEVENTH_SPATIAL_AXIS",
)
for token in required_router:
    assert token in router, token

required_definition=(
    "X6_NATIVE_SPATIAL = AFFINE_TORSOR(Z^6)",
    "FULL_NATIVE_SPATIAL_CELL_CENTER_IDENTITY_IS_COMPLETE_IN_SIX_SIGNED_AXIS_COORDINATES = TRUE",
    "G6_REL := Z^6 / Delta",
    "L_E(+e_i)=L_E(-e_i)=1",
    "X6_AXIS_PERMUTATION_ROTATION_SKELETON = S6",
    "COMMON_DEPTH != SEVENTH_SPATIAL_AXIS",
)
for token in required_definition:
    assert token in canonical, token

# Ensure the superseded full-spatial relative-quotient candidate is absent from current tree.
assert not (ROOT/"definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_CANDIDATE_20260905.md").exists()

# Reuse both current executable layers: full signed spatial and relative observer.
sys.path.insert(0,str(ROOT/"experiments/x6_signed_native_spatial_v16_20260905"))
sys.path.insert(0,str(ROOT/"experiments/x6_native_coordinate_completion_v7_20260905"))
from x6_signed import Spatial6, DIAGONAL, joint_slice_equal
from x6_coordinate import Coord6

origin=Spatial6((0,0,0,0,0,0))
diagonal=Spatial6(DIAGONAL)
assert diagonal!=origin
assert diagonal.norm_squared_from_origin()==6
assert joint_slice_equal(origin,diagonal)

# The relative observer kills exactly the diagonal difference.
assert Coord6.from_integer_lift(origin.coords)==Coord6.from_integer_lift(diagonal.coords)

# Full signed reverse is unit length, whereas the old relative canonical reverse is five ones.
full_reverse=origin.step(0,-1)
assert full_reverse.norm_squared_from_origin()==1
relative_reverse=Coord6.from_integer_lift(full_reverse.coords)
assert sorted(relative_reverse.values)==[0,1,1,1,1,1]
assert relative_reverse.norm_squared()==5

print("PASS_X6_FOUNDATION_ADMISSION")
print("p000_schema=V5")
print("full_spatial=Z^6_signed_torsor")
print("relative_observer=Z^6/Z1")
print("full_diagonal_nonzero_but_joint_positive_slice_invisible=true")
print("full_reverse_norm2=1; relative_positive_canonical_reverse_norm2=5")
