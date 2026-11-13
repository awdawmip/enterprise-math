#!/usr/bin/env python3
"""R749SNF exact certificate on 3/8 <= p <= 4/9."""
from fractions import Fraction as F
from itertools import combinations
from collections import Counter
import json

def chi(m, x):
    return 1 if ((m & x).bit_count() % 2) == 0 else -1

R = [tuple(chi(m,x) for m in (3,12,15,1,2,4,8)) for x in range(16)]
BASE = [(a+d,ad,p0,ap,q,dq) for a,d,ad,p0,ap,q,dq in R]

def constraints(lo, hi):
    return BASE+[(lo.denominator,0,0,0,0,0),(-hi.denominator,0,0,0,0,0)], [-1]*16+[lo.numerator,-hi.numerator]

def exact_solve(indices,m,b):
    n=6
    a=[list(m[i])+[b[i]] for i in indices]
    previous=1
    for j in range(n-1):
        k=next((i for i in range(j,n) if a[i][j]),None)
        if k is None:
            return None
        if k!=j:
            a[j],a[k]=a[k],a[j]
        pivot=a[j][j]
        for i in range(j+1,n):
            under=a[i][j]
            for k in range(j+1,n+1):
                numerator=a[i][k]*pivot-under*a[j][k]
                assert numerator%previous==0
                a[i][k]=numerator//previous
            a[i][j]=0
        previous=pivot
    if not a[n-1][n-1]:
        return None
    z=[None]*n
    for j in range(n-1,-1,-1):
        z[j]=(F(a[j][-1])-sum((a[j][k]*z[k] for k in range(j+1,n)),F(0)))/a[j][j]
    return tuple(z)

def mu(p,h,u,v,w,z):
    return tuple((1+p*(a+d)+h*ad+u*p0+v*ap+w*q+z*dq)/16
                 for a,d,ad,p0,ap,q,dq in R)

def center(tau,eta):
    return tuple((1+tau*(a+d)+eta*ad)/16 for a,d,ad,*_ in R)

def tv(a,b):
    return sum((abs(x-y) for x,y in zip(a,b)),F(0))/2

def witnesses(p):
    return {
      "AD":mu(p,F(1),F(0),F(0),F(0),F(0)),
      "alpha":mu(p,2*p-1,p-1,p-1,1-3*p,1-3*p),
      "beta":mu(p,F(0),p-1,-p,-p,-p)
    }

EVENTS={
 "AD":[1,2,4,7,8,11,13,14],
 "alpha_I":[0,4,5,6,8,9,10,12],
 "beta":[0,1,2,3,4,6,8,10,12],
 "alpha_II":[0,1,2,4,5,6,8,9,10,12]
}

def dual_check(p,tau,eta):
    q=center(tau,eta)
    ws=witnesses(p)
    assert all(min(w)>=0 and sum(w)==1 for w in ws.values())
    event_laws={"AD":"AD","alpha_I":"alpha","beta":"beta","alpha_II":"alpha"}
    L={tag:sum((q[i]-ws[event_laws[tag]][i] for i in ids),F(0))
       for tag,ids in EVENTS.items()}
    assert L["AD"]==(1-eta)/2
    assert L["alpha_I"]==(3-3*p-tau+eta)/4
    assert L["beta"]==F(5,16)+tau/8+eta/16
    assert L["alpha_II"]==(3+2*p)/8-tau/4+eta/8
    assert L["AD"]/5+4*L["alpha_I"]/15+8*L["beta"]/15==(7-3*p)/15
    assert L["AD"]/7+4*L["beta"]/7+2*L["alpha_II"]/7==(5+p)/14
    if tau==p:
        assert L["AD"]/3+2*L["alpha_I"]/3==2*(1-p)/3
        assert L["AD"]/5+4*L["alpha_II"]/5==F(2,5)
    return L

def free_center(p):
    if p<=F(23,57):
        return (6-9*p)/5,(6*p+1)/15,(7-3*p)/15
    return (3+9*p)/14,(2-p)/7,(5+p)/14

def cal_center(p):
    if p<=F(2,5):
        return p,(4*p-1)/3,2*(1-p)/3
    return p,F(1,5),F(2,5)

def certify():
    intervals=[(F(3,8),F(2,5)),(F(2,5),F(23,57)),(F(23,57),F(4,9))]
    cert=[]
    for lo,hi in intervals:
        mat,bound=constraints(lo,hi)
        counts=Counter()
        vertices=set()
        for ix in combinations(range(18),6):
            counts["six_facet_subsets"]+=1
            z=exact_solve(ix,mat,bound)
            if z is None:continue
            counts["nonsingular_bases"]+=1
            if any(sum((a*v for a,v in zip(row,z)),F(0))<lower
                   for row,lower in zip(mat,bound)):
                continue
            counts["feasible_bases"]+=1
            vertices.add(z)
        counts["distinct_vertices"]=len(vertices)
        sat_free=sat_cal=0
        for z in vertices:
            p=z[0]
            assert p in (lo,hi)
            counts["vertices_at_lower" if p==lo else "vertices_at_upper"]+=1
            law=mu(*z)
            tau,eta,rf=free_center(p)
            qf=center(tau,eta)
            tc,ec,rc=cal_center(p)
            qc=center(tc,ec)
            assert min(law)>=0 and min(qf)>=0 and min(qc)>=0
            assert sum(law)==sum(qf)==sum(qc)==1
            assert tv(law,qf)<=rf,(z,"free",rf-tv(law,qf))
            assert tv(law,qc)<=rc,(z,"cal",rc-tv(law,qc))
            sat_free+=int(tv(law,qf)==rf)
            sat_cal+=int(tv(law,qc)==rc)
        assert counts["six_facet_subsets"]==18564
        assert counts["nonsingular_bases"]==10848
        assert counts["feasible_bases"]==464
        assert counts["distinct_vertices"]==82
        assert counts["vertices_at_lower"]==counts["vertices_at_upper"]==41
        for p in (lo,hi):
            dual_check(p,F(1,5),F(2,7))
            tf,ef,rf=free_center(p)
            tc,ec,rc=cal_center(p)
            assert min(center(tf,ef))>=0 and min(center(tc,ec))>=0
        cert.append({
          "interval":[str(lo),str(hi)],
          "counts":dict(sorted(counts.items())),
          "free_tight_vertices":sat_free,
          "calibrated_tight_vertices":sat_cal
        })
    return {
      "unit":"R749SNF","status":"PASS",
      "frozen_scientific_pin":"a72226e2430ffa4786321ac86e7f0c599d5f0389",
      "free": {"3/8..23/57":"(7-3*p)/15",
               "23/57..4/9":"(5+p)/14"},
      "calibrated":{"3/8..2/5":"2*(1-p)/3",
                    "2/5..4/9":"2/5"},
      "certificates":cert
    }

if __name__=="__main__":
    print(json.dumps(certify(),indent=2,ensure_ascii=False))
