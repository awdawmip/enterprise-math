#!/usr/bin/env python3
"""Verify and optionally recompute the complete anchored R5 f=8 seven-state star.
Run: g++ -O3 -std=c++17 VERIFY_SEVEN.cpp -o verify_seven
     python3 RECOMPUTE_ANCHORED_SEVEN.py --input EXACT_R5_ALL_101_BUDGETS.json --solver ./verify_seven --spot 4
Use --all to recompute all 500 endpoint games (batchable external runner).
"""
import argparse
import base64
import hashlib
import json
import subprocess
import zlib
from pathlib import Path

H0 = (18,24,82,34,17)
L = 25845652773852463277015040000
U = 58182461585441404127941754880
PIN_SHA256 = "50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b"
CANDIDATES = [i for i in range(256) if i not in H0 and i != 0]

def read_rows(certificate, side):
    encoded = certificate[side + "_rows_zlib_base64"]
    raw = zlib.decompress(base64.b64decode(encoded))
    assert hashlib.sha256(raw).hexdigest() == certificate[side + "_rows_json_sha256"]
    rows = json.loads(raw)
    assert len(rows) == 250 and [r[0] for r in rows] == CANDIDATES
    assert all(r[1] == 8335 and r[2] > 0 and r[3] > 0 for r in rows)
    assert sum(r[2] for r in rows) == certificate[side + "_aggregate_states"]
    return rows

def actions(counts, names, tau):
    distinct = {}
    for k in range(214,315):
        centers = {}
        for i,h in enumerate(names):
            c=counts[k][h]
            centers[c] = centers.get(c,0) | (1 << i)
        masks = set()
        for center in centers:
            support = 0
            for other,flags in centers.items():
                if center <= other <= center + tau: support |= flags
            masks.add(support)
        maximal = tuple(sorted(m for m in masks if not any(m!=n and (m&n)==m for n in masks)))
        distinct.setdefault(maximal,k)
    return sorted(((k,supports) for supports,k in distinct.items()), key=lambda x:x[0])

def solve(counts,h,tau,solver):
    query = actions(counts, H0+(0,h), tau)
    inp = "7 " + str(len(query)) + "\n"
    for k,supports in query:
        inp += f"{k} {len(supports)} " + " ".join(map(str,supports)) + "\n"
    out = subprocess.run([str(solver),"8"],input=inp,check=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True,timeout=60)
    val = dict(x.split("=",1) for x in out.stdout.split() if "=" in x)
    assert int(val["n"])==7 and int(val["f"])==8
    return [h,int(val["V"]),int(val["states"]),int(val["actions"])]

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--input",type=Path,required=True)
    p.add_argument("--certificate",type=Path,default=Path("RESULTS_COMPACT_ANCHORED_SEVEN.json"))
    p.add_argument("--solver",type=Path,default=Path("./verify_seven"))
    p.add_argument("--spot",type=int,default=0)
    p.add_argument("--all",action="store_true")
    a=p.parse_args()
    assert hashlib.sha256(a.input.read_bytes()).hexdigest()==PIN_SHA256
    cert=json.loads(a.certificate.read_text())
    assert cert["original_counts_sha256"]==PIN_SHA256
    assert cert["H0"]==list(H0) and cert["anchor"]==0 and cert["f"]==8
    rows={side:read_rows(cert,side) for side in ("left","right")}
    n=250 if a.all else a.spot
    assert 0 <= n <= 250
    if n:
        table=json.loads(a.input.read_text())["counts_and_cohorts"]
        counts={k:[int(v) for v in table[str(k)]["counts"]] for k in range(214,315)}
        solver=a.solver.resolve()
        assert solver.is_file()
        for side,tau in (("left",L),("right",U-1)):
            for expected in rows[side][:n]:
                observed=solve(counts,expected[0],tau,solver)
                assert observed==expected,(side,expected,observed)
    print("PASS_R5_F8_ANCHORED_SEVEN_ALL_250_BOTH_ENDPOINTS",
          "stored_rows",sum(len(r) for r in rows.values()),
          "independently_recomputed_each_side",n)

if __name__=="__main__":
    main()
