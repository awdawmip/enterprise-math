#!/usr/bin/env python3
"""Exact checker for primitive critical branch-orbit Euler products."""

from __future__ import annotations

from fractions import Fraction
from itertools import product
from math import comb

from enterprise_math.brc_critical_degeneracy import (
    critical_degeneracy_analysis,
    critical_graph_shaped,
    critical_log_zero,
    criticality_polynomial,
)

Matrix = tuple[tuple[int, ...], ...]
EdgeToken = tuple[int, int, int]


def identity(n: int) -> Matrix:
    return tuple(tuple(1 if i == j else 0 for j in range(n)) for i in range(n))


def matmul(left: Matrix, right: Matrix) -> Matrix:
    n = len(left)
    return tuple(
        tuple(sum(left[i][k] * right[k][j] for k in range(n)) for j in range(n))
        for i in range(n)
    )


def traces(matrix: Matrix, upto: int) -> list[int]:
    current = identity(len(matrix))
    out = [0]
    for _ in range(1, upto + 1):
        current = matmul(current, matrix)
        out.append(sum(current[i][i] for i in range(len(matrix))))
    return out


def divisors(n: int) -> tuple[int, ...]:
    return tuple(d for d in range(1, n + 1) if n % d == 0)


def mobius(n: int) -> int:
    if n == 1:
        return 1
    value = n
    prime_count = 0
    p = 2
    while p * p <= value:
        if value % p == 0:
            value //= p
            prime_count += 1
            if value % p == 0:
                return 0
            while value % p == 0:
                value //= p
        p += 1
    if value > 1:
        prime_count += 1
    return -1 if prime_count % 2 else 1


