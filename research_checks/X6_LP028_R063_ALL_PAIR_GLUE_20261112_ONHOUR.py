#!/usr/bin/env python3
"""Exact support-at-most-two X6 gluing census from R063 positive component roots.

This checker enumerates only the declared <=2-support subfamily. It does
not rerun the full six-dimensional N=2500 shell benchmark.
"""
from itertools import combinations, product
from math import comb, isqrt
import json


def ordered_positive_roots(r: int) -> list[tuple[int, int]]:
    n = r * r
    return [(a, b) for a in range(r + 1)
            if (b := isqrt(n - a * a)) ** 2 == n - a * a]


def all_pair_endpoints(dimension: int, r: int, signed: bool) -> set[tuple[int, ...]]:
    endpoints = set()
    for i, j in combinations(range(dimension), 2):
        for a, b in ordered_positive_roots(r):
            signs_a = (1, -1) if signed and a else (1,)
            signs_b = (1, -1) if signed and b else (1,)
            for sa, sb in product(signs_a, signs_b):
                x = [0] * dimension
                x[i], x[j] = sa * a, sb * b
                endpoints.add(tuple(x))
    return endpoints


def shortest_word_mass(x: tuple[int, ...]) -> int:
    absolute = [abs(z) for z in x]
    total = sum(absolute)
    result = 1
    used = 0
    for a in absolute:
        result *= comb(used + a, a)
        used += a
    assert used == total
    return result


def closed_forms(dimension: int, r: int, signed: bool) -> tuple[int, int]:
    roots = ordered_positive_roots(r)
    positive_mass = sum(comb(a + b, a) for a, b in roots)
    pairs = comb(dimension, 2)
    if signed:
        return (2 * dimension + 4 * pairs * (len(roots) - 2),
                2 * dimension + 4 * pairs * (positive_mass - 2))
    return (dimension + pairs * (len(roots) - 2),
            dimension + pairs * (positive_mass - 2))


def main() -> None:
    cases = 0
    for dimension in range(2, 7):
        for r in range(1, 129):
            for signed in (False, True):
                points = all_pair_endpoints(dimension, r, signed)
                actual = (len(points), sum(shortest_word_mass(x) for x in points))
                assert actual == closed_forms(dimension, r, signed), (dimension, r, signed)
                assert all(sum(z*z for z in x) == r*r for x in points)
                assert all(sum(z != 0 for z in x) <= 2 for x in points)
                cases += 1

    roots50 = ordered_positive_roots(50)
    assert roots50 == [(0, 50), (14, 48), (30, 40),
                       (40, 30), (48, 14), (50, 0)]
    P50 = sum(comb(a + b, a) for a, b in roots50)
    assert P50 == 110695538274255714208
    pos = closed_forms(6, 50, False)
    signed = closed_forms(6, 50, True)
    assert pos == (66, 1660433074113835713096)
    assert signed == (252, 6641732296455342852372)
    assert comb(6, 2) * 20 - signed[0] == 48
    assert comb(6, 2) * (4*P50 - 4) - signed[1] == 48
    full_endpoint_anchor = 102539052
    full_mass_anchor = int(
        "46263931428930653590904265855801056735441499817749479001025131238806458196360489958119492948372"
    )
    assert full_endpoint_anchor - signed[0] == 102538800
    assert full_mass_anchor - signed[1] == int(
        "46263931428930653590904265855801056735441499817749479001025131238806458189718757661664150096000"
    )
    print(json.dumps({
        "result": "PASS", "exhaustive_cases": cases, "radius_max": 128,
        "dimensions": [2, 3, 4, 5, 6],
        "N2500": {
            "original_positive_pair_roots": len(roots50),
            "positive_union_endpoints": pos[0],
            "positive_union_BRC_mass": str(pos[1]),
            "signed_union_endpoints": signed[0],
            "signed_union_BRC_mass": str(signed[1]),
            "signed_naive_duplicate_endpoints": 48,
            "signed_naive_duplicate_word_mass": 48,
            "full_X6_complement_endpoints": full_endpoint_anchor-signed[0],
            "full_X6_complement_BRC_mass": str(full_mass_anchor-signed[1]),
        },
    }, sort_keys=True))


if __name__ == "__main__":
    main()
