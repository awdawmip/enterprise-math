#!/usr/bin/env python3
"""R749SNM: exact 7-D rational vertex certificate for an all-real Walsh zero-gap polygon."""
from fractions import Fraction as F
from itertools import combinations
from math import comb
import json

B=(3,5,6,7,9,10,11,12,13,14)
R=[tuple(1 if ((m&x).bit_count()%2)==0 else -1 for m in (3,12,15,1,2,4,8)) for x in range(16)]
E=(3,5,7,9,11,13,14,15)
VERTICES=((F(3,5),F(1,4)),(F(4,5),F(1,5)),(F(13,20),F(7,20)),(F(3,5),F(7,20)))

def law(t,s,h,u,v,w,z):
    return tuple((1+t*a+s*d+h*ad+u*p+v*ap+w*q+z*dq)/16 for a,d,ad,p,ap,q,dq in R)

def center(t,s):
    return tuple((1+t*a+s*d)/16 for a,d,*_ in R)

def radius(t,s):
    return (3+t-s)/8

def constraints():
    L=20
    M=list(R)
    b=[-L]*16
    M.extend(((1,0,0,0,0,0,0),(0,-1,0,0,0,0,0),(-1,-1,0,0,0,0,0),(1,4,0,0,0,0,0)))
    b.extend((12,-7,-20,32))
    return L,M,b

def solve_exact(indices,M,b,n=7):
    a=[list(M[i])+[b[i]] for i in indices]
    prev=1
    for j in range(n-1):
        pivot=next((i for i in range(j,n) if a[i][j]),None)
        if pivot is None:
            return None
        if pivot!=j:
            a[j],a[pivot]=a[pivot],a[j]
        p=a[j][j]
        for i in range(j+1,n):
            q=a[i][j]
            for k in range(j+1,n+1):
                val=a[i][k]*p-q*a[j][k]
                assert val%prev==0
                a[i][k]=val//prev
            a[i][j]=0
        prev=p
    if a[-1][-2]==0:
        return None
    v=[F(0)]*n
    for j in range(n-1,-1,-1):
        v[j]=(F(a[j][-1])-sum((a[j][k]*v[k] for k in range(j+1,n)),F(0)))/a[j][j]
    return tuple(v)

def main():
    L,M,b=constraints()
    assert len(M)==20 and comb(20,7)==77520
    assert all(t>=F(3,5) and s<=F(7,20) and t+s<=1 and t+4*s>=F(8,5) for t,s in VERTICES)
    assert all(sum(R[x][j] for x in E)==0 for j in range(3))
    for t,s in VERTICES:
        w=law(t,s,F(0),s-1,-t,-s,-s)
        q=center(t,s)
        assert all(a>=0 for a in w+q) and sum(w)==sum(q)==1
        assert sum((w[x] for x in E),F(0))-F(1,2)==radius(t,s)
    stats=dict(active_seven_facet_sets=0,nonsingular_bases=0,feasible_bases=0,unique_joint_vertices=0,tight_vertices=0,violating_vertices=0)
    seen=set()
    for inds in combinations(range(20),7):
        stats['active_seven_facet_sets']+=1
        v=solve_exact(inds,M,b)
        if v is None:
            continue
        stats['nonsingular_bases']+=1
        if any(sum((u*z for u,z in zip(row,v)),F(0))<rhs for row,rhs in zip(M,b)):
            continue
        stats['feasible_bases']+=1
        seen.add(tuple(z/L for z in v))
    stats['unique_joint_vertices']=len(seen)
    assert seen
    worst=None
    for params in seen:
        t,s=params[:2]
        mu=law(*params)
        q=center(t,s)
        assert all(z>=0 for z in mu+q) and sum(mu)==sum(q)==1
        tv=sum((abs(m-p) for m,p in zip(mu,q)),F(0))/2
        excess=tv-radius(t,s)
        if worst is None or excess>worst:
            worst=excess
        stats['tight_vertices']+=int(excess==0)
        stats['violating_vertices']+=int(excess>0)
    assert stats['active_seven_facet_sets']==77520
    assert stats['violating_vertices']==0,('UPPER_FAIL',worst)
    return {
      'status':'PASS',
      'unit':'R749SNM',
      'scope':'author exact rational certificate; independent review pending',
      'frozen_scientific_pin':'a72226e2430ffa4786321ac86e7f0c599d5f0389',
      'polygon_vertices':[[str(t),str(s)] for t,s in VERTICES],
      'polygon_halfspaces':['t >= 3/5','s <= 7/20','t+s <= 1','t+4s >= 8/5'],
      'theorem':'rho(t,s)=rho_cal(t,s)=(3+t-s)/8 on all real points of P',
      'calibrated_center':'(1+t*chi_3+s*chi_12)/16',
      'event_lower_certificate':'W=(h,u,v,w,z)=(0,s-1,-t,-s,-s), E={3,5,7,9,11,13,14,15}',
      'coverage':stats,
      'max_vertex_excess':str(worst)
    }

if __name__=='__main__':
    print(json.dumps(main(),indent=2,sort_keys=True))
