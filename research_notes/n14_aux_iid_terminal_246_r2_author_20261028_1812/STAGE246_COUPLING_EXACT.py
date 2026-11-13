#!/usr/bin/env python3
"""Exact Stage246 full-history witness checker for external ternary IID (N=14).

Independent of the Stage245 Bellman convex-polytope enumerator. Uses positive
rational branch masses and explicit ordered path enumeration (no count merging).
It verifies one particular time-balanced rule, not global optimality; the
universal global lower bound is proved analytically by maximal coupling.
"""
from fractions import Fraction as Q
from collections import defaultdict

P = tuple(map(lambda x: Q(x,24), (3,1,20)))
R = tuple(map(lambda x: Q(x,24), (2,2,20)))
q = Q(6) - Q(6,5)**9 # Pr(try sample 9 | eight third symbols)
assert 0 <= q <= 1
N=14
leaves=[]

def visit(history, mp, mq):
    n=len(history)
    if n==8:
        leaves.append((history,"Q", mp*(1-q), mq*(1-q)))
        mp,mq=mp*q,mq*q
    if n==9:
        leaves.append((history,"Q",mp,mq))
        return
    assert n<9 and n<N
    for symbol in range(3):
        hp=mp*P[symbol]
        hq=mq*R[symbol]
        h=history+(symbol,)
        if symbol==2:
            visit(h,hp,hq)
        else:
            leaves.append((h,"P" if symbol==0 else "Q",hp,hq))

visit((),Q(1),Q(1))
assert sum(wp for _,_,wp,wq in leaves)==1
assert sum(wq for _,_,wp,wq in leaves)==1
errors_P=sum(wp for h,decision,wp,wq in leaves if decision=='Q')
errors_Q=sum(wq for h,decision,wp,wq in leaves if decision=='P')
time_P=sum(len(h)*wp for h,decision,wp,wq in leaves)
time_Q=sum(len(h)*wq for h,decision,wp,wq in leaves)
signal_P=sum(wp for h,decision,wp,wq in leaves if h and h[-1]!=2)
signal_Q=sum(wq for h,decision,wp,wq in leaves if h and h[-1]!=2)
assert (signal_P,signal_Q)==(Q(4,5),Q(4,5))
assert (errors_P,errors_Q,time_P,time_Q)==(Q(2,5),Q(2,5),Q(24,5),Q(24,5))
assert q==Q(1641054,1953125)
# Coupled one-step branch masses, retaining matched/mismatch provenance.
coupling={(0,0):Q(2,24), (1,1):Q(1,24), (2,2):Q(20,24), (0,1):Q(1,24)}
assert sum(coupling.values())==1
assert tuple(sum(w for (i,j),w in coupling.items() if i==a) for a in range(3)) == P
assert tuple(sum(w for (i,j),w in coupling.items() if j==b) for b in range(3)) == R
assert sum(w for (i,j),w in coupling.items() if i!=j)==Q(1,24)
for a in (Q(2,5),Q(41,100),Q(9,20),Q(1,2)):
    weight=Q(5)-10*a
    assert 0<=weight<=1
    e=weight*errors_P+(1-weight)*Q(1,2)
    t=weight*time_P
    assert e==a and t==Q(24)-48*a
# This algebra is valid for every real a in [2/5,1/2]: weights are affine.
print('STAGE246_COUPLING_AUTHOR_EXACT_PASS')
print('q', q, 'leaves',len(leaves),'signal',signal_P)
print('witness ep eq tP tQ',errors_P,errors_Q,time_P,time_Q)
print('coupling TV',Q(1,24),'tested rational alphas: 2/5,41/100,9/20,1/2')
print('theorem for ALL real alpha in [2/5,1/2]: V14(alpha)=24-48*alpha')
print('for alpha>=1/2: V14(alpha)=0')
