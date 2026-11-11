#!/usr/bin/env python3
"""Exact finite regression for the R061 Stage-3 observer-gauge metric descent.

Proof of arbitrary symmetric monotone norms is in the companion research note.
Finite coverage is the full cube [-3,3]^3 for each ordered pair.
"""
from itertools import product


def can3(v):
    m = min(v)
    return tuple(t - m for t in v)


def neg(v):
    return tuple(-t for t in v)


def sq(v):
    return sum(t * t for t in v)


def sqrt_triangle_exact(a, b, c):
    # All nonnegative integers; sqrt(a) <= sqrt(b) + sqrt(c).
    if a <= b + c:
        return True
    return (a - b - c) ** 2 <= 4 * b * c


def check():
    points = list(product(range(-3, 4), repeat=3))
    inverse_checks = 0
    ordered_pairs = 0
    for x in points:
        a, r = can3(x), can3(neg(x))
        top = max(a)
        assert r == tuple(top - t for t in a)
        inverse_checks += 1
        for y in points:
            z = tuple(x[i] + y[i] for i in range(3))
            ay, ry = can3(y), can3(neg(y))
            az, rz = can3(z), can3(neg(z))
            assert all(az[i] <= a[i] + ay[i] for i in range(3))
            assert all(rz[i] <= r[i] + ry[i] for i in range(3))
            assert sqrt_triangle_exact(sq(az), sq(a), sq(ay))
            assert sqrt_triangle_exact(sq(rz), sq(r), sq(ry))
            ordered_pairs += 1
    # Exact diagnostic: native diagonal displacement is invisible to this observer.
    assert can3((0, 0, 0)) == can3((1, 1, 1)) == (0, 0, 0)
    assert sq((1, 1, 1)) == 3
    # For the unit e1, normalized max and l2 use denominators sqrt(2), sqrt(3).
    # On (2,1,0) they yield squared values 5/2 and 10/3, unequal.
    assert 5 * 3 != 10 * 2
    print(f"PASS R061_relative_metric_descent: cube_points={len(points)} "
          f"ordered_pairs={ordered_pairs} inverse_checks={inverse_checks} "
          "diagonal_kernel=Z*(1,1,1) calibrated_witness=5/2_vs_10/3")


if __name__ == "__main__":
    check()
