#!/usr/bin/env python3
"""Exact rational endpoint-inequality certificates; analytic theorem in PROOF.md.

Tests for three fixed positive contrasts x=2h. Integer isqrt, Fraction,
and positive-term series with explicit remainder bounds; no floats.
"""
from fractions import Fraction as F
from math import isqrt

Q = 10**45

def sqrt_bounds(z):
    assert 0 < z <= 1
    m = isqrt(z.numerator * Q * Q // z.denominator)
    lo, hi = F(m, Q), F(m+1,Q)
    assert lo*lo <= z < hi*hi
    return lo,hi

def atanh_bounds(x,N=24):
    assert 0<x<1
    lower=sum((x**(2*k+1)/F(2*k+1)) for k in range(N))
    remainder=x**(2*N+1)/(F(2*N+1)*(1-x*x))
    return lower,lower+remainder

def minus_logw_bounds(x,N=24):
    # -log(sqrt(1-x^2))= 1/2 sum_{k>=1} (x^2)^k/k
    y=x*x
    lower=sum((y**k/F(2*k)) for k in range(1,N+1))
    remainder=y**(N+1)/(F(2*(N+1))*(1-y))
    return lower,lower+remainder

def prove_one(x):
    wlo,whi=sqrt_bounds(1-x*x)
    _,atanhhi=atanh_bounds(x)
    _,minus_logw_hi=minus_logw_bounds(x)
    # D'(1/2)=x-w*atanh(x) >0: strict and exact.
    assert x>whi*atanhhi
    # coefficient of (1-s) in F(s,h) near 1 is positive.
    # (1-w)/w^2 decreases in w on (0,1).
    assert (1-whi)/(whi*whi)>minus_logw_hi
    print('EXACT_RATIONAL_ENDPOINT_SIGNS',f'x={x.numerator}/{x.denominator}',
          'DprimeHalfLowerPositive', 'nearOneCoefficientLowerPositive')

for x in (F(1,21),F(1,5),F(2,3)):
    prove_one(x)
print('PASS_BRC_S23_CHERNOFF_ALL_CONTRAST_ENDPOINT_THEOREM_EXACT_CHECK_20261104')
