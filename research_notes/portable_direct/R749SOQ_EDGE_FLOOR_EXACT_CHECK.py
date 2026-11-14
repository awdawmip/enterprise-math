#!/usr/bin/env python3
"""R749SOQ exact axis minimax and lower-triangle floor certificates.
Python 3 standard library only; all vertex checks use exact integer/rational arithmetic.
Frozen source: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389.
"""
from fractions import Fraction as F
from itertools import combinations
from math import comb
import json

MASKS=(12,15,1,2,4,8)       # s,h,u,v,w,z with t=0
ROWS=tuple(tuple(1 if (k&m).bit_count()%2==0 else -1 for m in MASKS) for k in range(16))
FACETS=ROWS+((1,0,0,0,0,0),(-1,0,0,0,0,0))
RHS=(-1,)*16+(0,-1)

def solve(active):
    n=6
    a=[[ *FACETS[i], RHS[i]] for i in active]
    prev=1
    for j in range(n-1):
        k=next((k for k in range(j,n) if a[k][j]),None)
        if k is None:return None
        if k!=j:a[j],a[k]=a[k],a[j]
        pivot=a[j][j]
        for i in range(j+1,n):
            q=a[i][j]
            for c in range(j+1,n+1):
                x=a[i][c]*pivot-q*a[j][c]
                assert x%prev==0
                a[i][c]=x//prev
            a[i][j]=0
        prev=pivot
    if a[n-1][n-1]==0:return None
    v=[F(0)]*n
    for j in range(n-1,-1,-1):
        v[j]=(F(a[j][n])-sum((a[j][k]*v[k] for k in range(j+1,n)),F(0)))/a[j][j]
    return tuple(v)

def law(s,h,u,v,w,z):
    return tuple((1+sum(a*b for a,b in zip(row,(s,h,u,v,w,z))))/16 for row in ROWS)

def tv(p,q):
    return sum((abs(x-y) for x,y in zip(p,q)),F(0))/2

def axis_certificate():
    stats={'bases':0,'nonsingular_bases':0,'feasible_bases':0,'distinct_vertices':0,
           'bound_tight_vertices':0,'bound_violations':0,'interior_vertices':0,
           's_endpoints_counts':{'0':0,'1':0},'max_tv':None}
    vertices=set()
    for basis in combinations(range(18),6):
        stats['bases']+=1
        v=solve(basis)
        if v is None:continue
        stats['nonsingular_bases']+=1
        if any(sum(a*b for a,b in zip(row,v))<rhs for row,rhs in zip(FACETS,RHS)):continue
        stats['feasible_bases']+=1
        vertices.add(v)
    assert stats['bases']==comb(18,6)==18564 and vertices
    maximum=F(0)
    for v in vertices:
        s=v[0]
        p=law(*v)
        q=law(s,0,0,0,0,0)
        assert min(p)>=0 and min(q)>=0 and sum(p)==sum(q)==1
        d=tv(p,q)
        maximum=max(maximum,d)
        stats['bound_tight_vertices']+=int(d==F(1,2))
        stats['bound_violations']+=int(d>F(1,2))
        if s==0:stats['s_endpoints_counts']['0']+=1
        elif s==1:stats['s_endpoints_counts']['1']+=1
        else:stats['interior_vertices']+=1
    stats['distinct_vertices']=len(vertices)
    stats['max_tv']=str(maximum)
    assert maximum==F(1,2) and stats['bound_violations']==0
    for s in (F(0),F(1,7),F(1,2),F(6,7),F(1)):
        p=law(s,0,0,0,s,1)
        m=law(s,0,0,0,-s,-1)
        q=law(s,0,0,0,0,0)
        assert min(p)>=0 and min(m)>=0 and tv(p,m)==1
        assert tv(p,q)==tv(m,q)==F(1,2)
    return stats

ALL_MASKS=(3,12,15,1,2,4,8)
def full(t,s,h,u,v,w,z):
    return tuple((1+sum(a*b for a,b in zip((t,s,h,u,v,w,z),
      (1 if (k&m).bit_count()%2==0 else -1 for m in ALL_MASKS))))/16
        for k in range(16))

def floor_certificate():
    pairs=[(F(0),F(0)),(F(1,9),F(4,9)),(F(1,3),F(2,3)),
           (F(3,7),F(2,7)),(F(1),F(0)),(F(0),F(1))]
    tests=0
    for t,s in pairs:
        for k in range(16):
            x=1 if k&1==0 else -1
            y=1 if k&4==0 else -1
            p00=full(0,0,0,-x,0,0,0)
            p10=full(1,0,0,-x,-x,0,0)
            p01=full(0,1,0,0,0,-y,-y)
            for p in (p00,p10,p01):
                assert min(p)>=0 and sum(p)==1 and p[k]==0
            mix=tuple((1-t-s)*p00[i]+t*p10[i]+s*p01[i] for i in range(16))
            assert min(mix)>=0 and sum(mix)==1 and mix[k]==0
            tests+=1
    return {'param_pairs':len(pairs),'atom_witness_checks':tests,
      'analytic_domain':'all real t>=0,s>=0,t+s<=1 via convex corner construction',
      'upper_triangle_reference':'R749SOP exact common floor for t+s>=1'}

def main():
    return {'research_id':'R749SOQ','status':'PASS',
      'scientific_pin':'a72226e2430ffa4786321ac86e7f0c599d5f0389',
      'scope':'auxiliary 16-atom Walsh model; author-side NOT_REVIEWED',
      'axis_theorem':'rho(0,s)=rho_cal(0,s)=1/2 for all real 0<=s<=1, and swapped',
      'common_floor':'t+s<=1: all atomwise infima 0; t+s>=1: (t+s-1)*sigma using R749SOP',
      'axis_certificate':axis_certificate(),'common_floor_checks':floor_certificate()}

if __name__=='__main__':print(json.dumps(main(),ensure_ascii=False,sort_keys=True,indent=2))
