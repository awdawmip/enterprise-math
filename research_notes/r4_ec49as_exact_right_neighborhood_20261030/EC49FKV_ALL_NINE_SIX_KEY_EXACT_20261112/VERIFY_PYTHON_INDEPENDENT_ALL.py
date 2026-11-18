#!/usr/bin/env python3
"""Independent pure-Python exact signed-X6 prefix DP for all nine six-key sets.

Original pinned BRC generator from EC49FGW and keys from EC49FKS.
"""
import sys,collections,json,time
from MAKE_INSTANCE_ALL import KEY_BASE, EXTRAS, PIN
from EC49FGW_RADIUS5_SCREEN import all_words, raw_key, pref,REQ
labels=sorted((h,s) for h,v in REQ.items() for s in v)
assert PIN=='fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'
labelno={v:i for i,v in enumerate(labels)}

def eval_case(idx):
 keyset=KEY_BASE|set(EXTRAS[idx]);trie=[{'c':{},'mask':0}];count=0
 for lab,w in all_words():
  if raw_key(w) not in keyset:continue
  count+=1
  u=0
  for step in pref(w)[-1]:
   nxt=trie[u]['c'].get(step)
   if nxt is None:
    nxt=len(trie);trie[u]['c'][step]=nxt;trie.append({'c':{},'mask':0})
   u=nxt
  trie[u]['mask']|=1<<labelno[lab]
 def collect(root):
  ret=trie[root]['mask']
  for u in trie[root]['c'].values():ret|=collect(u)
  return ret
 roots={step:(u,collect(u)) for step,u in trie[0]['c'].items()}
 assert set(roots)=={5,6,7}
 assert all(i.bit_count()==12 for j,(u,i) in roots.items() if j in (5,6))
 assert roots[7][1].bit_count()==8 and (roots[5][1]&roots[6][1])==0
 def rec(u,lab_map):
  k=trie[u]['mask'];start=0
  for glob,loc in lab_map.items():
   if k & (1<<glob):start |= 1<<loc
  dp={0:0}
  if start:dp[start]=0
  for child in trie[u]['c'].values():
   nxt=rec(child,lab_map)
   out={}
   for a,ca in dp.items():
    for b,cb in nxt.items():
     m=a|b;cost=ca+cb
     if cost<out.get(m,10**9):out[m]=cost
   dp=out
  return {m:cost+(m!=0) for m,cost in dp.items()}
 rootinfo={}
 for k,(u,globmask) in roots.items():
  mapping={g:j for j,g in enumerate(i for i in range(24) if globmask&(1<<i))}
  dp=rec(u,mapping)
  n=1<<len(mapping)
  cost=[dp.get(m,10**6) for m in range(n)]
  for j in range(len(mapping)):
   for m in range(n):
    if not m&(1<<j):cost[m]=min(cost[m],cost[m|(1<<j)])
  rootinfo[k]=(mapping,cost)
 def locmask(s,mapping):return sum(1<<t for g,t in mapping.items() if s&(1<<g))
 rmasks={k:roots[k][1] for k in roots}
 R7=list(rootinfo[7][0]); costs=[]
 for s in range(256):
  covered7=sum(1<<g for j,g in enumerate(R7) if s&(1<<j))
  cost=0
  for k in (5,6):
   m=rmasks[k]&~covered7
   cost+=rootinfo[k][1][locmask(m,rootinfo[k][0])]
  cost+=rootinfo[7][1][s]
  costs.append(cost)
 assert len(trie)-1 in (19962,26704,42024,46278,39100)
 assert min(costs)==(98 if idx<4 else 112)
 return {'case':idx,'words':count,'nodes':len(trie)-1,'labels':len(labels), 'root_best':[rootinfo[k][1][-1] for k in (5,6,7)],'min_cost':min(costs),'opt_allocations':costs.count(min(costs)),'nonzero_allocation_min':min(costs[1:]),'allocation_costs':costs}

if __name__=='__main__':
 start=time.time()
 for i in range(9):
  r=eval_case(i)
  print('PYTHON_INDEPENDENT_CASE_PASS',i,r['words'],r['nodes'],r['min_cost'],r['opt_allocations'],r['nonzero_allocation_min'],flush=True)
  if "--write-costs" in sys.argv:open(f'PY_COSTS_{i}.json','w').write(json.dumps(r,indent=2,sort_keys=True))
 print('EC49FKV_NINE_CASES_INDEPENDENT_PYTHON_PASS',round(time.time()-start,2),flush=True)
