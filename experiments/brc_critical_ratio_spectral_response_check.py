#!/usr/bin/env python3
"""Exact checker for the first spectral response of a finite critical ratio jet.

No floating eigensolver is used.  The checker works with integer matrices,
Fraction ratio bases, exact determinant expansions, and the existing algebraic
smallest-positive-root selector.
"""
from __future__ import annotations

from fractions import Fraction
from itertools import permutations, product

import enterprise_math.brc_critical_degeneracy as cd

Q = Fraction
IntMatrix = tuple[tuple[int, ...], ...]
Poly = tuple[Fraction, ...]  # ascending z powers


def trim(poly: Poly) -> Poly:
    values = list(poly)
    while len(values) > 1 and values[-1] == 0:
        values.pop()
    return tuple(values)


def padd(left: Poly, right: Poly) -> Poly:
    n = max(len(left), len(right))
    return trim(tuple(
        (left[i] if i < len(left) else Q(0))
        + (right[i] if i < len(right) else Q(0))
        for i in range(n)
    ))


def pscale(poly: Poly, scalar: Fraction) -> Poly:
    return trim(tuple(scalar * value for value in poly))


def pmul(left: Poly, right: Poly) -> Poly:
    out = [Q(0) for _ in range(len(left) + len(right) - 1)]
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] += a * b
    return trim(tuple(out))


def peval(poly: Poly, value: Fraction) -> Fraction:
    out = Q(0)
    for coefficient in reversed(poly):
        out = out * value + coefficient
    return out


def derivative(poly: Poly) -> Poly:
    if len(poly) <= 1:
        return (Q(0),)
    return trim(tuple(Q(i) * poly[i] for i in range(1, len(poly))))


def sign_of_permutation(perm: tuple[int, ...]) -> int:
    inversions = sum(
        perm[i] > perm[j]
        for i in range(len(perm))
        for j in range(i + 1, len(perm))
    )
    return -1 if inversions % 2 else 1


def irreducible(matrix: IntMatrix) -> bool:
    n = len(matrix)
    reach = [[matrix[i][j] > 0 for j in range(n)] for i in range(n)]
    for i in range(n):
        reach[i][i] = True
    for k in range(n):
        for i in range(n):
            if reach[i][k]:
                for j in range(n):
                    reach[i][j] = reach[i][j] or reach[k][j]
    return all(reach[i][j] for i in range(n) for j in range(n))


def support_edges(matrix: IntMatrix) -> tuple[tuple[int, int], ...]:
    return tuple(
        (i, j)
        for i, row in enumerate(matrix)
        for j, value in enumerate(row)
        if value
    )


def unit_layer(n: int, edge: tuple[int, int]) -> IntMatrix:
    out = [[0 for _ in range(n)] for _ in range(n)]
    out[edge[0]][edge[1]] = 1
    return tuple(tuple(row) for row in out)


def factor_components(
    row: int,
    col: int,
    theta: tuple[Fraction, ...],
    layers: tuple[IntMatrix, ...],
) -> dict[Fraction, Poly]:
    components: dict[Fraction, Poly] = {}
    # theta[0]=1, layers[0]=K.  The diagonal identity term belongs to base 1.
    baseline = (Q(1), Q(-layers[0][row][col])) if row == col else (Q(0), Q(-layers[0][row][col]))
    if baseline != (Q(0),):
        components[Q(1)] = trim(baseline)
    for ratio, layer in zip(theta[1:], layers[1:]):
        if layer[row][col]:
            components[ratio] = (Q(0), Q(-layer[row][col]))
    return components


def determinant_exponential_expansion(
    theta: tuple[Fraction, ...],
    layers: tuple[IntMatrix, ...],
) -> dict[Fraction, Poly]:
    n = len(layers[0])
    total: dict[Fraction, Poly] = {}
    for perm in permutations(range(n)):
        states: dict[Fraction, Poly] = {Q(1): (Q(sign_of_permutation(tuple(perm))),)}
        for row, col in enumerate(perm):
            factors = factor_components(row, col, theta, layers)
            if not factors:
                states = {}
                break
            next_states: dict[Fraction, Poly] = {}
            for base_a, poly_a in states.items():
                for base_b, poly_b in factors.items():
                    base = base_a * base_b
                    poly = pmul(poly_a, poly_b)
                    next_states[base] = padd(next_states.get(base, (Q(0),)), poly)
            states = next_states
        for base, poly in states.items():
            total[base] = padd(total.get(base, (Q(0),)), poly)
    return {base: poly for base, poly in total.items() if poly != (Q(0),)}


