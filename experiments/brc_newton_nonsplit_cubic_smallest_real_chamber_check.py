#!/usr/bin/env python3
"""Exact checker for the non-degenerate monic-cubic smallest-real chamber."""
from __future__ import annotations

from fractions import Fraction
from itertools import product

from enterprise_math import brc_critical_degeneracy as cd
from enterprise_math.brc_newton_schedule_strata import RationalAffineForm

Q = Fraction
Poly = tuple[Fraction, ...]


def cubic_discriminant(a: Fraction, b: Fraction, c: Fraction) -> Fraction:
    return a * a * b * b - 4 * b * b * b - 4 * a * a * a * c - 27 * c * c + 18 * a * b * c


def cubic_data(a: Fraction, b: Fraction, c: Fraction, root: Fraction):
    value = root**3 + a * root * root + b * root + c
    first = 3 * root * root + 2 * a * root + b
    second = 6 * root + 2 * a
    disc = cubic_discriminant(a, b, c)
    return disc, value, first, second


def chamber_formula(a: Fraction, b: Fraction, c: Fraction, root: Fraction) -> bool | None:
    disc, value, first, second = cubic_data(a, b, c, root)
    if value == 0 or disc == 0:
        return None
    return value < 0 and (disc < 0 or (disc > 0 and first > 0 and second < 0))


def poly_eval(poly: Poly, value: Fraction) -> Fraction:
    out = Q(0)
    for coefficient in reversed(poly):
        out = out * value + coefficient
    return out


def sturm_smallest_real_predicate(a: Fraction, b: Fraction, c: Fraction, root: Fraction) -> bool:
    poly: Poly = (c, b, a, Q(1))
    if poly_eval(poly, root) == 0:
        return False
    coefficient_bound = max(abs(a), abs(b), abs(c), Q(0))
    bound = max(abs(root) + 2, coefficient_bound + 2)
    left = -bound
    assert left < root
    assert poly_eval(poly, left) != 0
    sequence = cd._sturm_sequence(poly)
    return cd._root_count(sequence, left, root) == 0


def exhaustive_rational_catalog():
    values = (Q(-2), Q(-1), Q(-1, 2), Q(0), Q(1, 2), Q(1), Q(2))
    roots = (Q(-2), Q(-1), Q(0), Q(1), Q(2))
    total = collisions = degenerate = valid = stable = unstable = sturm_checks = 0
    one_real = three_real = 0
    one_real_stable = three_real_stable = 0
    r_negative_but_unsafe = derivative_rejections = 0

    for a, b, c, root in product(values, values, values, roots):
        disc, value, first, second = cubic_data(a, b, c, root)
        predicted = chamber_formula(a, b, c, root)
        total += 1
        if value == 0:
            collisions += 1
            assert predicted is None
            continue
        if disc == 0:
            degenerate += 1
            assert predicted is None
            # Boundary is intentionally outside the theorem, but the exact
            # Sturm observer remains well-defined and is exercised separately.
            _ = sturm_smallest_real_predicate(a, b, c, root)
            continue

        actual = sturm_smallest_real_predicate(a, b, c, root)
        assert predicted == actual
        sturm_checks += 1
        valid += 1
        stable += int(actual)
        unstable += int(not actual)

        if disc < 0:
            one_real += 1
            assert predicted == (value < 0)
            one_real_stable += int(actual)
        else:
            assert disc > 0
            three_real += 1
            assert predicted == (value < 0 and first > 0 and second < 0)
            three_real_stable += int(actual)
            if value < 0 and not actual:
                r_negative_but_unsafe += 1
                assert not (first > 0 and second < 0)
                derivative_rejections += 1

    assert total == len(values) ** 3 * len(roots)
    assert valid + collisions + degenerate == total
    assert stable + unstable == valid
    assert one_real > 0 and three_real > 0
    assert one_real_stable > 0 and three_real_stable > 0
    assert r_negative_but_unsafe > 0 and derivative_rejections == r_negative_but_unsafe
    return (
        total,
        collisions,
        degenerate,
        valid,
        stable,
        unstable,
        sturm_checks,
        one_real,
        three_real,
        one_real_stable,
        three_real_stable,
        r_negative_but_unsafe,
        derivative_rejections,
    )


def depressed_cubic_witness():
    # Q_t=x^3-3x+t, declared r=-2.
    root = Q(-2)
    grid = tuple(Q(n, 4) for n in range(-16, 17))
    stable = unstable = collision = discriminant_boundary = one_real_stable = three_real_stable = checks = 0
    for t in grid:
        a, b, c = Q(0), Q(-3), t
        disc, value, first, second = cubic_data(a, b, c, root)
        assert value == t - 2
        assert first == 9
        assert second == -12
        assert disc == 27 * (4 - t * t)
        predicted = chamber_formula(a, b, c, root)
        actual = sturm_smallest_real_predicate(a, b, c, root)

        if t == 2:
            assert value == 0 and predicted is None
            collision += 1
        elif t == -2:
            assert disc == 0 and value != 0 and predicted is None
            assert actual
            discriminant_boundary += 1
        elif t < 2:
            assert predicted is True and actual
            stable += 1
            if t < -2:
                assert disc < 0
                one_real_stable += 1
            else:
                assert -2 < t < 2 and disc > 0
                three_real_stable += 1
        else:
            assert predicted is False and not actual
            assert disc < 0
            unstable += 1
        checks += 8

    assert stable == 23
    assert unstable == 8
    assert collision == 1
    assert discriminant_boundary == 1
    assert one_real_stable == 8
    assert three_real_stable == 15
    return len(grid), stable, unstable, collision, discriminant_boundary, one_real_stable, three_real_stable, checks


