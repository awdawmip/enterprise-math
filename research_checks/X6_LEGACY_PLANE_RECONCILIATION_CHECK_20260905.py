#!/usr/bin/env python3
"""Anti-regression checks for RS-X6-LEGACY-PLANE-RECONCILIATION.

This checker is deliberately standalone (Python stdlib only). It certifies
the centered signed-Z^3 slice semantics against the legacy min-zero observer
artifacts that motivated the reconciliation.
"""

from collections import Counter
from itertools import product
from math import factorial


ONE = (1, 1, 1)


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def sub(a, b):
    return tuple(x - y for x, y in zip(a, b))


def scale(k, a):
    return tuple(k * x for x in a)


def rho(z):
    m = min(z)
    return sub(z, scale(m, ONE))


def mu(z):
    return min(z)


def reconstruct(addr, level):
    return add(addr, scale(level, ONE))


def square_gauge(d):
    return sum(x * x for x in d)


def step_count(d):
    return sum(abs(x) for x in d)


def shortest_path_multiplicity(d):
    counts = [abs(x) for x in d]
    total = sum(counts)
    out = factorial(total)
    for n in counts:
        out //= factorial(n)
    return out


def support_size(d):
    return sum(x != 0 for x in d)


def signed_shell(n):
    r = int(n ** 0.5)
    return [
        z
        for z in product(range(-r, r + 1), repeat=3)
        if square_gauge(z) == n
    ]


def positive_minzero_shell(n):
    r = int(n ** 0.5)
    return [
        z
        for z in product(range(0, r + 1), repeat=3)
        if square_gauge(z) == n and min(z) == 0
    ]


def main():
    # 1. Observer section + common level is globally lossless.
    for z in product(range(-3, 4), repeat=3):
        assert min(rho(z)) == 0
        assert all(x >= 0 for x in rho(z))
        assert reconstruct(rho(z), mu(z)) == z

    # 2. rho alone is intentionally non-injective.
    z1 = (2, -1, 0)
    z2 = (3, 0, 1)
    assert rho(z1) == rho(z2) == (3, 0, 1)
    assert mu(z1) == -1
    assert mu(z2) == 0
    assert z1 != z2

    # 3. Diagonal shifts are invisible to rho but not to native Cell identity.
    z = (-2, 4, 1)
    for k in range(-5, 6):
        shifted = add(z, scale(k, ONE))
        assert rho(shifted) == rho(z)
        assert mu(shifted) == mu(z) + k
        assert reconstruct(rho(shifted), mu(shifted)) == shifted

    # 4. Intrinsic signed quantities are reversal symmetric.
    for p in product(range(-2, 3), repeat=3):
        for q in product(range(-2, 3), repeat=3):
            d = sub(q, p)
            dr = sub(p, q)
            assert dr == tuple(-x for x in d)
            assert square_gauge(d) == square_gauge(dr)
            assert step_count(d) == step_count(dr)
            assert shortest_path_multiplicity(d) == shortest_path_multiplicity(dr)

    # 5. Exact legacy 3-4-5 observer artifact: 25 -> 17 after independent rho.
    d = (3, 4, 0)
    dr = (-3, -4, 0)
    assert rho(d) == (3, 4, 0)
    assert square_gauge(rho(d)) == 25
    assert rho(dr) == (1, 0, 4)
    assert square_gauge(rho(dr)) == 17
    assert square_gauge(d) == square_gauge(dr) == 25
    assert shortest_path_multiplicity(d) == shortest_path_multiplicity(dr) == 35

    # 6. Exact N=25 shell recomputation.
    shell = signed_shell(25)
    support = Counter(support_size(z) for z in shell)
    mass = sum(shortest_path_multiplicity(z) for z in shell)
    assert len(shell) == 30
    assert support == Counter({2: 24, 1: 6})
    assert support.get(3, 0) == 0
    assert mass == 846

    # 7. Historical min-zero positive section survives only as observer census.
    old_shell = positive_minzero_shell(25)
    old_mass = sum(shortest_path_multiplicity(z) for z in old_shell)
    assert len(old_shell) == 9
    assert old_mass == 213

    # 8. BRC multiplicities are positive and sign-stable under reversal.
    for d in shell:
        m = shortest_path_multiplicity(d)
        assert isinstance(m, int) and m > 0
        assert m == shortest_path_multiplicity(tuple(-x for x in d))

    # 9. The centered selected slice has six nearest signed axis neighbors.
    neighbors = {
        (1, 0, 0), (-1, 0, 0),
        (0, 1, 0), (0, -1, 0),
        (0, 0, 1), (0, 0, -1),
    }
    assert len(neighbors) == 6
    assert all(step_count(z) == 1 and square_gauge(z) == 1 for z in neighbors)

    print(
        "PASS RS-X6-LEGACY-PLANE-RECONCILIATION "
        "rho+mu=lossless reversal=intrinsic-symmetric "
        "legacy_25_to_17=observer-artifact "
        "N25_signed=30 support=6+24 BRC_mass=846 "
        "legacy_observer_N25=9 legacy_mass=213"
    )


if __name__ == "__main__":
    main()
