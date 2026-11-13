#!/usr/bin/env python3
"""R749SNJ: exact real-parameter segment t=1/2, 1/4<=s<=1/3."""
from fractions import Fraction as F
from itertools import combinations
from math import lcm
import json

T=F(1,2)
R=[tuple(1 if ((m&x).bit_count()%2)==0 else -1 for m in (3,12,15,1,2,4,8)) for x in range(16)]

def solve6(indices,M,b):
    n=6
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

def law(s,h,u,v,w,z):
    return tuple((1+T*a+s*d+h*ad+u*P+v*AP+w*Q+z*DQ)/16 for a,d,ad,P,AP,Q,DQ in R)

def center(tau,sigma,eta):
    return tuple((1+tau*a+sigma*d+eta*ad)/16 for a,d,ad,*_ in R)

def tv(mu,q):
    return sum((abs(a-b) for a,b in zip(mu,q)),F(0))/2

def qfree(s):
    return center(F(5,2)*s-F(1,4),F(3,8)-s/F(4),F(5,4)*s-F(3,8))

def qcal1(s):
    return center(T,s,F(5,3)*s-F(1,2))

def qcal2(s):
    return center(T,s,s-F(3,10))

def rf(s):
    return F(7,16)-s/F(8)

def rc1(s):
    return F(1,2)-s/F(3)

def rc2(s):
    return F(2,5)

def check_segment(lo,hi,decoder,radius):
    L=lcm(2,lo.denominator,hi.denominator)
    M=[(d,ad,p,ap,q,dq) for a,d,ad,p,ap,q,dq in R]
    b=[-L-int(L*T)*a for a,d,ad,p,ap,q,dq in R]
    M.extend([(1,0,0,0,0,0),(-1,0,0,0,0,0)])
    b.extend([int(L*lo),-int(L*hi)])
    counts=dict(facet_subsets=0,nonsingular=0,feasible_bases=0)
    seen=set()
    for inds in combinations(range(18),6):
        counts['facet_subsets']+=1
        v=solve6(inds,M,b)
        if v is None:continue
        counts['nonsingular']+=1
        if any(sum((x*y for x,y in zip(row,v)),F(0))<lim for row,lim in zip(M,b)):
            continue
        counts['feasible_bases']+=1
        seen.add(tuple(x/L for x in v))
    counts['distinct_vertices']=len(seen)
    tight=0
    for par in sorted(seen):
        s=par[0]
        mu=law(*par)
        q=decoder(s)
        r=radius(s)
        assert lo<=s<=hi
        assert all(x>=0 for x in mu+q)
        assert sum(mu)==sum(q)==1
        d=tv(mu,q)
        assert d<=r,('UNIVERSAL_UPPER_BOUND_FAILED',par,str(d),str(r))
        tight+=int(d==r)
    counts['tight_vertices']=tight
    return counts

def main():
    free=check_segment(F(1,4),F(1,3),qfree,rf)
    cal1=check_segment(F(1,4),F(3,10),qcal1,rc1)
    cal2=check_segment(F(3,10),F(1,3),qcal2,rc2)
    Ef=(3,5,7,9,11,13,14,15)
    E1=(0,3,5,6,9,10,12,15)
    E2=(1,2,3,7,11,13,14,15)
    E3=(3,7,11,13,14,15)
    E4=E1
    for s in (F(1,4),F(4,15),F(3,10),F(5,16),F(1,3)):
        wf=law(s,F(0),s-1,-F(1,2),-s,-s)
        assert all(x>=0 for x in wf)
        assert sum((wf[i]-qfree(s)[i] for i in Ef),F(0))==rf(s)
        if s<=F(3,10):
            w1=law(s,s+F(1,2),s-F(1,2),s-F(1,2),F(0),F(0))
            w2=law(s,s-F(1,2),s-1,s-1,F(1,2)-2*s,F(1,2)-2*s)
            assert all(x>=0 for x in w1+w2)
            d=F(1,3)*sum((w1[i]-qcal1(s)[i] for i in E1),F(0))+F(2,3)*sum((w2[i]-qcal1(s)[i] for i in E2),F(0))
            assert d==rc1(s)
        if s>=F(3,10):
            w3=law(s,s-F(1,2),s-1,s-1,F(1,2)-2*s,F(1,2)-2*s)
            w4=law(s,s+F(1,2),s-F(1,2),s-F(1,2),F(0),F(0))
            assert all(x>=0 for x in w3+w4)
            d=F(4,5)*sum((w3[i]-qcal2(s)[i] for i in E3),F(0))+F(1,5)*sum((w4[i]-qcal2(s)[i] for i in E4),F(0))
            assert d==rc2(s)
    assert rf(F(3,10))==rc1(F(3,10))==rc2(F(3,10))==F(2,5)
    return {
      'unit':'R749SNJ','status':'PASS',
      'frozen_scientific_pin':'a72226e2430ffa4786321ac86e7f0c599d5f0389',
      'scope':'t=1/2, real s in [1/4,1/3], auxiliary 16-element Walsh fiber',
      'formulae':{'free':'7/16-s/8',
                  'calibrated_left':'1/2-s/3 for 1/4<=s<=3/10',
                  'calibrated_right':'2/5 for 3/10<=s<=1/3'},
      'segment_certificates':{'free':free,'calibrated_left':cal1,'calibrated_right':cal2},
      'calibration_gap_zero_at':'s=3/10',
      'proof_method':'exact 6-dimensional joint polytope enumeration plus affine witness families and event-dual certificates; no floating point'
    }

if __name__=='__main__':
    print(json.dumps(main(),indent=2,sort_keys=True,ensure_ascii=False))
