#!/usr/bin/env python3
"""EC49FPB: exact unrestricted Bellman optimization and min-depth tie break.
Consumes original EC49FOZ evidence and FPA 75-config prior, exact integers.
"""
import json, sys, os
from pathlib import Path
from functools import lru_cache
from collections import defaultdict
R=Path(__file__).resolve().parent
sys.path[:0]=[str(R/'EC49FOZ_evidence'), str(R)]
os.chdir(R/'EC49FOZ_evidence')
import EC49FOZ_verify as frozen
from EC49FPA_CONFIG_WEIGHTED_3 import weights_for

def solve(X,weights):
 n=len(X); q=len(X[0]); FULL=(1<<n)-1
 masks=[]
 for j in range(q):
  fibers={}
  for i in range(n):
   k=X[i][j];fibers[k]=fibers.get(k,0)|(1<<i)
  masks.append(tuple(fibers.values()))
 @lru_cache(None)
 def sumw(v):return sum(weights[i] for i in range(n) if v>>i&1)
 @lru_cache(None)
 def dp(v):
  if v.bit_count()==1:return (0,0)
  best=None
  for parts in masks:
   kids=[v&p for p in parts];kids=[k for k in kids if k.bit_count()>1]
   if len(kids)==1 and kids[0]==v:continue
   parts2=[dp(k) for k in kids]
   cost=sumw(v)+sum(e for e,d in parts2)
   depth=1+max((d for e,d in parts2),default=0)
   if best is None or (cost,depth)<best:best=(cost,depth)
  return best
 root=dp(FULL)
 first=[]
 for j,p in enumerate(masks):
  kids=[FULL&v for v in p];kids=[k for k in kids if k.bit_count()>1]
  cost=sumw(FULL)+sum(dp(k)[0] for k in kids)
  depth=1+max((dp(k)[1] for k in kids),default=0)
  if cost==root[0]:
   first.append({'first':j,'best_expected_weighted_total':cost,
                 'minimal_worst_case_depth_given_first':depth})
 return {'global_minimum':root,
         'expectation_optimal_first_queries':first,
         'memoized_states':dp.cache_info().currsize}

if __name__=='__main__':
 k,c=frozen.load();out={}
 for rep in (14304,14309):
  x=frozen.costs(rep,k,c);out[rep]={}
  for prior,w in [('profiles',[1]*40),
                  ('configurations',weights_for(rep))]:
   o=solve(x,w);out[rep][prior]=o
   expected=(73,3) if prior=='profiles' else (177,3)
   assert tuple(o['global_minimum'])==expected
   assert [(t['first'],t['minimal_worst_case_depth_given_first'])
           for t in o['expectation_optimal_first_queries']] == (
           [(78,3),(99,4),(177,4)] if (rep,prior)==(14304,'profiles')
           else [(119,3),(153,4),(191,4)] if prior=='profiles'
           else [(78,3)] if rep==14304 else [(119,3)])
   print('GLOBAL_OPTIMUM_PASS',rep,prior,o,flush=True)
 (R/'EC49FPB_OPTIMAL_FIRST_DEPTH_RESULT.json').write_text(json.dumps(out,indent=2)+'\n')
 print('EC49FPB_GLOBAL_EXPECTATION_AND_DEPTH_CLASSIFICATION_PASS')
