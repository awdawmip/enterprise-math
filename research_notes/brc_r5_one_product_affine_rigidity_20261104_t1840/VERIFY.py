#!/usr/bin/env python3
"""Exact exhaustive verification; analytic all-real proof is in RESEARCH.md."""
from fractions import Fraction as F
from itertools import combinations, product
Z=(0,0)
def add(a,b): return (a[0]+b[0],a[1]+b[1])
def sub(a,b): return (a[0]-b[0],a[1]-b[1])
def dot(a,b): return a[0]*b[0]+a[1]*b[1]
def det(a,b): return a[0]*b[1]-a[1]*b[0]
def mul(q,a): return (q*a[0],q*a[1])
def in_hull(p,pts):
    if p in pts: return True
    for u,v in combinations(pts,2):
        e=sub(v,u);t=sub(p,u)
        if e!=Z and det(e,t)==0 and 0<=dot(e,t)<=dot(e,e): return True
    for u,v,w in combinations(pts,3):
        e=sub(v,u);f=sub(w,u);t=sub(p,u);d=det(e,f)
        if not d: continue
        n1=det(t,f);n2=det(e,t);n0=d-n1-n2
        if (d>0 and min(n0,n1,n2)>=0) or (d<0 and max(n0,n1,n2)<=0): return True
    return False
def full(a,b,c):
    return [Z,b,a,add(a,b),add(a,c),add(add(a,b),c)]
def lr(a,b,c):
    return [Z,a,b,add(add(a,b),c)]
vectors=list(product(range(-2,3),repeat=2))
total=0; equal=0; strict=0
for a,b,c in product(vectors,repeat=3):
    eq=all(in_hull(p,lr(a,b,c)) for p in full(a,b,c))
    expected=b==Z or (det(b,c)==0 and dot(b,c)>=0)
    assert eq==expected,(a,b,c)
    total+=1;equal+=int(eq);strict+=int(not eq)
print('EXACT_BOX_CHECK','vectors',len(vectors),'triples',total,'hull_equal',equal,'hull_strict',strict)
def read(a,b,c,x,y,z):
    return add(add(mul(x,a),mul(y,b)),mul(z,c))
for a,b,c,tag in [((1,1),(1,0),(2,0),'POSITIVE_ALIGNED'),
                  ((1,0),Z,(0,1),'ZERO_BYPASS')]:
    cases=0
    for xi in range(5):
        x=F(xi,4)
        for yi in range(5):
            y=F(yi,4)
            for zi in range(xi+1):
                z=F(zi,4)
                if b==Z: yy=z/x if x else F(0)
                else:
                    lam=F(dot(b,c),dot(b,b))
                    assert lam>=0 and mul(lam,b)==c
                    yy=(y+lam*z)/(1+lam*x)
                assert 0<=yy<=1
                assert read(a,b,c,x,yy,x*yy)==read(a,b,c,x,y,z)
                cases+=1
    print('EXACT_RATIONAL_RECONSTRUCTION',tag,cases)
for a,b,c,n,w,tag in [
 ((1,1),(1,0),(0,1),(1,-1),(1,0,1),'INDEPENDENT_B_C'),
 ((1,1),(1,0),(-1,0),(1,-1),(1,0,1),'NEGATIVE_ALIGNED')]:
    x,y,z=map(F,w)
    witness=read(a,b,c,x,y,z)
    lower_lr=min(dot(n,p) for p in lr(a,b,c))
    lower_f=min(dot(n,p) for p in full(a,b,c))
    assert dot(n,witness)==lower_f and lower_lr-lower_f==1
    print('EXACT_STRICT_SEPARATOR',tag,'witness',witness,'normal',n,
          'min_LR',lower_lr,'min_FULL',lower_f,'gap',lower_lr-lower_f)
print('PASS_EXACT_R5_ONE_PRODUCT_AFFINE_RIGIDITY')
