#!/usr/bin/env python3
"""PREFIX-972 source-fiber gcd join; requires PREFIX968 and PREFIX972 verifier alongside."""
import argparse
import hashlib
import json
import statistics
import time
from collections import Counter,defaultdict
from math import gcd
from PREFIX968_R6_MODULAR_BUCKET_JOIN import mjoin,slots,direct_small
from PREFIX972_R6_PARITY_FIBER_VERIFIER import source_fiber


def accelerated(p,k,m):
    H=1<<(p-1); low=H+1; high=2*H-1
    s=slots(p); cache={}; ans=[]; st=Counter()
    for t in range(1,2*k+1):
        g=gcd(k,t)
        if g not in cache:
            fib=defaultdict(list)
            for i,j,sgn,c in source_fiber(p,g):fib[c].append((i,j,sgn))
            cache[g]={b:sorted((c,tuple(v)) for c,v in fib.items() if c%2==b) for b in (0,1)}
        left=cache[g][(1-t)%2]; right=s[t%2]
        d=2*t-k*m; mod=abs(d)
        tab=defaultdict(list)
        for C,Cs in right:tab[k*C%mod].append((C,Cs))
        st['bucket_entries']+=len(right)
        st['gcd_filtered_numeric_c_probes']+=len(left)
        for c,cs in left:
            for C,Cs in tab[(k+2)*c%mod]:
                st['joined_pairs']+=1
                N=k*C-(k+2)*c
                assert N%d==0
                b=N//d
                if not low<=b<=high:continue
                v=m*b+C-c
                if v%4!=2:continue
                a=v//2
                if not low<=a<=high or a==b:continue
                st['arithmetic_pairs']+=1
                ls=[(i,j) for i,j,sgn in cs if ((t*b+(1<<i))>>j)&1==(sgn==1)]
                rs=[(i,j) for i,j,sgn in Cs if (((t+m)*b+(1<<i))>>j)&1==(sgn==1)]
                for i,j in ls:
                    for I,J in rs:
                        assert (((k*a)^(1<<j))-(1<<i))==t*b
                        assert ((((k+2)*a)^(1<<J))-(1<<I))==(t+m)*b
                        ans.append((a,b,t,t+m,i,j,I,J))
    ans.sort()
    return ans,dict(st)


def run():
    p,k=19,21; expected={1:(442,614),3:(839,1286),5:(3,3)}
    comparisons=[]
    for m,(n_pairs,n_hist) in expected.items():
        slow,st_old,old_hash=mjoin(p,k,m)
        fast,st_new=accelerated(p,k,m)
        assert slow==fast and len(fast)==n_hist
        assert len({(x[0],x[1]) for x in fast})==n_pairs
        comparisons.append({'m':m,'num_pairs':n_pairs,'named_histories':n_hist,'hash':old_hash,'baseline':st_old,'gcd_source_join':st_new})
    cases=0
    for pp in range(4,8):
        for kk in range(1,(1<<(pp-1))-2,2):
            for mm in (1,3,5):
                a,_=accelerated(pp,kk,mm)
                assert Counter(a)==direct_small(pp,kk,mm),(pp,kk,mm)
                cases+=1
    baseline=[]; enhanced=[]
    for r in range(12):
        for name in (('baseline','enhanced') if r%2==0 else ('enhanced','baseline')):
            begin=time.perf_counter()
            for m in (1,3,5):
                if name=='baseline': mjoin(p,k,m)
                else: accelerated(p,k,m)
            elapsed=time.perf_counter()-begin
            (baseline if name=='baseline' else enhanced).append(elapsed)
    return {'schema':'PREFIX972_SOURCE_GCD_JOIN_V1','q19':comparisons,'raw_xor_small_cases':cases,
            'benchmark':{'repeats_each':12,'baseline_median_s':statistics.median(baseline),'source_gcd_join_median_s':statistics.median(enhanced),'measurement':'Local CPython, 12 alternating whole-triplet runs including source-fiber construction, bucket building, named restoration and XOR checks'},
            'status':'AUTHOR_PROOF_EXACT_INTEGER_VERIFIED_NOT_REVIEWED'}


if __name__=='__main__':
    x=run(); print(json.dumps(x,indent=2))
