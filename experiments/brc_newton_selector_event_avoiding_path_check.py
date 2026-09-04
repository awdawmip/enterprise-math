#!/usr/bin/env python3
"""Exact checker for multivariate selector event-avoiding path certificates."""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction

from enterprise_math import brc_critical_degeneracy as cd

Q = Fraction
Poly = tuple[Fraction, ...]


def trim(poly: Poly) -> Poly:
    return cd._trim(poly)


def p_add(a: Poly, b: Poly) -> Poly:
    return cd._p_add(a, b)


def p_scale(poly: Poly, scalar) -> Poly:
    return cd._p_scale(poly, Q(scalar))


def p_mul(a: Poly, b: Poly) -> Poly:
    return cd._p_mul(a, b)


def p_eval(poly: Poly, x: Fraction) -> Fraction:
    return cd._p_eval(poly, x)


def p_sub(a: Poly, b: Poly) -> Poly:
    return p_add(a, p_scale(b, -1))


@dataclass(frozen=True)
class PathSegment2D:
    u: Poly
    v: Poly

    def point(self, s: Fraction) -> tuple[Fraction, Fraction]:
        return p_eval(self.u, s), p_eval(self.v, s)


def rho2_pullback(segment: PathSegment2D) -> Poly:
    return p_add(p_mul(segment.u, segment.u), p_mul(segment.v, segment.v))


def event_pullback(segment: PathSegment2D) -> Poly:
    rho2 = rho2_pullback(segment)
    return p_mul(p_sub((Q(1),), rho2), p_sub((Q(17),), rho2))


def open_unit_root_count(poly: Poly) -> int:
    poly = trim(poly)
    if poly == (Q(0),):
        raise ValueError("identically zero pullback is not event-avoiding")
    if p_eval(poly, Q(0)) == 0 or p_eval(poly, Q(1)) == 0:
        raise ValueError("event hit at path endpoint")
    derivative = cd._p_derivative(poly)
    gcd = cd._p_gcd(poly, derivative)
    sf = cd._p_div_exact(poly, gcd) if len(gcd) > 1 else poly
    return cd._root_count(cd._sturm_sequence(sf), Q(0), Q(1))


def certify_segment(segment: PathSegment2D) -> tuple[Poly, bool, int]:
    pullback = event_pullback(segment)
    count = open_unit_root_count(pullback)
    return pullback, count == 0, count


def selector_safe(u: Fraction, v: Fraction) -> bool | None:
    # Q_{u,v}(x)=x^2+(1-u^2-v^2)/4, declared root r=-2.
    rho2 = u * u + v * v
    collision = rho2 == 17
    if collision:
        return None
    # T62 with a=0,r=-2 reduces exactly to rho^2<17.
    return rho2 < 17


def straight_line_failure():
    segment = PathSegment2D((Q(-2), Q(4)), (Q(0),))
    pullback, certified, count = certify_segment(segment)
    assert not certified and count == 2
    assert selector_safe(*segment.point(Q(0))) is True
    assert selector_safe(*segment.point(Q(1))) is True
    for s in (Q(0), Q(1, 8), Q(1, 4), Q(1, 2), Q(3, 4), Q(7, 8), Q(1)):
        assert selector_safe(*segment.point(s)) is True
    # Exact inner-circle events at s=1/4 and 3/4.
    assert p_eval(pullback, Q(1, 4)) == 0
    assert p_eval(pullback, Q(3, 4)) == 0
    return 11


def detour_certificate():
    first = PathSegment2D((Q(-2), Q(2)), (Q(0), Q(2)))
    second = PathSegment2D((Q(0), Q(2)), (Q(2), Q(-2)))
    assert first.point(Q(1)) == second.point(Q(0)) == (Q(0), Q(2))
    checks = 1
    for segment in (first, second):
        pullback, certified, count = certify_segment(segment)
        assert certified and count == 0
        # rho^2=4(1-2s+2s^2), so 2<=rho^2<=4 on [0,1].
        expected_rho2 = (Q(4), Q(-8), Q(8))
        assert rho2_pullback(segment) == expected_rho2
        # Event pullback has constant negative sign on the whole segment.
        for s in (Q(0), Q(1, 8), Q(1, 4), Q(1, 2), Q(3, 4), Q(7, 8), Q(1)):
            rho2 = p_eval(expected_rho2, s)
            assert Q(2) <= rho2 <= Q(4)
            assert p_eval(pullback, s) < 0
            assert selector_safe(*segment.point(s)) is True
            checks += 3
        checks += 3
    assert first.point(Q(0)) == (Q(-2), Q(0))
    assert second.point(Q(1)) == (Q(2), Q(0))
    return checks + 2


def genuine_separator_witness():
    # Radial segment from A=(-2,0) to C=(5,0).
    segment = PathSegment2D((Q(-2), Q(7)), (Q(0),))
    pullback, certified, count = certify_segment(segment)
    assert not certified
    assert count == 3  # crosses u=-1, u=1, and u=sqrt(17)
    assert selector_safe(*segment.point(Q(0))) is True
    assert selector_safe(*segment.point(Q(1))) is False
    # Outer factor must change sign somewhere because rho^2 goes 4 -> 25.
    outer = p_sub((Q(17),), rho2_pullback(segment))
    assert p_eval(outer, Q(0)) > 0 and p_eval(outer, Q(1)) < 0
    assert p_eval(pullback, Q(0)) != 0 and p_eval(pullback, Q(1)) != 0
    return 8


def piecewise_transport_reversal():
    first = PathSegment2D((Q(-2), Q(2)), (Q(0), Q(2)))
    second = PathSegment2D((Q(0), Q(2)), (Q(2), Q(-2)))
    reverse_second = PathSegment2D((Q(2), Q(-2)), (Q(0), Q(2)))
    reverse_first = PathSegment2D((Q(0), Q(-2)), (Q(2), Q(-2)))
    for segment in (first, second, reverse_second, reverse_first):
        assert certify_segment(segment)[1]
    assert reverse_second.point(Q(0)) == second.point(Q(1))
    assert reverse_second.point(Q(1)) == second.point(Q(0))
    assert reverse_first.point(Q(0)) == first.point(Q(1))
    assert reverse_first.point(Q(1)) == first.point(Q(0))
    return 8


def main() -> int:
    straight = straight_line_failure()
    detour = detour_certificate()
    separator = genuine_separator_witness()
    reversal = piecewise_transport_reversal()
    print("BRC selector event-avoiding path certificate checker: PASS")
    print(f"straight_line_failure_checks={straight}")
    print("straight_line_event_root_count=2")
    print(f"detour_certificate_checks={detour}")
    print("detour_segment_event_root_counts=(0,0)")
    print(f"genuine_separator_checks={separator}")
    print("radial_separator_event_root_count=3")
    print(f"path_reversal_checks={reversal}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
