#!/usr/bin/env python3
"""Exact checker for single-generator irrational translated-root handoff."""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import product
from math import comb, factorial, isqrt

import brc_critical_ratio_spectral_response_check as rsp
import brc_rational_root_newton_recursion_check as rr
import brc_selected_root_evaluation_algebra_check as alg
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


def padd(a: Poly, b: Poly) -> Poly:
    n = max(len(a), len(b))
    return trim(tuple((a[i] if i < len(a) else Q(0)) + (b[i] if i < len(b) else Q(0)) for i in range(n)))


def pscale(poly: Poly, scalar: Fraction) -> Poly:
    return trim(tuple(scalar * c for c in poly))


def pmul(a: Poly, b: Poly) -> Poly:
    out = [Q(0) for _ in range(len(a) + len(b) - 1)]
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return trim(tuple(out))


def peval(poly: Poly, x: Fraction) -> Fraction:
    out = Q(0)
    for c in reversed(poly):
        out = out * x + c
    return out


def derivative(poly: Poly) -> Poly:
    if len(poly) <= 1:
        return (Q(0),)
    return trim(tuple(Q(i) * poly[i] for i in range(1, len(poly))))


def derivative_n(poly: Poly, n: int) -> Poly:
    out = poly
    for _ in range(n):
        out = derivative(out)
    return out


def taylor_rep(poly: Poly, order: int) -> Poly:
    return pscale(derivative_n(poly, order), Q(1, factorial(order)))


def cauchy_bound(poly: Poly) -> Fraction:
    poly = trim(poly)
    if len(poly) <= 1 or poly[-1] == 0:
        raise ValueError("nonconstant polynomial required")
    leading = abs(poly[-1])
    return Q(1) + max((abs(c) / leading for c in poly[:-1]), default=Q(0))


@dataclass(frozen=True)
class RealRootSelector:
    polynomial: Poly
    lower: Fraction
    upper: Fraction
    selector: str = "SMALLEST_REAL_ROOT"

    def verify(self) -> bool:
        poly = trim(self.polynomial)
        if not self.lower < self.upper:
            return False
        if peval(poly, self.lower) == 0 or peval(poly, self.upper) == 0:
            return False
        seq = cd._sturm_sequence(poly)
        if cd._root_count(seq, self.lower, self.upper) != 1:
            return False
        bound = cauchy_bound(poly) + 1
        return cd._root_count(seq, -bound, self.lower) == 0


def smallest_real_root_selector(poly: Poly, *, max_width: Fraction = Q(1, 4096)) -> RealRootSelector:
    poly = trim(poly)
    if len(poly) <= 1:
        raise ValueError("nonconstant polynomial required")
    bound = cauchy_bound(poly) + 1
    while peval(poly, -bound) == 0 or peval(poly, bound) == 0:
        bound += 1
    seq = cd._sturm_sequence(poly)
    if cd._root_count(seq, -bound, bound) <= 0:
        raise ValueError("polynomial has no real root")
    left, right = -bound, bound
    for _ in range(4096):
        count = cd._root_count(seq, left, right)
        if count == 1 and right - left <= max_width and cd._root_count(seq, -bound, left) == 0:
            out = RealRootSelector(poly, left, right)
            assert out.verify()
            return out
        midpoint = (left + right) / 2
        if peval(poly, midpoint) == 0:
            # This research selector is used only for irrational handoff roots.
            raise AssertionError("handoff selector unexpectedly hit a rational root")
        if cd._root_count(seq, left, midpoint) > 0:
            right = midpoint
        else:
            left = midpoint
    raise AssertionError("smallest-real-root isolation did not converge")


