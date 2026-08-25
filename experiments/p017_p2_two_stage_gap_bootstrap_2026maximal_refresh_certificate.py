#!/usr/bin/env python3
"""Exact endpoint certificate for the May-2026 maximal-gap refresh.

External premise: the confirmed maximal-gap sequence has gap 1724 followed by
confirmed record gap 1854 starting at B. This script only verifies the exact
arithmetic transfer through the two-stage bootstrap theorem.
"""

from math import isqrt

B = 101_412_319_996_363_309_069
G = 1724
K_MIN = 1_486_089
K_MAX = 117_647_703_010_536_312
K2_MAX = 13_840_982_023_655_354_809_893_685_870_561_344


def admissible(k: int) -> bool:
    return G * k * k + B * G * G <= 2 * B * k


def main() -> None:
    disc = B * B - B * G**3
    assert disc > 0
    s = isqrt(disc)

    low_floor = (B - s) // G
    high_floor = (B + s) // G

    assert low_floor == K_MIN - 1
    assert high_floor == K_MAX

    assert not admissible(K_MIN - 1)
    assert admissible(K_MIN)
    assert admissible(K_MAX)
    assert not admissible(K_MAX + 1)
    assert K_MAX < B

    assert K_MIN < 70_500_000_000_000
    assert K_MAX * K_MAX == K2_MAX
    assert K2_MAX > 1384 * 10**31
    assert K2_MAX < 1385 * 10**31

    print("P017 May-2026 maximal-gap refresh certificate: PASS")
    print("B =", B)
    print("G =", G)
    print("K_min =", K_MIN)
    print("K_max =", K_MAX)
    print("K_max^2 =", K2_MAX)
    print("K_max^2 / 1e31 ~=", K2_MAX / 10**31)


if __name__ == "__main__":
    main()
