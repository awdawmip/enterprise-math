#!/usr/bin/env python3
"""Exact checker for factorized BRC selector certificates and root-support Möbius calculus."""
from __future__ import annotations

from fractions import Fraction
from itertools import combinations, product

import brc_newton_resultant_event_generator_check as rg
from enterprise_math import brc_critical_degeneracy as cd

Q = Fraction
Poly = tuple[Fraction, ...]


def trim(poly) -> Poly:
    return cd._trim(tuple(Q(value) for value in poly))


def peval(poly: Poly, value: Fraction) -> Fraction:
    return cd._p_eval(trim(poly), value)


def pmul(left: Poly, right: Poly) -> Poly:
    return cd._p_mul(trim(left), trim(right))


def ppow(poly: Poly, exponent: int) -> Poly:
    if isinstance(exponent, bool) or not isinstance(exponent, int) or exponent < 0:
        raise ValueError("exponent must be a non-negative integer")
    out: Poly = (Q(1),)
    base = trim(poly)
    for _ in range(exponent):
        out = pmul(out, base)
    return out


def product_polynomials(factors: tuple[Poly, ...], exponents: tuple[int, ...] | None = None) -> Poly:
    if not factors:
        return (Q(1),)
    powers = exponents if exponents is not None else tuple(1 for _ in factors)
    if len(powers) != len(factors):
        raise ValueError("factor/exponent length mismatch")
    out: Poly = (Q(1),)
    for factor, exponent in zip(factors, powers):
        out = pmul(out, ppow(factor, exponent))
    return out


def deflate_rational_endpoint(poly: Poly, endpoint: Fraction) -> Poly:
    out = trim(poly)
    factor = (Q(-endpoint), Q(1))
    while len(out) > 1 and peval(out, endpoint) == 0:
        out = cd._p_div_exact(out, factor)
    return trim(out)


def squarefree_part(poly: Poly) -> Poly:
    out = trim(poly)
    if len(out) <= 1:
        return out
    derivative = cd._p_derivative(out)
    gcd = cd._p_gcd(out, derivative)
    return cd._p_div_exact(out, gcd) if len(gcd) > 1 else out


def distinct_open_root_count(poly: Poly, left: Fraction, right: Fraction) -> int:
    if not left < right:
        raise ValueError("left must be smaller than right")
    out = deflate_rational_endpoint(trim(poly), left)
    out = deflate_rational_endpoint(out, right)
    out = squarefree_part(out)
    if len(out) <= 1:
        return 0
    assert peval(out, left) != 0 and peval(out, right) != 0
    return cd._root_count(cd._sturm_sequence(out), left, right)


def multiplicity_open_root_count(poly: Poly, left: Fraction, right: Fraction) -> int:
    """Count real roots in the open interval with algebraic multiplicity."""
    original = trim(poly)
    if len(original) <= 1:
        return 0
    total = distinct_open_root_count(original, left, right)
    common = original
    derivative = original
    for _ in range(1, len(original) - 1):
        derivative = cd._p_derivative(derivative)
        common = cd._p_gcd(common, derivative)
        if len(common) <= 1:
            break
        total += distinct_open_root_count(common, left, right)
    return total


def gcd_many(factors: tuple[Poly, ...]) -> Poly:
    if not factors:
        raise ValueError("at least one factor is required")
    out = trim(factors[0])
    for factor in factors[1:]:
        out = cd._p_gcd(out, trim(factor))
        if len(out) <= 1:
            return (Q(1),)
    return trim(out)


def pairwise_coprime(factors: tuple[Poly, ...]) -> bool:
    return all(
        len(cd._p_gcd(factors[i], factors[j])) <= 1
        for i in range(len(factors))
        for j in range(i + 1, len(factors))
    )


def failing_factor_support(
    factors: tuple[Poly, ...],
    left: Fraction,
    right: Fraction,
) -> tuple[int, ...]:
    return tuple(
        index
        for index, factor in enumerate(factors)
        if distinct_open_root_count(factor, left, right) > 0
    )


