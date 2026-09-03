#!/usr/bin/env python3
"""Exact checker for selected-root evaluation algebra Newton recursion."""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import product
from math import comb

import brc_critical_ratio_spectral_response_check as rsp
import brc_multiple_root_first_newton_edge_check as ne
import brc_rational_root_newton_recursion_check as rr
import brc_unique_winner_root_active_characteristic_jet_check as win
from enterprise_math import brc_critical_degeneracy as cd

Q = Fraction
Poly = tuple[Fraction, ...]
Scale = rr.Scale
EvalPoly = tuple[Poly, ...]
EvalJet = dict[Scale, EvalPoly]
ONE: Scale = ()


def trim(poly: Poly) -> Poly:
    values = list(poly)
    while len(values) > 1 and values[-1] == 0:
        values.pop()
    return tuple(values) if values else (Q(0),)


def p_add(a: Poly, b: Poly) -> Poly:
    n = max(len(a), len(b))
    return trim(tuple((a[i] if i < len(a) else Q(0)) + (b[i] if i < len(b) else Q(0)) for i in range(n)))


def p_scale(poly: Poly, scalar: Fraction) -> Poly:
    return trim(tuple(scalar * value for value in poly))


def p_mul(a: Poly, b: Poly) -> Poly:
    out = [Q(0) for _ in range(len(a) + len(b) - 1)]
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return trim(tuple(out))


def p_eval(poly: Poly, value: Fraction) -> Fraction:
    out = Q(0)
    for coefficient in reversed(poly):
        out = out * value + coefficient
    return out


def p_derivative(poly: Poly) -> Poly:
    if len(poly) <= 1:
        return (Q(0),)
    return trim(tuple(Q(i) * poly[i] for i in range(1, len(poly))))


def p_derivative_n(poly: Poly, order: int) -> Poly:
    out = poly
    for _ in range(order):
        out = p_derivative(out)
    return out


@dataclass(frozen=True)
class RootEvalState:
    p0_int: tuple[int, ...]
    selector: cd.CriticalRootSelector

    @property
    def p0(self) -> Poly:
        return tuple(Q(value) for value in self.p0_int)

    def zero(self, poly: Poly) -> bool:
        return win.vanishes_at_selector(self.p0, trim(poly), self.selector)

    def equal(self, left: Poly, right: Poly) -> bool:
        return self.zero(p_add(left, p_scale(right, Q(-1))))

    def sign(self, poly: Poly) -> int:
        poly = trim(poly)
        if self.zero(poly):
            return 0
        if self.selector.is_rational:
            assert self.selector.exact_root is not None
            value = p_eval(poly, self.selector.exact_root)
            return (value > 0) - (value < 0)
        for power in range(10, 36):
            selector = cd.smallest_positive_root_selector(self.p0_int, max_width=Q(1, 2**power))
            seq = cd._sturm_sequence(poly)
            if cd._root_count(seq, selector.lower, selector.upper) == 0:
                midpoint = (selector.lower + selector.upper) / 2
                value = p_eval(poly, midpoint)
                assert value != 0
                return (value > 0) - (value < 0)
        raise AssertionError("could not determine selected-root coefficient sign")


def evalpoly_trim(poly: EvalPoly, root: RootEvalState) -> EvalPoly:
    values = list(poly)
    while len(values) > 1 and root.zero(values[-1]):
        values.pop()
    return tuple(values) if values else ((Q(0),),)


def evalpoly_derivative(poly: EvalPoly, root: RootEvalState) -> EvalPoly:
    if len(poly) <= 1:
        return ((Q(0),),)
    return evalpoly_trim(tuple(p_scale(poly[i], Q(i)) for i in range(1, len(poly))), root)


def evalpoly_at_rational(poly: EvalPoly, value: Fraction) -> Poly:
    out: Poly = (Q(0),)
    for coefficient in reversed(poly):
        out = p_add(p_scale(out, value), coefficient)
    return out


