#!/usr/bin/env python3
"""Compare bounded (new) against unbounded EC49ER exact OR-mask trie DP on deterministic sample."""
from VERIFY_EC49ER import *
from VERIFY_EC49ES import bounded_opt
import json,time
fs=fibers();out=[]
for m,lim in ((4,80),(5,60)):
 cases=json.load(open(f'EC49ES_M{m}_SCREENED.json'))['screened']
 ids=sorted(set([0,1,2,len(cases)//3,len(cases)//2,2*len(cases)//3,len(cases)-3,len(cases)-2,len(cases)-1]))
 for i in ids:
  ps=tuple(tuple(p) for p in cases[i]);choice=dict(zip(range(3,7),ps))
  a=exact_trie_opt(fs,choice)['E'];b=bounded_opt(fs,ps,lim)['E']
  assert b==(a if a<=lim else None),(m,i,a,b)
  out.append({'M':m,'index':i,'unbounded_E':a,'bounded_E_or_none':b})
report={'unit':'EC49ES','status':'PASS','checks':len(out),'test':'unbounded EC49ER DP agrees exactly with EC49ES bound-pruned DP on deterministic sample, including over-bound cases','cases':out}
with open('EC49ES_CROSSCHECK_EXECUTED.json','w') as f:json.dump(report,f,indent=2)
print('PASS',len(out),'comparisons')
