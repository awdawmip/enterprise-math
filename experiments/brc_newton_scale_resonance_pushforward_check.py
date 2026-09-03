#!/usr/bin/env python3
"""Exact checker for Newton-scale resonance as an affine valuation pushforward."""
from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from itertools import product
from math import comb, factorial

import brc_single_generator_root_handoff_check as handoff
from enterprise_math.brc_newton_recursion import RationalValuationScale, rational_newton_step

Q = Fraction
Poly = tuple[Fraction, ...]
Scale = RationalValuationScale
ONE = RationalValuationScale.one()


def trim(poly) -> Poly:
    values = [Q(value) for value in poly]
    if not values:
        return (Q(0),)
    while len(values) > 1 and values[-1] == 0:
        values.pop()
    return tuple(values)


def peval(poly: Poly, value: Fraction) -> Fraction:
    out = Q(0)
    for coefficient in reversed(poly):
        out = out * value + coefficient
    return out


def derivative(poly: Poly) -> Poly:
    if len(poly) <= 1:
        return (Q(0),)
    return trim(tuple(Q(i) * poly[i] for i in range(1, len(poly))))


def derivative_n(poly: Poly, order: int) -> Poly:
    out = poly
    for _ in range(order):
        out = derivative(out)
    return out


def taylor_coefficient(poly: Poly, root: Fraction, order: int) -> Fraction:
    return peval(derivative_n(poly, order), root) / Q(factorial(order))


def vanish_order(poly: Poly, root: Fraction) -> int:
    current = trim(poly)
    order = 0
    while peval(current, root) == 0:
        current = derivative(current)
        order += 1
        if current == (Q(0),):
            return 10**9
    return order


def scale_from(value) -> Scale:
    return Scale.from_rational(Q(value))


def scale_equal(left: Scale, right: Scale) -> bool:
    return left.compare(right) == 0


def scale_max(scales: list[Scale]) -> Scale:
    best = scales[0]
    for scale in scales[1:]:
        if scale.compare(best) > 0:
            best = scale
    return best


def normalize_jet(jet):
    out = {}
    for scale, poly in jet:
        poly = trim(poly)
        if scale in out:
            old = out[scale]
            n = max(len(old), len(poly))
            merged = tuple(
                (old[i] if i < len(old) else Q(0)) + (poly[i] if i < len(poly) else Q(0))
                for i in range(n)
            )
            out[scale] = trim(merged)
        else:
            out[scale] = poly
    return {scale: poly for scale, poly in out.items() if any(poly)}


def candidate_scale(jet, root: Fraction, multiplicity: int) -> Scale:
    candidates = []
    for scale, poly in jet:
        if scale == ONE:
            continue
        q = vanish_order(trim(poly), root)
        if q < multiplicity:
            candidates.append(scale.root(multiplicity - q))
    if not candidates:
        raise ValueError("no strict Newton candidate")
    return scale_max(candidates)


def independent_pushforward(jet, root: Fraction, multiplicity: int, theta: Scale):
    raw: dict[Scale, list[Fraction]] = {}
    sources: dict[Scale, list[tuple[Scale, int, Fraction]]] = defaultdict(list)
    atom_checks = 0
    for scale, poly_raw in jet:
        poly = trim(poly_raw)
        for order in range(len(poly)):
            coefficient = taylor_coefficient(poly, root, order)
            if coefficient == 0:
                continue
            residual = scale.multiply(theta.power(order - multiplicity))
            assert residual.compare(ONE) <= 0
            values = raw.setdefault(residual, [])
            while len(values) <= order:
                values.append(Q(0))
            values[order] += coefficient
            sources[residual].append((scale, order, coefficient))
            atom_checks += 1
    frozen = {
        scale: trim(tuple(values))
        for scale, values in raw.items()
        if any(values)
    }
    return frozen, sources, atom_checks


def production_map(step):
    return {scale: trim(poly) for scale, poly in step.jet}


