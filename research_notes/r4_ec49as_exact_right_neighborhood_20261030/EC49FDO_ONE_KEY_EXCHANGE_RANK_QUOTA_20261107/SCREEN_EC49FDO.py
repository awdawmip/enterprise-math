#!/usr/bin/env python3
"""EC49FDO exact DFA signature + five-key + horizon-slot enumeration; stdlib only.
Run python SCREEN_EC49FDO.py . Uses frozen EC49FDL transition and signature table.
Does not optimize prefix edges; prefix MILPs are in REPLAY_EC49FDO_MILP.py.
"""
from functools import lru_cache
import json
TRANS=((1,2,3,1,4,5),(1,6,7,1,1,1),(2,2,8,2,2,2),
       (3,8,3,3,3,3),(4,2,7,4,4,4),(5,6,3,5,5,5),
       (6,6,8,6,6,6),(7,8,7,7,7,7),(8,8,8,8,8,8))
SIG=(0,0,4,1,16,32,8,2,0);CLAUSES=(18,20,33,40)
FAMILIES={
 '1512':((3,1,1),(4,2,1),(4,3,1),(4,4,1),(5,5,1)),
 '1513':((3,1,1),(4,2,1),(5,2,1),(6,2,1),(7,3,1)),
 '2200':((3,1,1),(3,2,1),(4,3,1),(4,4,1),(5,5,1)),
 '2203':((3,1,1),(4,1,1),(5,2,1),(6,2,1),(7,3,1))}
QUOTAS={'1512':(4,2,2,2,4,2),'1513':(4,2,2,2,4,2),
        '2200':(2,4,2,2,4,2),'2203':(2,4,2,2,4,2)}
def viable(s):return all(s & clause for clause in CLAUSES)
@lru_cache(None)
def mask(h,k):
 x,y,z=k;r=x+y-h-1;a=z-1;e=z;f=h+1-y-2*z;g=h+1-x
 if min(r,a,e,f,g)<0:return 0
 @lru_cache(None)
 def rec(counts,state):
  if sum(counts)==0:return SIG[state]
  out=0
  for i,n in enumerate(counts):
   if n and TRANS[state][i]!=8:
    v=list(counts);v[i]-=1
    out|=rec(tuple(v),TRANS[state][i])
  return out
 return functools_or(rec((a,c,r-c,e,f,g),0) for c in range(r+1))
def functools_or(values):
 out=0
 for a in values:out|=a
 return out
@lru_cache(None)
def masks_with_slots(keys,h,q):
 types=[(s,1<<j) for j,k in enumerate(keys[1:]) for s in (1,2,4,8,16,32) if mask(h,k)&s]
 dp=[{(0,0)}]+[set() for _ in range(q)]
 for s,bit in types:
  for t in range(q-1,-1,-1):
   dp[t+1].update((p|s,u|bit) for p,u in dp[t])
 return {u for row in dp for p,u in row if viable(p)}
def slot_keys_feasible(keys,quotas):
 used={0}
 for h,q in zip(range(4,10),quotas):
  options=masks_with_slots(keys,h,q)
  if not options:return False
  used={a|b for a in used for b in options}
 return 15 in used
def main():
 domain=sorted({(x,y,z) for h in range(4,10)
                for x in range(1,h+2) for y in range(h+2)
                for z in range(1,h+2)
                if x+y>=h+1 and h+1-y-2*z>=0})
 assert len(domain)==158
 useful=[k for k in domain if any(mask(h,k) for h in range(4,10))]
 assert len(useful)==155
 results={}
 for fid,oldkeys in FAMILIES.items():
  assert slot_keys_feasible(oldkeys,QUOTAS[fid])
  rank_swaps=[];slot_swaps=[]
  for removed in oldkeys[1:]:
   for new in useful:
    if new in oldkeys:continue
    keys=tuple(sorted((set(oldkeys)-{removed})|{new}))
    if all(viable(functools_or(mask(h,k) for k in keys)) for h in range(4,10)):
     rank_swaps.append((removed,new))
     if removed==oldkeys[-1] and slot_keys_feasible(keys,QUOTAS[fid]):
      slot_swaps.append(new)
  bottleneck=[new for old,new in rank_swaps if old==oldkeys[-1]]
  results[fid]={'all_rank9_one_key_swaps':len(rank_swaps),
                'last_key_rank9_swaps':len(bottleneck),
                'last_key_slot_and_exact_5_key_swaps':len(slot_swaps),
                'last_key_feasible_new_keys':[list(k) for k in slot_swaps]}
  assert (len(rank_swaps),len(bottleneck),len(slot_swaps))==(502,49,15)
 return {'schema':'EC49FDO_EXACT_KEY_SWAP_SCREEN_V1',
         'frozen_science_pin':'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab',
         'domain':len(domain),'nonempty_six_signature_domain':len(useful),
         'distinct_exchange_events':sum(v['all_rank9_one_key_swaps'] for v in results.values()),
         'critical_key_events':196,'critical_key_viable_events':60,'results':results}
if __name__=='__main__':print(json.dumps(main(),indent=2,ensure_ascii=False))
