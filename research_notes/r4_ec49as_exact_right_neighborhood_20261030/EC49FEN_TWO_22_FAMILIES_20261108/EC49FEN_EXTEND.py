"""EC49FEN exact finite lower-bound search: high horizons H3,H4,H7,H8,H9.
Scientific input pin: fc0f038e7bfd12c886b4d37f900bfb770c0f61ab.
Uses unchanged EC49FEJ/EC49FEK finite signed-native BRC semantics.
"""
from EC49FEJ_SIEVE import high_keys
from EC49FEM_FEASIBILITY_6 import mask
from itertools import product
from collections import Counter
from functools import reduce
from time import monotonic
import EC49FEK_ALT_TEST as A
import json,sys
A.HIGHS=tuple(map(int,sys.argv[1].split(',')))
A.GROUPS={h:((16,32) if h in A.HIGHS else (1,2,4,8)) for h in range(2,10)}
A.groups.cache_clear()
opts=[high_keys(h) for h in A.HIGHS if h!=3]
N=__import__('math').prod(map(len,opts))
start,stop=map(int,sys.argv[2:4])
assert 0<=start<stop<=N
rows=[];cnt=Counter();t=monotonic()
for i,ks in enumerate(product(*opts)):
 if i<start:continue
 if i>=stop:break
 K=((3,1,1),)+ks
 if not all(reduce(lambda a,b:a|b,(mask(h,k) for k in K),0)&15==15 for h in range(2,10) if h not in A.HIGHS):
  result={'index':i,'keys':K,'status':'infeasible'}
 else:
  lb,counts,stop_depth=A.lower(K,cap=94)
  result={'index':i,'keys':K,'status':'excluded93' if lb>=94 else 'unresolved','lower_bound':lb,'counts':counts,'stop_depth':stop_depth}
 cnt[result['status']]+=1;rows.append(result)
 if len(rows)%250==0: print('PROGRESS',i+1,dict(cnt),'sec',round(monotonic()-t,3),flush=True)
result={'start':start,'stop':stop,'science_pin':'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab','high':A.HIGHS, 'counts':dict(cnt),'elapsed_sec':round(monotonic()-t,3),'rows':rows}
with open('EC49FEN_%s_%s_%s.json'%(''.join(map(str,A.HIGHS)),start,stop),'w') as f:json.dump(result,f,separators=(',',':'))
print('COMPLETE',dict(cnt),'sec',round(monotonic()-t,3),flush=True)