#!/usr/bin/env python3
"""Independent native signed-prefix rooted trie and root allocation check of real DFS witnesses."""
import hashlib,sys,json,itertools
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent))
import VERIFY_EC49FNY_INDEPENDENT as native
src=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).resolve().parent/'master_and_radius3_cases.txt'
assert hashlib.sha256(src.read_bytes()).hexdigest()=='cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e'
ROOTS=(3,5,6,7)
W={32279:((2048,5312837,8668698,0),(5,7,15,17,19,21,13),120,156),
   32315:((0,5312869,8668698,10240),(7,15,17,19,21),141,156)}
out={}
for case,(masks,U,lb,whole) in W.items():
 words,keys=native.frozen(src,case)
 profile={r:native.table(words,keys,r) for r in ROOTS}
 options={i:[r for r in ROOTS if i in profile[r][1]] for i in U}
 assert all(options.values())
 for r,m in zip(ROOTS,masks):
  assert all(i in profile[r][1] for i in range(24) if m>>i&1)
 base={r:sum((1<<profile[r][1][i] for i in range(24) if m>>i&1)) for r,m in zip(ROOTS,masks)}
 def f(T):
  mandatory=base.copy();flex=[]
  for i in T:
   if len(options[i])==1:mandatory[options[i][0]]|=1<<profile[options[i][0]][1][i]
   else:flex.append(i)
  z=10**9
  for roots in itertools.product(*(options[i] for i in flex)):
   m=mandatory.copy()
   for i,r in zip(flex,roots):m[r]|=1<<profile[r][1][i]
   z=min(z,sum(profile[r][2][m[r]] for r in ROOTS))
  return z
 all_options={label:[r for r in ROOTS if label in profile[r][1]] for label in range(24)}
 one={label:min(profile[r][2][1<<profile[r][1][label]] for r in all_options[label]) for label in range(24)}
 order=sorted(range(24),key=lambda label:(len(all_options[label]),-one[label],label))
 assigned={i for mask in masks for i in range(24) if mask>>i&1}
 assert assigned==set(order[:len(assigned)]),(case,assigned,order)
 assert tuple(order[len(assigned):])==U
 partial={r:0 for r in ROOTS}
 root_of={i:r for r,mask in zip(ROOTS,masks) for i in range(24) if mask>>i&1}
 for i in order[:len(assigned)]:
  r=root_of[i];partial[r]|=1<<profile[r][1][i]
  assert sum(profile[r][2][partial[r]] for r in ROOTS)<=155
 assert f(())==lb
 costs={mask:f([v for j,v in enumerate(U) if mask>>j&1]) for mask in range(1<<len(U))}
 assert costs[(1<<len(U))-1]==whole
 H=[max(v for m,v in costs.items() if m.bit_count()==h) for h in range(len(U)+1)]
 strict=[(tuple(U[i] for i in range(len(U)) if m>>i&1),v) for m,v in costs.items() if v>155]
 assert len(strict)==1 and strict[0][0]==U and strict[0][1]==156,(case,strict)
 assert H[-2]<=155 and H[-1]==156
 out[str(case)]={'prefix_masks_24bit':masks,'remaining_labels_in_dfs_order':U,'H':H,'strict_subsets':len(strict),'full_cost':whole,'base_cost':lb,'exact_subsets_checked':len(costs)}
 print('INDEPENDENT_PY_PASS',case,'H',H,'subsets',len(costs),flush=True)
Path(sys.argv[2] if len(sys.argv)>2 else 'EC49FOF_INDEPENDENT_CERT.json').write_text(json.dumps(out,indent=2)+'\n')
