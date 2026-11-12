#!/usr/bin/env python3
"""Exact sampled activation bitmaps on the frozen R5 certificate set.

Stacked on research/r5-bitplane-rank-20261113-0140. Uses the pinned original
28-coordinate source via its offline-Fenwick verifier. Python stdlib only.
"""
from array import array
from bisect import bisect_right
from fractions import Fraction as F
from pathlib import Path
from random import Random
from statistics import median
from time import perf_counter
import json
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] /
                       "brc_r5_offline_fenwick_20261112"))
import VERIFY_R5_OFFLINE_FENWICK_FROM_PINNED as prev

N, M = prev.N, prev.M
walls = prev.walls
W = len(walls)
pairs = prev.pairs
lohi = prev.lohi
assert (N, M, W) == (2880, 1065, 953)
wall_id = {w: i for i, w in enumerate(walls)}
codes = array("H", [wall_id[(1-F(36*q,n))/23] for q,n in pairs])
order = array("H", sorted(range(M), key=lambda i: (codes[i],i)))
frequency = [0] * W
for code in codes:
    frequency[code] += 1
offsets = array("H", [0])
for count in frequency:
    offsets.append(offsets[-1] + count)
assert offsets[-1] == M

class Sampled:
    def __init__(self, stride):
        self.stride = stride
        self.snapshots = []
        mask = 0
        idx = 0
        for bound in range(0, W+1, stride):
            while idx < offsets[bound]:
                mask |= 1 << order[idx]
                idx += 1
            self.snapshots.append(mask)

    def count(self, node, r):
        b = bisect_right(walls, r)
        if b == 0:
            return 0
        lo, hi = lohi[node]
        if hi == lo:
            return 0
        block = b // self.stride
        mask = self.snapshots[block]
        for j in range(offsets[block*self.stride], offsets[b]):
            mask |= 1 << order[j]
        return ((mask >> lo) & ((1 << (hi-lo))-1)).bit_count()

    def runtime_mask_object_bytes(self):
        return sys.getsizeof(self.snapshots) + sum(sys.getsizeof(x) for x in self.snapshots)

strides = (1,2,4,8,16,32,64)
indexes = {b: Sampled(b) for b in strides}

# Complete frozen prefix and rational-wall equality checks.
cases = 0
for r in prev.prev.samples:
    for node in range(N):
        expected = prev.prev.pinned.count(node, r)
        for stride in strides:
            assert indexes[stride].count(node,r) == expected, (stride,node,r)
        cases += 1
assert cases == 57600
for r in walls:
    expected = prev.prev.pinned.count(0,r)
    for stride in strides:
        assert indexes[stride].count(0,r) == expected

# The previous 10-plane hybrid is an exact comparator on the same corpus.
width = (W-1).bit_length()
planes = [sum(((int(c)>>d)&1)<<i for i,c in enumerate(codes))
          for d in range(width)]

def direct(node,r):
    left,right = lohi[node]
    bound = bisect_right(walls,r)
    return sum(int(c)<bound for c in codes[left:right])

def bitsliced(node,r):
    left,right = lohi[node]
    bound = bisect_right(walls,r)
    if bound<=0: return 0
    if bound>=W: return right-left
    eq=((1 << (right-left))-1)<<left
    less=0
    for d in range(width-1,-1,-1):
        zero=eq & ~planes[d]
        if (bound>>d)&1:
            less |= zero
            eq &= planes[d]
        else:
            eq = zero
    return less.bit_count()

def hybrid(node,r):
    left,right=lohi[node]
    return direct(node,r) if right-left<8 else bitsliced(node,r)

rng=Random(20261113)
pool=list(prev.prev.samples)+list(walls)
pool += [F(-rng.randrange(0,100),50) for _ in range(100)]
pool += [(walls[i]+walls[i+1])/2 for i in range(0,W-1,11)]
large=[i for i,(a,b) in enumerate(lohi) if b-a>=32]

def workload(kind,k):
    if kind=="root": nodes=[0]*k
    elif kind=="broad": nodes=[large[rng.randrange(len(large))] for _ in range(k)]
    elif kind=="random": nodes=[rng.randrange(N) for _ in range(k)]
    elif kind=="hotmix":
        hot=[0]+large[:18]
        nodes=[hot[rng.randrange(len(hot))] if rng.randrange(4)
               else rng.randrange(N) for _ in range(k)]
    else: raise ValueError(kind)
    return list(zip(nodes,(pool[rng.randrange(len(pool))] for _ in range(k))))

def bench(func,request):
    durations=[]
    expected=None
    for _ in range(5):
        start=perf_counter()
        checksum=sum(func(v,r) for v,r in request)
        durations.append(1000*(perf_counter()-start))
        if expected is not None: assert checksum==expected
        expected=checksum
    return round(median(durations),3), expected

loads={}
for kind,k in (("root",256),("broad",512),("random",2048),("hotmix",2048)):
    req=workload(kind,k)
    exact=[prev.prev.pinned.count(v,r) for v,r in req]
    funcs=[("hybrid8",hybrid),("scan",direct)]
    funcs.extend((f"bitmap_{b}",indexes[b].count) for b in strides)
    times={}
    for name,fun in funcs:
        assert [fun(v,r) for v,r in req] == exact
        duration,s=bench(fun,req)
        assert s==sum(exact)
        times[name]=duration
    loads[kind]={"requests":k,"unique_nodes":len({v for v,_ in req}),
                 "checksum":sum(exact),"median_ms":times}

report={
 "status":"PASS_R5_SAMPLED_BITMAP_PINNED",
 "scientific_input_pin":"435e77af0d180eac32bd1f9c4c464bc4010b7551",
 "nodes":N,"terminals":M,"distinct_walls":W,
 "prefix_parameter_checks":cases,"root_wall_ties":W,
 "max_tied_wall_multiplicity":max(frequency),
 "event_positions_uint16_bytes":2*len(order),
 "wall_offsets_uint16_bytes":2*len(offsets),
 "index":[{
     "stride":b,"snapshots":len(indexes[b].snapshots),
     "snapshot_python_object_bytes":indexes[b].runtime_mask_object_bytes(),
     "maximum_tail_events":max(offsets[x]-offsets[(x//b)*b]
                                for x in range(W+1))}
     for b in strides],
 "workloads":loads,
 "timing_scope":"Five CPython same-process medians, includes exact rational bisect; excludes corpus/seed rebuild; snapshot sizes exclude event-order/offset/wall/fixture heaps."
}
print(json.dumps(report,ensure_ascii=False,indent=2))
