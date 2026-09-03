#!/usr/bin/env python3
"""Exact checker for the BRC critical multiplicity automaton interpretation."""

from __future__ import annotations

from fractions import Fraction
from itertools import product

import brc_critical_degeneracy_log_correction_check as logsel
import brc_critical_degeneracy_matrix_moment_asymptotic_check as crit
import brc_unique_critical_cycle_moment_asymptotic_check as uc

Q = Fraction
Matrix = tuple[tuple[int, ...], ...]


def identity(n: int) -> Matrix:
    return tuple(tuple(1 if i == j else 0 for j in range(n)) for i in range(n))


def matmul(left: Matrix, right: Matrix) -> Matrix:
    n = len(left)
    return tuple(
        tuple(sum(left[i][k] * right[k][j] for k in range(n)) for j in range(n))
        for i in range(n)
    )


def powers(matrix: Matrix, upto: int) -> tuple[Matrix, ...]:
    out = [identity(len(matrix))]
    for _ in range(upto):
        out.append(matmul(out[-1], matrix))
    return tuple(out)


def total_words(matrix: Matrix) -> int:
    return sum(sum(row) for row in matrix)


def trace(matrix: Matrix) -> int:
    return sum(matrix[i][i] for i in range(len(matrix)))


def recurrence_check(poly: tuple[int, ...], sequence: list[int], order: int) -> int:
    # p(z)=1+c1 z+...+cr z^r corresponds to
    # A^r+c1 A^(r-1)+...+cr I=0.
    degree = len(poly) - 1
    checks = 0
    for start in range(order):
        lhs = sequence[start + degree]
        for j in range(1, degree + 1):
            lhs += poly[j] * sequence[start + degree - j]
        assert lhs == 0
        checks += 1
    return checks


def log_derivative_series(poly: tuple[int, ...], upto: int) -> list[Fraction]:
    # s(z)=-z p'(z)/p(z); p_0=1.
    q = [Q(0) for _ in range(upto + 1)]
    for degree in range(1, min(len(poly), upto + 1)):
        q[degree] = -Q(degree * poly[degree])
    series = [Q(0) for _ in range(upto + 1)]
    for n in range(upto + 1):
        value = q[n]
        for k in range(1, min(n, len(poly) - 1) + 1):
            value -= Q(poly[k]) * series[n - k]
        series[n] = value
    return series


def direct_word_enumeration(matrix: Matrix, length: int) -> int:
    n = len(matrix)
    words = [(state,) for state in range(n)]
    for _ in range(length):
        new_words: list[tuple[int, ...]] = []
        for word in words:
            source = word[-1]
            for target in range(n):
                for copy in range(matrix[source][target]):
                    new_words.append((*word, target * 100 + copy))
                    # Encode the chosen parallel copy in the temporary final
                    # symbol, then restore the state for the next transition.
                    new_words[-1] = (*word, target)
        words = new_words
    return len(words)


def direct_word_count_dp(matrix: Matrix, length: int) -> int:
    counts = [1 for _ in range(len(matrix))]
    for _ in range(length):
        next_counts = [0 for _ in counts]
        for source, count in enumerate(counts):
            for target, multiplicity in enumerate(matrix[source]):
                next_counts[target] += count * multiplicity
        counts = next_counts
    return sum(counts)


def validate_matrix(matrix: Matrix) -> tuple[int, int, int]:
    n = len(matrix)
    poly = logsel.criticality_polynomial(matrix)
    degree = len(poly) - 1
    horizon = degree + 7
    pw = powers(matrix, horizon)
    b = [total_words(value) for value in pw]
    tr = [trace(value) for value in pw]

    recurrence = recurrence_check(poly, b, 6) + recurrence_check(poly, tr, 6)

    series = log_derivative_series(poly, 7)
    zeta_checks = 0
    for power in range(1, 8):
        assert series[power] == tr[power]
        zeta_checks += 1

    zero_checks = 0
    is_zero = logsel.zero_correction_structure(matrix)
    if is_zero:
        recurrent_states = sum(any(value for value in row) for row in matrix)
        assert all(b[length] == recurrent_states for length in range(1, horizon + 1))
        selector = logsel.smallest_positive_selector(poly)
        assert selector.exact_root == 1
        zero_checks += horizon + 1
    else:
        selector = logsel.smallest_positive_selector(poly)
        if selector.is_rational:
            assert selector.exact_root is not None and selector.exact_root < 1
        else:
            assert selector.upper < 1
        zero_checks += 1

    return recurrence, zeta_checks, zero_checks


