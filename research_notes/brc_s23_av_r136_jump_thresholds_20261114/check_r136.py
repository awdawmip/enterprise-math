#!/usr/bin/env python3
"""Exact finite Sturmian tied-phase saturation enumeration (R136).
Uses rational floor-event sweep and independent Fraction floor recomputation.
"""
from fractions import Fraction
from math import gcd
from time import perf_counter
import argparse, json
from pathlib import Path

def totient(q):
    r=q; n=q; p=2
    while p*p <= n:
        if n%p==0:
            while n%p==0:n//=p
            r-=r//p
        p+=1
    if n>1:r-=r//n
    return r

def F(m):
    return 1+sum((m+1-q)*totient(q) for q in range(1,m+1))

def word_at(K,m,theta):
    out=0
    for i in range(m):
        if (K+i)*theta//1-((K+i-1)*theta//1):out|=1<<i
    return out

def sweep(K,m,verify=False):
    # n=L..L+m (nonzero n only)
    L=K-1
    events={}
    for n in range(max(1,L),L+m+1):
        mask=0
        j=n-L
        if j>=1:mask ^=1<<(j-1)
        if j<m:mask ^=1<<j
        for p in range(1,n):
            theta=Fraction(p,n)
            events[theta]=events.get(theta,0)^mask
    state=0
    words={state}
    cuts=sorted(events)
    for j,theta in enumerate(cuts):
        flip=events[theta]
        assert flip!=0, (K,m,theta)
        state ^=flip
        words.add(state)
        if verify and (j%max(1,len(cuts)//23)==0 or j==len(cuts)-1):
            assert state==word_at(K,m,theta), (K,m,theta,state,word_at(K,m,theta))
    if verify:
        assert state==word_at(K,m,Fraction(2*max(1,L+m)-1,2*max(1,L+m)))
        assert len(cuts)==sum(totient(q) for q in range(2,L+m+1) if ((L+m)//q - max(1,L-1)//q)>0), (K,m,len(cuts))
    return words,len(cuts)

def main(limit):
    t=perf_counter()
    rows=[]
    for m in range(1,limit+1):
        target=F(m)
        B=max(1,m*(m-1)) + 1
        counts=[];cuts=[]
        complement_checked=0
        for K in range(1,B+1):
            w,c=sweep(K,m,verify=(K in {1,B,m,2*m,m*m//4+1}))
            counts.append(len(w));cuts.append(c)
            if K>=2:
                full=(1<<m)-1
                assert all((v^full) in w for v in w),(m,K,"complement")
                complement_checked+=1
            if m<=8:
                # Independently evaluate every singleton cut, not just samples.
                cuts_direct=set()
                for n in range(max(1,K-1),K+m):
                    cuts_direct.update(Fraction(p,n) for p in range(1,n))
                W_direct={word_at(K,m,Fraction(1,10**20))}
                for theta in cuts_direct:
                    W_direct.add(word_at(K,m,theta))
                assert w==W_direct, (m,K,'independent_all_event_check')
            assert len(w)<=target,(m,K,len(w),target)
        assert counts[B-1]==target
        first=counts.index(target)+1
        last_bad=max((i+1 for i,c in enumerate(counts) if c!=target),default=0)
        row={"m":m,"finite_sturmian_language_size":target,"K_first":first,"K_eventual":last_bad+1,"R135_uniform_bound":B,"prebound_failure_count":sum(c!=target for c in counts),"failure_K_after_first":[k for k in range(first,B+1) if counts[k-1]!=target],"max_distinct_jump_cuts_at_B":cuts[-1],"complement_checks":complement_checked}
        rows.append(row)
        print('M',m,'F',target,'first',first,'eventual',last_bad+1,'oldbound',B,'elapsed',round(perf_counter()-t,1),flush=True)
    result={"status":"R136_EXACT_THRESHOLD_SWEEP_PASS","scope":{"m_inclusive":[1,limit],"K_for_each_m":"1..R135_uniform_bound(m), as reported in each row"},"method":"Exact Fraction sorting; aggregated floor jumps; independently recomputed floor words at selected rational events","rows":rows,"duration_seconds":round(perf_counter()-t,2)}
    with Path(__file__).with_name('verification_r136.json').open('w') as f:json.dump(result,f,indent=2)
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--limit',type=int,default=15)
    args=p.parse_args();main(args.limit)
