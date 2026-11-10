#!/usr/bin/env python3
"""R37: exact suffix saturation for owner-labelled rotation source selection.

Fractions only; exact output certificate. Independent floor-sum whole-window
rank/select verifies every selected last source, even for billion-length windows.
"""
from bisect import bisect_right
from fractions import Fraction as F
from math import isqrt
import hashlib, json, time

S23_PIN='43ec6098b1330ae86d0a7863be336c5d97f6ef34'

def root2_pair(D=10**45):
    a=isqrt(2*D*D)
    return F(a,D), F(a+1,D)

def theta_pair(kind):
    if kind=='S23':
        return F(262204504569236716045286,10**24), F(262204504569236716045287,10**24)
    a,b=root2_pair()
    if kind=='SQRT2':return a-1,b-1
    if kind=='NEAR_THIRD':return F(1,3)+a/10**7,F(1,3)+b/10**7
    raise ValueError(kind)

def floor(x):return x.numerator//x.denominator

def floor_sum(n,mod,a,b):
    assert n>=0 and mod>0 and a>=0 and b>=0
    out=0
    while True:
        if a>=mod:out+=n*(n-1)*(a//mod)//2;a%=mod
        if b>=mod:out+=n*(b//mod);b%=mod
        z=a*n+b
        if z<mod:return out
        n,b,mod,a=z//mod,z%mod,a,mod

def shifted(l,r,s,P,Q):
    if l>=r:return 0
    k=r-l
    q,b=divmod((l-s)*P,Q)
    return k*q+floor_sum(k,Q,P,b)

def below(s,l,r,P,Q):
    return shifted(l,r,0,P,Q)-shifted(l,r,s,P,Q)-(r-l)*((s*P)//Q)

def count_arc(s,e,l,r,P,Q):
    if l>=r:return 0
    z=below(e,l,r,P,Q)-below(s,l,r,P,Q)
    if (s*P)%Q>(e*P)%Q:z+=r-l
    assert 0<=z<=r-l
    return z

def oracle_tau(arcs,l,r,P,Q):
    ans=[];n_queries=0
    for s,e in arcs:
        c=count_arc(s,e,l,r,P,Q);n_queries+=1
        if not c:ans.append(None);continue
        left,right=l,r
        while left+1<right:
            mid=(left+right)//2
            cm=count_arc(s,e,mid,r,P,Q);n_queries+=1
            if cm:left=mid
            else:right=mid
        ans.append(left)
    return ans,n_queries

class Owner:
    def __init__(self,m,lo,hi):
        self.m,self.lo,self.hi=m,lo,hi
        mid=(lo+hi)/2;self.P,self.Q=mid.numerator,mid.denominator
        self.order=sorted(range(m),key=lambda t:(t*self.P)%self.Q)
        self.phase=[(s*self.P)%self.Q for s in self.order]
        self.arcs=[(s,self.order[(k+1)%m]) for k,s in enumerate(self.order)]
        # Historical arc ordering is fixed over the whole enclosure.
        for d in range(1,m):
            assert floor(d*lo)==floor(d*hi)
        self.min_gap=min(F((self.phase[(k+1)%m]-self.phase[k])%self.Q,self.Q)
                         for k in range(m))
        self.delta=min(F((self.phase[(k+1)%m]-self.phase[k])%self.Q,self.Q)
                       -m*(hi-lo) for k in range(m))
        assert self.delta>0
        self.labels_checked=0

    def owner(self,t,cert=True):
        idx=(bisect_right(self.phase,(t*self.P)%self.Q)-1)%self.m
        if cert:
            s,e=self.arcs[idx]
            # No intersection with the two boundaries of this owner arc.
            for d in (t-s,t-e):
                assert d==0 or floor(d*self.lo)==floor(d*self.hi),(t,d,idx)
            self.labels_checked+=1
        return idx

    def suffix(self,j,N,scan_budget=2000):
        last=[None]*self.m;seen=0
        stop=min(N,scan_budget)
        for r in range(1,stop+1):
            idx=self.owner(j-r)
            if last[idx] is None:
                last[idx]=j-r;seen+=1
                if seen==self.m:
                    return last,r,'CERTIFIED_SATURATED',seen
        if N<=scan_budget:return last,stop,'COMPLETE_WINDOW',seen
        return last,stop,'NEEDS_FLOOR_SUM_FALLBACK',seen

    def convergent_bound(self,max_denom=10**9):
        x=F(self.P,self.Q);p0,p1=0,1;q0,q1=1,0
        while True:
            a=x.numerator//x.denominator
            p=a*p1+p0;q=a*q1+q0
            if q>max_denom:return None
            eps=max(abs(self.lo-F(p,q)),abs(self.hi-F(p,q)))
            G=F(1,q)+2*(q-1)*eps
            if G<self.delta:return (p,q,str(G),str(self.delta))
            p0,p1=p1,p;q0,q1=q1,q
            rem=x-a
            if not rem:return None
            x=1/rem

def run_case(kind,m,j,N,budget=2000):
    lo,hi=theta_pair(kind);ob=Owner(m,lo,hi)
    began=time.perf_counter()
    last,seen,mode,hit=ob.suffix(j,N,budget)
    # Independent full-window per-arc floor-sum last-source selector.
    complete,oracle_q=oracle_tau(ob.arcs,j-N,j,ob.P,ob.Q)
    if mode=='NEEDS_FLOOR_SUM_FALLBACK':
        method='floor_sum_fallback'
        assert all(v is None or complete[k]==v for k,v in enumerate(last))
    else:
        method='suffix_scan'
        assert complete==last,(kind,m,j,N,seen)
    assert all(v is None or count_arc(*ob.arcs[k],v,j,ob.P,ob.Q)>0
               for k,v in enumerate(complete))
    if mode=='CERTIFIED_SATURATED':
        assert sum(x is not None for x in last)==m
        assert ob.owner(j-seen,cert=False) in [
            k for k,v in enumerate(last) if v==j-seen]
    conv=ob.convergent_bound(max_denom=10**7)
    return dict(case=kind,m=m,j=j,N=N,scan_budget=budget,
                scan_count=seen,seen_owners=hit,method=method,mode=mode,
                whole_window_owners=sum(x is not None for x in complete),
                floor_sum_oracle_queries=oracle_q,bound_convergent=conv,
                min_historical_gap_mid=str(ob.min_gap),
                owner_labels_certified=ob.labels_checked,
                last_source_by_historical_arc=complete,
                elapsed_s=round(time.perf_counter()-began,4))

def brute_regress():
    for kind,m in [('SQRT2',16),('SQRT2',32),('NEAR_THIRD',21)]:
        lo,hi=theta_pair(kind);ob=Owner(m,lo,hi)
        for j in (m+7,2*m+21,1177):
            for N in (1,2,3,10,40,100,240):
                if j-N<0:continue
                got,seen,mode,_=ob.suffix(j,N,scan_budget=200)
                baseline=[None]*m
                for t in range(j-N,j):baseline[ob.owner(t)]=t
                if mode=='NEEDS_FLOOR_SUM_FALLBACK':
                    got,_=oracle_tau(ob.arcs,j-N,j,ob.P,ob.Q)
                assert got==baseline,(kind,m,j,N,mode)
    return 'PASS_SMALL_WINDOWS_BRUTE_AND_FLOOR_SUM'

def main():
    rows=[]
    for kind,m,j,N in [('SQRT2',16,10**12,10**9),
                       ('SQRT2',32,10**12,10**9),
                       ('SQRT2',128,10**12,10**9),
                       ('SQRT2',257,10**12,10**9),
                       ('S23',128,10**12,10**9),
                       ('NEAR_THIRD',21,10**9,10**8)]:
        row=run_case(kind,m,j,N);rows.append(row)
        print(kind,m,'mode',row['mode'],'H/scan',row['scan_count'],
              'oracle',row['floor_sum_oracle_queries'],
              'bound',row['bound_convergent'] and row['bound_convergent'][1])
    verdict=brute_regress()
    from pathlib import Path
    out=Path(__file__).resolve().parent
    obj={'schema':'EM_R37_SUFFIX_COVER_CERT_V1','frozen_science_pin':S23_PIN,
         'rows':rows,'small_tests':verdict,
         'scope':'rotation observer, exact rational midpoint plus certified suffix labels over each input enclosure; oracle whole-window comparisons at midpoint'}
    (out/'CERTIFICATE_R37.json').write_text(
        json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
    print('PASS_R37_EXACT_SUFFIX_SATURATION_AND_FLOOR_SUM_REFERENCE',verdict)
    print('certificate_SHA256',
          hashlib.sha256((out/'CERTIFICATE_R37.json').read_bytes()).hexdigest())

if __name__=='__main__':main()
