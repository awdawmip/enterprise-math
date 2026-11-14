#!/usr/bin/env python3
"""R749SOJ exact 7D Walsh joint-polytope certificate; stdlib only.
Science pin a72226e2430ffa4786321ac86e7f0c599d5f0389.
"""
from itertools import combinations
from fractions import Fraction as Q
from math import comb
import json
M=(3,12,15,1,2,4,8)
W=tuple(tuple(1 if (k&m).bit_count()%2==0 else -1 for m in M) for k in range(16))
A=W+((20,0,0,0,0,0,0),(-25,0,0,0,0,0,0),(0,25,0,0,0,0,0),(0,-25,0,0,0,0,0),(-3,2,0,0,0,0,0))
B=(-1,)*16+(13,-17,12,-13,-1)
P=((Q(13,20),Q(12,25)),(Q(49,75),Q(12,25)),(Q(17,25),Q(13,25)),(Q(13,20),Q(13,25)))
EA=(1,2,4,7,8,11,13,14);EG=(0,1,2,4,5,6,8,9,10,12)
def solve(ids):
    n=7;a=[list(A[i])+[B[i]] for i in ids];d=1
    for j in range(n-1):
        p=next((i for i in range(j,n) if a[i][j]),None)
        if p is None:return None
        if p!=j:a[p],a[j]=a[j],a[p]
        for i in range(j+1,n):
            z=a[i][j]
            for k in range(j+1,n+1):
                numerator=a[i][k]*a[j][j]-z*a[j][k]
                assert numerator%d==0
                a[i][k]=numerator//d
            a[i][j]=0
        d=a[j][j]
    if not a[-1][-2]:return None
    x=[Q(0)]*n
    for i in range(n-1,-1,-1):
        x[i]=(Q(a[i][n])-sum((a[i][k]*x[k] for k in range(i+1,n)),Q(0)))/a[i][i]
    return tuple(x)
def law(t,s,h,u=0,v=0,w=0,z=0):
    c=(t,s,h,u,v,w,z)
    return tuple((1+sum((a*b for a,b in zip(row,c)),Q(0)))/16 for row in W)
def tv(p,q):return sum((abs(x-y) for x,y in zip(p,q)),Q(0))/2
def run():
    v=set(); nonsing=feasible=0
    for ids in combinations(range(21),7):
        x=solve(ids)
        if x is None:continue
        nonsing+=1
        if any(sum((a*b for a,b in zip(row,x)),Q(0))<b for row,b in zip(A,B)):continue
        feasible+=1;v.add(x)
    assert len(v)==80
    fmax=cmax=Q(-100); ft=ct=0
    for t,s,h,u,v0,w,z in v:
        source=law(t,s,h,u,v0,w,z)
        free=law(Q(1),2*t-1,2*t-1)
        cal=law(t,s,(9*s-t-3)/5)
        assert all(sum(p)==1 and min(p)>=0 for p in (source,free,cal))
        f=tv(free,source)-(3-t-2*s)/4
        c=tv(cal,source)-(4-2*t-2*s)/5
        fmax=max(fmax,f);cmax=max(cmax,c)
        ft+=int(f==0);ct+=int(c==0)
    assert fmax==cmax==0 and ft==16 and ct==32
    for t,s in P:
        x=law(t,s,1+s-t,s-t,s-t)
        y=law(t,s,t+s-1,s-1,s-1,t-1,t-1)
        z=law(t,s,t+s-1,1-s,1-s,1-t,1-t)
        assert all(min(p)>=0 and sum(p)==1 for p in (x,y,z))
        assert tv(y,z)==(3-t-2*s)/2
        for h in (Q(-1,5),Q(0),Q(1,5)):
            q=law(t,s,h)
            la=sum((q[i]-x[i] for i in EA),Q(0))
            lg=sum((q[i]-y[i] for i in EG),Q(0))
            assert (la+4*lg)/5==(4-2*t-2*s)/5
    assert sum((P[i][0]*P[(i+1)%4][1]-P[(i+1)%4][0]*P[i][1] for i in range(4)),Q(0))/2==Q(1,1500)
    return dict(unit='R749SOJ',status='PASS',scientific_pin='a72226e2430ffa4786321ac86e7f0c599d5f0389',
      scope='16-state auxiliary Walsh, all real (t,s) in [13/20,17/25] x [12/25,13/25]',
      rho='(3-t-2s)/4',rho_cal='max((3-t-2s)/4,(4-2t-2s)/5)',
      gap='max(0,1-3t+2s)/20',phase_boundary='3t-2s=1',
      positive_polygon=[list(map(str,p)) for p in P],positive_area='1/1500',
      zero_area='1/1875',active_bases=comb(21,7),nonsingular_bases=nonsing,
      feasible_bases=feasible,distinct_vertices=len(v),free_tight=ft,cal_tight=ct,
      max_free_excess=str(fmax),max_cal_excess=str(cmax),violations=0,
      proof_status='AUTHOR_EXACT_NOT_REVIEWED',native_correspondence='OPEN')
if __name__=='__main__':print(json.dumps(run(),ensure_ascii=False,indent=2,sort_keys=True))
