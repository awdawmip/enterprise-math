#!/usr/bin/env python3
"""Exhaustive 101 choose 3 cover count and exact minimum-cost triple."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parent
raw=(ROOT/'EXACT_R5_ALL_101_BUDGETS.json').read_bytes()
assert hashlib.sha256(raw).hexdigest()=='50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b'
D=json.loads(raw)['counts_and_cohorts']
N={k:list(map(int,D[str(k)]['counts'])) for k in range(214,315)}
U=58182461585441404127941754880
pairs=[(i,j) for i in range(256) for j in range(i+1,256)]
FULL=(1<<len(pairs))-1
C=[]
for k in N:
 mask=0
 for p,(i,j) in enumerate(pairs):
  if abs(N[k][i]-N[k][j])>=U:mask|=1<<p
 C.append(mask)
K=list(N)
double=0;triple=0;low=10**9;opt=[]
for i,a in enumerate(K):
 for j in range(i+1,len(K)):
  cov=C[i]|C[j]
  if cov==FULL:double+=1
  for z in range(j+1,len(K)):
   if cov|C[z]==FULL:
    triple+=1
    cost=a+K[j]+K[z]
    if cost<low:low=cost;opt=[(a,K[j],K[z])]
    elif cost==low:opt.append((a,K[j],K[z]))
assert double==0 and triple==3468 and low==735 and opt==[(216,223,296)]
print('PASS_101_BUDGET_TRIPLE_COVER',len(pairs),double,triple,low,opt)
