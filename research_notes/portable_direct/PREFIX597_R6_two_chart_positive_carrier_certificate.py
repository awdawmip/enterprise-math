#!/usr/bin/env python3
"""PREFIX-597-R6 exact abstract circuit/positive-carrier certificate.

Independent standard-library algebraic checks; does not execute the original
native BRC kernel. Native four-port input is previously checked in PREFIX-595.
"""
from fractions import Fraction as Q
from itertools import product
import json

A, B, C, D = 0, 1, 2, 3
N=34
c=[0]*N
for i,v in ((A,1),(B,1),(C,-1),(D,-1)):
    c[i]=v

def normalize(p):
    assert len(p)==N and all(x>=0 for x in p)
    t=min(p[A],p[B])
    q=[p[i]-t*c[i] for i in range(N)]
    assert min(q)>=0 and (q[A]==0 or q[B]==0) and sum(p)==sum(q)
    return q

def circuit_shift(p,t):
    return [p[i]+t*c[i] for i in range(N)]

def rank(rows):
    piv={}
    for row in rows:
        v=[Q(z) for z in row]
        for i,b in sorted(piv.items()):
            if v[i]:
                t=v[i];v=[x-t*y for x,y in zip(v,b)]
        j=next((i for i,x in enumerate(v) if x),None)
        if j is not None:
            t=v[j];piv[j]=[x/t for x in v]
    return len(piv)

# Universal coordinate model imposed by a unique 4-point affine circuit.
V=[[Q(0)]*32 for _ in range(N)]
V[C][0]=1;V[D][1]=1;V[B][0]=1;V[B][1]=1
for k in range(30):
    V[k+4][k+2]=1
U=[[Q(1)]+v for v in V]
assert rank(U)==33
assert all(sum(c[i]*U[i][j] for i in range(N))==0 for j in range(33))
assert rank([U[i] for i in range(N) if i != A])==33
assert rank([U[i] for i in range(N) if i != B])==33
assert rank([U[i] for i in range(N) if i not in (A,B)])==32

probes=[]
for xs in product(range(3),repeat=4):
    p=[Q(0)]*N
    for k,x in enumerate(xs):p[k]=Q(x,12)
    p[4]=Q(1,3)
    probes.append(p)
for i in range(N):
    p=[Q(0)]*N;p[i]=Q(1);probes.append(p)
for p in probes:
    q=normalize(p)
    assert normalize(q)==q
    assert all(sum(p[i]*U[i][j] for i in range(N)) ==
               sum(q[i]*U[i][j] for i in range(N)) for j in range(33))
    left=-min(p[A],p[B]);right=min(p[C],p[D])
    for t in (left,right,(left+right)/2):
        z=circuit_shift(p,t)
        assert min(z)>=0 and normalize(z)==q
        assert all(sum(z[i]*U[i][j] for i in range(N)) ==
                   sum(q[i]*U[i][j] for i in range(N)) for j in range(33))

# Synthetic *non-BRC* emitted-symbol substochastic transfer family,
# testing the universal algebraic implication from c*K[r,rho]=0.
K=[]
for sym in range(2):
    M=[[Q(0)]*N for _ in range(N)]
    rows={A:(4,5),B:(6,7),C:(4,6),D:(5,7)}
    for i in range(N):
        if i in rows:
            for j in rows[i]:M[i][j]+=Q(1,4)
        else:M[i][i]+=Q(1,2)
    K.append(M)
    assert all(sum(c[i]*M[i][j] for i in range(N))==0 for j in range(N))
for p in probes:
    q=normalize(p)
    for M in K:
        x=[sum(p[i]*M[i][j] for i in range(N)) for j in range(N)]
        y=[sum(q[i]*M[i][j] for i in range(N)) for j in range(N)]
        assert x==y and normalize(x)==normalize(y)

result=dict(status="ALL_ABSTRACT_CHECKS_PASS",
    scientific_pin="f42f2906d77f24085c123f3ccfe9667d41caa96d",
    native_premise="PREFIX-595 full-seven-reward next-original-port four-port identity",
    full_behavior_polytope_vertices=34, affine_dimension=32,
    linear_rank_including_constant=33, affine_circuit=[1,1,-1,-1],
    parallelogram_pyramid_apices=30, predicted_facets=34,
    positive_charts=2, chart_vertices=33,
    checked_rational_mixtures=len(probes), synthetic_emissions=len(K),
    original_native_brc_kernel_executed=False)
print("ALL_ABSTRACT_CHECKS_PASS")
print(json.dumps(result,indent=2))
