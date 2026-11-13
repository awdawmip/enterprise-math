#!/usr/bin/env python3
"""R749SNH: exact off-diagonal Walsh minimax at (m3,m12)=(1/2,1/3)."""
from fractions import Fraction as F
from itertools import combinations
import json

T,S=F(1,2),F(1,3)
R=[tuple(1 if ((m&x).bit_count()%2)==0 else -1 for m in (3,12,15,1,2,4,8)) for x in range(16)]

def solve5(indices,M,b):
    n=5
    a=[list(M[i])+[b[i]] for i in indices]
    prev=1
    for j in range(n-1):
        piv=next((i for i in range(j,n) if a[i][j]),None)
        if piv is None:return None
        if piv!=j:a[j],a[piv]=a[piv],a[j]
        pivot=a[j][j]
        for i in range(j+1,n):
            u=a[i][j]
            for k in range(j+1,n+1):
                num=a[i][k]*pivot-u*a[j][k]
                assert num%prev==0
                a[i][k]=num//prev
            a[i][j]=0
        prev=pivot
    if a[-1][-2]==0:return None
    result=[F(0)]*n
    for j in range(n-1,-1,-1):
        result[j]=(F(a[j][-1])-sum((a[j][k]*result[k] for k in range(j+1,n)),F(0)))/a[j][j]
    return tuple(result)

def law(coeff):
    h,u,v,w,z=coeff
    return tuple((1+T*a+S*d+h*ad+u*P+v*AP+w*Q+z*DQ)/16 for a,d,ad,P,AP,Q,DQ in R)

def center(tau,sigma,eta):
    return tuple((1+tau*a+sigma*d+eta*ad)/16 for a,d,ad,*_ in R)

def tv(mu,q):
    return sum((abs(x-y) for x,y in zip(mu,q)),F(0))/2

def event_diff(mu,q,inds):
    return sum((mu[i]-q[i] for i in inds),F(0))

def main():
    M=[tuple(row[2:]) for row in R]
    b=[-(6+3*a+2*d) for a,d,ad,P,AP,Q,DQ in R]
    seen=set()
    counts={'five_facet_subsets':0,'nonsingular':0,'feasible_bases':0}
    for inds in combinations(range(16),5):
        counts['five_facet_subsets']+=1
        scaled=solve5(inds,M,b)
        if scaled is None:continue
        counts['nonsingular']+=1
        if any(sum((v*w for v,w in zip(row,scaled)),F(0))<lower for row,lower in zip(M,b)):
            continue
        counts['feasible_bases']+=1
        seen.add(tuple(c/6 for c in scaled))
    counts['distinct_vertices']=len(seen)
    vertices=sorted(seen)
    qfree=center(F(7,12),F(7,24),F(1,24))
    qcal=center(T,S,F(1,30))
    rf=F(19,48);rc=F(2,5)
    assert all(x>=0 for x in qfree+qcal) and sum(qfree)==sum(qcal)==1
    exf=exc=0
    for v in vertices:
        mu=law(v)
        assert all(x>=0 for x in mu) and sum(mu)==1
        df=tv(mu,qfree);dc=tv(mu,qcal)
        assert df<=rf, ('free violation',v,df)
        assert dc<=rc, ('cal violation',v,dc)
        exf+=int(df==rf);exc+=int(dc==rc)
    wf=(F(0),-F(2,3),-F(1,2),-F(1,3),-F(1,3))
    ef=(3,5,7,9,11,13,14,15)
    assert wf in seen
    for tau,sigma,eta in ((F(0),F(0),F(0)),(F(1,3),F(1,5),F(1,7))):
        assert sum((center(tau,sigma,eta)[i] for i in ef),F(0))==F(1,2)
        assert event_diff(law(wf),center(tau,sigma,eta),ef)==rf
    w1=(-F(1,6),-F(2,3),-F(2,3),-F(1,6),-F(1,6))
    e1=(3,7,11,13,14,15)
    w2=(F(5,6),-F(1,6),-F(1,6),F(0),F(0))
    e2=(0,3,5,6,9,10,12,15)
    assert w1 in seen and w2 in seen
    for eta in (F(-1,10),F(0),F(1,30),F(1,8)):
        q=center(T,S,eta)
        assert F(4,5)*event_diff(law(w1),q,e1)+F(1,5)*event_diff(law(w2),q,e2)==rc
    return {
      'unit':'R749SNH','status':'PASS',
      'scientific_pin':'a72226e2430ffa4786321ac86e7f0c599d5f0389',
      'scope':'auxiliary Walsh observer fiber at (m3,m12)=(1/2,1/3), eight other retained moments zero',
      'counts':counts,
      'centers':{'free':{'tau':'7/12','sigma':'7/24','eta':'1/24'},
                 'calibrated':{'tau':'1/2','sigma':'1/3','eta':'1/30'}},
      'radii':{'free':'19/48','calibrated':'2/5','strict_calibration_penalty':'1/240'},
      'upper_bound_tight_vertices':{'free':exf,'calibrated':exc},
      'lower_bound':{'free':{'witness':list(map(str,wf)),'event':list(ef),'event_difference':'19/48'},
                     'calibrated':{'weights':['4/5','1/5'],
                                   'witnesses':[list(map(str,w1)),list(map(str,w2))],
                                   'events':[list(e1),list(e2)],'combined_event_difference':'2/5'}},
      'full_vertices_enumeration':'C(16,5)=4368 exact 5-facet checks; compact full-dimensional bounded 5-polytope'
    }

if __name__=='__main__':
    print(json.dumps(main(),indent=2,ensure_ascii=False,sort_keys=True))