def targeted_regime_examples():
    checks = 0

    # Three-real safe: x^3-3x at r=-2.
    a, b, c, r = Q(0), Q(-3), Q(0), Q(-2)
    disc, value, first, second = cubic_data(a, b, c, r)
    assert disc > 0 and value < 0 and first > 0 and second < 0
    assert chamber_formula(a, b, c, r) is True
    assert sturm_smallest_real_predicate(a, b, c, r)
    checks += 6

    # Three-real false friend: value<0 but r=1/2 lies between beta and gamma.
    r = Q(1, 2)
    disc, value, first, second = cubic_data(a, b, c, r)
    assert disc > 0 and value < 0 and first < 0
    assert chamber_formula(a, b, c, r) is False
    assert not sturm_smallest_real_predicate(a, b, c, r)
    checks += 6

    # One-real safe/unsafe pair: x^3+x, unique root 0.
    a, b, c = Q(0), Q(1), Q(0)
    for r, expected in ((Q(-1), True), (Q(1), False)):
        disc, value, _, _ = cubic_data(a, b, c, r)
        assert disc < 0
        assert chamber_formula(a, b, c, r) is expected
        assert sturm_smallest_real_predicate(a, b, c, r) is expected
        assert (value < 0) is expected
        checks += 4

    # Discriminant-zero boundary, actual selector safe but theorem silent.
    # x^3-3x-2=(x+1)^2(x-2), r=-2.
    a, b, c, r = Q(0), Q(-3), Q(-2), Q(-2)
    disc, value, _, _ = cubic_data(a, b, c, r)
    assert disc == 0 and value != 0
    assert chamber_formula(a, b, c, r) is None
    assert sturm_smallest_real_predicate(a, b, c, r)
    checks += 4

    # Discriminant-zero boundary with a real competitor to the left.
    # x^3+3x^2-4=(x+2)^2(x-1), r=-1.
    a, b, c, r = Q(3), Q(0), Q(-4), Q(-1)
    disc, value, _, _ = cubic_data(a, b, c, r)
    assert disc == 0 and value != 0
    assert chamber_formula(a, b, c, r) is None
    assert not sturm_smallest_real_predicate(a, b, c, r)
    checks += 4

    return checks


def affine_parameter_checks():
    # a(u,v)=u-v, b(u,v)=-1+u+2v, c(u,v)=1-2u+v, r=-1.
    a = RationalAffineForm((Q(0), Q(1), Q(-1)))
    b = RationalAffineForm((Q(-1), Q(1), Q(2)))
    c = RationalAffineForm((Q(1), Q(-2), Q(1)))
    root = Q(-1)
    checks = 0
    valid = 0
    for params in product((Q(-2), Q(-1), Q(0), Q(1), Q(2)), repeat=2):
        av, bv, cv = a.evaluate(params), b.evaluate(params), c.evaluate(params)
        predicted = chamber_formula(av, bv, cv, root)
        disc, value, _, _ = cubic_data(av, bv, cv, root)
        if value != 0 and disc != 0:
            assert predicted == sturm_smallest_real_predicate(av, bv, cv, root)
            valid += 1
        else:
            assert predicted is None
        checks += 2
    assert valid > 0
    return checks, valid


def main() -> int:
    catalog = exhaustive_rational_catalog()
    witness = depressed_cubic_witness()
    targeted = targeted_regime_examples()
    affine = affine_parameter_checks()
    print("BRC non-split cubic smallest-real chamber checker: PASS")
    print(f"cubic_catalog_points={catalog[0]}")
    print(f"fixed_multiplicity_collision_points={catalog[1]}")
    print(f"discriminant_zero_boundary_points={catalog[2]}")
    print(f"nondegenerate_valid_points={catalog[3]}")
    print(f"smallest_real_stable_points={catalog[4]}")
    print(f"smallest_real_unstable_points={catalog[5]}")
    print(f"exact_sturm_selector_checks={catalog[6]}")
    print(f"one_real_regime_points={catalog[7]}")
    print(f"three_real_regime_points={catalog[8]}")
    print(f"one_real_stable_points={catalog[9]}")
    print(f"three_real_stable_points={catalog[10]}")
    print(f"R_negative_but_unsafe_three_real_points={catalog[11]}")
    print(f"derivative_rejection_checks={catalog[12]}")
    print(f"depressed_cubic_grid_points={witness[0]}")
    print(f"depressed_cubic_stable={witness[1]}")
    print(f"depressed_cubic_unstable={witness[2]}")
    print(f"depressed_cubic_collision={witness[3]}")
    print(f"depressed_cubic_discriminant_boundary={witness[4]}")
    print(f"depressed_cubic_one_real_stable={witness[5]}")
    print(f"depressed_cubic_three_real_stable={witness[6]}")
    print(f"depressed_cubic_formula_checks={witness[7]}")
    print(f"targeted_regime_checks={targeted}")
    print(f"affine_parameter_checks={affine[0]}")
    print(f"affine_parameter_valid_points={affine[1]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