def determinant_first_derivative(K: IntMatrix, L: IntMatrix) -> Poly:
    n = len(K)
    total: Poly = (Q(0),)
    for perm in permutations(range(n)):
        sign = Q(sign_of_permutation(tuple(perm)))
        base_factors: list[Poly] = []
        diff_factors: list[Poly] = []
        for row, col in enumerate(perm):
            base = (Q(1), Q(-K[row][col])) if row == col else (Q(0), Q(-K[row][col]))
            diff = (Q(0), Q(-L[row][col]))
            base_factors.append(trim(base))
            diff_factors.append(trim(diff))
        for chosen in range(n):
            if diff_factors[chosen] == (Q(0),):
                continue
            term: Poly = (sign,)
            alive = True
            for index in range(n):
                factor = diff_factors[index] if index == chosen else base_factors[index]
                if factor == (Q(0),):
                    alive = False
                    break
                term = pmul(term, factor)
            if alive:
                total = padd(total, term)
    return total


def as_int_poly(poly: Poly) -> tuple[int, ...]:
    assert all(value.denominator == 1 for value in poly)
    return tuple(value.numerator for value in poly)


def response_sign_certificate(p0: Poly, p1: Poly) -> int:
    selector = cd.smallest_positive_root_selector(as_int_poly(p0), max_width=Q(1, 2**18))
    dp0 = derivative(p0)
    if selector.is_rational:
        assert selector.exact_root is not None
        root = selector.exact_root
        assert peval(p0, root) == 0
        assert peval(p1, root) != 0
        assert peval(dp0, root) != 0
        assert peval(p1, root) * peval(dp0, root) > 0
        return 4

    left, right = selector.lower, selector.upper
    # Use the same exact Sturm primitives as the production selector to prove
    # p1 and p0' have no zeros inside the algebraic-root interval.
    seq1 = cd._sturm_sequence(tuple(p1))  # research-only use of exact internals
    seqd = cd._sturm_sequence(tuple(dp0))
    assert cd._root_count(seq1, left, right) == 0
    assert cd._root_count(seqd, left, right) == 0
    midpoint = (left + right) / 2
    value1 = peval(p1, midpoint)
    valued = peval(dp0, midpoint)
    assert value1 != 0 and valued != 0 and value1 * valued > 0
    return 5


def validate(K: IntMatrix, theta1: Fraction, with_second_layer: bool) -> tuple[int, int, int] | None:
    if not irreducible(K):
        return None
    edges = support_edges(K)
    if not edges:
        return None
    L1 = unit_layer(len(K), edges[0])
    theta = [Q(1), theta1]
    layers = [K, L1]
    if with_second_layer and len(edges) >= 2:
        theta.append(Q(1, 2))
        layers.append(unit_layer(len(K), edges[1]))
    theta_t = tuple(theta)
    layers_t = tuple(layers)

    expansion = determinant_exponential_expansion(theta_t, layers_t)
    p0 = tuple(Q(value) for value in cd.criticality_polynomial(K))
    p1 = determinant_first_derivative(K, L1)
    assert expansion.get(Q(1)) == p0
    assert expansion.get(theta1) == p1
    assert p1 != (Q(0),)

    delta = theta1 * theta1
    if len(theta_t) >= 3:
        delta = max(delta, theta_t[2])
    strict_bases = [base for base in expansion if base not in (Q(1), theta1)]
    assert all(Q(0) < base <= delta < theta1 for base in strict_bases)

    coefficient_checks = len(p0) + len(p1) + len(strict_bases)
    max_degree = max(len(poly) for poly in expansion.values())
    constants = [0 for _ in range(max_degree)]
    for base in strict_bases:
        poly = expansion[base]
        for degree, coefficient in enumerate(poly):
            constants[degree] += abs(coefficient.numerator)
            assert coefficient.denominator == 1

    for m in range(1, 6):
        direct = [Q(0) for _ in range(max_degree)]
        approx = [Q(0) for _ in range(max_degree)]
        for base, poly in expansion.items():
            for degree, coefficient in enumerate(poly):
                direct[degree] += coefficient * (base**m)
        for degree, coefficient in enumerate(p0):
            approx[degree] += coefficient
        for degree, coefficient in enumerate(p1):
            approx[degree] += coefficient * (theta1**m)
        for degree in range(max_degree):
            error = abs(direct[degree] - approx[degree])
            assert error <= Q(constants[degree]) * (delta**m)
            coefficient_checks += 1

    sign_checks = response_sign_certificate(p0, p1)
    return coefficient_checks, sign_checks, len(strict_bases)


