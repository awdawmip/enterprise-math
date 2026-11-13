#!/usr/bin/env python3
"""R748 signed-Port BRC graph spectrum and exact walk checker; stdlib only."""
from itertools import combinations
from collections import Counter
from fractions import Fraction
import json

AXES=range(6)
PORTS=[(i,s) for i in AXES for s in (-1,1)]
V=[tuple(sorted((a,b))) for a,b in combinations(PORTS,2) if a[0]!=b[0]]
assert len(V)==60

def adjacent(v,w):
    return len(set(v)&set(w))==1 and len({p[0] for p in set(v)|set(w)})==3

A=[[int(adjacent(v,w)) for w in V] for v in V]
assert A==[list(row) for row in zip(*A)]
assert all(sum(row)==16 for row in A)

def mv(v): return [sum(a*b for a,b in zip(row,v)) for row in A]
def check_eigen(v,lam):
    assert any(v) and mv(v)==[lam*x for x in v]

PAIRS=list(combinations(AXES,2))
def alpha(x): return [x[(a[0],b[0])] for a,b in V]
def beta(i,coeff):
    return [((a[1] if a[0]==i else b[1])*coeff.get(b[0] if a[0]==i else a[0],0))
            if (a[0]==i or b[0]==i) else 0 for a,b in V]
def gamma(i,j):
    return [a[1]*b[1] if (a[0],b[0])==(i,j) else 0 for a,b in V]

def nullspace(mat):
    m=[[Fraction(x) for x in row] for row in mat]
    n=len(m[0]); pivots=[]; r=0
    for c in range(n):
        k=next((k for k in range(r,len(m)) if m[k][c]),None)
        if k is None: continue
        m[r],m[k]=m[k],m[r]; d=m[r][c]
        m[r]=[v/d for v in m[r]]
        for i in range(len(m)):
            if i!=r and m[i][c]:
                t=m[i][c];m[i]=[x-t*y for x,y in zip(m[i],m[r])]
        pivots.append(c);r+=1
        if r==len(m): break
    out=[]
    for j in range(n):
        if j in pivots: continue
        v=[Fraction(0)]*n;v[j]=1
        for i,p in enumerate(pivots):v[p]=-m[i][j]
        out.append(v)
    return out

vecs=[];counts=Counter()
def add(v,lam):
    check_eigen(v,lam);vecs.append(v);counts[lam]+=1

add(alpha({p:1 for p in PAIRS}),16)
for i in range(5):
    u=[0]*6;u[i]=1;u[5]=-1
    add(alpha({(a,b):u[a]+u[b] for a,b in PAIRS}),4)
kernel=nullspace([[int(i in p) for p in PAIRS] for i in AXES])
assert len(kernel)==9
for x in kernel:add(alpha(dict(zip(PAIRS,x))),-4)
for i in AXES:
    other=[j for j in AXES if j!=i]
    add(beta(i,{j:1 for j in other}),8)
    for j in other[:-1]:add(beta(i,{j:1,other[-1]:-1}),-2)
for i,j in PAIRS:add(gamma(i,j),0)
assert counts=={16:1,8:6,4:5,0:15,-2:24,-4:9}
assert len(vecs)==60
assert len(nullspace([[v[k] for v in vecs] for k in range(60)]))==0

B=[[int(i==j) for j in range(60)] for i in range(60)]
checks={}
for n in range(1,7):
    B=[[sum(B[i][k]*A[k][j] for k in range(60)) for j in range(60)] for i in range(60)]
    tr=sum(B[i][i] for i in range(60))
    assert tr==sum(lam**n*m for lam,m in counts.items())
    assert len({B[i][i] for i in range(60)})==1
    checks[n]={"trace":tr,"return_walks_per_vertex":B[0][0],
               "resampled_return":f"{B[0][0]}/{16**n}",
               "retained_return":int(n%3==0)}
assert checks[3]["return_walks_per_vertex"]==112
result={"schema":"EM_R748_C1_SIGNED_PAIR_BRC_SPECTRUM_EXACT_V1",
"status":"PASS","vertices":60,"signed_ports":12,"edges":sum(map(sum,A)),
"degree":16,"spectrum":{str(l):m for l,m in sorted(counts.items())},
"verified_independent_eigenvectors":60,"integer_walk_checks":checks,
"second_eigen_absolute_P":"1/2","observer_limit_return":"1/60",
"retained_source_period":3,"3k_gap_limit":"59/60",
"frozen_scientific_pin":"a72226e2430ffa4786321ac86e7f0c599d5f0389",
"scope":"exact finite proposed C1 Port model; no native V29/V39 execution"}
print(json.dumps(result,indent=2,ensure_ascii=False))
