#!/usr/bin/env python3
"""Exact-rational audit of the two-tail shared-gate affine-hull obstruction.

No source-native runtime, external package, float or random sample is used.
Finite verification tests concrete algebraic certificates. All-real coverage is
proved separately in RESEARCH.md, not inferred from these finite checks.
"""
from fractions import Fraction as F
from itertools import product

ZERO = F(0)
ONE = F(1)


def dot(a, b):
    return sum((x * y for x, y in zip(a, b)), ZERO)


def matvec(A, x):
    return tuple(dot(row, x) for row in A)


def inverse(A):
    n = len(A)
    aug = [[F(x) for x in row] + [F(i == j) for j in range(n)]
           for i, row in enumerate(A)]
    for j in range(n):
        pivot = next(i for i in range(j, n) if aug[i][j] != 0)
        aug[j], aug[pivot] = aug[pivot], aug[j]
        q = aug[j][j]
        aug[j] = [x / q for x in aug[j]]
        for i in range(n):
            if i != j:
                t = aug[i][j]
                aug[i] = [x - t * y for x, y in zip(aug[i], aug[j])]
    return tuple(tuple(row[n:]) for row in aug)


def determinant(A):
    n = len(A)
    B = [[F(z) for z in row] for row in A]
    d = ONE
    for j in range(n):
        pivot = next((i for i in range(j, n) if B[i][j] != 0), None)
        if pivot is None:
            return ZERO
        if pivot != j:
            B[j], B[pivot] = B[pivot], B[j]
            d = -d
        q = B[j][j]
        d *= q
        for i in range(j + 1, n):
            t = B[i][j] / q
            B[i] = [z - t * w for z, w in zip(B[i], B[j])]
    return d


def transpose(A):
    return tuple(zip(*A))


def p_lr(x, u, v):
    return (x, x*u, x*v, x*u*v)


def p_full(x, u, v_direct, v_via):
    return (x, x*u, x*v_direct, x*u*v_via)


def barycentric(p):
    a,b,c,d = p
    return (1-a, a-b-c+d, c-d, b-d, d)


def norm_inf_matrix(A):
    return max(sum(abs(z) for z in row) for row in A)


L = sorted(set(p_lr(*v) for v in product((ZERO, ONE), repeat=3)))
Fv = sorted(set(p_full(*v) for v in product((ZERO, ONE), repeat=4)))
assert len(L) == 5, (len(L), L)
assert len(Fv) == 7, (len(Fv), Fv)
extra = sorted(set(Fv)-set(L))
assert extra == [(ONE, ONE, ZERO, ONE), (ONE, ONE, ONE, ZERO)]
q1 = (ZERO, ZERO, -ONE, ONE)
q2 = (-ONE, ONE, ONE, -ONE)
for q in (q1, q2):
    assert max(dot(q,p) for p in L) == 0
    assert max(dot(q,p) for p in Fv) == 1
for p in L:
    lam = barycentric(p)
    assert all(z >= 0 for z in lam)
    assert sum(lam) == 1
assert barycentric(extra[0])[2] == -ONE
assert barycentric(extra[1])[1] == -ONE

# Rational behavior regression: convex LR coefficients and full feasibility.
grid = (ZERO, F(1,3), F(1,2), F(2,3), ONE)
for x,u,v in product(grid, repeat=3):
    p = p_lr(x,u,v)
    lam = barycentric(p)
    assert all(z >= 0 for z in lam)
    assert sum(lam) == 1
    assert p == tuple(sum((lam[j]*Lk[i] for j,Lk in enumerate([
        (ZERO,ZERO,ZERO,ZERO),
        (ONE,ZERO,ZERO,ZERO),
        (ONE,ZERO,ONE,ZERO),
        (ONE,ONE,ZERO,ZERO),
        (ONE,ONE,ONE,ONE),
    ])), ZERO) for i in range(4))
for x,u,v_direct,v_via in product(grid, repeat=4):
    a,b,c,d = p_full(x,u,v_direct,v_via)
    assert ZERO <= b <= a <= ONE and ZERO <= c <= a and ZERO <= d <= b

# Current predecessor's exact path-model four-observer map (2026-10-31 10:42).
M = (
    (F(0), F(3,512), F(0), F(9,512)),
    (F(0), F(3,256), F(0), F(3,256)),
    (F(31,32), F(1,32), F(3,32), F(3,128)),
    (F(15,32), F(1,32), F(1,16), F(1,64)),
)
b0 = (F(1,8), F(1,8), ONE, ONE)
assert determinant(M) == F(153,67108864)
Minv = inverse(M)
assert tuple(tuple(dot(row, col) for col in transpose(M)) for row in Minv) == (
    (ONE,ZERO,ZERO,ZERO),(ZERO,ONE,ZERO,ZERO),
    (ZERO,ZERO,ONE,ZERO),(ZERO,ZERO,ZERO,ONE))

h1 = matvec(transpose(Minv), q1)
h2 = matvec(transpose(Minv), q2)
assert h1 == (F(448,17),F(3424,51),F(480,17),-F(992,17))
assert h2 == (-F(320,3),F(160,3),-F(32),F(64))
assert tuple(v*F(51,32) for v in h1) == (F(42),F(107),F(45),-F(93))
obs = lambda p: tuple(b0[i]+matvec(M,p)[i] for i in range(4))
for h in (h1,h2):
    assert max(dot(h,obs(p)) for p in Fv) - max(dot(h,obs(p)) for p in L) == ONE
om = obs(extra[0]); op = obs(extra[1])
assert om == (F(19,128),F(19,128),F(259,128),F(97,64))
assert op == (F(67,512),F(35,256),F(67,32),F(25,16))
assert ONE / sum(map(abs,h1)) == F(51,9184)
assert ONE / sum(map(abs,h2)) == F(1,256)

pstar = (ONE,F(1,2),F(1,2),F(1,2))
assert pstar == tuple((r+s)/2 for r,s in zip(
    p_lr(ONE,ZERO,ZERO),p_lr(ONE,ONE,ONE)))
assert pstar == p_full(ONE,F(1,2),F(1,2),ONE)
assert pstar[0]*pstar[3] - pstar[1]*pstar[2] == F(1,4)
assert norm_inf_matrix(Minv) == F(13024,51)
assert ONE/(16*norm_inf_matrix(Minv)) == F(51,208384)
assert obs(pstar) == (F(35,256),F(35,256),F(523,256),F(195,128))

print('LR_BINARY_UNIQUE', len(L), 'FULL_BINARY_UNIQUE', len(Fv))
print('EXTRA_VERTICES', extra)
print('M_DET', determinant(M))
print('NORMALIZED_SEPARATORS', h1, h2)
print('FULL_WITNESS_MINUS', om, 'FULL_WITNESS_PLUS', op)
print('FULL_VS_LR_CONV_DIST_LINF_LOWER', F(51,9184), F(1,256))
print('REAL_LR_NONMEMBER', obs(pstar))
print('REAL_LR_NONMEMBER_DIST_LINF_LOWER', F(51,208384))
print('RATIONAL_REGRESSION_LR', len(grid)**3, 'FULL',len(grid)**4)
print('PASS_EXACT_R5_TWO_TAIL_AFFINE_RANK_FOUR_NO_GO')
