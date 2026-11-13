#!/usr/bin/env python3
"""R749SND exact proof certificate: every vertex of two rational six-polytopes."""
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
      'E':mu(p,-p,F(0),F(0),-2*p,p-1),
      'C':mu(p,(1-2*p)/3,-(1+p)/3,-(1+p)/3,-(1+p)/3,-(1+p)/3)
    }

EVENTS={
 'AD':[1,2,4,7,8,11,13,14],
 'E':[0,1,2,3,5,6,9,10],
 'C':[0,1,2,3,4,8,12]
}

def dual_check(p,tau,eta):
    q=center(tau,eta); ws=witnesses(p)
    assert all(min(w)>=0 and sum(w)==1 for w in ws.values())
    lower={name:sum((q[i]-ws[name][i] for i in event),F(0))
           for name,event in EVENTS.items()}
    assert lower['AD']==(1-eta)/2
    assert lower['E']==(1+3*p-tau+eta)/4
    assert lower['C']==(13-8*p+18*tau-3*eta)/48
    assert lower['AD']/5+12*lower['E']/25+8*lower['C']/25==23*(1+p)/75
    return lower

def certify_interval(lo,hi,phase):
    mat,bound=constraints(lo,hi)
    counts=Counter()
    vertices=set()
    for indices in combinations(range(18),6):
        counts['six_facet_subsets']+=1
        z=exact_solve(indices,mat,bound)
        if z is None:
            continue
        counts['nonsingular_bases']+=1
        if any(sum((a*v for a,v in zip(row,z)),F(0))<lower
               for row,lower in zip(mat,bound)):
            continue
        counts['feasible_bases']+=1
        vertices.add(z)
    counts['distinct_vertices']=len(vertices)
    free_slack=Counter(); cal_slack=Counter()
    for z in vertices:
        p=z[0]
        assert p in (lo,hi)
        counts['vertices_at_lower' if p==lo else 'vertices_at_upper']+=1
        law=mu(*z)
        if phase==1:
            tau,eta,radius=3*p-F(2,5),F(1,5),F(2,5)
        else:
            tau,eta,radius=(4+29*p)/25,(29-46*p)/75,23*(1+p)/75
        pred=center(tau,eta)
        calibrated=center(p,(1-2*p)/3)
        assert min(law)>=0 and sum(law)==1
        assert min(pred)>=0 and sum(pred)==1
        assert min(calibrated)>=0 and sum(calibrated)==1
        sf=radius-tv(law,pred)
        sc=(1+p)/3-tv(law,calibrated)
        assert sf>=0 and sc>=0, (z,sf,sc)
        free_slack[str(sf)]+=1
        cal_slack[str(sc)]+=1
    assert counts['six_facet_subsets']==18564
    for p in (lo,hi):
        ws=witnesses(p)
        assert all(min(w)>=0 and sum(w)==1 for w in ws.values())
        # The support event from R749SNC gives the (3+eta)/8 lower bound.
        old_event=[i for i,(a,d,ad,P,AP,Q,DQ) in enumerate(R)
                   if DQ==-1 or (a==1 and d==-1)]
        assert sum(ws['E'][i] for i in old_event)==1
        assert sum(center(F(0),F(1,5))[i] for i in old_event)==F(3,5)
        # Calibrated H event gives the (1+2p+eta)/4 lower bound.
        h_event=[i for i,(a,d,ad,P,AP,Q,DQ) in enumerate(R)
                 if (d==1 and Q==-1) or (a==1 and d==-1)]
        assert sum(ws['E'][i] for i in h_event)==3*(1+p)/4
        if phase==2:
            dual_check(p,F(1,7),F(2,9))
    return {
      'interval':[str(lo),str(hi)], 'phase':phase,
      'free_radius':'2/5' if phase==1 else '23*(1+p)/75',
      'calibrated_radius':'(1+p)/3',
      'center_tau':'3*p-2/5' if phase==1 else '(4+29*p)/25',
      'center_eta':'1/5' if phase==1 else '(29-46*p)/75',
      'counts':dict(sorted(counts.items())),
      'free_slack_distribution':dict(sorted(free_slack.items())),
      'calibrated_slack_distribution':dict(sorted(cal_slack.items()))
    }

def certify():
    first=certify_interval(F(3,10),F(7,23),1)
    second=certify_interval(F(7,23),F(1,3),2)
    assert 23*(1+F(7,23))/75==F(2,5)
    assert 23*(1+F(1,3))/75==F(92,225)
    assert first['counts']['distinct_vertices']==106
    assert second['counts']['distinct_vertices']==90
    return {
      'unit':'R749SND', 'status':'PASS',
      'frozen_scientific_pin':'a72226e2430ffa4786321ac86e7f0c599d5f0389',
      'arithmetic':'integer Bareiss and Fraction, exhaustive vertex enumeration',
      'new_transition':'7/23', 'intervals':[first,second]
    }

if __name__=='__main__':
    print(json.dumps(certify(),ensure_ascii=False,indent=2))
