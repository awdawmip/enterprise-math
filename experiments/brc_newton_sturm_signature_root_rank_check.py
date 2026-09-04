#!/usr/bin/env python3
"""Exact checker for arbitrary-degree Sturm-signature selector root rank."""
from __future__ import annotations

from fractions import Fraction
from itertools import combinations

from enterprise_math import brc_critical_degeneracy as cd

Q = Fraction
Poly = tuple[Fraction, ...]


def trim(poly: Poly) -> Poly:
    return cd._trim(poly)


def eval_poly(poly: Poly, x: Fraction) -> Fraction:
    return cd._p_eval(poly, x)


def sign(value: Fraction) -> int:
    return (value > 0) - (value < 0)


def variations(signs) -> int:
    filtered = [s for s in signs if s]
    return sum(filtered[i] != filtered[i - 1] for i in range(1, len(filtered)))


def sturm_signature(poly: Poly, x: Fraction):
    poly = trim(poly)
    if len(poly) <= 1:
        raise ValueError("nonconstant polynomial required")
    if eval_poly(poly, x) == 0:
        raise ValueError("probe must not be a root")
    sequence = cd._sturm_sequence(poly)
    data = []
    minus_signs = []
    probe_signs = []
    for member in sequence:
        member = trim(member)
        degree = len(member) - 1
        lead_sign = sign(member[-1])
        probe_sign = sign(eval_poly(member, x))
        minus_sign = lead_sign * (-1 if degree % 2 else 1)
        data.append((degree, lead_sign, probe_sign))
        minus_signs.append(minus_sign)
        probe_signs.append(probe_sign)
    vminus = variations(minus_signs)
    vx = variations(probe_signs)
    return tuple(data), vminus, vx, vminus - vx


def cauchy_left_bound(poly: Poly, x: Fraction) -> Fraction:
    poly = trim(poly)
    lead = abs(poly[-1])
    coefficient_bound = max((abs(c) / lead for c in poly[:-1]), default=Q(0))
    bound = max(abs(x) + 2, coefficient_bound + 2)
    return -bound


def direct_sturm_rank(poly: Poly, x: Fraction) -> int:
    if eval_poly(poly, x) == 0:
        raise ValueError("probe must not be a root")
    left = cauchy_left_bound(poly, x)
    assert eval_poly(poly, left) != 0
    return cd._root_count(cd._sturm_sequence(poly), left, x)


def linear(root: Fraction):
    return (Q(-root), Q(1)), ("linear", root)


def quadratic(a: Fraction, b: Fraction):
    d = a * a - 4 * b
    if d == 0:
        raise ValueError("factor library avoids repeated quadratic roots")
    return (Q(b), Q(a), Q(1)), ("quadratic", Q(a), Q(b))


def factor_library():
    factors = [linear(Q(r)) for r in (-2, -1, 0, 1, 2)]
    factors.extend(
        [
            quadratic(Q(0), Q(1)),       # x^2+1, no real roots
            quadratic(Q(0), Q(-2)),      # x^2-2, irrational real roots
            quadratic(Q(-1), Q(-1)),     # x^2-x-1
            quadratic(Q(2), Q(2)),       # x^2+2x+2, no real roots
            quadratic(Q(2), Q(-1)),      # x^2+2x-1
        ]
    )
    return tuple(factors)


def factor_rank(meta, x: Fraction) -> int | None:
    if meta[0] == "linear":
        root = meta[1]
        if x == root:
            return None
        return int(root < x)
    _, a, b = meta
    value = x * x + a * x + b
    if value == 0:
        return None
    d = a * a - 4 * b
    if d < 0:
        return 0
    assert d > 0
    if value < 0:
        return 1
    derivative = 2 * x + a
    assert derivative != 0  # at the vertex value would be negative for d>0
    return 0 if derivative < 0 else 2


def factor_zero_right_rank(meta) -> int:
    if meta[0] == "linear":
        return int(meta[1] <= 0)
    rank = factor_rank(meta, Q(0))
    assert rank is not None
    return rank


def multiply_factors(selected):
    poly: Poly = (Q(1),)
    for factor, _ in selected:
        poly = cd._p_mul(poly, factor)
    return trim(poly)


def independent_product_rank(selected, x: Fraction) -> int | None:
    total = 0
    for _, meta in selected:
        item = factor_rank(meta, x)
        if item is None:
            return None
        total += item
    return total


def independent_zero_right_rank(selected) -> int:
    return sum(factor_zero_right_rank(meta) for _, meta in selected)


def sturm_zero_right_rank(poly: Poly) -> int:
    poly = trim(poly)
    had_zero = False
    while len(poly) > 1 and eval_poly(poly, Q(0)) == 0:
        poly = cd._p_div_exact(poly, (Q(0), Q(1)))
        had_zero = True
    if len(poly) <= 1:
        return int(had_zero)
    rank = sturm_signature(poly, Q(0))[3]
    return rank + int(had_zero)


