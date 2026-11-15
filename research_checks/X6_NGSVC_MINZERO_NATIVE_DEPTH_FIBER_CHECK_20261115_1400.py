#!/usr/bin/env python3
"""Independent exact check of the old three-positive-axis NGSVC enumerator's
lossless common-depth lift to the frozen P000 V5 signed Z^3 native cube.
This is not R063 Stage0's 17-gate/512-case benchmark.
"""
from collections import defaultdict
from itertools import product
from math import factorial


def can3(z):
    h = min(z)
    return tuple(x-h for x in z)


def shortest_brc(z):
    n = sum(abs(x) for x in z)
    out = factorial(n)
    for x in z:
        out //= factorial(abs(x))
    return out


def old_shell(m):
    return 1 if m == 0 else 6*m


def verify(d):
    assert d >= 0
    native = set(product(range(-d, d+1), repeat=3))
    fibers = defaultdict(set)
    for z in native:
        fibers[can3(z)].add(z)
    t = 2*d
    old_addresses = {r for r in product(range(t+1), repeat=3) if min(r) == 0}
    assert set(fibers) == old_addresses
    assert len(fibers) == 3*t*t+3*t+1
    grade_counts = defaultdict(int)
    for r, targets in fibers.items():
        m = max(r)
        grade_counts[m] += 1
        expected = {tuple(a+h for a in r) for h in range(-d, d-m+1)}
        assert targets == expected, (d, r)
        assert len(targets) == t-m+1
    assert {m:grade_counts[m] for m in range(t+1)} == {m:old_shell(m) for m in range(t+1)}
    assert sum((t-m+1)*old_shell(m) for m in range(t+1)) == (t+1)**3 == len(native)
    return len(native),len(fibers),len(fibers[(0,0,0)])


def main():
    cases = [verify(d) for d in range(13)]
    for t in range(100):
        assert sum((t-m+1)*old_shell(m) for m in range(t+1)) == (t+1)**3
    d=1
    r=(0,1,1)
    native_fiber={tuple(a+h for a in r) for h in range(-d, d-max(r)+1)}
    assert native_fiber == {(-1,0,0),(0,1,1)}
    assert {shortest_brc(z) for z in native_fiber} == {1,2}
    assert {sum(x*x for x in z) for z in native_fiber} == {1,2}
    print('PASS_X6_NGSVC_MINZERO_NATIVE_COMMON_DEPTH_LIFT')
    print('exact_cube_d=0..12',cases)
    print('exact_polynomial_convolution_t=0..99', 'PASS')
    print('signed_native_BRC_fiber_collision',sorted((z,shortest_brc(z)) for z in native_fiber))


if __name__ == '__main__':
    main()
