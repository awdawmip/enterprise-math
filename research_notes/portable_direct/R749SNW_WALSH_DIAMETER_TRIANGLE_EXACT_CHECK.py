#!/usr/bin/env python3
"""R749SNW: certified two-parameter diameter phase in the frozen 16-state Walsh fiber.
Scientific pin: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389.
Python standard library: integer Bareiss elimination and exact Fraction arithmetic.
"""
import itertools, json
from fractions import Fraction as F
from math import comb

PIN='a72226e2430ffa4786321ac86e7f0c599d5f0389'
MASKS=(3,12,15,1,2,4,8)
ROWS=tuple(tuple(1 if (m&x).bit_count()%2 == 0 else -1 for m in MASKS) for x in range(16))
TRI=((F(1,2),F(0)),(F(1,1),F(0)),(F(1,2),F(1,6)))
SCALE=6

def law(t,s,h,u,v,w,z):
    c=(t,s,h,u,v,w,z)
    return tuple((1+sum((a*b for a,b in zip(row,c)),F(0)))/16 for row in ROWS)

def eta(t,s): return t+3*s-1

def center(t,s): return law(t,s,eta(t,s),0,0,0,0)

def radius(t,s): return (1-s)/2

def witnesses(t,s):
    return (law(t,s,-s,1-s,t+s,0,0),law(t,s,-s,s-1,-t-s,0,0))

def tv(a,b): return sum((abs(x-y) for x,y in zip(a,b)),F(0))/2

def solve_bareiss(normals,bounds,active,n=7):
    a=[list(normals[k])+[bounds[k]] for k in active]
    prev=1
    for j in range(n-1):
        k=next((k for k in range(j,n) if a[k][j]),None)
        if k is None: return None
        if j!=k:a[j],a[k]=a[k],a[j]
        pivot=a[j][j]
        for i in range(j+1,n):
            mul=a[i][j]
            for k in range(j+1,n+1):
                num=a[i][k]*pivot-mul*a[j][k]
                assert num%prev==0
                a[i][k]=num//prev
            a[i][j]=0
        prev=pivot
    if not a[n-1][n-1]:return None
    x=[F(0)]*n
    for j in range(n-1,-1,-1):
        x[j]=(F(a[j][n])-sum((a[j][k]*x[k] for k in range(j+1,n)),F(0)))/a[j][j]
    return tuple(x)

def main():
    for t,s in TRI:
        p,m=witnesses(t,s)
        q=center(t,s)
        assert min(p)>=0 and min(m)>=0 and min(q)>=0
        assert sum(p)==sum(m)==sum(q)==1
        assert tv(p,m)==1-s
    # y=6(t,s,h,u,v,w,z), all 19 halfspaces have integer coefficients
    normals=list(ROWS)+[(1,0,0,0,0,0,0),(0,1,0,0,0,0,0),(-1,-3,0,0,0,0,0)]
    bounds=[-SCALE]*16+[3,0,-SCALE]
    assert len(normals)==19
    seen=set()
    stats={'active_bases':0,'nonsingular_bases':0,'feasible_bases':0}
    for active in itertools.combinations(range(19),7):
        stats['active_bases']+=1
        point=solve_bareiss(normals,bounds,active)
        if point is None:continue
        stats['nonsingular_bases']+=1
        if any(sum((a*b for a,b in zip(row,point)),F(0))<rhs
               for row,rhs in zip(normals,bounds)):
            continue
        stats['feasible_bases']+=1
        seen.add(tuple(v/SCALE for v in point))
    assert stats['active_bases']==comb(19,7)==50388
    assert seen
    max_excess=F(-10)
    tight=violate=0
    for t,s,h,u,v,w,z in seen:
        source=law(t,s,h,u,v,w,z)
        q=center(t,s)
        assert min(source)>=0 and min(q)>=0
        assert sum(source)==sum(q)==1
        ex=tv(source,q)-radius(t,s)
        max_excess=max(max_excess,ex)
        tight+=int(ex==0)
        violate+=int(ex>0)
    stats.update(distinct_vertices=len(seen),tight_vertices=tight,violating_vertices=violate,max_excess=str(max_excess))
    assert max_excess==0 and violate==0
    return dict(unit='R749SNW',status='PASS',review='NOT_REVIEWED',scientific_pin=PIN,
        model='16-state auxiliary Walsh source observer, not native X6/V29/V39',
        domain='all real t,s with 1/2<=t<=1, s>=0, t+3s<=1',
        triangle_vertices=[[str(a),str(b)] for a,b in TRI],
        theorem='rho(t,s)=rho_cal(t,s)=(1-s)/2',
        calibrated_center='(1+t*chi_3+s*chi_12+(t+3*s-1)*chi_15)/16',
        lower_source_pair='h=-s, u=+/- (1-s), v=+/- (t+s), w=z=0, simultaneous signs',
        lower_diameter='TV(mu_plus,mu_minus)=1-s',
        area='1/24',
        exact_joint_vertex_certificate=stats,
        next_question='Extend the lower-s diameter phase to t<1/2 and determine its sharp boundary; test admissible alternative calibrated centers across the t+3s=1 interface')

if __name__=='__main__':
    print(json.dumps(main(),ensure_ascii=False,sort_keys=True,indent=2))
