#!/usr/bin/env python3
"""Exact rational Newton coefficients for R576/R577 limit F; illustrative, not a proof of all-n signs."""
from fractions import Fraction
from math import factorial
from collections import Counter

N=120
f=[Fraction((-1)**j*24*8**j, factorial(2*j+4)) for j in range(N+1)]
assert f[0]==1
L=[Fraction(0)]*(N+1)
for n in range(1,N+1):
    L[n]=-n*f[n]-sum(f[j]*L[n-j] for j in range(1,n))
    # derivative identity F'(z) + F(z) sum_{n>=1} L_n*z^{n-1} = 0
    assert n*f[n] + sum(f[j]*L[n-j] for j in range(n)) == 0
    assert L[n]!=0
signs=['+' if x>0 else '-' for x in L[1:]]
print('R578_SOURCE R462@18783e01e3646c72b7aab3b16d3f565e83e6446f')
print('RECURRENCE exact Fraction n=1..'+str(N))
print('L_1',L[1]);print('L_2',L[2]);print('L_3',L[3]);print('L_4',L[4]);print('L_5',L[5]);print('L_6',L[6]);print('L_7',L[7]);print('L_8',L[8])
print('SIGNS_1_TO_120',''.join(signs))
print('COUNT', dict(Counter(signs)))
print('R578_EXACT_NEWTON_RECURRENCE_PASS')
