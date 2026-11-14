#!/usr/bin/env python3
"""Independent per-depth integer maximum clique validation, no C++ bound code reused."""
import json
from pathlib import Path
p=Path(__file__).resolve().parent
src=json.loads((p/'EC49EXY_EXACT_CAPS.json').read_text())
familyid={(f['h'],*f['key']):f['id'] for f in src['family']}
caps=src['max_lcp_primitive_steps']
match={}
for ln in (p.parent/'EC49EXS_H8_M5_OBSERVER_SIGNED_MATCH/EC49EXS_MATCH_TABLE.txt').read_text().splitlines()[1:]:
 n,h1,h2,h3,u,v,w,old,new=map(int,ln.split())
 match[(tuple([h1,h2]+([h3] if n==3 else [])),(u,v,w))]=new

def check(line):
 values=list(map(int,line.split()))
 expected,exs,a,b,c,d=values[:6]
 keys=[tuple(values[6+i*3:9+i*3]) for i in range(5)]
 hs=[(a,b),(c,d)]+[(h,) for h in range(2,9) if h not in (a,b,c,d)]
 assert len(hs)==5
 Ms=[];Rs=[];Ls=[]
 for k,wins in zip(keys,hs):
  types=[4 if sum(k[:2])-h-1>=1 else 2 for h in wins]
  m=sum(types)
  Ms.append(m)
  Rs.append(m-match.get((wins,k),0))
  Ls.append(2*(sum(k)-1))
 xcap={}
 for i in range(5):
  for j in range(i+1,5):
   xcap[i,j]=max(caps[familyid[h,*keys[i]]][familyid[g,*keys[j]]] for h in hs[i] for g in hs[j])
 total=0
 for depth in range(1,max(Ls)+1):
  q=[(0 if depth>L else (M if depth>=L-2 else R if depth==L-3 else 1)) for L,M,R in zip(Ls,Ms,Rs)]
  best=0
  for mask in range(1,32):
   members=[i for i in range(5) if mask & 1<<i]
   if all(xcap[i,j]<depth for i in members for j in members if i<j):
    best=max(best,sum(q[i] for i in members))
  total+=best
 assert total==expected,(total,expected,line)
 return total
rows=(p/'EC49EXY_DOUBLE_CANDIDATES.tsv').read_text().splitlines()[1:]
sel=rows[::101]
sel+=(p/'EC49EXY_NEW_EXCLUSION_SAMPLES.tsv').read_text().splitlines()[1:]
for x in sel:check(x)
report={'status':'PASS','implementation':'independent_python_direct_depth_and_clique','checked_double_schedules':len(sel),'survivors_sampled':len(sel)-10,'newly_excluded_samples':10,'all_bounds_match':True}
(p/'EC49EXY_INDEPENDENT_SCHEDULE_AUDIT.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report))
