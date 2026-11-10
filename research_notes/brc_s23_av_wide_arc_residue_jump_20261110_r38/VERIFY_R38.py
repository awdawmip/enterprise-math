#!/usr/bin/env python3
"""R38 exact q-residue first-hit selector; independent R36/R37 floor-sum oracle.
All scientific decisions use integer/Fraction arithmetic; finite rational enclosures
for irrational parameters are certified by integer isqrt. No float decisions.
"""
from fractions import Fraction as F
from math import isqrt
from bisect import bisect_right
from pathlib import Path
import json, hashlib, time

FROZEN_S23='43ec6098b1330ae86d0a7863be336c5d97f6ef34'
D=10**45
S=isqrt(2*D*D)
SQ2_L,SQ2_U=F(S,D),F(S+1,D)

def theta_pair(kind):
    if kind=='NEAR_3':return F(1,3)+SQ2_L/10**7,F(1,3)+SQ2_U/10**7
    if kind=='NEAR_3_NEG':return F(1,3)-SQ2_U/10**7,F(1,3)-SQ2_L/10**7
    if kind=='NEAR_7':return F(2,7)+SQ2_L/10**8,F(2,7)+SQ2_U/10**8
    if kind=='SQRT2':return SQ2_L-1,SQ2_U-1
    if kind=='S23':return F(262204504569236716045286,10**24),F(262204504569236716045287,10**24)
    raise ValueError(kind)

def frac(x):return x-x.numerator//x.denominator

def flo(x):return x.numerator//x.denominator

