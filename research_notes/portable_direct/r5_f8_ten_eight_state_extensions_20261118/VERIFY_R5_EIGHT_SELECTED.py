#!/usr/bin/env python3
"""Exact eight-state R5 f=8 Bellman verification: all original query budgets."""
import hashlib
import json
import subprocess
import sys
import tempfile
from pathlib import Path

SHA = "50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b"
L = 25845652773852463277015040000
U = 58182461585441404127941754880
BASE = (18, 24, 82, 34, 17)
TRIPLES = ((0,144,208), (0,16,32), (0,48,160), (0,64,128),
           (0,96,192), (1,144,208), (16,144,208), (144,160,208),
           (144,208,240), (48,144,208))

def maximal(masks):
    pool = set(masks)
    return tuple(sorted(m for m in pool if not any(
        m != t and (m & t) == m for t in pool)))

def windows(centers, tau):
    return maximal(sum(1 << i for i,c in enumerate(centers)
                       if left <= c <= left + tau) for left in centers)

def sweep(centers, tau):
    # Exact doubled response coordinates: closed endpoints and open interiors.
    endpoints = sorted(set(z for c in centers for z in (2*c-tau,2*c+tau)))
    at_endpoints = [sum(1 << i for i,c in enumerate(centers)
                        if abs(z-2*c) <= tau) for z in endpoints]
    in_between = [sum(1 << i for i,c in enumerate(centers)
                      if abs(a+b-4*c) <= 2*tau)
                  for a,b in zip(endpoints,endpoints[1:])]
    return maximal(at_endpoints + in_between)

def action_families(table, ids, tau):
    cheapest={}
    for k in range(214,315):
        centers=[int(table[str(k)]["counts"][h]) for h in ids]
        supports=windows(centers,tau)
        assert supports == sweep(centers,tau), (ids,k,tau)
        cheapest[supports]=min(k,cheapest.get(supports,10**9))
    return sorted((k,supports) for supports,k in cheapest.items())

def solve(executable, actions):
    lines=["8 8",str(len(actions))]
    lines += [f"{k} {len(masks)} " + " ".join(map(str,masks))
              for k,masks in actions]
    result=subprocess.run([str(executable)],input="\n".join(lines)+"\n",
                          text=True,capture_output=True,check=True)
    fields=dict(s.split("=",1) for s in result.stdout.split()[1:] if "=" in s)
    return {"cost":int(fields["cost"]), "memo_states":int(fields["states"]),
            "distinct_action_families":len(actions)}

def main():
    if len(sys.argv)!=3:
        raise SystemExit("usage: python3 VERIFY_R5_EIGHT_SELECTED.py EXACT_R5_ALL_101_BUDGETS.json EXACT_EIGHT_SUBSET.cpp")
    raw=Path(sys.argv[1]).read_bytes()
    assert hashlib.sha256(raw).hexdigest()==SHA
    table=json.loads(raw)["counts_and_cohorts"]
    with tempfile.TemporaryDirectory() as temp:
        exe=Path(temp)/"exact_eight"
        subprocess.run(["g++","-O3","-std=c++17",sys.argv[2],"-o",str(exe)],check=True)
        rows=[]
        for triple in TRIPLES:
            ids=BASE+triple
            left=solve(exe,action_families(table,ids,L))
            right=solve(exe,action_families(table,ids,U-1))
            assert left["cost"]==8335 and right["cost"]==8335, (ids,left,right)
            rows.append({"added":list(triple),"left":left,"right":right})
    print(json.dumps({"status":"PASS_R5_TEN_EIGHT_STATE_F8_BOTH_ENDPOINTS",
       "science_commit":"435e77af0d180eac32bd1f9c4c464bc4010b7551",
       "input_sha256":SHA,"base":list(BASE),"f":8,
       "L":str(L),"U_exclusive":str(U),
       "coverage":"10 triples x 2 endpoints x 101 independently swept/windowed actions",
       "rows":rows},indent=2,sort_keys=True))

if __name__=="__main__":
    main()
