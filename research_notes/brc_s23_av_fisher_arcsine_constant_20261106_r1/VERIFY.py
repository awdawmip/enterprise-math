#!/usr/bin/env python3
"""Exact finite checks and illustrative numeric convergence for S23 arcsine kernel.
The uniform all-n asymptotic statement is proved analytically in PROOF.md.
"""
from fractions import Fraction
from math import comb, lgamma, log, exp, asin, sqrt, pi


def q_arc(m, k):
    return Fraction(comb(2*k, k)*comb(2*(m-k), m-k), 4**m)


def overlap_exact(m, r):
    return sum((min(Fraction(comb(m, k), 1)*r**k*(1-r)**(m-k), q_arc(m, k))
                for k in range(m+1)), Fraction(0))

count = 0
for m in range(0, 121):
    assert sum(comb(2*k, k)*comb(2*(m-k), m-k) for k in range(m+1)) == 4**m
    count += 1
assert [q_arc(2, k) for k in range(3)] == [Fraction(3, 8), Fraction(1, 4), Fraction(3, 8)]
count += 1
corners = [(Fraction(7,8), Fraction(7,8)), (Fraction(1,2), Fraction(1,2)), (Fraction(7,8), Fraction(1,2))]
for a,c in corners:
    z = (1-a)*c
    r = (1-a)*(1-c)/(1-z)
    assert Fraction(1,57) <= r <= Fraction(1,3)
    assert Fraction(1,16) <= z <= Fraction(7,16)
    count += 2
assert (1-corners[2][0])*corners[2][1] == Fraction(1,16)
count += 1
for m in (5,10,30,75,100):
    for r in (Fraction(1,57), Fraction(1,15), Fraction(1,3)):
        ov = overlap_exact(m, r)
        assert Fraction(0) < ov <= 1
        count += 1

I = 2*(asin(sqrt(1/3))-asin(sqrt(1/57)))
C = 8/(I*sqrt(15))
C_full = 8/(pi*sqrt(15))
print('EXACT_ASSERTIONS_PASSED', count)
print('I_star =',format(I,'.15f'))
print('padded_fisher_limit_C =',format(C,'.15f'))
print('full_arcsine_C =',format(C_full,'.15f'))

# Floating-point diagnostics ONLY (not input to proof).
def ov_float(m, r):
    lp=log(r); lq=log(1-r)
    out=0.0
    for k in range(m+1):
        logp = lgamma(m+1)-lgamma(k+1)-lgamma(m-k+1)+k*lp+(m-k)*lq
        logq = lgamma(k+.5)+lgamma(m-k+.5)-lgamma(k+1)-lgamma(m-k+1)-log(pi)
        out += exp(min(logp,logq))
    return out

for m in (100,1000,10000):
    print('FULL_ARCSINE_DIAGNOSTIC', m, [(str(r),format(ov_float(m,float(r))*sqrt(m/log(m)),'.8f')) for r in (Fraction(1,57),Fraction(1,15),Fraction(1,3))])
print('PASS_S23_ARCSINE_BRC_FISHER_MIXTURE_20261106')
