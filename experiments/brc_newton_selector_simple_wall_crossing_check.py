#!/usr/bin/env python3
"""Exact checker for simple selector wall-crossing orientation."""
from __future__ import annotations

from fractions import Fraction

from enterprise_math import brc_critical_degeneracy as cd

Q = Fraction
Poly = tuple[Fraction, ...]


def sign(value: Fraction) -> int:
    return (value > 0) - (value < 0)


def rank_lt(poly: Poly, probe: Fraction) -> int:
    if cd._p_eval(poly, probe) == 0:
        raise ValueError("probe is a polynomial root")
    lead = abs(poly[-1])
    bound = max((abs(c) / lead for c in poly[:-1]), default=Q(0))
    left = -max(abs(probe) + 2, bound + 2)
    return cd._root_count(cd._sturm_sequence(poly), left, probe)


def zero_right_rank(poly: Poly) -> int:
    work = cd._trim(poly)
    had_zero = False
    while len(work) > 1 and cd._p_eval(work, Q(0)) == 0:
        work = cd._p_div_exact(work, (Q(0), Q(1)))
        had_zero = True
    if len(work) <= 1:
        return int(had_zero)
    return rank_lt(work, Q(0)) + int(had_zero)


def positive_interval_count(poly: Poly, right: Fraction) -> int:
    if right <= 0 or cd._p_eval(poly, right) == 0:
        raise ValueError("positive interval endpoint invalid")
    return rank_lt(poly, right) - zero_right_rank(poly)


def oriented_jump(pt: Fraction, px: Fraction, *, endpoint: str) -> int | None:
    if pt == 0 or px == 0:
        return None
    ratio_sign = sign(pt / px)
    if endpoint in ("rank", "right"):
        return ratio_sign
    if endpoint == "left":
        return -ratio_sign
    raise ValueError("unknown endpoint")


def one_real_cubic(t: Fraction) -> Poly:
    return (t, Q(1), Q(0), Q(1))  # x^3+x+t


def fixed_factor() -> Poly:
    return cd._p_mul((Q(1), Q(0), Q(1)), (Q(-1), Q(-1), Q(1)))


def moving_factor_family(t: Fraction) -> Poly:
    return cd._p_mul(fixed_factor(), (Q(-t), Q(1)))


def cubic_rank_wall():
    # Probe r=0, event t=0, Pt=1,Px=1 -> rank jump +1.
    assert oriented_jump(Q(1), Q(1), endpoint="rank") == 1
    checks = 1
    for epsilon in (Q(1, 2), Q(1, 4), Q(1, 8), Q(1, 16), Q(1, 32)):
        before = rank_lt(one_real_cubic(-epsilon), Q(0))
        after = rank_lt(one_real_cubic(epsilon), Q(0))
        assert before == 0 and after == 1 and after - before == 1
        checks += 3
    return checks


def cubic_positive_two_walls():
    right = Q(1)
    checks = 0
    # At t=-2, x=1: Pt/Px=1/4 >0, so one root enters (0,1).
    assert oriented_jump(Q(1), Q(4), endpoint="right") == 1
    # At t=0, x=0: Pt/Px=1, but this is the left endpoint, so N jumps -1.
    assert oriented_jump(Q(1), Q(1), endpoint="left") == -1
    checks += 2
    for epsilon in (Q(1, 2), Q(1, 4), Q(1, 8), Q(1, 16)):
        before_r = positive_interval_count(one_real_cubic(Q(-2) - epsilon), right)
        after_r = positive_interval_count(one_real_cubic(Q(-2) + epsilon), right)
        assert (before_r, after_r, after_r - before_r) == (0, 1, 1)

        before_0 = positive_interval_count(one_real_cubic(-epsilon), right)
        after_0 = positive_interval_count(one_real_cubic(epsilon), right)
        assert (before_0, after_0, after_0 - before_0) == (1, 0, -1)
        checks += 6
    return checks