def floor_sum(n,m,a,b):
    assert n>=0 and m>0 and a>=0 and b>=0
    out=0
    while True:
        if a>=m:out+=n*(n-1)*(a//m)//2;a%=m
        if b>=m:out+=n*(b//m);b%=m
        y=a*n+b
        if y<m:return out
        n,b,m,a=y//m,y%m,a,m

def shifted(l,r,s,P,Q):
    if l>=r:return 0
    n=r-l;z,b=divmod((l-s)*P,Q)
    return n*z+floor_sum(n,Q,P,b)

def below(s,l,r,P,Q):
    return shifted(l,r,0,P,Q)-shifted(l,r,s,P,Q)-(r-l)*((s*P)//Q)

def count_arc(s,e,l,r,P,Q):
    if l>=r:return 0
    count=below(e,l,r,P,Q)-below(s,l,r,P,Q)
    if (s*P)%Q>(e*P)%Q:count+=r-l
    assert 0<=count<=r-l
    return count

def oracle(arcs,l,r,P,Q):
    result=[];calls=0
    for s,e in arcs:
        v=count_arc(s,e,l,r,P,Q);calls+=1
        if not v:result.append(None);continue
        left,right=l,r
        while left+1<right:
            md=(left+right)//2
            if count_arc(s,e,md,r,P,Q):left=md
            else:right=md
            calls+=1
        result.append(left)
    return result,calls

class Model:
    def __init__(self,kind,m):
        self.lo,self.hi=theta_pair(kind)
        self.mid=(self.lo+self.hi)/2
        self.P,self.Q=self.mid.numerator,self.mid.denominator
        self.m=m;self.kind=kind
        self.order=sorted(range(m),key=lambda s:frac(s*self.mid))
        self.phases=[frac(s*self.mid) for s in self.order]
        self.arcs=[(s,self.order[(a+1)%m]) for a,s in enumerate(self.order)]
        for d in range(1,m):assert flo(d*self.lo)==flo(d*self.hi)
    def owner_idx(self,x):return (bisect_right(self.phases,x)-1)%self.m
    def arc_contains(self,i,x):
        a=self.phases[i];b=self.phases[(i+1)%self.m]
        return (a<=x<b if a<b else x>=a or x<b)
    def wide_certificate(self,p,q):
        lo,hi=self.lo,self.hi
        assert 0<=p<q and 0<lo<hi<1
        d0=q*lo-p;d1=q*hi-p
        if d0>0:sign=1
        elif d1<0:sign=-1
        else:return False,'residual crosses zero'
        maxdelta=max(abs(d0),abs(d1))
        if not(0<maxdelta<1):return False,'residual not subunit'
        for s,e in self.arcs:
            dd=e-s
            if flo(dd*lo)!=flo(dd*hi):return False,'historical gap branch unstable'
            for t in (lo,hi):
                gap=frac(dd*t)
                if gap < abs(q*t-p):return False,'arc shorter than residue drift'
        return True,sign
    def select(self,j,N,p,q,cert=True):
        ok,sign=self.wide_certificate(p,q)
        if not ok:return None,{'method':'INAPPLICABLE','reason':sign}
        delta=abs(q*self.mid-p)
        answer=[None]*self.m
        checks=0
        for s in range(1,min(q,N)+1):
            t=j-s
            x=frac(t*self.mid)
            first_owner=self.owner_idx(x)
            if cert:
                for boundary in (self.arcs[first_owner]):
                    d=t-boundary
                    assert flo(d*self.lo)==flo(d*self.hi)
            max_k=(N-s)//q
            for i,(a,e) in enumerate(self.arcs):
                if i==first_owner:k=0
                else:
                    endpoint=e if sign==1 else a
                    d=t-endpoint if sign==1 else endpoint-t
                    f=frac(d*self.mid)
                    ratio=f/delta
                    k=(flo(ratio)+1) if sign==1 else -flo(-ratio)
                    if cert:
                        assert flo(d*self.lo)==flo(d*self.hi)
                        low_ratio=frac(d*self.lo)/abs(q*self.lo-p)
                        high_ratio=frac(d*self.hi)/abs(q*self.hi-p)
                        if sign==1:
                            assert flo(low_ratio)==flo(high_ratio)==k-1,(self.kind,self.m,s,i,k)
                        else:
                            assert -flo(-low_ratio)==-flo(-high_ratio)==k,(self.kind,self.m,s,i,k)
                        checks+=1
                if k>max_k:continue
                hit=j-s-k*q
                assert self.arc_contains(i,frac(hit*self.mid)),(self.kind,s,i,hit,k)
                if answer[i] is None or hit>answer[i]:answer[i]=hit
        return answer,{'method':'MODULAR_JUMP','q':q,'m':self.m,'j':j,'N':N,
                       'residual_sign':sign,'endpoint_quotient_certificates':checks,
                       'owner_labels_certified':q,'candidate_tests':self.m*min(q,N)}

def do_case(kind,m,p,q,j,N,independent=True):
    model=Model(kind,m)
    t0=time.perf_counter()
    pred,stats=model.select(j,N,p,q,cert=True)
    if pred is None:return {**stats,'case':kind,'m':m,'p':p,'q':q,'j':j,'N':N}
    if independent:
        checked,calls=oracle(model.arcs,j-N,j,model.P,model.Q)
        assert pred==checked,(kind,m,p,q,j,N,[(i,x,y) for i,(x,y) in enumerate(zip(pred,checked)) if x!=y])
    else:calls=None
    stats.update(case=kind,p=p,selected_owners=sum(x is not None for x in pred),
                 oracle_floor_sum_queries=calls,last_source_by_historical_arc=pred,
                 elapsed_s=round(time.perf_counter()-t0,4))
    return stats

def brute_tests():
    count=0
    for kind,m,p,q in [('NEAR_3',7,1,3),('NEAR_7',8,2,7),('NEAR_3_NEG',8,1,3),('SQRT2',4,2,5),('SQRT2',16,5,12)]:
        mo=Model(kind,m)
        for j in (m+5,50,1000):
            for N in (1,2,3,5,10,23,100,503):
                if j-N < 0:continue
                res,_=mo.select(j,N,p,q)
                if res is None:continue
                raw=[None]*m
                for t in range(j-N,j):raw[mo.owner_idx(frac(t*mo.mid))]=t
                assert res==raw,(kind,m,j,N,res,raw)
                count+=1
    return count

def main():
    cases=[
       ('NEAR_3',21,1,3,10**9,10**8),
       ('NEAR_3',21,1,3,10**12,10**9),
       ('NEAR_3',63,1,3,10**12,10**9),
       ('NEAR_7',31,2,7,10**9,10**8),
       ('NEAR_7',70,2,7,10**12,10**9),
       ('NEAR_3_NEG',21,1,3,10**12,10**9),
       ('SQRT2',16,5,12,10**12,10**9),
       ('S23',128,43,164,10**12,10**9),
       ('SQRT2',16,2,5,10**12,10**9),
    ]
    rows=[]
    for z in cases:
        r=do_case(*z);rows.append(r)
        print(z[0],z[1],f'q={z[3]}',r['method'],r.get('candidate_tests'),r.get('oracle_floor_sum_queries'),r.get('reason'))
    n=brute_tests()
    dest=Path(__file__).resolve().parent/'CERTIFICATE_R38.json'
    data={'schema':'EM_R38_MODULAR_RESIDUE_JUMP_V1','science_pin':FROZEN_S23,
          'cases':rows,'brute_tests_count':n,'method':'exact fractions, interval endpoint quotient stability, independent floor-sum select'}
    dest.write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n')
    print('PASS_R38_WIDE_ARC_MODULAR_JUMP',len([r for r in rows if r['method']=='MODULAR_JUMP']),'families, brute',n,
          'certificate_SHA256',hashlib.sha256(dest.read_bytes()).hexdigest())
if __name__=='__main__':main()
