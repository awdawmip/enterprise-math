#!/usr/bin/env python3
"""Exact, dependency-free S23/AV five-point 1000-trial risk certificate.

Scientific input is the shared-parameter conditional AV experiment of
awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34.
The general all-n rate is proved analytically in PROOF.md using Hoeffding;
this checker verifies the finite-n rational statement only.
"""
from decimal import Decimal, localcontext
from fractions import Fraction
from math import comb

N = 1000
FIRST_STOP_MASSES = (
    Fraction(1, 2), Fraction(111, 200), Fraction(61, 100),
    Fraction(663, 1000), Fraction(5, 7),
)
# Disjoint, full partition of {0,...,1000}; no optimize-time input needed.
INTERVALS = ((0, 527), (528, 582), (583, 636), (637, 688), (689, 1000))
TARGET = Fraction(92, 125)  # 0.736


def exact_binomial_interval(n: int, p: Fraction, lo: int, hi: int) -> Fraction:
    a, d = p.numerator, p.denominator
    b = d - a
    assert 0 <= lo <= hi <= n and 0 < a < d
    total = sum(comb(n, k) * pow(a, k) * pow(b, n - k)
                for k in range(lo, hi + 1))
    return Fraction(total, pow(d, n))


def main() -> None:
    assert len(FIRST_STOP_MASSES) == len(INTERVALS) == 5
    assert INTERVALS[0][0] == 0 and INTERVALS[-1][1] == N
    for i in range(4):
        assert INTERVALS[i][1] + 1 == INTERVALS[i+1][0]

    full_laws = []
    for a in FIRST_STOP_MASSES:
        c = Fraction(1, 4) / (1-a)
        z = (1-a)*c
        assert Fraction(1, 2) <= a <= Fraction(7, 8)
        assert Fraction(1, 2) <= c <= Fraction(7, 8)
        assert z == Fraction(1, 4)
        P = (a, z, 1-a-z)
        assert min(P) >= 0 and sum(P) == 1
        full_laws.append(P)
    assert len(set(full_laws)) == 5
    assert all(Fraction(1, 4) == P[1] for P in full_laws)

    success = [exact_binomial_interval(N, a, *bounds)
               for a, bounds in zip(FIRST_STOP_MASSES, INTERVALS)]
    assert all(Fraction(0) < q < Fraction(1) for q in success)
    lower = (sum(success, Fraction(0)) - 1) / 5
    assert lower > TARGET  # exact rational comparison; no floating point
    assert lower < 1

    with localcontext() as ctx:
        ctx.prec = 40
        approx = Decimal(lower.numerator) / Decimal(lower.denominator)
        delta = Decimal((lower - TARGET).numerator) / Decimal((lower - TARGET).denominator)
    print('PASS_S23_AV_1000_FIVE_POINT_EXACT_AND_HOEFFDING_RATE_20261106')
    print('trials=1000; shared_z=1/4; legal_hypotheses=5; partition=[527,582,636,688]')
    print('five_point_lower_decimal=' + str(approx))
    print('strict_bound=delta_1000 > 92/125')
    print('margin_over_92/125=' + str(delta))
    print('arithmetic=integer-binomial-sums/Fraction; assertions=all_passed')
    print('scope=author_exact_finite_certificate; all_n_rate=analytic_Hoeffding_proof')


if __name__ == '__main__':
    main()