def resonance_criterion_checks(theta: Scale, sources) -> tuple[int, int]:
    resonance_fibers = criterion_checks = 0
    for residual, atoms in sources.items():
        distinct = {(atom[0], atom[1]) for atom in atoms}
        if len(distinct) <= 1:
            continue
        resonance_fibers += 1
        items = list(distinct)
        for i in range(len(items)):
            for j in range(i + 1, len(items)):
                scale1, k1 = items[i]
                scale2, k2 = items[j]
                left = scale1.multiply(scale2.power(-1))
                right = theta.power(k2 - k1)
                assert scale_equal(left, right)
                assert scale_equal(
                    scale1.multiply(theta.power(k1)),
                    scale2.multiply(theta.power(k2)),
                )
                criterion_checks += 2
    return resonance_fibers, criterion_checks


def synthetic_exhaustive_regression():
    base = (Q(1), Q(-2), Q(1))
    root = Q(1)
    scales = [Q(1, 2), Q(1, 3), Q(1, 4), Q(1, 6), Q(1, 8), Q(1, 9)]
    polynomials = [
        (Q(1),),
        (Q(-1),),
        (Q(-1), Q(1)),
        (Q(-2), Q(2)),
    ]
    samples = pushforward_checks = atom_checks = resonance_fibers = criterion_checks = edge_checks = order_checks = 0
    for (s1, s2), (p1, p2) in product(product(scales, repeat=2), product(polynomials, repeat=2)):
        jet = (
            (ONE, base),
            (scale_from(s1), p1),
            (scale_from(s2), p2),
        )
        try:
            theta = candidate_scale(jet, root, 2)
            step = rational_newton_step(jet, root, 2)
        except ValueError:
            continue
        assert scale_equal(theta, step.scale)
        pushed, sources, atoms = independent_pushforward(jet, root, 2, theta)
        assert pushed == production_map(step)
        assert pushed[ONE] == trim(step.edge_polynomial)
        pushforward_checks += len(pushed) + 2
        atom_checks += atoms
        rf, cc = resonance_criterion_checks(theta, sources)
        resonance_fibers += rf
        criterion_checks += cc

        reversed_step = rational_newton_step(tuple(reversed(jet)), root, 2)
        assert scale_equal(reversed_step.scale, step.scale)
        assert production_map(reversed_step) == production_map(step)
        order_checks += 2
        edge_checks += 1
        samples += 1
    return samples, pushforward_checks, atom_checks, resonance_fibers, criterion_checks, edge_checks, order_checks


def canonical_resonant_edge_witness():
    jet = (
        (ONE, (Q(1), Q(-2), Q(1))),
        (scale_from(Q(1, 2)), (Q(-1), Q(1))),
        (scale_from(Q(1, 4)), (Q(-1),)),
    )
    step = rational_newton_step(jet, Q(1), 2)
    assert step.scale == scale_from(Q(1, 2))
    assert trim(step.edge_polynomial) == (Q(-1), Q(1), Q(1))
    pushed, sources, _ = independent_pushforward(jet, Q(1), 2, step.scale)
    assert pushed[ONE] == (Q(-1), Q(1), Q(1))
    assert len({(scale, k) for scale, k, _ in sources[ONE]}) == 3
    rf, cc = resonance_criterion_checks(step.scale, sources)
    assert rf >= 1 and cc >= 6
    return 6 + cc


def cancellation_after_aggregation_witness():
    jet = (
        (ONE, (Q(1), Q(-2), Q(1))),
        (scale_from(Q(1, 4)), (Q(1),)),
        (scale_from(Q(1, 4)), (Q(-1),)),
    )
    step = rational_newton_step(jet, Q(1), 2)
    assert step.scale == scale_from(Q(1, 2))
    assert trim(step.edge_polynomial) == (Q(0), Q(0), Q(1))
    pushed, sources, _ = independent_pushforward(jet, Q(1), 2, step.scale)
    assert pushed[ONE] == (Q(0), Q(0), Q(1))
    assert len(sources[ONE]) == 3
    return 5


def direct_two_step(original, root1, mult1, theta1, root2, mult2, theta2):
    raw: dict[Scale, list[Fraction]] = {}
    for scale, poly_raw in original:
        poly = trim(poly_raw)
        for k in range(len(poly)):
            coefficient = taylor_coefficient(poly, root1, k)
            if coefficient == 0:
                continue
            for j in range(k + 1):
                value = coefficient * Q(comb(k, j)) * (root2 ** (k - j))
                if value == 0:
                    continue
                residual = scale.multiply(theta1.power(k - mult1)).multiply(theta2.power(j - mult2))
                values = raw.setdefault(residual, [])
                while len(values) <= j:
                    values.append(Q(0))
                values[j] += value
    return {
        scale: trim(tuple(values))
        for scale, values in raw.items()
        if any(values)
    }