def exhaustive_regression() -> tuple[int, int, int, int]:
    samples = coefficient_checks = sign_checks = strict_base_checks = 0
    for n in (2, 3):
        for values in product((0, 1, 2), repeat=n * n):
            K = tuple(tuple(values[n * i + j] for j in range(n)) for i in range(n))
            if not irreducible(K):
                continue
            theta1 = Q(2, 3) if sum(values) % 2 == 0 else Q(3, 4)
            result = validate(K, theta1, with_second_layer=(sum(values) % 3 == 0))
            assert result is not None
            samples += 1
            coefficient_checks += result[0]
            sign_checks += result[1]
            strict_base_checks += result[2]
    return samples, coefficient_checks, sign_checks, strict_base_checks


def char2(matrix: tuple[tuple[Fraction, Fraction], tuple[Fraction, Fraction]], lam: Fraction) -> Fraction:
    return (lam - matrix[0][0]) * (lam - matrix[1][1]) - matrix[0][1] * matrix[1][0]


def closed_form_regressions() -> int:
    checks = 0
    # K=ones(2), L=E00: beta=1/4 and rho=2+epsilon/2+O(epsilon^2).
    K = ((1, 1), (1, 1))
    L = ((1, 0), (0, 0))
    p0 = tuple(Q(value) for value in cd.criticality_polynomial(K))
    p1 = determinant_first_derivative(K, L)
    assert p0 == (Q(1), Q(-2))
    assert p1 == (Q(0), Q(-1), Q(1))
    z = Q(1, 2)
    beta = peval(p1, z) / (z * peval(derivative(p0), z))
    assert beta == Q(1, 4)
    checks += 3
    for m in range(3, 10):
        eps = Q(1, 2) ** m
        matrix = ((Q(1) + eps, Q(1)), (Q(1), Q(1)))
        lower = Q(2) + eps / 2
        upper = lower + eps * eps
        assert char2(matrix, lower) < 0 < char2(matrix, upper)
        checks += 2

    # Irrational base rho=sqrt(6), but beta is exactly 1/4.
    K2 = ((0, 2), (3, 0))
    L2 = ((0, 1), (0, 0))
    p02 = tuple(Q(value) for value in cd.criticality_polynomial(K2))
    p12 = determinant_first_derivative(K2, L2)
    assert p02 == (Q(1), Q(0), Q(-6))
    assert p12 == (Q(0), Q(0), Q(-3))
    # p1/(z p0')=(-3 z^2)/(-12 z^2)=1/4 for every nonzero z.
    assert pscale(p12, Q(4)) == pmul((Q(0), Q(1)), derivative(p02))
    checks += 3

    # Golden-ratio core: beta=z/(1+2z) remains algebraic.
    Kg = ((1, 1), (1, 0))
    Lg = ((0, 1), (0, 0))
    p0g = tuple(Q(value) for value in cd.criticality_polynomial(Kg))
    p1g = determinant_first_derivative(Kg, Lg)
    assert p0g == (Q(1), Q(-1), Q(-1))
    assert p1g == (Q(0), Q(0), Q(-1))
    selector = cd.smallest_positive_root_selector(as_int_poly(p0g))
    assert not selector.is_rational
    # Exact formula is beta=(-z^2)/(z(-1-2z))=z/(1+2z).
    checks += 3
    return checks


def main() -> int:
    samples, coefficient_checks, sign_checks, strict_base_checks = exhaustive_regression()
    special = closed_form_regressions()
    assert samples > 5000
    print("BRC critical ratio-jet spectral response checker: PASS")
    print(f"irreducible_integer_cores={samples}")
    print(f"exact_characteristic_ratio_jet_checks={coefficient_checks}")
    print(f"exact_algebraic_response_sign_checks={sign_checks}")
    print(f"strict_remainder_base_checks={strict_base_checks}")
    print(f"closed_form_checks={special}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
