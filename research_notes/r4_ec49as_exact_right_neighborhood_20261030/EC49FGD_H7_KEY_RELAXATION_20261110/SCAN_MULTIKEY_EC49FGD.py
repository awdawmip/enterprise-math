#!/usr/bin/env python3
from VERIFY_EC49FGD import *
import json
pools={s:[] for s in NEED}
keys={}
for z in (1,2,3):
 for x in range(1,9):
  for y in range(1,9-2*z):
   if x+y<8:continue
   pool,counts=candidates(7,x,y,z)
   for s,v in pool.items():
    pools[s].extend(v)
    for w in v:keys[w]=(x,y,z)
print('total',sum(len(v) for v in pools.values()),'distinct keys',len(set(keys.values())), flush=True)
best,nodes=optimize(pools)
print('best',best,'nodes',nodes)
print('keys of witness',{s:keys[w] for s,w in best['witness'].items()})
with open(str(Path(__file__).with_name('MULTIKEY_REPORT_EC49FGD.json')),'w') as f:
 json.dump({'pooled':{str(s):len(v) for s,v in pools.items()},'distinct_keys':len(set(keys.values())),'trie_nodes':nodes,'best':best,'keys_in_witness':{s:keys[w] for s,w in best['witness'].items()}},f,indent=2);f.write('\n')
