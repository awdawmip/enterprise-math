#!/usr/bin/env python3
"""Exact regression for common-depth Cell covers."""
from itertools import product

from x6_coordinate import Coord6, ORIGIN_COORD
from x6_cover import CoverState, depth_carry, diagonal_loop, first_positive_diagonal_return


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

    # m=1 is exactly coordinate-complete: depth never changes Cell identity.
    for a in coords:
        for d in range(-20,21):
            assert CoverState(a,d,1)==CoverState(a,0,1)
            checks+=1

    print("PASS_X6_CELL_COVER_CLASSIFICATION_V13_V14")
    print("checks=",checks)
    print("tested_moduli=0..8")
    print("m=1=>coordinate_complete")
    print("m>1=>cyclic_common_depth_fibre")
    print("m=0=>integer_common_depth_fibre")


if __name__=="__main__":
    main()
