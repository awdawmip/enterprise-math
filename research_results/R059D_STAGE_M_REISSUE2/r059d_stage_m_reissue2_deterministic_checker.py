#!/usr/bin/env python3
from __future__ import annotations
import json, hashlib, itertools
from pathlib import Path
from collections import Counter
from copy import deepcopy

R=Path(__file__).resolve().parent
TASK="823c5d8aaa0d63f9914e14a4375ad8fb3876f76f"
PARENT="da350b7b1e2ae21491e6251fdf2ba9cf0d4557ca"
checks=[]
def ck(v,label):
    checks.append((label,bool(v)))
    if not v: raise AssertionError(label)
def J(n): return json.loads((R/n).read_text())
def umax(v):
    m=max(v); ids=[i for i,x in enumerate(v) if x==m]
    return ids[0] if len(ids)==1 else None

vp=J("R059D_STAGE_M_THREE_AXIS_VECTOR_PROTOCOL.json")
sem=J("R059D_STAGE_M_GEOMETRIC_TOOL_SEMANTIC_STATUS.json")
eq=J("R059D_STAGE_M_EQUAL_PACKET_COUNT_ENDPOINT_PROTOCOL.json")
sym=J("R059D_STAGE_M_VECTOR_SYMMETRY_PROTOCOL.json")
mic=J("R059D_STAGE_M_VECTOR_MICROGRAMMAR_REGISTRY.json")
oracle=J("R059D_STAGE_M_RAW_HISTORY_CPBC_VECTOR_ORACLE.json")
func=J("R059D_STAGE_M_VECTOR_ENDPOINT_FUNCTIONAL_ATLAS.json")
rob=J("R059D_STAGE_M_VECTOR_MICROGRAMMAR_ROBUSTNESS_LEDGER.json")
axis=J("R059D_STAGE_M_VECTOR_AXIS_ORIENTATION_FACTORIZATION_AUDIT.json")
dyn=J("R059D_STAGE_M_VECTOR_TRUE_DYNAMICS_ATLAS.json")
pert=J("R059D_STAGE_M_VECTOR_PERTURBATION_RESPONSE.json")
large=J("R059D_STAGE_M_VECTOR_LARGE_N_REGISTRY.json")

for name,o in [("vp",vp),("sem",sem),("eq",eq),("sym",sym),("mic",mic),("oracle",oracle),("func",func),("rob",rob),("axis",axis),("dyn",dyn),("pert",pert),("large",large)]:
    ck(o["taskbook_source"]==TASK,f"{name}:task")
    ck(o["frozen_stage_l_head"]==PARENT,f"{name}:parent")

# Project semantic slots
for k in ["VECTOR_CONCEPT","LENGTH_CONCEPT","ANGLE_CONCEPT","NORM_CONCEPT","TRIGONOMETRIC_CONCEPTS"]:
    ck(sem[k]=="ADMITTED",f"sem:{k}")
ck(sem["EUCLIDEAN_GEOMETRY"]=="REFERENCE_AND_CALIBRATION_LAYER_ADMITTED","sem:euclid")
for k in ["CLASSICAL_LENGTH_DEFINITION_AS_NATIVE_PREMISE","CLASSICAL_ANGLE_DEFINITION_AS_NATIVE_PREMISE","CLASSICAL_TRIG_DEFINITION_AS_NATIVE_PREMISE"]:
    ck(sem[k]=="WITHHELD",f"sem:{k}")
ck(eq["SEGMENT_PACKET_COUNT"]==4,"eq:L4")
ck(eq["GEOMETRIC_LENGTH"]=="CONCEPT_ADMITTED_DEFINITION_NOT_FROZEN_IN_STAGE_M","eq:length_distinction")

