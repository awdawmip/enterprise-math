#!/usr/bin/env python3
"""Exact integer verifier for PREFIX-858. Python 3 standard library only."""
import json
from pathlib import Path

def residues(p,q):
    return {0} | {pow(2,i,q) for i in range(p)}

def oracle(p,q1):
    a=residues(p,q1)
    r=((1<<p)-1)%q1
    matches=[(u,v) for u in sorted(a) for v in sorted(a) if (u+v)%q1==r]
    return {"p":p,"q1":q1,"q2":(1<<p)-1,"good":not matches,
            "witness":list(matches[0]) if matches else None,"A":sorted(a),"r":r}

def direct(p,q1):
    n=1<<p
    seen={}
    for u in range(n):
        for v in [u]+[u^(1<<i) for i in range(p)]:
            key=(u%q1,v%(n-1))
            if key in seen and seen[key]!=v:
                return False
            seen[key]=v
    return True

def run():
    family=[]
    for k in range(4,17):
        q1=(1<<k)-1
        for multiple in (2,3,5,8):
            p=multiple*k-1
            assert oracle(p,q1)["good"],(p,k)
            family.append({"k":k,"p":p,"q1":q1,"q2_bits":p})
    four=[]
    for p in range(4,97):
        ok=oracle(p,15)["good"]
        assert ok==(p%4==3),(p,ok)
        four.append({"p":p,"works":ok})
    lower=[]
    for p in (7,11,15,19,23):
        rows=[oracle(p,q) for q in (3,5,7,9,11,13,15)]
        assert [x["q1"] for x in rows if x["good"]]==[15]
        lower.append({"p":p,"tested":rows})
    independent=[]
    for p in (4,5,6,7,8):
        for q in range(3,32,2):
            a=oracle(p,q)["good"]
            b=direct(p,q)
            assert a==b,(p,q,a,b)
            independent.append({"p":p,"q1":q,"good":a})
    a=sorted(residues(7,15))
    r=((1<<7)-1)%15
    b=sorted({(r-x)%15 for x in a})
    assert a==[0,1,2,4,8] and b==[3,5,6,7,14] and not set(a)&set(b)
    return {"status":"ALL_EXACT_ASSERTIONS_PASSED",
        "scope":"named binary BRC scalar state; no-op or one-bit flip per heartbeat; known baseline, odd moduli",
        "orbit_criterion":"r not in A+A modulo q1; r=(2^p-1) modulo q1; A={0} union {2^i modulo q1:0<=i<p}",
        "infinite_family":"k>=4, p>=k, p=(k-1) mod k; q1=2^k-1; q2=2^p-1",
        "four_bit_family":"p>=7, p=3 mod 4; q1=15 is minimum odd q1 with q2=2^p-1",
        "p7_example":{"first_predecessor_residues":a,"second_predecessor_residues":b},
        "family_cases":family,"four_bit_residue_cases":four,
        "lower_bound_witnesses":lower,"direct_crosschecks":independent,
        "counts":{"family":len(family),"residue":len(four),
                  "small_q":len(lower)*7,"direct":len(independent)}}

if __name__=="__main__":
    result=run()
    path=Path(__file__).with_name("PREFIX858_R6_ORBIT_TWO_READ_RESULTS.json")
    path.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(result["status"],result["counts"])
