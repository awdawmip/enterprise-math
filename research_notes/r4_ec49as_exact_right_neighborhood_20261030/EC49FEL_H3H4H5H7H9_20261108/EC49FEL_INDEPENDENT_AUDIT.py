"""Independent sampled exact 0-1 MILP check for depthwise cover, EC49FEL."""
import json
from scipy.optimize import milp,Bounds,LinearConstraint
import numpy as np
from collections import defaultdict
from EC49FEJ_SIEVE import pool
from EC49FEJ_CONSTRUCT import native
import EC49FEK_ALT_TEST as A
A.GROUPS={h:((16,32) if h in (3,4,5,7,9) else (1,2,4,8)) for h in range(2,10)}
A.groups.cache_clear()
files=('EC49FEL_0_144.json','EC49FEL_144_1152.json','EC49FEL_936_1152.json')
allrows=[r for file in files for r in json.load(open(file))['results']]
assert len(allrows)==1152
out=[]
for i in [0,31,100,256,393,512,777,901,1021,1151]:
 r=allrows[i];K=tuple(tuple(k) for k in r['keys'])
 gg=[]
 for h in range(4,10):
  for s in A.GROUPS[h]:
   gg.append(set(native(w) for k in K for w,t in pool(h,k) if t==s))
 for d,v in r['depth_covers']:
  if not (9<=d<=12): continue
  active=[g for g in gg if min(map(len,g))>=d]
  if not active: continue
  masks=defaultdict(set)
  for j,g in enumerate(active):
   for w in g:masks[w[:d]].add(j)
  free={p for p in A.EARLY_U if len(p)==d}
  covered=set().union(*(masks[p] for p in free)) if free else set()
  rem=set(range(len(active)))-covered
  if not rem: assert v==0;out.append((i,d,v,0));continue
  cols=[p for p in masks if p not in free and masks[p]&rem]
  needed=sorted(rem)
  mat=np.array([[float(j in masks[p]) for p in cols] for j in needed],dtype=float)
  res=milp(np.ones(len(cols)),integrality=np.ones(len(cols)),bounds=Bounds(np.zeros(len(cols)),np.ones(len(cols))),constraints=[LinearConstraint(mat,np.ones(len(needed)),np.full(len(needed),np.inf))],options={'mip_rel_gap':0})
  assert res.success and abs(res.fun-round(res.fun))<=1e-7,(i,d,res.message)
  exact=int(round(res.fun));assert exact==v,(i,d,exact,v)
  out.append((i,d,v,exact))
report={'audit_type':'independent SciPy HiGHS 0-1 integer covering model','cases':len(set(t[0] for t in out)),'depth_subproblems':len(out),'all_equal':True,'sample':out}
open('EC49FEL_MILP_AUDIT.json','w').write(json.dumps(report,indent=2)+'\n')
print({k:v for k,v in report.items() if k!='sample'})