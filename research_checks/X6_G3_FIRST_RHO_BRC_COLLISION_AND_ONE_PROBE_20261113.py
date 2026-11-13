#!/usr/bin/env python3
"""Exact X6 signed-native small-shell observer/BRC certificate.

Frozen scientific model: P000 V5, native Z^6, free unweighted signed
primitive-axis shortest paths. This is an independent finite checker; it does
not claim to run the original signed_brc.py native benchmark.
"""
from collections import Counter, defaultdict
from itertools import combinations, product
from math import factorial, isqrt

DIM = 6
AXES = range(DIM)


def g(z):
    return sum(a * a for a in z)


def rho(z):
    depth = min(z)
    return tuple(a - depth for a in z)


def brc(z):
    length = sum(abs(a) for a in z)
    numerator = factorial(length)
    for a in z:
        numerator //= factorial(abs(a))
    return numerator


def native_shell(n):
    m = isqrt(n)
    return tuple(z for z in product(range(-m, m + 1), repeat=DIM) if g(z) == n)


def probe(z, axis):
    return g(z) + 2 * z[axis] + 1  # G(z + e_axis)


def decode(r, norm_square, probe_square, axis):
    coordinate, rem = divmod(probe_square - norm_square - 1, 2)
    assert rem == 0
    depth = coordinate - r[axis]
    return tuple(a + depth for a in r)


def main():
    totals = {}
    for n in range(4):
        points = native_shell(n)
        fibers = defaultdict(list)
        for z in points:
            fibers[rho(z)].append(z)
        ambiguities = [f for f in fibers.values() if len(f) > 1]
        same_brc = [f for f in ambiguities if len({brc(z) for z in f}) == 1]
        sizes = dict(sorted(Counter(map(len, fibers.values())).items()))
        totals[n] = (len(points), len(fibers), sizes, len(same_brc))
        assert all(decode(rho(z), n, probe(z, 0), 0) == z for z in points)
        if n < 3:
            assert not ambiguities
        else:
            assert len(points) == 160 and len(fibers) == 140
            assert sizes == {1: 120, 2: 20}
            assert len(same_brc) == 20
            assert all(brc(z) == 6 for z in points)
            assert sum(brc(z) for z in points) == 960
            assert sum(brc(f[0]) for f in fibers.values()) == 840
            for negative_axes in combinations(AXES, 3):
                lower = tuple(-1 if j in negative_axes else 0 for j in AXES)
                upper = tuple(0 if j in negative_axes else 1 for j in AXES)
                assert g(lower) == g(upper) == 3
                assert rho(lower) == rho(upper)
                assert brc(lower) == brc(upper) == 6
                assert probe(lower, 0) != probe(upper, 0)
                assert set(fibers[rho(lower)]) == {lower, upper}
    box = range(-2, 3)
    checked = 0
    for z in product(box, repeat=DIM):
        r, norm = rho(z), g(z)
        assert decode(r, norm, probe(z, 0), 0) == z
        checked += 1
    for z in [(10**40, -10**40, 2, -7, 0, 11), (0,) * DIM]:
        assert decode(rho(z), g(z), probe(z, 5), 5) == z
    print({"status": "PASS_X6_G3_FIRST_RHO_BRC_ALIAS",
           "shell_stats": totals, "first_same_rho_brc_shell": 3,
           "g3_ambiguous_fibers": 20, "g3_native_path_mass": 960,
           "g3_deduplicated_observer_mass": 840,
           "g3_lost_mass": 120, "one_probe_box_checked": checked})


if __name__ == '__main__':
    main()
