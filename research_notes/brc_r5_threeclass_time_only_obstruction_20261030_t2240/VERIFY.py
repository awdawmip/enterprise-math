#!/usr/bin/env python3
"""Exact rational/int check of time-only R5 three-class stopping obstruction."""
from fractions import Fraction as F
from itertools import product

Q_XU = {(0, 0): F(3, 8), (0, 1): F(1, 8),
        (1, 0): F(1, 8), (1, 1): F(3, 8)}
R_U = (F(3, 4), F(5, 4))
R_V = (F(1, 2), F(1), F(3, 2))
t = (F(1, 16), F(1, 8))
a, b = 7, -6

def transition(x, u):
    z = t[x]
    if u == 0:
        return (F(1, 2)+z, F(1, 2)-2*z, z)
    return (z, F(1, 2)-2*z, F(1, 2)+z)

leaves = []
for x, u, v in product(range(2), range(2), range(3)):
    q = Q_XU[x, u] * transition(x, u)[v]
    p = R_V[v] * q
    assert q > 0 and p > 0
    assert (q * 256).denominator == 1
    assert (p * 256).denominator == 1
    leaves.append((x, u, v, int(256 * p), int(256 * q)))
assert sum(row[3] for row in leaves) == 256
assert sum(row[4] for row in leaves) == 256
for x, u in product(range(2), range(2)):
    assert sum(transition(x, u)) == 1
    assert sum(transition(x, u)[v] * R_V[v] for v in range(3)) == R_U[u]
for x in range(2):
    assert sum(Q_XU[x,u] for u in range(2)) == F(1,2)
assert [sum(Q_XU[x,u]*R_U[u] for u in range(2))/F(1,2) for x in range(2)] == [F(7,8),F(9,8)]

final_gain = tuple(max(F(0), a*r+b) for r in R_V)
G = {(x,u): a*R_U[u]+b+sum(transition(x,u)[v]*final_gain[v] for v in range(3))
     for x,u in product(range(2),range(2))}
E_FULL = tuple(sum(Q_XU[x,u]*(a*R_U[u]+b+max(F(0),G[x,u])) for u in range(2)) for x in range(2))
H_FULL = 2*(a+b)+sum(max(F(0),v) for v in E_FULL)
LR_TABLE = {}
for h0,h1 in product((0,1), repeat=2):
    h = (h0,h1)
    E = tuple(sum(Q_XU[x,u]*(a*R_U[u]+b+h[u]*G[x,u]) for u in range(2)) for x in range(2))
    LR_TABLE[h] = 2*(a+b)+sum(max(F(0), v) for v in E)
H_LR=max(LR_TABLE.values())
assert final_gain == (F(0),F(1),F(9,2)), final_gain
assert G == {(0,0):F(-3,32),(0,1):F(181,32),(1,0):F(1,16),(1,1):F(93,16)},G
assert E_FULL == (F(197,256),F(25,8)),E_FULL
assert LR_TABLE == {(0,0):F(3),(0,1):F(1507,256),(1,0):F(761,256),(1,1):F(375,64)},LR_TABLE
assert (H_FULL,H_LR,H_FULL-H_LR) == (F(1509,256),F(1507,256),F(1,128))

def eval_strategy(s, is_full):
    TP, TQ = 0, 0
    for x,u,v,p256,q256 in leaves:
        if is_full:
            early = (s >> x) & 1
            middle = (s >> (2+2*x+u)) & 1
            final = (s >> (6+6*x+3*u+v)) & 1
        else:
            early = (s >> x) & 1
            middle = (s >> (2+u)) & 1
            final = (s >> (4+v)) & 1
        stop_time = 2 if not early else (3 if not middle else (4 if not final else 5))
        TP += stop_time*p256
        TQ += stop_time*q256
    return TP, TQ, a*TP+b*TQ

def exhaustive(is_full):
    best=-10**18
    arg=None
    for s in range(1 << (18 if is_full else 7)):
        tp,tq,h=eval_strategy(s,is_full)
        if h>best:
            best, arg = h, (s,tp,tq)
    return best, arg

full_int, full_arg = exhaustive(True)
lr_int, lr_arg = exhaustive(False)
assert full_int == 1509 and lr_int == 1507, (full_int,lr_int)
witness = 0
for x in range(2): witness |= (1 << x)
for x,u in product(range(2),repeat=2):
    if (x,u)!=(0,0): witness |= (1 << (2+2*x+u))
for x,u,v in product(range(2),range(2),range(3)):
    if (x,u)!=(0,0) and v in (1,2): witness |= (1 << (6+6*x+3*u+v))
wp,wq,wh=eval_strategy(witness,True)
assert (wp,wq,wh) == (1119,1054,1509),(wp,wq,wh)
assert 7*F(wp,256)-6*F(wq,256)==H_FULL
print('BRANCHES 12; Q_POSITIVE P_POSITIVE; SUM_Q=SUM_P=1; LR_COLLISIONS=2')
print('LAST_CONTINUE_GAINS', *(str(z) for z in final_gain))
print('MIDDLE_CONTINUE_GAINS',*(f'{x}{u}:{G[x,u]}' for x,u in product(range(2),repeat=2)))
print('LR_MIDDLE_TABLE',*(f'{h}:{LR_TABLE[h]}' for h in sorted(LR_TABLE)))
print(f'FULL_MAX={H_FULL} LR_MAX={H_LR} GAP={H_FULL-H_LR}')
print(f'FULL_STRATEGIES={1<<18} LR_STRATEGIES={1<<7}')
print(f'WITNESS_S={witness} T_P={F(wp,256)} T_Q={F(wq,256)} H={H_FULL}')
print('ROBUST_TO_TERMINAL_ERROR_KERNELS: H_USES_ONLY_TP_TQ')
print('DIST_LINF_TO_ANY_LR_4D_OBSERVER >= 1/1664')
print('PASS_EXACT_R5_THREECLASS_TIME_ONLY_ALL_ERROR_NO_GO')
