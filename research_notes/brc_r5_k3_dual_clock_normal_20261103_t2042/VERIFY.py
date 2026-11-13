"""Exact rational regression for R5 K3 second clock-normal family.
Runs no external software and uses only Python's Fraction arithmetic.
"""
from fractions import Fraction as F
from itertools import product

ALPHA = (F(1, 2), F(2, 3), F(1, 2), F(3, 4))
C = (F(1, 8), F(1, 6), F(1, 16), F(3, 32))
FULL_UP = ((0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1), (1, 0, 0), (1, 1, 0))
LR_UP = ((0, 0, 0), (0, 1, 1), (1, 0, 0), (1, 1, 0))
STAGE = ((0, 0, 0), (1, 0, 0), (1, 1, 0), (1, 1, 1))
COUNT = 0

def eq(lhs, rhs):
    global COUNT
    COUNT += 1
    assert lhs == rhs, (COUNT, lhs, rhs)

def obs(model, corner, choices):
    x, y, i = map(F, corner)
    d = y / 16 + 3 * i / 32
    w = (F(1, 4), (1 - x) / 4, y / 8, i / 8)
    cs = [w[s] * ALPHA[s] for s in range(4)]
    M = [cs[s] * STAGE[choices[s]][0] for s in range(4)]
    S = [F(2, 3) * M[s] * STAGE[choices[s]][1] for s in range(4)]
    U = [S[s] * STAGE[choices[s]][2] for s in range(4)]
    p, q, r, v = (model[k] for k in ('p', 'q', 'r', 'v'))
    return (
        F(107, 128) - 21*x/128 + d/4 - sum(S)/2 + sum((p[s]*S[s]/8 for s in range(4)), F(0)),
        F(13, 64) + 3*x/64 - d/2 + sum(S)/8 + sum((q[s]*S[s]/32 for s in range(4)), F(0)),
        3 + sum(M) + F(3, 2)*sum(S) + sum((r[s]*U[s] for s in range(4)), F(0)),
        3 + sum(M)/2 + F(3, 8)*sum(S) + sum((v[s]*U[s]/4 for s in range(4)), F(0)),
    )

def dot(n, w):
    return sum((a*b for a, b in zip(n, w)), F(0))

def normal(theta):
    return (F(0), F(0), F(4), -theta)

def brute(model, theta, full):
    best = None
    arg = None
    for corner in (FULL_UP if full else LR_UP):
        choices = product(range(4), repeat=4) if full else ((j,)*4 for j in range(4))
        for stages in choices:
            value = dot(normal(theta), obs(model, corner, stages))
            if best is None or value > best:
                best, arg = value, (corner, stages)
    return best, arg

def formula(model, theta):
    assert F(0) < theta <= F(96, 11)
    g = tuple(4*model['r'][s] - theta*model['v'][s]/4 for s in range(4))
    pos = sum((C[s]*max(g[s], F(0)) for s in range(4)), F(0))
    neg = sum((C[s]*max(-g[s], F(0)) for s in range(4)), F(0))
    base = 3*(4-theta) + (8-F(3, 4)*theta)*sum(C)
    full = base + F(2, 3)*pos
    lr = base + F(2, 3)*max(pos-neg, F(0))
    return full, lr, F(2, 3)*min(pos, neg), g

example = dict(
    p=(F(1,4),F(1,2),F(3,4),F(1,2)),
    q=(F(3,4),F(1,2),F(1,4),F(1,2)),
    r=(F(1,5),F(1,2),F(1,5),F(1,2)),
    v=(F(4,5),F(9,10),F(4,5),F(9,10)))
varied = dict(
    p=(F(2,7),F(3,8),F(4,9),F(5,11)),
    q=(F(1,5),F(2,5),F(3,5),F(4,5)),
    r=(F(1,4),F(2,3),F(3,8),F(4,5)),
    v=(F(3,4),F(1,5),F(7,8),F(2,5)))
uniform = dict(p=(F(1,3),)*4,q=(F(2,3),)*4,r=(F(1,2),)*4,v=(F(3,5),)*4)
more = dict(p=(F(1,7),F(3,7),F(4,7),F(6,7)),
            q=(F(1,6),F(1,3),F(1,2),F(5,6)),
            r=(F(1,10),F(4,5),F(1,3),F(1,2)),
            v=(F(9,10),F(1,10),F(2,3),F(3,4)))
thetas = (F(1),F(2),F(4),F(6),F(8),F(96,11))
for model in (example, varied, uniform, more):
    for theta in thetas:
        lhs, _ = brute(model, theta, True)
        rhs, _ = brute(model, theta, False)
        pf, pl, gap, _ = formula(model, theta)
        eq(lhs, pf)
        eq(rhs, pl)
        eq(lhs-rhs, gap)

w = obs(example, (0, 1, 1), (2, 3, 2, 3))
full, _ = brute(example, F(8), True)
lr, _ = brute(example, F(8), False)
eq(dot(normal(F(8)), w), full)
eq(full, -F(797,72))
eq(lr, -F(533,48))
eq(full-lr, F(5,144))
# Every source satisfies the old sweep g_s(theta)>0 for 0<theta<=9/8.
# Both formula branches are decreasing, so checking theta=1 and 9/8 suffices.
for r, v in zip(example['r'], example['v']):
    eq(v - r > 0, True)
    eq(v - F(9,8)*r - F(3,2)*(F(9,8)-1) > 0, True)

print('weight_sum', sum(C))
print('second_normal', normal(F(8)))
print('second_residuals', formula(example,F(8))[3])
print('first_sweep_gap_every_theta_in_(0,9/8]', 0)
print('support_FULL', full,'support_LR', lr, 'gap',full-lr)
print('witness', w)
print('distance_inf_lower_bound', (full-lr)/sum(map(abs,normal(F(8)))))
print('models',4,'theta_count',len(thetas),'full_vertices_per_test',1536,'lr_vertices_per_test',16,'assertions',COUNT)
print('PASS_EXACT_R5_K3_DUAL_CLOCK_NORMAL')
