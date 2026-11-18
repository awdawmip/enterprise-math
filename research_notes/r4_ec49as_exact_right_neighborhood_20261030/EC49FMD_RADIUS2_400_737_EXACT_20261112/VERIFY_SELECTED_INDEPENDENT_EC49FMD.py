#!/usr/bin/env python3
"""Independent Python exact trie DP for three EC49FMD sample key sets."""
import collections,sys
from pathlib import Path
P=Path(__file__).resolve().parent
sys.path.insert(0,str(P))
from REPLAY_EC49FMD import cat,sets,pref,raw_key,rows

def root_dp(candidates,labels):
 index={lab:i for i,lab in enumerate(labels)}
 children=[{}];final=[0]
 for lab,path in candidates:
  v=0
  for prefix in path:
   if prefix not in children[v]:
    children[v][prefix]=len(children);children.append({});final.append(0)
   v=children[v][prefix]
  final[v]|=1<<index[lab]
 def walk(v):
  dp={0:0}
  if final[v]:dp[final[v]]=0
  for w in children[v].values():
   q=walk(w);next={}
   for a,x in dp.items():
    for b,y in q.items():
     m=a|b;z=x+y
     if z<next.get(m,10**9):next[m]=z
   dp=next
  return {m:d+(v!=0 and m!=0) for m,d in dp.items()}
 vals=[10**9]*(1<<len(labels))
 for m,d in walk(0).items():vals[m]=d
 for j in range(len(labels)):
  for m in range(len(vals)):
   if not (m&(1<<j)):vals[m]=min(vals[m],vals[m|(1<<j)])
 return vals,index

def check(global_idx):
 K=set(sets[global_idx]);roots=collections.defaultdict(list)
 for label,word in cat:
  if raw_key(word) in K:
   p=pref(word);roots[p[0]].append((label,p))
 costs={};options=collections.defaultdict(list)
 for r,group in roots.items():
  labs=sorted({lab for lab,_ in group})
  vals,idx=root_dp(group,labs);costs[r]=vals
  for lab,j in idx.items():options[lab].append((r,j))
 assert len(options)==24
 bits={r:0 for r in roots};order=sorted(options,key=lambda lab:len(options[lab]))
 best=10**9
 def search(i):
  nonlocal best
  if i==24:
   best=min(best,sum(costs[r][bits[r]] for r in roots));return
  for r,j in options[order[i]]:
   bits[r]|=1<<j;search(i+1);bits[r]&=~(1<<j)
 search(0)
 reference=rows[global_idx-400][1]
 assert best==reference,(global_idx,best,reference)
 print('EC49FMD_INDEPENDENT_PASS',global_idx,best)
for case in (404,588,673):check(case)
