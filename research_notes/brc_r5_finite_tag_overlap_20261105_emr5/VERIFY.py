#!/usr/bin/env python3
"""R5 exact finite-tag support loss and overlap certificate (stdlib Fraction)."""
from fractions import Fraction as F
from itertools import product

def plus(x):
    return max(F(0), x)

def certificate(w, A, u, T):
    m, q = len(w), len(T[0])
    assert len(A)==len(u)==len(T)==m
    assert all(x>0 for x in w)
    assert all(len(row)==q and all(x>=0 for x in row) and sum(row)==1 for row in T)
    M = [max(F(0), A[i], A[i]+u[i]) for i in range(m)]
    full = sum(w[i]*M[i] for i in range(m))
    Sminus = [i for i in range(m) if A[i]>0 and u[i]<0]
    Splus = [i for i in range(m) if A[i]+u[i]>0 and u[i]>0]
    bminus = [sum((w[i]*min(A[i],-u[i])*T[i][y] for i in Sminus),F(0)) for y in range(q)]
    bplus  = [sum((w[i]*min(A[i]+u[i],u[i])*T[i][y] for i in Splus),F(0)) for y in range(q)]
    overlap = sum((min(bminus[y],bplus[y]) for y in range(q)),F(0))
    selectors = list(product((0,1),repeat=q))
    values = []
    for z in selectors:
        t = [sum((T[i][y]*z[y] for y in range(q)),F(0)) for i in range(m)]
        value=sum((w[i]*plus(A[i]+u[i]*t[i]) for i in range(m)),F(0))
        values.append((value,z))
    tag = max(x[0] for x in values)
    loss = full-tag
    # Perfect recovery iff the output supports of stop/continue classes do not overlap.
    overlap_support = any(bminus[y]>0 and bplus[y]>0 for y in range(q))
    assert loss >= overlap >= 0
    assert (loss==0)==(not overlap_support)
    return dict(full=full,tag=tag,loss=loss,overlap_lower_bound=overlap,perfect=(loss==0),witness=[z for v,z in values if v==tag])

# Predecessor model S at the fixed exposed direction, with binary symmetric tag.
w = [F(1,2),F(1,2)]
A = [F(1,200),-F(47,400)]
u = [-F(9,500),F(49,400)]
C = -F(43,40)
for eta in [F(0),F(1,1000),F(1,50),F(10,281),F(1,20),F(1,4),F(1,2)]:
    T = [[1-eta,eta],[eta,1-eta]]
    r=certificate(w,A,u,T)
    h_tag=C+r['tag']
    expected=-F(43,40)+F(1,400)+plus(F(1,400)-F(281,4000)*eta)
    assert h_tag == expected
    assert r['full']-r['tag']==min(F(281,4000)*eta,F(1,400))
    assert r['overlap_lower_bound']==eta/F(200)
    print(f'MODEL_S eta={eta} h_tag={h_tag} exact_gap={r["loss"]} overlap_lower={r["overlap_lower_bound"]}')

# Three histories with nonidentical strictly positive ternary channel rows.
w3 = [F(1,3),F(1,2),F(1,6)]
A3 = [F(1,7),-F(1,5),F(1,9)]
u3 = [-F(1,3),F(3,10),F(0)]
T3 = [[F(1,2),F(1,3),F(1,6)],
      [F(1,6),F(1,2),F(1,3)],
      [F(1,4),F(1,4),F(1,2)]]
r3 = certificate(w3,A3,u3,T3)
assert r3['loss']>0 and r3['overlap_lower_bound']>0
print('THREE_HISTORY positive_ternary',r3)

Tclean=[[F(1),F(0),F(0)], [F(0),F(1),F(0)], [F(0),F(0),F(1)]]
rc=certificate(w3,A3,u3,Tclean)
assert rc['loss']==0 and rc['overlap_lower_bound']==0
print('THREE_HISTORY disjoint_support',rc)

# Several fixed exact channels, four histories, including an idle/nonconstraining row.
w4=[F(1,5), F(1,5), F(2,5), F(1,5)]
A4=[F(1,8), -F(1,9), -F(3,10), F(0)]
u4=[-F(1,4), F(1,2), F(1,10), F(0)]
for delta in (F(0), F(1,100),F(1,4)):
    T4=[[1-delta,delta,0],[delta,1-delta,0],
        [F(1,3),F(1,3),F(1,3)],
        [F(1,3),F(1,3),F(1,3)]]
    r4=certificate(w4,A4,u4,T4)
    print(f'FOUR_HISTORY delta={delta}',r4)
print('PASS_EXACT_R5_FINITE_TAG_OVERLAP_DEFECT_CERTIFICATE')
