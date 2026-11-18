#!/usr/bin/env python3
"""Direct independent checker of the second explicit 84-prefix witness."""
from pathlib import Path
import sys,json
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'EC49FJD_RELEASE_B11_COMPLETE_20261111'))
from EC49FGW_RADIUS5_SCREEN import PIN,REQ,OPS,T,SIG,STEPS,raw_key,pref

assert PIN=='fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'
W=json.loads((HERE/'EXPLICIT_84_WITNESS_EC49FLB.json').read_text())
assert W['frozen_scientific_pin']==PIN and W['case_index']==266
demands=W['demands']
assert len(demands)==24
required={(h,s) for h,signals in REQ.items() for s in signals}
assert {(d['window'],d['signature']) for d in demands}==required
keys=set();prefixes=set()
for row in demands:
    h,s,w=row['window'],row['signature'],row['word']
    assert len(w)==h
    q=0;pos=[0]*6
    for op in w:
        q=T[q][OPS.index(op)]
        assert q!=8
        for signed_axis in STEPS[op]:
            pos[abs(signed_axis)-1] += 1 if signed_axis>0 else -1
    assert SIG[q]==s and pos==[2,0,0,0,0,0]
    k=raw_key(w)
    assert list(k)==row['key']
    keys.add(k)
    prefixes.update(pref(w))
assert len(keys)==7 and len(prefixes)==84
assert keys=={(2,1,1),(3,0,1),(3,1,1),(4,2,1),
              (5,3,1),(6,3,1),(7,3,1)}
print('EC49FLB_SECOND_EXPLICIT_84_NATIVE_WITNESS_PASS')
