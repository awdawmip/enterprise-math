"""Independent explicit 22-word signed-X6 BRC witness check for all 1152 EC49FEL inventories."""
import json
from collections import Counter
from EC49FEJ_SIEVE import pool,OPS,ORDER,TRANS,SIG,high_keys
from EC49FEJ_CONSTRUCT import endpoint,key,sig,prefixes
files=('EC49FEL_0_144.json','EC49FEL_144_1152.json','EC49FEL_936_1152.json')
rows=[r for file in files for r in json.load(open(file))['results']]
assert len(rows)==1152 and sorted(r['index'] for r in rows)==list(range(1152))
high={3,4,5,7,9}
errors=[];dist=Counter();wct=0;minc=(10**9,None)
for row in rows:
 K=tuple(tuple(x) for x in row['keys']);assert row['status']=='excluded93'
 W=[]
 for h in range(2,10):
  ss=(16,32) if h in high else (1,2,4,8)
  for s in ss:
   opts=[w for k in K for w,t in pool(h,k) if t==s]
   assert opts,(row['index'],h,s)
   W.append((h,s,min(opts)))
 assert len(W)==22
 pref=set();used=set()
 for h,s,w in W:
  assert len(w)==h and endpoint(w)==(2,0,0,0,0,0)
  assert sig(w)==s and key(w) in K
  pref.update(prefixes(w));used.add(key(w));wct+=1
 assert used==set(K)
 cost=len(pref)
 dist[cost]+=1
 if cost<minc[0]: minc=(cost, row['index'])
report={'frozen_input_pin':'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab','family_high':[3,4,5,7,9],'inventories':1152,'legal_witnesses':len(rows),'legal_words':wct,'all_five_keys_used':True,'min_lex_cost':minc[0],'min_lex_index':minc[1],'max_lex_cost':max(dist),'lex_cost_counts':dict(sorted(dist.items()))}
open('EC49FEL_WITNESS_REPORT.json','w').write(json.dumps(report,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k!='lex_cost_counts'},indent=2))