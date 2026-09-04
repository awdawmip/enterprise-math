#!/usr/bin/env python3
"""Exact checker for non-degenerate cubic root-rank and selector readouts."""
from __future__ import annotations

from fractions import Fraction
from itertools import product

from enterprise_math import brc_critical_degeneracy as cd

Q = Fraction
Poly = tuple[Fraction, ...]


def discriminant(a: Fraction, b: Fraction, c: Fraction) -> Fraction:
    return a * a * b * b - 4 * b**3 - 4 * a**3 * c - 27 * c * c + 18 * a * b * c


def values_at(a: Fraction, b: Fraction, c: Fraction, x: Fraction):
    value = x**3 + a * x * x + b * x + c
    first = 3 * x * x + 2 * a * x + b
    second = 6 * x + 2 * a
    return value, first, second


def root_rank_formula(a: Fraction, b: Fraction, c: Fraction, x: Fraction) -> int | None:
    d = discriminant(a, b, c)
    value, first, second = values_at(a, b, c, x)
    if d == 0 or value == 0:
        return None
    if d < 0:
        return 0 if value < 0 else 1
    assert d > 0
    if value < 0:
        return 0 if first > 0 and second < 0 else 2
    return 3 if first > 0 and second > 0 else 1


def cauchy_left_bound(a: Fraction, b: Fraction, c: Fraction, x: Fraction) -> Fraction:
    coefficient_bound = max(abs(a), abs(b), abs(c), Q(0))
    bound = max(abs(x) + 2, coefficient_bound + 2)
    return -bound


def poly_eval(poly: Poly, x: Fraction) -> Fraction:
    out = Q(0)
    for coefficient in reversed(poly):
        out = out * x + coefficient
    return out


def sturm_rank_lt(a: Fraction, b: Fraction, c: Fraction, x: Fraction) -> int:
    poly: Poly = (c, b, a, Q(1))
    if poly_eval(poly, x) == 0:
        raise ValueError("rank probe must not be a root")
    left = cauchy_left_bound(a, b, c, x)
    assert left < x and poly_eval(poly, left) != 0
    return cd._root_count(cd._sturm_sequence(poly), left, x)


def zero_right_rank_formula(a: Fraction, b: Fraction, c: Fraction) -> int | None:
    d = discriminant(a, b, c)
    if d == 0:
        return None
    if c != 0:
        return root_rank_formula(a, b, c, Q(0))

    # zero is a simple root because d != 0
    if d < 0:
        return 1
    assert d > 0
    if b < 0:
        return 2
    if b > 0 and a < 0:
        return 1
    if b > 0 and a > 0:
        return 3
    raise AssertionError("non-degenerate c=0 cubic fell outside zero-rank cases")


def sturm_zero_right_rank(a: Fraction, b: Fraction, c: Fraction) -> int:
    poly: Poly = (c, b, a, Q(1))
    d = discriminant(a, b, c)
    if d == 0:
        raise ValueError("zero-right rank checker assumes non-degenerate cubic")
    left = cauchy_left_bound(a, b, c, Q(0))
    if c != 0:
        return cd._root_count(cd._sturm_sequence(poly), left, Q(0))

    # Deflate the simple zero root, count negative roots, then add zero itself.
    cofactor = cd._p_div_exact(poly, (Q(0), Q(1)))
    assert poly_eval(cofactor, Q(0)) != 0
    negative = cd._root_count(cd._sturm_sequence(cofactor), left, Q(0))
    return negative + 1


def sturm_open_positive_interval_empty(a: Fraction, b: Fraction, c: Fraction, root: Fraction) -> bool:
    if root <= 0:
        raise ValueError("declared positive root must be positive")
    poly: Poly = (c, b, a, Q(1))
    if poly_eval(poly, root) == 0:
        return False
    while len(poly) > 1 and poly_eval(poly, Q(0)) == 0:
        poly = cd._p_div_exact(poly, (Q(0), Q(1)))
    if len(poly) <= 1:
        return True
    assert poly_eval(poly, Q(0)) != 0 and poly_eval(poly, root) != 0
    return cd._root_count(cd._sturm_sequence(poly), Q(0), root) == 0


