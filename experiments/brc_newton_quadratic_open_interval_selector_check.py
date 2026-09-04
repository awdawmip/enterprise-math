#!/usr/bin/env python3
"""Exact checker for non-split quadratic open-interval selector chambers.

The checker validates the closed four-chamber criterion against the existing
exact rational Sturm implementation.  No quadratic root or floating square
root is materialized.
"""
from __future__ import annotations

from fractions import Fraction
from itertools import combinations, product

from enterprise_math import brc_critical_degeneracy as cd

Q = Fraction
Poly = tuple[Fraction, ...]


def poly_eval(poly: Poly, value: Fraction) -> Fraction:
    out = Q(0)
    for coefficient in reversed(poly):
        out = out * value + coefficient
    return out


def quadratic_interval_data(
    a: Fraction,
    b: Fraction,
    left: Fraction,
    right: Fraction,
) -> tuple[Fraction, Fraction, Fraction, Fraction, Fraction]:
    """Return D, Q(left), Q(right), Q'(left), Q'(right)."""
    if not left < right:
        raise ValueError("left must be smaller than right")
    discriminant = a * a - 4 * b
    left_value = left * left + a * left + b
    right_value = right * right + a * right + b
    left_slope = 2 * left + a
    right_slope = 2 * right + a
    return discriminant, left_value, right_value, left_slope, right_slope


def chamber_flags(
    a: Fraction,
    b: Fraction,
    left: Fraction,
    right: Fraction,
) -> tuple[bool, bool, bool, bool]:
    """The four mutually exclusive root-free placement chambers."""
    discriminant, lv, rv, ls, rs = quadratic_interval_data(a, b, left, right)
    complex_pair = discriminant < 0
    both_left = discriminant >= 0 and ls >= 0 and lv >= 0
    both_right = discriminant >= 0 and rs <= 0 and rv >= 0
    straddling = lv <= 0 and rv <= 0
    return complex_pair, both_left, both_right, straddling


def quadratic_open_interval_root_free(
    a: Fraction,
    b: Fraction,
    left: Fraction,
    right: Fraction,
) -> bool:
    flags = chamber_flags(a, b, left, right)
    if sum(flags) > 1:
        raise AssertionError("quadratic root-placement chambers overlapped")
    return any(flags)


def exact_open_root_count(
    a: Fraction,
    b: Fraction,
    left: Fraction,
    right: Fraction,
) -> int:
    """Count distinct roots in (left,right), handling endpoint roots explicitly."""
    poly: Poly = (b, a, Q(1))
    left_value = poly_eval(poly, left)
    right_value = poly_eval(poly, right)

    # If an endpoint itself is a root, Vieta gives the other root exactly.
    # This avoids relying on a library convention for Sturm endpoint counts.
    if left_value == 0:
        other = -a - left
        return int(left < other < right)
    if right_value == 0:
        other = -a - right
        return int(left < other < right)

    sequence = cd._sturm_sequence(poly)
    return cd._root_count(sequence, left, right)


