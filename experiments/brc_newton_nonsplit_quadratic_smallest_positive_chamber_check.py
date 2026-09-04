#!/usr/bin/env python3
"""Exact checker for the non-split monic-quadratic smallest-positive chamber."""
from __future__ import annotations

from fractions import Fraction
from itertools import product
from math import isqrt

from enterprise_math import brc_critical_degeneracy as cd
from enterprise_math.brc_newton_schedule_strata import RationalAffineForm

Q = Fraction
Poly = tuple[Fraction, ...]


def quadratic_data(a: Fraction, b: Fraction, root: Fraction):
    if root <= 0:
        raise ValueError("smallest-positive declared root must be positive")
    discriminant = a * a - 4 * b
    left_margin = -a - 2 * root
    root_value = root * root + a * root + b
    return discriminant, left_margin, root_value


def chamber_piecewise(a: Fraction, b: Fraction, root: Fraction) -> bool:
    d, left, value = quadratic_data(a, b, root)
    if value == 0:
        return False
    if d < 0:
        return True
    if b < 0:
        return value < 0
    if b == 0:
        return a >= 0 or value < 0
    return a >= 0 or (left > 0 and value > 0)


def chamber_compact(a: Fraction, b: Fraction, root: Fraction) -> bool:
    d, _, value = quadratic_data(a, b, root)
    if value == 0:
        return False
    return (
        b * value >= 0
        and (
            b < 0
            or value < 0
            or d < 0
            or a >= 0
            or a <= -2 * root
        )
    )


def unsafe_interval_formula(a: Fraction, b: Fraction, root: Fraction) -> bool:
    d, _, value = quadratic_data(a, b, root)
    if value == 0:
        return False  # fixed-multiplicity failure is classified separately
    sign_crossing = b * value < 0
    two_root_or_tangent_crossing = (
        b >= 0
        and value > 0
        and d >= 0
        and -2 * root < a < 0
    )
    return sign_crossing or two_root_or_tangent_crossing


def poly_eval(poly: Poly, value: Fraction) -> Fraction:
    out = Q(0)
    for coefficient in reversed(poly):
        out = out * value + coefficient
    return out


def sturm_smallest_positive_predicate(a: Fraction, b: Fraction, root: Fraction) -> bool:
    """Independent exact oracle: no Q-root in the open interval (0,root)."""
    poly: Poly = (b, a, Q(1))
    if poly_eval(poly, root) == 0:
        return False

    # A root at zero is not positive.  Deflate every y-factor so the Sturm
    # interval has non-root endpoints and counts only roots strictly in (0,r).
    while len(poly) > 1 and poly_eval(poly, Q(0)) == 0:
        poly = cd._p_div_exact(poly, (Q(0), Q(1)))
    if len(poly) <= 1:
        return True

    assert poly_eval(poly, Q(0)) != 0
    assert poly_eval(poly, root) != 0
    sequence = cd._sturm_sequence(poly)
    return cd._root_count(sequence, Q(0), root) == 0


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
    roots = (Q(1, 4), Q(1, 2), Q(1), Q(2), Q(3))
    total = collisions = stable = unstable = sturm_checks = identity_checks = compact_checks = 0
    d_negative = d_zero_stable = d_zero_unstable = d_positive = 0
    b_negative = b_zero = b_positive = zero_endpoint_checks = 0
    irrational_real_competitor_points = 0
    sign_crossing_unsafe = vertex_unsafe = 0

    for a, b, root in product(values, values, roots):
        d, left, rv = quadratic_data(a, b, root)
        assert left * left - d == 4 * rv
        identity_checks += 1
        predicted = chamber_piecewise(a, b, root)
        compact = chamber_compact(a, b, root)
        assert predicted == compact
        compact_checks += 1

        if rv == 0:
            collisions += 1
            assert not predicted
            total += 1
            continue

        sturm = sturm_smallest_positive_predicate(a, b, root)
        assert predicted == sturm
        assert unsafe_interval_formula(a, b, root) == (not sturm)
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

        if b < 0:
            b_negative += 1
        elif b == 0:
            b_zero += 1
            zero_endpoint_checks += 1
        else:
            b_positive += 1

        if not predicted:
            if b * rv < 0:
                sign_crossing_unsafe += 1
            else:
                assert b >= 0 and rv > 0 and d >= 0 and -2 * root < a < 0
                vertex_unsafe += 1
        total += 1

    assert total == len(values) * len(values) * len(roots)
    assert stable + unstable + collisions == total
    assert d_zero_stable > 0 and d_zero_unstable > 0
    assert b_negative > 0 and b_zero > 0 and b_positive > 0
    assert zero_endpoint_checks > 0
    assert irrational_real_competitor_points > 0
    assert sign_crossing_unsafe > 0 and vertex_unsafe > 0
    return (
        total,
        collisions,
        stable,
        unstable,
        sturm_checks,
        identity_checks,
        compact_checks,
        d_negative,
        d_zero_stable,
        d_zero_unstable,
        d_positive,
        b_negative,
        b_zero,
        b_positive,
        zero_endpoint_checks,
        irrational_real_competitor_points,
        sign_crossing_unsafe,
        vertex_unsafe,
    )


