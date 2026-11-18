#!/usr/bin/env python3
"""Standalone exact certificate checker for EC49FLA's seven-key, 24-demand, 84-native-prefix witness.
The nine-state DFA and signed microsteps are the fixed source model, with no floating arithmetic.
"""
import json
from pathlib import Path

P=Path(__file__).resolve().parent
T=((1,2,3,1,4,5),(1,6,7,1,1,1),(2,2,8,2,2,2),
   (3,8,3,3,3,3),(4,2,7,4,4,4),(5,6,3,5,5,5),
   (6,6,8,6,6,6),(7,8,7,7,7,7),(8,8,8,8,8,8))
OPS="acdefg"
SIG=(0,0,4,1,16,32,8,2,0)
STEPS={"a":(-1,-1),"c":(1,2,-1,-2),"d":(2,1,-2,-1),
       "e":(3,1,1,-3),"f":(1,-1),"g":(2,-2)}
REQ={2:(16,32),3:(16,32),4:(1,2,4,8),5:(16,32),
     6:(1,2,4,8),7:(1,2,4,8),8:(1,2,4,8),9:(16,32)}
PIN="fc0f038e7bfd12c886b4d37f900bfb770c0f61ab"
def verify():
    v=json.loads((P/"EC49FLA_84_NEW_WITNESS.json").read_text())
    assert v["frozen_scientific_pin"]==PIN
    assert v["feasible_index"]==5883 and v["cost"]==84
    keys={tuple(k) for k in v["keys"]}
    assert len(keys)==7
    found={}
    allprefix=set()
    actualkeys=set()
    for row in v["word_per_demand"]:
        h,s,w=row["h"],row["sig"],row["word"]
        assert len(w)==h and s in REQ[h] and (h,s) not in found
        q=0
        z=[0]*6
        signed=[]
        for c in w:
            assert c in OPS
            q=T[q][OPS.index(c)]
            assert q!=8
            for axis in STEPS[c]:
                signed.append(axis)
                z[abs(axis)-1]+=1 if axis>0 else -1
        assert SIG[q]==s and z==[2,0,0,0,0,0]
        key=tuple(signed.count(j) for j in (1,2,3))
        assert key in keys
        x,y,kz=key
        a=kz-1
        b=x+y-h-1
        f=h+1-y-2*kz
        g=h+1-x
        assert min(a,b,f,g)>=0
        assert w.count("a")==a and w.count("e")==kz
        assert w.count("f")==f and w.count("g")==g
        assert w.count("c")+w.count("d")==b
        path=()
        for axis in signed:
            path=path+(axis,)
            allprefix.add(path)
        actualkeys.add(key)
        found[(h,s)]=w
    assert set(found)=={(h,s) for h in REQ for s in REQ[h]}
    assert len(found)==24 and actualkeys==keys and len(allprefix)==84
    print("EC49FLA_INDEPENDENT_EXPLICIT_84_PREFIX_WITNESS_PASS",
          "demands",len(found),"keys",len(keys),"prefixes",len(allprefix))
if __name__=="__main__":
    verify()
