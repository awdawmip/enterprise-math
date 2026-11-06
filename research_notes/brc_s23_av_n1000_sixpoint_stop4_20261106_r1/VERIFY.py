#!/usr/bin/env python3
"""Exact six-hypothesis binomial stop4 certificate for frozen S23/AV."""
from decimal import Decimal, localcontext
from fractions import Fraction
from math import comb

N = 1000
Z = Fraction(1, 4)
STOP4 = (
    Fraction(1, 28), Fraction(3217, 50000),
    Fraction(10091, 100000), Fraction(14447, 100000),
    Fraction(9727, 50000), Fraction(1, 4),
)
EVENTS = ((0, 48), (49, 81), (82, 121),
          (122, 168), (169, 221), (222, 1000))
TARGET = Fraction(201, 250)


def exact_binomial_interval(n, p, left, right):
    assert isinstance(p, Fraction) and 0 < p < 1
    assert 0 <= left <= right <= n
    r, d = p.numerator, p.denominator
    total = sum(comb(n, k) * pow(r, k) * pow(d-r, n-k)
                for k in range(left, right+1))
    return Fraction(total, pow(d, n))


def main():
    assert len(STOP4) == len(EVENTS) == 6
    assert EVENTS[0][0] == 0 and EVENTS[-1][1] == N
    assert all(EVENTS[i][1] + 1 == EVENTS[i+1][0] for i in range(5))
    for q in STOP4:
        a = Fraction(3, 4) - q
        c = Z / (1 - a)
        p = (a, Z, q)
        assert Fraction(1, 2) <= a <= Fraction(7, 8)
        assert Fraction(1, 2) <= c <= Fraction(7, 8)
        assert sum(p) == 1 and min(p) > 0
        assert (1-a)*c == Z
    cert = [exact_binomial_interval(N, q, *e) for q,e in zip(STOP4, EVENTS)]
    assert all(Fraction(0) < value < Fraction(1) for value in cert)
    lower = (sum(cert, Fraction(0)) - 1) / 6
    assert lower > TARGET
    assert lower > Fraction(92, 125)
    assert 0 < lower < 1
    with localcontext() as ctx:
        ctx.prec = 42
        val = Decimal(lower.numerator) / Decimal(lower.denominator)
        margin = Decimal((lower-TARGET).numerator) / Decimal((lower-TARGET).denominator)
    print('PASS_S23_AV_1000_SIXPOINT_STOP4_EXACT_20261106')
    print('n=1000; hypotheses=6; shared_z=1/4')
    print('stop4='+str([str(x) for x in STOP4]))
    print('intervals='+str(EVENTS))
    print('sixpoint_lower='+str(val))
    print('bound=delta_1000 > 201/250 (0.804)')
    print('exact_margin_above_201_250='+str(margin))
    print('arithmetic=math.comb+integer powers+Fraction; all_assertions_passed')
    print('scope=conditional AV observer; author exact-rational certificate; independent review pending')


if __name__ == '__main__':
    main()