def mobius_distinct_root_count(
    factors: tuple[Poly, ...],
    left: Fraction,
    right: Fraction,
) -> tuple[int, int]:
    """Inclusion-exclusion over subset gcd root supports."""
    total = 0
    terms = 0
    for size in range(1, len(factors) + 1):
        sign = 1 if size % 2 else -1
        for indices in combinations(range(len(factors)), size):
            common = gcd_many(tuple(factors[index] for index in indices))
            total += sign * distinct_open_root_count(common, left, right)
            terms += 1
    return total, terms


def linear(root: Fraction) -> Poly:
    return (Q(-root), Q(1))


def factor_library() -> tuple[tuple[str, Poly], ...]:
    x = linear(Q(0))
    xm1 = linear(Q(1))
    xm2 = linear(Q(2))
    xm3 = linear(Q(3))
    return (
        ("x(x-1)", pmul(x, xm1)),
        ("x(x-2)", pmul(x, xm2)),
        ("x(x-3)", pmul(x, xm3)),
        ("(x-1)(x-2)", pmul(xm1, xm2)),
        ("x^2-2", (Q(-2), Q(0), Q(1))),
        ("x^2+1", (Q(1), Q(0), Q(1))),
        ("x^2-x-1", (Q(-1), Q(-1), Q(1))),
        ("x+1", linear(Q(-1))),
        ("x-5/2", linear(Q(5, 2))),
    )


def factorized_root_support_regression() -> tuple[int, ...]:
    library = factor_library()
    intervals = (
        (Q(-2), Q(4)),
        (Q(0), Q(2)),
        (Q(-1, 2), Q(3, 2)),
        (Q(1), Q(3)),
        (Q(-3, 2), Q(1, 2)),
    )

    samples = conjunction_checks = mobius_checks = mobius_terms = 0
    coprime_samples = additive_checks = noncoprime_samples = nonadditive_witnesses = 0

    for size in range(1, 5):
        for selected in combinations(library, size):
            factors = tuple(poly for _, poly in selected)
            expanded = product_polynomials(factors)
            is_coprime = pairwise_coprime(factors)
            for left, right in intervals:
                actual = distinct_open_root_count(expanded, left, right)
                support = failing_factor_support(factors, left, right)
                assert (actual == 0) == (not support)
                conjunction_checks += 2

                reconstructed, terms = mobius_distinct_root_count(factors, left, right)
                assert reconstructed == actual
                mobius_checks += 1
                mobius_terms += terms

                singles = sum(distinct_open_root_count(factor, left, right) for factor in factors)
                if is_coprime:
                    assert singles == actual
                    coprime_samples += 1
                    additive_checks += 1
                else:
                    noncoprime_samples += 1
                    if singles != actual:
                        nonadditive_witnesses += 1
                samples += 1

    assert samples == 1275
    assert mobius_terms == 12975
    assert coprime_samples > 0
    assert noncoprime_samples > 0
    assert nonadditive_witnesses > 0
    return (
        samples,
        conjunction_checks,
        mobius_checks,
        mobius_terms,
        coprime_samples,
        additive_checks,
        noncoprime_samples,
        nonadditive_witnesses,
    )


def multiplicity_additivity_regression() -> tuple[int, ...]:
    library = tuple(poly for _, poly in factor_library()[:7])
    intervals = (
        (Q(-2), Q(4)),
        (Q(0), Q(2)),
        (Q(-1, 2), Q(3, 2)),
    )
    samples = factor_terms = shared_root_samples = 0

    for indices in combinations(range(len(library)), 3):
        factors = tuple(library[index] for index in indices)
        shared = not pairwise_coprime(factors)
        for exponents in product((1, 2), repeat=3):
            expanded = product_polynomials(factors, exponents)
            for left, right in intervals:
                expected = sum(
                    exponent * multiplicity_open_root_count(factor, left, right)
                    for factor, exponent in zip(factors, exponents)
                )
                actual = multiplicity_open_root_count(expanded, left, right)
                assert actual == expected
                samples += 1
                factor_terms += len(factors)
                shared_root_samples += int(shared)

    assert samples == 840
    assert shared_root_samples > 0
    return samples, factor_terms, shared_root_samples


