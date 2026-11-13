#!/usr/bin/env python3
"""Exact all-real verification of zero calibration on t+s=1, 3/5<=t<=1."""
from fractions import Fraction as F
from itertools import combinations
from math import comb
import json

R=[tuple(1 if (m&x).bit_count()%2==0 else -1 for m in (3,12,15,1,2,4,8)) for x in range(16)]
E=(3,5,7,9,11,13,14,15)

def source(t,h,u,v,w,z):
    s=1-t
    return tuple((1+t*a+s*d+h*ad+u*p+v*ap+w*q+z*dq)/16 for a,d,ad,p,ap,q,dq in R)

def center(t):
    return tuple((1+t*a+(1-t)*d)/16 for a,d,*_ in R)

def radius(t):
    return (1+t)/4

def exact_solve(indices,M,b,n=6):
    a=[list(M[i])+[b[i]] for i in indices]
    prev=1
    for j in range(n-1):
        piv=next((i for i in range(j,n) if a[i][j]),None)
        if piv is None:
            return None
        if piv!=j:
            a[j],a[piv]=a[piv],a[j]
        p=a[j][j]
        for i in range(j+1,n):
            v=a[i][j]
            for k in range(j+1,n+1):
                term=a[i][k]*p-v*a[j][k]
                assert term%prev==0
                a[i][k]=term//prev
            a[i][j]=0
        prev=p
    if a[-1][-2]==0:
        return None
    x=[F(0)]*n
    for j in range(n-1,-1,-1):
        x[j]=(F(a[j][-1])-sum((a[j][k]*x[k] for k in range(j+1,n)),F(0)))/a[j][j]
    return tuple(x)

def main():
    L=5
    M=[(a-d,ad,p,ap,q,dq) for a,d,ad,p,ap,q,dq in R]
    b=[-L*(1+d) for a,d,ad,p,ap,q,dq in R]
    M.extend(((1,0,0,0,0,0),(-1,0,0,0,0,0)))
    b.extend((3,-5))
    assert len(M)==18 and comb(18,6)==18564
    count={'all_bases':0,'nonsingular':0,'feasible_bases':0,
           'distinct_vertices':0,'tight':0,'violations':0}
    seen=set()
    for ids in combinations(range(18),6):
        count['all_bases']+=1
        sol=exact_solve(ids,M,b)
        if sol is None:continue
        count['nonsingular']+=1
        if any(sum((a*z for a,z in zip(row,sol)),F(0))<rhs for row,rhs in zip(M,b)):
            continue
        count['feasible_bases']+=1
        seen.add(tuple(z/L for z in sol))
    assert seen
    count['distinct_vertices']=len(seen)
    for params in seen:
        t=params[0]
        mu=source(*params)
        qc=center(t)
        assert all(v>=0 for v in mu+qc) and sum(mu)==sum(qc)==1
        tv=sum((abs(u-v) for u,v in zip(mu,qc)),F(0))/2
        count['tight']+=int(tv==radius(t))
        count['violations']+=int(tv>radius(t))
    assert count['all_bases']==18564 and count['violations']==0
    assert all(sum(R[x][j] for x in E)==0 for j in range(3))
    for t in (F(3,5),F(1)):
        s=1-t
        witness=source(t,F(0),s-1,-t,-s,-s)
        assert all(v>=0 for v in witness) and sum(witness)==1
        assert sum((witness[x] for x in E),F(0))-F(1,2)==radius(t)
    return {
      'unit':'R749SNN',
      'status':'PASS',
      'domain':'all real t in [3/5,1] with s=1-t',
      'theorem':'rho(t,1-t)=rho_cal(t,1-t)=(1+t)/4',
      'calibrated_center':'(1+t*chi_3+(1-t)*chi_12)/16',
      'frozen_scientific_pin':'a72226e2430ffa4786321ac86e7f0c599d5f0389',
      'complete_vertex_certificate':count,
      'lower_witness':'W=(0,s-1,-t,-s,-s) on event E={3,5,7,9,11,13,14,15}'
    }

if __name__=='__main__':
    print(json.dumps(main(),indent=2,sort_keys=True))
