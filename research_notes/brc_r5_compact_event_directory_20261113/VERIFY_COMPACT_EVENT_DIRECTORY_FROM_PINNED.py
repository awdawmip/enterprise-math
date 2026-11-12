#!/usr/bin/env python3
"""R5 complete-wall event-count quotient; portable exact verifier on the stacked frozen ancestry."""
from array import array
from bisect import bisect_left,bisect_right
from fractions import Fraction
from pathlib import Path
from statistics import median
from time import perf_counter
import json,random,sys

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"brc_r5_offline_fenwick_20261112"))
import VERIFY_R5_OFFLINE_FENWICK_FROM_PINNED as P

N,M,walls,pairs,lohi=P.N,P.M,P.walls,P.pairs,P.lohi
assert (N,M,len(walls))==(2880,1065,953)
wi={w:i for i,w in enumerate(walls)}
codes=[wi[(1-Fraction(36*q,n))/23] for q,n in pairs]
order=sorted(range(M),key=lambda i:(codes[i],i))
freq=[0]*len(walls)
for c in codes:freq[c]+=1
E=[0]
for v in freq:E.append(E[-1]+v)
assert E[-1]==M and max(freq)==3 and len(E)==954

def greedy(R):
    out=[];p=0
    while p<len(E):
        c=bisect_right(E,E[p]+R)-1
        out.append(c);p=bisect_right(E,E[c]+R)
    return out

def solve(K):
    l,h=0,M
    while l<h:
        mid=(l+h)//2
        if len(greedy(mid))<=K:h=mid
        else:l=mid+1
    return l,greedy(l)

def masks(coords):
    out=[];bitset=0;k=0
    for x in coords:
        while k<x:
            bitset|=1<<order[k];k+=1
        out.append(bitset)
    return out

class Index:
    def __init__(self,bounds,compact):
        self.compact=compact
        if compact:
            # One complete-wall event count per checkpoint; no stored wall index.
            self.coords=array('H',(E[b] for b in bounds))
        else:
            self.bounds=list(bounds)
            self.coords=[E[b] for b in bounds]
        self.masks=masks(self.coords)
    def count(self,v,b):
        a,z=lohi[v]
        if a==z:return 0
        x=E[b];j=bisect_left(self.coords,x)
        if j==0:p=0
        elif j==len(self.coords):p=j-1
        else:p=j if self.coords[j]-x<x-self.coords[j-1] else j-1
        y=self.coords[p];bits=self.masks[p]
        if y<x:
            for i in range(y,x):bits|=1<<order[i]
        elif y>x:
            for i in range(x,y):bits &= ~(1<<order[i])
        return ((bits>>a)&((1<<(z-a))-1)).bit_count()
    def size(self):
        m=sys.getsizeof(self.masks)+sum(map(sys.getsizeof,self.masks))
        d=sys.getsizeof(self.coords)
        if not self.compact:
            d+=sys.getsizeof(self.bounds)+sum(map(sys.getsizeof,self.bounds))
            d+=sum(map(sys.getsizeof,self.coords))
        return m,d

R,bounds=solve(239)
assert (R,len(bounds))==(2,213)
old,compact=Index(bounds,False),Index(bounds,True)
uniform=Index(range(0,len(E),4),True)
assert old.coords==list(compact.coords) and old.masks==compact.masks
# Independent exact integer oracle for every wall boundary and node.
full=0
for b in range(len(E)):
    prefix=[0]
    for c in codes:prefix.append(prefix[-1]+(c<b))
    for v,(a,z) in enumerate(lohi):
        assert compact.count(v,b)==prefix[z]-prefix[a],(v,b)
        full+=1
assert full==2747520
checks=0
for r in P.prev.samples:
    b=bisect_right(walls,r)
    for v in range(N):
        assert compact.count(v,b)==P.prev.pinned.count(v,r),(v,r)
        checks+=1
assert checks==57600
# Fixed-seed same-request timing, query-only after import/build.
rng=random.Random(2026111304)
pool=list(P.prev.samples)+walls+[(walls[i]+walls[i+1])/2 for i in range(0,len(walls)-1,11)]
large=[i for i,(a,z) in enumerate(lohi) if z-a>=32]
bench={}
for kind,K in (("root",256),("broad",512),("random",2048),("hotmix",2048)):
    if kind=="root":nodes=[0]*K
    elif kind=="broad":nodes=[rng.choice(large) for _ in range(K)]
    elif kind=="random":nodes=[rng.randrange(N) for _ in range(K)]
    else:
        hot=[0]+large[:18]
        nodes=[rng.choice(hot) if rng.randrange(4) else rng.randrange(N) for _ in range(K)]
    qs=list(zip(nodes,(rng.choice(pool) for _ in range(K))))
    expect=[P.prev.pinned.count(v,r) for v,r in qs]
    times={}
    for label,idx in (("uniform_nearest",uniform),("weighted_lists",old),("weighted_uint16",compact)):
        assert [idx.count(v,bisect_right(walls,r)) for v,r in qs]==expect
        t=[]
        for _ in range(7):
            s=perf_counter()
            z=sum(idx.count(v,bisect_right(walls,r)) for v,r in qs)
            assert z==sum(expect)
            t.append((perf_counter()-s)*1000)
        times[label]=round(median(t),3)
    bench[kind]={"n":K,"checksum":sum(expect),"median_ms":times}
print(json.dumps({"status":"PASS_R5_EVENT_COUNT_COMPACT_PINNED",
  "scientific_pin":"435e77af0d180eac32bd1f9c4c464bc4010b7551",
  "nodes":N,"terminals":M,"walls":len(walls),"R":R,"centers":len(bounds),
  "all_boundary_node_checks":full,"fraction_wavelet_checks":checks,
  "old_weighted_mask_directory_bytes":old.size(),
  "compact_weighted_mask_directory_bytes":compact.size(),
  "uniform_mask_directory_bytes":uniform.size(),"bench":bench},indent=2))
