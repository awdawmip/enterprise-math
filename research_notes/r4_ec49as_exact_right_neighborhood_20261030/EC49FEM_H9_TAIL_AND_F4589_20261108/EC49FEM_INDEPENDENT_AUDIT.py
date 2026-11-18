"""Independent exact BRC tail-count audit + sampled independent MILP check.
Requires pinned predecessor EC49FEJ/FEK primitive source, and generated
EC49FEM_F4589_EXACT_*.json files. Python3, SciPy/HiGHS for MILP samples.
"""
from itertools import combinations
from collections import Counter
from pathlib import Path
import json
from EC49FEJ_SIEVE import high_keys,pool
import EC49FEK_MILP_AUDIT as M
import EC49FEK_ALT_TEST as A
H={h:high_keys(h) for h in range(3,10)}
assert [len(H[h]) for h in range(3,10)]==[1,2,4,6,9,12,16]
for h in H:
 for k in H[h]:
  assert k[0]+k[1]==h+1
  assert {16,32}<={s for _,s in pool(h,k)}
assert all(not pool(9,k) for h in range(3,9) for k in H[h])
tail=[]
for four in combinations(range(4,9),4):
 hs=(3,)+four
 n=1
 for h in hs:n*=len(H[h])
 tail.append((hs,n))
assert len(tail)==5 and sum(x[1] for x in tail)==5760
rows=sorted((r for p in Path('.').glob('EC49FEM_F4589_EXACT_[0-9]*_[0-9]*.json') for r in json.load(p.open())['rows']),key=lambda r:r['index'])
assert [r['index'] for r in rows]==list(range(1536))
cnt=Counter(r['status'] for r in rows)
assert cnt=={'infeasible':576,'excluded93':960}
A.GROUPS={h:((16,32) if h in {3,4,5,8,9} else (1,2,4,8)) for h in range(2,10)}
A.groups.cache_clear()
audits=[]
for i in (0,113,325,512,700,913,1111,1451,1534):
 rec=rows[i]
 if rec['status']!='excluded93':continue
 K=tuple(tuple(k) for k in rec['keys'])
 for d,c in rec['counts']:
  if d not in (9,12,16):continue
  got=M.dp_independent_milp(K,d)
  assert got==c,(i,d,c,got)
  audits.append((i,d,c))
assert len(audits)>=10
print('PASS: 5 H9-low families / 5760 impossible; 1536 F4589 cases; independent MILPs:',len(audits))
