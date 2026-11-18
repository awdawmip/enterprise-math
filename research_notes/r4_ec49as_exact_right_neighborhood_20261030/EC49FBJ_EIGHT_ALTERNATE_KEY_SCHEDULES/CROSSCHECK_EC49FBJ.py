#!/usr/bin/env python3
"""Independent integer witness checker for compact EC49FBJ report."""
import json,sys
from pathlib import Path
S={'a':(-1,-1),'c':(1,2,-1,-2),'d':(2,1,-2,-1),'e':(3,1,1,-3),'f':(1,-1),'g':(2,-2)}
T=((1,2,3,1,4,5),(1,6,7,1,1,1),(2,2,8,2,2,2),(3,8,3,3,3,3),(4,2,7,4,4,4),(5,6,3,5,5,5),(6,6,8,6,6,6),(7,8,7,7,7,7),(8,8,8,8,8,8))
SG=(0,0,4,1,16,32,8,2,0);AB={c:i for i,c in enumerate('acdefg')};C=(18,20,33,40)
d=json.loads(Path(sys.argv[1] if len(sys.argv)>1 else 'EXACT_REPORT_EC49FBJ.json').read_text())
for name,r in sorted(d['findings'].items()):
 seen=set();paths=set();early=set();covers={h:0 for h in range(4,10)};keys=set()
 for h,w,s,k in r['selected_words']:
  assert len(w)==h and (h,w) not in seen;seen.add((h,w))
  st=0;p=[0]*6;plus=[0]*6;seq=[]
  for c in w:
   st=T[st][AB[c]]
   for a in S[c]:
    seq.append(a);p[abs(a)-1]+=1 if a>0 else -1
    if a>0:plus[a-1]+=1
  assert p==[2,0,0,0,0,0] and SG[st]==s and plus==k+[0,0,0]
  if h in covers:
   assert k==(r['L'] if h<=6 else r['M'])
   if h<9:
    for i,c in enumerate(C):
     if s&c:covers[h]|=1<<i
   elif s==16:covers[h]|=1
   elif s==32:covers[h]|=2
  else:assert w in ('fe','ge','feg','gef')
  keys.add(tuple(plus))
  for j in range(1,len(seq)+1):
   paths.add(tuple(seq[:j]))
   if h<=6:early.add(tuple(seq[:j]))
 assert list(covers.values())==[15,15,15,15,15,3] and len(keys)==5
 assert len(paths)==r['total_edges'] and len(early)==r['early_edges_in_witness']
 assert r['solver_status']==0 and r['reported_mip_gap']==0
 assert abs(r['solver_extra_dual_bound']+16-r['total_edges'])<1e-6
 print(name,r['total_edges'],r['early_edges_in_witness'],'PASS')
