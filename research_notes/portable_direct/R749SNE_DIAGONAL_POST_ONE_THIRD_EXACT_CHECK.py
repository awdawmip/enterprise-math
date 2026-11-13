#!/usr/bin/env python3
"""R749SNE exact certificate on 1/3 <= p <= 3/8."""
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
      'AD':mu(p,F(1),F(0),F(0),F(0),F(0)),
      'N':mu(p,2*p-1,1-3*p,1-3*p,p-1,p-1),
      'C':mu(p,(1-2*p)/3,-(1+p)/3,-(1+p)/3,-(1+p)/3,-(1+p)/3)
    }

EVENTS={
 'AD':[1,2,4,7,8,11,13,14],
 'N':[0,1,2,3,5,6,9,10],
 'C':[0,1,2,3,4,8,12]
}

def dual_check(p,tau,eta):
    q=center(tau,eta); ws=witnesses(p)
    assert all(min(w)>=0 and sum(w)==1 for w in ws.values())
    lower={name:sum((q[i]-ws[name][i] for i in event),F(0))
           for name,event in EVENTS.items()}
    assert lower['AD']==(1-eta)/2
    assert lower['N']==(3-3*p-tau+eta)/4
    assert lower['C']==(13-8*p+18*tau-3*eta)/48
    assert lower['AD']/5+12*lower['N']/25+8*lower['C']/25==(41-31*p)/75
    return lower

def certify():
    lo,hi=F(1,3),F(3,8)
    mat,bound=constraints(lo,hi)
    counts=Counter()
    vertices=set()
    for ix in combinations(range(18),6):
        counts['six_facet_subsets']+=1
        z=exact_solve(ix,mat,bound)
        if z is None:
            continue
        counts['nonsingular_bases']+=1
        if any(sum((a*v for a,v in zip(row,z)),F(0))<lower
               for row,lower in zip(mat,bound)):
            continue
        counts['feasible_bases']+=1
        vertices.add(z)
    counts['distinct_vertices']=len(vertices)
    sf,sc=Counter(),Counter()
    for z in vertices:
        p=z[0]
        assert p in (lo,hi)
        counts['vertices_at_lower' if p==lo else 'vertices_at_upper']+=1
        law=mu(*z)
        tau,eta=(18-13*p)/25,(62*p-7)/75
        qc=center(p,(4*p-1)/3)
        qf=center(tau,eta)
        assert min(law)>=0 and min(qf)>=0 and min(qc)>=0
        assert sum(law)==sum(qf)==sum(qc)==1
        free=(41-31*p)/75-tv(law,qf)
        cal=2*(1-p)/3-tv(law,qc)
        assert free>=0 and cal>=0,(z,free,cal)
        sf[str(free)]+=1
        sc[str(cal)]+=1
    assert counts['six_facet_subsets']==18564
    assert counts['distinct_vertices']==78
    assert counts['vertices_at_lower']==37 and counts['vertices_at_upper']==41
    for p in (lo,hi):
        dual_check(p,F(1,7),F(2,9))
        ws=witnesses(p)
        h_event=[i for i,(a,d,ad,P,AP,Q,DQ) in enumerate(R)
                 if (d==1 and Q==-1) or (a==1 and d==-1)]
        assert sum(ws['N'][i] for i in h_event)==(5-3*p)/4
        assert sum(center(p,(4*p-1)/3)[i] for i in h_event)==(2+p-(4*p-1)/3)/4
    return {
       'unit':'R749SNE','status':'PASS',
       'frozen_scientific_pin':'a72226e2430ffa4786321ac86e7f0c599d5f0389',
       'interval':['1/3','3/8'],
       'unrestricted_radius':'(41-31*p)/75',
       'calibrated_radius':'2*(1-p)/3',
       'counts':dict(sorted(counts.items())),
       'free_slack_distribution':dict(sorted(sf.items())),
       'calibrated_slack_distribution':dict(sorted(sc.items()))
    }

if __name__=='__main__':
    print(json.dumps(certify(),ensure_ascii=False,indent=2))
