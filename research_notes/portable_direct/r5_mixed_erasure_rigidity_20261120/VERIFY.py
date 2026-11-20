#!/usr/bin/env python3
"""Independent finite premise checker for the R5 mixed-fault theorem.
Place the exact frozen EXACT_R5_ALL_101_BUDGETS.json and stages_18.json beside this file.
Only the Python standard library is required.
"""
import json,hashlib
from pathlib import Path
from collections import Counter,defaultdict
R=Path(__file__).resolve().parent
src=(R/'EXACT_R5_ALL_101_BUDGETS.json').read_bytes()
expected='50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b'
assert hashlib.sha256(src).hexdigest()==expected
obj=json.loads(src)
stage=json.loads((R/'stages_18.json').read_text())
assert stage['frozen_sha256']==expected
tau=int(stage['U'])-1
assert tau==58182461585441404127941754879
prices=list(range(214,315))
centers=[[int(z) for z in obj['counts_and_cohorts'][str(k)]['counts']] for k in prices]
assert len(centers)==101 and all(len(r)==256 for r in centers)
P=defaultdict(list)
for h in range(256):
 for j in range(h+1,256):
  mask=0
  for i in range(101):
   if abs(centers[i][h]-centers[i][j])>tau:mask|=1<<i
  P[mask].append((h,j))
assert 0 not in P and sum(map(len,P.values()))==32640 and len(P)==53
minimal=[]
for x in sorted(P,key=lambda z:(z.bit_count(),z)):
 if not any((x&y)==y for y in minimal):minimal.append(x)
mask=lambda s:sum(1<<(k-214) for k in s)
S=[set(range(214,219)),{214,216,217,218,219,220,221},
   set(range(215,222)),set(range(223,291)),set(range(296,313))]
assert len(minimal)==5 and set(minimal)=={mask(x) for x in S}
assert all(any((x&mask(s))==mask(s) for s in S) for x in P)
assert [P[mask(s)][0] for s in S]==[(9,12),(1,2),(2,8),(0,64),(16,32)]
weights=[72,72,72,223,296]
slack={k:k-sum(weights[i] for i in range(5) if k in S[i]) for k in prices}
assert all(s>=0 for s in slack.values())
assert [k for k in prices if slack[k]==0]==[216,223,296]
assert [k for k in prices if slack[k]==1]==[217,224,297]
assert sum(weights)==735
for m in (1,2,17):
 baseline=Counter({216:m,223:m,296:m})
 for a,b in ((216,217),(223,224),(296,297)):
  Q=baseline.copy();Q[a]-=1;Q[b]+=1
  assert sum(k*n for k,n in Q.items())==735*m+1
  assert all(sum(n for k,n in Q.items() if k in s)>=m for s in S)
hist=Counter()
for x,pairs in P.items():
 n=sum(bool(x&(1<<(k-214))) for k in (216,223,296))
 assert n>=1
 hist[n]+=len(pairs)
assert dict(hist)=={1:2448,2:12192,3:18000}
print("PASS frozen SHA, 32640 pairs, 53 patterns, 5 antichain witnesses")
print("PASS 101 dual inequalities, unique three zero-slack and three unit-slack prices")
print("PASS 3 second-best substitutions for m=1,2,17")
print("Symbolic mixed fault, rigidity and all-budget proofs: see RESEARCH.md")