def exhaustive_matrix_regression() -> tuple[int, int, int, int]:
    samples = recurrence_checks = zeta_checks = zero_checks = 0
    for n in (2, 3):
        for values in product((0, 1, 2), repeat=n * n):
            matrix = tuple(tuple(values[n * i + j] for j in range(n)) for i in range(n))
            if not logsel.critical_graph_shaped(matrix):
                continue
            samples += 1
            a, b, c = validate_matrix(matrix)
            recurrence_checks += a
            zeta_checks += b
            zero_checks += c
    return samples, recurrence_checks, zeta_checks, zero_checks


def explicit_word_examples() -> int:
    examples = (
        ((0, 1, 0), (0, 0, 1), (1, 0, 0)),
        ((0, 2, 0), (0, 0, 3), (4, 0, 0)),
        ((1, 1), (1, 1)),
        ((1, 1), (1, 0)),
        ((1, 0), (0, 3)),
    )
    checks = 0
    for matrix in examples:
        pw = powers(matrix, 6)
        for length in range(0, 7):
            assert direct_word_count_dp(matrix, length) == total_words(pw[length])
            checks += 1
    return checks


def gauge_edges(edges: uc.EdgeMap, potentials: tuple[Fraction, ...]) -> uc.EdgeMap:
    return {
        (source, target): tuple(weight * potentials[target] / potentials[source] for weight in weights)
        for (source, target), weights in edges.items()
    }


def gauge_invariance_examples() -> int:
    examples = [
        (
            2,
            uc.normalize_edges(
                2,
                {
                    (0, 0): (Q(1, 2), Q(1, 5)),
                    (0, 1): (Q(1, 2), Q(1, 4)),
                    (1, 0): (Q(1, 2), Q(1, 6)),
                    (1, 1): (Q(1, 2), Q(1, 7)),
                },
            ),
        ),
        (
            3,
            uc.normalize_edges(
                3,
                {
                    (0, 1): (Q(2, 3), Q(2, 3), Q(1, 7)),
                    (1, 2): (Q(3, 5), Q(3, 5), Q(3, 5)),
                    (2, 0): (Q(5, 8),),
                    (0, 2): (Q(1, 9),),
                },
            ),
        ),
    ]
    gauges = (
        (Q(1), Q(2), Q(3)),
        (Q(5, 7), Q(11, 3), Q(13, 5)),
    )
    checks = 0
    for n, edges in examples:
        base = crit.critical_structure(n, edges)
        assert base is not None
        base_critical, _, _, base_k, base_edges = base
        for gauge in gauges:
            potentials = gauge[:n]
            transformed = crit.critical_structure(n, gauge_edges(edges, potentials))
            assert transformed is not None
            transformed_critical, _, _, transformed_k, transformed_edges = transformed
            assert set(transformed_critical) == set(base_critical)
            assert transformed_edges == base_edges
            assert transformed_k == base_k
            checks += 3
    return checks


def special_semantics() -> int:
    checks = 0
    unit = ((0, 1, 0), (0, 0, 1), (1, 0, 0))
    pw = powers(unit, 8)
    assert all(total_words(pw[n]) == 3 for n in range(1, 9))
    checks += 1

    unique = ((0, 2, 0), (0, 0, 3), (4, 0, 0))
    # Every three steps multiply strongest-word count by D=24.
    pw = powers(unique, 9)
    assert total_words(pw[6]) == 24 * total_words(pw[3])
    assert total_words(pw[9]) == 24 * total_words(pw[6])
    checks += 2

    branching = ((1, 1), (1, 1))
    pw = powers(branching, 8)
    assert all(total_words(pw[n]) == 2 ** (n + 1) for n in range(1, 9))
    checks += 1

    golden = ((1, 1), (1, 0))
    pw = powers(golden, 8)
    totals = [total_words(value) for value in pw]
    # Fibonacci-type recurrence follows p_K=1-z-z^2.
    assert all(totals[n] == totals[n - 1] + totals[n - 2] for n in range(2, len(totals)))
    checks += 1
    return checks


def main() -> int:
    samples, recurrence_checks, zeta_checks, zero_checks = exhaustive_matrix_regression()
    word_checks = explicit_word_examples()
    gauge_checks = gauge_invariance_examples()
    special_checks = special_semantics()

    assert samples == 11626
    print("BRC critical multiplicity residual-entropy checker: PASS")
    print(f"critical_graph_matrices={samples}")
    print(f"cayley_hamilton_scalar_checks={recurrence_checks}")
    print(f"critical_zeta_trace_checks={zeta_checks}")
    print(f"zero_structure_checks={zero_checks}")
    print(f"explicit_word_checks={word_checks}")
    print(f"rational_gauge_invariance_checks={gauge_checks}")
    print(f"special_semantics_checks={special_checks}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
