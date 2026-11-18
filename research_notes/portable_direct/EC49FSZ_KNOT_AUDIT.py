#!/usr/bin/env python3
"""EC49FSZ: exact rational policy-knot audit; optional original-native evidence replay.
The exact unrestricted Bellman computations and raw tree bytes are supplied in
the companion self-contained conversation evidence archive. Run from an extracted
archive root to enable --trees, --native, --independent.
"""
from fractions import Fraction as Q
from pathlib import Path
import hashlib, json, sys
R=Path(__file__).resolve().parent
C=json.loads((R/"EC49FSZ_CERT.json").read_text())
a,b=Q(C["a"]),Q(C["b"])
knots=list(map(Q,C["knots"]))
D=[tuple(r) for r in C["policy_vectors"]["D"]]
S=[tuple(r) for r in C["policy_vectors"]["S"]]
def affine(r,orient,z):
 u,n32,n34,n140=r
 return Q(u)-(a*n32+b*n34 if orient=="D" else b*n32+a*n34)-n140*z
def optimum(orient,z):
 return min(affine(r,orient,z) for r in (D if orient=="D" else S))
assert knots==[Q(1,2),Q(3,5),Q(199,320),Q(121,192),
               Q(2065,3232),Q(3061,4608),Q(1)]
for orient in "DS":
 anchors=C["native_Bellman_anchors"][orient]
 assert len(anchors)==7
 for z,anchor in zip(knots,anchors):
  assert Q(anchor["z"])==z and Q(anchor["value"])==optimum(orient,z)
assert affine(D[0],"D",knots[2])==affine(D[1],"D",knots[2])
assert affine(D[1],"D",knots[4])==affine(D[2],"D",knots[4])
for left,right,which in [(0,1,1),(1,2,2),(2,3,3),(3,4,5)]:
 assert affine(S[left],"S",knots[which])==affine(S[right],"S",knots[which])
gap=[optimum("D",z)-optimum("S",z) for z in knots]
assert min(gap)==Q(1255,128) and max(gap)==Q(213257,12928)
assert optimum("D",Q(1))-optimum("S",Q(1))==Q(5867,384)
print("PASS exact seven-knot policy geometry; full-real-interval claim uses native Bellman and tree evidence")

if any(k in sys.argv for k in ("--trees","--native","--independent")):
 from native_code.EC49FQI_NATIVE_DATA import V,PIN
 assert PIN==C["frozen_input_commit"] and len(V)==228
 for key,path in (("master","source/frozen_original_master.txt"),
                  ("profiles_csv","source/EC49FPG_PROFILE.csv")):
  assert hashlib.sha256((R/path).read_bytes()).hexdigest()==C["source_sha256"][key]
 def check_tree(node,states,used,counts):
  if "leaf" in node:
   assert len(states)==1 and node["leaf"]==states[0]
   return
  q=node["named_observer"]
  assert q not in used and 0<=q<228
  groups={}
  for i in states: groups.setdefault(str(V[q][i]),[]).append(i)
  assert len(groups)>=2 and set(groups)==set(node["children"])
  counts[q]=counts.get(q,0)+len(states)
  for outcome,subset in groups.items():
   check_tree(node["children"][outcome],subset,used|{q},counts)
 for path,h in C["tree_witness_sha256"].items():
  p=R/path
  assert hashlib.sha256(p.read_bytes()).hexdigest()==h
  saved=json.loads(p.read_text())
  counts={}
  check_tree(saved["tree"],list(range(141)),set(),counts)
  vector=(sum(counts.values()),counts.get(32,0),counts.get(34,0),counts.get(140,0))
  orient=saved["mode"]
  assert vector in (D if orient=="D" else S)
  assert affine(vector,orient,Q(saved["z_witness"]))==Q(saved["info"]["numerator"],saved["info"]["denominator"])
 print("PASS 8 full original physical named-decision-tree replays and source SHA256")

if "--native" in sys.argv:
 from native_code.EC49FSA_THREE_OBSERVER_SOLVER import solve
 for orient in "DS":
  for z,anchor in zip(knots,C["native_Bellman_anchors"][orient]):
   costs={32:a,34:b,140:z} if orient=="D" else {32:b,34:a,140:z}
   result,_=solve(costs,return_tree=False)
   assert Q(result["numerator"],result["denominator"])==Q(anchor["value"])
   print("EXACT_NATIVE",orient,z,anchor["value"],flush=True)
if "--independent" in sys.argv:
 from native_code.EC49FSA_FSB_INDEPENDENT_CHECK import certify
 for r in C["independent_raw94_checks"]:
  z=Q(r["z"]);o=r["orientation"]
  costs={32:a,34:b,140:z} if o=="D" else {32:b,34:a,140:z}
  result=certify(costs)
  assert Q(result["value"])==Q(r["value"])
  print("INDEPENDENT_RAW94",o,z,r["value"],flush=True)
print("EC49FSZ_KNOT_CERTIFICATE_PASS")
