#!/usr/bin/env python3
"""Exact author checks: universal root masking is proved separately in PROOF.md."""
from fractions import Fraction as F
from itertools import product
R = (F(1, 2), F(1), F(3, 2))
Y = (F(1, 4), F(1), F(2))
Q1 = {'a': F(1, 2), 'b': F(1, 2)}
Q2 = {'a': (F(1, 4), F(1, 2), F(1, 4)), 'b': (F(1, 3),) * 3}
P2 = {h: tuple(q*r for q,r in zip(Q2[h], R)) for h in Q2}
Q3 = {R[0]: (F(5, 7), F(1, 4), F(1, 28)),
      R[1]: (F(15, 28), F(1, 16), F(45, 112)),
      R[2]: (F(1, 28), F(7, 16), F(59, 112))}
P3 = {r: tuple(y*q/r for q,y in zip(Q3[r], Y)) for r in R}
for h in Q2:
    assert sum(Q2[h]) == sum(P2[h]) == 1
    assert all(x > 0 for x in Q2[h] + P2[h])
for r in R:
    assert sum(Q3[r]) == sum(P3[r]) == 1
    assert sum(y*q for y,q in zip(Y,Q3[r])) == r
    assert all(x > 0 for x in Q3[r] + P3[r])
qbar = tuple(sum(Q1[h]*Q2[h][i] for h in Q2) for i in range(3))
assert qbar == (F(7, 24), F(5, 12), F(7, 24))
assert Q2['a'] != Q2['b']  # not strongly LR lumpable at time 1
calls = tuple(sum(q*max(F(0), y-F(1)) for q,y in zip(Q3[r], Y)) for r in R)
violation = calls[1] - (calls[0]+calls[2])/2
assert calls == (F(1,28), F(45,112), F(59,112))
assert violation == F(27,224) > 0  # mu_1 NOT convex-dominated by endpoints

def support(A, B, C, D):
    H = lambda x: min(A*x, B)
    def phi(r):
        return min(H(r), C*r + D + sum(q*H(y) for q,y in zip(Q3[r], Y)))
    m, gamma = H(F(1)), C+D
    d0 = m-phi(F(1))
    G = 2*phi(F(1)) - phi(F(1,2)) - phi(F(3,2))
    da, db = d0 + G/4, d0 + G/3
    dbar, dmin = (da+db)/2, min(da,db)
    assert d0 >= 0 and G >= -2*d0
    assert dmin >= 0 and dbar <= 2*dmin
    f = tuple(sum(q*phi(r) for q,r in zip(Q2[h],R)) for h in Q2)
    full = min(m, gamma + sum(min(m,gamma+v) for v in f)/2)
    lr = min(m, gamma + min(m,gamma+sum(f)/2))
    assert full == lr, (A,B,C,D,full,lr)
    return full

def observe(pooled):
    ep = eq = tp = tq = F(0)
    def walk(t, h, r, y, pm, qm):
        nonlocal ep, eq, tp, tq
        if t == 0: actions = {'C': F(1)}
        elif pooled:
            if t == 1: actions = {'P': F(1,2), 'C': F(1,2)}
            elif t == 2: actions = {'P': F(1,7), 'C': F(6,7)} if r == R[2] else {'P': F(1)}
            else: actions = {'Q': F(1)} if y == Y[0] else {'P': F(1)}
        else:
            if t == 1: actions = {'C': F(1)} if h == 'a' else {'P': F(1)}
            elif t == 2: actions = {'C': F(1)} if h == 'a' and r == R[2] else {'P': F(1)}
            else: actions = {'Q': F(1)} if y == Y[0] else {'P': F(1)}
        assert sum(actions.values()) == 1
        for action, w in actions.items():
            p, q = pm*w, qm*w
            if action == 'P': eq += q
            elif action == 'Q': ep += p
            else:
                assert t < 3
                tp += p; tq += q
                if t == 0:
                    for hh in Q1: walk(1, hh, None, None, p*Q1[hh], q*Q1[hh])
                elif t == 1:
                    for i, rr in enumerate(R): walk(2, h, rr, None, p*P2[h][i], q*Q2[h][i])
                else:
                    for i, yy in enumerate(Y): walk(3, h, r, yy, p*P3[r][i], q*Q3[r][i])
    walk(0, None, None, None, F(1), F(1))
    return ep, eq, tp, tq

raw, pooled = observe(False), observe(True)
assert raw == pooled == (F(1,896), F(223,224), F(27,16), F(13,8))
grid = [F(x,2) for x in (-6,-4,-2,-1,0,1,2,4,6)]
for coefficients in product(grid, repeat=4):
    support(*coefficients)
print('Q3=',Q3)
print('STRICT_POSITIVE_NORMALIZED_MEAN_PRESERVING=PASS')
print('TIME1_STRONG_LR_LUMPABILITY=FALSE')
print('CONVEX_ORDER_VIOLATION_THETA_1='+str(violation))
print('RAW_OBSERVER='+','.join(map(str,raw)))
print('LR_ONLY_OBSERVER='+','.join(map(str,pooled)))
print('SIGNED_SUPPORT_GRID_TESTS='+str(len(grid)**4))
print('SIGNED_SUPPORT_GRID_EXACT_EQUALITY=PASS')
print('ALL_REAL_COEFFICIENTS=PROVED_IN_PROOF_MD_NOT_BY_GRID')
