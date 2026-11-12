#!/usr/bin/env python3
"""Exact signed residual event correction, portable stacked frozen R5 verifier."""
from array import array
from bisect import bisect_left, bisect_right
from fractions import Fraction
from pathlib import Path
from random import Random
from statistics import median
from time import perf_counter
import sys, json

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"brc_r5_offline_fenwick_20261112"))
import VERIFY_R5_OFFLINE_FENWICK_FROM_PINNED as P

N,M,walls,pairs,lohi=P.N,P.M,P.walls,P.pairs,P.lohi
samples=P.prev.samples
assert (N,M,len(walls)) == (2880,1065,953)
wall_to_id={w:i for i,w in enumerate(walls)}
code=[wall_to_id[(1-Fraction(36*q,n))/23] for q,n in pairs]
order=array('H',sorted(range(M),key=lambda i:(code[i],i)))
f=[0]*len(walls)
for a in code:f[a]+=1
E=[0]
for n in f:E.append(E[-1]+n)
assert E[-1]==M and max(f)==3

def greedy(radius):
    centers=[];pos=0
    while pos<len(E):
        j=bisect_right(E,E[pos]+radius)-1
        centers.append(j);pos=bisect_right(E,E[j]+radius)
    return centers

left,right=0,M
while left<right:
    m=(left+right)//2
    if len(greedy(m))<=239:right=m
    else:left=m+1
R=left;centers=greedy(R)
assert (R,len(centers))==(2,213)
coords=array('H',(E[b] for b in centers))
masks=[];bits=0;j=0
for y in coords:
    while j<y:bits|=1<<order[j];j+=1
    masks.append(bits)

def anchor(x):
    j=bisect_left(coords,x)
    if j==0:return 0
    if j==len(coords):return j-1
    return j if coords[j]-x<x-coords[j-1] else j-1

def bitmap(v,b):
    a,z=lohi[v]
    if a==z:return 0
    x=E[b];j=anchor(x);y=coords[j];bits=masks[j]
    if y<x:
        for k in range(y,x):bits|=1<<order[k]
    elif y>x:
        for k in range(x,y):bits &= ~(1<<order[k])
    return ((bits>>a)&((1<<(z-a))-1)).bit_count()

def signed(v,b):
    a,z=lohi[v]
    if a==z:return 0
    x=E[b];j=anchor(x);y=coords[j]
    ans=((masks[j]>>a)&((1<<(z-a))-1)).bit_count()
    if y<x:
        for k in range(y,x):
            i=order[k];ans+=(a<=i<z)
    elif y>x:
        for k in range(x,y):
            i=order[k];ans-=(a<=i<z)
    return ans

checks=0
for b in range(len(E)):
    pref=[0]
    for c in code:pref.append(pref[-1]+(c<b))
    for v,(a,z) in enumerate(lohi):
        target=pref[z]-pref[a]
        assert signed(v,b)==target
        assert bitmap(v,b)==target
        checks+=1
assert checks==2747520
fraction_checks=0
for r in samples:
    b=bisect_right(walls,r)
    for v in range(N):
        assert signed(v,b)==P.prev.pinned.count(v,r)
        fraction_checks+=1
assert fraction_checks==57600

rng=Random(2026111305)
pool=list(samples)+walls+[(walls[i]+walls[i+1])/2 for i in range(0,len(walls)-1,11)]
large=[v for v,(a,z) in enumerate(lohi) if z-a>=32]
workloads={}
for kind,K in (("root",256),("broad",512),("random",2048),("hotmix",2048)):
    if kind=="root":nodes=[0]*K
    elif kind=="broad":nodes=[rng.choice(large) for _ in range(K)]
    elif kind=="random":nodes=[rng.randrange(N) for _ in range(K)]
    else:
        hot=[0]+large[:18]
        nodes=[rng.choice(hot) if rng.randrange(4) else rng.randrange(N) for _ in range(K)]
    req=[(v,bisect_right(walls,rng.choice(pool))) for v in nodes]
    truth=[signed(v,b) for v,b in req]
    assert [bitmap(v,b) for v,b in req]==truth
    times={}
    for name,fn in (("bitmap",bitmap),("signed",signed)):
        trials=[]
        for _ in range(11):
            t=perf_counter();values=[fn(v,b) for v,b in req]
            assert values==truth
            trials.append(1000*(perf_counter()-t))
        times[name]=round(median(trials),3)
    workloads[kind]={"n":K,"checksum":sum(truth),"median_ms":times}

result={"status":"PASS_R5_SIGNED_EVENT_CORRECTION_PORTABLE",
"scientific_pin":"435e77af0d180eac32bd1f9c4c464bc4010b7551",
"nodes":N,"certificates":M,"walls":len(walls),"radius":R,"checkpoints":len(coords),
"all_boundary_prefix_checks_each_method":checks,"fraction_wavelet_checks":fraction_checks,
"checkpoint_mask_bytes":sys.getsizeof(masks)+sum(map(sys.getsizeof,masks)),
"checkpoint_coord_bytes":sys.getsizeof(coords),
"event_order_bytes":sys.getsizeof(order),"workloads":workloads,
"timing_scope":"pre-ranked queries, excludes source generation/initialization/serialization"}
print(json.dumps(result,ensure_ascii=False,indent=2))