def primitive_counts(trace_values: list[int]) -> list[int]:
    upto = len(trace_values) - 1
    out = [0]
    for n in range(1, upto + 1):
        numerator = sum(mobius(d) * trace_values[n // d] for d in divisors(n))
        assert numerator % n == 0
        value = numerator // n
        assert value >= 0
        out.append(value)
    return out


def reconstruct_traces(primitive: list[int]) -> list[int]:
    upto = len(primitive) - 1
    out = [0]
    for n in range(1, upto + 1):
        out.append(sum(d * primitive[d] for d in divisors(n)))
    return out


def reciprocal_series(poly: tuple[int, ...], upto: int) -> list[int]:
    assert poly[0] == 1
    out = [0 for _ in range(upto + 1)]
    out[0] = 1
    for n in range(1, upto + 1):
        out[n] = -sum(
            poly[k] * out[n - k]
            for k in range(1, min(n, len(poly) - 1) + 1)
        )
    return out


def multiply_series(left: list[int], right: list[int], upto: int) -> list[int]:
    out = [0 for _ in range(upto + 1)]
    for i, a in enumerate(left):
        if not a:
            continue
        for j, b in enumerate(right):
            if i + j > upto:
                break
            if b:
                out[i + j] += a * b
    return out


def euler_product_series(primitive: list[int], upto: int) -> list[int]:
    series = [0 for _ in range(upto + 1)]
    series[0] = 1
    for length in range(1, upto + 1):
        exponent = primitive[length]
        if exponent == 0:
            continue
        factor = [0 for _ in range(upto + 1)]
        max_power = upto // length
        for copies in range(max_power + 1):
            # (1-x)^(-P) = sum_k binom(P+k-1,k) x^k.
            factor[copies * length] = comb(exponent + copies - 1, copies)
        series = multiply_series(series, factor, upto)
    return series


def expanded_edges(matrix: Matrix) -> tuple[EdgeToken, ...]:
    return tuple(
        (source, target, copy)
        for source, row in enumerate(matrix)
        for target, multiplicity in enumerate(row)
        for copy in range(multiplicity)
    )


def rotations(word: tuple[EdgeToken, ...]) -> tuple[tuple[EdgeToken, ...], ...]:
    return tuple(word[offset:] + word[:offset] for offset in range(len(word)))


def is_primitive_word(word: tuple[EdgeToken, ...]) -> bool:
    n = len(word)
    for period in divisors(n):
        if period == n:
            continue
        if all(word[i] == word[i % period] for i in range(n)):
            return False
    return True


def direct_primitive_orbits(matrix: Matrix, length: int) -> int:
    edges = expanded_edges(matrix)
    outgoing: dict[int, list[EdgeToken]] = {state: [] for state in range(len(matrix))}
    for edge in edges:
        outgoing[edge[0]].append(edge)

    closed_words: set[tuple[EdgeToken, ...]] = set()

    def extend(start: int, state: int, word: tuple[EdgeToken, ...]) -> None:
        if len(word) == length:
            if state == start:
                closed_words.add(word)
            return
        for edge in outgoing[state]:
            extend(start, edge[1], word + (edge,))

    for start in range(len(matrix)):
        extend(start, start, ())

    primitive_orbits: set[tuple[EdgeToken, ...]] = set()
    for word in closed_words:
        if is_primitive_word(word):
            primitive_orbits.add(min(rotations(word)))
    return len(primitive_orbits)


def validate_matrix(matrix: Matrix, upto: int = 8) -> tuple[int, int, int, int]:
    trace_values = traces(matrix, upto)
    primitive = primitive_counts(trace_values)
    assert reconstruct_traces(primitive) == trace_values

    poly = criticality_polynomial(matrix)
    reciprocal = reciprocal_series(poly, upto)
    euler = euler_product_series(primitive, upto)
    assert euler == reciprocal

    integrality_checks = upto
    inversion_checks = upto
    euler_checks = upto + 1
    zero_checks = 0
    if critical_log_zero(matrix):
        # For 2x2/3x3 unit-cycle unions, primitive lengths can only be 1..3.
        assert all(primitive[n] == 0 for n in range(4, upto + 1))
        zero_checks += upto - 3
    return integrality_checks, inversion_checks, euler_checks, zero_checks


def exhaustive_regression() -> tuple[int, int, int, int, int]:
    samples = integral = inversion = euler = zero = 0
    for n in (2, 3):
        for values in product((0, 1, 2), repeat=n * n):
            matrix = tuple(tuple(values[n * i + j] for j in range(n)) for i in range(n))
            if not critical_graph_shaped(matrix):
                continue
            samples += 1
            a, b, c, d = validate_matrix(matrix)
            integral += a
            inversion += b
            euler += c
            zero += d
    return samples, integral, inversion, euler, zero


def direct_orbit_examples() -> int:
    examples = (
        ((1,),),
        ((2,),),
        ((0, 1), (1, 0)),
        ((1, 1), (1, 1)),
        ((1, 1), (1, 0)),
        ((0, 2), (1, 0)),
    )
    checks = 0
    for matrix in examples:
        primitive = primitive_counts(traces(matrix, 6))
        for length in range(1, 7):
            assert direct_primitive_orbits(matrix, length) == primitive[length]
            checks += 1
    return checks


def gauge_branches(branches, potentials):
    return tuple(
        (source, target, Fraction(weight) * potentials[target] / potentials[source])
        for source, target, weight in branches
    )


def gauge_invariance_examples() -> int:
    examples = (
        (
            2,
            (
                (0, 0, Fraction(1, 2)), (0, 0, Fraction(1, 5)),
                (0, 1, Fraction(1, 2)), (0, 1, Fraction(1, 4)),
                (1, 0, Fraction(1, 2)), (1, 0, Fraction(1, 6)),
                (1, 1, Fraction(1, 2)), (1, 1, Fraction(1, 7)),
            ),
        ),
        (
            3,
            (
                (0, 1, Fraction(2, 3)), (0, 1, Fraction(2, 3)), (0, 1, Fraction(1, 7)),
                (1, 2, Fraction(3, 5)), (1, 2, Fraction(3, 5)), (1, 2, Fraction(3, 5)),
                (2, 0, Fraction(5, 8)), (0, 2, Fraction(1, 9)),
            ),
        ),
    )
    gauges = (
        (Fraction(1), Fraction(2), Fraction(3)),
        (Fraction(5, 7), Fraction(11, 3), Fraction(13, 5)),
    )
    checks = 0
    for n, branches in examples:
        base = critical_degeneracy_analysis(n, branches)
        base_p = primitive_counts(traces(base.critical_matrix, 8))
        for gauge in gauges:
            transformed = critical_degeneracy_analysis(n, gauge_branches(branches, gauge[:n]))
            assert transformed.critical_matrix == base.critical_matrix
            assert transformed.critical_edges == base.critical_edges
            assert primitive_counts(traces(transformed.critical_matrix, 8)) == base_p
            checks += 3
    return checks


def special_examples() -> int:
    checks = 0

    # Unit 3-cycle: exactly one primitive orbit of length 3.
    unit3 = ((0, 1, 0), (0, 0, 1), (1, 0, 0))
    p = primitive_counts(traces(unit3, 8))
    assert p[3] == 1 and sum(p[1:]) == 1
    checks += 1

    # One-state binary tie: classical primitive binary necklace prefix.
    binary = ((2,),)
    p = primitive_counts(traces(binary, 6))
    expected = [0, 2, 1, 2, 3, 6, 9]
    assert p == expected
    checks += 1

    # Branching all-ones 2x2 has the same T_n=2^n and same primitive counts.
    branching = ((1, 1), (1, 1))
    assert primitive_counts(traces(branching, 6)) == expected
    checks += 1

    # Golden critical automaton has p_K=1-z-z^2 and an infinite primitive inventory.
    golden = ((1, 1), (1, 0))
    p = primitive_counts(traces(golden, 8))
    assert sum(value > 0 for value in p[1:]) >= 4
    assert criticality_polynomial(golden) == (1, -1, -1)
    checks += 2

    return checks


def main() -> int:
    samples, integral, inversion, euler, zero = exhaustive_regression()
    direct = direct_orbit_examples()
    gauge = gauge_invariance_examples()
    special = special_examples()

    assert samples == 11626
    print("BRC critical primitive-orbit Euler checker: PASS")
    print(f"critical_graph_matrices={samples}")
    print(f"primitive_integrality_checks={integral}")
    print(f"mobius_inversion_checks={inversion}")
    print(f"euler_product_coefficient_checks={euler}")
    print(f"zero_inventory_tail_checks={zero}")
    print(f"direct_orbit_enumeration_checks={direct}")
    print(f"rational_gauge_invariance_checks={gauge}")
    print(f"special_checks={special}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
