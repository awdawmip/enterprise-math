#!/usr/bin/env python3
"""Exact pinned R5 event-wall covering class and reversible rank.
Standard-library Python. Source: enterprise-math frozen 435e77af0d180eac32bd1f9c4c464bc4010b7551.
This rederives the original event walls from 15-atom k0/k1 coefficients.
The earlier 28-coordinate legal-word census remains a cited premise.
"""
from collections import Counter
from fractions import Fraction
from bisect import bisect_left,bisect_right
from hashlib import sha256
from time import perf_counter
from tracemalloc import start as memory_start,get_traced_memory,stop as memory_stop
import json

W=(336,184,18,169,64,84,299,126,52,16,-420,-483,-144,-221,-80)
K=(-432,0,0,0,0,-108,0,0,0,0,540,0,0,0,0)
ORIG56_HEX='d500a95a516544511a50596555556a5a441665a66a9195956669611456565551aa5669aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa6a00'
raw=bytes.fromhex(ORIG56_HEX)
assert len(raw)==56 and sha256(raw).hexdigest()=='bf4f377e8a3b9823d589d0f5c5b0b5973f374a09aa986d5b729bc695c5de0326'

pairs={3:set(),12:set(),15:set()}
for mask in range(1,1<<15):
    n=-sum(W[j] for j in range(15) if mask&(1<<j))
    k=-sum(K[j] for j in range(15) if mask&(1<<j))
    if n>=3 and k%36==0 and k//36 in pairs:pairs[k//36].add(n)
assert {q:len(v) for q,v in pairs.items()}=={3:538,12:298,15:229}
assert sum(map(len,pairs.values()))==1065
walls=Counter((Fraction(1,1)-Fraction(36*q,n))/23 for q,nn in pairs.items() for n in nn)
assert len(walls)==953 and Counter(walls.values())==Counter({1:869,2:56,3:28})
thresholds=sorted(walls)
E=[0]
for r in thresholds:E.append(E[-1]+walls[r])
assert len(E)==954 and E[-1]==1065
assert sum(1 for q,nn in pairs.items() for n in nn if n<=36*q)==605

bits=int.from_bytes(raw[2:],'little')
centers=[bits&3];bits>>=2
for _ in range(212):
    gap_symbol=bits&3;bits>>=2
    assert gap_symbol<3
    centers.append(centers[-1]+3+gap_symbol)
assert bits==0 and len(centers)==213 and centers[0]==1 and centers[-1]==952
assert Counter(centers[i+1]-centers[i] for i in range(212))=={3:16,4:77,5:119}
R=2; Kc=213; N=len(E)
residuals=[min(abs(e-E[s]) for s in centers) for e in E]
assert max(residuals)==R and sum(residuals)==1070

starts=[p for p in range(N) if E[p]-E[0]<=R]
ends=[p for p in range(N) if E[-1]-E[p]<=R]
upper=[bisect_right(E,E[p]+R)-1 for p in range(N)]
lower=[bisect_left(E,E[p]-R) for p in range(N)]
edges=[[] for _ in range(N)]
for p in range(N):
    for q in range(p+1,min(N,p+2*R+2)):
        if lower[q]<=upper[p]+1:
            edges[p].append(q)
            assert all(min(E[b]-E[p],E[q]-E[b])<=R for b in range(p,q+1))
assert all(centers[j+1] in edges[centers[j]] for j in range(Kc-1))

memory_start(); begin=perf_counter()
F=[[0]*N for _ in range(Kc+1)]
for p in ends:F[1][p]=1
for t in range(2,Kc+1):
    prev=F[t-1];curr=F[t]
    for p in range(N-1,-1,-1):curr[p]=sum(prev[q] for q in edges[p])
T=sum(F[Kc][p] for p in starts)
backward_sec=perf_counter()-begin
peak_bytes=get_traced_memory()[1];memory_stop()
assert T>0

# Second independent count: propagate from starts forward.
D=[0]*N
for p in starts:D[p]=1
for t in range(2,Kc+1):
    nxt=[0]*N
    for p,ways in enumerate(D):
        if ways:
            for q in edges[p]:nxt[q]+=ways
    D=nxt
T2=sum(D[p] for p in ends)
assert T2==T

rank=sum(F[Kc][p] for p in starts if p<centers[0])
for j,(p,q) in enumerate(zip(centers,centers[1:])):
    rank+=sum(F[Kc-1-j][a] for a in edges[p] if a<q)
assert centers[-1] in ends and 0<=rank<T
remainder=rank
restored=[]
for p in starts:
    block=F[Kc][p]
    if remainder<block:
        restored=[p];break
    remainder-=block
for t in range(Kc-1,0,-1):
    for q in edges[restored[-1]]:
        block=F[t][q]
        if remainder<block:
            restored.append(q);break
        remainder-=block
    else:raise AssertionError('Invalid suffix rank')
assert restored==centers and remainder==0

width=(T-1).bit_length(); size=(width+7)//8
code=rank.to_bytes(size,'big')
assert len(code)==17 and int.from_bytes(code,'big')==rank
assert T>1<<128 and T<=1<<136
out={
 'status':'PASS_EXACT_PINNED_R5_EVENT_COVER_CLASS',
 'frozen_scientific_source_commit':'435e77af0d180eac32bd1f9c4c464bc4010b7551',
 'distinct_qn_counts':{str(q):len(ns) for q,ns in sorted(pairs.items())},
 'distinct_pairs':sum(map(len,pairs.values())),
 'distinct_walls':len(walls),'boundaries':len(E),
 'wall_group_multiplicity_histogram':{str(k):v for k,v in sorted(Counter(walls.values()).items())},
 'total_events':E[-1],'root_activated_at_r0':605,
 'historical_centers':len(centers),'first_center':centers[0],'last_center':centers[-1],
 'center_gap_histogram':{str(k):v for k,v in sorted(Counter(b-a for a,b in zip(centers,centers[1:])).items())},
 'radius':R,'historical_max_correction':max(residuals),'historical_total_correction':sum(residuals),
 'edge_count':sum(map(len,edges)),'admissible_starts':starts,'admissible_ends':ends,
 'legal_center_sets':str(T),'second_DP_agrees':T2==T,
 'rank_of_historical_centers':str(rank),'capacity_bits':width,'capacity_bytes':size,
 'rank_be_17byte_hex':code.hex(),'rank_sha256':sha256(code).hexdigest(),
 'rank_unrank_identical_historical_centers':restored==centers,
 'event_increments_sha256':sha256(bytes(walls[r] for r in thresholds)).hexdigest(),
 'backward_DP_elapsed_seconds':round(backward_sec,6),
 'backward_DP_tracemalloc_peak_bytes':peak_bytes,
 'scope':'Frozen R5 auxiliary dual-zero event-wall/index model; independent k0/k1 event reconstruction, not full 28-coordinate path admissibility or native X6 dynamics.'
}
print(json.dumps(out,sort_keys=True,indent=2))
