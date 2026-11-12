#!/usr/bin/env python3
"""R749S: exact spectral + source-defect closed-walk certificates (stdlib)."""
from itertools import combinations
from collections import defaultdict, Counter
import json
from fractions import Fraction

ports = tuple(range(12))  # axis = p//2, sign = (-1)**(p%2)
verts = tuple((a,b) for a,b in combinations(ports,2) if a//2 != b//2)
assert len(verts) == 60
vid = {v:i for i,v in enumerate(verts)}
sets = [frozenset(v) for v in verts]
neighbor = []
for i,v in enumerate(sets):
    neighbor.append(tuple(j for j,w in enumerate(sets)
        if len(v&w)==1 and len({x//2 for x in v|w})==3))
assert all(len(row)==16 for row in neighbor)
D = tuple((i,j) for i in range(60) for j in neighbor[i])
did = {e:k for k,e in enumerate(D)}
assert len(D)==960
F=[]; B=[]
for i,j in D:
    w = vid[tuple(sorted(sets[i] ^ sets[j]))]
    assert w in neighbor[j]
    F.append(did[(j,w)])
    B.append(tuple(did[(j,x)] for x in neighbor[j] if x!=w))
assert all(len(row)==15 for row in B)
assert all(F[F[F[e]]]==e for e in range(960))

def fpower(e,n):
    for _ in range(n%3): e=F[e]
    return e

# Canonical local two-defect table, evaluated against every directed source.
table_expected = ((1,0,0),(0,1,0),(0,0,15))
for e in range(960):
    for a in range(3):
        for b in range(3):
            n = sum(fpower(z,b)==e for x in B[e] for z in B[fpower(x,a)])
            assert n == table_expected[a][b], (e,a,b,n)

# Histogram of closed n-step source paths by forced step count.
first=did[D[0]]
state = {first:[1]}
closed={}
for n in range(1,13):
    new=defaultdict(lambda: [0]*(n+1))
    for e, cs in state.items():
        for j in (F[e],):
            for k,c in enumerate(cs): new[j][k+1]+=c
        for j in B[e]:
            for k,c in enumerate(cs): new[j][k]+=c
    state=new
    coeffs=state.get(first,[0]*(n+1))
    closed[n]=coeffs
    assert coeffs[n-1]==0
    assert coeffs[n]==(1 if n%3==0 else 0)
    if n>=2:
        formula= ((5*n*(n-3))//2 if n%3==0 else
                  (n*(n-1))//6 if n%3==1 else (n*(n+1))//6)
        assert coeffs[n-2]==formula,(n,coeffs[n-2],formula)
assert closed[2]==[1,0,0]
assert closed[3]==[6,0,0,1]
assert closed[4]==[72,24,2,0,0]

# Exact spectrum analytically determined by signed-axis Fourier blocks:
# empty character -> 2*Johnson(6,2), 1-axis -> 2*(J5-I5),
# 2-axis -> zero; see companion full proof.
spec={16:1,8:6,4:5,-2:24,-4:9,0:15}
assert sum(spec.values())==60

# Check graph trace(A^n) from EVERY starting vertex for n=1..10.
traces={}
for start in range(60):
    x={start:1}
    for n in range(1,11):
        nxt=defaultdict(int)
        for v,c in x.items():
            for w in neighbor[v]:nxt[w]+=c
        x=nxt
        traces[n]=traces.get(n,0)+x.get(start,0)
for n,v in traces.items():
    assert v==sum(m*(lam**n) for lam,m in spec.items()),(n,v)
    assert v==960*sum(closed[n]) if n<=10 else True

def return_probability(n,p):
    q=(1+15*p)/16
    r=(1-p)/16
    return sum(Fraction(c)*q**k*r**(n-k) for k,c in enumerate(closed[n]))
for n in range(1,11):
    assert return_probability(n,Fraction(0)) == Fraction(traces[n],960*16**n)
    assert return_probability(n,Fraction(1)) == int(n%3==0)

out={
 "schema":"EM_R749S_EXACT_SPECTRAL_BRC_LOOPS_V1",
 "status":"PASS",
 "vertex_count":60,"vertex_degree":16,"directed_edge_count":960,
 "vertex_adjacency_eigenvalues_multiplicity": {str(v):m for v,m in sorted(spec.items())},
 "two_defect_local_table_rows_a_columns_b":[list(row) for row in table_expected],
 "local_table_checked_directed_sources":960,
 "closed_loop_weight_polynomials_by_length_n_k_coefficients":{str(n):coeffs for n,coeffs in closed.items()},
 "spectral_trace_verified_lengths":list(traces),
 "exact_return_p0_n2":str(return_probability(2,Fraction(0))),
 "exact_return_p0_n3":str(return_probability(3,Fraction(0))),
 "exact_return_p0_n4":str(return_probability(4,Fraction(0))),
 "exact_return_phalf_n4":str(return_probability(4,Fraction(1,2))),
 "native_event_permission":False,
 "claim_or_independent_acceptance":False,
}
print(json.dumps(out,sort_keys=True,ensure_ascii=False,indent=2))
