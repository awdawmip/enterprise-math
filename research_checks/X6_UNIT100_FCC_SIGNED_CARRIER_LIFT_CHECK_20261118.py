#!/usr/bin/env python3
"""Exact signed-orientation carrier lift of the historical 24 FCC rotations.

Derived 3D FCC line representation only; this does not promote an S4 carrier
representation to native P000 signed six-axis rotation dynamics.
"""
from itertools import combinations, permutations, product
from collections import Counter
import json

VERTICES = 'ABCD'
EDGES = tuple(combinations(VERTICES, 2))
VEC = {
    ('A', 'B'): (1, 1, 0),
    ('A', 'C'): (1, 0, 1),
    ('A', 'D'): (0, 1, -1),
    ('B', 'C'): (0, 1, 1),
    ('B', 'D'): (1, 0, -1),
    ('C', 'D'): (1, -1, 0),
}
INDEX = {e: i for i, e in enumerate(EDGES)}

def determinant(m):
    return (m[0][0] * (m[1][1]*m[2][2]-m[1][2]*m[2][1])
           -m[0][1] * (m[1][0]*m[2][2]-m[1][2]*m[2][0])
           +m[0][2] * (m[1][0]*m[2][1]-m[1][1]*m[2][0]))

def matvec(m,v):
    return tuple(sum(m[i][j] * v[j] for j in range(3)) for i in range(3))

def matmul(a,b):
    return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(3)) for j in range(3)) for i in range(3))

def signed_orientation_map(m):
    out=[]
    for e in EDGES:
        image=matvec(m,VEC[e])
        options=[(INDEX[f],s) for f in EDGES for s in (-1,1)
                 if image==tuple(s*x for x in VEC[f])]
        assert len(options)==1, (e,m,image,options)
        out.append(options[0])
    assert sorted(j for j,s in out)==list(range(6))
    return tuple(out)

def compose(a,b):
    return tuple((a[j][0], a[j][1]*sign) for j,sign in b)

matrices=[]
for cp in permutations(range(3)):
    for signs in product((-1,1),repeat=3):
        m=[[0]*3 for _ in range(3)]
        for j,row in enumerate(cp):m[row][j]=signs[j]
        m=tuple(tuple(row) for row in m)
        if determinant(m)==1:matrices.append(m)
assert len(matrices)==24 and len(set(matrices))==24
images={m:signed_orientation_map(m) for m in matrices}
unsigned={tuple(j for j,s in v) for v in images.values()}
assert len(unsigned)==24
negative=sum(s==-1 for v in images.values() for j,s in v)
fixed_but_reversed=sum(j==i and s==-1 for v in images.values() for i,(j,s) in enumerate(v))
wrong_any=sum(any(s==-1 for j,s in v) for v in images.values())
for a in matrices:
    for b in matrices:
        ab=matmul(a,b)
        assert ab in images
        assert images[ab]==compose(images[a],images[b])

witness=((-1,0,0),(0,-1,0),(0,0,1))
assert witness in images
ab_image=images[witness][INDEX[('A','B')]]
assert ab_image==(INDEX[('A','B')],-1)
result={
    'schema':'EM_X6_UNIT100_DERIVED_FCC_SIGNED_CARRIER_LIFT_CERT_V1',
    'historical_source':'fd2bcff10ca6e147348b6c1236027fc0d2877df3:research_checks/P000_6D_AXIS_MIXING_ROTATION_ALGEBRA_CHECK_20260829.py',
    'operations':'derived 3D determinant+1 signed coordinate permutation of six unoriented FCC carrier lines',
    'matrices':len(matrices),
    'unoriented_line_actions':len(unsigned),
    'signed_source_images':len(matrices)*6,
    'negative_orientation_images':negative,
    'fixed_line_with_orientation_reverse':fixed_but_reversed,
    'transformations_with_some_negative_images':wrong_any,
    'pair_compositions_checked':len(matrices)**2,
    'signed_basis_action_equalities_checked':len(matrices)**2*len(EDGES),
    'counterexample_matrix':witness,
    'counterexample_named_line':'AB',
    'counterexample_image_as_unoriented_line':'AB',
    'counterexample_image_as_signed_carrier_vector':'-AB',
    'claimed_native_p000_six_axis_rotation':False,
    'status':'EXACT_INTEGER_EXECUTED / UNREVIEWED / NOT_ADMITTED',
}
print(json.dumps(result,ensure_ascii=False,sort_keys=True,indent=2))
