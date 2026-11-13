#!/usr/bin/env python3
"""R749SNL: all-real two-parameter Walsh minimax rectangle, exact Fraction certificate."""
from fractions import Fraction as F
from itertools import combinations
from math import lcm
import json

TLO,THI=F(3,5),F(13,20)
SLO,SHI=F(1,4),F(7,20)
R=[tuple(1 if ((m&x).bit_count()%2)==0 else -1 for m in (3,12,15,1,2,4,8)) for x in range(16)]
E=(3,5,7,9,11,13,14,15)

def law(t,s,h,u,v,w,z):
    return tuple((1+t*a+s*d+h*ad+u*p+v*ap+w*q+z*dq)/16 for a,d,ad,p,ap,q,dq in R)

def center(t,s):
    return tuple((1+t*a+s*d)/16 for a,d,*_ in R)

def radius(t,s):return (3+t-s)/8

def exact_solve(indices,M,b,n=7):
    a=[list(M[i])+[b[i]] for i in indices]
    prev=1
    for j in range(n-1):
        piv=next((i for i in range(j,n) if a[i][j]),None)
        if piv is None:return None
        if piv!=j:a[j],a[piv]=a[piv],a[j]
        p=a[j][j]
        for i in range(j+1,n):
            q=a[i][j]
            for k in range(j+1,n+1):
                num=a[i][k]*p-q*a[j][k]
                assert num%prev==0
                a[i][k]=num//prev
            a[i][j]=0
        prev=p
    if a[-1][-2]==0:return None
    v=[F(0)]*n
    for j in range(n-1,-1,-1):
        v[j]=(F(a[j][-1])-sum((a[j][k]*v[k] for k in range(j+1,n)),F(0)))/a[j][j]
    return tuple(v)

def enumerate_joint_vertices():
    L=lcm(TLO.denominator,THI.denominator,SLO.denominator,SHI.denominator)
    M=list(R)
    b=[-L]*16
    M += [(1,0,0,0,0,0,0),(-1,0,0,0,0,0,0),
          (0,1,0,0,0,0,0),(0,-1,0,0,0,0,0)]
    b += [int(L*TLO),-int(L*THI),int(L*SLO),-int(L*SHI)]
    count=dict(facet_subsets=0,nonsingular=0,feasible_bases=0)
    seen=set()
    for inds in combinations(range(20),7):
        count['facet_subsets']+=1
        v=exact_solve(inds,M,b)
        if v is None:continue
        count['nonsingular']+=1
        if any(sum((x*y for x,y in zip(row,v)),F(0))<lim for row,lim in zip(M,b)):
            continue
        count['feasible_bases']+=1
        seen.add(tuple(x/L for x in v))
    assert seen
    count['distinct_vertices']=len(seen)
    count['tight_vertices']=0
    for par in seen:
        t,s=par[:2]
        assert TLO<=t<=THI and SLO<=s<=SHI
        mu=law(*par)
        q=center(t,s)
        assert all(x>=0 for x in mu+q) and sum(mu)==sum(q)==1
        dist=sum((abs(x-y) for x,y in zip(mu,q)),F(0))/2
        assert dist<=radius(t,s),('UPPER_BOUND_FAIL',par,dist,radius(t,s))
        count['tight_vertices']+=int(dist==radius(t,s))
    return count

def main():
    counts=enumerate_joint_vertices()
    assert len(E)==8
    assert all(sum(R[x][i] for x in E)==0 for i in range(3))
    for t in (TLO,THI):
        for s in (SLO,SHI):
            w=law(t,s,F(0),s-1,-t,-s,-s)
            q=center(t,s)
            assert all(a>=0 for a in w+q)
            assert sum(w)==sum(q)==1
            assert sum((w[x] for x in E),F(0))-F(1,2)==radius(t,s)
    return {
        'unit':'R749SNL','status':'PASS',
        'frozen_scientific_pin':'a72226e2430ffa4786321ac86e7f0c599d5f0389',
        'domain':'all real (t,s) in [3/5,13/20] x [1/4,7/20]',
        'formula':'rho(t,s)=rho_cal(t,s)=(3+t-s)/8',
        'calibrated_optimal_decoder':'q(x)=(1+t*chi_3(x)+s*chi_12(x))/16',
        'dual_witness':'(h,u,v,w,z)=(0,s-1,-t,-s,-s), E=(3,5,7,9,11,13,14,15)',
        'joint_polytope':counts,
        'coverage':'20 facets, all C(20,7) active sets; exact Bareiss/Fraction; vertex convexity for all real parameters',
    }

if __name__=='__main__':
    print(json.dumps(main(),sort_keys=True,indent=2))
