#!/usr/bin/env python3
"""Exact seven-dimensional proof certificate for a new auxiliary Walsh zero-gap wedge.

Scientific pin: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389.
Only standard Python, exact integer Bareiss elimination and rational TV.
"""
import json
from fractions import Fraction as F
from itertools import combinations
from math import comb

MASKS=(3,12,15,1,2,4,8)
W=tuple(tuple(-1 if (k&m).bit_count()%2 else 1 for m in MASKS) for k in range(16))

def law(t,s,h=F(0),u=F(0),v=F(0),w=F(0),z=F(0)):
    coefs=(t,s,h,u,v,w,z)
    return tuple((1+sum((a*b for a,b in zip(row,coefs)),F(0)))/16 for row in W)

def tv(p,q):
    return sum((abs(a-b) for a,b in zip(p,q)),F(0))/2

def solve(rows,rhs,inds):
    n=7
    a=[list(rows[i])+[rhs[i]] for i in inds]
    prev=1
    for j in range(n-1):
        idx=next((i for i in range(j,n) if a[i][j]),None)
        if idx is None:return None
        if idx!=j:a[j],a[idx]=a[idx],a[j]
        pivot=a[j][j]
        for i in range(j+1,n):
            v=a[i][j]
            for k in range(j+1,n+1):
                numerator=a[i][k]*pivot-v*a[j][k]
                if numerator%prev:raise ArithmeticError('Bareiss exact division failed')
                a[i][k]=numerator//prev
            a[i][j]=0
        prev=pivot
    if not a[-1][-2]:return None
    x=[F(0)]*n
    for j in range(n-1,-1,-1):
        x[j]=(F(a[j][n])-sum((a[j][k]*x[k] for k in range(j+1,n)),F(0)))/a[j][j]
    return tuple(x)

def fmt(x):
    return str(x.numerator) if x.denominator==1 else f'{x.numerator}/{x.denominator}'

def source_pair(t,s):
    return (law(t,s,0,-t,-t,s,1-t),law(t,s,0,-t,-t,-s,t-1))

def run():
    # S = conv((0,0),(0,1),(1/5,1/5)); exact facets t>=0,s>=t,4t+s<=1.
    rows=list(W)+[(1,0,0,0,0,0,0),(-1,1,0,0,0,0,0),(-4,-1,0,0,0,0,0)]
    rhs=[-1]*16+[0,0,-1]
    assert len(rows)==19
    vertices=set();nonsingular=feasible=0
    for inds in combinations(range(19),7):
        x=solve(rows,rhs,inds)
        if x is None:continue
        nonsingular+=1
        if all(sum((a*b for a,b in zip(row,x)),F(0))>=bound for row,bound in zip(rows,rhs)):
            feasible+=1
            vertices.add(x)
    assert comb(19,7)==50388 and vertices
    projection={};tight=0;maximum=None
    for x in vertices:
        t,s=x[:2]
        assert 0<=t and t<=s and 4*t+s<=1
        p=law(*x)
        q=law(t,s,t,0,0,0,0)
        assert min(p)>=0 and min(q)>=0 and sum(p)==sum(q)==1
        excess=tv(p,q)-(1-t)/2
        if maximum is None or excess>maximum:maximum=excess
        tight+=int(excess==0)
        projection[(t,s)]=projection.get((t,s),0)+1
        a,b=source_pair(t,s)
        assert min(a)>=0 and min(b)>=0 and tv(a,b)==1-t
    assert maximum==0,maximum
    print(json.dumps({
      'theorem':'R749SPN auxiliary Walsh new zero-gap wedge with nonzero-h calibrated center',
      'scientific_pin':'awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389',
      'status':'PASS',
      'domain':'conv{(0,0),(0,1),(1/5,1/5)} = {t>=0, s>=t, 4t+s<=1}',
      'calibrated_center':'p(t,s,h=t,u=0,v=0,w=0,z=0)',
      'risk_radius':'(1-t)/2',
      'gap':'0',
      'reflected_domain':'conv{(0,0),(1,0),(1/5,1/5)}',
      'reflected_radius':'(1-s)/2',
      'new_triangle_area':'1/10',
      'total_reflected_area':'1/5',
      'candidate_active_seven_facets':comb(19,7),
      'nonsingular_bases':nonsingular,
      'feasible_bases_with_repetition':feasible,
      'distinct_exact_vertices':len(vertices),
      'tight_vertices':tight,
      'vertex_projection':{','.join(map(fmt,p)):n for p,n in sorted(projection.items())},
      'maximum_risk_excess':fmt(maximum),
      'verification':'Complete 7D rational joint-source vertex enumeration; exact convexity and source-pair distance',
      'review':'AUTHOR_EXACT_NOT_REVIEWED'
    },ensure_ascii=False,sort_keys=True,indent=2))

if __name__=='__main__':run()
