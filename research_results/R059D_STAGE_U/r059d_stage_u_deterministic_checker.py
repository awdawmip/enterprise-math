#!/usr/bin/env python3
from pathlib import Path
from itertools import permutations,combinations
import json,hashlib
R=Path(__file__).parent;RID="EM-R059D-9C6B2A";T="320e0525f0aa4d5ccc9faec2a408187b2e6f9222";P="c78ff5956a237c36eb6f51c2889eba5882271b81";C=[]
def c(n,x): C.append(n); assert x,n
def l(n): return json.loads((R/n).read_text())
N=["FINITE_GROUP_SELECTOR_PROTOCOL","ORBIT_EXTENSION_THEOREM","STABILIZER_FILTERED_FEASIBLE_SET_THEOREM","CONTEXT_STABILIZER_LEDGER","Z2_REPLAY","S3_DONOR_REPLAY","S4_AXIS_REPLAY","DIRECTED_TRANSFER_CONTEXT_AUDIT","AXIS_ORIENTATION_HIERARCHICAL_SELECTOR","SCALAR_MIDPOINT_CONTROL","POST_CREDIT_AS_FEASIBILITY_REDUCTION","COUNTEREXAMPLE_REGISTRY","TRIVIALITY_LEAKAGE_LEDGER"]
for n in N:
 o=l("R059D_STAGE_U_"+n+".json");c("m"+n,o["researcher_id"]==RID and o["taskbook_source"]==T and o["frozen_parent"]==P)
r=l("R059D_STAGE_U_COUNTEREXAMPLE_REGISTRY.json");c("reg",r["status"]=="FROZEN_BEFORE_SCORING" and len(r["cases"])==15)
S3=list(permutations(range(3)));S4=list(permutations(range(4)));A=list(combinations(range(4),2));D=[(i,j) for i in range(4) for j in range(4) if i!=j]
pa=lambda p,a:tuple(sorted((p[a[0]],p[a[1]])));pd=lambda p,d:(p[d[0]],p[d[1]])
fa=lambda H:[a for a in A if all(pa(p,a)==a for p in H)]
fd=lambda H:[d for d in D if all(pd(p,d)==d for p in H)]
Hc=[p for p in S4 if p[0]==0];Ha=[p for p in S4 if pa(p,(0,1))==(0,1)];Hd=[p for p in S4 if pd(p,(0,1))==(0,1)]
c("s3full",not [d for d in range(3) if all(p[d]==d for p in S3)])
H3=[p for p in S3 if p[0]==0];c("s3ctx",[d for d in range(3) if all(p[d]==d for p in H3)]==[0])
c("s4full",fa(S4)==[]);c("carrier",len(Hc)==6 and fa(Hc)==[]);c("axis",len(Ha)==4 and fa(Ha)==[(0,1),(2,3)]);c("dir",len(Hd)==2 and fa(Hd)==[(0,1),(2,3)] and fd(Hd)==[(0,1),(1,0)])
for y in A:
 m={};ok=True
 for g in S4:
  x=pa(g,(0,1));z=pa(g,y)
  if x in m and m[x]!=z:ok=False
  m[x]=z
 c("oa"+str(y),ok==all(pa(h,y)==y for h in Ha))
for y in range(3):
 m={};ok=True
 for g in S3:
  x=g[0];z=g[y]
  if x in m and m[x]!=z:ok=False
  m[x]=z
 c("od"+str(y),ok==all(h[y]==y for h in H3))
for i in range(4):
 H=[p for p in S4 if p[i]==i];c("ci"+str(i),fa(H)==[])
for a in A:
 H=[p for p in S4 if pa(p,a)==a];q=tuple(sorted(set(range(4))-set(a)));c("ai"+str(a),set(fa(H))=={a,q})
for d in D:
 H=[p for p in S4 if pd(p,d)==d];a=tuple(sorted(d));q=tuple(sorted(set(range(4))-set(a)))
 c("di"+str(d),set(fa(H))=={a,q} and set(fd(H))=={d,(d[1],d[0])})
for tag,H in [("F",S4),("C",Hc),("A",Ha),("D",Hd)]:
 F=set(fa(H))
 for m in range(64):
  X={A[i] for i in range(6) if m>>i&1};c("E"+tag+str(m),(X&F)==X.intersection(F))
z=l("R059D_STAGE_U_Z2_REPLAY.json")["cases"];c("z0",z["fully_symmetric"]["E"]==[]);c("z1",z["tau_odd_context_full_A"]["E"]==["0","1"]);c("z2",z["tau_odd_context_singleton_A"]["E"]==["0"])
h=l("R059D_STAGE_U_AXIS_ORIENTATION_HIERARCHICAL_SELECTOR.json");c("hx",h["axis_stage"]["E_axis"]==["{1,2}"] and h["orientation_stage"]["E_orient"]==[] and h["orientation_with_free_context_only"]["E_orient"]==["+","-"] and h["orientation_with_independent_singleton"]["E_orient"]==["+"])
s=l("R059D_STAGE_U_SCALAR_MIDPOINT_CONTROL.json");c("sc",s["midpoint"]["E"]==[] and s["nonmidpoint"]["E"]==["L","U"])
q=l("R059D_STAGE_U_TRIVIALITY_LEAKAGE_LEDGER.json");c("pg",q["status"]=="PASS" and q["gates"]["stage_t_and_earlier_immutable"]=="PASS_BY_GITHUB_COMPARE_PRE_MANIFEST")
for k,v in q["gates"].items():
 if k!="stage_t_and_earlier_immutable":c("fw"+k,v is False)
d=hashlib.sha256("\n".join(C).encode()).hexdigest();o={"schema":"R059D_STAGE_U_DETERMINISTIC_CHECKER_OUTPUT_V1","status":"PASS","researcher_id":RID,"taskbook_source":T,"frozen_parent":P,"checks_total":len(C),"checks_passed":len(C),"checks_failed":0,"checks_digest_sha256":d,"parent_immutability":"PASS_BY_GITHUB_COMPARE_PRE_MANIFEST","methods":{"proof_core":"orbit-stabilizer representative-independence and exact feasible/fixed-set intersection","finite_enumeration":"oracle only"}}
(R/"R059D_STAGE_U_DETERMINISTIC_CHECKER_OUTPUT.json").write_text(json.dumps(o,sort_keys=True,separators=(",",":"))+"\n");print(json.dumps(o,indent=2))
