#!/usr/bin/env python3
"""Independent Python dict DP for complete EC49FDH 92-edge key-pair model."""
import sys,json,time
from pathlib import Path
P=Path(__file__).resolve().parent
sys.path.insert(0,str(P.parent/'EC49FDE_ALTERNATE_BRC_LATE_KEY_EXACT_112'))
import VERIFY_EC49FDE as r
keys={4:r.L,5:r.L,6:(5,3,1),7:(6,4,1),8:(6,5,1),9:(6,4,1)}
labels=[f'{h}:{s}' for h in range(4,10) for s in r.REQ[h]]
pool={f'{h}:{s}':ww for h in range(4,10) for s,ww in r.language(h,keys[h]).items()}
assert list(pool)==labels and all(pool.values())
fixed=set().union(*(r.prefixes(w) for w in r.FIXED.values()))
child=[{}];terminal=[0];edge=[0];name=['']
for i,k in enumerate(labels):
 for w in pool[k]:
  v=0
  for c in r.native(w):
   if c not in child[v]:
    u=len(child);child[v][c]=u;child.append({});terminal.append(0)
    name.append(name[v]+c);edge.append(int(name[u] not in fixed))
   v=child[v][c]
  terminal[v]|=1<<i
start=time.monotonic()
extra,states,inspected,compatible,peak=r.independent_dp(child,terminal,edge,20)
result={'exact_optimum':len(fixed)+extra,'fixed_edges':len(fixed),
'trie_nodes':len(child),'candidate_words':sum(map(len,pool.values())),
'root_states':states,'inspected_pairs':inspected,'compatible_pairs':compatible,
'peak_states':peak,'elapsed_sec':round(time.monotonic()-start,3)}
assert (result['exact_optimum'],result['trie_nodes'],result['candidate_words'],
result['root_states'],result['inspected_pairs'])==(92,30059,5612,1048576,25815852)
print(json.dumps(result,sort_keys=True))