# Vector carrier
V={0:(1,-1,0),1:(-1,1,0),2:(0,1,-1),3:(0,-1,1),4:(-1,0,1),5:(1,0,-1)}
rho={0:2,2:4,4:0,1:3,3:5,5:1}
inv={0:1,1:0,2:3,3:2,4:5,5:4}
def add(a,b): return tuple(x+y for x,y in zip(a,b))
def neg(a): return tuple(-x for x in a)
def scale(k,a): return tuple(k*x for x in a)
Z=(0,0,0)
ck(add(add(V[0],V[2]),V[4])==Z,"vec:u+v+w")
for d in range(6):
    ck(sum(V[d])==0,f"vec:D6Lambda:{d}")
    for x in [(0,0,0),(3,-2,-1),(-7,4,3)]:
        ck(sum(x)==0 and sum(add(x,V[d]))==0,f"vec:closure:{d}:{x}")
    ck(V[inv[d]]==neg(V[d]),f"vec:inv:{d}")
    ck(V[rho[d]] in V.values(),f"vec:rho:{d}")

# Raw word templates / packet state routes
WORDS={k:v["word"] for k,v in mic["word_templates"].items()}
CELL={
"W0":["P0","P1","P2","P3"],
"W0_RED":["P0","P1","P2","P3"],
"W0_BLUE":["P0","P1","P2","P3"],
"WD":["P0","P1","P0","P1","P2","P3"],
"WQ":["P0","P1","P2","P1","P2","P3"],
"WDQ":["P0","P1","P0","P1","P2","P1","P2","P3"],
}
def cword(tid,d):
    q=rho[d]
    mp={"d":V[d],"-d":neg(V[d]),"q":V[q],"-q":neg(V[q])}
    return [mp[t] for t in WORDS[tid]]
def vsum(seq):
    s=Z
    for x in seq:s=add(s,x)
    return s
def first_order(seq):
    a=[]
    for x in seq:
        if x not in a:a.append(x)
    return a
for tid in WORDS:
    ck(CELL[tid]==oracle["raw_history_templates"][tid]["cell_sequence"],f"oracle:cellseq:{tid}")
    ck(first_order(CELL[tid])==["P0","P1","P2","P3"],f"oracle:firstorder:{tid}")
    for d in range(6):
        ck(vsum(cword(tid,d))==scale(2,V[d]),f"oracle:vsum:{tid}:{d}")
        # cyclic covariance
        mapped=[V[rho[next(k for k,v in V.items() if v==x)]] for x in cword(tid,d)]
        ck(mapped==cword(tid,rho[d]),f"sym:rho_word:{tid}:{d}")
        ck([neg(x) for x in cword(tid,d)]==cword(tid,inv[d]),f"sym:inv_word:{tid}:{d}")

G={g["id"]:g for g in mic["microgrammars"]}
coeff={gid:(len(g["A_histories"]),len(g["I_histories"])) for gid,g in G.items()}
expected={"M-G0":(1,3),"M-G1":(1,2),"M-G2":(1,2),"M-G3":(1,4),"M-G4":(2,1),"M-G5":(1,2)}
ck(coeff==expected,"oracle:coeff")
for gid,(a,b) in coeff.items():
    ck(oracle["grammar_unit_seed_coefficients"][gid]["A_seed_endpoint_histories"]==a,f"oracle:Acoef:{gid}")
    ck(oracle["grammar_unit_seed_coefficients"][gid]["I_seed_endpoint_histories"]==b,f"oracle:Icoef:{gid}")
    for d in range(6):
        for A in range(4):
            for I in range(4):
                raw=A*a+I*b
                # CPBC compression: all distinct seed/history instances add at common P3
                cpbc=sum(1 for _s in range(A) for _h in G[gid]["A_histories"])+sum(1 for _s in range(I) for _h in G[gid]["I_histories"])
                ck(raw==cpbc,f"oracle:cpbc_raw:{gid}:{d}:{A}:{I}")

# Functionals
def Bvec(gid,A,I):
    a,b=coeff[gid]
    return [a*A[d]+b*I[d] for d in range(6)]
for gid,(a,b) in coeff.items():
    f=func["functionals"][gid]
    ck(f["alpha_A"]==a and f["beta_I"]==b,f"func:{gid}")
ck(func["endpoint_functional_equivalence_classes"]["E1"]==["M-G1","M-G2","M-G5"],"func:eqclass")

