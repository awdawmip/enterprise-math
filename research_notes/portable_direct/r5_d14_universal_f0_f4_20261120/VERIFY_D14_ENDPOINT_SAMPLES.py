#!/usr/bin/env python3
"""Independent doubled-left-endpoint Bellman checks for selected D14 cases.
Reads only frozen integer centers; does not use C++ generated adjacency.
"""
import json,hashlib
from pathlib import Path
from functools import lru_cache
import csv
P=Path(__file__).parent
raw=(P/'EXACT_R5_ALL_101_BUDGETS.json').read_bytes()
assert hashlib.sha256(raw).hexdigest()=='50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b'
data=json.loads(raw)
tau=int(json.loads((P/'stages_18.json').read_text())['U'])-1
centers={k:list(map(int,data['counts_and_cohorts'][str(k)]['counts'])) for k in range(214,315)}
W=(0,16,32,48,1,64,17,80,18,24,34,82)
classes=list(csv.DictReader((P/'classes_1906.tsv').open(),delimiter='\t'))
def actions(u,v):
 h=W+(u,v);by_family={}
 for k in centers:
  a=[centers[k][i] for i in h]
  endpoints=[2*x-tau for x in a]
  masks={sum(1<<j for j,y in enumerate(a) if abs(2*y-z)<=tau) for z in endpoints}
  top=tuple(sorted(s for s in masks if not any(s!=m and (s&m)==s for m in masks)))
  if top==(16383,):continue
  by_family[top]=min(k,by_family.get(top,k))
 return sorted((cost,fam) for fam,cost in by_family.items())
def solve(a,f):
 @lru_cache(None)
 def value(e):
  live=sum(1<<i for i,x in enumerate(e) if x<=f)
  if live.bit_count()<=1:return 0
  candidates=[]
  for k,fam in a:
   if any((mask&live)==live for mask in fam):continue
   candidates.append(k+max(value(tuple(min(f+1,e[j]+int(not(mask&(1<<j)))) for j in range(14))) for mask in fam))
  return min(candidates)
 return value((0,)*14)
for i,f in [(0,3),(699,3),(1905,2),(35,2),(200,1),(1000,1),(1800,0),(35,4),(699,4),(1504,4)]:
 r=classes[i]
 sig=actions(int(r['u']),int(r['v']))
 assert len(sig)==int(r['actions'])
 val=solve(sig,f)
 assert val==735+950*f,(i,f,val)
 print('PASS_INDEPENDENT',i,'f',f,'value',val)
print('PASS_D14_ENDPOINT_SAMPLES')
