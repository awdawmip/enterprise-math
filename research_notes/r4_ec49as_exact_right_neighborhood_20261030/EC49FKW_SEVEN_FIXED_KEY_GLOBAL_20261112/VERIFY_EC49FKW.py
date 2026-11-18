#!/usr/bin/env python3
"""Exact fixed-seven-cache-key signed-native prefix optimization.
Original frozen model and witness source: EC49FGW_RADIUS5_SCREEN.py.
"""
import sys,json,time
from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent/'EC49FJD_RELEASE_B11_COMPLETE_20261111'
sys.path.insert(0,str(ROOT))
from EC49FGW_RADIUS5_SCREEN import all_words,raw_key,pref,REQ,W,PIN
labels=sorted((h,s) for h,v in REQ.items() for s in v)
labelno={v:i for i,v in enumerate(labels)}

def calc(profile):
 keys=set(map(tuple,profile['allowed_keys']))
 trie=[{'c':{},'mask':0}];count=0
 for lab,w in all_words():
  if raw_key(w) not in keys: continue
  count+=1;u=0
  for step in pref(w)[-1]:
   nxt=trie[u]['c'].get(step)
   if nxt is None:
    nxt=len(trie);trie[u]['c'][step]=nxt;trie.append({'c':{},'mask':0})
   u=nxt
  trie[u]['mask'] |= 1<<labelno[lab]
 def collect(u):
  mask=trie[u]['mask']
  for child in trie[u]['c'].values():mask|=collect(child)
  return mask
 roots={step:(v,collect(v)) for step,v in trie[0]['c'].items()}
 assert set(roots)=={5,6,7}
 assert len(roots[5][1].to_bytes(3,'little'))==3
 def dp_subtree(u,remap):
  mask=trie[u]['mask']; initial=0
  for gl,lo in remap.items():
   if mask & (1<<gl):initial|=1<<lo
  dp={0:0}
  if initial:dp[initial]=0
  for ch in trie[u]['c'].values():
   cp=dp_subtree(ch,remap)
   out={}
   for a,ca in dp.items():
    for b,cb in cp.items():
     m=a|b;v=ca+cb
     if v<out.get(m,10**9):out[m]=v
   dp=out
  return {m:v+(m!=0) for m,v in dp.items()}
 root_info={}
 for k,(u,globmask) in roots.items():
  mapping={g:i for i,g in enumerate(j for j in range(24) if globmask & 1<<j)}
  begin=time.monotonic()
  dp=dp_subtree(u,mapping)
  cost=[dp.get(i,10**9) for i in range(1<<len(mapping))]
  for bit in range(len(mapping)):
   for mask in range(len(cost)):
    if not mask>>bit&1:cost[mask]=min(cost[mask],cost[mask|1<<bit])
  root_info[k]=(mapping,cost)
  print(profile['profile_id'],'root',k,'exact full',cost[-1], 'time',round(time.monotonic()-begin,2),flush=True)
 def local_mask(glob,mapping):
  return sum(1<<loc for i,loc in mapping.items() if glob & 1<<i)
 rmasks={k:roots[k][1] for k in roots}
 seven=list(root_info[7][0]);costs=[]
 for s in range(1<<len(seven)):
  cover=sum(1<<g for j,g in enumerate(seven) if s>>j&1)
  obj=root_info[7][1][s]
  for r in [5,6]:obj += root_info[r][1][local_mask(rmasks[r]&~cover,root_info[r][0])]
  costs.append(obj)
 ans=min(costs);best=[i for i,v in enumerate(costs) if v==ans]
 return {'profile':profile['profile_id'],'keyset':[list(i) for i in sorted(keys)],'words':count,'trie_nodes':len(trie)-1,'root_labels':{str(k):[labels[i] for i in range(24) if mask>>i&1] for k,(u,mask) in roots.items()},'root_full_cost':{str(k):root_info[k][1][-1] for k in roots},'costs':costs,'exact_best':ans,'opt_allocations':best,'baseline_edges':94}
if __name__=='__main__':
 assert PIN=='fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'
 start=time.monotonic();r=[]
 for p in W['profiles']:
  obj=calc(p);r.append(obj)
  print('RESULT',p['profile_id'],obj['exact_best'],obj['opt_allocations'],flush=True)
 with open(Path(__file__).resolve().parent/'EXACT_REPORT_EC49FKW.json','w') as f:json.dump({'frozen_scientific_pin':PIN,'results':r},f,indent=2)
 print('EC49FKW_EXACT_DONE',round(time.monotonic()-start,2))
