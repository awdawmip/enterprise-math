#!/usr/bin/env python3
"""R166 independent exact Fraction verification for external finite-Sturmian signatures."""
from fractions import Fraction as F
from collections import defaultdict, Counter
from functools import lru_cache
from itertools import product
import json

@lru_cache(None)
def signature(w):
    n=len(w)
    p=[0]
    for a in w:p.append(p[-1]+(a=='1'))
    lo,hi=F(0),F(1)
    for i in range(n):
        for k in range(i+1,n+1):
            d=p[k]-p[i];length=k-i
            lo=max(lo,F(d-1,length));hi=min(hi,F(d+1,length))
    if lo>=hi:return None
    A=min(F(p[i])-i*lo for i in range(n+1))
    B=max(F(p[i])-i*hi for i in range(n+1))
    return (lo,hi,int(lo.denominator*(1+A)),int(hi.denominator*B))

def contact_data(w,v):
    assert len(w)==len(v)
    p=[0];s=[0]
    for x,y in zip(w,v):
        p.append(p[-1]+int(x));s.append(s[-1]+int(y))
    loc=[i for i in range(len(p)) if p[i]!=s[i]]
    assert len(loc)==1,(w,v,loc)
    j=loc[0]
    assert j<len(w) and p[-1]==s[-1]
    return j,max(p[j],s[j]),p[-1]

def criterion(w,v,bit):
    alpha,beta,_,_=signature(w)
    m=len(w)
    j,q,N=contact_data(w,v)
    t=m+1-j
    r=N+int(bit)
    return F(r-q,t)<=alpha and beta<=F(r+1-q,t)

def main(max_length=16):
    assert max_length>=2
    by=[]
    total_pairs=total_tests=survive=0
    examples={}
    for m in range(2,max_length+1):
        groups=defaultdict(list)
        for v in range(1<<m):
            w=format(v,'0%db'%m)
            s=signature(w)
            if s is not None:groups[s].append(w)
        ct=Counter()
        for s,words in groups.items():
            assert len(words)<=2,(m,s,words)
            if len(words)!=2:continue
            u,v=words
            j,q,N=contact_data(u,v)
            assert u[j-1:j+1]!=v[j-1:j+1]
            predicted=[]
            observed=[]
            for bit in '01':
                prec=criterion(u,v,bit)
                a=signature(u+bit);b=signature(v+bit)
                truth=(a is not None and a==b)
                assert prec==truth,(m,u,v,bit,prec,a,b)
                if prec:predicted.append(bit)
                if truth:observed.append(bit)
                total_tests+=1
            assert predicted==observed and len(observed)<=1,(u,v,observed)
            ct['double_pairs']+=1
            ct['persistence_'+(''.join(observed) if observed else 'none')]+=1
            total_pairs+=1
            survive+=len(observed)
            if observed:examples.setdefault(observed[0],dict(m=m,w=u,v=v,bit=observed[0],signature=str(s)))
            else:examples.setdefault('none',dict(m=m,w=u,v=v,signature=str(s)))
        by.append(dict(m=m,**ct))
    horizon_checks=0
    horizon_counts=Counter()
    for m in range(2,10):
        groups=defaultdict(list)
        for i in range(1<<m):
            w=format(i,'0%db'%m);s=signature(w)
            if s is not None:groups[s].append(w)
        for words in groups.values():
            if len(words)!=2:continue
            u,v=words
            for k in range(1,6):
                survivors=[]
                for bits in map(''.join,product('01',repeat=k)):
                    ok=True
                    for j in range(1,k+1):
                        x=signature(u+bits[:j]);y=signature(v+bits[:j])
                        if x is None or x!=y:
                            ok=False;break
                    if ok:survivors.append(bits)
                    horizon_checks+=1
                assert len(survivors)<=1,(u,v,k,survivors)
                horizon_counts[k]+=len(survivors)
    deterministic_paths_checked=0; predicted_steps=0; max_surviving_steps=0; max_width_bound=0
    for m in range(2,max_length+1):
        groups=defaultdict(list)
        for n in range(1<<m):
            w=format(n,'0%db'%m)
            sig=signature(w)
            if sig is not None:groups[sig].append(w)
        for sig,words in groups.items():
            if len(words)!=2:continue
            u,v=words
            j,q,N=contact_data(u,v)
            alpha,beta,_,_=sig
            delta=beta-alpha
            width_bound=(1//delta)-(m-j)
            assert width_bound>=0
            max_width_bound=max(max_width_bound,width_bound)
            deterministic_paths_checked+=1
            suffix=''; prev=N
            for h in range(1,width_bound+2):
                t=m+h-j
                R=F(q)+t*alpha
                L=F(q)+t*beta-1
                candidate=R.numerator//R.denominator
                if candidate<L or candidate-prev not in (0,1):
                    break
                suffix+=str(candidate-prev)
                prev=candidate
                p=signature(u+suffix)
                assert p==sig and signature(v+suffix)==sig,(u,v,suffix,p,sig)
                predicted_steps+=1
            assert len(suffix)<=width_bound
            max_surviving_steps=max(max_surviving_steps,len(suffix))
            for bit in '01':
                x=signature(u+suffix+bit);y=signature(v+suffix+bit)
                assert x is None or x!=y,(u,v,suffix,bit,x,y)
    return dict(marker='R166_EXACT_APPEND_PRESERVATION_PASS',
                candidate_words=sum(1<<m for m in range(2,max_length+1)),
                m_min=2,m_max=max_length,collision_pairs=total_pairs,
                next_bit_checks=total_tests,persistent_next_bit_cases=survive,
                exact_future_path_pairs=deterministic_paths_checked,
                verified_persistent_steps=predicted_steps,
                maximum_actual_survival_steps=max_surviving_steps,
                max_geometric_width_bound=max_width_bound,
                both_next_bits_persistent=0,horizon_candidate_checks=horizon_checks,
                unique_prefixwise_horizon_survivors=dict(horizon_counts),
                per_length=by,representative_cases=examples,
                validation='complete binary enumeration by length, independent O(m^2) Fraction signature oracle; criterion uses only old signature, swap index and total ones',
                independent_review='NOT_REVIEWED')
if __name__=='__main__':
    print(json.dumps(main(),indent=2,ensure_ascii=False))
