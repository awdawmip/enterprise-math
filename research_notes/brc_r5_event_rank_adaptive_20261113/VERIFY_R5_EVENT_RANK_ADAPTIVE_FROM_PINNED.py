#!/usr/bin/env python3
"""R5 frozen 1065-terminal model: exact 953-wall rank carrier and adaptive cache.
Run on the stacked GitHub branch; the predecessor verifies the frozen input.
"""
from array import array
from bisect import bisect_right
from fractions import Fraction
from pathlib import Path
from random import Random
from time import perf_counter
import json, sys

base=Path(__file__).resolve().parents[1]/"brc_r5_offline_fenwick_20261112"
sys.path.insert(0,str(base))
import VERIFY_R5_OFFLINE_FENWICK_FROM_PINNED as prev

N,M=prev.N,prev.M
assert (N,M)==(2880,1065)
walls=sorted(set(t for t,_ in prev.events))
assert len(walls)==953
wall_code={w:i for i,w in enumerate(walls)}
codes=array("H",[0]*M)
for tau,node in prev.events:
    codes[prev.terminal_rank[node]]=wall_code[tau]
assert len(codes)==M and codes.itemsize==2
assert all(codes[i]==wall_code[(1-Fraction(36*q,n))/23]
           for i,(q,n) in enumerate(prev.pairs))

def count_direct(v,r):
    bound=bisect_right(walls,r)
    lo,hi=prev.lohi[v]
    return sum(c<bound for c in codes[lo:hi])

class Adaptive:
    def __init__(self, minimum=16, second_hit=2):
        self.minimum=minimum
        self.second_hit=second_hit
        self.hits={}
        self.cache={}
    def count(self,v,r):
        bound=bisect_right(walls,r)
        row=self.cache.get(v)
        if row is not None:
            return bisect_right(row,bound-1)
        lo,hi=prev.lohi[v]
        if hi-lo>=self.minimum:
            hits=self.hits.get(v,0)+1
            if hits>=self.second_hit:
                row=array("H",sorted(codes[lo:hi]))
                self.cache[v]=row
                self.hits.pop(v,None)
                return bisect_right(row,bound-1)
            self.hits[v]=hits
        return sum(c<bound for c in codes[lo:hi])

model=Adaptive()
checks=0
for r in prev.prev.samples:
    for v in range(N):
        truth=prev.prev.pinned.count(v,r)
        assert count_direct(v,r)==truth
        assert model.count(v,r)==truth
        checks+=1
assert checks==57600
for tau in walls:
    assert count_direct(0,tau)==prev.prev.pinned.count(0,tau)

rng=Random(20261113)
pool=list(prev.prev.samples)+walls
pool += [Fraction(-rng.randrange(0,100),50) for _ in range(100)]
pool += [(walls[i]+walls[i+1])/2 for i in range(0,len(walls)-1,11)]
broad=[i for i,(a,b) in enumerate(prev.lohi) if b-a>=32]

def workload(kind,k):
    if kind=="root": nodes=[0]*k
    elif kind=="broad": nodes=[broad[rng.randrange(len(broad))] for _ in range(k)]
    elif kind=="hotmix":
        hot=[0]+broad[:18]
        nodes=[hot[rng.randrange(len(hot))] if rng.randrange(4)
               else rng.randrange(N) for _ in range(k)]
    else: nodes=[rng.randrange(N) for _ in range(k)]
    return list(zip(nodes,(pool[rng.randrange(len(pool))] for _ in range(k))))

def run_timed(fn,repeats=3):
    durations=[];checksum=None
    for _ in range(repeats):
        start=perf_counter()
        result=fn()
        dt=perf_counter()-start
        s=sum(result)
        if checksum is None:checksum=s
        assert s==checksum
        durations.append(dt)
    return round(sorted(durations)[len(durations)//2],6),checksum

report={}
for kind,k in (("root",256),("broad",512),("random",2048),("hotmix",2048)):
    requests=workload(kind,k)
    correct=[prev.prev.pinned.count(v,r) for v,r in requests]
    assert correct==[count_direct(v,r) for v,r in requests]
    cache=Adaptive()
    t0=perf_counter()
    cold=[cache.count(v,r) for v,r in requests]
    cold_time=perf_counter()-t0
    assert cold==correct
    warm_time,_=run_timed(lambda:[cache.count(v,r) for v,r in requests])
    direct_time,_=run_timed(lambda:[count_direct(v,r) for v,r in requests])
    report[kind]={"requests":k,"checksum":sum(correct),
        "unique_nodes":len(set(v for v,r in requests)),
        "direct_seconds":direct_time,
        "lazy_cold_seconds":round(cold_time,6),
        "lazy_warm_seconds":warm_time,
        "materialized_nodes":len(cache.cache),
        "materialized_codes":sum(map(len,cache.cache.values())),
        "raw_cache_bytes":sum(len(a)*a.itemsize for a in cache.cache.values())}

all_rows=[array("H",sorted(codes[a:b])) for a,b in prev.lohi]
assert sum(map(len,all_rows))==7444
for r in prev.prev.samples:
    rank=bisect_right(walls,r)-1
    for v in range(N):
        assert bisect_right(all_rows[v],rank)==prev.prev.pinned.count(v,r)

print(json.dumps({"status":"PASS_R5_EVENT_RANK_ADAPTIVE_BRANCH",
    "scientific_input_pin":"435e77af0d180eac32bd1f9c4c464bc4010b7551",
    "nodes":N,"terminals":M,"distinct_walls":len(walls),
    "minimum_code_width_bits":len(walls).bit_length(),
    "terminal_codes_16bit_bytes":len(codes)*codes.itemsize,
    "all_ancestor_code_references":sum(map(len,all_rows)),
    "all_ancestor_raw_code_bytes":sum(len(a)*a.itemsize for a in all_rows),
    "full_prefix_checks":checks,"root_wall_checks":len(walls),
    "workloads":report},ensure_ascii=False,indent=2))