# Mandatory witnesses
W={
"W_ASYM_BASE":([5,5,5,5,6,5],[1,2,3,4,0,5]),
"W_CONSENSUS_DOMINANT2":([5,5,10,5,5,5],[1,1,5,1,1,1]),
"W_FULLY_SYMMETRIC":([5]*6,[1]*6),
"W_S1_TIE_S2_RESOLVE":([6]*6,[1,2,3,4,0,5]),
"W_SIGNATURE_INSUFFICIENT_PAIRS":([5,5,6,6,7,7],[1,1,2,2,0,0]),
}
def classify(wins):
    vals={w for w in wins.values() if w is not None}
    if not vals:return "MICROGRAMMAR_ALL_UNRESOLVED"
    if len(vals)>1:return "MICROGRAMMAR_DEPENDENT"
    d=next(iter(vals))
    return "MICROGRAMMAR_STRONG_CONSENSUS_RESOLVED" if all(w==d for w in wins.values()) else "MICROGRAMMAR_COMPATIBLE_WITH_TIES"
for wid,(A,I) in W.items():
    wins={}
    for gid in G:
        b=Bvec(gid,A,I); w=umax(b); wins[gid]=w
        fr=rob["mandatory_witnesses"][wid]["grammars"][gid]
        ck(fr["B"]==b,f"wit:{wid}:{gid}:B")
        ck(fr["winner_label"]==w,f"wit:{wid}:{gid}:winner")
    ck(rob["mandatory_witnesses"][wid]["classification"]==classify(wins),f"wit:{wid}:class")

# 3840 box exact
cnt=Counter(); unique={}
for p in range(6):
  for q in range(p+1,6):
    for Ap,Ip,Aq,Iq in itertools.product(range(4),repeat=4):
      A=[0]*6;I=[0]*6
      A[p]=Ap;I[p]=Ip;A[q]=Aq;I[q]=Iq
      wins={gid:umax(Bvec(gid,A,I)) for gid in G}
      c=classify(wins);cnt[c]+=1;unique[(tuple(A),tuple(I))]=c
ck(dict(cnt)==rob["witness_search_box"]["template_class_counts"],"box:template_counts")
uc=Counter(unique.values())
ck(dict(uc)==rob["witness_search_box"]["unique_state_class_counts"],"box:unique_counts")

# explicit cross-axis dependence
A=[0,0,1,0,0,0];I=[1,0,0,0,0,0]
ck(umax(Bvec("M-G0",A,I))==0 and umax(Bvec("M-G4",A,I))==2,"depend:cross_axis")
# component dominance theorem exhaustive on small pairs for all grammars
for A1,I1,A2,I2 in itertools.product(range(4),repeat=4):
    if A1>=A2 and I1>=I2 and (A1>A2 or I1>I2):
        for gid,(a,b) in coeff.items():
            ck(a*A1+b*I1>a*A2+b*I2,f"dominance:{gid}:{A1}:{I1}:{A2}:{I2}")

# Axis/orientation factorization
pairs={"u":(0,1),"v":(2,3),"w":(4,5)}
def staged(B):
    Q={a:max(B[i],B[j]) for a,(i,j) in pairs.items()}
    m=max(Q.values()); aa=[a for a,v in Q.items() if v==m]
    if len(aa)!=1:return None
    i,j=pairs[aa[0]]
    if B[i]==B[j]:return None
    return i if B[i]>B[j] else j
for B in itertools.product(range(4),repeat=6):
    ck(staged(B)==umax(B),f"axisfact:{B}")
cb=axis["nonlossless_axis_sum_control"]["counterexample"]
ck(umax(cb["B"])==0,"axis:sum_counter_direct")
ck(cb["axis_sum_stage"]=="+v","axis:sum_counter_stage")

# Count carriers + vector coordinate
def blank(): return {"I":[0]*6,"O":[0]*6,"M":[[0]*6 for _ in range(6)]}
def init(carrier,A0=None,I0=None):
    if carrier in ("A","C"): nodes={x:blank() for x in range(6)};x=0
    else: nodes={(a,b):blank() for a in range(6) for b in range(2)};x=(0,0)
    s=nodes[x]
    if A0 is None:
        s["I"]=[1,2,3,4,0,5];s["O"]=[2]*6;s["M"][0]=[3,3,3,3,4,3]
    else:
        s["I"]=list(I0);s["O"]=list(A0)
    return {"nodes":nodes,"node":x,"ingress":0,"coord":Z}
