#!/usr/bin/env python3
"""Exact checker for rational-root Newton recursion over rational-valuation scales."""
from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from itertools import product
from math import comb, gcd, lcm

import brc_critical_ratio_spectral_response_check as rsp
import brc_global_powered_strict_gauge_reducible_check as red
import brc_multiple_root_first_newton_edge_check as ne
import brc_unique_winner_root_active_characteristic_jet_check as win
from enterprise_math import brc_critical_degeneracy as cd
from enterprise_math.brc_rational_holonomy import (
    rational_from_prime_valuations,
    rational_prime_valuations,
)

Q = Fraction
Branch = tuple[int, int, Fraction]
Poly = tuple[Fraction, ...]
Scale = tuple[tuple[int, Fraction], ...]
Jet = dict[Scale, Poly]
ONE: Scale = ()


def trim(poly: Poly) -> Poly:
    values = list(poly)
    while len(values) > 1 and values[-1] == 0:
        values.pop()
    return tuple(values) if values else (Q(0),)


def p_eval(poly: Poly, x: Fraction) -> Fraction:
    out = Q(0)
    for coefficient in reversed(poly):
        out = out * x + coefficient
    return out


def derivative(poly: Poly) -> Poly:
    if len(poly) <= 1:
        return (Q(0),)
    return trim(tuple(Q(i) * poly[i] for i in range(1, len(poly))))


def vanish_order_at_rational(poly: Poly, root: Fraction) -> int:
    current = poly
    order = 0
    while current != (Q(0),) and p_eval(current, root) == 0:
        current = derivative(current)
        order += 1
    return 10**6 if current == (Q(0),) else order


def taylor_coefficient(poly: Poly, root: Fraction, order: int) -> Fraction:
    return sum(
        (poly[j] * comb(j, order) * root ** (j - order) for j in range(order, len(poly))),
        Q(0),
    )


def scale_normalize(values: dict[int, Fraction]) -> Scale:
    return tuple(sorted((prime, exponent) for prime, exponent in values.items() if exponent))


def scale_from_rational(value: Fraction) -> Scale:
    if value <= 0:
        raise ValueError("scale rational must be positive")
    return scale_normalize({prime: Q(exp) for prime, exp in rational_prime_valuations(value)})


def scale_mul(left: Scale, right: Scale) -> Scale:
    values: dict[int, Fraction] = defaultdict(Q)
    for prime, exponent in left:
        values[prime] += exponent
    for prime, exponent in right:
        values[prime] += exponent
    return scale_normalize(values)


def scale_pow(scale: Scale, exponent: int | Fraction) -> Scale:
    power = Q(exponent)
    return scale_normalize({prime: value * power for prime, value in scale})


def scale_root(scale: Scale, degree: int) -> Scale:
    if isinstance(degree, bool) or not isinstance(degree, int) or degree <= 0:
        raise ValueError("root degree must be positive integer")
    return scale_pow(scale, Q(1, degree))


def scale_to_rational_power(scale: Scale, power: int) -> Fraction:
    if power <= 0:
        raise ValueError("power must be positive")
    coords = []
    for prime, exponent in scale:
        value = exponent * power
        if value.denominator != 1:
            raise ValueError("power did not clear valuation denominators")
        coords.append((prime, value.numerator))
    return rational_from_prime_valuations(tuple(coords))


def scale_compare(left: Scale, right: Scale) -> int:
    diff = scale_mul(left, scale_pow(right, -1))
    denominator = 1
    for _, exponent in diff:
        denominator = lcm(denominator, exponent.denominator)
    value = scale_to_rational_power(diff, denominator)
    return (value > 1) - (value < 1)


def scale_max(scales: list[Scale]) -> Scale:
    if not scales:
        raise ValueError("empty scale list")
    best = scales[0]
    for scale in scales[1:]:
        if scale_compare(scale, best) > 0:
            best = scale
    return best


def add_poly(target: dict[Scale, list[Fraction]], scale: Scale, order: int, coefficient: Fraction) -> None:
    if coefficient == 0:
        return
    values = target.setdefault(scale, [])
    while len(values) <= order:
        values.append(Q(0))
    values[order] += coefficient


