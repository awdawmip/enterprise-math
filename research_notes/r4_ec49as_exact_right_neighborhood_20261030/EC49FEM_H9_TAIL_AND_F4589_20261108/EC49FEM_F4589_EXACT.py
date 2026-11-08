"""Exact native-prefix-depth cover for highs H3,H4,H5,H8,H9;
allow five complete BRC keys and unrestricted within-horizon key mixing.
Frozen science fc0f038e7bfd12c886b4d37f900bfb770c0f61ab.
Requires EC49FEJ_SIEVE.py, EC49FEK_ALT_TEST.py and EC49FEM_FEASIBILITY_6.py.
Run four disjoint ranges 0 384, 384 768, 768 1152, 1152 1536.
"""
from EC49FEJ_SIEVE import high_keys
import EC49FEK_ALT_TEST as A
from EC49FEM_FEASIBILITY_6 import mask
from itertools import product
from collections import Counter
from functools import reduce
import sys,json
A.HIGHS=(3,4,5,8,9)
A.GROUPS={h:((16,32) if h in A.HIGHS else (1,2,4,8)) for h in range(2,10)}
A.groups.cache_clear()
start,stop=map(int,sys.argv[1:3])
assert 0<=start<stop<=1536
assert len(high_keys(4))*len(high_keys(5))*len(high_keys(8))*len(high_keys(9))==1536
rows=[];counts=Counter()
for i,ks in enumerate(product(*(high_keys(h) for h in (4,5,8,9)))):
 if i<start:continue
 if i>=stop:break
 K=((3,1,1),)+ks
 good=all((reduce(lambda a,b:a|b,(mask(h,k) for k in K),0)&15)==15 for h in (2,6,7))
 if not good:
  counts['infeasible']+=1
  rows.append({'index':i,'keys':K,'status':'infeasible'})
  continue
 lb,dc,stop_depth=A.lower(K,cap=94)
 assert lb is not None
 status='excluded93' if lb>=94 else 'unresolved'
 counts[status]+=1
 rows.append({'index':i,'keys':K,'status':status,'lower_bound':lb,'stop_depth':stop_depth,'counts':dc})
with open(f'EC49FEM_F4589_EXACT_{start}_{stop}.json','w') as f:
 json.dump({'start':start,'stop':stop,'pin':'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab','high':[3,4,5,8,9],'total':len(rows),'counts':dict(counts),'rows':rows},f,separators=(',',':'))
print('COMPLETE',start,stop,dict(counts))
