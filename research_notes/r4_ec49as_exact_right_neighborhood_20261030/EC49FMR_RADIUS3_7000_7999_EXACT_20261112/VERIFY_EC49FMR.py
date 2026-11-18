#!/usr/bin/env python3
"""EC49FMR exact packed-vector and native BRC constructive witness check."""
from pathlib import Path
from collections import Counter
import hashlib,base64,json,zlib
D=Path(__file__).resolve().parent
a=json.loads((D/'EXACT_VECTOR_EC49FMR.json').read_text())
v=zlib.decompress(base64.b64decode(a['cost_uint8_zlib_base64']))
assert len(v)==a['count']==1000 and a['index_start']==7000 and a['index_end_inclusive']==7999
assert hashlib.sha256(v).hexdigest()==a['cost_uint8_sha256']
assert (min(v),max(v),[i+7000 for i,c in enumerate(v) if c==min(v)])==(110,138,[7145,7157])
assert {str(k):n for k,n in Counter(v).items()}==a['histogram']
print('VECTOR_PASS',len(v),min(v),max(v))
r=D/'EXACT_NATIVE_OUTPUT_7000_7999.txt'
if r.exists():
    lines=[s.split() for s in r.read_text().splitlines()]
    assert len(lines)==1000 and [int(s[0]) for s in lines]==list(range(7000,8000))
    assert bytes(int(s[1]) for s in lines)==v
    assert hashlib.sha256(r.read_bytes()).hexdigest()==a['complete_raw_rows_sha256']
    print('RAW_PASS',len(lines))
OPS='acdefg'
T=((1,2,3,1,4,5),(1,6,7,1,1,1),(2,2,8,2,2,2),
   (3,8,3,3,3,3),(4,2,7,4,4,4),(5,6,3,5,5,5),
   (6,6,8,6,6,6),(7,8,7,7,7,7),(8,8,8,8,8,8))
SIG=(0,0,4,1,16,32,8,2,0)
STEPS={'a':(-1,-1),'c':(1,2,-1,-2),'d':(2,1,-2,-1),
       'e':(3,1,1,-3),'f':(1,-1),'g':(2,-2)}
REQ={2:(16,32),3:(16,32),4:(1,2,4,8),5:(16,32),
     6:(1,2,4,8),7:(1,2,4,8),8:(1,2,4,8),9:(16,32)}
w=json.loads((D/'WITNESS_7145_EC49FMR.json').read_text())
assert a['scientific_input_pin']==w['scientific_input_pin']=='fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'
assert w['case_index']==7145 and w['cost']==v[7145-7000]==110 and len(w['words'])==24
labels=set();keys=set();prefixes=set();roots={}
for h,s,word in w['words']:
    assert len(word)==h and s in REQ[h]
    q=0;z=[0]*6;native=[]
    for op in word:
        assert op in OPS
        q=T[q][OPS.index(op)]
        assert q!=8
        for d in STEPS[op]:
            z[abs(d)-1]+=1 if d>0 else -1
            native.append(d)
    assert SIG[q]==s and z==[2,0,0,0,0,0]
    labels.add((h,s))
    keys.add(tuple(native.count(i) for i in (1,2,3)))
    p=[bytes(x+4 for x in native[:j]) for j in range(1,len(native)+1)]
    prefixes.update(p)
    roots.setdefault(p[0].hex(),set()).update(p)
assert labels=={(h,s) for h in REQ for s in REQ[h]}
assert len(keys)==7 and len(prefixes)==110
assert {k:len(v) for k,v in roots.items()}==w['root_costs']=={'05':48,'06':44,'07':18}
print('NATIVE_WITNESS_PASS',len(labels),len(prefixes),len(keys))
print('EC49FMR_VERIFICATION_PASS')
