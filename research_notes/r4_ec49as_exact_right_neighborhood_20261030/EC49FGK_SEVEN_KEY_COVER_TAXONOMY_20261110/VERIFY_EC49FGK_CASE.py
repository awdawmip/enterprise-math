#!/usr/bin/env python3
"""Exact independent witness replay for EC49FGK one seven-key allowlist, 102 native prefixes."""
from pathlib import Path
import json
OPS='acdefg'
T=((1,2,3,1,4,5),(1,6,7,1,1,1),(2,2,8,2,2,2),(3,8,3,3,3,3),(4,2,7,4,4,4),(5,6,3,5,5,5),(6,6,8,6,6,6),(7,8,7,7,7,7),(8,8,8,8,8,8))
SIG=(0,0,4,1,16,32,8,2,0)
STEPS={'a':(-1,-1),'c':(1,2,-1,-2),'d':(2,1,-2,-1),'e':(3,1,1,-3),'f':(1,-1),'g':(2,-2)}
REQ={2:(16,32),3:(16,32),4:(1,2,4,8),5:(16,32),6:(1,2,4,8),7:(1,2,4,8),8:(1,2,4,8),9:(16,32)}
data=json.loads(Path(__file__).with_name('WITNESS_WITHOUT_311_EC49FGK.json').read_text())
assert data['frozen_scientific_pin']=='fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'
seen=set();keys=set();labels=set()
for row in data['demands']:
    h,s,w=row['window'],row['signature'],row['word']
    assert len(w)==h and (h,s) not in labels
    labels.add((h,s))
    state=0;point=[0]*6;path=[];plus=[0,0,0]
    for op in w:
        assert op in OPS
        state=T[state][OPS.index(op)]
        assert state!=8
        for a in STEPS[op]:
            path.append(a);seen.add(tuple(path))
            point[abs(a)-1]+=1 if a>0 else -1
            if 0<a<=3:plus[a-1]+=1
    assert point==[2,0,0,0,0,0] and SIG[state]==s,(h,s,w)
    keys.add(tuple(plus))
assert labels=={(h,s) for h,ss in REQ.items() for s in ss}
assert len(seen)==102 and len(keys)==7
assert sorted(keys)==sorted(map(tuple,data['allowed_keys']))
assert (3,1,1) not in keys
print('PASS',len(labels),'frozen_labels',len(keys),'raw_keys',len(seen),'signed_X6_prefix_edges')
