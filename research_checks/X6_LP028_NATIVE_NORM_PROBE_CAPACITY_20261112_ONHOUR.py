#!/usr/bin/env python3
"""Exact R063/LP028 future-operation probes in an embedded signed X6 axis pair.

Both omitted X6 directions and the ambient time channel are outside this
restricted static calculation. All arithmetic is integer-exact.
"""
from math import comb, isqrt


def positive_roots(r):
    roots = set()
    for a in range(r + 1):
        square = r * r - a * a
        b = isqrt(square)
        if b * b == square:
            roots.add((a, b))
    return roots


def signed_endpoints(r):
    endpoints = set()
    for x in range(-r, r + 1):
        square = r * r - x * x
        y = isqrt(square)
        if y * y == square:
            endpoints.update(((x, y), (x, -y)))
    return endpoints


def after_x(x, y):
    return (x + 1) ** 2 + y * y


def after_y(x, y):
    return x * x + (y + 1) ** 2


def check_radius(r):
    positive = positive_roots(r)
    signed = signed_endpoints(r)
    assert {(abs(x), abs(y)) for x, y in signed} == positive
    interior = len(positive) - 2  # axis roots (0,r),(r,0)
    q0 = len(positive)
    q1 = len({after_x(x, y) for x, y in signed})
    q2 = len({(after_x(x, y), after_y(x, y)) for x, y in signed})
    assert (q0, q1, q2) == (interior + 2, 2 * interior + 3, 4 * interior + 4)
    assert len(signed) == q2
    for x, y in signed:
        v1, v2 = after_x(x, y), after_y(x, y)
        assert (v1 - r * r - 1) % 2 == 0
        assert (v2 - r * r - 1) % 2 == 0
        assert ((v1 - r * r - 1) // 2, (v2 - r * r - 1) // 2) == (x, y)
    mass = sum(comb(abs(x) + abs(y), abs(x)) for x, y in signed)
    assert mass == sum((2 if a else 1) * (2 if b else 1) * comb(a + b, a)
                       for a, b in positive)
    return q0, q1, q2, mass


def main():
    for r in range(1, 257):
        check_radius(r)
    assert check_radius(50) == (6, 11, 20, 442782153097022856828)
    assert (after_x(14, 48), after_x(-14, 48)) == (2529, 2473)
    assert (after_y(14, 48), after_y(14, -48)) == (2597, 2405)
    print({"status": "PASS", "exact_radii": 256,
           "r50_capacity_trace": 6, "r50_capacity_one_probe": 11,
           "r50_capacity_two_probes": 20,
           "r50_signed_shortest_brc_mass": 442782153097022856828,
           "r50_probe_values": [2529, 2473, 2597, 2405]})


if __name__ == "__main__":
    main()
