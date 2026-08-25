#!/usr/bin/env python3
"""Exact Tier-A endpoint certificate for the conservative public exhaustive range."""

from math import isqrt

B = 10**20
G = 1724
K_MIN = 1_486_089
K_MAX = 116_009_280_740_973_308
K2_MAX = 13_458_153_218_037_960_469_637_923_168_462_864


def admissible(k: int) -> bool:
    return G * k * k + B * G * G <= 2 * B * k


def main() -> None:
    disc = B * B - B * G**3
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
    assert K_MAX * K_MAX == K2_MAX
    assert 1345 * 10**31 < K2_MAX < 1346 * 10**31

    print("P017 Tier-A exhaustive gap-bootstrap certificate: PASS")
    print("B =", B)
    print("G =", G)
    print("K_min =", K_MIN)
    print("K_max =", K_MAX)
    print("K_max^2 =", K2_MAX)


if __name__ == "__main__":
    main()
