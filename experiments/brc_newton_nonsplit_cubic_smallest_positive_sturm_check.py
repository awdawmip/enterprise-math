#!/usr/bin/env python3
"""Exact checker for the monic-cubic smallest-positive specialized Sturm selector."""
from __future__ import annotations

from fractions import Fraction
from itertools import product

from enterprise_math import brc_critical_degeneracy as cd

Q = Fraction
Poly = tuple[Fraction, ...]  # ascending powers


def trim(poly: Poly) -> Poly:
    values = list(poly)
    while len(values) > 1 and values[-1] == 0:
        values.pop()
    return tuple(values) if values else (Q(0),)


def peval(poly: Poly, x: Fraction) -> Fraction:
    out = Q(0)
    for coefficient in reversed(poly):
        out = out * x + coefficient
    return out


def derivative(poly: Poly) -> Poly:
    if len(poly) <= 1:
        return (Q(0),)
    return trim(tuple(Q(i) * poly[i] for i in range(1, len(poly))))


def pdivmod(numerator: Poly, denominator: Poly):
    n = list(trim(numerator))
    d = trim(denominator)
    if d == (Q(0),):
        raise ZeroDivisionError
    if len(n) < len(d):
        return (Q(0),), tuple(n)
    q = [Q(0) for _ in range(len(n) - len(d) + 1)]
    while len(n) >= len(d) and any(n):
        degree = len(n) - len(d)
        factor = n[-1] / d[-1]
        q[degree] += factor
        for index, value in enumerate(d):
            n[index + degree] -= factor * value
        while len(n) > 1 and n[-1] == 0:
            n.pop()
    return trim(tuple(q)), trim(tuple(n))


def variation(values) -> int:
    signs = []
    for value in values:
        value = Q(value)
        if value:
            signs.append((value > 0) - (value < 0))
    return sum(a != b for a, b in zip(signs, signs[1:]))


def invariants(a: Fraction, b: Fraction, c: Fraction):
    A = a * a - 3 * b
    B = a * b - 9 * c
    Delta = a * a * b * b - 4 * b**3 - 4 * a**3 * c - 27 * c * c + 18 * a * b * c
    return A, B, Delta


def cubic_poly(a: Fraction, b: Fraction, c: Fraction) -> Poly:
    return (c, b, a, Q(1))


def specialized_cubic_values(a: Fraction, b: Fraction, c: Fraction, x: Fraction):
    poly = cubic_poly(a, b, c)
    prime = derivative(poly)
    A, B, Delta = invariants(a, b, c)
    values = [peval(poly, x), peval(prime, x)]
    if A != 0:
        values.extend((2 * A * x + B, Delta))
    elif B != 0:
        values.append(B)
    return tuple(values)


def specialized_cubic_variation(a: Fraction, b: Fraction, c: Fraction, x: Fraction) -> int:
    return variation(specialized_cubic_values(a, b, c, x))


def specialized_remainder_identity_checks(a: Fraction, b: Fraction, c: Fraction) -> int:
    poly = cubic_poly(a, b, c)
    prime = derivative(poly)
    A, B, Delta = invariants(a, b, c)
    _, rem1 = pdivmod(poly, prime)
    expected1 = (Q(-B, 9), Q(-2 * A, 9))
    assert rem1 == trim(expected1)
    checks = 2
    if A != 0:
        s2 = (B, 2 * A)
        _, rem2 = pdivmod(prime, s2)
        expected2 = Q(-9) * Delta / (4 * A * A)
        assert rem2 == (expected2,)
        assert 4 * a * A * B - 4 * b * A * A - 3 * B * B == 9 * Delta
        checks += 3
    elif B != 0:
        # The first negative remainder is already a nonzero constant B/9.
        assert Delta == -B * B / 3
        checks += 1
    else:
        assert Delta == 0
        checks += 1
    return checks


def deflate_zero_roots(poly: Poly):
    values = trim(poly)
    order = 0
    while len(values) > 1 and values[0] == 0:
        values = values[1:]
        order += 1
    return trim(values), order


def quadratic_variation(poly: Poly, x: Fraction) -> int:
    # monic x^2+a*x+b after zero-root deflation
    if len(poly) != 3 or poly[-1] != 1:
        raise ValueError("expected monic quadratic")
    b, a, _ = poly
    D = a * a - 4 * b
    return variation((peval(poly, x), 2 * x + a, D))


