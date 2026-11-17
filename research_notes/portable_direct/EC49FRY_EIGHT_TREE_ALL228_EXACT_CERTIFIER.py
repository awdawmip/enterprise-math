#!/usr/bin/env python3
"""EC49FRY: verify 8 original physical-named BRC witnesses and all 13 exact Bellman polygon vertices.

Extract the self-contained 23-file evidence archive, then run this script with
the extracted directory as its first argument. --solve-vertices recomputes each
exact 228-observer Bellman point in its own Python subprocess; on constrained
hosts call the original solver separately at each vertex instead.
Does not replace the native 228 response vectors by response quotients.
"""
import sys, json, subprocess, hashlib
from pathlib import Path
from fractions import Fraction as F
from collections import Counter
root=Path(sys.argv[1]).resolve()
sys.path.insert(0,str(root/'code'))
from EC49FRW_TWO_PRICE_SOLVER import V,PIN
assert PIN=='fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'
assert len(V)==228 and all(len(v)==141 for v in V)
src={'frozen_original_master.txt':'cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e','EC49FPG_PROFILE.csv':'a61a3ee4d2f13f9d216f52cd3529c72d395c1250bfb1d7ae96a1adf5a6837c1f'}
for f,h in src.items():assert hashlib.sha256((root/'source'/f).read_bytes()).hexdigest()==h
witnesses={
 'L32':('EC49FRW_T32_FULL_TREE.json',(296,141,11),3),
 'L34':('EC49FRW_T34_FULL_TREE.json',(296,11,141),3),
 'H32':('EC49FRX_HIGH32_FULL_TREE.json',(297,141,15),3),
 'H34':('EC49FRX_HIGH34_FULL_TREE.json',(297,15,141),3),
 'M32':('EC49FRY_M32_FULL_TREE.json',(304,141,36),4),
 'M34':('EC49FRY_M34_FULL_TREE.json',(304,36,141),4),
 'N32':('EC49FRY_N32_FULL_TREE.json',(306,141,41),4),
 'N34':('EC49FRY_N34_FULL_TREE.json',(306,41,141),4)}
for name,(fn,expected,max_expected) in witnesses.items():
 j=json.loads((root/'evidence'/fn).read_text())
 tree=j.get('tree',j);cnt=Counter();mx=0
 for s in range(141):
  node=tree;seen=set();depth=0
  while 'named_observer' in node:
   q=node['named_observer'];assert isinstance(q,int) and q in range(228) and q not in seen
   cnt[q]+=1;seen.add(q);depth+=1
   node=node['children'][str(V[q][s])]
  assert node['leaf']==s
  mx=max(mx,depth)
 assert (sum(cnt.values()),cnt[32],cnt[34])==expected and mx==max_expected
 print('TREE_OK',name,'141/141',expected,'max depth',mx,flush=True)

vertices=[('0','0','296'),('1/2','0','451/2'),('0','1/2','451/2'),('1/4','1/4','258'),('1/2','1/4','891/4'),('1/4','1/2','891/4'),('1/3','1/3','245'),('1/2','1/3','443/2'),('1/3','1/2','443/2'),('2/5','2/5','1166/5'),('1/2','2/5','2191/10'),('2/5','1/2','2191/10'),('1/2','1/2','215')]
for aa,bb,expected in vertices:
 a,b=F(aa),F(bb);M=max(a,b);m=min(a,b)
 f=F(296)-141*M-11*m if m<=F(1,4) else (F(297)-141*M-15*m if m<=F(1,3) else (F(304)-141*M-36*m if m<=F(2,5) else F(306)-141*M-41*m))
 assert f==F(expected)
 if '--solve-vertices' in sys.argv:
  cp=subprocess.run([sys.executable,str(root/'code'/'EC49FRW_TWO_PRICE_SOLVER.py'),aa,bb],check=True,capture_output=True,text=True,timeout=45)
  z=json.loads(cp.stdout.strip().splitlines()[-1])
  assert F(z['Bellman_integer_value'],z['denominator'])==f
  print('BELLMAN_OK',aa,bb,expected,'memo subsets',z['states'],flush=True)
print('COMPLETE: 8 full original native 141-state tree replays and 13 exact polytope vertex values (recompute flag optional)')
