#!/usr/bin/env python3
"""Exact N=4 hidden-kernel residual: first-branch bit is not enough.

External finite positive BRC-style branch-mass ledger (not P000 dynamics).
All arithmetic is Python Fraction; this is not a native Heartbeat/Shor run.
"""
from fractions import Fraction as F
from itertools import product

A, B, C, D = F(1), F(1), F(-33, 8), F(17, 4)

def terminal(l):
    return min(A * l, B)

def continuation_step(l):
    return C * l + D

# Ordered history -> conditional symbol, Q mass, P mass.
def transitions(h):
    if len(h) == 0:
        return [
            ('a', F(1, 6), F(1, 6)),
            ('b', F(1, 6), F(1, 6)),
            ('c', F(1, 6), F(1, 3)),
            ('d', F(1, 2), F(1, 3)),
        ]
    if len(h) == 1:
        return [('x', F(1, 2), F(1, 2)), ('y', F(1, 2), F(1, 2))]
    if len(h) == 2 and h == ('a', 'x'):
        return [('u', F(1, 2), F(1, 4)), ('v', F(1, 2), F(3, 4))]
    if len(h) == 2:
        return [('u', F(1, 2), F(1, 2)), ('v', F(1, 2), F(1, 2))]
    if len(h) == 3:
        return [('s', F(1, 2), F(1, 2)), ('t', F(1, 2), F(1, 2))]
    raise ValueError('terminal history')

P, Q = {(): F(1)}, {(): F(1)}
for n in range(4):
    for h in [h for h in tuple(Q) if len(h) == n]:
        tx = transitions(h)
        assert all(q > 0 and p > 0 for _, q, p in tx)
        assert sum((q for _, q, _ in tx), F(0)) == 1
        assert sum((p for _, _, p in tx), F(0)) == 1
        for sym, q, p in tx:
            child = h + (sym,)
            Q[child], P[child] = Q[h]*q, P[h]*p
assert len(Q) == len(P) == 61  # root+4+8+16+32
assert sum((Q[h] for h in Q if len(h) == 4), F(0)) == 1
assert sum((P[h] for h in P if len(h) == 4), F(0)) == 1
L = {h: P[h]/Q[h] for h in Q}
assert L[('a',)] == L[('b',)] == L[('a','x')] == L[('a','y')] == 1
assert (L[('c',)],L[('d',)]) == (F(2),F(2,3))
assert (L[('a','x','u')],L[('a','x','v')]) == (F(1,2),F(3,2))

# Exact unrestricted Bellman recursion. It is valid for every nonanticipative
# randomized stopping/decision policy because each action has linear cost.
V = {}
for n in range(4,-1,-1):
    for h in [h for h in Q if len(h)==n]:
        ell = L[h]
        if n==4:
            V[h] = terminal(ell)
        else:
            cont = continuation_step(ell) + sum(
                (q*V[h+(sym,)] for sym,q,_ in transitions(h)), F(0))
            V[h] = min(terminal(ell),cont)

# At time 3, the final observation contains no information, so LR suffices.
def v3(ell):
    return min(terminal(ell), continuation_step(ell)+terminal(ell))
for h in Q:
    if len(h)==3:
        assert V[h] == v3(L[h])

# Stronger-than-requested compressed class keeps the bit 1[first branch=a]
# all the way until termination, as well as exact LR and time. It still
# cannot distinguish (a,x) and (a,y) at t=2. For other branch classes,
# the bit/LR pair uniquely determines the first symbol.
V2_compressed = {}
V1_compressed = {}
for first in ['a','b','c','d']:
    ell = L[(first,)]
    downstream = F(0)
    for second,q2,_ in transitions((first,)):
        h=(first,second)
        downstream += q2 * sum((q3*v3(L[h+(third,)]) for third,q3,_ in transitions(h)),F(0))
    V2_compressed[first] = min(terminal(ell),continuation_step(ell)+downstream)
    V1_compressed[first] = min(terminal(ell),continuation_step(ell)+V2_compressed[first])
V0_compressed = min(terminal(F(1)),continuation_step(F(1)) + sum(
    (q*V1_compressed[sym] for sym,q,_ in transitions(())),F(0)))

# An explicit unrestricted policy attains the strict lower supporting value.
# Stopping labels: 'P' = decide P; 'Q' = decide Q.
stop_table={
    ('a','y'): ('P',2),
    ('a','x','u'): ('Q',3),
    ('b',): ('P',1),
    ('d',): ('Q',1),
}
for last in ('s','t'):
    stop_table[('a','x','v',last)]=('P',4)
for second,third,fourth in product(('x','y'),('u','v'),('s','t')):
    stop_table[('c',second,third,fourth)]=('P',4)

outcomes=[]
for leaf in [h for h in Q if len(h)==4]:
    selected=next((h for n in range(5) if (h:=leaf[:n]) in stop_table),None)
    assert selected is not None
    decision,tau=stop_table[selected]
    assert tau == len(selected)
    outcomes.append((decision,tau,P[leaf],Q[leaf]))
eP=sum((p for dec,_,p,_ in outcomes if dec=='Q'),F(0))
eQ=sum((q for dec,_,_,q in outcomes if dec=='P'),F(0))
tP=sum((tau*p for _,tau,p,_ in outcomes),F(0))
tQ=sum((tau*q for _,tau,_,q in outcomes),F(0))
J=A*eP+B*eQ+C*tP+D*tQ
assert (eP,eQ,tP,tQ)==(F(17,48),F(11,24),F(37,16),F(43,24))
assert V[('a','x')]==F(-3,32) and V[('a','y')]==1
assert V[('a',)]==F(37,64)
assert V2_compressed['a']==F(33,64)
assert V1_compressed['a']==F(41,64)
assert V[('c',)]==V1_compressed['c']==-11
assert V[('b',)]==V1_compressed['b']==1
assert V[('d',)]==V1_compressed['d']==F(2,3)
assert V[()]==J==F(-427,384)
assert V0_compressed==F(-141,128)
assert V0_compressed-V[()]==F(1,96)

for name, value in [
    ('positive_leaves',sum(len(h)==4 for h in Q)),
    ('P_total',sum((P[h] for h in P if len(h)==4),F(0))),
    ('Q_total',sum((Q[h] for h in Q if len(h)==4),F(0))),
    ('L_t1_a',L[('a',)]),('L_t1_b',L[('b',)]),
    ('L_t2_ax',L[('a','x')]),('L_t2_ay',L[('a','y')]),
    ('L_t3_axu',L[('a','x','u')]),('L_t3_axv',L[('a','x','v')]),
    ('v2_full_ax',V[('a','x')]),('v2_full_ay',V[('a','y')]),
    ('v1_full_a',V[('a',)]),('v1_compressed_a',V1_compressed['a']),
    ('v_root_full',V[()]),('v_root_compressed',V0_compressed),
    ('separation_gap',V0_compressed-V[()]),
    ('O_error_P',eP),('O_error_Q',eQ),('O_E_P_tau',tP),('O_E_Q_tau',tQ),
    ('explicit_witness_J',J),
]:
    print(f'{name}={value}')
print('PASS: 32 strictly positive leaves; exact four-observer witness; strict support separation')
