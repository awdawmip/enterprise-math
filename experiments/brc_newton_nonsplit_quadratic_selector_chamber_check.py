#!/usr/bin/env python3
"""Exact checker for the non-split monic-quadratic smallest-real chamber."""
from __future__ import annotations

from fractions import Fraction
from itertools import product
from math import isqrt

from enterprise_math import brc_critical_degeneracy as cd
from enterprise_math.brc_newton_schedule_strata import RationalAffineForm

Q = Fraction
Poly = tuple[Fraction, ...]


def quadratic_data(a: Fraction, b: Fraction, root: Fraction):
    discriminant = a * a - 4 * b
    left_margin = -a - 2 * root
    root_value = root * root + a * root + b
    return discriminant, left_margin, root_value


def chamber_formula(a: Fraction, b: Fraction, root: Fraction) -> bool:
    d, left, value = quadratic_data(a, b, root)
    return value != 0 and (d < 0 or (left > 0 and value > 0))


def poly_eval(poly: Poly, value: Fraction) -> Fraction:
    out = Q(0)
    for coefficient in reversed(poly):
        out = out * value + coefficient
    return out


def sturm_smallest_real_predicate(a: Fraction, b: Fraction, root: Fraction) -> bool:
    poly: Poly = (b, a, Q(1))
    if poly_eval(poly, root) == 0:
        return False  # fixed declared multiplicity failed
    bound = max(abs(root) + 2, Q(2) + max(abs(a), abs(b)))
    while poly_eval(poly, -bound) == 0:
        bound += 1
    sequence = cd._sturm_sequence(poly)
    count = cd._root_count(sequence, -bound, root)
    return count == 0


def rational_square_root(value: Fraction):
    if value < 0:
        return None
    n = isqrt(value.numerator)
    d = isqrt(value.denominator)
    if n * n == value.numerator and d * d == value.denominator:
        return Q(n, d)
    return None


def exhaustive_rational_catalog():
    values = (Q(-3), Q(-2), Q(-1), Q(-1, 2), Q(0), Q(1, 2), Q(1), Q(2), Q(3))
    roots = (Q(-2), Q(-1), Q(0), Q(1), Q(2))
    total = collisions = stable = unstable = sturm_checks = identity_checks = 0
    d_negative = d_zero_stable = d_zero_unstable = d_positive = 0
    irrational_real_competitor_points = 0

    for a, b, root in product(values, values, roots):
        d, left, rv = quadratic_data(a, b, root)
        assert left * left - d == 4 * rv
        identity_checks += 1
        predicted = chamber_formula(a, b, root)
        if rv == 0:
            collisions += 1
            assert not predicted
            total += 1
            continue

        sturm = sturm_smallest_real_predicate(a, b, root)
        assert predicted == sturm
        sturm_checks += 1
        stable += int(predicted)
        unstable += int(not predicted)

        if d < 0:
            d_negative += 1
            assert predicted
        elif d == 0:
            if predicted:
                d_zero_stable += 1
            else:
                d_zero_unstable += 1
        else:
            d_positive += 1
            if rational_square_root(d) is None:
                irrational_real_competitor_points += 1
        total += 1

    assert total == len(values) * len(values) * len(roots)
    assert d_zero_stable > 0 and d_zero_unstable > 0
    assert irrational_real_competitor_points > 0
    assert stable + unstable + collisions == total
    return (
        total,
        collisions,
        stable,
        unstable,
        sturm_checks,
        identity_checks,
        d_negative,
        d_zero_stable,
        d_zero_unstable,
        d_positive,
        irrational_real_competitor_points,
    )


