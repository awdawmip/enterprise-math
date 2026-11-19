#!/usr/bin/env python3
"""Exact Fraction verification of an independent C-infinity price-prior counterexample.
No numeric bump integral or native BRC Bellman rerun is needed: its fixed mass cancels.
"""
from fractions import Fraction as F
m0,m1=F(11457,512),F(1461,64)
x=m0+(m1-m0)/3
y=m0+2*(m1-m0)/3
s0,s1=F(441,1000),F(442,1000)
c=F(1,20)
L=lambda m:(4*m+2647)/3696
U=lambda m:(64*m+1411)/3840
b=lambda m,z:F(1,27)-m/54+F(10,9)*z
invz=lambda m,v:F(9,10)*(v-F(1,27)+m/54)
t=invz(y,s1)
blx,bly,b_upper=b(x,L(x)),b(y,L(y)),b(y,U(y))
assert m0 < x < y < m1
assert bly < s0 < s1 < blx < b_upper
assert L(x) < t < U(x)
assert L(y) < t < U(y)
assert b(y,t)==s1
prob_x=(t-L(x))/(U(x)-L(x))
prob_y=((s1-bly)+c)/((b_upper-bly)+c)
assert prob_x==F(7177,9000)
assert prob_y==F(47,50)
assert prob_y-prob_x==F(1283,9000)>0
print('m_low=',x,'m_high=',y,'z_threshold=',t)
print('b_lower_low=',blx,'b_lower_high=',bly,'b_upper=',b_upper)
print('CDF_low=',prob_x,'CDF_high=',prob_y,'difference=',prob_y-prob_x)
print('PASS: exact positive C-infinity bump prior refutes universal conditional FOSD, without evaluating the bump normalizer')
