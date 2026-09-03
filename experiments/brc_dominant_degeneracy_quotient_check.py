#!/usr/bin/env python3
"""Exact checks for the BRC dominant-degeneracy leading-pair quotient."""

from __future__ import annotations

from fractions import Fraction as Q
from itertools import product

Histogram = dict[Q, int]
Lead = tuple[Q, int]
Edge = tuple[int, int, Q]


def hist(weights: tuple[Q, ...]) -> Histogram:
    out: Histogram = {}
    for weight in weights:
        out[weight] = out.get(weight, 0) + 1
    return out


def lead(value: Histogram) -> Lead:
    if not value:
        return Q(0), 0
    maximum = max(value)
    return maximum, value[maximum]


def ladd(left: Lead, right: Lead) -> Lead:
    if left[0] > right[0]:
        return left
    if right[0] > left[0]:
        return right
    if left[0] == 0:
        return Q(0), 0
    return left[0], left[1] + right[1]


def lmul(left: Lead, right: Lead) -> Lead:
    if left[0] == 0 or right[0] == 0:
        return Q(0), 0
    return left[0] * right[0], left[1] * right[1]


def hadd(left: Histogram, right: Histogram) -> Histogram:
    out = dict(left)
    for q, count in right.items():
        out[q] = out.get(q, 0) + count
    return out


def hmul(left: Histogram, right: Histogram) -> Histogram:
    out: Histogram = {}
    for q, c in left.items():
        for r, d in right.items():
            out[q * r] = out.get(q * r, 0) + c * d
    return out


def hcount(value: Histogram) -> int:
    return sum(value.values())


def hmass(value: Histogram) -> Q:
    return sum((q * c for q, c in value.items()), Q(0))


def hmoment(value: Histogram, moment: int) -> Q:
    return sum((c * q**moment for q, c in value.items()), Q(0))


def check_leading_semiring() -> int:
    values = [Q(1, 4), Q(1, 2), Q(1), Q(2)]
    families = [()] + [(value,) for value in values] + [pair for pair in product(values, repeat=2)]
    histograms = [hist(tuple(family)) for family in families]
    checks = 0
    for left in histograms:
        for right in histograms:
            assert lead(hadd(left, right)) == ladd(lead(left), lead(right))
            assert lead(hmul(left, right)) == lmul(lead(left), lead(right))
            checks += 2
    return checks


def check_cwm_collision() -> None:
    a = hist((Q(1), Q(1), Q(1, 4), Q(1, 4)))
    b = hist((Q(1), Q(1, 2), Q(1, 2), Q(1, 2)))
    assert (hcount(a), hmass(a), lead(a)[0]) == (4, Q(5, 2), Q(1))
    assert (hcount(b), hmass(b), lead(b)[0]) == (4, Q(5, 2), Q(1))
    assert lead(a) == (Q(1), 2)
    assert lead(b) == (Q(1), 1)


def check_moment_asymptotic_bounds() -> int:
    values = [Q(1, 5), Q(1, 3), Q(1, 2), Q(2, 3), Q(1), Q(3, 2)]
    families = [
        tuple(combo)
        for length in [1, 2, 3, 4]
        for combo in product(values, repeat=length)
    ]
    checks = 0
    for weights in families:
        value = hist(weights)
        maximum, degeneracy = lead(value)
        lower_count = hcount(value) - degeneracy
        subdominant = [q for q in value if q < maximum]
        ratio = max((q / maximum for q in subdominant), default=Q(0))
        for moment in range(13):
            normalized = hmoment(value, moment) / (maximum**moment)
            assert normalized >= degeneracy
            error = normalized - degeneracy
            if subdominant:
                assert error <= lower_count * ratio**moment
            else:
                assert error == 0
                assert hmoment(value, moment) == degeneracy * maximum**moment
            checks += 1
        # Direct exact tail check at a high moment, stronger than monotonic prose.
        normalized_20 = hmoment(value, 20) / (maximum**20)
        if subdominant:
            assert Q(0) <= normalized_20 - degeneracy <= lower_count * ratio**20
        else:
            assert normalized_20 == degeneracy
    return checks


