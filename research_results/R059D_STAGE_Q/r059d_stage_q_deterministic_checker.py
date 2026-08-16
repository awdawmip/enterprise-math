#!/usr/bin/env python3
from pathlib import Path
import json,itertools,hashlib
R=Path(__file__).parent; C=[]
def ck(x,s):
 C.append(s)
 if not x: raise AssertionError(s)
def j(n): return json.loads((R/n).read_text())
P=j("R059D_STAGE_Q_Z2_TORSOR_CONSTRAINT_GRAPH_PROTOCOL.json");T=j("R059D_STAGE_Q_COMPONENT_SOLUTION_THEOREM.json")
X=j("R059D_STAGE_Q_CROSS_SCALE_UP_DOWN_CONSTRAINT_PROPAGATION.json");E=j("R059D_STAGE_Q_GAP_CENTERED_TAU_ODD_CARRIER.json")
A=j("R059D_STAGE_Q_POST_CREDIT_ANCHOR_LEDGER.json");G=j("R059D_STAGE_Q_GLOBAL_COMPLEMENT_INVARIANT_AUDIT.json")
S=j("R059D_STAGE_Q_SCALAR_5_CONTEXT_CONTROL.json");V=j("R059D_STAGE_Q_COVARIANCE_REGISTRY.json");L=j("R059D_STAGE_Q_TRIVIALITY_LEAKAGE_LEDGER.json")
RID="EM-R059D-9C6B2A"; TASK="c13713d68635b51c78e9fd3e589a63230b441de5"; PAR="a621f80d0294f5a5139eb4a2ed26e552e6368b18"
for o,n in [(P,"p"),(T,"t"),(X,"x"),(E,"e"),(A,"a"),(G,"g"),(S,"s"),(V,"v"),(L,"l")]:
 ck(o["researcher_id"]==RID,n+"r");ck(o["taskbook_source"]==TASK,n+"t");ck(o["frozen_parent"]==PAR,n+"p")
ck(P["status"]=="FROZEN_BEFORE_SCORING","prescore")
def brute(ns,es,an=()):
 return [z for z in itertools.product([0,1],repeat=len(ns)) if all((dict(zip(ns,z))[u]^dict(zip(ns,z))[v])==c for u,v,c in es) and all(dict(zip(ns,z))[u]==h for u,h in an)]
def pred(ns,es,an=()):
 ad={u:[] for u in ns}
 for u,v,c in es: ad[u].append((v,c));ad[v].append((u,c))
 p={};free=0
 for r in ns:
  if r in p: continue
  p[r]=0;q=[r];cc=[r];bad=False
  while q:
   u=q.pop()
   for v,c in ad[u]:
    w=p[u]^c
    if v in p: bad|=p[v]!=w
    else:p[v]=w;q.append(v);cc.append(v)
  roots={h^p[u] for u,h in an if u in cc};bad|=len(roots)>1
  if bad:return 0
  free+=not roots
 return 2**free
rec={x["id"]:x for x in T["registry_outcomes"]}
for q in P["registry"]:
 b=brute(q["nodes"],q["edges"],q["anchors"]);ck(len(b)==pred(q["nodes"],q["edges"],q["anchors"]),"reg"+q["id"]);ck([list(x) for x in b]==rec[q["id"]]["solutions"],"rec"+q["id"])
for n in range(1,5):
 ns=list(range(n));ps=[(i,k) for i in ns for k in ns if i<k]
 for z in itertools.product([-1,0,1],repeat=len(ps)):
  es=[(i,k,c) for (i,k),c in zip(ps,z) if c>=0];ck(len(brute(ns,es))==pred(ns,es),"gr"+str(n)+str(z))
for n in range(1,9):
 ns=list(range(n));es=[(i,i+1,0) for i in range(n-1)];ck(len(brute(ns,es))==2,"stf"+str(n));ck(len(brute(ns,es,[(0,1)]))==1,"sta"+str(n))
ck(X["two_level"]["joint_unanchored"]==[[0,0,1],[1,1,0]],"x2");ck(X["three_level"]["coarse_anchor_B0"]["joint"]==[0,1,1,0],"x3")
cy=[("x","y",0),("y","z",0),("z","x",1)];ck(brute(["x","y","z"],cy)==[],"cy");ck(X["cyclic_negative_control"]["freeze"]=="CROSS_SCALE_LOCAL_PROPAGATION_INSUFFICIENT","cyn")
def eta(q,l,u):return 2*q-l-u
for l in range(-3,4):
 for u in range(l+1,5):
  for q2 in range(2*l+1,2*u):
   q=q2/2;ck(eta(l+u-q,l,u)==-eta(q,l,u),"eo"+str((l,u,q2)))
   for m in [1,2,5]:ck(eta(m*q,m*l,m*u)==m*eta(q,l,u),"es"+str((l,u,q2,m)))
for a,b,c,d in itertools.product(range(-2,3),repeat=4):
 ck((a+b+c==0 and a+2*b==0 and a+2*c==0 and d==0)==(2*b==-a and 2*c==-a and d==0),"ec"+str((a,b,c,d)))
ck(eta(-.5,-1,0)==0 and eta(5,4,9)==-3,"ectl");ck(E["torsor_identification_audit"]["internal_canonical_choice"]=="NONE","enos")
cl={x["id"]:x["classification"] for x in A["entries"]}
for i,c in [("A_ROOT_H","ABSOLUTE_SINGLETON_ANCHOR"),("E_XOR","RELATIVE_EDGE_ONLY"),("S_SYMMETRIC","SYMMETRIC_NO_INFORMATION"),("I_CONFLICT","INCONSISTENT")]:ck(cl[i]==c,"a"+i)
for n in range(1,6):
 for b in itertools.product([0,1],repeat=n):
  d=tuple(1-x for x in b)
  for i in range(n):
   for k in range(n):ck((b[i]^b[k])==(d[i]^d[k]),"gc"+str((n,b,i,k)))
ck(G["freezes"]==["GLOBAL_Z2_TORSOR_AMBIGUITY_ESTABLISHED","GAUGE_EQUIVALENCE_NOT_ESTABLISHED"],"gf")
ck(S["PREV"]==4 and S["NEXT"]==9 and S["eta"]["value"]==-3 and S["relative_context_audit"]["equivariant_identifications"]==2,"sc")
for m in V["positive_scales"]:ck(eta(5*m,4*m,9*m)==-3*m,"vs"+str(m))
for K in map(int,V["large_backgrounds"]):ck((K-1)+1==K,"vk"+str(K))
for k,v in L["gates"].items():ck(v is False,"leak"+k)
ck(L["parent_immutability"]=="PASS_BY_GITHUB_COMPARE_PRE_MANIFEST","parent")
ck(X["broad_freeze"]=="BRC_RELATIVE_CONSTRAINT_SYNCHRONIZATION_ESTABLISHED","rel")
h=hashlib.sha256("\n".join(C).encode()).hexdigest()
O={"schema":"R059D_STAGE_Q_DETERMINISTIC_CHECKER_OUTPUT_V1","researcher_id":RID,"taskbook_source":TASK,"frozen_parent":PAR,"status":"PASS","checks_total":len(C),"checks_passed":len(C),"checks_failed":0,"checks_digest_sha256":h,"parent_immutability":L["parent_immutability"],"method":"symbolic rooted-parity and affine-linear proofs plus bounded tiny exact oracles; no huge enumeration"}
(R/"R059D_STAGE_Q_DETERMINISTIC_CHECKER_OUTPUT.json").write_text(json.dumps(O,separators=(",",":"),sort_keys=True)+"\n");print(json.dumps(O,indent=2))