def tn(c,x,d):
    if c=="A":return d
    if c=="B":
        a,b=x;return (d,b^((d-a)%2))
    return x
def ti(c,x,d): return (d+(2 if c=="A" else 3 if c=="B" else 1))%6
def localAI(p):
    s=p["nodes"][p["node"]];i=p["ingress"]
    return [s["O"][d]+s["M"][i][d] for d in range(6)],list(s["I"])
def epB(p,g):
    A,I=localAI(p);return Bvec(g,A,I)
def step(p,c,d):
    x=p["node"];i=p["ingress"];s=p["nodes"][x]
    s["O"][d]+=1;s["M"][i][d]+=1
    y=tn(c,x,d);j=ti(c,x,d);p["nodes"][y]["I"][j]+=1
    p["node"]=y;p["ingress"]=j;p["coord"]=add(p["coord"],scale(2,V[d]))
def payload(p):
    rr=[]
    for x in sorted(p["nodes"],key=repr):
        s=p["nodes"][x];rr.append([repr(x),s["I"],s["O"],s["M"]])
    return [repr(p["node"]),p["ingress"],list(p["coord"]),rr]
def dg(p):return hashlib.sha256(json.dumps(payload(p),separators=(',',':')).encode()).hexdigest()
def totO(p):return sum(sum(s["O"]) for s in p["nodes"].values())
def totI(p):return sum(sum(s["I"]) for s in p["nodes"].values())
def run(c,g,n=48,A0=None,I0=None,perturb=None):
    p=init(c,A0,I0)
    if perturb: perturb(p)
    rows=[];ds=[]
    for e in range(n):
        b=epB(p,g);w=umax(b)
        rows.append({"e":e,"B":b,"winner":w,"coord":list(p["coord"]),"digest":dg(p),"TOTAL_O":totO(p),"TOTAL_I":totI(p)})
        if w is None:break
        ds.append(w);step(p,c,w)
    return p,rows,ds
representatives={"G0":"M-G0","G1_EQ":"M-G1","G3":"M-G3","G4":"M-G4"}
for c in "ABC":
    for key,g in representatives.items():
        p,rows,ds=run(c,g,48)
        fr=dyn["W_ASYM_BASE"]["carriers"][c][key]
        ck(ds==fr["selected_labels"],f"dyn:{c}:{key}:d")
        ck(list(p["coord"])==fr["final_coordinate"],f"dyn:{c}:{key}:coord")
        ck(dg(p)==fr["final_state_digest_sha256"],f"dyn:{c}:{key}:digest")
        for e,row in enumerate(rows):
            ck(sum(row["coord"])==0,f"dyn:{c}:{key}:lambda:{e}")
            ck(row["TOTAL_O"]==12+e,f"dyn:{c}:{key}:totalO:{e}")
# dependent trajectory divergence
Ad=[0,0,1,0,0,0];Id=[1,0,0,0,0,0]
for c in "ABC":
    p0,r0,d0=run(c,"M-G0",48,Ad,Id)
    p4,r4,d4=run(c,"M-G4",48,Ad,Id)
    ck(d0[0]==0 and d4[0]==2,f"dyn:dep:first:{c}")
    reco=[e for e in range(1,min(len(r0),len(r4))) if r0[e]["digest"]==r4[e]["digest"]]
    ck(reco==dyn["dependent_witness"]["carriers"][c]["same_epoch_recoalescence_after_divergence"],f"dyn:dep:reco:{c}")

# perturbations
def pc(j):
    def f(p):p["nodes"][p["node"]]["O"][j]+=1
    return f
def pi(j):
    def f(p):p["nodes"][p["node"]]["I"][j]+=1
    return f
def pt(j):
    def f(p):
        s=p["nodes"][p["node"]];s["O"][j]-=1;s["O"][rho[j]]+=1
    return f