def lzero_matrix(n: int) -> list[list[Lead]]:
    return [[(Q(0), 0) for _ in range(n)] for _ in range(n)]


def lidentity(n: int) -> list[list[Lead]]:
    out = lzero_matrix(n)
    for i in range(n):
        out[i][i] = (Q(1), 1)
    return out


def lmat_mul(left: list[list[Lead]], right: list[list[Lead]]) -> list[list[Lead]]:
    n = len(left)
    out = lzero_matrix(n)
    for i in range(n):
        for j in range(n):
            value = (Q(0), 0)
            for k in range(n):
                value = ladd(value, lmul(left[i][k], right[k][j]))
            out[i][j] = value
    return out


def lmat_pow(matrix: list[list[Lead]], exponent: int) -> list[list[Lead]]:
    result = lidentity(len(matrix))
    base = [row[:] for row in matrix]
    power = exponent
    while power:
        if power & 1:
            result = lmat_mul(result, base)
        base = lmat_mul(base, base)
        power >>= 1
    return result


def leading_edge_matrix(vertex_count: int, edges: list[Edge]) -> list[list[Lead]]:
    matrix = lzero_matrix(vertex_count)
    for source, target, weight in edges:
        matrix[source][target] = ladd(matrix[source][target], (weight, 1))
    return matrix


def explicit_max_paths(vertex_count: int, edges: list[Edge], length: int) -> list[list[Lead]]:
    outgoing: list[list[tuple[int, Q]]] = [[] for _ in range(vertex_count)]
    for source, target, weight in edges:
        outgoing[source].append((target, weight))
    result = lzero_matrix(vertex_count)
    for source in range(vertex_count):
        def walk(state: int, depth: int, weight: Q) -> None:
            if depth == length:
                result[source][state] = ladd(result[source][state], (weight, 1))
                return
            for target, edge_weight in outgoing[state]:
                walk(target, depth + 1, weight * edge_weight)
        walk(source, 0, Q(1))
    return result


def check_path_leading_semiring() -> int:
    edges: list[Edge] = [
        (0, 0, Q(1, 2)),
        (0, 0, Q(1, 3)),
        (0, 1, Q(2, 3)),
        (0, 1, Q(2, 3)),
        (1, 1, Q(1, 2)),
        (1, 2, Q(3, 4)),
        (1, 2, Q(1, 4)),
        (2, 0, Q(1, 5)),
    ]
    matrix = leading_edge_matrix(3, edges)
    checks = 0
    for length in range(7):
        powered = lmat_pow(matrix, length)
        explicit = explicit_max_paths(3, edges, length)
        assert powered == explicit
        checks += 9
    # Parallel equal dominant 0->1 edges must retain tie multiplicity two at length one.
    assert matrix[0][1] == (Q(2, 3), 2)
    return checks


def check_equal_weight_exactness() -> None:
    for count in range(1, 8):
        for weight in [Q(1, 3), Q(2, 5), Q(1), Q(3, 2)]:
            value = hist((weight,) * count)
            assert lead(value) == (weight, count)
            for moment in range(13):
                assert hmoment(value, moment) == count * weight**moment


def main() -> int:
    semiring_checks = check_leading_semiring()
    check_cwm_collision()
    asymptotic_checks = check_moment_asymptotic_bounds()
    path_checks = check_path_leading_semiring()
    check_equal_weight_exactness()
    print("BRC dominant-degeneracy quotient checker: PASS")
    print(f"leading_semiring_checks={semiring_checks}")
    print(f"moment_asymptotic_checks={asymptotic_checks}")
    print(f"path_leading_checks={path_checks}")
    print("cwm_collision_witness=PASS")
    print("equal_weight_exactness=PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