def linear_variation(poly: Poly, x: Fraction) -> int:
    if len(poly) != 2 or poly[-1] != 1:
        raise ValueError("expected monic linear")
    return variation((peval(poly, x), Q(1)))


def specialized_positive_interval_count(a: Fraction, b: Fraction, c: Fraction, root: Fraction) -> int:
    if root <= 0:
        raise ValueError("root must be positive")
    original = cubic_poly(a, b, c)
    if peval(original, root) == 0:
        raise ValueError("fixed multiplicity collision")
    deflated, _ = deflate_zero_roots(original)
    if len(deflated) == 1:
        return 0
    if len(deflated) == 2:
        count = linear_variation(deflated, Q(0)) - linear_variation(deflated, root)
    elif len(deflated) == 3:
        count = quadratic_variation(deflated, Q(0)) - quadratic_variation(deflated, root)
    elif len(deflated) == 4:
        # c != 0 after full zero-root deflation, so both endpoints are nonroots.
        count = specialized_cubic_variation(a, b, c, Q(0)) - specialized_cubic_variation(a, b, c, root)
    else:
        raise AssertionError("deflated cubic degree out of range")
    if count < 0 or count > 3:
        raise AssertionError("specialized interval count left valid range")
    return count


def generic_positive_interval_count(a: Fraction, b: Fraction, c: Fraction, root: Fraction) -> int:
    original = cubic_poly(a, b, c)
    if root <= 0 or peval(original, root) == 0:
        raise ValueError("invalid fixed-multiplicity positive selector point")
    deflated, _ = deflate_zero_roots(original)
    if len(deflated) == 1:
        return 0
    assert peval(deflated, Q(0)) != 0
    assert peval(deflated, root) != 0
    return cd._root_count(cd._sturm_sequence(deflated), Q(0), root)


def exhaustive_catalog():
    values = (Q(-2), Q(-1), Q(0), Q(1), Q(2))
    roots = (Q(1, 2), Q(1), Q(2))
    total = collisions = stable = unsafe = 0
    interval_checks = variation_checks = identity_checks = 0
    zero_simple = zero_double = zero_triple = 0
    A_zero = B_zero = delta_zero = 0
    genuine_cubic = 0

    for a, b, c, root in product(values, values, values, roots):
        poly = cubic_poly(a, b, c)
        if peval(poly, root) == 0:
            collisions += 1
            total += 1
            continue
        count = specialized_positive_interval_count(a, b, c, root)
        generic = generic_positive_interval_count(a, b, c, root)
        assert count == generic
        interval_checks += 1
        stable += int(count == 0)
        unsafe += int(count > 0)

        A, B, Delta = invariants(a, b, c)
        A_zero += int(A == 0)
        B_zero += int(B == 0)
        delta_zero += int(Delta == 0)
        identity_checks += specialized_remainder_identity_checks(a, b, c)

        deflated, zero_order = deflate_zero_roots(poly)
        if zero_order == 1:
            zero_simple += 1
        elif zero_order == 2:
            zero_double += 1
        elif zero_order == 3:
            zero_triple += 1

        if c != 0:
            genuine_cubic += 1
            # Compare the specialized finite-endpoint variation directly with
            # the repository's generic Sturm sequence at endpoints.
            generic_seq = cd._sturm_sequence(poly)
            assert specialized_cubic_variation(a, b, c, Q(0)) == cd._sign_variations(generic_seq, Q(0))
            assert specialized_cubic_variation(a, b, c, root) == cd._sign_variations(generic_seq, root)
            variation_checks += 2
        total += 1

    assert total == 375
    assert stable + unsafe + collisions == total
    assert zero_simple > 0 and zero_double > 0 and zero_triple > 0
    assert A_zero > 0 and B_zero > 0 and delta_zero > 0
    return (
        total,
        collisions,
        stable,
        unsafe,
        interval_checks,
        variation_checks,
        identity_checks,
        zero_simple,
        zero_double,
        zero_triple,
        A_zero,
        B_zero,
        delta_zero,
        genuine_cubic,
    )