def factorized_degree_six_regression():
    library = factor_library()
    probes = tuple(Q(v) for v in (-3, -2, -1, 0, 1, 2, 3))
    products = signature_checks = independent_checks = zero_checks = positive_checks = 0
    degree_counts = {degree: 0 for degree in range(1, 7)}
    rank_support = set()

    for size in (1, 2, 3):
        for chosen in combinations(library, size):
            poly = multiply_factors(chosen)
            degree = len(poly) - 1
            assert 1 <= degree <= 6
            degree_counts[degree] += 1
            products += 1
            zero_expected = independent_zero_right_rank(chosen)
            zero_actual = sturm_zero_right_rank(poly)
            assert zero_actual == zero_expected
            zero_checks += 1

            for x in probes:
                expected = independent_product_rank(chosen, x)
                if expected is None:
                    continue
                signature, vminus, vx, rank = sturm_signature(poly, x)
                assert rank == expected
                assert rank == direct_sturm_rank(poly, x)
                assert vminus >= vx >= 0
                assert signature
                signature_checks += len(signature) + 3
                independent_checks += 2
                rank_support.add(rank)

            for r in (Q(1, 2), Q(1), Q(3, 2), Q(3)):
                expected_r = independent_product_rank(chosen, r)
                if expected_r is None:
                    continue
                expected_safe = expected_r == zero_expected
                actual_rank = sturm_signature(poly, r)[3]
                actual_safe = actual_rank == zero_actual
                assert actual_safe == expected_safe
                positive_checks += 2

    assert products == 175
    assert degree_counts[6] > 0
    assert max(rank_support) >= 5
    return products, degree_counts, signature_checks, independent_checks, zero_checks, positive_checks, tuple(sorted(rank_support))


def repeated_factor_squarefree_regression():
    probes = tuple(Q(v) for v in (-3, -1, Q(1, 2), 1, 3))
    checks = 0
    for factor, _ in factor_library():
        squared = cd._p_mul(factor, factor)
        cubed = cd._p_mul(squared, factor)
        for x in probes:
            if eval_poly(factor, x) == 0:
                continue
            base_rank = sturm_signature(factor, x)[3]
            assert sturm_signature(squared, x)[3] == base_rank
            assert sturm_signature(cubed, x)[3] == base_rank
            checks += 2
        assert sturm_zero_right_rank(squared) == sturm_zero_right_rank(factor)
        assert sturm_zero_right_rank(cubed) == sturm_zero_right_rank(factor)
        checks += 2
    return checks


def degree_five_witness():
    q_complex = quadratic(Q(0), Q(1))[0]
    q_real = quadratic(Q(-1), Q(-1))[0]
    l_two = linear(Q(2))[0]
    poly = cd._p_mul(cd._p_mul(q_complex, q_real), l_two)
    assert len(poly) - 1 == 5
    assert sturm_signature(poly, Q(1))[3] == 1
    assert sturm_zero_right_rank(poly) == 1
    assert sturm_signature(poly, Q(1))[3] == sturm_zero_right_rank(poly)
    assert sturm_signature(poly, Q(3))[3] == 3
    assert sturm_signature(poly, Q(3))[3] != sturm_zero_right_rank(poly)
    return 6


def signature_scale_invariance():
    checks = 0
    poly = multiply_factors((linear(Q(-1)), quadratic(Q(-1), Q(-1)), quadratic(Q(0), Q(1))))
    for scalar in (Q(1, 3), Q(2), Q(7, 2)):
        scaled = tuple(scalar * c for c in poly)
        for x in (Q(-2), Q(0), Q(1), Q(3)):
            if eval_poly(poly, x) == 0:
                continue
            assert sturm_signature(poly, x)[3] == sturm_signature(scaled, x)[3]
            checks += 1
    return checks


def main() -> int:
    factorized = factorized_degree_six_regression()
    repeated = repeated_factor_squarefree_regression()
    witness = degree_five_witness()
    scale = signature_scale_invariance()
    print("BRC Sturm-signature root-rank checker: PASS")
    print(f"factorized_products={factorized[0]}")
    print(f"degree_counts={factorized[1]}")
    print(f"sturm_signature_checks={factorized[2]}")
    print(f"independent_factor_rank_checks={factorized[3]}")
    print(f"zero_right_rank_checks={factorized[4]}")
    print(f"smallest_positive_readout_checks={factorized[5]}")
    print(f"observed_root_ranks={factorized[6]}")
    print(f"repeated_factor_squarefree_checks={repeated}")
    print(f"degree_five_witness_checks={witness}")
    print(f"positive_scale_invariance_checks={scale}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
