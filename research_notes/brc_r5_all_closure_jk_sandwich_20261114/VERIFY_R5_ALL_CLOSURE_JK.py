#!/usr/bin/env python3
"""Exact R5 fixed-budget observer certificate across all 2**28 gap closures.
Derived 1D integer radius-2 event cover only; not native X6 / full BRC.
No external dependencies. Two independent exact DPs plus bounded brute force.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations
import json
import random

SCIENCE_PIN='435e77af0d180eac32bd1f9c4c464bc4010b7551'
W=(336,184,18,169,64,84,299,126,52,16,-420,-483,-144,-221,-80)
K0=(-432,0,0,0,0,-108,0,0,0,0,540,0,0,0,0)


def frozen():
    pools={3:set(),12:set(),15:set()};n=k=mask=0
    for t in range(1,1<<15):
        bit=t&-t;i=bit.bit_length()-1;mask^=bit
        sign=1 if mask&bit else -1
        n+=sign*W[i];k+=sign*K0[i]
        if n>=3 and k%36==0 and k//36 in pools:
            pools[k//36].add(n)
    assert [len(pools[q]) for q in (3,12,15)]==[538,298,229]
    events=Counter(Fraction(p,q) for q,values in pools.items() for p in values)
    x=[0]
    for value in sorted(events): x.append(x[-1]+events[value])
    cuts=[i for i in range(len(x)-1) if x[i+1]-x[i]>2]
    assert len(x)==954 and x[-1]==1065
    assert len(cuts)==28 and all(x[c+1]-x[c]==3 for c in cuts)
    return x,cuts


def closed_points(x,cuts,closed):
    positions={cuts[j] for j in closed};out=[];shift=0
    for i,value in enumerate(x):
        out.append(value-shift)
        if i in positions:shift+=1
    return out


def center_path_dp(x,max_k=None):
    """DP on consecutive chosen centers, with exact nearest-point edge costs."""
    n=len(x);r=2;infinity=10**12; max_k=max_k or n
    max_gap=max(x[j+1]-x[j] for j in range(n-1))
    incoming=[[] for _ in range(n)]
    for j in range(n):
        for i in range(j-1,-1,-1):
            if x[j]-x[i]>2*r+max_gap:break
            cost=0
            for t in range(i+1,j):
                d=min(x[t]-x[i],x[j]-x[t])
                if d>r:break
                cost+=d
            else:
                incoming[j].append((i,cost))
    dp=[infinity]*n
    for j in range(n):
        if x[j]-x[0]<=r:
            dp[j]=sum(x[j]-x[t] for t in range(j))
    out={}
    for k in range(1,max_k+1):
        if k>1:
            new=[infinity]*n
            for j in range(n):
                new[j]=min((dp[i]+c for i,c in incoming[j]),default=infinity)
            dp=new
        best=min((dp[i]+sum(x[t]-x[i] for t in range(i+1,n))
                  for i in range(n-1,-1,-1) if x[-1]-x[i]<=r),default=infinity)
        if best<infinity:out[k]=best
    return out


def contiguous_cluster_dp(x,max_k=None):
    """Independent DP: partition events into contiguous served clusters."""
    n=len(x);infinity=10**12; max_k=max_k or n
    candidates=[[] for _ in range(n+1)]
    for b in range(1,n+1):
        for a in range(b-1,-1,-1):
            if x[b-1]-x[a]>4:break
            best=infinity
            for j in range(a,b):
                if max(x[j]-x[a],x[b-1]-x[j])<=2:
                    best=min(best,sum(abs(x[t]-x[j]) for t in range(a,b)))
            if best<infinity:candidates[b].append((a,best))
    dp=[infinity]*(n+1);dp[0]=0;out={}
    for k in range(1,max_k+1):
        nxt=[infinity]*(n+1)
        for b in range(k,n+1):
            nxt[b]=min((dp[a]+c for a,c in candidates[b]),default=infinity)
        dp=nxt
        if dp[n]<infinity:out[k]=dp[n]
    return out


def small_brute(x):
    out={}
    for k in range(1,len(x)+1):
        costs=[]
        for centers in combinations(x,k):
            distances=[min(abs(p-c) for c in centers) for p in x]
            if max(distances)<=2:costs.append(sum(distances))
        if costs:out[k]=min(costs)
    return out


def main():
    random.seed(20261114)
    small=0
    for n in range(2,10):
        for _ in range(60):
            gaps=[random.randint(1,4) for j in range(n-1)]
            x=[0]
            for g in gaps:x.append(x[-1]+g)
            assert center_path_dp(x)==contiguous_cluster_dp(x)==small_brute(x)
            small+=1
    source,cuts=frozen()
    anchors={'none':(), 'all':tuple(range(28)),
             'without_8_9':tuple(i for i in range(28) if i not in (8,9)),
             'only_8':(8,), 'only_9':(9,)}
    results={}
    for name,indices in anchors.items():
        x=closed_points(source,cuts,indices)
        a=center_path_dp(x);b=contiguous_cluster_dp(x)
        assert a==b,(name,'independent DP mismatch')
        results[name]=a
    original=results['none'];full=results['all'];without=results['without_8_9']
    assert set(original)==set(range(213,955))
    assert set(full)==set(range(207,955))
    assert set(without)==set(range(208,955))
    assert all(original[k]==full[k] for k in range(214,955))
    assert (original[213],full[213],without[213],results['only_8'][213],
            results['only_9'][213])==(1070,1069,1070,1069,1069)
    assert all(original[k]==(1305-2*k if 315<=k<=350 else 954-k)
               for k in range(315,955))
    margins=Counter(original[k]-original[k+1] for k in range(213,954))
    assert margins=={6:1,5:8,4:70,3:23,2:36,1:603}
    # Direct tests are corroboration only; the all-pattern proof is the
    # monotonic sandwich using the five fully checked anchor spectra.
    sampled=0
    for _ in range(100):
        indices=tuple(i for i in range(28) if random.getrandbits(1))
        costs=center_path_dp(closed_points(source,cuts,indices),315)
        assert costs[213]==(1069 if (8 in indices or 9 in indices) else 1070)
        assert costs[214]==1064 and costs[315]==675
        sampled+=1
    output={
      'status':'PASS_EXACT_R5_ALL_CLOSURE_HIGH_BUDGET_SPECTRUM',
      'science_pin':SCIENCE_PIN,'scope':'derived one-dimensional radius-2 cover observer',
      'event_count':len(source),'cut_count':len(cuts),'closure_patterns':1<<28,
      'all_pattern_certificate':'monotonic sandwich between exactly solved anchors',
      'fixed_K_range':[214,954],'fixed_K_formula_from_315':
          {'315_to_350':'1305-2*K','351_to_954':'954-K'},
      'K_213':'1070 - int(cut8_closed or cut9_closed)',
      'anchors':{name:{'min_feasible_K':min(arr),'J_213':arr[213],
                       'J_214':arr[214],'J_315':arr[315],'J_351':arr[351],
                       'J_954':arr[954], 'spectrum_length':len(arr)}
                 for name,arr in results.items()},
      'original_margin_counts':dict(sorted(margins.items())),
      'small_sequences_exhaustive_subset_crosschecks':small,
      'independent_full_spectrum_DP_anchor_count':len(results),
      'random_closure_direct_crosschecks':sampled,
      'not_done':['full 2**28 brute force enumeration',
                  'exact J_K for partially closed patterns with K=207..212',
                  'native X6 / BRC performance benchmark',
                  'independent formal mathematical review']}
    print(json.dumps(output,indent=2,ensure_ascii=False))
    return output

if __name__=='__main__':main()
