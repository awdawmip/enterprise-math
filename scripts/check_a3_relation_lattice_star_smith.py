#!/usr/bin/env python3
"""Independent exact-minor regression for the A3 star Smith theorem.

This checker deliberately does not call a Smith-normal-form implementation.
For each tested star coordinate matrix it computes the kth determinantal
divisor as the gcd of all k x k minors, using Bareiss exact determinants, then
recovers the invariant factors from successive determinantal divisors.

The theorem being regression-checked is:

Let g=gcd(m_i), a_i=m_i/g, tau=sum(a_i), and let r=a_c for star center c.

Primitive relation coordinates:
  N=1: (1)
  N=2: (1, tau)
  N>=3: (1, 1, r,...,r, r*tau), with r repeated N-3 times.

Unnormalized relation coordinates:
  N=1: (1)
  N=2: (1, g*tau)
  N>=3: (1, g, g*r,...,g*r, g*r*tau), with g*r repeated N-3 times.
"""

from __future__ import annotations

from functools import reduce
from itertools import combinations, product
from math import gcd


def bareiss_det(matrix: list[list[int]]) -> int:
    n = len(matrix)
    if n == 0:
        return 1
    if any(len(row) != n for row in matrix):
        raise ValueError("matrix must be square")
    a = [row[:] for row in matrix]
    sign = 1
    previous = 1
    for k in range(n - 1):
        if a[k][k] == 0:
            swap = next((i for i in range(k + 1, n) if a[i][k] != 0), None)
            if swap is None:
                return 0
            a[k], a[swap] = a[swap], a[k]
            sign *= -1
        pivot = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                numerator = a[i][j] * pivot - a[i][k] * a[k][j]
                if numerator % previous:
                    raise AssertionError("Bareiss exact division failed")
                a[i][j] = numerator // previous
        previous = pivot
        for i in range(k + 1, n):
            a[i][k] = 0
        for j in range(k + 1, n):
            a[k][j] = 0
    return sign * a[-1][-1]


def determinantal_divisors(matrix: list[list[int]]) -> list[int]:
    n = len(matrix)
    divisors: list[int] = []
    for k in range(1, n + 1):
        divisor = 0
        for rows in combinations(range(n), k):
            for cols in combinations(range(n), k):
                minor = [[matrix[i][j] for j in cols] for i in rows]
                divisor = gcd(divisor, abs(bareiss_det(minor)))
        divisors.append(divisor)
    return divisors


def invariant_factors_from_minors(matrix: list[list[int]]) -> list[int]:
    divisors = determinantal_divisors(matrix)
    factors: list[int] = []
    previous = 1
    for divisor in divisors:
        if divisor == 0:
            factors.append(0)
            continue
        if divisor % previous:
            raise AssertionError("determinantal divisors lost divisibility")
        factors.append(divisor // previous)
        previous = divisor
    return factors


def primitive_data(capacities: tuple[int, ...]) -> tuple[int, tuple[int, ...], int]:
    g = reduce(gcd, capacities)
    primitive = tuple(value // g for value in capacities)
    return g, primitive, sum(primitive)


def star_matrix(
    capacities: tuple[int, ...],
    center: int,
    *,
    primitive: bool,
) -> list[list[int]]:
    n = len(capacities)
    if n == 1:
        return [[1]]
    g, a, _ = primitive_data(capacities)
    values = a if primitive else capacities
    rows = [[1] * n]
    for leaf in range(n):
        if leaf == center:
            continue
        row = [0] * n
        row[center] = values[leaf]
        row[leaf] = -values[center]
        rows.append(row)
    if primitive and g <= 0:
        raise AssertionError("capacity gcd must be positive")
    return rows


def expected_factors(
    capacities: tuple[int, ...],
    center: int,
    *,
    primitive: bool,
) -> list[int]:
    n = len(capacities)
    if n == 1:
        return [1]
    g, a, tau = primitive_data(capacities)
    r = a[center]
    if primitive:
        if n == 2:
            return [1, tau]
        return [1, 1, *([r] * (n - 3)), r * tau]
    if n == 2:
        return [1, g * tau]
    return [1, g, *([g * r] * (n - 3)), g * r * tau]


def run() -> dict[str, int]:
    matrix_cases = 0
    vector_cases = 0
    # Exhaustive capacities 1..6 through N=4, plus 1..4 for N=5.
    # Every center and both primitive/unnormalized coordinate matrices are checked.
    for n, maximum in ((1, 6), (2, 6), (3, 6), (4, 6), (5, 4)):
        for capacities in product(range(1, maximum + 1), repeat=n):
            vector_cases += 1
            for center in range(n):
                for primitive in (False, True):
                    matrix = star_matrix(capacities, center, primitive=primitive)
                    got = invariant_factors_from_minors(matrix)
                    expected = expected_factors(capacities, center, primitive=primitive)
                    matrix_cases += 1
                    if got != expected:
                        raise AssertionError(
                            "Smith regression mismatch: "
                            f"capacities={capacities} center={center} "
                            f"primitive={primitive} got={got} expected={expected}"
                        )
                    determinant = abs(bareiss_det(matrix))
                    factor_product = 1
                    for factor in expected:
                        factor_product *= factor
                    if determinant != factor_product:
                        raise AssertionError(
                            "determinant/index mismatch: "
                            f"capacities={capacities} center={center} "
                            f"primitive={primitive} det={determinant} "
                            f"factor_product={factor_product}"
                        )
    return {
        "capacity_vectors": vector_cases,
        "coordinate_matrices": matrix_cases,
        "failures": 0,
    }


if __name__ == "__main__":
    summary = run()
    print(
        "A3_STAR_SMITH_REGRESSION_PASS "
        f"capacity_vectors={summary['capacity_vectors']} "
        f"coordinate_matrices={summary['coordinate_matrices']} "
        f"failures={summary['failures']}"
    )
