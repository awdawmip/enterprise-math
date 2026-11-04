#!/usr/bin/env python3
"""Exact rational and optional symbolic diagnostics for D25 original-216 no-Gosper theorem.
The theorem is analytically proved in the companion note, not by finite sampling.
Native H0/B0 is NOT_RUN.
"""
from fractions import Fraction
from math import comb

def original(k):
    return Fraction((6*k+1)*comb(2*k,k)**2*comb(3*k,k),216**k)

def poch(k):
    z=Fraction(1)
    for j in range(k):
        z *= Fraction((2*j+1)*(3*j+1)*(3*j+2),36*(j+1)**3)
    return (6*k+1)*z

def adjacent(k):
    return Fraction((6*k+7)*(2*k+1)*(3*k+1)*(3*k+2),
                    (6*k+1)*36*(k+1)**3)

def run():
    for k in range(30):
        assert original(k)==poch(k)
        assert original(k+1)/original(k)==adjacent(k)
    a,b='not_run','not_run'
    try:
        import sympy as s
        from sympy.concrete.gosper import gosper_term
        k,n=s.symbols('k n',integer=True)
        orig=(6*k+1)*s.rf(s.Rational(1,2),k)*s.rf(s.Rational(1,3),k)*s.rf(s.Rational(2,3),k)/(2**k*s.factorial(k)**3)
        cent=(6*k+1)*s.rf(-3*n,k)*s.rf(-2*n,k)*s.rf(-4*n,k)/(2**k*s.factorial(k)**3)
        a='NONE' if gosper_term(orig,k) is None else 'CANDIDATE'
        b='NONE' if gosper_term(cent,k) is None else 'CANDIDATE'
    except ImportError:
        a=b='sympy_unavailable'
    value='mpmath_unavailable'
    try:
        import mpmath as m
        m.mp.dps=65
        term=m.mpf(1); total=term
        for k in range(1,420):
            term *= (k-m.mpf(1)/2)*(k-m.mpf(1)/3)*(k-m.mpf(2)/3)/(2*k**3)
            total+=(6*k+1)*term
        assert abs(total-3*m.sqrt(3)/m.pi)<m.mpf('1e-59')
        value=m.nstr(total,45)
    except ImportError:
        pass
    print('PASS: exact 30 original indexed coefficients and ratios')
    print('GOSPER_UNSHIFTED_DIAGNOSTIC:',a)
    print('GOSPER_CENTERED_DIAGNOSTIC:',b)
    print('HIGH_PRECISION_SUM:',value)
    print('THEOREM_PROOF: analytic telescoping + transcendent pi')
    print('NATIVE_H0_B0_EXECUTED: False')
if __name__=='__main__':
    run()
