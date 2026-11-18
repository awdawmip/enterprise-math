#!/usr/bin/env python3
"""Exact n=1000, five-point, common-fiber S23/AV reconstruction lower certificate."""
from fractions import Fraction
from math import comb
from decimal import Decimal, getcontext

N = 1000
A = (Fraction(1, 2), Fraction(5551, 10000), Fraction(381, 625),
     Fraction(6627, 10000), Fraction(5, 7))
CUTS = (527, 582, 636, 688)
INTERVALS = ((0, 527), (528, 582), (583, 636), (637, 688), (689, N))

def binomial_interval(p: Fraction, lo: int, hi: int) -> Fraction:
    x, d = p.numerator, p.denominator
    numer = sum(comb(N, k) * x**k * (d-x)**(N-k)
                for k in range(lo, hi + 1))
    return Fraction(numer, d**N)

assert len(A) == len(INTERVALS) == 5
assert [i[1] + 1 for i in INTERVALS[:-1]] == [i[0] for i in INTERVALS[1:]]
assert INTERVALS[0][0] == 0 and INTERVALS[-1][-1] == N
assert all(Fraction(1,2) <= a <= Fraction(5,7) for a in A)
C = tuple(Fraction(1,4) / (1-a) for a in A)
assert all(Fraction(1,2) <= c <= Fraction(7,8) for c in C)
assert all((1-a)*c == Fraction(1,4) for a,c in zip(A,C))
assert all(sum((a, Fraction(1,4), Fraction(3,4)-a)) == 1 for a in A)
assert all(Fraction(3,4)-a >= 0 for a in A)

S = tuple(binomial_interval(p, *interval)
          for p, interval in zip(A, INTERVALS))
LB = (sum(S, Fraction(0)) - 1) / 5
assert all(Fraction(0) <= s <= 1 for s in S)
assert LB > Fraction(7361, 10000), "The stronger finite-n bound failed"
assert LB > Fraction(13, 20), "Predecessor rational bound failed"
getcontext().prec = 27
approx = Decimal(LB.numerator) / Decimal(LB.denominator)
print('frozen_binary_fiber_z=1/4')
print('source_stop1_masses=' + ','.join(map(str, A)))
print('source_c_parameters=' + ','.join(map(str, C)))
print('n=1000_count_intervals=' + str(INTERVALS))
print('rigorous_lower_bound_greater_than_7361_over_10000=' + str(LB > Fraction(7361,10000)))
print('n1000_exact_lower_decimal_20=' + format(approx, '.20f'))
print('PASS_S23_N1000_FIVE_FIBER_PACKING_EXACT_20261107')