def general_interval_catalog() -> tuple[int, ...]:
    values = (
        Q(-3),
        Q(-2),
        Q(-1),
        Q(-1, 2),
        Q(0),
        Q(1, 2),
        Q(1),
        Q(2),
        Q(3),
    )
    endpoints = (Q(-2), Q(-1), Q(0), Q(1), Q(2), Q(3))

    total = stable = unstable = 0
    complex_count = left_count = right_count = straddle_count = 0
    zero_root = one_root = two_root = 0
    endpoint_root_cases = identity_checks = 0

    for a, b in product(values, repeat=2):
        for left, right in combinations(endpoints, 2):
            discriminant, lv, rv, ls, rs = quadratic_interval_data(a, b, left, right)
            flags = chamber_flags(a, b, left, right)
            assert sum(flags) <= 1

            predicted = any(flags)
            root_count = exact_open_root_count(a, b, left, right)
            assert root_count in (0, 1, 2)
            assert predicted == (root_count == 0)

            # Endpoint/Vieta identities behind the four placement chambers.
            # If alpha,beta are roots then their shifts from x have sum -Q'(x)
            # and product Q(x); these two exact symmetric data determine whether
            # both shifted roots have the same non-positive/non-negative sign.
            assert ls == 2 * left + a
            assert rs == 2 * right + a
            assert discriminant == ls * ls - 4 * lv
            assert discriminant == rs * rs - 4 * rv
            identity_checks += 4

            total += 1
            stable += int(predicted)
            unstable += int(not predicted)
            complex_count += int(flags[0])
            left_count += int(flags[1])
            right_count += int(flags[2])
            straddle_count += int(flags[3])
            zero_root += int(root_count == 0)
            one_root += int(root_count == 1)
            two_root += int(root_count == 2)
            endpoint_root_cases += int(lv == 0 or rv == 0)

    assert total == 1215
    assert stable == zero_root == 736
    assert unstable == one_root + two_root == 479
    assert (complex_count, left_count, right_count, straddle_count) == (390, 139, 55, 152)
    assert (one_root, two_root) == (386, 93)
    assert endpoint_root_cases == 154
    return (
        total,
        stable,
        unstable,
        complex_count,
        left_count,
        right_count,
        straddle_count,
        one_root,
        two_root,
        endpoint_root_cases,
        identity_checks,
    )


def smallest_positive_formula(a: Fraction, b: Fraction, root: Fraction) -> bool:
    """Whether declared positive root is smallest positive, with fixed multiplicity."""
    if root <= 0:
        raise ValueError("declared root must be positive")
    discriminant = a * a - 4 * b
    value_at_root = root * root + a * root + b
    if value_at_root == 0:
        return False
    right_margin = -a - 2 * root
    return (
        discriminant < 0
        or (discriminant >= 0 and a >= 0 and b >= 0)
        or (discriminant >= 0 and right_margin >= 0 and value_at_root > 0)
        or (b <= 0 and value_at_root < 0)
    )


def smallest_positive_catalog() -> tuple[int, ...]:
    values = (
        Q(-3),
        Q(-2),
        Q(-1),
        Q(-1, 2),
        Q(0),
        Q(1, 2),
        Q(1),
        Q(2),
        Q(3),
    )
    roots = (Q(1, 2), Q(1), Q(2), Q(3))

    total = collisions = stable = unstable = 0
    complex_count = nonpositive_count = right_count = straddle_count = 0
    one_root = two_root = 0

    for a, b, root in product(values, values, roots):
        value_at_root = root * root + a * root + b
        total += 1
        if value_at_root == 0:
            collisions += 1
            assert not smallest_positive_formula(a, b, root)
            continue

        predicted = smallest_positive_formula(a, b, root)
        interval_predicted = quadratic_open_interval_root_free(a, b, Q(0), root)
        root_count = exact_open_root_count(a, b, Q(0), root)
        assert predicted == interval_predicted == (root_count == 0)

        flags = chamber_flags(a, b, Q(0), root)
        stable += int(predicted)
        unstable += int(not predicted)
        complex_count += int(flags[0])
        nonpositive_count += int(flags[1])
        right_count += int(flags[2])
        straddle_count += int(flags[3])
        one_root += int(root_count == 1)
        two_root += int(root_count == 2)

    assert total == 324
    assert collisions == 15
    assert stable == 215 and unstable == 94
    assert (complex_count, nonpositive_count, right_count, straddle_count) == (104, 40, 2, 69)
    assert (one_root, two_root) == (89, 5)
    return (
        total,
        collisions,
        stable,
        unstable,
        complex_count,
        nonpositive_count,
        right_count,
        straddle_count,
        one_root,
        two_root,
    )


