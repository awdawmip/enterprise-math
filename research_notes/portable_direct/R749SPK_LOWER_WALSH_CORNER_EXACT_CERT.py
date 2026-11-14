#!/usr/bin/env python3
"""R749SPK: exact 2D lower-triangle Walsh calibrated minimax theorem.

Complete seven-dimensional rational polytope vertex enumeration; all arithmetic
is integer or fractions.Fraction. No third-party packages or tolerances.
"""
import json
from fractions import Fraction as F
from itertools import combinations
from math import comb

MASKS = (3,12,15,1,2,4,8)
W = tuple(tuple(-1 if ((k&m).bit_count() & 1) else 1 for m in MASKS) for k in range(16))

def law(t,s,h=F(0),u=F(0),v=F(0),w=F(0),z=F(0)):
    vals = (t,s,h,u,v,w,z)
    return tuple((1+sum((a*b for a,b in zip(row,vals)), F(0)))/16 for row in W)

def tv(p,q):
    return sum((abs(a-b) for a,b in zip(p,q)), F(0))/2

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
                numer=a[i][k]*pivot-v*a[j][k]
                if numer%prev:raise ArithmeticError('non-integral Bareiss division')
                a[i][k]=numer//prev
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
    # For the entire lower parameter triangle t,s>=0,t+s<=1, both are legal.
    return (law(t,s,0,-t,-t,s,1-t),
            law(t,s,0,-t,-t,-s,t-1))

def check():
    # T = conv{(0,0),(0,1),(1/5,2/5)} =
    # {(t,s): t>=0, s>=2t, s+3t<=1}.
    rows=list(W)+[(1,0,0,0,0,0,0),(-2,1,0,0,0,0,0),(-3,-1,0,0,0,0,0)]
    rhs=[-1]*16+[0,0,-1]
    assert len(rows)==19
    vertices=set()
    nonsingular=feasible=0
    for inds in combinations(range(19),7):
        x=solve(rows,rhs,inds)
        if x is None:continue
        nonsingular+=1
        if all(sum((a*b for a,b in zip(row,x)),F(0))>=bound for row,bound in zip(rows,rhs)):
            feasible+=1
            vertices.add(x)
    assert comb(19,7)==50388 and vertices
    projection={};max_excess=None;tight=0
    for x in vertices:
        t,s=x[:2]
        projection[(t,s)]=projection.get((t,s),0)+1
        assert 0<=t and 2*t<=s and s+3*t<=1
        p=law(*x)
        q=law(t,s)
        assert min(p)>=0 and min(q)>=0 and sum(p)==sum(q)==1
        excess=tv(p,q)-(1-t)/2
        if max_excess is None or excess>max_excess:max_excess=excess
        tight+=int(excess==0)
    assert max_excess==0, max_excess
    for t,s in projection:
        p1,p2=source_pair(t,s)
        assert min(p1)>=0 and min(p2)>=0
        assert sum(p1)==sum(p2)==1
        assert tv(p1,p2)==1-t
    for k in range(16):
        j=((k&3)<<2)|((k&12)>>2)
        assert W[j]==(W[k][1],W[k][0],W[k][2],W[k][5],W[k][6],W[k][3],W[k][4])
    data={
        'status':'PASS',
        'theorem':'R749SPK exact lower Walsh zero-gap triangles',
        'scientific_pin':'awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389',
        'domain_T':'conv{(0,0),(0,1),(1/5,2/5)}',
        'domain_T_reflection':'conv{(0,0),(1,0),(2/5,1/5)}',
        'radius':'(1-t)/2 in T; (1-s)/2 in reflected T',
        'gap':'0 on both triangles',
        'center':'q(t,s)=p(t,s,0,0,0,0,0)',
        'source_pair_distance':'TV(Pplus,Pminus)=1-t on T',
        'two_region_total_area':'1/5',
        'candidate_seven_facet_bases':comb(19,7),
        'nonsingular_bases':nonsingular,
        'feasible_bases_including_repetitions':feasible,
        'distinct_exact_vertices':len(vertices),
        'tight_vertices':tight,
        'vertex_parameter_projection':{','.join(fmt(y) for y in p):n for p,n in sorted(projection.items())},
        'maximum_risk_excess':fmt(max_excess),
        'bit_pair_exchange_exact':True,
        'verification':'Bareiss integer elimination + Fraction exact feasibility and convexity',
        'mathematical_status':'AUTHOR_EXACT_NOT_REVIEWED; auxiliary model only'
    }
    print(json.dumps(data,ensure_ascii=False,sort_keys=True,indent=2))

if __name__=='__main__':check()
