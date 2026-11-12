#!/usr/bin/env python3
"""Independent exact check of signed-X6 finite cyclic common-depth cover BRC.

All computations use Python integers and combinatorial coefficients. Run alone.
No result admission, native claim, or actual repository-source import is asserted.
"""
from collections import defaultdict
from itertools import product
from math import factorial
from pathlib import Path
import sys

D = 6
ZERO = (0,) * D
STEPS = []
for i in range(D):
    for e in (-1, 1):
        v = [0] * D
        v[i] = e
        STEPS.append(tuple(v))


def add(a, b):
    return tuple(x+y for x, y in zip(a, b))


def canonical(z):
    h = min(z)
    return tuple(x-h for x in z), h


def cover_key(z, modulus):
    r, h = canonical(z)
    return (r, h if modulus == 0 else h % modulus)


def cover_step(key, direction, modulus):
    r, h = key
    # For finite m, the chosen h is a representative: the quotient is well-defined.
    return cover_key(add(tuple(x+h for x in r), direction), modulus)


def native_brc(n, z):
    a = tuple(max(x, 0) for x in z)
    b = tuple(max(-x, 0) for x in z)
    gap = n - sum(a) - sum(b)
    if gap < 0 or gap % 2:
        return 0
    k_total = gap // 2
    # Positive/negative cancellation pairs distributed over the 6 axes.
    total = 0
    def visit(i, rem, den):
        nonlocal total
        if i == D-1:
            k = rem
            term = den * factorial(a[i]+k) * factorial(b[i]+k)
            total += factorial(n) // term
            return
        for k in range(rem+1):
            visit(i+1, rem-k, den*factorial(a[i]+k)*factorial(b[i]+k))
    visit(0, k_total, 1)
    return total


def fiber_brc(n, key, modulus):
    r, h = key
    # All contributing native endpoints have |z_i| <= n, hence -n <= h' <= n.
    depths = (h,) if modulus == 0 else range(-n, n+1)
    return sum(native_brc(n, tuple(x+t for x in r)) for t in depths
               if modulus == 0 or (t-h) % modulus == 0)


def projected_native(states, modulus):
    out = defaultdict(int)
    for z, weight in states.items():
        out[cover_key(z, modulus)] += weight
    return dict(out)


def main():
    native = {ZERO: 1}
    covers = {m: {cover_key(ZERO, m): 1} for m in (0, 1, 2, 3, 4, 5)}
    cases = 0
    for n in range(7):
        assert sum(native.values()) == 12**n
        for z, v in native.items():
            assert native_brc(n, z) == v, (n, z, v)
        for m, cov in covers.items():
            assert cov == projected_native(native, m), (n, m)
            assert sum(cov.values()) == 12**n
            for key, val in cov.items():
                assert fiber_brc(n, key, m) == val, (n, m, key, val)
                cases += 1
        if n == 6:
            r = ZERO
            assert covers[0][(r, 0)] == 19920
            assert covers[0][(r, +1)] == 720
            assert covers[0][(r, -1)] == 720
            assert covers[1][(r, 0)] == 21360
            assert covers[2][(r, 0)] == 19920
            assert covers[2][(r, 1)] == 1440
            assert covers[3][(r, 0)] == 19920
            assert covers[3][(r, 1)] == 720
            assert covers[3][(r, 2)] == 720
        if n < 6:
            nxt = defaultdict(int)
            for z, count in native.items():
                for step in STEPS:
                    nxt[add(z, step)] += count
            native = dict(nxt)
            for m, cov in tuple(covers.items()):
                nxtc = defaultdict(int)
                for key, count in cov.items():
                    for step in STEPS:
                        nxtc[cover_step(key, step, m)] += count
                covers[m] = dict(nxtc)
    # When executed inside the canonical repository, also check the real
    # existing consumer imports. The isolated independent checker above still
    # runs without a checkout; a missing source layout is reported, not PASS.
    repo_root = Path(__file__).resolve().parents[1]
    coord_dir = repo_root / 'experiments' / 'x6_native_coordinate_completion_v7_20260905'
    signed_dir = repo_root / 'experiments' / 'x6_signed_native_spatial_v16_20260905'
    if (coord_dir / 'x6_cover.py').is_file() and (signed_dir / 'signed_brc.py').is_file():
        sys.path.insert(0, str(coord_dir))
        sys.path.insert(0, str(signed_dir))
        from x6_coordinate import Coord6
        from x6_cover import CoverState
        from signed_brc import endpoint_multiplicity
        imported_cases = 0
        for modulus in (0, 1, 2, 3, 4, 5):
            for z in product(range(-2, 3), repeat=6):
                if sum(abs(i) for i in z) > 3:
                    continue
                r, h = cover_key(z, modulus)
                source_state = CoverState(Coord6(r), h, modulus)
                for e in STEPS:
                    actual = source_state.step(next(i for i,v in enumerate(e) if v),
                                               next(v for v in e if v))
                    expect = cover_step((r,h), e, modulus)
                    assert (actual.coordinate.values, actual.depth) == expect
                    imported_cases += 1
                assert endpoint_multiplicity(sum(abs(x) for x in z), z) == native_brc(sum(abs(x) for x in z),z)
        print('current_source_import PASS', imported_cases)
    else:
        print('current_source_import NOT_RUN_NO_CHECKOUT')
    print('PASS X6_FINITE_CYCLIC_COVER_SIGNED_BRC')
    print('moduli=0,1,2,3,4,5; all n=0..6')
    print('cover_fiber_state_length_cases', cases)
    print('n6_zero_relative:m0_h0,m0_h+1,m0_h-1,m1,m2h0,m2h1,m3h0,m3h1,m3h2',
          19920, 720, 720, 21360, 19920, 1440, 19920, 720, 720)


if __name__ == '__main__':
    main()
