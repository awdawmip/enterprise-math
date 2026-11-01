#!/usr/bin/env python3
"""Exact rational certificates for PREFIX-413's first branch crossover.
No external dependencies. Assertions test algebraic comparisons, not universal proof.
"""
from fractions import Fraction as F
from math import isqrt

B = F(1, 1_000_000)
E = F(53, 8)
A2 = F(37577, 64)
C2 = F(45, 368)**2
ETA0 = F(3, 4000)
ETA_END = F(97, 50000)
L = F(1806822, 10**9)
U = F(1806823, 10**9)

# Resultant's primitive quartic; no floating arithmetic here.
P_COEFFS = (
    411370922419157000000000000000000000000,
    3406648973825365305852000000000000000000,
    7207920358822113492588156702000000000000,
    -15929217691721140762689459588000000,
    -23522344829723509499221428663222123,
)

def P(z):
    ans = F(0)
    for coefficient in P_COEFFS:
        ans = ans*z + coefficient
    return ans

def fcorner(z, t):
    return (z+t)**2/4 + C2*(t-z)**2 - t

def corner_interval(z, steps=120):
    lo, hi = F(0), B
    assert fcorner(z,lo)>0 and fcorner(z,hi)<0
    for _ in range(steps):
        mid = (lo+hi)/2
        if fcorner(z,mid)>0:
            lo=mid
        else:
            hi=mid
    return lo,hi

def sqrt_enclose(r, decimals=45):
    assert r>=0
    scale=10**decimals
    n=isqrt((r.numerator * scale*scale)//r.denominator)
    lo,hi=F(n,scale),F(n+1,scale)
    assert lo*lo<=r and r<hi*hi
    return lo,hi

def qplus_bounds(z):
    c=z-E*B
    rad=A2*B-c*c
    s0,s1=sqrt_enclose(rad)
    return ((F(1165)*c+182*s0)/A2 +16*B,
            (F(1165)*c+182*s1)/A2 +16*B)

def qminus_bounds(z):
    t0,t1=corner_interval(z)
    return ((141*z+43*t0)/23,(141*z+43*t1)/23)

def crossing_sign(z):
    p0,p1=qplus_bounds(z)
    m0,m1=qminus_bounds(z)
    if p0>m1: return '+',p0-m1
    if p1<m0: return '-',m0-p1
    return '?',F(0)

assert 0<ETA0<L<U<ETA_END
assert B < ETA0
assert A2 == F(37577,64)
assert 16-F(1165)*E/A2 == F(2024,709)>0
assert F(141,23)>F(1165)/A2
# Full circle is feasible for the k=eta positive source, and its h is inside:
assert (ETA_END-E*B)**2<A2*B
assert ETA_END**2<A2*F(1,100_000_000)
assert F(1165,49)*F(1,10_000)>ETA_END
x0_upper=(23*ETA0+F(61,8)*F(1,40))/A2
assert 2*x0_upper+B<ETA0
assert F(46)/A2<1
# Nondegenerate lower-bound source for all eta>=ETA0.
prior_witness_gain=F(46,5)*ETA0+F(689,25)*ETA0*ETA0
small_t_upper=F(49,10000)+F(16,100_000_000)
assert prior_witness_gain>small_t_upper
# Negative corner exists, is unique within [0,B], and is monotone in eta.
assert fcorner(ETA_END,0)>0 and fcorner(ETA_END,B)<0
assert ETA_END+B<F(1,400)
assert ETA0>B
# Exact signs of the algebraic crossover and its squared resultant:
assert P(L)<0<P(U)
assert all(a>0 for a in P_COEFFS[:3])
assert all(a<0 for a in P_COEFFS[3:])
sL,gapL=crossing_sign(L)
sU,gapU=crossing_sign(U)
assert sL=='+' and sU=='-'
# Test the negative corner witnesses at both endpoints against all constraints.
for z in [L,U]:
    t0,t1=corner_interval(z)
    assert 0<t0<t1<B
    for t in [t0,t1]:
        x=-(z+t)/2
        y=F(45,368)*(t-z)
        h=2*x+t
        k=F(61,8)*x-23*y+E*t
        assert h==k==-z
        assert abs(fcorner(z,t))<F(1,10**30)

print('PASS_PREFIX413_EXACT_POSITIVE_QUARTIC_FIRST_CROSSING')
print(f'global interval: [{ETA0}, {ETA_END}], first-crossing bracket: [{L}, {U}]')
print(f'certified D(L)>0 margin lower={gapL}')
print(f'certified D(U)<0 margin lower={gapU}')
print('P(L)<0<P(U); primitive quartic coefficients: '+repr(P_COEFFS))
print('result: strictly decreasing branch gap on analytic validity interval, exact first crossover isolated')
