#!/usr/bin/env python3
"""EC49FRT: exact original-BRC unrestricted four-named-query cost phase.
Place in extracted prior EC49FRR evidence package's code/ directory.
Run python code/EC49FRT_FOUR_QUERY_STRUCTURAL_VERIFY_20261117.py
Produces evidence/EC49FRT_FOUR_EQUAL_SURCHARGE_CERTIFICATE_20261117.json
Full exact original native q46/q93 winning tree certificates included in output.
"""
import sys,json,hashlib,time,collections
from pathlib import Path
from functools import cache
BASE=Path(__file__).resolve().parent.parent
sys.path.insert(0,str(BASE/'code'))
from EC49FRQ_INDEPENDENT_ALL228 import PARTS,ALL,OBS,subset_keys
from EC49FQI_NATIVE_DATA import V,keys,PIN,MASTER,CSV
CHARGED=(32,34,140,142)
assert PIN=='fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'
assert hashlib.sha256((BASE/'source/frozen_original_master.txt').read_bytes()).hexdigest()==MASTER
assert hashlib.sha256((BASE/'source/EC49FPG_PROFILE.csv').read_bytes()).hexdigest()==CSV
assert len(V)==len(OBS)==228
assert all(OBS[q]==V[q] for q in range(144))
assert len(keys)==len(subset_keys)==84 and set(keys)==set(subset_keys)
assert all(OBS[144+i]==V[144+keys.index(key)] for i,key in enumerate(subset_keys))
def native(q):return q if q<144 else 144+keys.index(subset_keys[q-144])
res={'schema':'EC49FRT_FOUR_EQUAL_NAMED_SURCHARGE_V1','pin':PIN,
     'original_states':141,'original_actions':228,
     'source_master_sha256':MASTER,'source_profile_sha256':CSV,'cases':[]}
expected={0:(41736,[32,34]),1:(41877,[32,34]),
          3:(42159,[32,34,46,93]),10:(42159,[46,93])}
for delta in (0,1,3,10):
 @cache
 def opt(mask):
  if mask.bit_count()==1:return 0,()
  best=10**50;options=[]
  for q,partition in enumerate(PARTS):
   children=[mask & part for part in partition if mask & part]
   if len(children)<2:continue
   v=(141+delta*int(q in CHARGED))*mask.bit_count()+sum(opt(c)[0] for c in children)
   if v<best:best=v;options=[q]
   elif v==best:options.append(q)
  return best,tuple(options)
 value,qs=opt(ALL)
 first=sorted(native(q) for q in qs)
 assert (value,first)==expected[delta],(delta,value,first)
 assert opt.cache_info().currsize==13063
 res['cases'].append({'epsilon':f'{delta}/141','integer_bellman':value,
                      'all_first_original_physical_queries':first,
                      'reachable_subsets':opt.cache_info().currsize})
 print('PASS',delta,value,first,flush=True)
 if delta==10:
  def tree(mask,root=None):
   if mask.bit_count()==1:return {'leaf':mask.bit_length()-1}
   q=root if root is not None else opt(mask)[1][0]
   children={}
   for part in PARTS[q]:
    sub=part & mask
    if not sub:continue
    i=(sub&-sub).bit_length()-1
    children[str(OBS[q][i])]=tree(sub)
   assert len(children)>=2
   return {'q':native(q),'children':children}
  for q in (46,93):
   t=tree(ALL,root=q);cnt=collections.Counter();total=0
   for i in range(141):
    node=t
    while 'leaf' not in node:
     p=node['q'];cnt[p]+=1;total+=1
     node=node['children'][str(V[p][i])]
    assert node['leaf']==i,(q,i)
   assert total==299 and all(cnt[j]==0 for j in CHARGED)
   res.setdefault('avoiding_native_trees',{})[str(q)]={
      'tree':t,'total_path_observation_uses':total,
      'named_charged_path_uses':{str(j):cnt[j] for j in CHARGED}}
   print('REPLAY_PASS',q,total,flush=True)
res['conclusion']='W(epsilon)/t=min(296/141+epsilon,299/141), epsilon>=0'
res['status']='AUTHOR_PROVED / EXACT_FINITE_BELLMAN_AND_TREE_REPLAY / NOT_REVIEWED'
out=BASE/'evidence/EC49FRT_FOUR_EQUAL_SURCHARGE_CERTIFICATE_20261117.json'
out.write_text(json.dumps(res,indent=2,ensure_ascii=False)+'\n')
print('WROTE',out)