def one_parameter_nonsplit_witness():
    root = Q(1)
    b = Q(1)
    grid = tuple(Q(n, 4) for n in range(-16, 17))
    stable = collision = unstable = complex_competitors = irrational_real_stable = checks = 0
    for t in grid:
        d, left, rv = quadratic_data(t, b, root)
        predicted = chamber_piecewise(t, b, root)
        compact = chamber_compact(t, b, root)
        sturm = sturm_smallest_positive_predicate(t, b, root) if rv != 0 else False
        assert predicted == compact == sturm
        assert left == -t - 2
        assert rv == t + 2
        assert d == t * t - 4

        if t == -2:
            assert rv == 0 and not predicted
            collision += 1
        elif t > -2:
            assert predicted
            stable += 1
            if -2 < t < 2:
                assert d < 0
                complex_competitors += 1
            elif t > 2 and rational_square_root(d) is None:
                assert d > 0
                irrational_real_stable += 1
        else:
            assert not predicted
            unstable += 1
        checks += 8

    assert stable == 24
    assert collision == 1
    assert unstable == 8
    assert complex_competitors == 15
    assert irrational_real_stable > 0
    return len(grid), stable, collision, unstable, complex_competitors, irrational_real_stable, checks


def discriminant_zero_boundary_examples():
    root = Q(1)

    # Stable D=0: Q=(y+1)^2, only non-positive competitor.
    a1, b1 = Q(2), Q(1)
    d1, _, v1 = quadratic_data(a1, b1, root)
    assert d1 == 0 and v1 > 0
    assert chamber_piecewise(a1, b1, root)
    assert sturm_smallest_positive_predicate(a1, b1, root)

    # Unstable D=0: Q=(y-1/2)^2 has a positive competitor in (0,1).
    a2, b2 = Q(-1), Q(1, 4)
    d2, _, v2 = quadratic_data(a2, b2, root)
    assert d2 == 0 and v2 > 0
    assert not chamber_piecewise(a2, b2, root)
    assert not sturm_smallest_positive_predicate(a2, b2, root)

    # Collision D=0: Q=(y-1)^2 at declared r=1.
    a3, b3 = Q(-2), Q(1)
    d3, _, v3 = quadratic_data(a3, b3, root)
    assert d3 == 0 and v3 == 0
    assert not chamber_piecewise(a3, b3, root)
    return 12


def zero_endpoint_examples():
    root = Q(1)
    cases = (
        # Q=y(y+1): roots 0,-1; zero is harmless.
        (Q(1), Q(0), True),
        # Q=y(y-2): roots 0,2; positive competitor is beyond r.
        (Q(-2), Q(0), True),
        # Q=y(y-1/2): competitor 1/2 lies inside (0,1).
        (Q(-1, 2), Q(0), False),
        # Q=y^2: only a double zero root, still harmless.
        (Q(0), Q(0), True),
    )
    checks = 0
    for a, b, expected in cases:
        d, _, rv = quadratic_data(a, b, root)
        assert rv != 0
        assert d >= 0
        assert chamber_piecewise(a, b, root) is expected
        assert chamber_compact(a, b, root) is expected
        assert sturm_smallest_positive_predicate(a, b, root) is expected
        checks += 5
    return checks


def affine_parameter_checks():
    # a(u,v)=1+2u-v, b(u,v)=2-u+3v, r=1.
    a = RationalAffineForm((Q(1), Q(2), Q(-1)))
    b = RationalAffineForm((Q(2), Q(-1), Q(3)))
    root = Q(1)
    checks = 0
    for params in product((Q(-2), Q(-1), Q(0), Q(1), Q(2)), repeat=2):
        av = a.evaluate(params)
        bv = b.evaluate(params)
        d, left, rv = quadratic_data(av, bv, root)
        assert left * left - d == 4 * rv
        assert chamber_piecewise(av, bv, root) == chamber_compact(av, bv, root)
        if rv != 0:
            assert chamber_piecewise(av, bv, root) == sturm_smallest_positive_predicate(av, bv, root)
        checks += 3
    return checks


def main() -> int:
    catalog = exhaustive_rational_catalog()
    witness = one_parameter_nonsplit_witness()
    boundary = discriminant_zero_boundary_examples()
    zero = zero_endpoint_examples()
    affine = affine_parameter_checks()
    print("BRC non-split quadratic smallest-positive chamber checker: PASS")
    print(f"quadratic_catalog_points={catalog[0]}")
    print(f"fixed_multiplicity_collision_points={catalog[1]}")
    print(f"smallest_positive_stable_points={catalog[2]}")
    print(f"smallest_positive_unstable_points={catalog[3]}")
    print(f"exact_open_interval_sturm_checks={catalog[4]}")
    print(f"L2_minus_D_equals_4R_checks={catalog[5]}")
    print(f"piecewise_compact_equivalence_checks={catalog[6]}")
    print(f"negative_discriminant_points={catalog[7]}")
    print(f"discriminant_zero_stable_points={catalog[8]}")
    print(f"discriminant_zero_unstable_points={catalog[9]}")
    print(f"positive_discriminant_points={catalog[10]}")
    print(f"b_negative_points={catalog[11]}")
    print(f"b_zero_points={catalog[12]}")
    print(f"b_positive_points={catalog[13]}")
    print(f"zero_endpoint_catalog_checks={catalog[14]}")
    print(f"irrational_real_competitor_points={catalog[15]}")
    print(f"sign_crossing_unsafe_points={catalog[16]}")
    print(f"vertex_crossing_unsafe_points={catalog[17]}")
    print(f"one_parameter_points={witness[0]}")
    print(f"one_parameter_stable={witness[1]}")
    print(f"one_parameter_collision={witness[2]}")
    print(f"one_parameter_unstable={witness[3]}")
    print(f"complex_competitor_points={witness[4]}")
    print(f"irrational_real_stable_points={witness[5]}")
    print(f"one_parameter_formula_checks={witness[6]}")
    print(f"D_zero_boundary_checks={boundary}")
    print(f"zero_root_boundary_checks={zero}")
    print(f"affine_parameter_checks={affine}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