def evalpoly_vanish_order(poly: EvalPoly, value: Fraction, root: RootEvalState) -> int:
    current = poly
    order = 0
    while root.zero(evalpoly_at_rational(current, value)):
        current = evalpoly_derivative(current, root)
        order += 1
        if current == ((Q(0),),):
            return 10**6
    return order


def factorial(value: int) -> int:
    out = 1
    for k in range(2, value + 1):
        out *= k
    return out


def taylor_eval_coeff(poly: Poly, order: int) -> Poly:
    return p_scale(p_derivative_n(poly, order), Q(1, factorial(order)))


def add_eval_coeff(raw: dict[Scale, list[Poly]], scale: Scale, order: int, coefficient: Poly) -> None:
    if coefficient == (Q(0),):
        return
    values = raw.setdefault(scale, [])
    while len(values) <= order:
        values.append((Q(0),))
    values[order] = p_add(values[order], coefficient)


def freeze_eval_jet(raw: dict[Scale, list[Poly]], root: RootEvalState) -> EvalJet:
    out: EvalJet = {}
    for scale, coefficients in raw.items():
        normalized = evalpoly_trim(tuple(coefficients), root)
        if not all(root.zero(value) for value in normalized):
            out[scale] = normalized
    return out


def algebraic_base_first_step(expansion: dict[Fraction, Poly], root: RootEvalState):
    p0 = root.p0
    r = ne.vanish_order(p0, p0, root.selector)
    assert r >= 2
    candidates: list[Scale] = []
    contacts: dict[Fraction, int] = {}
    for base, poly in expansion.items():
        if base == 1:
            continue
        q = ne.vanish_order(p0, poly, root.selector)
        contacts[base] = q
        if q < r:
            candidates.append(rr.scale_root(rr.scale_from_rational(base), r - q))
    if not candidates:
        return None
    theta = rr.scale_max(candidates)
    raw: dict[Scale, list[Poly]] = {}
    checks = 0
    for base, poly in expansion.items():
        sigma = rr.scale_from_rational(base)
        for k in range(len(poly)):
            coefficient = taylor_eval_coeff(poly, k)
            if root.zero(coefficient):
                continue
            residual = rr.scale_mul(sigma, rr.scale_pow(theta, k - r))
            assert rr.scale_compare(residual, ONE) <= 0
            add_eval_coeff(raw, residual, k, coefficient)
            checks += 1
    jet = freeze_eval_jet(raw, root)
    assert ONE in jet
    return r, theta, jet, jet[ONE], contacts, checks


def eval_newton_step(jet: EvalJet, root_value: Fraction, multiplicity: int, root: RootEvalState):
    assert evalpoly_vanish_order(jet[ONE], root_value, root) == multiplicity
    candidates: list[Scale] = []
    for scale, poly in jet.items():
        if scale == ONE:
            continue
        q = evalpoly_vanish_order(poly, root_value, root)
        if q < multiplicity:
            candidates.append(rr.scale_root(scale, multiplicity - q))
    if not candidates:
        return None
    theta = rr.scale_max(candidates)
    raw: dict[Scale, list[Poly]] = {}
    checks = 0
    for scale, poly in jet.items():
        current = poly
        for k in range(len(poly)):
            coefficient = evalpoly_at_rational(current, root_value)
            if k > 0:
                coefficient = p_scale(coefficient, Q(1, factorial(k)))
            if not root.zero(coefficient):
                residual = rr.scale_mul(scale, rr.scale_pow(theta, k - multiplicity))
                assert rr.scale_compare(residual, ONE) <= 0
                add_eval_coeff(raw, residual, k, coefficient)
                checks += 1
            current = evalpoly_derivative(current, root)
    output = freeze_eval_jet(raw, root)
    assert ONE in output
    return theta, output, output[ONE], checks


