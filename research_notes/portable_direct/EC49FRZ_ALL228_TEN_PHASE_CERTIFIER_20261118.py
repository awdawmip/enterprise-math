#!/usr/bin/env python3
"""EC49FRZ: reproducible all-228 native BRC ten-phase exact certificate.
Run from the 23-file evidence archive root with Python 3.10+, standard library.
"""
import sys, json, hashlib
from pathlib import Path
from fractions import Fraction as F
from collections import Counter

ROOT=Path(__file__).resolve().parent.parent
sys.path.insert(0,str(ROOT/"code"))
from EC49FRW_TWO_PRICE_SOLVER import solve, V, PIN

assert PIN=="fc0f038e7bfd12c886b4d37f900bfb770c0f61ab"
assert len(V)==228 and all(len(q)==141 for q in V)
for name, sha in [
  ("frozen_original_master.txt","cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e"),
  ("EC49FPG_PROFILE.csv","a61a3ee4d2f13f9d216f52cd3529c72d395c1250bfb1d7ae96a1adf5a6837c1f")
]:
    assert hashlib.sha256((ROOT/"source"/name).read_bytes()).hexdigest()==sha

cert=json.loads((ROOT/"evidence"/"EC49FRZ_10_PIECE_DIAGONAL_MACHINE_CERT.json").read_text())
assert cert["frozen_pin"]==PIN
assert len(cert["cost_lines_and_intervals"])==10 and len(cert["vertices"])==11
lines=[]
for i, entry in enumerate(cert["cost_lines_and_intervals"]):
    tree=json.loads((ROOT/"evidence"/entry["full_tree"]).read_text())["tree"]
    count=Counter();depthmax=0
    for state in range(141):
        node=tree; seen=set(); depth=0
        while "named_observer" in node:
            q=node["named_observer"]
            assert 0<=q<228 and q not in seen
            seen.add(q); count[q]+=1; depth+=1
            node=node["children"][str(V[q][state])]
        assert node["leaf"]==state,(i,state)
        depthmax=max(depthmax,depth)
    U=sum(count.values()); K=count[32]+count[34]
    assert (U,K)==(entry["U"],entry["K"])
    a,b=map(F,entry["segment"])
    assert a==F(cert["vertices"][i]) and b==F(cert["vertices"][i+1])
    assert F(entry["at_left"])==U-K*a and F(entry["at_right"])==U-K*b
    assert depthmax<=4
    lines.append((U,K))
    print("TREE_OK",i,U,K,depthmax,flush=True)

vertices=list(map(F,cert["vertices"]))
assert vertices==sorted(vertices) and vertices[0]==0 and vertices[-1]==1
for i,s in enumerate(vertices):
    optimum=min(F(U)-s*K for U,K in lines)
    if i>0:
        assert F(lines[i-1][0])-s*lines[i-1][1]==optimum
    if i<10:
        assert F(lines[i][0])-s*lines[i][1]==optimum
    if "--quick" not in sys.argv:
        info,_=solve(s,s,False) # 228 original physical named queries, exact rationals
        actual=F(info["Bellman_integer_value"],info["denominator"])
        assert actual==optimum,(s,actual,optimum)
        print("FULL_BELLMAN_OK",str(s),str(actual),info["states"],flush=True)
    else:
        print("WITNESS_VERTEX_OK_ONLY",str(s),str(optimum),flush=True)
print("PASS: ten native full trees, 141 state paths each, 11 exact phase vertices; full Bellman" if "--quick" not in sys.argv else "PASS tree-only verification; full Bellman not rerun")
