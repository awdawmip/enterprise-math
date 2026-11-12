#!/usr/bin/env python3
"""R5 original-frozen 1065-word corpus: arbitrary-order offline Fenwick and online ancestor-wall ranks.
Run from stacked branch; predecessor imports and fully verifies the pinned corpus.
New verification is exact Fraction arithmetic. Timers are indicative only.
"""
from fractions import Fraction as F
from bisect import bisect_right
from pathlib import Path
from random import Random
from time import perf_counter
import sys, json

base = Path(__file__).resolve().parents[1] / "brc_r5_batch_from_seed_20261112"
sys.path.insert(0,str(base))
import VERIFY_R5_BATCH_FROM_PINNED as prev

N=prev.N
term=prev.term
M=sum(term)
parent=prev.parent
events=prev.events
pairs=prev.pairs
term_nodes=prev.terminal_ids
assert (N,M,len(events),len(set(t for t,_ in events)))==(2880,1065,1065,953)
terminal_rank={node:k for k,node in enumerate(term_nodes)}
end=[i+1 for i in range(N)]
for i in range(N-1,0,-1):
    p=parent[i]
    if end[p]<end[i]:end[p]=end[i]
cumulative=[0]
for bit in term:cumulative.append(cumulative[-1]+bit)
lohi=[(cumulative[i],cumulative[end[i]]) for i in range(N)]

class BIT:
    def __init__(self,n):self.n=n;self.t=[0]*(n+1)
    def add(self,i):
        i+=1
        while i<=self.n:self.t[i]+=1;i+=i&-i
    def prefix(self,i):
        s=0
        while i:s+=self.t[i];i-=i&-i
        return s
    def interval(self,lo,hi):return self.prefix(hi)-self.prefix(lo)

def offline(requests):
    b=BIT(M);out=[0]*len(requests);ptr=0
    for j,(v,r) in sorted(enumerate(requests),key=lambda a:a[1][1]):
        while ptr<M and events[ptr][0]<=r:
            b.add(terminal_rank[events[ptr][1]]);ptr+=1
        lo,hi=lohi[v];out[j]=b.interval(lo,hi)
    return out

node_walls=[[] for _ in range(N)]
for tau,i in events:node_walls[i].append(tau)
for i in range(N-1,0,-1):node_walls[parent[i]].extend(node_walls[i])
for a in node_walls:a.sort()
assert sum(map(len,node_walls))==7444
assert all(len(node_walls[i])==lohi[i][1]-lohi[i][0] for i in range(N))
def rank(i,r):return bisect_right(node_walls[i],r)
def scan(i,r):
    lo,hi=lohi[i]
    return sum(prev.active(q,n,r) for q,n in pairs[lo:hi])

requests=[(i,r) for r in prev.samples for i in range(N)]
exact=offline(requests)
assert len(exact)==57600
for (i,r),value in zip(requests,exact):
    assert value==rank(i,r)==prev.pinned.count(i,r)
for r in sorted(set(t for t,_ in events)):
    assert rank(0,r)==prev.pinned.count(0,r)

rng=Random(509197)
walls=sorted(set(t for t,_ in events))
pool=list(prev.samples)+walls+[F(-rng.randint(0,100),50) for _ in range(100)]
pool += [(walls[j]+walls[j+1])/2 for j in range(0,len(walls)-1,7)]
pool += [F(1,23)]
def workload(kind,K):
    rs=[pool[rng.randrange(len(pool))] for _ in range(K)]
    if kind=="root":ns=[0]*K
    elif kind=="broad":
        candidates=[i for i,(lo,hi) in enumerate(lohi) if hi-lo>=32]
        ns=[candidates[rng.randrange(len(candidates))] for _ in range(K)]
    else:ns=[rng.randrange(N) for _ in range(K)]
    return list(zip(ns,rs))

def timed(fn,rep=3):
    ts=[];checksum=None
    for _ in range(rep):
        t=perf_counter();v=fn();ts.append(perf_counter()-t)
        s=sum(v)
        if checksum is None:checksum=s
        assert checksum==s
    return round(sorted(ts)[len(ts)//2],6)

bench={}
for kind,K in (("root",256),("broad",512),("any",2048)):
    req=workload(kind,K)
    truth=[scan(i,r) for i,r in req]
    assert truth==offline(req)==[rank(i,r) for i,r in req]
    assert truth==[prev.pinned.count(i,r) for i,r in req]
    bench[kind]={
      "queries":K,
      "mean_terminal_window":round(sum(lohi[i][1]-lohi[i][0] for i,_ in req)/K,4),
      "checksum":sum(truth),
      "timings_seconds":{
        "wavelet":timed(lambda:[prev.pinned.count(i,r) for i,r in req]),
        "direct":timed(lambda:[scan(i,r) for i,r in req],1),
        "ancestor_rank":timed(lambda:[rank(i,r) for i,r in req]),
        "offline_fenwick":timed(lambda:offline(req))
      }
    }
mixed=workload("root",128)+workload("broad",128)+workload("any",128)
rng.shuffle(mixed)
assert offline(mixed)==[scan(i,r) for i,r in mixed]
print(json.dumps({
 "status":"PASS_R5_PINNED_BRANCH_OFFLINE_FENWICK_ANCESTOR_RANK",
 "terminals":M,"nodes":N,"unique_walls":len(walls),
 "threshold_references":sum(map(len,node_walls)),
 "full_exact_query_checks":len(requests),
 "root_wall_checks":len(walls),
 "mixed_exact_checks":len(mixed),
 "workloads":bench
},indent=2))