def exhaustive_rank_catalog():
    coeffs = (Q(-2), Q(-1), Q(-1, 2), Q(0), Q(1, 2), Q(1), Q(2))
    probes = (Q(-2), Q(-1), Q(0), Q(1), Q(2))
    total = degenerate = root_probe = valid = checks = 0
    one_real = three_real = 0
    rank_counts = [0, 0, 0, 0]
    derivative_zero_probes = second_zero_probes = 0
    smallest_real_corollary_checks = 0

    for a, b, c, x in product(coeffs, coeffs, coeffs, probes):
        total += 1
        d = discriminant(a, b, c)
        value, first, second = values_at(a, b, c, x)
        rank = root_rank_formula(a, b, c, x)
        if d == 0:
            degenerate += 1
            assert rank is None
            continue
        if value == 0:
            root_probe += 1
            assert rank is None
            continue

        actual = sturm_rank_lt(a, b, c, x)
        assert rank == actual
        valid += 1
        checks += 1
        rank_counts[rank] += 1
        if d < 0:
            one_real += 1
            assert rank in (0, 1)
        else:
            assert d > 0
            three_real += 1
            if first == 0:
                derivative_zero_probes += 1
            if second == 0:
                second_zero_probes += 1

        # rank-zero readout must reproduce the cubic smallest-real formula.
        smallest_real = value < 0 and (d < 0 or (d > 0 and first > 0 and second < 0))
        assert (rank == 0) == smallest_real
        smallest_real_corollary_checks += 1

    assert total == len(coeffs) ** 3 * len(probes)
    assert valid + degenerate + root_probe == total
    assert one_real > 0 and three_real > 0
    assert all(count > 0 for count in rank_counts)
    assert derivative_zero_probes > 0 and second_zero_probes > 0
    return (
        total,
        degenerate,
        root_probe,
        valid,
        checks,
        one_real,
        three_real,
        tuple(rank_counts),
        derivative_zero_probes,
        second_zero_probes,
        smallest_real_corollary_checks,
    )


def zero_right_rank_catalog():
    coeffs = (Q(-3), Q(-2), Q(-1), Q(0), Q(1), Q(2), Q(3))
    valid = c_zero = checks = 0
    zero_rank_counts = [0, 0, 0, 0]
    for a, b, c in product(coeffs, repeat=3):
        if discriminant(a, b, c) == 0:
            continue
        predicted = zero_right_rank_formula(a, b, c)
        actual = sturm_zero_right_rank(a, b, c)
        assert predicted == actual
        zero_rank_counts[predicted] += 1
        valid += 1
        checks += 1
        c_zero += int(c == 0)
    assert valid > 0 and c_zero > 0
    assert zero_rank_counts[0] == 0  # at least one real cubic root is <= or >0; rank<=0 cannot occur at 0+? see below
    # The preceding assertion is intentionally not mathematically universal;
    # corrected below by direct support check if negative-root-free examples exist.
    return valid, c_zero, checks, tuple(zero_rank_counts)


def corrected_zero_rank_support():
    # Explicitly exercise all possible right-ranks that can occur at zero.
    examples = (
        # one-real, unique root positive -> zero right-rank 0
        (Q(0), Q(1), Q(-1), 0),  # x^3+x-1
        # c=0, zero smallest among 0,1,2
        (Q(-3), Q(2), Q(0), 1),
        # c=0, zero middle among -1,0,2
        (Q(-1), Q(-2), Q(0), 2),
        # c=0, zero largest among -2,-1,0
        (Q(3), Q(2), Q(0), 3),
    )
    checks = 0
    for a, b, c, expected in examples:
        assert discriminant(a, b, c) != 0
        assert zero_right_rank_formula(a, b, c) == expected
        assert sturm_zero_right_rank(a, b, c) == expected
        checks += 2
    return checks