def third_order_intersection_witness() -> tuple[int, ...]:
    x = linear(Q(0))
    factors = (
        pmul(x, linear(Q(1))),
        pmul(x, linear(Q(2))),
        pmul(x, linear(Q(3))),
    )
    left, right = Q(-1), Q(4)
    singles = sum(distinct_open_root_count(factor, left, right) for factor in factors)
    pairs = sum(
        distinct_open_root_count(gcd_many((factors[i], factors[j])), left, right)
        for i, j in combinations(range(3), 2)
    )
    triple = distinct_open_root_count(gcd_many(factors), left, right)
    expanded = product_polynomials(factors)
    actual = distinct_open_root_count(expanded, left, right)
    mobius, terms = mobius_distinct_root_count(factors, left, right)

    assert (singles, pairs, triple, actual) == (6, 3, 1, 4)
    assert singles - pairs == 3 != actual
    assert singles - pairs + triple == mobius == actual
    assert terms == 7
    return singles, pairs, triple, actual, terms


def contextual_selector_minimality() -> tuple[int, ...]:
    """AND is one-shot sufficient; factor-local contexts recover every safety bit."""
    width = 5
    signatures: dict[tuple[bool, ...], tuple[bool, ...]] = {}
    one_shot_classes: set[bool] = set()
    context_checks = 0
    for state in product((False, True), repeat=width):
        one_shot_classes.add(all(state))
        observations = []
        for retained in range(width):
            context = tuple(state[index] if index == retained else True for index in range(width))
            observations.append(all(context))
            assert observations[-1] == state[retained]
            context_checks += 1
        signature = tuple(observations)
        assert signature == state
        signatures[state] = signature

    assert len(one_shot_classes) == 2
    assert len(set(signatures.values())) == 2**width

    left = (False, True, True, True, True)
    right = (True, False, True, True, True)
    assert all(left) == all(right) is False
    expose_first_left = all((left[0], True, True, True, True))
    expose_first_right = all((right[0], True, True, True, True))
    assert expose_first_left is False and expose_first_right is True
    return width, len(one_shot_classes), len(signatures), context_checks, 4


def t_associate(left, right) -> bool:
    left, right = rg.t_trim(left), rg.t_trim(right)
    if left == rg.ZERO or right == rg.ZERO:
        return left == right
    if len(left) != len(right):
        return False
    scalar = left[-1] / right[-1]
    return scalar != 0 and left == rg.t_scale(right, scalar)


def interval_factor_event(family, left: Fraction, right: Fraction):
    event = rg.resultant_event_factor(family)
    event = rg.t_mul(event, rg.x_eval(family, left))
    event = rg.t_mul(event, rg.x_eval(family, right))
    return rg.t_trim(event)


def specialize_x(family, parameter: Fraction) -> Poly:
    return trim(tuple(rg.t_eval(coefficient, parameter) for coefficient in family))