def disconnected_parameter_witness() -> tuple[int, ...]:
    """Q_t(y)=y^2-3y+t on (0,1): stable iff t<=0 or t>2."""
    root = Q(1)
    grid = tuple(Q(index, 8) for index in range(-32, 33))
    straddle = unstable = collision = both_right = complex_pair = checks = 0

    for parameter in grid:
        a = Q(-3)
        b = parameter
        discriminant, left_value, right_value, left_slope, right_slope = quadratic_interval_data(
            a, b, Q(0), root
        )
        predicted = smallest_positive_formula(a, b, root)
        count = exact_open_root_count(a, b, Q(0), root)

        assert discriminant == 9 - 4 * parameter
        assert left_value == parameter
        assert right_value == parameter - 2
        assert left_slope == -3
        assert right_slope == -1

        if parameter == 2:
            assert right_value == 0 and not predicted
            collision += 1
        elif parameter <= 0:
            assert predicted and count == 0
            assert chamber_flags(a, b, Q(0), root)[3]
            straddle += 1
        elif parameter < 2:
            assert not predicted and count >= 1
            unstable += 1
        elif parameter <= Q(9, 4):
            assert predicted and count == 0 and discriminant >= 0
            assert chamber_flags(a, b, Q(0), root)[2]
            both_right += 1
        else:
            assert predicted and count == 0 and discriminant < 0
            assert chamber_flags(a, b, Q(0), root)[0]
            complex_pair += 1
        checks += 9

    assert (straddle, unstable, collision, both_right, complex_pair) == (33, 15, 1, 2, 14)
    return len(grid), straddle, unstable, collision, both_right, complex_pair, checks


def positive_endpoint_signs_are_not_enough() -> int:
    # Q(y)=y^2-y+1/8 has two roots strictly inside (0,1), while both endpoint
    # values are positive.  The derivative/vertex conditions correctly reject it.
    a, b, left, right = Q(-1), Q(1, 8), Q(0), Q(1)
    discriminant, lv, rv, ls, rs = quadratic_interval_data(a, b, left, right)
    assert discriminant == Q(1, 2) > 0
    assert lv == rv == Q(1, 8) > 0
    assert ls < 0 < rs
    assert not quadratic_open_interval_root_free(a, b, left, right)
    assert exact_open_root_count(a, b, left, right) == 2
    return 7


def main() -> int:
    general = general_interval_catalog()
    positive = smallest_positive_catalog()
    witness = disconnected_parameter_witness()
    endpoint_warning = positive_endpoint_signs_are_not_enough()

    print("BRC quadratic open-interval selector checker: PASS")
    print(f"general_interval_catalog_points={general[0]}")
    print(f"general_root_free_points={general[1]}")
    print(f"general_unstable_points={general[2]}")
    print(f"complex_pair_chamber_points={general[3]}")
    print(f"both_roots_left_chamber_points={general[4]}")
    print(f"both_roots_right_chamber_points={general[5]}")
    print(f"straddling_chamber_points={general[6]}")
    print(f"one_open_interval_root_points={general[7]}")
    print(f"two_open_interval_root_points={general[8]}")
    print(f"endpoint_root_cases={general[9]}")
    print(f"quadratic_shift_identity_checks={general[10]}")
    print(f"smallest_positive_catalog_points={positive[0]}")
    print(f"smallest_positive_collision_points={positive[1]}")
    print(f"smallest_positive_stable_points={positive[2]}")
    print(f"smallest_positive_unstable_points={positive[3]}")
    print(f"smallest_positive_complex_points={positive[4]}")
    print(f"smallest_positive_nonpositive_root_points={positive[5]}")
    print(f"smallest_positive_both_right_points={positive[6]}")
    print(f"smallest_positive_straddling_points={positive[7]}")
    print(f"smallest_positive_one_competitor_points={positive[8]}")
    print(f"smallest_positive_two_competitor_points={positive[9]}")
    print(f"disconnected_witness_grid_points={witness[0]}")
    print(f"disconnected_witness_straddle_stable={witness[1]}")
    print(f"disconnected_witness_unstable={witness[2]}")
    print(f"disconnected_witness_collision={witness[3]}")
    print(f"disconnected_witness_both_right_stable={witness[4]}")
    print(f"disconnected_witness_complex_stable={witness[5]}")
    print(f"disconnected_witness_formula_checks={witness[6]}")
    print(f"positive_endpoint_sign_warning_checks={endpoint_warning}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
