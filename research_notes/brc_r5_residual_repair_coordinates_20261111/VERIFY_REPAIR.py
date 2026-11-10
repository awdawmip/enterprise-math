#!/usr/bin/env python3
"""Exact 15-coordinate R5 residual reconstruction and one rational 14-arc vertex.
Requires the copied immutable predecessor witness WITNESS.txt in this same directory.
"""
from fractions import Fraction as Q
from itertools import combinations
from pathlib import Path
from sympy import Matrix, Rational

r=tuple(map(Q,('1/10','1/2','3/4','1','5/4','3/2','19/10')))
D=tuple((i,j) for j in (0,1,2,3,5,6) for i in range(7) if j not in (0,6) or i==j)
data=dict(line.split('=',1) for line in Path(__file__).with_name('WITNESS.txt').read_text().splitlines())
E0=tuple(map(Q,data['ARCS'].split(',')))
assert len(D)==len(E0)==30 and min(E0)==Q(data['MARGIN'])>0

def obs(x):
    return (tuple(sum((x[D.index((i,j))] for j in (0,1,2,3,5,6) if (i,j) in D),Q()) for i in range(7))
          +tuple(sum((x[D.index((i,j))] for i in range(7) if (i,j) in D),Q()) for j in range(7))
          +tuple(sum(((r[i]-r[j])*x[D.index((i,j))] for i in range(7) if (i,j) in D),Q()) for j in range(7)))

def circuit(j,k):
    # j in {2,3,5}; k in {1,...,5}. All six nonzero arcs lie in K_{2,3}.
    d={(k,j):Q(1),(0,j):(r[k]-r[6])/(r[6]-r[0]),
       (6,j):(r[0]-r[k])/(r[6]-r[0])}
    for i in (0,k,6): d[i,1]=-d[i,j]
    return tuple(d.get(a,Q()) for a in D)

B=[circuit(j,k) for j in (2,3,5) for k in range(1,6)]
C=Matrix.hstack(*(Matrix([Rational(t.numerator,t.denominator)
    for t in obs(tuple(Q(m==n) for m in range(30)))]) for n in range(30)))
Bm=Matrix.hstack(*(Matrix([Rational(t.numerator,t.denominator) for t in b]) for b in B))
assert C.shape==(21,30) and C.rank()==15 and Bm.rank()==15 and C*Bm==Matrix.zeros(21,15)
assert all(sum(v!=0 for v in b)==6 for b in B)

def rebuild(a):
    assert len(a)==15
    return tuple(sum((a[t]*B[t][i] for t in range(15)),Q()) for i in range(30))

# All 210 independently enumerated K2,3 circuits reconstruct from the chosen 15 mass coordinates.
count=0
for ja,jb in combinations((1,2,3,5),2):
    for tri in combinations(range(7),3):
        u,v,w=tri
        d={(u,ja):r[v]-r[w],(v,ja):r[w]-r[u],(w,ja):r[u]-r[v]}
        for i in tri: d[i,jb]=-d[i,ja]
        h=tuple(d.get(arc,Q()) for arc in D)
        a=tuple(h[D.index((k,j))] for j in (2,3,5) for k in range(1,6))
        assert rebuild(a)==h
        count+=1
assert count==210
# A nonzero 15-coordinate physical-fiber test, reusing the exact published positive witness.
a=tuple(Q(n-7,50000) for n in range(15))
h=rebuild(a)
assert obs(h)==(Q(),)*21
assert all(E0[i]+h[i]>0 for i in range(30))
# Every nonnegative coupling in this fixed fiber is E0+rebuild(a) >= 0.
assert all(B[t][D.index((0,0))]==B[t][D.index((6,6))]==0 for t in range(15))
# Rational kernel pivots until the positive columns are linearly independent.
x=list(E0)
for _ in range(30):
    S=[i for i,z in enumerate(x) if z>0]
    null=C[:,S].nullspace()
    if not null: break
    d=[Q() for i in range(30)]
    for i,coef in zip(S,null[0]): d[i]=Q(int(coef.p),int(coef.q))
    if not any(z<0 for z in d): d=[-z for z in d]
    step=min(x[i]/(-d[i]) for i in S if d[i]<0)
    x=[x[i]+step*d[i] for i in range(30)]
    assert min(x)>=0 and obs(x)==obs(E0)
else: raise AssertionError('pivot iteration failed')
S=[i for i,z in enumerate(x) if z>0]
assert len(S)==14 and C[:,S].rank()==len(S)
print('C_RANK',C.rank(),'KERNEL_DIMENSION',30-C.rank())
print('CANONICAL_REPAIR_COORDINATES',len(B),'SPARSE_K23_BASIS_OK')
print('ALL_K23_SIX_ARC_CIRCUITS',count,'EXACT_RECONSTRUCTION_OK')
print('FIXED_BASE_ARCS',E0[D.index((0,0))],E0[D.index((6,6))])
print('POSITIVE_15_COORDINATE_EXAMPLE_MIN',min(E0[i]+h[i] for i in range(30)))
print('EXPLICIT_VERTEX_SUPPORT',len(S),'INDEPENDENT_COLUMNS_OK')
for i in S: print('VERTEX_ARC',D[i],x[i])
print('PASS_EXACT_REPAIR_AND_VERTEX')