def factorized_event_observer_regression() -> tuple[int, ...]:
    # Two moving linear factors collide at x=2 when t=0.  The collision is
    # invisible to Boolean interval emptiness but visible to distinct-root count.
    f_left = ((Q(-2), Q(-1)), rg.ONE)   # x-(2+t)
    f_right = ((Q(-2), Q(1)), rg.ONE)   # x-(2-t)
    f_complex = (rg.ONE, rg.ZERO, rg.ONE)  # x^2+1
    support_product = rg.x_mul(f_left, f_right)

    r_left = rg.resultant_event_factor(f_left)
    r_right = rg.resultant_event_factor(f_right)
    cross = rg.sylvester_resultant(f_left, f_right)
    product_resultant = rg.resultant_event_factor(support_product)
    cross_square = rg.t_mul(cross, cross)
    assert r_left == r_right == rg.ONE
    assert cross == (Q(0), Q(2))
    assert t_associate(product_resultant, rg.t_mul(rg.t_mul(r_left, r_right), cross_square))

    boolean_event = rg.t_mul(
        interval_factor_event(f_left, Q(0), Q(4)),
        interval_factor_event(f_right, Q(0), Q(4)),
    )
    distinct_event = rg.t_mul(boolean_event, cross)
    assert rg.real_root_count(boolean_event) == 2
    assert rg.real_root_count(distinct_event) == 3
    assert rg.t_eval(boolean_event, Q(0)) != 0
    assert rg.t_eval(distinct_event, Q(0)) == 0

    points = (Q(-3), Q(-1), Q(0), Q(1), Q(3))
    expected_distinct = (0, 2, 1, 2, 0)
    expected_multiplicity = (0, 2, 2, 2, 0)
    expected_safe = (True, False, False, False, True)
    point_checks = 0

    for parameter, distinct_expected, mult_expected, safe_expected in zip(
        points, expected_distinct, expected_multiplicity, expected_safe
    ):
        left_poly = specialize_x(f_left, parameter)
        right_poly = specialize_x(f_right, parameter)
        expanded = pmul(left_poly, right_poly)
        distinct = distinct_open_root_count(expanded, Q(0), Q(4))
        multiplicity = multiplicity_open_root_count(expanded, Q(0), Q(4))
        factor_counts = (
            distinct_open_root_count(left_poly, Q(0), Q(4)),
            distinct_open_root_count(right_poly, Q(0), Q(4)),
        )
        assert distinct == distinct_expected
        assert multiplicity == mult_expected == sum(factor_counts)
        assert (distinct == 0) == safe_expected
        if parameter == 0:
            assert sum(factor_counts) == 2 and distinct == 1
        else:
            assert sum(factor_counts) == distinct
        point_checks += 6

    # Three-factor discriminant/resultant product identity, up to a nonzero unit.
    three = rg.x_mul(support_product, f_complex)
    rhs = rg.t_mul(
        rg.t_mul(
            rg.t_mul(
                rg.resultant_event_factor(f_left),
                rg.resultant_event_factor(f_right),
            ),
            rg.resultant_event_factor(f_complex),
        ),
        rg.t_mul(
            rg.t_mul(
                rg.sylvester_resultant(f_left, f_right),
                rg.sylvester_resultant(f_left, f_right),
            ),
            rg.t_mul(
                rg.t_mul(
                    rg.sylvester_resultant(f_left, f_complex),
                    rg.sylvester_resultant(f_left, f_complex),
                ),
                rg.t_mul(
                    rg.sylvester_resultant(f_right, f_complex),
                    rg.sylvester_resultant(f_right, f_complex),
                ),
            ),
        ),
    )
    assert t_associate(rg.resultant_event_factor(three), rhs)

    # Expanded permanent multiplicity destroys the nominal resultant event
    # generator, while the typed factor support/event remains nonzero.
    repeated = rg.x_mul(f_left, f_left)
    assert rg.resultant_event_factor(repeated) == rg.ZERO
    assert interval_factor_event(f_left, Q(0), Q(4)) != rg.ZERO

    return (
        point_checks,
        rg.real_root_count(boolean_event),
        rg.real_root_count(distinct_event),
        7,
    )


def main() -> int:
    support = factorized_root_support_regression()
    multiplicity = multiplicity_additivity_regression()
    third = third_order_intersection_witness()
    context = contextual_selector_minimality()
    events = factorized_event_observer_regression()

    print("BRC factorized selector Möbius checker: PASS")
    print(f"factorized_interval_samples={support[0]}")
    print(f"selector_conjunction_checks={support[1]}")
    print(f"mobius_reconstruction_checks={support[2]}")
    print(f"mobius_subset_terms={support[3]}")
    print(f"pairwise_coprime_samples={support[4]}")
    print(f"coprime_additivity_checks={support[5]}")
    print(f"noncoprime_samples={support[6]}")
    print(f"nonadditive_distinct_count_witnesses={support[7]}")
    print(f"multiplicity_additivity_samples={multiplicity[0]}")
    print(f"multiplicity_factor_terms={multiplicity[1]}")
    print(f"shared_root_multiplicity_samples={multiplicity[2]}")
    print(f"third_order_intersection_witness={third}")
    print(f"contextual_selector_minimality={context}")
    print(f"factorized_event_observer_checks={events}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