def direct_two_step(expansion: dict[Fraction, Poly], root: RootEvalState, r1: int, theta1: Scale, y0: Fraction, r2: int, theta2: Scale):
    raw: dict[Scale, list[Poly]] = {}
    for base, poly in expansion.items():
        sigma = rr.scale_from_rational(base)
        for k in range(len(poly)):
            coefficient = taylor_eval_coeff(poly, k)
            if root.zero(coefficient):
                continue
            for j in range(k + 1):
                value = p_scale(coefficient, Q(comb(k, j)) * y0 ** (k - j))
                if root.zero(value):
                    continue
                residual = rr.scale_mul(sigma, rr.scale_mul(rr.scale_pow(theta1, k - r1), rr.scale_pow(theta2, j - r2)))
                add_eval_coeff(raw, residual, j, value)
    return freeze_eval_jet(raw, root)


def jets_semantically_equal(left: EvalJet, right: EvalJet, root: RootEvalState) -> bool:
    if set(left) != set(right):
        return False
    for scale in left:
        a, b = left[scale], right[scale]
        n = max(len(a), len(b))
        for index in range(n):
            x = a[index] if index < len(a) else (Q(0),)
            y = b[index] if index < len(b) else (Q(0),)
            if not root.equal(x, y):
                return False
    return True


def matmul2(a):
    return (
        (a[0][0] * a[0][0] + a[0][1] * a[1][0], a[0][0] * a[0][1] + a[0][1] * a[1][1]),
        (a[1][0] * a[0][0] + a[1][1] * a[1][0], a[1][0] * a[0][1] + a[1][1] * a[1][1]),
    )


def blockdiag(a, b):
    return (
        (a[0][0], a[0][1], 0, 0),
        (a[1][0], a[1][1], 0, 0),
        (0, 0, b[0][0], b[0][1]),
        (0, 0, b[1][0], b[1][1]),
    )


def offdiag_blocks(c):
    return (
        (0, 0, c[0][0], c[0][1]),
        (0, 0, c[1][0], c[1][1]),
        (c[0][0], c[0][1], 0, 0),
        (c[1][0], c[1][1], 0, 0),
    )


def expansion_for_B(B, levels):
    C = matmul2(B)
    K = blockdiag(B, B)
    layers = [K]
    for kind in levels[1:]:
        layers.append(blockdiag(C, C) if kind[1] == "diag" else offdiag_blocks(C))
    numeric_levels = tuple(level[0] for level in levels)
    return K, rsp.determinant_exponential_expansion(numeric_levels, tuple(layers))


def is_irreducible_B(B) -> bool:
    return B[0][1] > 0 and B[1][0] > 0


def systematic_two_edge_census():
    eta, tau = Q(1, 2), Q(1, 3)
    samples = first_checks = second_checks = semantic_checks = sign_checks = 0
    for a, b, c, d in product(range(3), repeat=4):
        B = ((a, b), (c, d))
        if not is_irreducible_B(B):
            continue
        K, expansion = expansion_for_B(B, ((Q(1), "base"), (eta, "diag"), (tau, "off")))
        p0_int = cd.criticality_polynomial(K)
        selector = cd.smallest_positive_root_selector(p0_int)
        if selector.is_rational:
            continue
        root = RootEvalState(p0_int, selector)
        first = algebraic_base_first_step(expansion, root)
        assert first is not None
        r1, theta1, jet1, edge1, _, c1 = first
        assert r1 == 2
        assert theta1 == rr.scale_from_rational(eta)
        assert evalpoly_vanish_order(edge1, Q(-1), root) == 2
        first_checks += c1 + 3

        second = eval_newton_step(jet1, Q(-1), 2, root)
        assert second is not None
        theta2, jet2, edge2, c2 = second
        assert theta2 == rr.scale_from_rational(tau / eta)
        assert evalpoly_vanish_order(edge2, Q(-1), root) == 1
        direct = direct_two_step(expansion, root, 2, theta1, Q(-1), 2, theta2)
        assert jets_semantically_equal(jet2, direct, root)
        second_checks += c2 + 4
        semantic_checks += sum(len(poly) for poly in jet2.values())

        x = (Q(0), Q(1))
        one = (Q(1),)
        assert root.sign(x) > 0
        assert root.sign(p_add(one, p_scale(x, Q(-1)))) != 0
        assert root.zero(root.p0)
        assert root.equal(p_mul(root.p0, x), (Q(0),))
        sign_checks += 4
        samples += 1
    assert samples > 0
    return samples, first_checks, second_checks, semantic_checks, sign_checks


