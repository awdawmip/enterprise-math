#!/usr/bin/env python3
"""Emit all 101 original-budget supports, retaining only cheapest identical families.
Usage: python build_nine.py x y U > input.txt. Requires frozen exact table.
"""
import hashlib,json,sys
from pathlib import Path
PIN="50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b"
L=25845652773852463277015040000
U=58182461585441404127941754880
def maximal(ms):
 s=set(ms)
 return tuple(sorted(m for m in s if not any(m!=n and (m&n)==m for n in s)))
def supports(c,t):
 return maximal(sum(1<<i for i,x in enumerate(c) if v<=x<=v+t) for v in c)
p=Path("EXACT_R5_ALL_101_BUDGETS.json")
raw=p.read_bytes();assert hashlib.sha256(raw).hexdigest()==PIN
D=json.loads(raw)["counts_and_cohorts"]
x,y=map(int,sys.argv[1:3]);assert x<y
H=(18,24,82,34,17,x,144,208,y)
assert len(set(H))==9
tau=L if sys.argv[3]=="L" else U-1
groups={}
for k in range(214,315):
 c=list(map(int,D[str(k)]["counts"]))
 sig=supports([c[h] for h in H],tau)
 if sig not in groups or k<groups[sig]:groups[sig]=k
acts=sorted((cost,masks) for masks,cost in groups.items())
print(9,8);print(len(acts))
for k,masks in acts:print(k,len(masks),*masks)
