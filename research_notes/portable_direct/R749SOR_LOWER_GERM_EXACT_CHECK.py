#!/usr/bin/env python3
"""R749SOR: exact joint rational certificate for s=1/2, 0<=t<=1/6.
Frozen Walsh source pin a72226e2430ffa4786321ac86e7f0c599d5f0389.
Python 3 standard library only.
"""
from fractions import Fraction as F
from itertools import combinations
from math import comb
import json

MASKS=(3,12,15,1,2,4,8)
SIGNS=tuple(tuple(1 if (k&m).bit_count()%2==0 else -1 for m in MASKS) for k in range(16))
# Unknowns: (t,h,u,v,w,z); all multiplied source inequalities by 2.
ROWS=tuple((2*a[0],2*a[2],2*a[3],2*a[4],2*a[5],2*a[6]) for a in SIGNS)+((1,0,0,0,0,0),(-6,0,0,0,0,0))
RHS=tuple(-2-a[1] for a in SIGNS)+(0,-1)

def solve(active):
    n=6
    a=[[ *ROWS[i], RHS[i]] for i in active]
    prev=1
    for col in range(n-1):
        k=next((k for k in range(col,n) if a[k][col]),None)
        if k is None:return None
        if k!=col:a[col],a[k]=a[k],a[col]
        pivot=a[col][col]
        for i in range(col+1,n):
            x=a[i][col]
            for j in range(col+1,n+1):
                numerator=a[i][j]*pivot-x*a[col][j]
                assert numerator%prev==0
                a[i][j]=numerator//prev
            a[i][col]=0
        prev=pivot
    if a[-1][-2]==0:return None
    v=[F(0)]*n
    for col in range(n-1,-1,-1):
        v[col]=(F(a[col][n])-sum((a[col][j]*v[j] for j in range(col+1,n)),F(0)))/a[col][col]
    return tuple(v)

def law(t,h,u,v,w,z):
    return tuple((1+t*r[0]+F(1,2)*r[1]+h*r[2]+u*r[3]+v*r[4]+w*r[5]+z*r[6])/16 for r in SIGNS)

def center(t):return law(t,3*t-F(1,2),F(0),F(0),F(0),F(0))

def tv(a,b):return sum((abs(x-y) for x,y in zip(a,b)),F(0))/2

def main():
    stat={'bases':0,'nonsingular':0,'feasible_bases':0,'distinct_vertices':0,
          'saturating_vertices':0,'violating_vertices':0,'max_excess':'','max_tv':'',
          'vertex_t_endpoints':{'0':0,'1/6':0},'interior_t_vertices':0}
    vertices=set()
    for active in combinations(range(18),6):
        stat['bases']+=1
        v=solve(active)
        if v is None:continue
        stat['nonsingular']+=1
        if any(sum(a*b for a,b in zip(row,v))<rhs for row,rhs in zip(ROWS,RHS)):continue
        stat['feasible_bases']+=1
        vertices.add(v)
    assert stat['bases']==comb(18,6)==18564 and vertices
    maximum=F(-100); maximum_tv=F(0)
    for v in vertices:
        t=v[0];p=law(*v);q=center(t)
        assert min(p)>=0 and min(q)>=0 and sum(p)==sum(q)==1
        d=tv(p,q);excess=d-(1-t)/2
        maximum=max(maximum,excess)
        maximum_tv=max(maximum_tv,d)
        stat['saturating_vertices']+=int(excess==0)
        stat['violating_vertices']+=int(excess>0)
        if t==0:stat['vertex_t_endpoints']['0']+=1
        elif t==F(1,6):stat['vertex_t_endpoints']['1/6']+=1
        else:stat['interior_t_vertices']+=1
    stat['distinct_vertices']=len(vertices)
    stat['max_excess']=str(maximum)
    stat['max_tv']=str(maximum_tv)
    assert maximum==0 and stat['violating_vertices']==0
    plus=law(0,0,0,0,F(1,2),1)
    minus=law(0,0,0,0,-F(1,2),-1)
    nu=law(1,F(1,2),0,0,0,0)
    assert min(plus)>=0 and min(minus)>=0 and min(nu)>=0
    for t in (F(0),F(1,20),F(1,12),F(1,6)):
        p=tuple((1-t)*x+t*z for x,z in zip(plus,nu))
        m=tuple((1-t)*x+t*z for x,z in zip(minus,nu))
        assert tv(p,m)==1-t and min(p)>=0 and min(m)>=0
    return {'research_id':'R749SOR','status':'PASS',
      'scientific_pin':'a72226e2430ffa4786321ac86e7f0c599d5f0389',
      'scope':'auxiliary Walsh source model, not reviewed',
      'theorem':'all real t in [0,1/6], s=1/2: rho=rho_cal=(1-t)/2',
      'calibrated_center':'(1+t*A+(1/2)*B+(3*t-1/2)*C)/16',
      'lower_diameter':'1-t from convexly mixed disjoint-support sources',
      'exact_joint_certificate':stat}

if __name__=='__main__':print(json.dumps(main(),sort_keys=True,indent=2))