def freeze_jet(raw: dict[Scale, list[Fraction]]) -> Jet:
    return {scale: trim(tuple(values)) for scale, values in raw.items() if any(values)}


def rational_jet(expansion: dict[Fraction, Poly]) -> Jet:
    return {scale_from_rational(base): trim(tuple(Q(c) for c in poly)) for base, poly in expansion.items()}


def newton_step(jet: Jet, root: Fraction, multiplicity: int):
    if multiplicity < 2:
        raise ValueError("Newton recursion step requires multiple selected root")
    if ONE not in jet:
        raise ValueError("jet lost scale-one polynomial")
    assert vanish_order_at_rational(jet[ONE], root) == multiplicity

    candidates: list[Scale] = []
    for scale, poly in jet.items():
        if scale == ONE:
            continue
        q = vanish_order_at_rational(poly, root)
        if q < multiplicity:
            candidates.append(scale_root(scale, multiplicity - q))
    if not candidates:
        return None
    theta = scale_max(candidates)

    raw: dict[Scale, list[Fraction]] = {}
    checks = 0
    for scale, poly in jet.items():
        for order in range(len(poly)):
            coefficient = taylor_coefficient(poly, root, order)
            if coefficient == 0:
                continue
            residual = scale_mul(scale, scale_pow(theta, order - multiplicity))
            assert scale_compare(residual, ONE) <= 0
            add_poly(raw, residual, order, coefficient)
            checks += 1
    output = freeze_jet(raw)
    assert ONE in output
    return theta, output, output[ONE], checks


def direct_two_step(original: Jet, z0: Fraction, r1: int, theta1: Scale, y0: Fraction, r2: int, theta2: Scale) -> Jet:
    raw: dict[Scale, list[Fraction]] = {}
    for scale, poly in original.items():
        for k in range(len(poly)):
            coefficient = taylor_coefficient(poly, z0, k)
            if coefficient == 0:
                continue
            for j in range(k + 1):
                value = coefficient * Q(comb(k, j)) * y0 ** (k - j)
                if value == 0:
                    continue
                residual = scale_mul(scale, scale_mul(scale_pow(theta1, k - r1), scale_pow(theta2, j - r2)))
                add_poly(raw, residual, j, value)
    return freeze_jet(raw)


def divisors(value: int) -> tuple[int, ...]:
    value = abs(value)
    if value == 0:
        return (0,)
    return tuple(i for i in range(1, value + 1) if value % i == 0)


