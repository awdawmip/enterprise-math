#!/usr/bin/env python3
"""Portable R5 minimax wall-event weighted sampled bitmap verifier; Python stdlib.
Run on stacked PR ancestry including brc_r5_offline_fenwick_20261112.
Imports and re-verifies the frozen original rational fixture, not synthetic records.
"""
from bisect import bisect_left,bisect_right
from fractions import Fraction
from pathlib import Path
from statistics import median
from time import perf_counter
import json,random,sys

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"brc_r5_offline_fenwick_20261112"))
import VERIFY_R5_OFFLINE_FENWICK_FROM_PINNED as prev
N,M,walls,pairs,lohi=prev.N,prev.M,prev.walls,prev.pairs,prev.lohi
W=len(walls)
assert (N,M,W)==(2880,1065,953)
wid={w:i for i,w in enumerate(walls)}
codes=[wid[(1-Fraction(36*q,n))/23] for q,n in pairs]
freq=[0]*W
for c in codes:freq[c]+=1
E=[0]
for n in freq:E.append(E[-1]+n)
assert E[-1]==M and max(freq)==3
order=sorted(range(M),key=lambda i:(codes[i],i))

def greedy(radius):
    selected=[];left=0
    while left<=W:
        j=bisect_right(E,E[left]+radius)-1
        assert j>=left
        selected.append(j)
        left=bisect_right(E,E[j]+radius)
    return selected

def solve(budget):
    low,high=0,M
    while low<high:
        mid=(low+high)//2
        if len(greedy(mid))<=budget: high=mid
        else:low=mid+1
    assert low==0 or len(greedy(low-1))>budget
    result=greedy(low)
    assert len(result)<=budget
    return low,result

class Index:
    def __init__(self,bounds):
        self.bounds=sorted(set(bounds))
        self.coord=[E[b] for b in self.bounds]
        self.masks=[]
        bits=0;j=0
        for b in self.bounds:
            while j<E[b]:
                bits|=1<<order[j];j+=1
            self.masks.append(bits)
    def event_cost(self,b,nearest):
        if nearest:return min(abs(E[b]-x) for x in self.coord)
        s=bisect_right(self.bounds,b)-1
        assert s>=0
        return E[b]-E[self.bounds[s]]
    def count_b(self,node,b,nearest):
        lo,hi=lohi[node]
        if lo==hi:return 0
        if nearest:
            x=E[b];j=bisect_left(self.coord,x)
            if j==0:p=0
            elif j==len(self.coord):p=j-1
            else:p=j if self.coord[j]-x<E[b]-self.coord[j-1] else j-1
        else:
            p=bisect_right(self.bounds,b)-1
            assert p>=0
        mask=self.masks[p];s=self.bounds[p]
        if s<b:
            for j in range(E[s],E[b]):mask|=1<<order[j]
        elif s>b:
            for j in range(E[b],E[s]):mask &= ~(1<<order[j])
        return ((mask>>lo)&((1<<(hi-lo))-1)).bit_count()
    def count(self,node,r,nearest):
        return self.count_b(node,bisect_right(walls,r),nearest)

rows=[];indices={}
for B in (1,2,4,8,16,32,64):
    uniform=list(range(0,W+1,B));K=len(uniform)
    R,centers=solve(K)
    original=Index(uniform);weighted=Index(centers)
    bmax=max(original.event_cost(b,False) for b in range(W+1))
    nmax=max(original.event_cost(b,True) for b in range(W+1))
    wmax=max(weighted.event_cost(b,True) for b in range(W+1))
    assert R==wmax and R<=nmax
    indices[B]=(original,weighted)
    rows.append(dict(stride=B,budget=K,weighted_centers=len(centers),
       one_sided_max=bmax,nearest_uniform_max=nmax,optimum_worst=R))

# 57,600 cases per scheme are validated with the independent frozen pinned oracle.
checks=0
for r in prev.prev.samples:
    b=bisect_right(walls,r)
    for node,(lo,hi) in enumerate(lohi):
        expected=prev.prev.pinned.count(node,r)
        assert expected==sum(c<b for c in codes[lo:hi])
        for B,(original,weighted) in indices.items():
            assert original.count_b(node,b,False)==expected,(B,node,r,"original")
            assert weighted.count_b(node,b,True)==expected,(B,node,r,"weighted")
        checks+=1
assert checks==57600
for r in walls:
    b=bisect_right(walls,r)
    expected=prev.prev.pinned.count(0,r)
    for original,weighted in indices.values():
        assert original.count_b(0,b,False)==expected
        assert weighted.count_b(0,b,True)==expected
assert len(walls)==953

# Exhaust all b values for all nodes for the K=239 minimax constructor.
all_boundaries=0
weighted=indices[4][1]
for b in range(W+1):
    for node,(lo,hi) in enumerate(lohi):
        assert weighted.count_b(node,b,True)==sum(c<b for c in codes[lo:hi])
        all_boundaries+=1
assert all_boundaries==2747520

rng=random.Random(2026111304)
pool=list(prev.prev.samples)+walls+[(walls[i]+walls[i+1])/2 for i in range(0,W-1,11)]
large=[i for i,(l,h) in enumerate(lohi) if h-l>=32]
bench={}
for kind,count in (("root",256),("broad",512),("random",2048),("hotmix",2048)):
    if kind=="root":nodes=[0]*count
    elif kind=="broad":nodes=[rng.choice(large) for _ in range(count)]
    elif kind=="random":nodes=[rng.randrange(N) for _ in range(count)]
    else:
        hot=[0]+large[:18]
        nodes=[rng.choice(hot) if rng.randrange(4) else rng.randrange(N) for _ in range(count)]
    queries=list(zip(nodes,(rng.choice(pool) for _ in range(count))))
    expected=[sum(c<bisect_right(walls,r) for c in codes[lohi[v][0]:lohi[v][1]]) for v,r in queries]
    times={}
    for B in (4,16,64):
        for label,idx,nearest in (("uniform",indices[B][0],False),("weighted",indices[B][1],True)):
            assert [idx.count(v,r,nearest) for v,r in queries]==expected
            durations=[]
            for _ in range(5):
                st=perf_counter();check=sum(idx.count(v,r,nearest) for v,r in queries)
                assert check==sum(expected)
                durations.append(1000*(perf_counter()-st))
            times[label+"_"+str(B)]=round(median(durations),3)
    bench[kind]=dict(count=count,checksum=sum(expected),median_ms=times)
print(json.dumps({"status":"PASS_R5_WEIGHTED_MINIMAX_PINNED",
"scientific_pin":"435e77af0d180eac32bd1f9c4c464bc4010b7551",
"nodes":N,"terminals":M,"walls":W,"max_multiplicity":max(freq),
"prefix_sample_checks":checks,"root_wall_checks":W,
"complete_b_node_checks_K239":all_boundaries,
"minimax":rows,"query_timings":bench},indent=2))
