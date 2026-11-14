#!/usr/bin/env python3
"""EC49FPB primary independent-source check: exact unrestricted adaptive
terminal-cost sensing optimization via bitset Bellman recursion.
All original data are SHA256 pinned inside EC49FOZ_verify.py, whose frozen
archive is supplied with this research evidence. No floats are used.
"""
import sys, os, json
from collections import Counter
from pathlib import Path
from functools import lru_cache
BASE=Path(__file__).resolve().parent
sys.path.insert(0,str(BASE/'EC49FOZ_evidence'))
sys.path.insert(0,str(BASE))
os.chdir(BASE/'EC49FOZ_evidence')
import EC49FOZ_verify as z
from EC49FPA_CONFIG_WEIGHTED_3 import weights_for

def optimize(X,weights):
 n=len(X);q=len(X[0]); allmask=(1<<n)-1
 partitions=[]
 for a in range(q):
  groups={}
  for i,row in enumerate(X):
   v=row[a];groups[v]=groups.get(v,0)|(1<<i)
  partitions.append(tuple(groups.values()))
 @lru_cache(None)
 def wgt(mask):
  return sum(weights[i] for i in range(n) if mask>>i&1)
 @lru_cache(None)
 def opt(mask):
  if mask.bit_count()==1:return (0,None)
  bcost=None;ba=None
  for a,parts in enumerate(partitions):
   cells=[mask & part for part in parts]
   subs=[c for c in cells if c.bit_count()>1]
   if len(subs)==1 and subs[0]==mask:continue
   if not subs:
    return (wgt(mask),a)
   val=wgt(mask)
   for sub in subs:
    val+=opt(sub)[0]
    if bcost is not None and val>bcost:break
   if bcost is None or val<bcost:
    bcost=val;ba=a
  if bcost is None:raise AssertionError('indistinguishable profiles')
  return (bcost,ba)
 total,first=opt(allmask)
 def walk(mask,depth,records):
  if mask.bit_count()==1:
   i=mask.bit_length()-1;records[i]=depth;return
  _,a=opt(mask)
  for group in partitions[a]:
   ch=mask&group
   if ch:walk(ch,depth+1,records)
 depths={};walk(allmask,0,depths)
 assert len(depths)==n
 assert sum(weights[i]*d for i,d in depths.items())==total
 return {'weighted_query_sum':total,'best_initial':first,
   'max_depth':max(depths.values()),
   'depth_histogram':dict(Counter(depths.values())),
   'weighted_depth_histogram':{d:sum(weights[i] for i,v in depths.items() if v==d)
                                for d in sorted(set(depths.values()))},
   'memo_states':opt.cache_info().currsize}
if __name__=='__main__':
 keys,cases=z.load();out={}
 for rep in [14304,14309]:
  X=z.costs(rep,keys,cases);out[rep]={}
  for prior,weight in [('uniform_profiles',[1]*40),
                       ('uniform_configurations',weights_for(rep))]:
   ans=optimize(X,weight)
   assert (ans['weighted_query_sum'],ans['best_initial'],ans['max_depth']) == (
     (73,78,3) if (rep,prior)==(14304,'uniform_profiles') else
     (73,119,3) if prior=='uniform_profiles' else
     (177,78,3) if rep==14304 else (177,119,3))
   print('EXACT_GLOBAL_VERIFIED',rep,prior,ans,flush=True)
   out[rep][prior]=ans
 (BASE/'EC49FPB_UNRESTRICTED_RESULT.json').write_text(json.dumps(out,indent=2)+'\n')
 print('EC49FPB_EXACT_UNRESTRICTED_GLOBAL_OPTIMALITY_PASS')
