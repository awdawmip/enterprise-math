#!/usr/bin/env python3
"""Independent native-path witness checker for EC49FKQ.
No generator or MILP imported; accepts 9 JSON witnesses and verifies literal words.
"""
from pathlib import Path
import json
OPS='acdefg'
T=((1,2,3,1,4,5),(1,6,7,1,1,1),(2,2,8,2,2,2),(3,8,3,3,3,3),(4,2,7,4,4,4),(5,6,3,5,5,5),(6,6,8,6,6,6),(7,8,7,7,7,7),(8,8,8,8,8,8))
SIG=(0,0,4,1,16,32,8,2,0)
STEPS={'a':(-1,-1),'c':(1,2,-1,-2),'d':(2,1,-2,-1),'e':(3,1,1,-3),'f':(1,-1),'g':(2,-2)}
REQ={2:(16,32),3:(16,32),4:(1,2,4,8),5:(16,32),6:(1,2,4,8),7:(1,2,4,8),8:(1,2,4,8),9:(16,32)}
req={(h,s) for h,ls in REQ.items() for s in ls}
for i in range(9):
 data=json.loads((Path(__file__).parent/f'MIP_WITNESS_{i}.json').read_text())
 assert data['set_index']==i
 K={tuple(t) for t in data['keys']}
 chosen=data['demand_words']
 assert len(K)==6 and len(chosen)==24
 ps=set();seen=set();used=set()
 for label,w in chosen.items():
  h,s=map(int,label.split('-'))
  assert (h,s) in req and len(w)==h and set(w)<=set(OPS)
  q=0;loc=[0]*6;signs=[]
  for c in w:
   q=T[q][OPS.index(c)]
   assert q!=8
   for e in STEPS[c]:
    loc[abs(e)-1]+=1 if e>0 else -1
    signs.append(e)
    ps.add(tuple(signs))
  assert tuple(loc)==(2,0,0,0,0,0) and SIG[q]==s
  k=tuple(signs.count(e) for e in (1,2,3))
  assert k in K
  seen.add((h,s));used.add(k)
 assert seen==req
 assert len(ps)==data['cost'] and len(ps)==int(data['solver_bound'])
 print(f'INDEPENDENT_WITNESS_PASS set={i} nodes={len(ps)} used_keys={len(used)}')
print('EC49FKQ_ALL_NINE_WITNESS_PASS')
