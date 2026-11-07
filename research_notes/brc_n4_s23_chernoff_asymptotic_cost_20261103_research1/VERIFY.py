#!/usr/bin/env python3
"""Exact rational enclosure of the Chernoff per-cost comparison; standard library only.
All assertions have rational-arithmetic or integer basis. The asymptotic theorem
uses a separate analytic tilted-measure proof in PROOF.md.
"""
from fractions import Fraction as Q
from math import isqrt

D=10**14

def sqrt_brackets(n):
    k=isqrt(n*D*D)
    return Q(k,D),Q(k+1,D)

def log_brackets_for_ratio_one_plus(x):
    # log((1+x)/(1-x))=2 sum_{j>=0}x^(2j+1)/(2j+1) for rational 0<x<1.
    assert Q(0)<x<Q(1)
    k=4
    lower=2*sum((x**(2*j+1))/Q(2*j+1) for j in range(k+1))
    tail=2*(x**(2*k+3))/((2*k+3)*(1-x*x))
    return lower,lower+tail

S110=sqrt_brackets(110)
S5402=sqrt_brackets(5402)
L1=log_brackets_for_ratio_one_plus(Q(1,21)) # ln(11/10)
L0=log_brackets_for_ratio_one_plus(Q(1,147)) # ln(74/73)
# Z_B(1/2) = (sqrt(110)+sqrt(5402))/84
z0_lo=(S110[0]+S5402[0])/84
assert z0_lo>Q(999837949,10**9)
# Z_T = 3/4 + sqrt(110)/42
zt_hi=Q(3,4)+S110[1]/42
assert zt_hi<Q(999716393,10**9)
# Z_B'(1/2) = sqrt110/84 * ln(11/10) - sqrt5402/84 * ln(74/73)
dlo=S110[0]*L1[0]/84 - S5402[1]*L0[1]/84
dhi=S110[1]*L1[1]/84 - S5402[0]*L0[0]/84
assert -Q(45,10**7)<dlo<=dhi<Q(45,10**7)
# Z_B''(t) >= (10/84)*ln(11/10)^2+(73/84)*ln(74/73)^2
mlo=Q(10,84)*L1[0]**2 + Q(73,84)*L0[0]**2
assert mlo>Q(124,100000)
L=Q(999837940,10**9)
U=Q(999716393,10**9)
zmin_cert=Q(999837949,10**9)-Q(45,10**7)**2/(2*Q(124,100000))
assert zmin_cert>L
assert L**7>U**4
print('PASS_BRC_S23_ASYMPTOTIC_CHERNOFF_COST_STRICT_CERT_20261103')
print('source_pair: p=11/21, q=10/21, s=1/4, costs T=7/4 B=1')
print('sqrt bracket denominator=',D,'log_series_terms=5, rational remainder')
print('Z_B_half > 999837949/1000000000')
print('abs_Z_B_prime_half < 45/10000000')
print('Z_B_second_all_t > 124/100000')
print('Z_B_min > 999837940/1000000000 = L')
print('Z_T < 999716393/1000000000 = U')
print('L^7 > U^4: exact=',L**7>U**4)
print('strict_result: -ln(Z_T)/(7/4) > -ln(min_t Z_B(t))')
