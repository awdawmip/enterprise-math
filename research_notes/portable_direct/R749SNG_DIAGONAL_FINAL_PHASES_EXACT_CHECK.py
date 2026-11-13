#!/usr/bin/env python3
"""Exact certificate: diagonal Walsh minimax for 4/9 <= p <= 1.
Pure Python rational arithmetic; exhaustive six-facet enumeration on three slabs.
"""
from fractions import Fraction as F
from itertools import combinations
from collections import Counter
import json

def chi(m,x):
    return 1 if ((m&x).bit_count()%2)==0 else -1

R=[tuple(chi(m,x) for m in (3,12,15,1,2,4,8)) for x in range(16)]
BASE=[(a+d,ad,P,AP,Q,DQ) for a,d,ad,P,AP,Q,DQ in R]

def constraints(lo,hi):
    return BASE+[(lo.denominator,0,0,0,0,0),(-hi.denominator,0,0,0,0,0)],[-1]*16+[lo.numerator,-hi.numerator]

def exact_solve(indices,m,b):
    n=6
    a=[list(m[i])+[b[i]] for i in indices]
    previous=1
    for j in range(n-1):
        k=next((i for i in range(j,n) if a[i][j]),None)
        if k is None:return None
        if k!=j:a[j],a[k]=a[k],a[j]
        pivot=a[j][j]
        for i in range(j+1,n):
            under=a[i][j]
            for k in range(j+1,n+1):
                numerator=a[i][k]*pivot-under*a[j][k]
                assert numerator%previous==0
                a[i][k]=numerator//previous
            a[i][j]=0
        previous=pivot
    if not a[n-1][n-1]:return None
    z=[None]*n
    for j in range(n-1,-1,-1):
        z[j]=(F(a[j][-1])-sum((a[j][k]*z[k] for k in range(j+1,n)),F(0)))/a[j][j]
    return tuple(z)

def mu(p,h,u,v,w,z):
    return tuple((1+p*(a+d)+h*ad+u*P+v*AP+w*Q+z*DQ)/16
                 for a,d,ad,P,AP,Q,DQ in R)

def center(tau,eta):
    return tuple((1+tau*(a+d)+eta*ad)/16 for a,d,ad,*_ in R)

def tv(a,b):
    return sum((abs(x-y) for x,y in zip(a,b)),F(0))/2

def free_center(p):
    if p<=F(1,2):return (18*p-3)/10,2*(1-p)/5,(3+2*p)/10
    return (4*p+1)/5,(8*p-3)/5,4*(1-p)/5

def cal_center(p):
    if p<=F(7,15):return p,F(1,5),F(2,5)
    if p<=F(1,2):return p,(5-6*p)/11,3*(1+p)/11
    return p,(18*p-7)/11,9*(1-p)/11

def witnesses(p):
    return {
        "AD":mu(p,F(1),F(0),F(0),F(0),F(0)),
        "alpha":mu(p,2*p-1,p-1,p-1,1-3*p,1-3*p),
        "beta":mu(p,F(0),p-1,-p,-p,-p),
        "gamma":mu(p,2*p-1,p-1,p-1,p-1,p-1),
    }

EVENTS={
   "AD":("AD",(1,2,4,7,8,11,13,14)),
   "alpha_II":("alpha",(0,1,2,4,5,6,8,9,10,12)),
   "alpha_III":("alpha",(0,1,2,3,4,5,6,8,9,10,12)),
   "beta":("beta",(0,1,2,3,4,6,8,10,12)),
   "gamma_I":("gamma",(0,1,2,3,4,8,12)),
   "gamma_II":("gamma",(0,1,2,3,4,5,6,8,9,10,12))
}

def dual_check(p):
    ws=witnesses(p)
    active=("AD","alpha","beta") if p<=F(1,2) else ("AD","gamma")
    for name in active:
        assert min(ws[name])>=0 and sum(ws[name])==1,(p,name)
    tf,ef,rf=free_center(p)
    tc,ec,rc=cal_center(p)
    assert min(center(tf,ef))>=0 and min(center(tc,ec))>=0
    assert sum(center(tf,ef))==sum(center(tc,ec))==1
    def L(tag,tau,eta):
        typ,event=EVENTS[tag]
        return sum((center(tau,eta)[x]-ws[typ][x] for x in event),F(0))
    if p<=F(1,2):
        assert (2*L("alpha_III",tf,ef)+2*L("beta",tf,ef)+L("AD",tf,ef))/5==rf
        if p<=F(7,15):
            assert (4*L("alpha_II",tc,ec)+L("AD",tc,ec))/5==rc
        else:
            assert (8*L("alpha_III",tc,ec)+3*L("AD",tc,ec))/11==rc
    else:
        assert (L("gamma_I",tf,ef)+3*L("gamma_II",tf,ef)+L("AD",tf,ef))/5==rf
        assert (8*L("gamma_II",tc,ec)+3*L("AD",tc,ec))/11==rc
    return True

def check_interval(lo,hi):
    m,b=constraints(lo,hi)
    counts=Counter();verts=set()
    for inds in combinations(range(18),6):
        counts["six_facet_subsets"]+=1
        z=exact_solve(inds,m,b)
        if z is None:continue
        counts["nonsingular_bases"]+=1
        if any(sum((i*j for i,j in zip(row,z)),F(0))<lower for row,lower in zip(m,b)):
            continue
        counts["feasible_bases"]+=1
        verts.add(z)
    counts["distinct_vertices"]=len(verts)
    for p in (lo,hi):dual_check(p)
    free_tight=cal_tight=0
    for z in verts:
        p=z[0]
        counts["vertices_at_lower" if p==lo else "vertices_at_upper" if p==hi else "vertices_interior"]+=1
        law=mu(*z)
        tf,ef,rf=free_center(p)
        tc,ec,rc=cal_center(p)
        assert min(law)>=0 and sum(law)==1
        dqf=tv(law,center(tf,ef));dqc=tv(law,center(tc,ec))
        assert dqf<=rf,(lo,hi,z,"free",dqf-rf)
        assert dqc<=rc,(lo,hi,z,"cal",dqc-rc)
        free_tight+=int(dqf==rf);cal_tight+=int(dqc==rc)
    return {"interval":[str(lo),str(hi)],"counts":dict(sorted(counts.items())),
            "free_tight_vertices":free_tight,"cal_tight_vertices":cal_tight}

def certify():
    spans=[(F(4,9),F(7,15)),(F(7,15),F(1,2)),(F(1,2),F(1))]
    return {"unit":"R749SNG","status":"PASS",
      "frozen_scientific_pin":"a72226e2430ffa4786321ac86e7f0c599d5f0389",
      "domain":"4/9 <= p <= 1",
      "free":{"4/9..1/2":"(3+2*p)/10","1/2..1":"4*(1-p)/5"},
      "calibrated":{"4/9..7/15":"2/5","7/15..1/2":"3*(1+p)/11","1/2..1":"9*(1-p)/11"},
      "certificates":[check_interval(*v) for v in spans]}
if __name__=='__main__':print(json.dumps(certify(),indent=2,ensure_ascii=False))
