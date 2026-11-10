#!/usr/bin/env python3
"""R5: exact four-dimensional 12-vertex Blackwell transport face at z_c.
This uses the verified 4,845-support and 1,140-support predecessor program.
"""
from pathlib import Path
import runpy
import sympy as S
from itertools import combinations

root=Path(__file__).resolve().parent.parent
prev=root/'brc_r5_first_contact_sheet_20261110_t1235'/'VERIFY_SHEET.py'
b=runpy.run_path(str(prev))
C,D,FSET,OTHER,q0,positive=(b[k] for k in ('C','D','FSET','OTHER','q0','positive'))
assert len(D)==30 and len(FSET)==10 and len(OTHER)==20
assert len(positive)==12 and len(b['matching'])==28
G1=((2,1),(3,1),(4,1))
G2=((3,2),(4,2))
G3=((0,3),(2,3))
SHARED=((1,5),)
U_ARCS=FSET+SHARED+G1+G2+G3
assert len(U_ARCS)==18 and len(set(U_ARCS))==18
U=C[:,[D.index(e) for e in U_ARCS]]
assert U.rank()==14 and U.row_join(q0).rank()==14

points=[]
witnessed=[]
for comb in positive:
    arcs=FSET+tuple(OTHER[i] for i in comb)
    active=set(arcs)
    assert SHARED[0] in active
    assert all(len(active.intersection(group))==1 for group in (G1,G2,G3))
    M=C[:,[D.index(e) for e in arcs]]
    assert M.rank()==14
    sol,_=M.gauss_jordan_solve(q0)
    assert all(v>0 for v in sol)
    coords={e:v for e,v in zip(arcs,sol)}
    points.append(S.Matrix([coords.get(e,S.Rational(0)) for e in U_ARCS]))
    witnessed.append((tuple(next(e for e in group if e in active)
         for group in (G1,G2,G3)),min(sol)))
assert len({v[0] for v in witnessed})==12
P=S.Matrix.hstack(*points)
assert S.Matrix.hstack(*(P[:,i]-P[:,0] for i in range(1,12))).rank()==4
assert all(points[j][U_ARCS.index(e)]>0 for e in FSET+SHARED for j in range(12))
for group in (G1,G2,G3):
    for e in group:
        zero=[j for j in range(12) if points[j][U_ARCS.index(e)]==0]
        assert len(zero)==(8 if len(group)==3 else 6)
        assert S.Matrix.hstack(*(points[j]-points[zero[0]]
            for j in zero[1:])).rank()==3
coords=[v[0] for v in witnessed]
edges=[(i,j) for i,j in combinations(range(12),2)
       if sum(a!=c for a,c in zip(coords[i],coords[j]))==1]
assert len(edges)==24
assert all(sum(i in e for e in edges)==4 for i in range(12))
g1=[sum(points[i][U_ARCS.index(e)] for e in G1) for i in range(12)]
assert len(set(g1))>1

print('R5_FACE_CONTACT_EXACT')
print('RANK18',U.rank(),'FACE_DIM',len(U_ARCS)-U.rank())
print('SUPPORT_CLASS',len(b['matching']),'POINTS',len(points),'FACETS',7)
print('SKELETON','K3 x K2 x K2','EDGES',len(edges),'DEGREE',4)
for i,(triplet,minimum) in enumerate(witnessed,1):
    print('VERTEX',i,'OPTIONS',triplet,'MIN_POS',minimum)
print('NONPRODUCT_AFFINE_COUPLING_G1_TOTALS',len(set(g1)))
print('PASS_EXACT_4D_12_VERTEX_7_FACET_COMBINATORIAL_DELTA2xI2_FACE')