def one_parameter_x3_plus_t_witness():
    # E_t=(x-1)^2(x^3+t), declared root r=1.
    root = Q(1)
    grid = tuple(Q(n, 4) for n in range(-12, 13))
    stable = collision = unsafe = irrational_competitor = zero_triple = checks = 0
    for t in grid:
        poly = cubic_poly(Q(0), Q(0), t)
        if peval(poly, root) == 0:
            assert t == -1
            collision += 1
            checks += 1
            continue
        count = specialized_positive_interval_count(Q(0), Q(0), t, root)
        assert count == generic_positive_interval_count(Q(0), Q(0), t, root)
        predicted_safe = t < -1 or t >= 0
        assert (count == 0) == predicted_safe
        stable += int(predicted_safe)
        unsafe += int(not predicted_safe)
        if -1 < t < 0:
            # Positive competitor cbrt(-t) lies in (0,1); on this rational
            # quarter-grid it is nonrational except at no interior point.
            irrational_competitor += 1
        if t == 0:
            _, order = deflate_zero_roots(poly)
            assert order == 3 and count == 0
            zero_triple += 1
        checks += 4
    assert stable == 21
    assert collision == 1
    assert unsafe == 3
    assert irrational_competitor == 3
    assert zero_triple == 1
    return len(grid), stable, collision, unsafe, irrational_competitor, zero_triple, checks


def endpoint_and_degenerate_examples():
    checks = 0
    # simple zero + quadratic positive competitor at 1/2: x(x-1/2)(x+1)
    # = x^3 + 1/2 x^2 -1/2 x
    count = specialized_positive_interval_count(Q(1, 2), Q(-1, 2), Q(0), Q(1))
    assert count == 1
    checks += 1

    # double zero + remaining negative root: x^2(x+1), no positive competitor.
    count = specialized_positive_interval_count(Q(1), Q(0), Q(0), Q(1))
    assert count == 0
    checks += 1

    # triple zero: x^3, no positive competitor.
    count = specialized_positive_interval_count(Q(0), Q(0), Q(0), Q(1))
    assert count == 0
    checks += 1

    # A=B=0 triple nonzero root: (x+1)^3, all competitors nonpositive.
    a, b, c = Q(3), Q(3), Q(1)
    A, B, Delta = invariants(a, b, c)
    assert A == 0 and B == 0 and Delta == 0
    assert specialized_positive_interval_count(a, b, c, Q(1)) == 0
    checks += 4

    # A=0, B!=0 degenerate specialized sequence.
    a, b, c = Q(0), Q(0), Q(1)
    A, B, Delta = invariants(a, b, c)
    assert A == 0 and B != 0 and Delta < 0
    assert specialized_cubic_variation(a, b, c, Q(0)) == cd._sign_variations(cd._sturm_sequence(cubic_poly(a, b, c)), Q(0))
    checks += 4
    return checks


def main() -> int:
    catalog = exhaustive_catalog()
    witness = one_parameter_x3_plus_t_witness()
    endpoint = endpoint_and_degenerate_examples()
    print("BRC non-split cubic smallest-positive Sturm checker: PASS")
    print(f"cubic_catalog_points={catalog[0]}")
    print(f"fixed_multiplicity_collisions={catalog[1]}")
    print(f"smallest_positive_stable_points={catalog[2]}")
    print(f"smallest_positive_unsafe_points={catalog[3]}")
    print(f"specialized_vs_generic_interval_checks={catalog[4]}")
    print(f"specialized_vs_generic_variation_checks={catalog[5]}")
    print(f"sturm_remainder_identity_checks={catalog[6]}")
    print(f"simple_zero_endpoint_points={catalog[7]}")
    print(f"double_zero_endpoint_points={catalog[8]}")
    print(f"triple_zero_endpoint_points={catalog[9]}")
    print(f"A_zero_points={catalog[10]}")
    print(f"B_zero_points={catalog[11]}")
    print(f"discriminant_zero_points={catalog[12]}")
    print(f"genuine_cubic_fixed_points={catalog[13]}")
    print(f"one_parameter_points={witness[0]}")
    print(f"one_parameter_stable={witness[1]}")
    print(f"one_parameter_collision={witness[2]}")
    print(f"one_parameter_unsafe={witness[3]}")
    print(f"one_parameter_irrational_competitor_points={witness[4]}")
    print(f"one_parameter_triple_zero_points={witness[5]}")
    print(f"one_parameter_checks={witness[6]}")
    print(f"endpoint_degenerate_checks={endpoint}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
