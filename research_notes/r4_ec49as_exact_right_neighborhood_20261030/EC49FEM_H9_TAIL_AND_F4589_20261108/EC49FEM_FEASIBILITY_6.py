"""Six unclassified H9-high BRC observation families, exact finite inventory test.
Frozen science: fc0f038e7bfd12c886b4d37f900bfb770c0f61ab.
Requires EC49FEJ_SIEVE.py from EC49FEJ pinned evidence.
"""
from EC49FEJ_SIEVE import high_keys,pool
from itertools import combinations,product
from collections import Counter
from functools import lru_cache
from time import monotonic
import json,math
PREVIOUS={(3,4,6,7,9),(3,4,6,8,9),(3,4,5,6,9),(3,4,5,7,9)}
@lru_cache(maxsize=None)
def mask(h,k):
 return sum(1<<i for i,s in enumerate((1,2,4,8,16,32)) if s in {v for _,v in pool(h,k)})
def classification(highs):
 opts=[high_keys(h) for h in highs if h!=3]
 lows=[h for h in range(2,10) if h not in highs]
 cnt=Counter();sample=None
 for ks in product(*opts):
  K=((3,1,1),)+ks
  missing=[]
  for h in lows:
   v=0
   for key in K:v|=mask(h,key)
   if v&15!=15:missing.append(h)
  category='feasible' if not missing else ';'.join(map(str,missing))
  cnt[category]+=1
  if not missing and sample is None:sample=K
 assert sum(cnt.values())==math.prod(len(v) for v in opts)
 return {'highs':highs,'total':sum(cnt.values()),'feasible':cnt['feasible'],'counts':dict(cnt),'example':sample}
if __name__=='__main__':
 rows=[]
 for four in combinations((4,5,6,7,8,9),4):
  hs=(3,)+four
  if hs not in PREVIOUS and hs[-1]==9:rows.append(classification(hs))
 with open('EC49FEM_FEASIBILITY_6.json','w') as f:json.dump(rows,f,indent=2)
 print(json.dumps(rows,indent=2))
