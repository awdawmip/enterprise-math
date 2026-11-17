#!/usr/bin/env python3
"""Exact R5 f=8 twelve-hypothesis endpoint checker.

Place the frozen EXACT_R5_ALL_101_BUDGETS.json in this directory,
and compile the pinned VERIFY_EXACT_SMALL_MINIMAX.cpp as ./exact_small
using g++ -O3 -DNDEBUG -std=c++17. Run python RECOMPUTE_TWELVE.py.
"""
import hashlib, json, subprocess, tempfile
from pathlib import Path
P=Path(__file__).resolve().parent
SHA="50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b"
L=25845652773852463277015040000
U=58182461585441404127941754880
H0=(18,24,82,34,17)
NAMES=["H8","H9","H10","H11","H12"]
SETS=[
 H0+(0,144,208),
 H0+(0,144,208,1),
 H0+(0,1,144,208,255),
 H0+(0,1,2,144,208,255),
 H0+(0,1,2,3,144,208,255),
]
EXPECTED_RIGHT=[1206404,5020198,4805671,6398337,9769571]
def families(T,H,tau):
    cheapest={}
    for k in range(214,315):
        vals={}
        for j,h in enumerate(H):
            v=int(T[str(k)]["counts"][h])
            vals[v]=vals.get(v,0)|(1<<j)
        supports={sum(mask for v,mask in vals.items() if lo<=v<=lo+tau) for lo in vals}
        maximum=tuple(sorted(x for x in supports
                    if not any(x!=y and x&y==x for y in supports)))
        cheapest.setdefault(maximum,k)
    return sorted(((k,s) for s,k in cheapest.items()),key=lambda x:x[0])
def calculate(T,H,tau):
    acts=families(T,H,tau)
    lines=[f"{len(H)} {len(acts)}"]
    lines += [f"{k} {len(s)} "+ " ".join(map(str,s)) for k,s in acts]
    with tempfile.NamedTemporaryFile("w",suffix=".actions") as t:
        t.write("\n".join(lines)+"\n");t.flush()
        cmd=[str(P/"exact_small"),t.name,"8"]
        res=subprocess.run(cmd,capture_output=True,text=True,check=True)
    fields=dict(x.split("=",1) for x in res.stdout.split() if "=" in x)
    return dict(V=int(fields["V"]),states=int(fields["states"]),
                actions=len(acts),costs=[k for k,_ in acts])
def main():
    raw=(P/"EXACT_R5_ALL_101_BUDGETS.json").read_bytes()
    assert hashlib.sha256(raw).hexdigest()==SHA
    T=json.loads(raw)["counts_and_cohorts"]
    assert len(T)==101
    H12=H0+(0,1,2,3,144,208,255)
    expected_costs={214,215,216,217,221,222,223,291,295,296}
    right=calculate(T,H12,U-1)
    left=calculate(T,H12,L)
    assert right["V"]==left["V"]==8335
    assert right["states"]==9769571 and left["states"]==5193976
    assert set(right["costs"])==expected_costs
    assert 291 in right["costs"]
    results={"H12":list(H12),"left":left,"right":right}
    for H,name,states in zip(SETS,NAMES,EXPECTED_RIGHT):
        res=calculate(T,H,U-1)
        assert res["V"]==8335 and res["states"]==states
        results[name]=res
    print("PASS_R5_F8_TWELVE_HYPOTHESES_ENTIRE_CHAMBER",json.dumps(results,sort_keys=True))
if __name__=="__main__":main()
