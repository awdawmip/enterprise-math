#!/usr/bin/env python3
"""Exact source-vertex certificate for the R749SPP optimal-center octahedron.
Frozen scientific input: enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389.
Standard-library integer Bareiss and Fraction, no floating tolerances.
"""
from fractions import Fraction as F
from itertools import combinations
from math import comb
import json

MASKS=(3,12,15,1,2,4,8)
W=tuple(tuple(-1 if (k&m).bit_count()%2 else 1 for m in MASKS) for k in range(16))

def law(t,s,h=0,u=0,v=0,w=0,z=0):
    coefs=(t,s,h,u,v,w,z)
    return tuple((1+sum(a*b for a,b in zip(row,coefs)))/16 for row in W)

def solve(rows,rhs,inds):
    n=5
    a=[list(rows[i])+[rhs[i]] for i in inds]
    prev=1
    for j in range(n-1):
        idx=next((i for i in range(j,n) if a[i][j]),None)
        if idx is None:return None
        if idx!=j:a[j],a[idx]=a[idx],a[j]
        p=a[j][j]
        for i in range(j+1,n):
            v=a[i][j]
            for k in range(j+1,n+1):
                num=a[i][k]*p-v*a[j][k]
                if num%prev:raise ArithmeticError('Nonexact Bareiss division')
                a[i][k]=num//prev
            a[i][j]=0
        prev=p
    if not a[-1][-2]:return None
    x=[F(0)]*n
    for j in range(n-1,-1,-1):
        x[j]=(F(a[j][n])-sum((a[j][k]*x[k] for k in range(j+1,n)),F(0)))/a[j][j]
    return tuple(x)

def tv(p,q):
    return sum((abs(a-b) for a,b in zip(p,q)),F(0))/2

def run():
    t,s=F(1,10),F(1,2)
    rows=[row[2:] for row in W]
    rhs=[int(10*(-1-row[0]*t-row[1]*s)) for row in W]
    vertices=set();nonsingular=feasible=0
    for inds in combinations(range(16),5):
        x10=solve(rows,rhs,inds)
        if x10 is None:continue
        nonsingular+=1
        if all(sum(a*b for a,b in zip(row,x10))>=v for row,v in zip(rows,rhs)):
            feasible+=1
            vertices.add(tuple(x/10 for x in x10))
    assert comb(16,5)==4368 and len(vertices)==50
    assert nonsingular==3008 and feasible==196
    rad=F(9,20)
    # Six extremal Walsh centers (h,u,v), w=z=0.
    corners={
       'h+':(F(1,5),F(0),F(0)),'h-':(-F(1,5),F(0),F(0)),
       'u+':(F(0),F(1,5),F(0)),'u-':(F(0),-F(1,5),F(0)),
       'v+':(F(0),F(0),F(1,5)),'v-':(F(0),F(0),-F(1,5))
    }
    endpoints={}
    for name,(h,u,v) in corners.items():
        q=law(t,s,h,u,v,0,0)
        assert sum(q)==1 and min(q)>=0
        excesses=[tv(law(t,s,*x),q)-rad for x in vertices]
        assert max(excesses)==0,(name,max(excesses))
        endpoints[name]={'max_exact_excess':'0','tight_source_vertices':excesses.count(F(0))}
    # The known pair is an exact radius lower bound.
    Pp=law(t,s,0,-t,-t,s,1-t)
    Pm=law(t,s,0,-t,-t,-s,t-1)
    assert min(Pp)>=0 and min(Pm)>=0 and tv(Pp,Pm)==F(9,10)
    print(json.dumps({
      'status':'PASS','source_pin':'awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389',
      'fixed_moments':{'t':'1/10','s':'1/2'},
      'radius':'9/20',
      'optimal_center_octahedron':'|h|+|u|+|v|<=1/5, w=z=0',
      'volume_in_huv_coordinates':'4/375',
      'candidate_bases':4368,'nonsingular_bases':nonsingular,
      'feasible_bases_with_repetition':feasible,'distinct_exact_source_vertices':len(vertices),
      'lower_source_pair_distance':'9/10',
      'six_extremal_centers':endpoints,
      'review':'AUTHOR_EXACT_NOT_REVIEWED'
    },indent=2,sort_keys=True))
if __name__=='__main__':run()
