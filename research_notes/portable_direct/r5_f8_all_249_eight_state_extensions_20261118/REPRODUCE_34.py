#!/usr/bin/env python3
"""Exact R5 f=8 completion replay. Python integers, C++ exact Bellman.

Usage: python3 REPRODUCE_34.py TABLE.json CLASSES.json NEW_34_ENDPOINTS.tsv PRIOR_19.json
Inputs are from the pinned existing R5 ZIP / original frozen science.
"""
import csv
import hashlib
import json
import subprocess
import sys
import tempfile
from pathlib import Path

HERE=Path(__file__).resolve().parent
TABLE_SHA="50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b"
CLASSES_SHA="ebbf8a88a49e0fa3babb0856b23c064be0699a799732235edd88d99c10d367a3"
PRIOR_SHA="1ca2636f6ce716225cb14dfe6096c08ed5e58b4dbcd714c55ea2b71329a2f2d5"
L=25845652773852463277015040000
U=58182461585441404127941754880
BASE=(18,24,82,34,17)
CONTEXT=BASE+(144,208)

def source(path, sha):
    raw=Path(path).read_bytes()
    assert hashlib.sha256(raw).hexdigest()==sha,(path,"wrong pinned input")
    return json.loads(raw)

def maximal(masks):
    s=set(masks)
    return tuple(sorted(m for m in s if not any(m!=v and m&v==m for v in s)))

def windows(centers,diameter):
    return maximal(sum(1<<i for i,z in enumerate(centers) if v<=z<=v+diameter) for v in centers)

def make_input(table,rep,tau):
    seen={}
    for k in range(214,315):
        c=table[k]
        family=windows([c[i] for i in BASE+(rep,144,208)],tau)
        if family not in seen:seen[family]=k
    costs=sorted((k,family) for family,k in seen.items())
    s=["8 8",str(len(costs))]
    s.extend(" ".join(map(str,(k,len(family),*family))) for k,family in costs)
    return "\n".join(s)+"\n"

def main():
    if len(sys.argv)!=5:
        raise SystemExit(__doc__)
    table0=source(sys.argv[1],TABLE_SHA)["counts_and_cohorts"]
    table={k:tuple(map(int,table0[str(k)]["counts"])) for k in range(214,315)}
    assert len(table)==101 and all(len(v)==256 for v in table.values())
    classes=source(sys.argv[2],CLASSES_SHA)["classes"]
    prior=source(sys.argv[4],PRIOR_SHA)["results"]
    assert len(classes)==53 and len(prior)==19
    assert sorted(x for g in classes for x in g)==sorted(set(range(256))-set(CONTEXT))
    assert all(p["endpoints"]["L"]["cost"]==p["endpoints"]["Uminus1"]["cost"]==8335 for p in prior)
    with open(sys.argv[3],newline="") as f:
        rows=list(csv.DictReader(f,delimiter="\t"))
    assert len(rows)==34
    old={p["representative"] for p in prior}
    new={int(row["x"]) for row in rows}
    assert len(new)==34 and old.isdisjoint(new)
    groups={g[0]:g for g in classes}
    assert old|new==set(groups)
    assert sum(len(groups[x]) for x in new)==185
    with tempfile.TemporaryDirectory() as td:
        solver=Path(td)/"r5_exact8"
        subprocess.run(["g++","-std=c++17","-O3",str(HERE/"EXACT_EIGHT_SUBSET.cpp"),"-o",str(solver)],check=True)
        for row in rows:
            rep=int(row["x"])
            assert int(row["members"])==len(groups[rep])
            for edge,tau in (("L",L),("Uminus1",U-1)):
                run=subprocess.run([str(solver)],input=make_input(table,rep,tau),
                                   text=True,capture_output=True,check=True,timeout=120)
                got=dict(z.split("=") for z in run.stdout.split()[1:])
                for key,col in (("cost",edge+"cost"),("states",edge+"states"),("actions",edge+"actions")):
                    assert int(got[key])==int(row[col]),(rep,edge,key,got[key],row[col])
            print("PASS_CLASS",rep,flush=True)
    print("PASS_R5_ALL_53_CLASSES_249_CANDIDATES_106_ENDPOINTS",flush=True)

if __name__=="__main__":
    main()
