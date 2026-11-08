"""EC49FEL: exact exhaustive positive BRC high-key inventory and depth-wise signed X6 bounds.
Inherits pinned EC49FEJ/FEK primitive libraries; no changed scientific semantics.
"""
from EC49FEJ_SIEVE import high_keys,pool
from itertools import product
from collections import Counter
import EC49FEK_ALT_TEST as A
import json,sys,time
assert len(sys.argv)>=4
start,stop=int(sys.argv[1]),int(sys.argv[2]); output=sys.argv[3]
high={3,4,5,7,9}
A.GROUPS={h:((16,32) if h in high else (1,2,4,8)) for h in range(2,10)}
A.groups.cache_clear()
h={i:high_keys(i) for i in (4,5,7,9)}
Ks=list(product(*(h[i] for i in (4,5,7,9))))
assert len(Ks)==1152 and 0<=start<stop<=1152
rows=[];c=Counter(); t0=time.monotonic()
for i in range(start,stop):
    K=((3,1,1),)+Ks[i]
    # This uses original exact full BRC words to certify feasible observer signature pools
    missing=[(h,s) for h in (6,8) for s in (1,2,4,8) if not any(any(x==s for _,x in pool(h,k)) for k in K)]
    if missing:
       row={'index':i,'keys':K,'status':'infeasible','missing':missing}; c['infeasible']+=1
    else:
       lb,counts,d=A.lower(K,cap=94)
       assert lb is not None
       stat='excluded93' if lb>=94 else 'unresolved'
       c[stat]+=1
       row={'index':i,'keys':K,'status':stat,'lower_bound':lb,'depth_covers':counts,'stop_depth':d}
    rows.append(row)
    if (i-start+1)%24==0:
       with open(output,'w') as f:json.dump({'pin':'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab','high':[3,4,5,7,9],'start':start,'requested_stop':stop,'processed_stop':i+1,'stats':dict(c),'results':rows},f,separators=(',',':'))
       print(i+1,round(time.monotonic()-t0,2),dict(c),flush=True)
with open(output,'w') as f:json.dump({'pin':'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab','high':[3,4,5,7,9],'start':start,'requested_stop':stop,'processed_stop':stop,'stats':dict(c),'results':rows},f,separators=(',',':'))
print('COMPLETE',start,stop,dict(c),'sec',round(time.monotonic()-t0,2),flush=True)