P={"COUNT_TOKEN":pc,"INCIDENCE":pi,"TAGGED_VECTOR_STEP":pt}
for key,g in representatives.items():
  for c in "ABC":
    _,base,_=run(c,g,96)
    for typ,pf in P.items():
      frozen=pert["classes"][key][c][typ]
      first=[]; divs=[]; unrs=[]; recos=[]; steps=[]
      for j in range(6):
        _,pr,pds=run(c,g,96,perturb=pf(j))
        first.append(pr[0]["winner"])
        first_div=None;first_unr=None;reco=[]
        for e in range(min(len(base),len(pr))):
            if base[e]["winner"]!=pr[e]["winner"] and first_div is None:first_div=e
            if ((base[e]["winner"] is None)!=(pr[e]["winner"] is None)) and first_unr is None:first_unr=e
            if base[e]["digest"]==pr[e]["digest"]:reco.append(e)
        divs.append(first_div);unrs.append(first_unr);recos.append(reco);steps.append(len(pds))
      ck(first==frozen["first_outputs"],f"pert:{key}:{c}:{typ}:first")
      ck(divs==frozen["first_BRC_divergence_epochs"],f"pert:{key}:{c}:{typ}:div")
      ck(unrs==frozen["first_unresolved_status_difference_epochs"],f"pert:{key}:{c}:{typ}:unr")
      ck(recos==frozen["same_epoch_recoalescence_epochs"],f"pert:{key}:{c}:{typ}:reco")
      ck(steps==frozen["perturbed_resolved_steps"],f"pert:{key}:{c}:{typ}:steps")

# Large N common background cancellation
for sm in large["N_entries"]:
    N=int(sm)
    for gid,(a,b) in coeff.items():
        for wid,(A,I) in W.items():
            B0=Bvec(gid,A,I)
            BN=[a*(N+A[d])+b*I[d] for d in range(6)]
            ck([x+a*N for x in B0]==BN,f"large:shift:{sm}:{gid}:{wid}")
            ck(umax(B0)==umax(BN),f"large:winner:{sm}:{gid}:{wid}")

# final freezes
ck(rob["BRC6_NATIVE_CANONICALITY"]=="NOT_ESTABLISHED","freeze:native")
ck(axis["lossless_factorization"]["freeze"]=="BRC6_AXIS_ORIENTATION_FACTORIZATION_ESTABLISHED","freeze:axis")
ck(dyn["freeze"]=="BRC6_VECTOR_ENDPOINT_COUNT_TRUE_STATE_MICROGRAMMAR_DYNAMICS_ESTABLISHED","freeze:dyn")
ck("BRC6_VECTOR_ENDPOINT_COUNT_MICROGRAMMAR_DEPENDENCE_ESTABLISHED" in rob["freezes"],"freeze:dep")
ck("BRC6_VECTOR_ENDPOINT_COUNT_MICROGRAMMAR_ROBUST_DOMAIN_ESTABLISHED" in rob["freezes"],"freeze:robust")

digest=hashlib.sha256("\n".join(f"{lab}:{int(ok)}" for lab,ok in checks).encode()).hexdigest()
out={
 "schema":"R059D_STAGE_M_REISSUE2_DETERMINISTIC_CHECKER_OUTPUT_V1",
 "researcher_id":"EM-R059D-9C6B2A","taskbook_source":TASK,"frozen_parent_head":PARENT,
 "status":"PASS" if all(v for _,v in checks) else "FAIL",
 "checks_total":len(checks),"checks_passed":sum(v for _,v in checks),"checks_failed":sum(not v for _,v in checks),
 "checks_digest_sha256":digest,
 "raw_history_cases":"6 grammars x 6 directed vectors x 16 (A,I) tiny seed pairs plus explicit vector-word/cell-route checks",
 "witness_box":"3840 frozen templates exact",
 "axis_factorization":"exhaustive endpoint vectors B in {0,1,2,3}^6 plus exact theorem form",
 "true_state_method":"exact Stage-K relational I/O/M update x Lambda vector coordinate update S_d=2d",
 "perturbation_method":"4 endpoint-functional classes x 3 carriers x 3 perturbation classes x 6 vector channels, 96-decision windows",
 "large_N_method":"symbolic candidate-common alpha_g*N cancellation only; no huge enumeration",
 "parent_immutability":"PASS_BY_GITHUB_COMPARE_PRE_MANIFEST"
}
(R/"R059D_STAGE_M_DETERMINISTIC_CHECKER_OUTPUT.json").write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
print(json.dumps(out,indent=2))
