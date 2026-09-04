#!/usr/bin/env python3
"""Exact checker for ordinary-fold selector wall jumps."""
from __future__ import annotations

from fractions import Fraction

from enterprise_math import brc_critical_degeneracy as cd

Q = Fraction
Poly = tuple[Fraction, ...]


def rank_lt(poly: Poly, probe: Fraction) -> int:
    if cd._p_eval(poly, probe) == 0:
        raise ValueError("probe is a root")
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


def interval_count(poly: Poly, right: Fraction) -> int:
    if right <= 0 or cd._p_eval(poly, right) == 0:
        raise ValueError("invalid positive endpoint")
    return rank_lt(poly, right) - zero_right_rank(poly)


def fold_kappa(pt: Fraction, pxx: Fraction) -> Fraction | None:
    if pt == 0 or pxx == 0:
        return None
    return -2 * pt / pxx


def expected_rank_jump(kappa: Fraction | None, x0: Fraction, probe: Fraction) -> int | None:
    if kappa is None or x0 == probe:
        return None
    return 2 * ((kappa > 0) - (kappa < 0)) if x0 < probe else 0


def expected_positive_jump(kappa: Fraction | None, x0: Fraction, right: Fraction) -> int | None:
    if kappa is None or x0 in (Q(0), right):
        return None
    if 0 < x0 < right:
        return 2 * ((kappa > 0) - (kappa < 0))
    return 0


def quadratic(t: Fraction) -> Poly:
    return (Q(1), t, Q(1))


def annihilation_fold():
    # t0=-2,x0=1: Pt=1,Pxx=2,kappa=-1.
    kappa = fold_kappa(Q(1), Q(2))
    assert kappa == -1
    assert expected_rank_jump(kappa, Q(1), Q(0)) == 0
    assert expected_rank_jump(kappa, Q(1), Q(2)) == -2
    assert expected_positive_jump(kappa, Q(1), Q(2)) == -2
    checks = 4
    for epsilon in (Q(1, 4), Q(1, 8), Q(1, 16), Q(1, 32), Q(1, 64)):
        before = quadratic(Q(-2) - epsilon)
        after = quadratic(Q(-2) + epsilon)
        assert rank_lt(before, Q(0)) == rank_lt(after, Q(0)) == 0
        rb = rank_lt(before, Q(2))
        ra = rank_lt(after, Q(2))
        assert (rb, ra, ra - rb) == (2, 0, -2)
        nb = interval_count(before, Q(2))
        na = interval_count(after, Q(2))
        assert (nb, na, na - nb) == (2, 0, -2)
        checks += 7
    return checks


def birth_fold():
    # t0=2,x0=-1: Pt=-1,Pxx=2,kappa=+1.
    kappa = fold_kappa(Q(-1), Q(2))
    assert kappa == 1
    assert expected_rank_jump(kappa, Q(-1), Q(0)) == 2
    assert expected_positive_jump(kappa, Q(-1), Q(2)) == 0
    checks = 3
    for epsilon in (Q(1, 4), Q(1, 8), Q(1, 16), Q(1, 32), Q(1, 64)):
        before = quadratic(Q(2) - epsilon)
        after = quadratic(Q(2) + epsilon)
        rb = rank_lt(before, Q(0))
        ra = rank_lt(after, Q(0))
        assert (rb, ra, ra - rb) == (0, 2, 2)
        nb = interval_count(before, Q(2))
        na = interval_count(after, Q(2))
        assert nb == na == 0
        checks += 5
    return checks


def endpoint_fold_refusal():
    # P=x^2+t at (t,x)=(0,0), kappa=-1.  Positive interval sees only one
    # member of the symmetric pair, so the interior +-2 rule must refuse.
    kappa = fold_kappa(Q(1), Q(2))
    assert kappa == -1
    assert expected_positive_jump(kappa, Q(0), Q(2)) is None
    checks = 2
    for epsilon in (Q(1, 4), Q(1, 16), Q(1, 64), Q(1, 256)):
        before: Poly = (Q(-epsilon), Q(0), Q(1))
        after: Poly = (Q(epsilon), Q(0), Q(1))
        nb = interval_count(before, Q(2))
        na = interval_count(after, Q(2))
        assert (nb, na, na - nb) == (1, 0, -1)
        checks += 3
    return checks


def degenerate_fold_refusals():
    checks = 0
    # x^2-t^2 at (0,0): Pt=0.
    assert fold_kappa(Q(0), Q(2)) is None
    for epsilon in (Q(1, 4), Q(1, 8), Q(1, 16)):
        poly: Poly = (Q(-(epsilon * epsilon)), Q(0), Q(1))
        assert rank_lt(poly, Q(2)) == 2
        checks += 1

    # x^3-t at (0,0): Pxx=0.
    assert fold_kappa(Q(-1), Q(0)) is None
    for epsilon in (Q(1, 4), Q(1, 8), Q(1, 16)):
        before: Poly = (epsilon, Q(0), Q(0), Q(1))   # x^3+eps
        after: Poly = (-epsilon, Q(0), Q(0), Q(1))  # x^3-eps
        assert rank_lt(before, Q(0)) == 1
        assert rank_lt(after, Q(0)) == 0
        checks += 2
    return checks + 2


def local_real_pair_side_checks():
    # Exact discriminant confirms the kappa side for the quadratic family.
    checks = 0
    for t0, expected_sign in ((Q(-2), -1), (Q(2), 1)):
        for epsilon in (Q(1, 8), Q(1, 32), Q(1, 128)):
            d_left = (t0 - epsilon) ** 2 - 4
            d_right = (t0 + epsilon) ** 2 - 4
            if expected_sign < 0:  # kappa<0 -> real pair on delta t<0
                assert d_left > 0 and d_right < 0
            else:
                assert d_left < 0 and d_right > 0
            checks += 2
    return checks


def main() -> int:
    annihilation = annihilation_fold()
    birth = birth_fold()
    endpoint = endpoint_fold_refusal()
    degenerate = degenerate_fold_refusals()
    pair_side = local_real_pair_side_checks()
    print("BRC ordinary-fold selector wall checker: PASS")
    print(f"annihilation_fold_checks={annihilation}")
    print(f"birth_fold_checks={birth}")
    print(f"endpoint_fold_refusal_checks={endpoint}")
    print(f"degenerate_fold_refusal_checks={degenerate}")
    print(f"real_pair_side_checks={pair_side}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
