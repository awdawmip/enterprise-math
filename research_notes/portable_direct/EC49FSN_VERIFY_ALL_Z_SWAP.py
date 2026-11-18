#!/usr/bin/env python3
"""EC49FSN: exact original-native full-tree witness and price-cell verifier.
Place code/ original frozen-source decoder modules, source/ raw family files, this
certificate, and the compact tree bundle together as in the evidence archive.
This checks the returned certificate, not reruns every global Bellman recursion.
"""
import json, hashlib, zlib, base64, sys
from collections import Counter
from fractions import Fraction as F
from pathlib import Path

root=Path(__file__).resolve().parent
sys.path.insert(0,str(root/"code"))
from EC49FSA_THREE_OBSERVER_SOLVER import V
assert len(V)==228 and len(V[0])==141
cert=json.loads((root/"EC49FSN_GLOBAL_SWAP_MACHINE_CERT.json").read_text())
trees=json.loads(zlib.decompress(base64.b64decode(
  (root/"EC49FSN_ALL_15_NATIVE_TREES_JSON_ZLIB_BASE64.txt").read_text()
)))
def opt(case,z):
  d=cert["cases"][case]
  a,b=F(d["a"]),F(d["b"])
  return min(F(p["counts"][0])-a*p["counts"][1]-b*p["counts"][2]-z*p["counts"][3]
             for p in d["phases"])
for case in ("A","B"):
  d=cert["cases"][case]
  for idx,p in enumerate(d["phases"]):
    tr=trees[case][str(idx)]
    canonical=json.dumps(tr,sort_keys=True,separators=(",",":")).encode()
    assert hashlib.sha256(canonical).hexdigest()==p["tree_sha256"]
    c=Counter()
    dep=0
    for i in range(141):
      node=tr;seen=set();n=0
      while "named_observer" in node:
        q=node["named_observer"]
        assert 0<=q<228 and q not in seen
        seen.add(q);c[q]+=1;n+=1
        node=node["children"][str(V[q][i])]
      assert node=={"leaf":i},(case,idx,i)
      dep=max(dep,n)
    assert [sum(c.values()),c[32],c[34],c[140]]==p["counts"]
    assert dep==p["max_depth"]
    lo,hi=map(F,p["z"])
    for z in (lo,(lo+hi)/2,hi):
      price=F(p["counts"][0])-F(d["a"])*p["counts"][1]-F(d["b"])*p["counts"][2]-z*p["counts"][3]
      assert price==opt(case,z)
  for v in d["bellman_vertices"]:
    assert opt(case,F(v["z"]))==F(v["F"])
for r in cert["difference_intervals"]:
  left,right=map(F,r["z"])
  assert opt("A",left)-opt("B",left)==F(r["D_left"])
  assert opt("A",right)-opt("B",right)==F(r["D_right"])
  assert left==0 or F(r["D_left"])>0
  assert F(r["D_right"])>0
assert opt("A",F(0))==opt("B",F(0))==F(3481,16)
print("PASS: 15/15 original native full trees, 17/17 cited Bellman endpoint values, 13/13 positive swap segments.")
print("Scope: native tree replay and certificate arithmetic; unrestricted global endpoints are verified by the separate exact Bellman solver.")
