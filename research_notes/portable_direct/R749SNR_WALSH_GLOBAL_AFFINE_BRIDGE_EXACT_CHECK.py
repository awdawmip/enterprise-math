#!/usr/bin/env python3
"""R749SNR: exact Walsh zero-calibration affine bridge, author-side certificate.
Frozen source: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389
Only Python standard library, integer Bareiss and Fraction.
"""
from fractions import Fraction as F
from itertools import combinations
from math import comb
import json

MASKS=(3,12,15,1,2,4,8)
ROWS=tuple(tuple(1 if (m&x).bit_count()%2==0 else -1 for m in MASKS) for x in range(16))
EVENT=(3,5,7,9,11,13,14,15)
TRI=((F(7,10),F(3,20)),(F(1,2),F(3,10)),(F(1),F(0)))
PIN='a72226e2430ffa4786321ac86e7f0c599d5f0389'

def law(t,s,h,u,v,w,z):
    coeffs=(t,s,h,u,v,w,z)
    return tuple((1+sum((a*b for a,b in zip(row,coeffs)),F(0)))/16 for row in ROWS)

def eta(t,s): return (3*t+5*s-3)/2
def radius(t,s): return (3+t-s)/8

def solve(rows,rhs,idx,n=7):
    a=[list(rows[i])+[rhs[i]] for i in idx]
    last=1
    for j in range(n-1):
        k=next((k for k in range(j,n) if a[k][j]),None)
        if k is None: return None
        if k!=j: a[j],a[k]=a[k],a[j]
        pivot=a[j][j]
        for i in range(j+1,n):
            c=a[i][j]
            for col in range(j+1,n+1):
                z=a[i][col]*pivot-c*a[j][col]
                assert z%last==0
                a[i][col]=z//last
            a[i][j]=0
        last=pivot
    if not a[n-1][n-1]: return None
    v=[F(0)]*n
    for j in range(n-1,-1,-1):
        v[j]=(F(a[j][n])-sum((a[j][k]*v[k] for k in range(j+1,n)),F(0)))/a[j][j]
    return tuple(v)

def exact_certificate():
    # y=20*(t,s,h,u,v,w,z); inequalities have integer normals/RHS
    # 30t+40s>=27, 3t+5s<=3, t+2s>=1.
    scale=20
    rows=list(ROWS)+[(30,40,0,0,0,0,0),(-3,-5,0,0,0,0,0),(1,2,0,0,0,0,0)]
    rhs=[-scale]*16+[27*scale,-3*scale,scale]
    stats={'active_bases':0,'nonsingular_bases':0,'feasible_bases':0,'distinct_vertices':0,
           'tight_vertices':0,'violating_vertices':0,'max_excess':None}
    seen=set()
    for active in combinations(range(19),7):
        stats['active_bases']+=1
        vals=solve(rows,rhs,active)
        if vals is None: continue
        stats['nonsingular_bases']+=1
        if any(sum((a*b for a,b in zip(row,vals)),F(0))<b for row,b in zip(rows,rhs)):
            continue
        stats['feasible_bases']+=1
        seen.add(tuple(x/scale for x in vals))
    assert stats['active_bases']==comb(19,7)==50388
    stats['distinct_vertices']=len(seen)
    assert seen
    biggest=F(-100)
    for t,s,h,u,v,w,z in seen:
        q=law(t,s,eta(t,s),0,0,0,0)
        mu=law(t,s,h,u,v,w,z)
        assert min(mu)>=0 and min(q)>=0 and sum(mu)==sum(q)==1
        tv=sum((abs(a-b) for a,b in zip(mu,q)),F(0))/2
        gap=tv-radius(t,s)
        biggest=max(biggest,gap)
        stats['tight_vertices']+=int(gap==0)
        stats['violating_vertices']+=int(gap>0)
    stats['max_excess']=str(biggest)
    assert biggest==0
    assert all(sum(ROWS[x][j] for x in EVENT)==0 for j in range(3))
    for t,s in TRI:
        q=law(t,s,eta(t,s),0,0,0,0)
        w=law(t,s,0,s-1,-t,-s,-s)
        assert min(q)>=0 and min(w)>=0
        assert sum(q)==sum(w)==1
        assert sum((w[x] for x in EVENT),F(0))-F(1,2)==radius(t,s)
    # For any invariant center with moments (1,t,s,h) on {1,A,D,AD},
    # E has every such non-constant Walsh character sum=0.
    return stats

def main():
    c=exact_certificate()
    return {'unit':'R749SNR','status':'PASS','frozen_scientific_pin':PIN,
      'scope':'16-state auxiliary Walsh source observer, all real points in bridge triangle; NOT_REVIEWED',
      'vertices':[[str(v) for v in p] for p in TRI],
      'halfspaces':['30t+40s>=27','3t+5s<=3','t+2s>=1'],
      'area':'3/400','rho_equals_rho_cal':'(3+t-s)/8',
      'calibrated_center':'q=(1+t chi_3+s chi_12+((3t+5s-3)/2)chi_15)/16',
      'lower_source':'(h,u,v,w,z)=(0,s-1,-t,-s,-s)',
      'lower_event':list(EVENT),'exact_joint_vertex_certificate':c}

if __name__=='__main__':
    print(json.dumps(main(),ensure_ascii=False,sort_keys=True,indent=2))
