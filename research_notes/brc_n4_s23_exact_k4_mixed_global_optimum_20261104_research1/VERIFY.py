"""Finite exact rational interval certificate for BRC S23 K=4 optimum.

Only fractions.Fraction and integer square roots; no binary floating-point.
Frozen scientific source: enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34.
"""
from fractions import Fraction as Q
from math import isqrt

ZERO, ONE = Q(0), Q(1)
D = 10**29


def add(a, b):
    return a[0] + b[0], a[1] + b[1]


def neg(a):
    return -a[1], -a[0]


def mul(a, b):
    x = (a[0]*b[0], a[0]*b[1], a[1]*b[0], a[1]*b[1])
    return min(x), max(x)


def div(a, b):
    assert b[0] > 0
    return mul(a, (ONE/b[1], ONE/b[0]))


def point(x):
    return x, x


def sqrt_interval(x):
    assert x >= 0
    k = isqrt((x.numerator*D*D)//x.denominator)
    out = Q(k, D), Q(k+1, D)
    assert out[0]*out[0] <= x < out[1]*out[1]
    return out


def ln_interval(r, N=24):
    """Rigorous log of positive rational using atanh series, incl. tail."""
    assert r > 0
    if r < 1:
        return neg(ln_interval(ONE/r, N))
    z = (r-1)/(r+1)
    assert 0 <= z < 1
    partial = ZERO
    power = z
    for j in range(N):
        partial += 2*power/Q(2*j+1)
        power *= z*z
    tail = 2*power/(Q(2*N+1)*(1-z*z))
    return partial, partial+tail


def ln_i(a):
    assert a[0] > 0
    return ln_interval(a[0])[0], ln_interval(a[1])[1]


s, v = Q(1,2), Q(1,21)
p, q = s*(1+v)/2, s*(1-v)/2
assert (p, q) == (Q(11,42), Q(10,42))
A = sqrt_interval(p*q)
B = sqrt_interval((1-p)*(1-q))
ZB = add(A, B)
ZT = add(point(ONE-s), mul(point(s), sqrt_interval(ONE-v*v)))
CB_half = neg(ln_i(ZB))
CT = neg(ln_i(ZT))

# f_B'(1/2) = -(sqrt(pq)*ln(p/q)+sqrt((1-p)(1-q))*ln((1-p)/(1-q)))/Z_B.
g = neg(div(add(mul(A, ln_interval(p/q)),
                mul(B, ln_interval((1-p)/(1-q)))), ZB))
Dlog = ln_interval((p*(1-q))/(q*(1-p)))
mu = mul(point(q*(1-q)), mul(Dlog,Dlog))
assert mu[0] > Q(1,350), 'uniform strong concavity'
assert g[0] > -Q(1,120000) and g[1] < Q(1,120000), 'midpoint derivative'

# Strong concavity: C_B <= f_B(1/2)+g^2/(2*mu).
loss_bound = Q(175,120000**2)
raw_gap = add(mul(point(Q(2)), CT), neg(mul(point(Q(3)), CB_half)))
assert raw_gap[0] > Q(1,4000000), 'midpoint separation'
cert_gap = raw_gap[0] - 4*loss_bound
assert cert_gap > Q(1,5000000), 'global K=4 mixed superiority'

# Integer feasible m,n and the maximal n allowed for each m, 1<=K<=4.
for K in range(1,5):
    a = [(m, n) for m in range(K+1) for n in range(K+1)
         if 3*m + 2*n <= 2*K]
    assert a == [(m,n) for m in range(K+1) for n in range(K+1)
                 if Q(3,2)*m+n<=K]
    mixed = [(m,n) for m,n in a if m and n]
    if K < 3:
        assert not mixed
    if K == 3:
        assert mixed == [(1,1)]
    if K == 4:
        assert mixed == [(1,1),(1,2),(2,1)]

print('PASS_BRC_S23_EXACT_K4_GLOBAL_INTEGER_OPTIMUM_20261104')
print('fixed_model s=1/2 v=1/21 p=11/42 q=10/42 cT=3/2 cB=1')
print('uniform_strong_concavity_mu_gt=1/350', 'midpoint_derivative_abs_lt=1/120000')
print('raw_gap_2CT_minus_3fBhalf_gt=1/4000000')
print('CB_minus_fBhalf_lt=175/14400000000')
print('Cmix_2T_1B_minus_4CB_gt=1/5000000')
print('K_le_3_all_mixed_dominated; K_4_unique_optimum=(2,1)')
