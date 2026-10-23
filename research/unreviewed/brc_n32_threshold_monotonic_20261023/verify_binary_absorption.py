#!/usr/bin/env python3
"""Exact Fraction and 16-mask checks for the N32 binary absorption lemma.

Finite tests complement, but cannot replace, the uniform proof.
"""
from fractions import Fraction as F
from itertools import combinations
import json
from pathlib import Path

GOOD={3,6,10,12}  # {0,1},{1,2},{1,3},{2,3}

def exact_dp(z,word):
    laws={0:(F(0),F(1+z,3),F(1-z,3),F(1,3)),
          2:(F(1,3),F(1,3),F(0),F(1,3))}
    state={0:F(1)}
    for act in word:
        out={}
        for mask,p in state.items():
            for label,q in enumerate(laws[act]):
                if not q:
                    continue
                dest=mask|(1<<label)
                out[dest]=out.get(dest,F(0))+p*q
        state=out
    return sum((p for mask,p in state.items() if mask in GOOD),F(0))

def closed(z,s,r):
    assert s>=1 and r>=1
    a=(1+z)/3
    b=(1-z)/3
    c=F(1,3)
    return ((2**r-3)*a**s+2**r*(a+c)**s+(a+b)**s
            +(b+c)**s-2*c**s)/3**r

def main():
    zs=(F(0),F(1,7),F(1,3),F(1,2),F(7,10),F(9,10),F(999,1000),F(1))
    counts={"full_16_state_agreement":0,"strict_action0_margins":0,
            "strict_action2_margins":0,"order_invariance":0}
    for z in zs:
        for s in range(1,9):
            for r in range(1,7):
                val=closed(z,s,r)
                assert exact_dp(z,[0]*s+[2]*r)==val
                counts["full_16_state_agreement"]+=1
                if r>=2:
                    assert closed(z,s+1,r)-val<=-F(1,3**(s+r+1))
                    assert closed(z,s,r+1)-val<=-F(4,3**(s+r+1))
                    counts["strict_action0_margins"]+=1
                    counts["strict_action2_margins"]+=1
    for z in (F(0),F(1,2),F(1)):
        for s in range(1,5):
            for r in range(1,5):
                n=s+r
                for ix in combinations(range(n),r):
                    v=[0]*n
                    for j in ix:
                        v[j]=2
                    assert exact_dp(z,v)==closed(z,s,r)
                    counts["order_invariance"]+=1
    report={"schema":"EM_BRC_N32_BINARY_ABSORPTION_AUTHOR_CHECKS_V1",
            "arithmetic":"exact fractions only",
            "observer":"all 16 occupancy masks; G={3,6,10,12}",
            "counts":counts,
            "limitations":"finite checks, not independent review or native X6 proof"}
    Path(__file__).with_name("BINARY_ABSORPTION_CHECKS.json").write_text(
        json.dumps(report,ensure_ascii=False,indent=2,sort_keys=True)+"\n",
        encoding="utf-8")
    print(json.dumps(counts,sort_keys=True))

if __name__=="__main__":
    main()
