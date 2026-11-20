#!/usr/bin/env python3
"""Exact rational-pair verification for E repeated-coupling time-window identity."""
from fractions import Fraction

ROOT = [(1, 0), (0, 1), (-1, -1)]  # omega**(k mod 3) in basis (1,omega)

def avg(n, d):
    return tuple(Fraction(sum(ROOT[(k*d)%3][j] for k in range(n)), n)
                 for j in (0, 1))

def expected(n, d):
    if d == 0:
        return (Fraction(1), Fraction(0))
    q, s = divmod(n, 3)
    if s == 0:
        return (Fraction(0), Fraction(0))
    if s == 1:
        return (Fraction(1, n), Fraction(0))
    return tuple(Fraction(ROOT[0][j]+ROOT[d][j], n) for j in (0, 1))

for n in range(1, 13):
    for d in range(3):
        actual = avg(n, d)
        assert actual == expected(n, d), (n, d, actual, expected(n, d))
# Strictly positive witness: calibrated r=a=0, uniform j=0,1,2.
for n in (3, 6, 9, 12):
    averaged = tuple(sum((avg(n, d)[j] for d in range(3)), Fraction(0))/3 for j in (0,1))
    assert averaged == (Fraction(1,3), Fraction(0)), averaged
assert tuple(sum((ROOT[d][j] for d in range(3)), 0) for j in (0,1)) == (0,0)
print("PASS: 36 exact (N,d) checks, four positive-weight averaged witness checks.")
