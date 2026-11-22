#!/usr/bin/env python3
"""T6 maximal-p13 v13=1 positive vertical order2, both splits.
Exact arithmetic, published q1/q0 lattice reused; author finite evidence only.
"""
import importlib.util
import math
from pathlib import Path
from fractions import Fraction
from itertools import combinations, combinations_with_replacement
from sympy import Matrix

src=Path(__file__).with_name("T6_P13_Q1_SPLIT0_1_GLOBAL_AFFINE_CHECK_20261123.py")
spec=importlib.util.spec_from_file_location("t6_p13_q1",src)
prior=importlib.util.module_from_spec(spec)
spec.loader.exec_module(prior)
P,CAP,N,W,U,UI=prior.P,prior.CAP,prior.N,prior.W,prior.U,prior.UI
mu,D,dmin=prior.mu,prior.D,prior.dmin
atom={(q,r):Matrix(1,N,prior.particular(q,r))
      for q in (1,2) for r in range(1,P)}

def search(plus,minus):
    cp=sum(P*(P*q+r)-1 for q,r in plus)
    cn=sum(P*(P*q+r)-1 for q,r in minus)
    rad=(CAP-cp)**2+(CAP-cn)**2
    assert rad<dmin
    v=Matrix(1,N,[0]*N)
    for a in plus:v+=atom[a]
    for a in minus:v-=atom[a]
    c=[Fraction(x) for x in v*UI]
    z=c[:];n=[0]*N
    nodes=0;leaves=0;valid=0
    def rec(i,spent):
        nonlocal nodes,leaves,valid
        if i<0:
            leaves+=1
            u=[sum((c[j]+n[j])*Fraction(int(U[j,t])) for j in range(N))
               for t in range(N)]
            assert all(x.denominator==1 for x in u)
            pp=cp+sum(w*max(0,int(x)) for w,x in zip(W,u))
            nn=cn+sum(w*max(0,-int(x)) for w,x in zip(W,u))
            valid+=int(pp<=CAP and nn<=CAP)
            return
        nodes+=1
        center=c[i]+sum(z[j]*mu[j][i] for j in range(i+1,N))
        lo=math.floor(-center)
        for ni in (lo,lo+1):
            nxt=spent+D[i]*(center+ni)**2
            if nxt<=rad:
                z[i]=c[i]+ni;n[i]=ni;rec(i-1,nxt)
        z[i]=c[i]
    rec(N-1,Fraction(0))
    return (nodes,leaves,valid)

s02=[search([(2,r)],[]) for r in range(1,P)]
s02 += [search([(1,r),(1,s)],[]) for r,s in
        combinations_with_replacement(range(1,P),2)]
s11=[search([(1,r)],[(1,s)]) for r,s in combinations(range(1,P),2)]
summary={
 '(0,2)':{'raw':len(s02),'GS_nodes':sum(t[0] for t in s02),
          'sphere_leaves':sum(t[1] for t in s02),'budget_valid':sum(t[2] for t in s02)},
 '(1,1)':{'raw':len(s11),'GS_nodes':sum(t[0] for t in s11),
          'sphere_leaves':sum(t[1] for t in s11),'budget_valid':sum(t[2] for t in s11)}}
assert summary=={
 '(0,2)':{'raw':90,'GS_nodes':357,'sphere_leaves':0,'budget_valid':0},
 '(1,1)':{'raw':66,'GS_nodes':268,'sphere_leaves':0,'budget_valid':0}}
print('AUTHOR_EXACT_P13_ORDER2_EMPTY',summary)
print('T6 remains OPEN; other p13 vertical orders remain')
