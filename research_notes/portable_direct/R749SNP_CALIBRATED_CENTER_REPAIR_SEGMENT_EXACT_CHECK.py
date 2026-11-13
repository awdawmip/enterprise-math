#!/usr/bin/env python3
"""R749SNP: exact calibrated affine-center repair over an entire real segment."""
from fractions import Fraction as F
from itertools import combinations
from math import comb
import json

MASKS=(3,12,15,1,2,4,8)
ROWS=[tuple(1 if (m&x).bit_count()%2==0 else -1 for m in MASKS) for x in range(16)]
EVENT=(3,5,7,9,11,13,14,15)
T=F(7,10)
PIN='a72226e2430ffa4786321ac86e7f0c599d5f0389'

def law(s,h,u,v,w,z):
    return tuple((1+sum((a*x for a,x in zip(row,(T,s,h,u,v,w,z))),F(0)))/16 for row in ROWS)

def radius(s):
    return (3+T-s)/8

def eta(s):
    if F(1,10)<=s<=F(3,20): return -F(3,2)*(s-F(1,10))
    if F(3,20)<=s<=F(1,5): return F(3,2)*(s-F(1,5))
    raise ValueError('parameter out of certified segment')

def solve(M,b,inds,n=6):
    a=[list(M[i])+[b[i]] for i in inds]
    last=1
    for j in range(n-1):
        pivot=next((i for i in range(j,n) if a[i][j]),None)
        if pivot is None:return None
        if pivot!=j: a[j],a[pivot]=a[pivot],a[j]
        p=a[j][j]
        for i in range(j+1,n):
            c=a[i][j]
            for k in range(j+1,n+1):
                v=a[i][k]*p-c*a[j][k]
                assert v%last==0
                a[i][k]=v//last
            a[i][j]=0
        last=p
    if not a[-1][-2]:return None
    v=[F(0)]*n
    for j in range(n-1,-1,-1):
        v[j]=(F(a[j][-1])-sum((a[j][k]*v[k] for k in range(j+1,n)),F(0)))/a[j][j]
    return tuple(v)

def interval(lo,hi):
    # Scale y=20*(s,h,u,v,w,z) to make all halfspaces integral.
    L=20
    M=[r[1:] for r in ROWS]
    b=[-int(L*(1+T*r[0])) for r in ROWS]
    M.extend(((1,0,0,0,0,0),(-1,0,0,0,0,0)))
    b.extend((int(L*lo),-int(L*hi)))
    seen=set()
    stats={'active_bases':0,'nonsingular_bases':0,'feasible_bases':0,
           'unique_vertices':0,'tight_vertices':0,'violating_vertices':0}
    for ids in combinations(range(18),6):
        stats['active_bases']+=1
        sol=solve(M,b,ids)
        if sol is None:continue
        stats['nonsingular_bases']+=1
        if any(sum((a*x for a,x in zip(row,sol)),F(0))<rhs for row,rhs in zip(M,b)):
            continue
        stats['feasible_bases']+=1
        seen.add(tuple(x/L for x in sol))
    assert stats['active_bases']==comb(18,6)==18564
    stats['unique_vertices']=len(seen)
    max_excess=F(-100)
    for s,h,u,v,w,z in seen:
        mu=law(s,h,u,v,w,z)
        center=law(s,eta(s),0,0,0,0)
        assert min(mu)>=0 and min(center)>=0
        assert sum(mu)==sum(center)==1
        tv=sum((abs(x-y) for x,y in zip(mu,center)),F(0))/2
        excess=tv-radius(s)
        max_excess=max(max_excess,excess)
        stats['tight_vertices']+=int(excess==0)
        stats['violating_vertices']+=int(excess>0)
    stats['max_excess']=str(max_excess)
    assert stats['violating_vertices']==0
    for s in (lo,hi):
        w=law(s,0,s-1,-T,-s,-s)
        center=law(s,eta(s),0,0,0,0)
        assert min(w)>=0 and min(center)>=0
        assert sum(w)==sum(center)==1
        assert all(sum(ROWS[x][j] for x in EVENT)==0 for j in range(3))
        assert sum((w[x] for x in EVENT),F(0))-F(1,2)==radius(s)
    return stats

def main():
    left=interval(F(1,10),F(3,20))
    right=interval(F(3,20),F(1,5))
    assert eta(F(1,10))==eta(F(1,5))==0
    assert eta(F(3,20))==-F(3,40)
    bad=law(F(3,20),-F(3,20),F(17,20),F(17,20),0,0)
    plain=law(F(3,20),0,0,0,0,0)
    repaired=law(F(3,20),eta(F(3,20)),0,0,0,0)
    assert sum((abs(x-y) for x,y in zip(bad,plain)),F(0))/2==F(37,80)
    assert sum((abs(x-y) for x,y in zip(bad,repaired)),F(0))/2<=radius(F(3,20))
    return {
        'unit':'R749SNP','status':'PASS',
        'scope':'author exact certificate, all real s in [1/10,1/5] at t=7/10; independent review pending',
        'frozen_scientific_pin':PIN,
        'theorem':'rho(7/10,s)=rho_cal(7/10,s)=37/80-s/8',
        'center':'q(x)=[1+(7/10)A+sD+eta(s)AD]/16',
        'eta_left':'-3/2*(s-1/10) for s in [1/10,3/20]',
        'eta_right':'3/2*(s-1/5) for s in [3/20,1/5]',
        'left_certificate':left,'right_certificate':right,
        'witness':'W=(h,u,v,w,z)=(0,s-1,-7/10,-s,-s); event E={3,5,7,9,11,13,14,15}',
        'center_repair_at_midpoint':{'s':'3/20','eta':'-3/40','radius':'71/160',
          'old_center_specific_witness_tv':'37/80','exact_lower_bound':'71/160'}
    }

if __name__=='__main__':
    print(json.dumps(main(),indent=2,sort_keys=True))
