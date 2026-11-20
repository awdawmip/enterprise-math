#!/usr/bin/env python3
"""PREFIX-973: exact source-mask/BRC positive-mass observer for odd-gap XOR.
Needs PREFIX968_R6_MODULAR_BUCKET_JOIN.py in the same directory (named reference).
"""
from bisect import bisect_left
from collections import Counter, defaultdict
from hashlib import sha256
from math import gcd
from statistics import median
from time import perf_counter
import json
from PREFIX968_R6_MODULAR_BUCKET_JOIN import slots, mjoin, direct_small

PIN = 'f42f2906d77f24085c123f3ccfe9667d41caa96d'
EXPECTED = {1:(442,614),3:(839,1286),5:(3,3)}

def mask_dictionary(p):
    """Each numeric c has + and - bit-j masks. For fixed (c,j,s), i is unique."""
    masks = defaultdict(lambda:[0,0])
    for i in range(p):
        for j in range(p):
            for s in (1,-1):
                c = (1<<i)-s*(1<<j)
                masks[c][0 if s==1 else 1] |= 1<<j
    return {c:tuple(pair) for c,pair in masks.items()}

def multiplicity(masks,x):
    plus,minus=masks
    return (plus & ~x).bit_count() + (minus & x).bit_count()

def ceildiv(a,b): return -((-a)//b)

def count(p,k,gaps=(1,3,5)):
    """Signed labels are summarized as bitmasks only for exact counting.
    To recover named tuples use the historical PREFIX968 mjoin source fibers.
    """
    assert p>=4 and k%2 and 0<k and k+2<(1<<(p-1))
    assert all(m>0 and m%2 for m in gaps)
    H=1<<(p-1); lo=H+1; hi=2*H-1
    M=mask_dictionary(p)
    right={r:sorted((c,M[c]) for c in M if c%2==r) for r in (0,1)}
    left_cache={};bucket_cache={};stats={m:Counter() for m in gaps}
    pairs={m:set() for m in gaps};hist={m:Counter() for m in gaps}
    for t in range(1,2*k+1):
        g=gcd(k,t);par=(1-t)%2
        if (g,par) not in left_cache:
            left_cache[(g,par)]=[(c,M[c]) for c in sorted(M) if c%g==0 and c%2==par]
        for m in gaps:
            d=2*t-k*m; q=abs(d)//g
            key=(q,t%2)
            if key not in bucket_cache:
                table=defaultdict(list)
                for C,Cm in right[t%2]: table[C%q].append((C,Cm))
                bucket_cache[key]=table
            inv=pow(k//g,-1,q) if q>1 else 0
            dl,dh=sorted((d*lo,d*hi))
            for c,cm in left_cache[(g,par)]:
                low=max(ceildiv((k+2)*c+dl,k),ceildiv((t+m)*c+dl,t))
                high=min(((k+2)*c+dh)//k,((t+m)*c+dh)//t)
                if low>high:continue
                bucket=bucket_cache[key][((k+2)*(c//g)*inv)%q]
                for C,Cm in bucket[bisect_left(bucket,(low,)):bisect_left(bucket,(high+1,))]:
                    stats[m]['interval_candidates']+=1
                    bn=k*C-(k+2)*c;an=t*C-(t+m)*c
                    assert bn%d==an%d==0
                    b=bn//d;a=an//d
                    assert lo<=a<=hi and lo<=b<=hi and a%2 and b%2
                    if a==b:continue
                    stats[m]['nondiagonal_numeric_candidates']+=1
                    w=multiplicity(cm,k*a)*multiplicity(Cm,(k+2)*a)
                    stats[m]['named_mass']+=w
                    hist[m][w]+=1
                    if w:pairs[m].add((a,b))
    return {m:{**stats[m],'distinct_modulus_pairs':len(pairs[m]),
               'weight_histogram':{str(w):hist[m][w] for w in sorted(hist[m])},
               'second_mass_moment':sum(w*w*n for w,n in hist[m].items())} for m in gaps}, {'source_residues':len(M),'source_slots':2*p*p,'index_builds':len(bucket_cache)}

def verify():
    cases=0
    for p in range(4,9):
        for k in range(1,(1<<(p-1))-2,2):
            result,_=count(p,k)
            for m in (1,3,5):
                direct=direct_small(p,k,m)
                assert result[m].get('named_mass',0)==sum(direct.values()),(p,k,m)
                assert result[m]['distinct_modulus_pairs']==len({(v[0],v[1]) for v in direct}),(p,k,m)
                groups=Counter()
                for row,n in direct.items():groups[row[:4]]+=n
                hist=Counter(groups.values())
                assert hist=={int(w):n for w,n in result[m]['weight_histogram'].items() if int(w)>0},(p,k,m,'histogram')
                cases+=1
    return cases

def main():
    small=verify()
    result,metadata=count(19,21)
    matched=[]
    for m,(np,nw) in EXPECTED.items():
        named,_,h=mjoin(19,21,m)
        assert result[m]['named_mass']==nw==len(named)
        assert result[m]['distinct_modulus_pairs']==np
        groups=Counter(row[:4] for row in named)
        observed=Counter(groups.values())
        assert observed=={int(w):n for w,n in result[m]['weight_histogram'].items() if int(w)>0},m
        matched.append({'gap':m,**result[m],'named_sha256_reference':h})
    times={'count':[],'named':[]}
    for repeat in range(10):
        for method in (('count','named') if repeat%2==0 else ('named','count')):
            start=perf_counter()
            if method=='count':count(19,21)
            else:
                for m in (1,3,5):mjoin(19,21,m)
            times[method].append(perf_counter()-start)
    answer={'schema':'PREFIX973_MASK_MASS_OBSERVER_V1','frozen_pin':PIN,'small_raw_xor_cases':small,'q19':matched,
            'mask_cache':metadata,'benchmark_median_seconds':{mode:median(ts) for mode,ts in times.items()},
            'benchmark_note':'10 alternating complete 3-gap executions; count path omits named recovery and sorting; not a like-for-like full-output speedup',
            'status':'AUTHOR_PROOF_EXACT_INTEGER_VERIFIED_NOT_REVIEWED'}
    with open('PREFIX973_R6_EXACT_RESULTS.json','w') as f:json.dump(answer,f,indent=2);f.write('\n')
    print(json.dumps(answer,indent=2))

if __name__=='__main__': main()
