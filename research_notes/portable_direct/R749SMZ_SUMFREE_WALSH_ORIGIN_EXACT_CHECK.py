#!/usr/bin/env python3
"""R749SMZ: rational, standard-library verification; general theorem is analytic."""
from fractions import Fraction as F
from itertools import combinations
import json

def chi(a,x):
    return -1 if ((a & x).bit_count() % 2) else 1

def moments(p,d):
    return [sum(p[x]*chi(k,x) for x in range(1<<d)) for k in range(1<<d)]

def solve(A,b):
    n=len(b); t=[[F(z) for z in A[i]]+[F(b[i])] for i in range(n)]
    for j in range(n):
        pivot=next((i for i in range(j,n) if t[i][j]),None)
        if pivot is None: return None
        t[j],t[pivot]=t[pivot],t[j]
        v=t[j][j]; t[j]=[z/v for z in t[j]]
        for i in range(n):
            if i!=j and t[i][j]:
                z=t[i][j]; t[i]=[a-z*b for a,b in zip(t[i],t[j])]
    return tuple(t[i][-1] for i in range(n))

def origin(d,C):
    N=1<<d; H=[[chi(c,x) for c in C] for x in range(N)]
    nonsing=feasible=0; vs=set()
    for idx in combinations(range(N),len(C)):
        m=solve([H[x] for x in idx],[-1]*len(C))
        if m is None: continue
        nonsing+=1
        p=[(1+sum(m[j]*H[x][j] for j in range(len(C))))/N for x in range(N)]
        if min(p)<0: continue
        feasible+=1; assert sum(p)==1
        mo=moments(p,d)
        assert all(mo[b]==0 for b in range(1,N) if b not in C)
        assert all(mo[c]==m[j] for j,c in enumerate(C))
        vs.add(m)
    risks=[]
    for m in vs:
        p=[(1+sum(m[j]*H[x][j] for j in range(len(C))))/N for x in range(N)]
        assert sum(x*x for x in m)<=1
        tv=sum(abs(z-F(1,N)) for z in p)/2
        assert tv<=F(1,2); risks.append(tv)
    assert max(risks)==F(1,2)
    return dict(active_subsets=4368,nonsingular=nonsing,feasible_active=feasible,
                vertices=len(vs),maximum_tv=str(max(risks)),
                vertices_attaining_half=sum(r==F(1,2) for r in risks))

def examples():
    ans=[]
    for d,C in [(2,(1,2)),(3,(1,2,4,7)),(4,(1,2,4,8,15))]:
        N=1<<d; B=[b for b in range(1,N) if b not in C]
        assert all((a^b) not in C for a,b in combinations(C,2))
        u=[F(1,N)]*N
        for m in [tuple(F(0) for _ in C),tuple(F((-1)**j,3*len(C)) for j in range(len(C)))]:
            p=[(1+sum(m[j]*chi(c,x) for j,c in enumerate(C)))/N for x in range(N)]
            assert min(p)>=0
            assert all(moments(p,d)[b]==0 for b in B)
            assert sum(abs(p[x]-u[x]) for x in range(N))/2<=F(1,2)
        c=C[0]
        plus=[F(1+chi(c,x),N) for x in range(N)]
        minus=[F(1-chi(c,x),N) for x in range(N)]
        assert sum(plus)==sum(minus)==1
        assert sum(abs(a-b) for a,b in zip(plus,minus))/2==1
        assert all(moments(plus,d)[b]==moments(minus,d)[b]==0 for b in B)
        for lam in (F(0),F(1,3),F(-2,3),F(1)):
            def observe(p):
                return [sum(p[x]*(1+y*lam*chi(c,x))/2 for x in range(N)) for y in (-1,1)]
            assert sum(abs(a-b) for a,b in zip(observe(plus),observe(u)))/2==abs(lam)/2
        ans.append(dict(d=d,omitted=list(C),retained_zero_count=len(B),extremal_pair_tv="1",
                        noisy_binary_exact_radius="|lambda|/2"))
    return ans

if __name__=="__main__":
    C=(1,2,4,8,15)
    assert sorted({a^b for a,b in combinations(C,2)})==[3,5,6,7,9,10,11,12,13,14]
    result=dict(status="PASS",theorem="sum-free C, all retained nonzero moments zero => unrestricted full-state minimax TV radius 1/2",
                proof="E[XX^T]=I; Cov=I-mmT PSD; orthogonality and Cauchy-Schwarz; disjoint extremal pair",
                five_circuit_origin=origin(4,C),exact_examples=examples(),
                non_sumfree_counterexample=dict(d=2,C=[1,2,3],exact_radius="3/4"))
    print(json.dumps(result,indent=2))