def one_parameter_nonsplit_witness():
    root = Q(-1)
    b = Q(1)
    grid = tuple(Q(n, 4) for n in range(-16, 17))
    stable = collision = unstable = complex_competitors = irrational_real_stable = checks = 0
    for t in grid:
        d, left, rv = quadratic_data(t, b, root)
        predicted = chamber_formula(t, b, root)
        sturm = sturm_smallest_real_predicate(t, b, root) if rv != 0 else False
        assert predicted == sturm
        assert left == Q(2) - t
        assert rv == Q(2) - t
        assert d == t * t - 4

        if t == 2:
            assert rv == 0 and not predicted
            collision += 1
        elif t < 2:
            assert predicted
            stable += 1
            if -2 < t < 2:
                assert d < 0
                complex_competitors += 1
            elif t < -2 and rational_square_root(d) is None:
                assert d > 0
                irrational_real_stable += 1
        else:
            assert not predicted
            unstable += 1
        checks += 7

    assert stable == 24
    assert collision == 1
    assert unstable == 8
    assert complex_competitors == 15
    assert irrational_real_stable > 0
    return len(grid), stable, collision, unstable, complex_competitors, irrational_real_stable, checks


def discriminant_zero_boundary_examples():
    # Stable D=0: Q=(y-1)^2, declared r=-1.
    a1, b1, r = Q(-2), Q(1), Q(-1)
    d1, l1, v1 = quadratic_data(a1, b1, r)
    assert d1 == 0 and l1 > 0 and v1 > 0
    assert chamber_formula(a1, b1, r)
    assert sturm_smallest_real_predicate(a1, b1, r)

    # Unstable D=0 without collision: Q=(y+2)^2, competing root -2<r=-1.
    a2, b2 = Q(4), Q(4)
    d2, l2, v2 = quadratic_data(a2, b2, r)
    assert d2 == 0 and v2 > 0 and l2 < 0
    assert not chamber_formula(a2, b2, r)
    assert not sturm_smallest_real_predicate(a2, b2, r)

    # Collision D=0: Q=(y+1)^2 at r=-1.
    a3, b3 = Q(2), Q(1)
    d3, _, v3 = quadratic_data(a3, b3, r)
    assert d3 == 0 and v3 == 0
    assert not chamber_formula(a3, b3, r)
    return 12


def affine_parameter_identity_checks():
    # a(u,v)=1+2u-v, b(u,v)=2-u+3v, r=-1.
    a = RationalAffineForm((Q(1), Q(2), Q(-1)))
    b = RationalAffineForm((Q(2), Q(-1), Q(3)))
    root = Q(-1)
    checks = 0
    for params in product((Q(-2), Q(-1), Q(0), Q(1), Q(2)), repeat=2):
        av = a.evaluate(params)
        bv = b.evaluate(params)
        d, left, rv = quadratic_data(av, bv, root)
        assert left * left - d == 4 * rv
        if rv != 0:
            assert chamber_formula(av, bv, root) == sturm_smallest_real_predicate(av, bv, root)
        checks += 2
    return checks


def main() -> int:
    catalog = exhaustive_rational_catalog()
    witness = one_parameter_nonsplit_witness()
    boundary = discriminant_zero_boundary_examples()
    affine = affine_parameter_identity_checks()
    print("BRC non-split quadratic selector chamber checker: PASS")
    print(f"quadratic_catalog_points={catalog[0]}")
    print(f"fixed_multiplicity_collision_points={catalog[1]}")
    print(f"smallest_real_stable_points={catalog[2]}")
    print(f"smallest_real_unstable_points={catalog[3]}")
    print(f"exact_sturm_selector_checks={catalog[4]}")
    print(f"L2_minus_D_equals_4R_checks={catalog[5]}")
    print(f"negative_discriminant_points={catalog[6]}")
    print(f"discriminant_zero_stable_points={catalog[7]}")
    print(f"discriminant_zero_unstable_points={catalog[8]}")
    print(f"positive_discriminant_points={catalog[9]}")
    print(f"irrational_real_competitor_points={catalog[10]}")
    print(f"one_parameter_points={witness[0]}")
    print(f"one_parameter_stable={witness[1]}")
    print(f"one_parameter_collision={witness[2]}")
    print(f"one_parameter_unstable={witness[3]}")
    print(f"complex_competitor_points={witness[4]}")
    print(f"irrational_real_stable_points={witness[5]}")
    print(f"one_parameter_formula_checks={witness[6]}")
    print(f"D_zero_boundary_checks={boundary}")
    print(f"affine_parameter_checks={affine}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
