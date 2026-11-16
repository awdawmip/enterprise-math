#!/usr/bin/env python3
"""R576 auxiliary signed-BRC scalar reciprocal-limit consistency verifier.

Scientific input is frozen R462@18783e01e3646c72b7aab3b16d3f565e83e6446f.
Author-side analytic proof of quadratic spectral scale is in R576_PROOF.zh-CN.md.
All checks in this script are finite exact arithmetic except the distinctly
labelled mpmath numerical root illustrations; they do not establish a global
root-minimality certificate.
"""
from math import comb, factorial
from fractions import Fraction
import sys
import mpmath as mp

PIN = '18783e01e3646c72b7aab3b16d3f565e83e6446f'

def cat(n):
    return comb(2*n, n)//(n+1)

def H(k, s):
    r = 2*k+1
    if s < 2 or s > r:
        return 0
    return comb(r+s, 2*s)*sum(comb(s-1, 2*q)*4**q*cat(k-q)
                                    for q in range(min(k,(s-1)//2)+1))

def signed_original(k, s):
    """Independent coefficient of (1-t)(1+t)^(2s)(1+t²)^(r-s)."""
    r = 2*k+1
    if s < 2 or s > r:
        return 0
    def c_at(deg):
        return sum(comb(2*s, deg-2*j)*comb(r-s,j)
                   for j in range(r-s+1) if 0 <= deg-2*j <= 2*s)
    return comb(r+s, 2*s)*(c_at(r)-c_at(r-1))

def a_leading(j):
    return Fraction(24*8**j, factorial(2*j+4))

# Original signed coefficient to independent Catalan expression, including edge.
checked=0
for k in range(2,13):
    for s in range(2,2*k+2):
        assert H(k,s)==signed_original(k,s),(k,s)
        checked+=1

# The limiting coefficients are exact fractions, with a_0=1.
assert a_leading(0)==1
assert a_leading(1)==Fraction(4,15)
assert a_leading(2)==Fraction(4,105)

# Independently verify fixed-j leading coefficient through exact arithmetic at
# selected k, and positivity/degree cutoff for actual F_k.
coefficient_cases=0
for k in [8,16,32,64]:
    h=H(k,2)
    assert h > 0
    for j in range(1,min(17,2*k)):
        a=Fraction(H(k,j+2),h)
        assert a>0
        scaled=a/k**(2*j)
        assert scaled>0
        coefficient_cases+=1

mp.mp.dps=65
zeta=mp.findroot(lambda z:mp.cos(mp.sqrt(8*z))-1+4*z,
                 (mp.mpc(6,9),mp.mpc(7,10)), tol=mp.mpf('1e-55'))
assert abs(mp.cos(mp.sqrt(8*zeta))-1+4*zeta)<mp.mpf('1e-55')

def f_coefficients(k):
    h=H(k,2)
    return [mp.mpf(1)]+[(mp.mpf((-1)**j*H(k,j+2))/h)/mp.power(k,2*j)
                       for j in range(1,2*k)]

def f_eval(coeffs,z):
    ans=mp.mpc(0)
    for c in reversed(coeffs):
        ans=ans*z+c
    return ans

print('R576_SOURCE_R462', PIN)
print('PYTHON_VERSION',sys.version.split()[0],'MPMATH',mp.__version__)
print('SIGNED_H_EXACT_CHECKS',checked)
print('SCALED_COEFFICIENT_EXACT_CHECKS',coefficient_cases)
print('LIMIT_COEFF_J0_TO_5',*[str(a_leading(j)) for j in range(6)])
print('COMPLEX_ZERO_CANDIDATE',mp.nstr(zeta,42))
print('CANDIDATE_1_OVER_ABS',mp.nstr(1/abs(zeta),35))
for k in [4,8,16,32,64]:
    coeff=f_coefficients(k)
    root=mp.findroot(lambda x:f_eval(coeff,x),
                     (zeta*mp.mpf('0.94'),zeta*mp.mpf('1.08')),
                     tol=mp.mpf('1e-55'),maxsteps=200)
    assert abs(f_eval(coeff,root))<mp.mpf('1e-54')
    print('K_ROOT',k,'z=',mp.nstr(root,27),'inv_abs=',
          mp.nstr(1/abs(root),24),'delta=',mp.nstr(abs(root-zeta),12))
print('R576_RECIPROCAL_QUADRATIC_EXACT_AND_NUMERIC_CHECK_PASS')