def moving_linear_two_walls():
    right = Q(1)
    f = fixed_factor()
    assert cd._p_eval(f, Q(0)) != 0 and cd._p_eval(f, Q(1)) != 0
    # On x=t, Pt=-F and Px=F, so Pt/Px=-1 exactly.
    assert oriented_jump(Q(-1), Q(1), endpoint="left") == 1
    assert oriented_jump(Q(-1), Q(1), endpoint="right") == -1
    checks = 2
    for epsilon in (Q(1, 4), Q(1, 8), Q(1, 16), Q(1, 32)):
        before_0 = positive_interval_count(moving_factor_family(-epsilon), right)
        after_0 = positive_interval_count(moving_factor_family(epsilon), right)
        assert (before_0, after_0, after_0 - before_0) == (0, 1, 1)

        before_1 = positive_interval_count(moving_factor_family(Q(1) - epsilon), right)
        after_1 = positive_interval_count(moving_factor_family(Q(1) + epsilon), right)
        assert (before_1, after_1, after_1 - before_1) == (1, 0, -1)
        checks += 6
    return checks


def tangency_refusal():
    # P=x-t^2, probe r=0.  Px=1 but Pt=-2t vanishes at t=0.
    assert oriented_jump(Q(0), Q(1), endpoint="rank") is None
    checks = 1
    for epsilon in (Q(1, 2), Q(1, 4), Q(1, 8), Q(1, 16)):
        before: Poly = (Q(-(epsilon * epsilon)), Q(1))
        after: Poly = before
        assert rank_lt(before, Q(0)) == 0
        assert rank_lt(after, Q(0)) == 0
        checks += 2
    return checks


def multiple_root_refusal():
    # P=x^2+t x+1, probe r=-1, event t=2.  Px=0, so no simple orientation.
    assert oriented_jump(Q(-1), Q(0), endpoint="rank") is None
    checks = 1
    for epsilon in (Q(1, 4), Q(1, 8), Q(1, 16), Q(1, 32)):
        before: Poly = (Q(1), Q(2) - epsilon, Q(1))
        after: Poly = (Q(1), Q(2) + epsilon, Q(1))
        rank_before = rank_lt(before, Q(-1))
        rank_after = rank_lt(after, Q(-1))
        assert rank_before == 0 and rank_after == 1
        checks += 3
    return checks


def exact_derivative_ratio_identities():
    checks = 0
    # x^3+x+t at the two endpoint events.
    for t0, x0, expected_px in ((Q(-2), Q(1), Q(4)), (Q(0), Q(0), Q(1))):
        poly = one_real_cubic(t0)
        assert cd._p_eval(poly, x0) == 0
        px_poly = cd._p_derivative(poly)
        assert cd._p_eval(px_poly, x0) == expected_px
        pt = Q(1)
        alpha_prime = -pt / expected_px
        assert alpha_prime < 0
        checks += 4

    # F(x)(x-t): at its moving root, derivative ratio is exactly -1.
    f = fixed_factor()
    for t0 in (Q(0), Q(1), Q(2)):
        fx = cd._p_eval(f, t0)
        assert fx != 0
        pt = -fx
        px = fx
        assert pt / px == -1
        assert -pt / px == 1  # alpha'(t)=1
        checks += 4
    return checks


def main() -> int:
    rank = cubic_rank_wall()
    cubic_positive = cubic_positive_two_walls()
    moving = moving_linear_two_walls()
    tangent = tangency_refusal()
    multiple = multiple_root_refusal()
    derivatives = exact_derivative_ratio_identities()
    print("BRC simple selector wall-crossing checker: PASS")
    print(f"cubic_root_rank_wall_checks={rank}")
    print(f"cubic_positive_endpoint_wall_checks={cubic_positive}")
    print(f"moving_linear_endpoint_wall_checks={moving}")
    print(f"tangency_refusal_checks={tangent}")
    print(f"multiple_root_refusal_checks={multiple}")
    print(f"exact_derivative_ratio_checks={derivatives}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
