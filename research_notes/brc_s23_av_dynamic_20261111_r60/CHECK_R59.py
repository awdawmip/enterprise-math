#!/usr/bin/env python3
"""R59 exact rational-circle youngest-only query, independent direct-phase oracle."""
from bisect import bisect_right
from math import gcd
from random import Random
import json
from pathlib import Path

PIN='43ec6098b1330ae86d0a7863be336c5d97f6ef34'

def floor_sum(n,m,a,b):
    """Sum_{0<=i<n} floor((a*i+b)/m); nonnegative a,b, positive m."""
    ans=0
    while True:
        if a>=m:
            ans+=n*(n-1)//2*(a//m); a%=m
        if b>=m:
            ans+=n*(b//m); b%=m
        y=a*n+b
        if y<m:return ans
        n=y//m
        b=y%m
        m,a=a,m

def farey(p,q,K):
    a,i,c,j=0,1,1,1
    while i+j<=K:
        if (a+c)*q<(i+j)*p:a,i=a+c,i+j
        else:c,j=c+a,j+i
    return i,j

def phase_rank_cuts(p,q,m,H,kmax):
    K=m+H-1
    i,j=farey(p,q,K)
    s=j;cuts=[]
    for _ in range(kmax):
        cuts.append(s)
        s=s-i if s>i else(s+j if s+j<=K else s+j-i)
    return i,j,cuts

def sample_phases(p,q,m,H,queries):
    K=m+H-1;maxk=max(queries,default=0)
    i,j,cuts=phase_rank_cuts(p,q,m,H,min(K,maxk+1))
    first=(j*p)%q
    phases=[]
    for k in queries:
        if k==0:x=q+first
        elif k==K:x=(cuts[-1]*p)%q
        else:x=(cuts[k-1]*p)%q+(cuts[k]*p)%q
        phases.append(x)
    return i,j,phases

def latest_from_direct_phase(p,q,m,H,x):
    bounds=sorted((2*(z*p%q),z) for z in range(m))
    starts=[b for b,z in bounds];labels=[z for b,z in bounds]
    newest=[None]*m; owners=[]
    for r in range(1,H+1):
        y=(x-2*r*p)%(2*q)
        z=labels[bisect_right(starts,y)-1]
        owners.append(z)
        if newest[z] is None:newest[z]=r
    return newest,owners

def youngest_floor_sum(p,q,m,H,x,stats=None):
    M=2*q; a=(M-2*p)%M
    boundaries=sorted((2*(z*p%q),z) for z in range(m))
    newest=[None]*m
    seen=0
    for h,(left,z) in enumerate(boundaries):
        right=boundaries[(h+1)%m][0]
        wrap=(h==m-1)
        b=(x+a)%M
        def hits(t):
            nonlocal seen
            seen+=2
            return floor_sum(t,M,a,b+M-left)-floor_sum(t,M,a,b+M-right)+(t if wrap else 0)
        if hits(H)==0:continue
        lo,hi=1,H
        while lo<hi:
            mid=(lo+hi)//2
            if hits(mid)>0:hi=mid
            else:lo=mid+1
        newest[z]=lo
    if stats is not None:stats['floor_sum_calls']+=seen
    return newest

def main():
    rng=Random(590011);count=queries=fs=0
    for m in range(1,13):
        for H in range(1,16):
            K=m+H-1
            for rep in range(8):
                p=rng.randrange(1,1009)
                ks=[K,0,1,min(K,rep% (K+1)),K//2,K];rng.shuffle(ks)
                i,j,xs=sample_phases(p,1009,m,H,ks)
                for x in xs:
                    stats={'floor_sum_calls':0}
                    got=youngest_floor_sum(p,1009,m,H,x,stats)
                    want,owners=latest_from_direct_phase(p,1009,m,H,x)
                    assert got==want,(m,H,p,ks,x,got,want)
                    fs+=stats['floor_sum_calls']
                count+=1;queries+=len(ks)
    D=10**24;plo=262204504569236716045286
    frozen=[]
    for p in (plo,plo+1):
        m,H=128,225;K=m+H-1
        ks=[352,0,1,4,32,88,176,264,352,176,351,225,61,126,127,163,164]
        rng.shuffle(ks)
        i,j,xs=sample_phases(p,D,m,H,ks)
        stats={'floor_sum_calls':0}
        got=[youngest_floor_sum(p,D,m,H,x,stats) for x in xs]
        want=[latest_from_direct_phase(p,D,m,H,x)[0] for x in xs]
        assert got==want
        assert (i,j)==(164,225)
        frozen.append({'p':str(p),'q':str(D),'Q':len(ks),'m':m,'H':H,'K':K,'farey_lower_den':i,'farey_upper_den':j,'floor_sum_calls':stats['floor_sum_calls'],'checkpoint_ranks':ks,'youngest_entries':len(ks)*m,'full_owner_entries_avoided':len(ks)*H,'earliest_first_five':got[0][:5]})
    m,H,p,q=3,20000,414214,1000003
    K=m+H-1
    assert q>K
    ks=[rng.randrange(K+1) for _ in range(60)]
    i,j,xs=sample_phases(p,q,m,H,ks)
    st={'floor_sum_calls':0}
    got=[youngest_floor_sum(p,q,m,H,x,st) for x in xs]
    for k in (0,1,10,30,45,59):
        want,_=latest_from_direct_phase(p,q,m,H,xs[k]);assert got[k]==want
    large={'m':m,'H':H,'Q':len(ks),'K':K,'floor_sum_calls':st['floor_sum_calls'],'explicit_full_owner_fields_avoided':H*len(ks),'youngest_fields':m*len(ks),'oracle_verified_queries':6}
    result={'science_pin':PIN,'mathematics':'exact rational auxiliary rotation with finite distinct phases','test_cases':count,'checkpoint_queries':queries,'small_floor_sum_calls':fs,'frozen_cases':frozen,'large_sparse_case':large,'author_only':True}
    path=Path(__file__).with_name('CERTIFICATE.json');path.write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
    print('PASS_R59',count,'queries',queries,'small_floor_sums',fs,'S23',frozen,'large',large)
if __name__=='__main__':main()
