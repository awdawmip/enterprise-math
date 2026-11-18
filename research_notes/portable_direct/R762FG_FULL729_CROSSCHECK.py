#!/usr/bin/env python3
"""Independent exact 729-terminal BRC convolution and one-character period check."""
import json
from pathlib import Path

Q=9
BRANCHES=((0,0,0),(1,0,0),(0,0,1),(1,1,0),(0,1,1),(1,1,1))
NS=(9,12,15)
LS=(18,54,162)
TARGETS={n for n in NS}|{n+L for n in NS for L in LS}

def at(a,b,c):
    return (a*Q+b)*Q+c

def v3(vec):
    vals=[]
    for x in vec:
        if x:
            t=0
            while x%3==0:
                t+=1;x//=3
            vals.append(t)
    return min(vals) if vals else None

def chi(v):
    coeff=[0]*9
    for a in range(Q):
        for b in range(Q):
            for c in range(Q):
                coeff[(b+2*c)%9]+=v[at(a,b,c)]
    for d in range(8,5,-1):
        t=coeff[d]
        coeff[d]=0
        coeff[d-3]-=t
        coeff[d-6]-=t
    return tuple(coeff[:6])

def main():
    state=[0]*(Q**3)
    state[0]=1
    observed={}
    for k in range(1,max(TARGETS)+1):
        nxt=[0]*(Q**3)
        for a in range(Q):
            for b in range(Q):
                for c in range(Q):
                    w=state[at(a,b,c)]
                    if not w:continue
                    for da,db,dc in BRANCHES:
                        nxt[at((a+da)%Q,(b+db)%Q,(c+dc)%Q)]+=w
        state=nxt
        if k in TARGETS:
            denom=3**(k//3-2)
            assert all(u%denom==0 for u in state),k
            observed[k]=chi([u//denom for u in state])
    cases=[]
    for n in NS:
        for L in LS:
            delta=[x-y for x,y in zip(observed[n+L],observed[n])]
            result=v3(delta)
            expected={18:3,54:4,162:5}[L]
            assert result==expected,(n,L,result)
            cases.append({"n":n,"L":L,"observed_valuation":result,"expected":expected})
    payload={"schema":"R762FG_FULL729_BRC_CROSSCHECK_V1", "branches":list(BRANCHES),
             "q":Q,"group_size":729,"max_power":max(TARGETS),
             "character":"X=1,Y=zeta_9,Z=zeta_9^2", "method":"complete exact integer six-branch cyclic convolution, normalize coefficientwise, evaluate character", "cases":cases, "status":"PASS / NOT_REVIEWED"}
    p=Path(__file__).with_name("R762FG_FULL729_CROSSCHECK_EVIDENCE.json")
    p.write_text(json.dumps(payload,indent=2)+"\n")
    print("PASS: 729 terminals, 9 exact character-discrepancy checks, n<=177")
if __name__=="__main__":main()
