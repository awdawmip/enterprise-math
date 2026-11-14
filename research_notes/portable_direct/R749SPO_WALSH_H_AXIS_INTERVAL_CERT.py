#!/usr/bin/env python3
"""Exact rational certificate for the complete h-axis minimax-center interval.
Scientific source pin: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389.
"""
import json
from itertools import combinations
from math import comb
from fractions import Fraction as F

MASKS=(3,12,15,1,2,4,8)
W=tuple(tuple(-1 if (k&m).bit_count()%2 else 1 for m in MASKS) for k in range(16))

def solve(rows,rhs,inds):
    n=7
    a=[list(rows[i])+[rhs[i]] for i in inds]
    prev=1
    for j in range(n-1):
        p=next((i for i in range(j,n) if a[i][j]),None)
        if p is None:return None
        if p!=j:a[j],a[p]=a[p],a[j]
        pivot=a[j][j]
        for i in range(j+1,n):
            v=a[i][j]
            for k in range(j+1,n+1):
                z=a[i][k]*pivot-v*a[j][k]
                if z%prev:raise ArithmeticError('Non-exact Bareiss division')
                a[i][k]=z//prev
            a[i][j]=0
        prev=pivot
    if not a[n-1][n-1]:return None
    x=[F(0)]*n
    for j in range(n-1,-1,-1):
        x[j]=(F(a[j][n])-sum((a[j][k]*x[k] for k in range(j+1,n)),F(0)))/a[j][j]
    return tuple(x)

def law(t,s,h,u=0,v=0,w=0,z=0):
    c=(t,s,h,u,v,w,z)
    return tuple((1+sum(a*b for a,b in zip(row,c)))/16 for row in W)

def tv(p,q):
    return sum((abs(a-b) for a,b in zip(p,q)),F(0))/2

# Affine h(t,s)=A*t+B*s+C. Each case has exactly one extra chamber facet.
CASES=(
 ('lower-left', (2,-1,0), (-1,-2,0,0,0,0,0), -1),
 ('lower-right',(3,1,-1),(1,2,0,0,0,0,0), 1),
 ('upper-left',(0,1,0),(-3,-2,0,0,0,0,0), -1),
 ('upper-right',(-3,-1,1),(3,2,0,0,0,0,0),1),
)

def run():
    out={}
    for tag, hcoef, extra, rhs_extra in CASES:
        rows=list(W)+[(1,0,0,0,0,0,0),(-1,1,0,0,0,0,0),(-4,-1,0,0,0,0,0),extra]
        rhs=[-1]*16+[0,0,-1,rhs_extra]
        nonsing=feasible=0
        verts=set()
        for inds in combinations(range(20),7):
            x=solve(rows,rhs,inds)
            if x is None:continue
            nonsing+=1
            if all(sum(a*b for a,b in zip(row,x))>=bound for row,bound in zip(rows,rhs)):
                feasible+=1
                verts.add(x)
        maximum=None
        tight=0
        for x in verts:
            t,s=x[:2]
            h=hcoef[0]*t+hcoef[1]*s+hcoef[2]
            p=law(*x)
            q=law(t,s,h)
            assert min(p)>=0 and min(q)>=0 and sum(p)==sum(q)==1
            excess=tv(p,q)-(1-t)/2
            maximum=excess if maximum is None else max(maximum,excess)
            tight+=excess==0
        assert maximum==0,(tag,maximum)
        out[tag]={
          'h':str(hcoef),
          'candidate_bases':comb(20,7),
          'nonsingular':nonsing,
          'feasible_bases_including_repeats':feasible,
          'distinct_vertices':len(verts),
          'tight_vertices':tight,
          'maximum_exact_excess':str(maximum)}
    print(json.dumps({
      'status':'PASS',
      'pin':'awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389',
      'cases':out},sort_keys=True,indent=2))

if __name__=='__main__':
    run()