def three_edge_family_census():
    eta1, eta2, tau = Q(1, 2), Q(2, 5), Q(1, 3)
    samples = checks = 0
    for a, b, c, d in product(range(3), repeat=4):
        B = ((a, b), (c, d))
        if not is_irreducible_B(B):
            continue
        K, expansion = expansion_for_B(B, ((Q(1), "base"), (eta1, "diag"), (eta2, "diag"), (tau, "off")))
        p0_int = cd.criticality_polynomial(K)
        selector = cd.smallest_positive_root_selector(p0_int)
        if selector.is_rational:
            continue
        root = RootEvalState(p0_int, selector)
        first = algebraic_base_first_step(expansion, root)
        assert first is not None
        _, theta1, jet1, edge1, _, _ = first
        assert theta1 == rr.scale_from_rational(eta1)
        assert evalpoly_vanish_order(edge1, Q(-1), root) == 2
        second = eval_newton_step(jet1, Q(-1), 2, root)
        assert second is not None
        theta2, jet2, edge2, _ = second
        assert theta2 == rr.scale_from_rational(eta2 / eta1)
        assert evalpoly_vanish_order(edge2, Q(-1), root) == 2
        third = eval_newton_step(jet2, Q(-1), 2, root)
        assert third is not None
        theta3, _, edge3, _ = third
        assert theta3 == rr.scale_from_rational(tau / eta2)
        assert evalpoly_vanish_order(edge3, Q(-1), root) == 1
        samples += 1
        checks += 8
    assert samples > 0
    return samples, checks


def golden_block_witness():
    B = ((1, 1), (1, 0))
    eta, tau = Q(1, 2), Q(1, 3)
    K, expansion = expansion_for_B(B, ((Q(1), "base"), (eta, "diag"), (tau, "off")))
    p0_int = cd.criticality_polynomial(K)
    selector = cd.smallest_positive_root_selector(p0_int)
    assert not selector.is_rational
    root = RootEvalState(p0_int, selector)
    first = algebraic_base_first_step(expansion, root)
    assert first is not None
    _, theta1, jet1, edge1, _, _ = first
    assert theta1 == rr.scale_from_rational(eta)
    assert evalpoly_vanish_order(edge1, Q(-1), root) == 2
    second = eval_newton_step(jet1, Q(-1), 2, root)
    assert second is not None
    theta2, jet2, edge2, _ = second
    assert theta2 == rr.scale_from_rational(tau / eta)
    assert evalpoly_vanish_order(edge2, Q(-1), root) == 1
    assert jets_semantically_equal(jet2, direct_two_step(expansion, root, 2, theta1, Q(-1), 2, theta2), root)
    return 7


def main() -> int:
    samples, first, second, semantic, signs = systematic_two_edge_census()
    three_samples, three_checks = three_edge_family_census()
    golden = golden_block_witness()
    print("BRC selected-root evaluation algebra checker: PASS")
    print(f"irrational_base_block_samples={samples}")
    print(f"algebraic_first_edge_checks={first}")
    print(f"algebraic_second_edge_checks={second}")
    print(f"semantic_recursive_direct_coefficient_checks={semantic}")
    print(f"selected_root_zero_sign_checks={signs}")
    print(f"three_edge_irrational_base_samples={three_samples}")
    print(f"three_edge_recursive_checks={three_checks}")
    print(f"golden_block_checks={golden}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