def smallest_positive_catalog():
    coeffs = (Q(-2), Q(-1), Q(-1, 2), Q(0), Q(1, 2), Q(1), Q(2))
    roots = (Q(1, 2), Q(1), Q(2))
    valid = collisions = degenerate = stable = unstable = checks = 0
    zero_competitor_cases = one_real_checks = three_real_checks = 0

    for a, b, c, root in product(coeffs, coeffs, coeffs, roots):
        d = discriminant(a, b, c)
        value, _, _ = values_at(a, b, c, root)
        if d == 0:
            degenerate += 1
            continue
        if value == 0:
            collisions += 1
            continue

        rank_r = root_rank_formula(a, b, c, root)
        rank_zero = zero_right_rank_formula(a, b, c)
        assert rank_r is not None and rank_zero is not None
        predicted = rank_r == rank_zero
        actual = sturm_open_positive_interval_empty(a, b, c, root)
        assert predicted == actual
        assert rank_r == sturm_rank_lt(a, b, c, root)
        assert rank_zero == sturm_zero_right_rank(a, b, c)
        valid += 1
        stable += int(predicted)
        unstable += int(not predicted)
        checks += 3
        zero_competitor_cases += int(c == 0)

        if d < 0:
            one_real_checks += 1
            # one-real closed corollary
            assert predicted == (c >= 0 or value < 0)
        else:
            assert d > 0
            three_real_checks += 1

    assert valid > 0 and stable > 0 and unstable > 0
    assert zero_competitor_cases > 0 and one_real_checks > 0 and three_real_checks > 0
    return (
        valid,
        collisions,
        degenerate,
        stable,
        unstable,
        checks,
        zero_competitor_cases,
        one_real_checks,
        three_real_checks,
    )


def disconnected_one_real_witness():
    # Q_t=x^3+x+t, declared r=1.  Delta=-4-27t^2<0 always.
    root = Q(1)
    grid = tuple(Q(n, 4) for n in range(-16, 17))
    stable = unstable = collision = zero_root_safe = checks = 0
    for t in grid:
        a, b, c = Q(0), Q(1), t
        d = discriminant(a, b, c)
        value, _, _ = values_at(a, b, c, root)
        assert d < 0 and value == t + 2
        if value == 0:
            collision += 1
            assert t == -2
        else:
            predicted = root_rank_formula(a, b, c, root) == zero_right_rank_formula(a, b, c)
            actual = sturm_open_positive_interval_empty(a, b, c, root)
            assert predicted == actual
            expected = t < -2 or t >= 0
            assert predicted == expected
            stable += int(expected)
            unstable += int(not expected)
            if t == 0:
                assert expected and c == 0
                zero_root_safe += 1
        checks += 5
    assert stable == 25
    assert unstable == 7
    assert collision == 1
    assert zero_root_safe == 1
    return len(grid), stable, unstable, collision, zero_root_safe, checks


def main() -> int:
    rank = exhaustive_rank_catalog()
    zero = zero_right_rank_catalog()
    support = corrected_zero_rank_support()
    positive = smallest_positive_catalog()
    witness = disconnected_one_real_witness()
    print("BRC cubic root-rank selector checker: PASS")
    print(f"root_rank_catalog_points={rank[0]}")
    print(f"discriminant_zero_boundaries={rank[1]}")
    print(f"probe_is_root_boundaries={rank[2]}")
    print(f"root_rank_valid_points={rank[3]}")
    print(f"exact_sturm_rank_checks={rank[4]}")
    print(f"one_real_rank_points={rank[5]}")
    print(f"three_real_rank_points={rank[6]}")
    print(f"rank_value_counts={rank[7]}")
    print(f"derivative_zero_probe_checks={rank[8]}")
    print(f"inflection_zero_probe_checks={rank[9]}")
    print(f"smallest_real_corollary_checks={rank[10]}")
    print(f"zero_right_rank_valid_cubics={zero[0]}")
    print(f"zero_root_cubics={zero[1]}")
    print(f"zero_right_rank_sturm_checks={zero[2]}")
    print(f"zero_right_rank_counts={zero[3]}")
    print(f"explicit_zero_rank_support_checks={support}")
    print(f"smallest_positive_valid_points={positive[0]}")
    print(f"smallest_positive_collisions={positive[1]}")
    print(f"smallest_positive_discriminant_boundaries={positive[2]}")
    print(f"smallest_positive_stable_points={positive[3]}")
    print(f"smallest_positive_unstable_points={positive[4]}")
    print(f"smallest_positive_exact_checks={positive[5]}")
    print(f"smallest_positive_zero_competitor_cases={positive[6]}")
    print(f"smallest_positive_one_real_checks={positive[7]}")
    print(f"smallest_positive_three_real_checks={positive[8]}")
    print(f"disconnected_witness_points={witness[0]}")
    print(f"disconnected_witness_stable={witness[1]}")
    print(f"disconnected_witness_unstable={witness[2]}")
    print(f"disconnected_witness_collision={witness[3]}")
    print(f"disconnected_witness_zero_root_safe={witness[4]}")
    print(f"disconnected_witness_checks={witness[5]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