@dataclass(frozen=True)
class RealRootEvalState:
    selector: RealRootSelector

    @property
    def polynomial(self) -> Poly:
        return self.selector.polynomial

    def zero(self, poly: Poly) -> bool:
        poly = trim(poly)
        if poly == (Q(0),):
            return True
        gcd = cd._p_gcd(self.polynomial, poly)
        if len(gcd) <= 1:
            return False
        seq = cd._sturm_sequence(gcd)
        return cd._root_count(seq, self.selector.lower, self.selector.upper) > 0

    def equal(self, a: Poly, b: Poly) -> bool:
        return self.zero(padd(a, pscale(b, Q(-1))))

    def sign(self, poly: Poly) -> int:
        poly = trim(poly)
        if self.zero(poly):
            return 0
        for power in range(12, 56):
            selector = smallest_real_root_selector(self.polynomial, max_width=Q(1, 2**power))
            seq = cd._sturm_sequence(poly)
            if cd._root_count(seq, selector.lower, selector.upper) == 0:
                value = peval(poly, (selector.lower + selector.upper) / 2)
                assert value != 0
                return (value > 0) - (value < 0)
        raise AssertionError("could not determine selected-root sign")


def vanish_order(poly: Poly, state: RealRootEvalState) -> int:
    current = trim(poly)
    order = 0
    while state.zero(current):
        current = derivative(current)
        order += 1
        if current == (Q(0),):
            return 10**9
    return order


def evalpoly_trim(poly: EvalPoly, state: RealRootEvalState) -> EvalPoly:
    values = list(poly)
    while len(values) > 1 and state.zero(values[-1]):
        values.pop()
    return tuple(values) if values else ((Q(0),),)


def evalpoly_derivative(poly: EvalPoly, state: RealRootEvalState) -> EvalPoly:
    if len(poly) <= 1:
        return ((Q(0),),)
    return evalpoly_trim(tuple(pscale(poly[i], Q(i)) for i in range(1, len(poly))), state)


def evalpoly_at_rational(poly: EvalPoly, value: Fraction) -> Poly:
    out: Poly = (Q(0),)
    for coefficient in reversed(poly):
        out = padd(pscale(out, value), coefficient)
    return out


def evalpoly_vanish_order(poly: EvalPoly, value: Fraction, state: RealRootEvalState) -> int:
    current = poly
    order = 0
    while state.zero(evalpoly_at_rational(current, value)):
        current = evalpoly_derivative(current, state)
        order += 1
        if len(current) == 1 and state.zero(current[0]):
            return 10**9
    return order


def add_eval(raw: dict[Scale, list[Poly]], scale: Scale, order: int, coefficient: Poly) -> None:
    if coefficient == (Q(0),):
        return
    values = raw.setdefault(scale, [])
    while len(values) <= order:
        values.append((Q(0),))
    values[order] = padd(values[order], coefficient)


def freeze_eval(raw: dict[Scale, list[Poly]], state: RealRootEvalState) -> EvalJet:
    out: EvalJet = {}
    for scale, coefficients in raw.items():
        poly = evalpoly_trim(tuple(coefficients), state)
        if not all(state.zero(c) for c in poly):
            out[scale] = poly
    return out


def handoff_step(jet: rr.Jet, state: RealRootEvalState, multiplicity: int):
    if vanish_order(jet[ONE], state) != multiplicity:
        raise ValueError("selected irrational root has wrong multiplicity")
    candidates: list[Scale] = []
    for scale, poly in jet.items():
        if scale == ONE:
            continue
        q = vanish_order(poly, state)
        if q < multiplicity:
            candidates.append(rr.scale_root(scale, multiplicity - q))
    if not candidates:
        return None
    theta = rr.scale_max(candidates)
    raw: dict[Scale, list[Poly]] = {}
    checks = 0
    for scale, poly in jet.items():
        for k in range(len(poly)):
            coefficient = taylor_rep(poly, k)
            if state.zero(coefficient):
                continue
            residual = rr.scale_mul(scale, rr.scale_pow(theta, k - multiplicity))
            assert rr.scale_compare(residual, ONE) <= 0
            add_eval(raw, residual, k, coefficient)
            checks += 1
    output = freeze_eval(raw, state)
    assert ONE in output
    return theta, output, output[ONE], checks


