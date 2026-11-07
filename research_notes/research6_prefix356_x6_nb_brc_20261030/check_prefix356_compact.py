#!/usr/bin/env python3
"""Exact native X6 signed-path positive BRC test; conditional NB rule, not native dynamics."""
from collections import defaultdict
S = [(i, s) for i in range(6) for s in (1,-1)]
O = (0,)*6

def step(z, d):
    r = list(z)
    r[d[0]] += d[1]
    return tuple(r)

def shift(p):
    q = defaultdict(int)
    for z, k in p.items():
        for d in S:
            q[step(z,d)] += k
    return dict(q)

def sub(p, q, c):
    r = dict(p)
    for z,k in q.items():
        r[z] = r.get(z,0)-c*k
        if r[z] == 0:
            del r[z]
    assert all(k>=0 for k in r.values())
    return r

U = [{O:1}]
for n in range(8):
    U.append(shift(U[-1]))
F = [U[0],U[1],sub(U[2],U[0],12)]
for n in range(3,9):
    F.append(sub(shift(F[-1]),F[-2],11))
expected = [1,0,0,0,120,0,5400,0,315720]
for n in range(9):
    assert F[n].get(O,0)==expected[n]
    assert sum(F[n].values())==(1 if n==0 else 12*11**(n-1))
    assert all(v<=U[n].get(z,0) for z,v in F[n].items())

# Independent labeled-branch BRC transition, exact every endpoint through n=6.
H={(O,None):1}
for n in range(7):
    P=defaultdict(int)
    for (z,last),k in H.items():
        P[z]+=k
    assert dict(P)==F[n],n

    if n in (4,6):
        closed=[H.get((O,d),0) for d in S]
        assert closed==([10]*12 if n==4 else [450]*12)
    J=defaultdict(int)
    for (z,last),k in H.items():
        for d in S:
            if last is not None and d==(last[0],-last[1]):
                continue
            J[(step(z,d),d)]+=k
    H=dict(J)

# Fixed-Cell next-step histogram reconstructs all twelve last-leg counts.
for h in ([1]*12,[2]*12,list(range(12)),[10 if j%3==0 else 0 for j in range(12)]):
    total=sum(h)
    y=[total-h[S.index((d[0],-d[1]))] for d in S]
    assert sum(y)==11*total
    back=[sum(y)//11-y[S.index((d[0],-d[1]))] for d in S]
    assert back==h
assert U[2][O]==12 and U[4][O]==396
print('PASS_PREFIX356_EXACT_X6_NONBACKTRACKING_BRC_N8_AND_FIBRE_INVERSION')
print('returns_nb_n0_n8=',expected)
print('returns_unrestricted_n2_n4_n6_n8=',[U[n].get(O,0) for n in (2,4,6,8)])
