#!/usr/bin/env python3
"""O(1)-per-event linked-label rank sweep on the frozen R5 first-zero spectrum.

Requires the sibling VERIFY_R5_EVENT_SWEEP.py, which independently
recomputes the exact bitset N, collision atlas and 2909 full chambers.
"""
from collections import defaultdict
from pathlib import Path
from runpy import run_path

g=run_path(str(Path(__file__).resolve().with_name("VERIFY_R5_EVENT_SWEEP.py")))
N, gates, atlas = g["N"],g["gates"],g["atlas"]

fixed_order=[("F",n) for n in sorted(N,reverse=True)]
head=("HEAD",0)
tail=("TAIL",0)
prev={head:None,tail:fixed_order[-1]}
nxt={tail:None,head:fixed_order[0]}
for i,key in enumerate(fixed_order):
    prev[key]=head if i==0 else fixed_order[i-1]
    nxt[key]=tail if i==len(fixed_order)-1 else fixed_order[i+1]
rank={k:i+1 for i,k in enumerate(fixed_order)}

events=defaultdict(list)
for q,r in gates.items():
    events[r].append(("G",q,None))
for r,pairs in atlas.items():
    for q,n in pairs:
        events[r].append(("C",q,n))

insertions=swaps=0
for r in sorted(events):
    bundle=events[r]
    assert len(bundle)<=3
    for kind,q,n in bundle:
        if kind=="G":
            key=("M",q)
            a=prev[tail]
            nxt[a]=key
            prev[key]=a
            nxt[key]=tail
            prev[tail]=key
            rank[key]=len(rank)+1
            insertions+=1
        else:
            a,b=("F",n),("M",q)
            assert nxt[a]==b and prev[b]==a
            assert rank[b]==rank[a]+1
            left,right=prev[a],nxt[b]
            nxt[left]=b
            prev[b]=left
            nxt[b]=a
            prev[a]=b
            nxt[a]=right
            prev[right]=a
            rank[a]+=1
            rank[b]-=1
            swaps+=1

assert (len(events),insertions,swaps)==(2908,3,3432)
out=[]
p=nxt[head]
while p!=tail:
    out.append(p)
    p=nxt[p]
assert out[:3]==[("M",15),("M",12),("M",3)]
assert out[3:]==fixed_order
assert all(rank[k]==i+1 for i,k in enumerate(out))
assert all(rank[("F",n)]==i+4 for i,n in enumerate(sorted(N,reverse=True)))

print("LINKED_SWEEP_EVENTS",len(events))
print("LINKED_SWEEP_INSERTIONS",insertions,"ADJACENT_SWAPS",swaps)
print("FINAL_MOVING_RANKS",[(q,rank[("M",q)]) for q in (15,12,3)])
print("FIXED_LABEL_FINAL_SHIFT",set(rank[("F",n)]-(i+1)
                                      for i,n in enumerate(sorted(N,reverse=True))))
print("PASS_R5_LINKED_EXACT_INCREMENTAL_RANK_SWEEP")
