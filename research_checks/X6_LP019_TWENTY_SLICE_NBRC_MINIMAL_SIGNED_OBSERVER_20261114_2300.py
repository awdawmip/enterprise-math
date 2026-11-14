#!/usr/bin/env python3
"""Exact signed-X6/20-slice observer N-BRC fibre certificate. Stdlib only."""
from itertools import combinations
from math import factorial, prod

DIM = 6
D = (1,) * DIM


def shell(n, d=DIM):
    """All ordered signed d-vectors with exact L1 mass n, without duplicates."""
    if d == 0:
        if n == 0:
            yield ()
        return
    for a in range(n + 1):
        for x in ((0,) if a == 0 else (-a, a)):
            for tail in shell(n - a, d - 1):
                yield (x,) + tail


def canonical(z):
    low = min(z)
    return tuple(x - low for x in z)


def full_twenty_slices(z):
    return tuple(canonical(tuple(z[i] for i in S))
                 for S in combinations(range(DIM), 3))


def brc(z):
    n = sum(abs(x) for x in z)
    return factorial(n) // prod(factorial(abs(x)) for x in z)


def check():
    # The relative six-coordinate label is equivalent to the full 20-slice
    # family. Fibre comparison uses that proved reconstruction equivalence.
    group_1_counts = []
    group_2_counts = []
    shell_sizes = []
    for n in range(8):
        fibre_1, fibre_2 = {}, {}
        size = 0
        for z in shell(n):
            size += 1
            rho = canonical(z)
            g = sum(x * x for x in z)
            b = brc(z)
            fibre_1.setdefault(rho, set()).add(b)
            fibre_2.setdefault((rho, g), set()).add(b)
        shell_sizes.append(size)
        group_1_counts.append(sum(len(v) > 1 for v in fibre_1.values()))
        group_2_counts.append(sum(len(v) > 1 for v in fibre_2.values()))
    assert shell_sizes == [1, 12, 72, 292, 912, 2364, 5336, 10836]
    assert group_1_counts == [0, 0, 0, 0, 120, 240, 1100, 2460]
    assert group_2_counts == [0, 0, 0, 0, 0, 0, 0, 360]

    # Minimal obstruction retaining only 20-slice observations and L1.
    a = (-2, -1, -1, 0, 0, 0)
    b = (-1, 0, 0, 1, 1, 1)
    assert full_twenty_slices(a) == full_twenty_slices(b)
    assert b == tuple(x + 1 for x in a)
    assert sum(map(abs, a)) == sum(map(abs, b)) == 4
    assert (brc(a), brc(b)) == (12, 24)

    # Minimal obstruction even retaining full signed-native squared norm.
    c = (-3, -1, -1, 1, 1, 0)
    d = (-2, 0, 0, 2, 2, 1)
    assert full_twenty_slices(c) == full_twenty_slices(d)
    assert d == tuple(x + 1 for x in c)
    assert sum(map(abs, c)) == sum(map(abs, d)) == 7
    assert sum(x*x for x in c) == sum(x*x for x in d) == 13
    assert (brc(c), brc(d)) == (840, 630)

    # Infinite two-chamber family with equal F, L1 and squared norm.
    for t in range(2, 25):
        x = (-t-1, -1, -1, t-1, 1, 0)
        y = (-t, 0, 0, t, 2, 1)
        assert y == tuple(v + 1 for v in x)
        assert full_twenty_slices(x) == full_twenty_slices(y)
        assert sum(map(abs, x)) == sum(map(abs, y)) == 2*t+3
        assert sum(v*v for v in x) == sum(v*v for v in y)
        assert brc(x)*(t+1) == brc(y)*2*t
    print('PASS_X6_LP019_TWENTY_SLICE_NBRC_NONFACTOR')
    print('shell_sizes=', shell_sizes)
    print('F+L1_nonconstant_fibres=', group_1_counts)
    print('F+L1+G_nonconstant_fibres=', group_2_counts)
    print('minimal_L1=4 BRC=12_vs_24; minimal_L1_plus_G=7 BRC=840_vs_630')


if __name__ == '__main__':
    check()
