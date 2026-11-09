#!/usr/bin/env python3
"""PREFIX634: exact Fraction certificate for the q-uniform BRC valley separation.

Upstream analytic lemmas: PREFIX621, 622, 625, 627, 631, 632.
This script checks the NEW arithmetic tail identity and constants.
"""
from fractions import Fraction as F
from math import comb
L=5244748236
n=25
weights=[F(comb(n+r,n),2**(n+r+1)) for r in range(n)]
tail=1-sum(weights,F(0))
closed=F(1,2)+F(comb(50,25),2**51)
assert tail==closed and tail>F(1,2)
assert tail>F(comb(50,25),2**51)
slope25=25*(F(5,6)**24-F(1,6)**24)
prob25=F(217,256)**25
m_old=F(comb(50,25),2**51)*prob25*slope25
m=tail*prob25*slope25
assert m>m_old>0
assert m/m_old==F(156538814160047,15801325804719)
gap=m/(24*L)
kappa=m*m/L
assert gap>F(1,50000000000000)
assert gap>F(9,4*10**15)*9
assert kappa>0
print('ALL_CHECKS_PASS')
print('neg_bin_tail=',tail)
print('slope_m=',m)
print('q12_q24_gap=',gap)
print('strong_concavity_modulus=',kappa)
print('display_gap=',float(gap))
