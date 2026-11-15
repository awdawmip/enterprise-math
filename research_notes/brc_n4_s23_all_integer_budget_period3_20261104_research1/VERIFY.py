"""Exact rational certificate, BRC N4 S23 all integer budgets (s=1/2,h=1/42).

Frozen science: awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34
Independent of floating-point maximizers. Uses fractions and integer square root.
"""
from fractions import Fraction as F
from math import isqrt

D = 10**29
O, Z = F(1), F(0)

def point(x): return (x, x)
def plus(a, b): return (a[0]+b[0], a[1]+b[1])
def neg(a): return (-a[1], -a[0])
def times(a, b):
    z = (a[0]*b[0], a[0]*b[1], a[1]*b[0], a[1]*b[1])
    return min(z), max(z)
def quotient(a, b):
    assert b[0] > 0
    return times(a, (O/b[1], O/b[0]))
def sqrt_i(x):
    assert x >= 0
    k = isqrt(x.numerator * D * D // x.denominator)
    ans = (F(k,D), F(k+1,D))
    assert ans[0]**2 <= x < ans[1]**2
    return ans

def log_r(x, count=24):
    assert x > 0
    if x < 1: return neg(log_r(1/x, count))
    z = (x-1)/(x+1)
    power = z
    series = Z
    for j in range(count):
        series += 2*power/F(2*j+1)
        power *= z*z
    tail = 2*power/(F(2*count+1)*(1-z*z))
    return series, series+tail

def log_i(x):
    assert x[0] > 0
    return log_r(x[0])[0], log_r(x[1])[1]

s, v = F(1,2), F(1,21)
p, q = s*(1+v)/2, s*(1-v)/2
assert (p,q) == (F(11,42), F(10,42))
A = sqrt_i(p*q)
B = sqrt_i((1-p)*(1-q))
zb = plus(A, B)
zt = plus(point(1-s), times(point(s), sqrt_i(1-v*v)))
b = neg(log_i(zb))                  # f_B(1/2) interval
c = neg(log_i(zt))                  # max f_T = f_T(1/2) interval

# Exponential family: f_B''(t)=-pi_t(1-pi_t)*logodds_diff**2.
logodds = log_r((p*(1-q))/(q*(1-p)))
mu = times(point(q*(1-q)), times(logodds, logodds))
g = neg(quotient(plus(times(A, log_r(p/q)), times(B, log_r((1-p)/(1-q)))), zb))
assert mu[0] > F(1,350)
assert -F(1,120000) < g[0] <= g[1] < F(1,120000)
eps = F(175,120000**2)             # d-b<eps, d=max_t f_B(t)
assert b[0] > F(1,10000)
assert 2*b[0]-c[1] > F(1,10000)
raw_gap = 2*c[0]-3*b[1]
assert raw_gap > F(1,4000000)
# Delta = 2c-3d > raw_gap-3eps > 2eps, making the 3B->2T exchange safe.
assert raw_gap-3*eps > 2*eps
assert F(1,4000000)-5*eps > F(1,6000000)
# With delta>0, c>3d/2>d; 2d-c>=2b-c>1/10000;
# hence all alternative linear-optimization choices have gap >2eps.
assert b[0]/2 > 2*eps
assert F(1,10000) > 2*eps

# Independent exhaustive finite corroboration: all feasible counts for K=1..100.
# The real-parameter theorem is proved by the exchange and residue argument, not this loop.
tested = 0
for K in range(1,101):
    a, r = divmod(K, 3)
    opt = (2*a, r)
    m0,n0=opt
    witness_lower = m0*c[0]+n0*b[0]
    for m in range((2*K)//3 + 1):
        for n in range((2*K-3*m)//2 + 1):
            if (m,n)==opt: continue
            competitor_upper = m*c[1]+n*(b[1]+eps)
            assert witness_lower > competitor_upper, (K,m,n,opt)
            tested+=1

print('PASS_BRC_S23_ALL_INTEGER_BUDGET_GLOBAL_OPTIMUM_EXACT_20261104')
print('model: s=1/2, v=1/21, p=11/42, q=10/42, costs T=3/2, B=1')
print('epsilon=175/14400000000 ; d-b<epsilon')
print('bounds: b>1/10000 ; 2b-c>1/10000 ; 2c-3b>1/4000000')
print('exchange: 2c-3d>2epsilon; all nonoptimal C gaps>1/6000000')
print('for every integer K>=1, unique optimal (m,n)=(2*(K//3),K%3)')
print('K<=100 exact rational exhaustive competing allocations:', tested)
print('shared-exponent objective: C(m,n)=max_t[m*f_T(t)+n*f_B(t)]')