def staged_composition_checks():
    original = (
        (ONE, (Q(1), Q(-2), Q(1))),
        (scale_from(Q(1, 2)), (Q(-2), Q(2))),
        (scale_from(Q(1, 4)), (Q(1),)),
        (scale_from(Q(1, 9)), (Q(-1),)),
    )
    step1 = rational_newton_step(original, Q(1), 2)
    assert step1.edge_polynomial == (Q(1), Q(2), Q(1))
    step2 = rational_newton_step(step1.jet, Q(-1), 2)
    staged = production_map(step2)
    direct = direct_two_step(original, Q(1), 2, step1.scale, Q(-1), 2, step2.scale)
    assert staged == direct
    return len(staged) + 3


def handoff_resonance_witness():
    b = ((1, 1), (1, 0))
    eta, tau1 = Q(1, 2), Q(1, 3)
    K = handoff.mat_identity(4)
    L = handoff.block_diag_b(b)

    def run(tau2: Fraction):
        expansion = handoff.rsp.determinant_exponential_expansion(
            (Q(1), eta, tau1, tau2),
            (K, L, K, K),
        )
        original = handoff.rr.rational_jet(expansion)
        first = handoff.rr.newton_step(original, Q(1), 4)
        assert first is not None
        _, jet1, edge1, _ = first
        state = handoff.RealRootEvalState(handoff.smallest_real_root_selector(edge1))
        assert handoff.vanish_order(edge1, state) == 2
        second = handoff.handoff_step(jet1, state, 2)
        assert second is not None
        theta2, jet2, edge2, _ = second
        assert theta2 == handoff.rr.scale_from_rational(tau1 / eta)
        assert handoff.evalpoly_vanish_order(edge2, Q(-1), state) == 2
        third = handoff.rational_eval_step(jet2, Q(-1), 2, state)
        assert third is not None
        return state, third

    common_res = handoff.rr.scale_from_rational(Q(1, 4) / tau1)
    intrinsic = handoff.rr.scale_from_rational((eta * eta) / tau1)
    assert handoff.rr.scale_compare(common_res, intrinsic) == 0
    state_r, third_r = run(Q(1, 4))
    theta_r, _, edge_r, _ = third_r
    assert theta_r == common_res
    assert handoff.evalpoly_vanish_order(edge_r, Q(-1), state_r) != 2

    common_sep = handoff.rr.scale_from_rational(Q(3, 10) / tau1)
    assert handoff.rr.scale_compare(common_sep, intrinsic) > 0
    state_s, third_s = run(Q(3, 10))
    theta_s, _, edge_s, _ = third_s
    assert theta_s == common_sep
    assert handoff.evalpoly_vanish_order(edge_s, Q(-1), state_s) == 2
    return 7


def main() -> int:
    samples, push, atoms, fibers, criterion, edges, order = synthetic_exhaustive_regression()
    resonant = canonical_resonant_edge_witness()
    cancellation = cancellation_after_aggregation_witness()
    composition = staged_composition_checks()
    handoff_checks = handoff_resonance_witness()
    assert samples > 100
    assert fibers > 0
    print("BRC Newton scale resonance pushforward checker: PASS")
    print(f"synthetic_newton_samples={samples}")
    print(f"pushforward_production_checks={push}")
    print(f"taylor_atom_checks={atoms}")
    print(f"resonant_scale_fibers={fibers}")
    print(f"valuation_resonance_criterion_checks={criterion}")
    print(f"scale_one_edge_checks={edges}")
    print(f"source_order_invariance_checks={order}")
    print(f"canonical_resonant_edge_checks={resonant}")
    print(f"aggregation_cancellation_checks={cancellation}")
    print(f"staged_one_shot_composition_checks={composition}")
    print(f"handoff_resonance_separation_checks={handoff_checks}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