def rational_eval_step(jet: EvalJet, root: Fraction, multiplicity: int, state: RealRootEvalState):
    if evalpoly_vanish_order(jet[ONE], root, state) != multiplicity:
        raise ValueError("rational translated root has wrong multiplicity")
    candidates: list[Scale] = []
    for scale, poly in jet.items():
        if scale == ONE:
            continue
        q = evalpoly_vanish_order(poly, root, state)
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
            coefficient = evalpoly_at_rational(current, root)
            if k:
                coefficient = pscale(coefficient, Q(1, factorial(k)))
            if not state.zero(coefficient):
                residual = rr.scale_mul(scale, rr.scale_pow(theta, k - multiplicity))
                assert rr.scale_compare(residual, ONE) <= 0
                add_eval(raw, residual, k, coefficient)
                checks += 1
            current = evalpoly_derivative(current, state)
    output = freeze_eval(raw, state)
    assert ONE in output
    return theta, output, output[ONE], checks


def direct_handoff_two_step(
    original: rr.Jet,
    z0: Fraction,
    r1: int,
    theta1: Scale,
    state: RealRootEvalState,
    r2: int,
    theta2: Scale,
) -> EvalJet:
    raw: dict[Scale, list[Poly]] = {}
    for scale, poly in original.items():
        for k in range(len(poly)):
            c = rr.taylor_coefficient(poly, z0, k)
            if c == 0:
                continue
            for j in range(k + 1):
                # beta^(k-j) is represented by the generator monomial x^(k-j).
                coeff = [Q(0)] * (k - j + 1)
                coeff[k - j] = c * Q(comb(k, j))
                residual = rr.scale_mul(
                    scale,
                    rr.scale_mul(
                        rr.scale_pow(theta1, k - r1),
                        rr.scale_pow(theta2, j - r2),
                    ),
                )
                add_eval(raw, residual, j, tuple(coeff))
    return freeze_eval(raw, state)


def eval_jets_equal(a: EvalJet, b: EvalJet, state: RealRootEvalState) -> bool:
    if set(a) != set(b):
        return False
    for scale in a:
        pa, pb = a[scale], b[scale]
        n = max(len(pa), len(pb))
        for i in range(n):
            ca = pa[i] if i < len(pa) else (Q(0),)
            cb = pb[i] if i < len(pb) else (Q(0),)
            if not state.equal(ca, cb):
                return False
    return True


def mat_identity(n: int):
    return tuple(tuple(1 if i == j else 0 for j in range(n)) for i in range(n))


def block_diag_b(b):
    return (
        (b[0][0], b[0][1], 0, 0),
        (b[1][0], b[1][1], 0, 0),
        (0, 0, b[0][0], b[0][1]),
        (0, 0, b[1][0], b[1][1]),
    )


def p_square(poly: Poly) -> Poly:
    return pmul(poly, poly)


def irrational_b_matrices():
    out = []
    for a, b, c, d in product(range(3), repeat=4):
        if b == 0 or c == 0:
            continue
        disc = (a - d) ** 2 + 4 * b * c
        if isqrt(disc) ** 2 == disc:
            continue
        out.append(((a, b), (c, d)))
    return tuple(out)


