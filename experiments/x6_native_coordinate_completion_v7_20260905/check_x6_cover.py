#!/usr/bin/env python3
"""Exact regression for common-depth Cell covers."""
from itertools import product
from pathlib import Path
import sys

from x6_coordinate import Coord6, ORIGIN_COORD
from x6_cover import CoverState, depth_carry, diagonal_loop, first_positive_diagonal_return

# P000 V5 signed-native reference: a CoverState with modulus=0 must
# reconstruct the exact same six-axis Cell after every primitive step.
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "experiments" / "x6_signed_native_spatial_v16_20260905"))
from x6_signed import Spatial6


def main():
    checks=0
    coords=(
        ORIGIN_COORD,
        Coord6((1,0,0,0,0,0)),
        Coord6((3,1,0,5,2,4)),
        Coord6((0,2,4,1,3,5)),
        Coord6((7,0,2,9,1,4)),
    )

    # Associativity is exactly the old common-depth 2-cocycle identity.
    for m in range(0,8):
        states=[CoverState(a,d,m) for a in coords for d in (-3,-1,0,1,4)]
        for a in states:
            for b in states:
                for c in states:
                    assert a.compose(b).compose(c)==a.compose(b.compose(c))
                    checks+=1

    # Coordinate result is independent of cover modulus; only common-depth
    # identity changes.
    for m in range(0,8):
        for a in coords:
            for b in coords:
                lhs=CoverState(a,0,m).compose(CoverState(b,0,m))
                assert lhs.coordinate.values==tuple(
                    x-min(x+y for x,y in zip(a.values,b.values))
                    for x in (tuple(x+y for x,y in zip(a.values,b.values)))
                )
                assert lhs.depth==(depth_carry(a,b) if m==0 else depth_carry(a,b)%m)
                checks+=2

    # One complete six-positive-axis diagonal loop advances only the cover fibre.
    for m in range(0,9):
        origin=CoverState(ORIGIN_COORD,0,m)
        once=diagonal_loop(origin,1)
        assert once.coordinate==ORIGIN_COORD
        assert once.depth==(1 if m==0 else 1%m)
        checks+=2
        first=first_positive_diagonal_return(m)
        if first is None:
            for r in range(1,10):
                assert diagonal_loop(origin,r)!=origin
                checks+=1
        else:
            for r in range(1,first):
                assert diagonal_loop(origin,r)!=origin
                checks+=1
            assert diagonal_loop(origin,first)==origin
            checks+=1

    # m=1 is coordinate-complete only in the quotient-cover model,
    # not in the current P000 signed-native Cell identity (m=0).
    for a in coords:
        for d in range(-20,21):
            assert CoverState(a,d,1)==CoverState(a,0,1)
            checks+=1

    # New exact cross-module native regression, including negative depths.
    # This tests the real existing CoverState.step against Spatial6.step.
    native_states=0
    native_steps=0
    for z in product(range(-2,3), repeat=6):
        h=min(z)
        relative=Coord6.from_integer_lift(z)
        cover=CoverState(relative,h,0)
        signed=Spatial6(z)
        assert cover.signed_native_displacement()==signed.coords
        native_states+=1
        checks+=1
        for axis in range(6):
            for direction in (-1,+1):
                next_cover=cover.step(axis,direction)
                next_signed=signed.step(axis,direction)
                assert next_cover.signed_native_displacement()==next_signed.coords
                assert sum(x*x for x in next_cover.signed_native_displacement())==next_signed.norm_squared_from_origin()
                native_steps+=1
                checks+=2

    # Explicit observer collision: m=1 identifies raw 0 with raw diagonal 1;
    # m=0 keeps both genuinely different native Cells.
    assert CoverState(ORIGIN_COORD,0,1)==CoverState(ORIGIN_COORD,1,1)
    assert CoverState(ORIGIN_COORD,0,0)!=CoverState(ORIGIN_COORD,1,0)
    for m in (1,2,3,7):
        try:
            CoverState(ORIGIN_COORD,0,m).signed_native_displacement()
        except ValueError:
            pass
        else:
            raise AssertionError("finite-m quotient was miscast as native Cell")
        checks+=1
    checks+=2

    print("PASS_X6_CELL_COVER_CLASSIFICATION_V13_V14")
    print("checks=",checks)
    print("tested_moduli=0..8")
    print("m=1=>quotient_cover_coordinate_complete_only; current_P000_signed_native_m=0")
    print("m>1=>cyclic_common_depth_fibre")
    print("m=0=>integer_common_depth_fibre; P000_native_signed_step_crossfile=PASS")
    print("native_m0_states=", native_states, "; native_m0_steps=", native_steps)


if __name__=="__main__":
    main()
