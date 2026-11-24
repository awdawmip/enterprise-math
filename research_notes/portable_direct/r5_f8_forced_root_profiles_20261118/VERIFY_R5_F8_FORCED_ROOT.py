#!/usr/bin/env python3
"""Reproduce all 20 eight-state f=8 forced-first-query profiles (exact integers).
Usage: python3 VERIFY_R5_F8_FORCED_ROOT.py EXACT_R5_ALL_101_BUDGETS.json
       [EXACT_R5_EIGHT_FORCED_ROOT.cpp] [output.json]
Needs Python 3 standard library and g++ -std=c++17.
"""
import hashlib, json, subprocess, sys, tempfile
from pathlib import Path

TABLE_SHA = "50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b"
PIN = "435e77af0d180eac32bd1f9c4c464bc4010b7551"
L = 25845652773852463277015040000
U = 58182461585441404127941754880
BASE = (18, 24, 82, 34, 17)
TRIPLES = ((0,144,208),(0,16,32),(0,48,160),(0,64,128),(0,96,192),
           (1,144,208),(16,144,208),(144,160,208),(144,208,240),
           (48,144,208))
ROOT = Path(__file__).resolve().parent

def maximal(masks):
    pool = set(masks)
    return tuple(sorted(m for m in pool if not any(
        m != other and (m & other) == m for other in pool)))

def center_window_supports(centers, tau):
    # Every inclusion-maximal feasible set is represented by some left
    # endpoint equal to the smallest center in the corresponding window.
    return maximal(sum(1 << i for i,c in enumerate(centers)
                       if start <= c <= start+tau) for start in centers)

def endpoint_sweep_supports(centers, tau):
    # Doubled observation coordinates z=2y avoid half-integers.
    ends = sorted(set(x for c in centers for x in (2*c-tau,2*c+tau)))
    at_ends = [sum(1 << i for i,c in enumerate(centers)
                   if abs(z-2*c) <= tau) for z in ends]
    between = [sum(1 << i for i,c in enumerate(centers)
                   if abs(a+b-4*c) <= 2*tau)
               for a,b in zip(ends,ends[1:])]
    return maximal(at_ends+between)

def action_table(frozen, ids, tau):
    families = {}
    per_budget = {}
    for k in range(214,315):
        centers = [int(frozen[str(k)]["counts"][i]) for i in ids]
        family = center_window_supports(centers,tau)
        assert family == endpoint_sweep_supports(centers,tau), (ids,k,tau)
        per_budget[k] = family
        families[family] = min(k, families.get(family,10**9))
    actions = sorted((price,family) for family,price in families.items())
    return actions,per_budget

def expected(k, tau, triple):
    if k == 214: offset=8334
    elif k == 215: offset=8325
    elif 216 <= k <= 221: offset=8119
    elif k == 222: offset=8335
    elif 223 <= k <= 290: offset=8112
    elif 291 <= k <= 295: offset=8335
    elif 296 <= k <= 312: offset=8039
    else: offset=8335
    if tau == U-1 and k == 221 and triple in ((0,16,32),(16,144,208)):
        offset = 8324
    return k+offset

def run(executable, actions, population):
    text = (f"{population} 8\n{len(actions)}\n" +
            "\n".join(f"{k} {len(f)} " + " ".join(map(str,f))
                      for k,f in actions) + "\n")
    cp = subprocess.run([str(executable)],input=text,text=True,
                        capture_output=True,check=True)
    lines = cp.stdout.strip().splitlines()
    assert lines[0].startswith("OPT ") and lines[-1].startswith("STATES ")
    optimum = int(lines[0].split()[1])
    profiles = dict(map(lambda t:tuple(map(int,t.split())), lines[1:-1]))
    return optimum,int(lines[-1].split()[1]),profiles,hashlib.sha256(text.encode()).hexdigest()

def main():
    if len(sys.argv) not in (2,3,4):
        raise SystemExit("usage: VERIFY_R5_F8_FORCED_ROOT.py table.json [solver.cpp] [output.json]")
    raw = Path(sys.argv[1]).read_bytes()
    assert hashlib.sha256(raw).hexdigest() == TABLE_SHA
    frozen = json.loads(raw)["counts_and_cohorts"]
    assert len(frozen) == 101
    source = Path(sys.argv[2]) if len(sys.argv)>=3 else ROOT/"EXACT_R5_EIGHT_FORCED_ROOT.cpp"
    rows = []
    with tempfile.TemporaryDirectory() as directory:
        exe=Path(directory)/"solver"
        subprocess.run(["g++","-std=c++17","-O3",str(source),"-o",str(exe)],check=True)
        for triple in TRIPLES:
            ids=BASE+triple
            for endpoint,tau in (("L",L),("U-1",U-1)):
                actions,per_budget=action_table(frozen,ids,tau)
                optimum,states,profile,stdin_sha=run(exe,actions,len(ids))
                assert optimum == 8335
                # The Bellman continuation value depends on the support
                # family, while a forced first budget pays its own price.
                by_family={family:profile[cheapest]-cheapest for cheapest,family in actions}
                exact={str(k):k+by_family[per_budget[k]] for k in range(214,315)}
                assert all(exact[str(k)] == expected(k,tau,triple) for k in range(214,315))
                assert min(exact.values())==8335
                excluded=[k for k in range(214,315) if exact[str(k)]>8343]
                assert len(excluded) == (78 if endpoint=="U-1" and triple in
                       ((0,16,32),(16,144,208)) else 77)
                rows.append({"added":list(triple),"endpoint":endpoint,"tau":str(tau),
                    "minimax":optimum,"states":states,"actions":len(actions),
                    "stdin_sha256":stdin_sha,"forced_101":exact,"excluded":excluded})
                print("VERIFIED",triple,endpoint,states,len(excluded),file=sys.stderr,flush=True)
    output={"status":"PASS_R5_F8_10x2_FORCED_ROOT_EXACT","source_pin":PIN,
            "table_sha256":TABLE_SHA,"hypotheses_base":list(BASE),"f":8,
            "support_checks":20*101,"cases":rows}
    out=json.dumps(output,sort_keys=True,indent=2)+"\n"
    if len(sys.argv)==4: Path(sys.argv[3]).write_text(out)
    else: print(out)
    print("PASS_R5_F8_10x2_FORCED_ROOT_EXACT",file=sys.stderr)

if __name__=="__main__":
    main()
