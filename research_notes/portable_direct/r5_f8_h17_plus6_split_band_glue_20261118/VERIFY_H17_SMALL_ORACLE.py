#!/usr/bin/env python3
"""Independent explicit-tuple Bellman oracle versus packed 128-bit C++ engine."""
import json,hashlib,subprocess,sys,tempfile
from functools import lru_cache
from pathlib import Path
SRC_SHA='50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b'
T=58182461585441404127941754879
K=(214,215,216,223,296)
SUBSETS=((18,5,6),(24,34,17),(82,144,208),(0,1,2))
def make_actions(table,H):
 out=[]
 for k in K:
  C=[int(table[str(k)]['counts'][h]) for h in H]
  unique={v:0 for v in C}
  for i,v in enumerate(C):unique[v]|=1<<i
  candidates={sum(mask for c,mask in unique.items() if start<=c<=start+T) for start in unique}
  maximal=tuple(sorted(s for s in candidates if not any(s!=z and s&z==s for z in candidates)))
  out.append((k,maximal))
 return out
def oracle(acts,n,f):
 @lru_cache(None)
 def rec(e):
  if sum(v<=f for v in e)<=1:return 0
  best=10**9
  for k,masks in acts:
   costs=[]
   for mask in masks:
    nxt=tuple(min(f+1,v+(1 if not(mask>>i&1) else 0)) for i,v in enumerate(e))
    if nxt==e:break
    costs.append(rec(nxt))
   else:
    best=min(best,k+max(costs))
  return best
 return rec((0,)*n)
if __name__=='__main__':
 if len(sys.argv)!=3:raise SystemExit('usage: python verifier.py frozen.json cpp_binary')
 raw=Path(sys.argv[1]).read_bytes();assert hashlib.sha256(raw).hexdigest()==SRC_SHA
 table=json.loads(raw)['counts_and_cohorts']
 results=[]
 with tempfile.TemporaryDirectory() as td:
  for H in SUBSETS:
   acts=make_actions(table,H)
   path=Path(td)/'actions.txt'
   path.write_text(f'{len(H)} {len(acts)}\n'+'\n'.join(f'{k} {len(m)} '+' '.join(map(str,m)) for k,m in acts)+'\n')
   for f in range(4):
    py=oracle(acts,len(H),f)
    p=subprocess.run([sys.argv[2],str(path),str(f)],capture_output=True,text=True,check=True)
    cpp=int(p.stdout.split(' V=')[1].split()[0]); assert py==cpp,(H,f,py,cpp)
    results.append({'H':H,'f':f,'value':py})
 print(json.dumps({'status':'PASS','comparisons':len(results),'exact_cases':results},indent=2))