def rational_factor_roots(poly: Poly):
    poly = trim(poly)
    roots: list[Fraction] = []
    current = poly
    while len(current) > 1 and current[0] == 0:
        roots.append(Q(0))
        current = trim(current[1:])
    if len(current) <= 1:
        return tuple(sorted(roots)), current

    denominator = 1
    for value in current:
        denominator = lcm(denominator, value.denominator)
    integers = [int(value * denominator) for value in current]
    content = 0
    for value in integers:
        content = gcd(content, abs(value))
    if content:
        integers = [value // content for value in integers]
    constant = integers[0]
    leading = integers[-1]
    candidates = {Q(sign * p, q) for p in divisors(constant) for q in divisors(leading) if q for sign in (-1, 1)}
    for root in sorted(candidates):
        while len(current) > 1 and p_eval(current, root) == 0:
            roots.append(root)
            current = trim(cd._p_div_exact(current, (-root, Q(1))))
    return tuple(sorted(roots)), current


def selected_rational_multiple_edge_root(edge: Poly):
    roots, residual = rational_factor_roots(edge)
    if len(residual) > 1 or not roots:
        return None
    selected = min(roots)
    multiplicity = roots.count(selected)
    if selected >= 0 or multiplicity < 2:
        return None
    return selected, multiplicity


def initial_multiple_sample(n: int, branches: tuple[Branch, ...]):
    try:
        data = red.global_strict_gauge(n, branches)
    except ValueError:
        return None
    gauge, _, _, _, records, _, _, _ = data
    K = gauge.analysis.critical_matrix
    levels, layers = win.levels_layers(n, records)
    expansion = rsp.determinant_exponential_expansion(levels, layers)
    p0_int = cd.criticality_polynomial(K)
    p0 = tuple(Q(value) for value in p0_int)
    selector = cd.smallest_positive_root_selector(p0_int)
    if not selector.is_rational or win.selector_simple(p0, selector):
        return None
    assert selector.exact_root is not None
    z0 = selector.exact_root
    r1 = vanish_order_at_rational(p0, z0)
    original = rational_jet(expansion)
    first = newton_step(original, z0, r1)
    if first is None:
        return None
    theta1, jet1, edge1, checks1 = first
    edge_root = selected_rational_multiple_edge_root(edge1)
    if edge_root is None:
        return None
    y0, r2 = edge_root
    second = newton_step(jet1, y0, r2)
    if second is None:
        return None
    theta2, jet2, edge2, checks2 = second
    direct = direct_two_step(original, z0, r1, theta1, y0, r2, theta2)
    assert jet2 == direct
    return theta1, theta2, edge1, edge2, checks1 + checks2, len(jet2)


def branches_from_assignment(cells, assignment) -> tuple[Branch, ...]:
    return tuple((u, v, q) for (u, v), weights in zip(cells, assignment) for q in weights)


def exhaustive_second_edge_regression():
    eligible = recursive_checks = scale_layers = 0
    catalog2 = [(), (Q(1, 4),), (Q(1, 2),), (Q(1, 2), Q(1, 2))]
    cells2 = [(0, 0), (0, 1), (1, 0), (1, 1)]
    for assignment in product(catalog2, repeat=4):
        result = initial_multiple_sample(2, branches_from_assignment(cells2, assignment))
        if result is not None:
            eligible += 1
            recursive_checks += result[4]
            scale_layers += result[5]

    catalog3 = [(), (Q(1, 3),), (Q(1, 2),)]
    cells3 = [(i, j) for i in range(3) for j in range(3)]
    for assignment in product(catalog3, repeat=9):
        result = initial_multiple_sample(3, branches_from_assignment(cells3, assignment))
        if result is not None:
            eligible += 1
            recursive_checks += result[4]
            scale_layers += result[5]
    return eligible, recursive_checks, scale_layers


def characteristic_expansion_from_branches(branches: tuple[Branch, ...]):
    data = red.global_strict_gauge(2, branches)
    gauge, _, _, _, records, _, _, _ = data
    levels, layers = win.levels_layers(2, records)
    return rsp.determinant_exponential_expansion(levels, layers)


def targeted_common_shift_regression():
    eligible = checks = irrational_scales = 0
    a_values = (Q(1, 2), Q(2, 5), Q(1, 3))
    lower = (Q(1, 3), Q(1, 4), Q(1, 5), Q(1, 6), Q(1, 7))
    for a, b, c in product(a_values, lower, lower):
        if not (b < a and c < a):
            continue
        branches = (
            (0, 0, Q(1)), (0, 0, a),
            (1, 1, Q(1)), (1, 1, a),
            (0, 1, b), (1, 0, c),
        )
        expansion = characteristic_expansion_from_branches(branches)
        original = rational_jet(expansion)
        first = newton_step(original, Q(1), 2)
        if first is None:
            continue
        theta1, jet1, edge1, c1 = first
        if theta1 != scale_from_rational(a) or edge1 != (Q(1), Q(2), Q(1)):
            continue
        second = newton_step(jet1, Q(-1), 2)
        if second is None:
            continue
        theta2, jet2, _, c2 = second
        direct = direct_two_step(original, Q(1), 2, theta1, Q(-1), 2, theta2)
        assert jet2 == direct
        eligible += 1
        checks += c1 + c2 + len(jet2)
        if any(exponent.denominator > 1 for _, exponent in theta2):
            irrational_scales += 1
    assert eligible > 0
    assert irrational_scales > 0
    return eligible, checks, irrational_scales


def two_step_radical_witness():
    a, b, c = Q(1, 2), Q(1, 3), Q(1, 5)
    branches = (
        (0, 0, Q(1)), (0, 0, a),
        (1, 1, Q(1)), (1, 1, a),
        (0, 1, b), (1, 0, c),
    )
    expansion = characteristic_expansion_from_branches(branches)
    original = rational_jet(expansion)
    first = newton_step(original, Q(1), 2)
    assert first is not None
    theta1, jet1, edge1, _ = first
    assert theta1 == scale_from_rational(a)
    assert edge1 == (Q(1), Q(2), Q(1))
    second = newton_step(jet1, Q(-1), 2)
    assert second is not None
    theta2, jet2, edge2, _ = second
    expected = scale_mul(scale_root(scale_from_rational(b * c), 2), scale_pow(scale_from_rational(a), -1))
    assert theta2 == expected
    assert dict(theta2) == {2: Q(1), 3: Q(-1, 2), 5: Q(-1, 2)}
    assert edge2 == (Q(-1), Q(0), Q(1))
    assert jet2 == direct_two_step(original, Q(1), 2, theta1, Q(-1), 2, theta2)
    return 7


def three_step_witness():
    a, b, c, d = Q(1, 2), Q(1, 3), Q(3, 10), Q(1, 4)
    branches = (
        (0, 0, Q(1)), (0, 0, a), (0, 0, b),
        (1, 1, Q(1)), (1, 1, a), (1, 1, b),
        (0, 1, c), (1, 0, d),
    )
    jet0 = rational_jet(characteristic_expansion_from_branches(branches))
    step1 = newton_step(jet0, Q(1), 2)
    assert step1 is not None
    theta1, jet1, edge1, _ = step1
    assert theta1 == scale_from_rational(a) and edge1 == (Q(1), Q(2), Q(1))
    step2 = newton_step(jet1, Q(-1), 2)
    assert step2 is not None
    theta2, jet2, edge2, _ = step2
    assert theta2 == scale_from_rational(b / a) and edge2 == (Q(1), Q(2), Q(1))
    step3 = newton_step(jet2, Q(-1), 2)
    assert step3 is not None
    theta3, _, edge3, _ = step3
    expected3 = scale_mul(scale_root(scale_from_rational(c * d), 2), scale_pow(scale_from_rational(b), -1))
    assert theta3 == expected3 and edge3 == (Q(-1), Q(0), Q(1))
    return 7


def scale_algebra_checks():
    half = scale_from_rational(Q(1, 2))
    third = scale_from_rational(Q(1, 3))
    radical = scale_root(scale_mul(half, third), 2)
    assert dict(radical) == {2: Q(-1, 2), 3: Q(-1, 2)}
    assert scale_compare(radical, half) < 0
    assert scale_compare(scale_root(scale_from_rational(Q(1, 3)), 2), half) > 0
    assert scale_compare(half, scale_root(scale_from_rational(Q(1, 3)), 2)) < 0
    assert scale_pow(scale_root(scale_from_rational(Q(2, 15)), 3), 3) == scale_from_rational(Q(2, 15))
    return 5


def main() -> int:
    old_eligible, old_recursive, old_layers = exhaustive_second_edge_regression()
    targeted, targeted_checks, irrational = targeted_common_shift_regression()
    radical = two_step_radical_witness()
    third = three_step_witness()
    scale_checks = scale_algebra_checks()
    assert old_eligible == 0  # informative negative census for the old coarse catalog
    print("BRC rational-root Newton recursion checker: PASS")
    print(f"old_catalog_second_edge_eligible_samples={old_eligible}")
    print(f"old_catalog_recursive_checks={old_recursive}")
    print(f"old_catalog_second_residual_scale_layers={old_layers}")
    print(f"targeted_common_shift_eligible_samples={targeted}")
    print(f"targeted_recursive_vs_direct_checks={targeted_checks}")
    print(f"targeted_irrational_scale_samples={irrational}")
    print(f"radical_second_edge_checks={radical}")
    print(f"three_step_recursive_checks={third}")
    print(f"rational_valuation_scale_checks={scale_checks}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
