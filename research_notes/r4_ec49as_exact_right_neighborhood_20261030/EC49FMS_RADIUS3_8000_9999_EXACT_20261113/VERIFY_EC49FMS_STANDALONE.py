#!/usr/bin/env python3
"""Standalone exact-vector and native signed-X6 constructive-witness checker."""
import base64,collections,hashlib,json,zlib
from pathlib import Path
D=Path(__file__).resolve().parent
v=json.loads((D/'EXACT_VECTOR_EC49FMS.json').read_text())
cost=zlib.decompress(base64.b64decode(v['cost_uint8_zlib_base64']))
assert len(cost)==v['count']==2000 and v['index_start']==8000 and v['index_end_inclusive']==9999
assert hashlib.sha256(cost).hexdigest()==v['cost_uint8_sha256']
assert min(cost)==v['min_cost']==126 and max(cost)==v['max_cost']==168
assert [8000+i for i,x in enumerate(cost) if x==126]==v['argmins']==[9004]
assert {str(k):n for k,n in collections.Counter(cost).items()}==v['histogram']
raw=D/'EXACT_NATIVE_OUTPUT_8000_9999.txt'
if raw.exists():
 assert hashlib.sha256(raw.read_bytes()).hexdigest()==v['complete_raw_rows_sha256']
 rows=[s.split() for s in raw.read_text().splitlines()]
 assert len(rows)==2000 and [int(r[0]) for r in rows]==list(range(8000,10000))
 assert bytes(int(r[1]) for r in rows)==cost
 assert {str(k):n for k,n in collections.Counter(int(r[3]) for r in rows).items()}==v['first_root_counts']
OPS='acdefg'
T=((1,2,3,1,4,5),(1,6,7,1,1,1),(2,2,8,2,2,2),
   (3,8,3,3,3,3),(4,2,7,4,4,4),(5,6,3,5,5,5),
   (6,6,8,6,6,6),(7,8,7,7,7,7),(8,8,8,8,8,8))
SIG=(0,0,4,1,16,32,8,2,0)
STEPS={'a':(-1,-1),'c':(1,2,-1,-2),'d':(2,1,-2,-1),
       'e':(3,1,1,-3),'f':(1,-1),'g':(2,-2)}
REQ={2:(16,32),3:(16,32),4:(1,2,4,8),5:(16,32),
     6:(1,2,4,8),7:(1,2,4,8),8:(1,2,4,8),9:(16,32)}
W=json.loads((D/'WITNESS_9004_EC49FMS.json').read_text())
assert W['scientific_input_pin']==v['scientific_input_pin']=='fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'
assert W['case_index']==9004 and W['cost']==cost[1004] and len(W['words'])==24
prefixes=set();roots=collections.defaultdict(set);labels=set();keys=set()
for h,s,word in W['words']:
 assert len(word)==h and s in REQ[h] and all(op in OPS for op in word)
 q=0;z=[0]*6;step=[]
 for op in word:
  q=T[q][OPS.index(op)]
  assert q!=8
  for a in STEPS[op]:
   z[abs(a)-1]+=(1 if a>0 else -1)
   step.append(a)
 assert SIG[q]==s and z==[2,0,0,0,0,0]
 keys.add(tuple(step.count(i) for i in (1,2,3)))
 labels.add((h,s))
 for i in range(1,len(step)+1):
  p=bytes(x+4 for x in step[:i]);prefixes.add(p);roots[f'{p[0]:02x}'].add(p)
assert labels=={(h,s) for h in REQ for s in REQ[h]}
assert len(keys)==7 and len(prefixes)==W['cost']==126
assert {k:len(s) for k,s in roots.items()}=={k:n for k,n in W['root_costs'].items() if n>0}=={'03':18,'05':54,'06':54}
print('PASS: 2000 integer cost entries; 24 lawful words; 126 signed-native prefixes; 7 keys')
