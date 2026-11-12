#!/usr/bin/env python3
"""R5 exact bit-sliced wall-rank query on the immutable pinned original certificate chain.

Run on stacked branch research/r5-bitplane-rank-20261113-0140.
The imported predecessor reconstructs and checks the frozen 28-coordinate corpus.
"""
from __future__ import annotations
from bisect import bisect_right
from fractions import Fraction as F
from pathlib import Path
from random import Random
from time import perf_counter
import json, statistics, sys

base=Path(__file__).resolve().parents[1]/"brc_r5_event_rank_adaptive_20261113"
sys.path.insert(0,str(base))
import VERIFY_R5_EVENT_RANK_ADAPTIVE_FROM_PINNED as prev

N,M=prev.N,prev.M
walls=prev.walls
codes=prev.codes
lohi=prev.prev.lohi
W=len(walls)
width=(W-1).bit_length()
assert (N,M,W,width)==(2880,1065,953,10)

planes=[0]*width
for i,k in enumerate(codes):
    for d in range(width):
        if (k>>d)&1:planes[d]|=1<<i

def count_plane(v,r):
    lo,hi=lohi[v]
    b=bisect_right(walls,r)
    if b<=0:return 0
    if b>=W:return hi-lo
    eq=((1<<(hi-lo))-1)<<lo
    less=0
    for d in range(width-1,-1,-1):
        one=planes[d]
        zero=eq&~one
        if (b>>d)&1:
            less|=zero
            eq &= one
        else:
            eq=zero
    return less.bit_count()

def count_direct(v,r):
    b=bisect_right(walls,r)
    lo,hi=lohi[v]
    return sum(k<b for k in codes[lo:hi])

def count_hybrid(v,r,cutoff=8):
    lo,hi=lohi[v]
    if hi-lo<cutoff:return count_direct(v,r)
    return count_plane(v,r)

# Exact original corpus: 2880 nodes * 20 fractional probes + all wall ties.
checks=0
for r in prev.prev.prev.samples:
    for v in range(N):
        exact=prev.prev.prev.pinned.count(v,r)
        assert count_plane(v,r)==exact
        assert count_hybrid(v,r)==exact
        checks+=1
assert checks==57600
for tau in walls:
    assert count_plane(0,tau)==prev.prev.prev.pinned.count(0,tau)

# Independent finite exhaustive bit-comparator logic over 3^n arrays, n<=6.
small_checks=0
for n in range(1,7):
    for case in range(3**n):
        a=[];s=case
        for _ in range(n):a.append(s%3);s//=3
        mini=[sum(((x>>d)&1)<<i for i,x in enumerate(a)) for d in range(2)]
        for lo in range(n):
            for hi in range(lo+1,n+1):
                for b in range(5):
                    eq=((1<<(hi-lo))-1)<<lo;less=0
                    for d in (1,0):
                        zero=eq&~mini[d]
                        if (b>>d)&1:less|=zero;eq&=mini[d]
                        else:eq=zero
                    observed=hi-lo if b==4 else less.bit_count()
                    assert observed==sum(x<b for x in a[lo:hi])
                    small_checks+=1
assert small_checks==99780

rng=Random(20261113)
pool=list(prev.prev.prev.samples)+list(walls)+[F(-rng.randrange(0,100),50) for _ in range(100)]
pool += [(walls[i]+walls[i+1])/2 for i in range(0,W-1,11)]
large=[i for i,(a,b) in enumerate(lohi) if b-a>=32]

def workload(kind,k):
    if kind=="root":nodes=[0]*k
    elif kind=="broad":nodes=[large[rng.randrange(len(large))] for _ in range(k)]
    elif kind=="random":nodes=[rng.randrange(N) for _ in range(k)]
    else:
        hot=[0]+large[:18]
        nodes=[hot[rng.randrange(len(hot))] if rng.randrange(4) else rng.randrange(N) for _ in range(k)]
    return list(zip(nodes,(pool[rng.randrange(len(pool))] for _ in range(k))))

def bench(fn,req):
    seconds=[]
    checksum=None
    for _ in range(5):
        t=perf_counter()
        s=sum(fn(v,r) for v,r in req)
        seconds.append(perf_counter()-t)
        if checksum is not None:assert checksum==s
        checksum=s
    return round(statistics.median(seconds),6),checksum

loads={}
for kind,k in (("root",256),("broad",512),("random",2048),("hotmix",2048)):
    req=workload(kind,k)
    exact=[prev.prev.prev.pinned.count(v,r) for v,r in req]
    times={}
    for name,func in (("direct",count_direct),("bitsliced",count_plane),("hybrid_8",count_hybrid)):
        assert [func(v,r) for v,r in req]==exact
        seconds,total=bench(func,req)
        assert total==sum(exact)
        times[name]=seconds
    loads[kind]={"requests":k,"checksum":sum(exact),"median_query_seconds":times}

print(json.dumps({"status":"PASS_R5_BITSLICED_RANK_PINNED_BRANCH",
    "scientific_input_pin":"435e77af0d180eac32bd1f9c4c464bc4010b7551",
    "trie_nodes":N,"terminal_certificates":M,"distinct_rational_walls":W,
    "bitplanes":width,"bitplane_logical_bits":width*M,
    "exact_prefix_checks":checks,"exact_root_wall_ties":W,
    "small_exhaustive_checks":small_checks,"workloads":loads,
    "note":"Branch program independently executable on its own stacked dependency tree; benchmark times depend on runtime."},
    indent=2,ensure_ascii=False))