def systematic_handoff_regression():
    eta, tau1, tau2 = Q(1, 2), Q(1, 3), Q(1, 4)
    samples = root_checks = recursive_checks = semantic_checks = continuation_checks = 0
    for b in irrational_b_matrices():
        K = mat_identity(4)
        L = block_diag_b(b)
        I = K
        levels = (Q(1), eta, tau1, tau2)
        layers = (K, L, I, I)
        expansion = rsp.determinant_exponential_expansion(levels, layers)
        original = rr.rational_jet(expansion)
        first = rr.newton_step(original, Q(1), 4)
        assert first is not None
        theta1, jet1, edge1, c1 = first
        assert theta1 == rr.scale_from_rational(eta)

        f = (Q(b[0][0] * b[1][1] - b[0][1] * b[1][0]), Q(b[0][0] + b[1][1]), Q(1))
        assert edge1 == p_square(f)
        selector = smallest_real_root_selector(edge1)
        state = RealRootEvalState(selector)
        assert state.sign((Q(0), Q(1))) < 0
        assert state.sign(derivative(f)) < 0
        assert vanish_order(edge1, state) == 2
        root_checks += 4

        second = handoff_step(jet1, state, 2)
        assert second is not None
        theta2, jet2, edge2, c2 = second
        assert theta2 == rr.scale_from_rational(tau1 / eta)
        assert evalpoly_vanish_order(edge2, Q(-1), state) == 2
        recursive_checks += c1 + c2

        direct = direct_handoff_two_step(original, Q(1), 4, theta1, state, 2, theta2)
        assert eval_jets_equal(jet2, direct, state)
        semantic_checks += sum(len(poly) for poly in jet2.values())

        third = rational_eval_step(jet2, Q(-1), 2, state)
        assert third is not None
        theta3, _, edge3, c3 = third
        assert theta3 == rr.scale_from_rational(tau2 / tau1)
        assert evalpoly_vanish_order(edge3, Q(-1), state) == 2
        continuation_checks += c3 + 2
        samples += 1
    return samples, root_checks, recursive_checks, semantic_checks, continuation_checks


def absorption_certificate():
    # alpha is the positive root of 1-x-x^2=0.  beta=-(alpha+1) is the
    # unique negative root of y^2+y-1, hence no second generator is needed.
    root = alg.RootEvalState((1, -1, -1), cd.smallest_positive_root_selector((1, -1, -1)))
    h: Poly = (Q(-1), Q(-1))
    h2 = alg.p_mul(h, h)
    edge_at_h = alg.p_add(alg.p_add(h2, h), (Q(-1),))
    assert root.zero(edge_at_h)
    assert root.sign(h) < 0
    assert root.sign(alg.p_add(h, (Q(1),))) < 0  # beta+1=-alpha<0 -> beta<-1
    # y^2+y-1 has product -1, so exactly one root is negative.
    return 3


def golden_witness():
    b = ((1, 1), (1, 0))
    assert b in irrational_b_matrices()
    eta, tau = Q(1, 2), Q(1, 3)
    K = mat_identity(4)
    L = block_diag_b(b)
    expansion = rsp.determinant_exponential_expansion((Q(1), eta, tau), (K, L, K))
    original = rr.rational_jet(expansion)
    first = rr.newton_step(original, Q(1), 4)
    assert first is not None
    theta1, jet1, edge1, _ = first
    assert theta1 == rr.scale_from_rational(eta)
    f = (Q(-1), Q(1), Q(1))  # y^2+y-1
    assert edge1 == p_square(f)
    state = RealRootEvalState(smallest_real_root_selector(edge1))
    assert vanish_order(edge1, state) == 2
    second = handoff_step(jet1, state, 2)
    assert second is not None
    theta2, _, edge2, _ = second
    assert theta2 == rr.scale_from_rational(Q(2, 3))
    assert evalpoly_vanish_order(edge2, Q(-1), state) == 2
    return 6


def main() -> int:
    samples, roots, recursive, semantic, continuation = systematic_handoff_regression()
    absorption = absorption_certificate()
    golden = golden_witness()
    assert samples >= 10
    print("BRC single-generator irrational root handoff checker: PASS")
    print(f"irrational_translated_root_block_samples={samples}")
    print(f"root_selector_and_multiplicity_checks={roots}")
    print(f"handoff_recursive_checks={recursive}")
    print(f"recursive_vs_direct_semantic_checks={semantic}")
    print(f"rational_continuation_checks={continuation}")
    print(f"absorption_certificate_checks={absorption}")
    print(f"golden_handoff_checks={golden}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
