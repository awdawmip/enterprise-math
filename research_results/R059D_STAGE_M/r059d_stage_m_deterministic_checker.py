#!/usr/bin/env python3
from __future__ import annotations
import json, hashlib, itertools, collections
from pathlib import Path
from copy import deepcopy
R=Path(__file__).resolve().parent
TASK="525f268408a66ee3f7bcae4e061f3f34dfa25366"
PARENT="da350b7b1e2ae21491e6251fdf2ba9cf0d4557ca"
checks=[]
def ck(v,label):
    checks.append((label,bool(v)))
    if not v: raise AssertionError(label)
def J(n): return json.loads((R/n).read_text())
def umax(v):
    m=max(v); ids=[i for i,x in enumerate(v) if x==m]
    return ids[0] if len(ids)==1 else None

prot=J("R059D_STAGE_M_MICROGRAMMAR_PROTOCOL.json")
wreg=J("R059D_STAGE_M_WITNESS_REGISTRY.json")
large=J("R059D_STAGE_M_LARGE_N_REGISTRY.json")
oracle=J("R059D_STAGE_M_RAW_HISTORY_ORACLE.json")
trans=J("R059D_STAGE_M_ENDPOINT_TRANSFER_FUNCTIONAL_ATLAS.json")
rob=J("R059D_STAGE_M_MICROGRAMMAR_ROBUSTNESS_LEDGER.json")
theo=J("R059D_STAGE_M_STRUCTURAL_THEOREMS.json")
cov=J("R059D_STAGE_M_SIX_OUTCOME_COVERAGE.json")
dyn=J("R059D_STAGE_M_TRUE_DYNAMICS_ATLAS.json")
pert=J("R059D_STAGE_M_PERTURBATION_RESPONSE.json")
kill=J("R059D_STAGE_M_TRIVIALITY_AND_LEAKAGE_LEDGER.json")

for name,o in [("prot",prot),("wreg",wreg),("large",large),("oracle",oracle),("trans",trans),("rob",rob),("theo",theo),("cov",cov),("dyn",dyn),("pert",pert),("kill",kill)]:
    ck(o["taskbook_source"]==TASK,f"{name}:task")
    ck(o["frozen_stage_l_head"]==PARENT,f"{name}:parent")
ck(prot["L"]==4 and prot["cells"]==[0,1,2,3] and prot["endpoint_cell_index"]==3,"protocol:L")
ck(prot["same_microgrammar_all_six_candidates"] is True,"protocol:sameg")
ck(prot["weights_forbidden"] is True,"protocol:weights")
ck(wreg["search_box"]["state_count"]==3840,"wbox:count")
ck(large["L"]==4 and large["no_huge_enumeration"] is True,"large:discipline")

# Raw histories and CPBC
def enum_paths(g,kind):
    start=g["seed_states"][kind]; end=g["endpoint_state"]
    E=collections.defaultdict(list)
    for a,b in g["edges"]: E[a].append(b)
    P=[[start]]
    for _ in range(3):
        P=[p+[b] for p in P for b in E[p[-1]]]
    return [p for p in P if p[-1]==end]
def cpbc(g,A,I):
    c=collections.Counter({g["seed_states"]["launch"]:A,g["seed_states"]["incidence"]:I})
    E=collections.defaultdict(list)
    for a,b in g["edges"]: E[a].append(b)
    for _ in range(3):
        n=collections.Counter()
        for a,m in c.items():
            for b in E[a]: n[b]+=m
        c=n
    return c[g["endpoint_state"]]
coeff={}
for g in prot["grammars"]:
    lp=enum_paths(g,"launch"); ip=enum_paths(g,"incidence")
    a,b=len(lp),len(ip); coeff[g["id"]]=(a,b)
    oo=oracle["grammars"][g["id"]]
    ck(oo["unit_launch_histories"]==lp,f"raw:{g['id']}:launch")
    ck(oo["unit_incidence_histories"]==ip,f"raw:{g['id']}:inc")
    ck((a,b)==(oo["launch_endpoint_multiplicity"],oo["incidence_endpoint_multiplicity"]),f"raw:{g['id']}:coef")
    for A in range(4):
        for I in range(4):
            ck(cpbc(g,A,I)==a*A+b*I,f"cpbc:{g['id']}:{A}:{I}")
    tr=trans["functionals"][g["id"]]
    ck((a,b)==(tr["alpha_launch"],tr["beta_incidence"]),f"transfer:{g['id']}")
ck(coeff["M-G0-AFFINE_UV_REPLAY"]==(1,3),"coef:g0")
ck(coeff["M-G1-SINGLE_SPLIT_RECOALESCE"]==(1,2),"coef:g1")
ck(coeff["M-G2-DELAYED_SPLIT_RECOALESCE"]==(1,2),"coef:g2")
ck(coeff["M-G3-TWO_STAGE_SPLIT_RECOALESCE"]==(1,4),"coef:g3")
ck(coeff["M-G4-LAUNCH_CLASS_SPLIT_CONTROL"]==(2,1),"coef:g4")
ck(coeff["M-G5-ENDPOINT_EQUIVALENT_INTERNAL_REWRITE"]==(1,2),"coef:g5")

def classify(A,I):
    outs={}; Bs={}
    for gid,(a,b) in coeff.items():
        B=[a*A[d]+b*I[d] for d in range(6)]
        Bs[gid]=B; outs[gid]=umax(B)
    rr=[x for x in outs.values() if x is not None]; u=set(rr)
    if not rr: c="MICROGRAMMAR_ALL_UNRESOLVED"
    elif len(u)>1: c="MICROGRAMMAR_DEPENDENT"
    elif len(rr)==len(outs): c="MICROGRAMMAR_STRONG_CONSENSSUS_RESOLVED" if False else "MICROGRAMMAR_STRONG_CONSENSUS_RESOLVED"
    else: c="MICROGRAMMAR_COMPATIBLE_WITH_TIES"
    return c,outs,Bs

W={
"W_ASYM_BASE":([5,5,5,5,6,5],[1,2,3,4,0,5]),
"W_CONSENSUS_DOMINANT2":([5,5,10,5,5,5],[1,1,5,1,1,1]),
"W_FULLY_SYMMETRIC":([5]*6,[1]*6),
"W_S1_TIE_S2_RESOLVE":([6]*6,[1,2,3,4,0,5]),
"W_SIGNATURE_INSUFFICIENT_PAIRS":([5,5,6,6,7,7],[1,1,2,2,0,0])
}
for wid,(A,I) in W.items():
    c,o,B=classify(A,I); fr=rob["mandatory_witnesses"][wid]
    ck(fr["classification"]==c,f"w:{wid}:class")
    ck(fr["winner_by_grammar"]==o,f"w:{wid}:out")
    ck(fr["B_by_grammar"]==B,f"w:{wid}:B")

# frozen witness search box
tc=collections.Counter(); us={}
pairs=list(itertools.product(range(4),repeat=2))
for p in range(6):
  for q in range(p+1,6):
    for ap,ip in pairs:
      for aq,iq in pairs:
        A=[0]*6;I=[0]*6;A[p]=ap;I[p]=ip;A[q]=aq;I[q]=iq
        c,o,B=classify(A,I);tc[c]+=1;us.setdefault((tuple(A),tuple(I)),c)
ck(dict(tc)==rob["search_box_results"]["template_class_counts"],"box:template_counts")
ck(collections.Counter(us.values())==collections.Counter(rob["search_box_results"]["unique_state_class_counts"]),"box:unique_counts")
ck(len(us)==rob["search_box_results"]["unique_state_count"],"box:unique_n")
for c,ex in rob["search_box_results"]["examples"].items():
    cc,o,B=classify(ex["A"],ex["I"]);ck(cc==c and o==ex["winner_by_grammar"] and B==ex["B_by_grammar"],f"box:example:{c}")

# T1 dominance exhaustive on search box
for (A,I),c in us.items():
    for d in range(6):
        dom=all(A[d]>=A[e] and I[d]>=I[e] and (A[d]>A[e] or I[d]>I[e]) for e in range(6) if e!=d)
        if dom:
            cc,o,B=classify(list(A),list(I));ck(all(x==d for x in o.values()),f"T1:{A}:{I}:{d}")
# T2
ck(coeff["M-G1-SINGLE_SPLIT_RECOALESCE"]==coeff["M-G2-DELAYED_SPLIT_RECOALESCE"]==coeff["M-G5-ENDPOINT_EQUIVALENT_INTERNAL_REWRITE"],"T2:coeff")
for (A,I),_ in us.items():
    vals=[]
    for gid in ["M-G1-SINGLE_SPLIT_RECOALESCE","M-G2-DELAYED_SPLIT_RECOALESCE","M-G5-ENDPOINT_EQUIVALENT_INTERNAL_REWRITE"]:
        a,b=coeff[gid];vals.append([a*A[d]+b*I[d] for d in range(6)])
    ck(vals[0]==vals[1]==vals[2],"T2:state")
# T3
ex=theo["M_T3_DEPENDENCE_CERTIFICATE"]["counterexample"]
cc,o,B=classify(ex["A"],ex["I"])
ck(cc=="MICROGRAMMAR_DEPENDENT","T3:dependent")
ck(o["M-G0-AFFINE_UV_REPLAY"]==0 and o["M-G4-LAUNCH_CLASS_SPLIT_CONTROL"]==1,"T3:reverse")

# coverage
A,I=W["W_ASYM_BASE"]
for gid,(a,b) in coeff.items():
    base=[a*A[d]+b*I[d] for d in range(6)]
    ck(umax(base)==5,f"cov:{gid}:base")
    for t in range(6):
        shifted=[None]*6
        for d,x in enumerate(base): shifted[(d+t)%6]=x
        ck(umax(shifted)==(5+t)%6,f"cov:{gid}:{t}")

# true dynamics
INIT_I=[1,2,3,4,0,5];INIT_O=[2]*6;INIT_M=[3,3,3,3,4,3]
def blank(): return {"I":[0]*6,"O":[0]*6,"M":[[0]*6 for _ in range(6)]}
def init(c):
    if c in ("A","C"): nodes={x:blank() for x in range(6)};x=0
    else: nodes={(a,b):blank() for a in range(6) for b in range(2)};x=(0,0)
    s=nodes[x];s["I"]=INIT_I.copy();s["O"]=INIT_O.copy();s["M"][0]=INIT_M.copy()
    return {"nodes":nodes,"x":x,"ingress":0}
def tn(c,x,d):
    if c=="A": return d
    if c=="B":
        a,b=x;return (d,b^((d-a)%2))
    return x
def ti(c,x,d): return (d+(2 if c=="A" else 3 if c=="B" else 1))%6
def Bv(p,ab):
    a,b=ab;s=p["nodes"][p["x"]];i=p["ingress"]
    return [a*(s["O"][d]+s["M"][i][d])+b*s["I"][d] for d in range(6)]
def step(p,c,d):
    x=p["x"];i=p["ingress"];s=p["nodes"][x];s["O"][d]+=1;s["M"][i][d]+=1
    y=tn(c,x,d);j=ti(c,x,d);p["nodes"][y]["I"][j]+=1;p["x"]=y;p["ingress"]=j
def payload(p):
    z=[]
    for x in sorted(p["nodes"],key=repr):
        s=p["nodes"][x];z.append([repr(x),s["I"],s["O"],s["M"]])
    return [repr(p["x"]),p["ingress"],z]
def dg(p): return hashlib.sha256(json.dumps(payload(p),separators=(',',':')).encode()).hexdigest()
def to(p): return sum(sum(s["O"]) for s in p["nodes"].values())
def run(c,ab,n=48,pert=None):
    p=init(c)
    if pert: pert(p)
    rows=[];ds=[]
    for e in range(n):
        B=Bv(p,ab);d=umax(B);rows.append((e,B,d,dg(p),to(p)))
        if d is None: break
        ds.append(d);step(p,c,d)
    return p,rows,ds
CAB={"M-E0-AFFINE":(1,3),"M-E12-SPLIT2":(1,2),"M-E3-SPLIT4":(1,4),"M-E4-LAUNCH2":(2,1)}
for c in "ABC":
    for ec,ab in CAB.items():
        p,rr,ds=run(c,ab,48);fr=dyn["carriers"][c][ec]
        ck(ds==fr["d_sequence"],f"dyn:{c}:{ec}:seq")
        ck(dg(p)==fr["final_state_digest_sha256"],f"dyn:{c}:{ec}:digest")
        ck(to(p)==fr["final_TOTAL_O"],f"dyn:{c}:{ec}:O")
        for e,row in enumerate(rr): ck(row[4]==12+e,f"dyn:{c}:{ec}:mono:{e}")
ck(dyn["carriers"]["C"]["M-E3-SPLIT4"]["first_unresolved_epoch"]==8,"C:g3tie8")
ck(dyn["carriers"]["C"]["M-E0-AFFINE"]["first_unresolved_epoch"]==12,"C:g0tie12")
ck(dyn["carriers"]["C"]["M-E12-SPLIT2"]["first_unresolved_epoch"] is None,"C:g12persist")
ck(dyn["carriers"]["C"]["M-E4-LAUNCH2"]["first_unresolved_epoch"] is None,"C:g4persist")

# perturbations
def pc(j):
    def f(p): p["nodes"][p["x"]]["O"][j]+=1
    return f
def pi(j):
    def f(p): p["nodes"][p["x"]]["I"][j]+=1
    return f
def pt(j):
    def f(p):
        s=p["nodes"][p["x"]];s["O"][j]-=1;s["O"][(j+1)%6]+=1
    return f
PM={"COUNT_TOKEN":pc,"INCIDENCE":pi,"TAGGED_ADJ":pt}
for ec,ab in CAB.items():
  for c in "ABC":
    _,base,_=run(c,ab,96)
    for typ,pf in PM.items():
      fr=pert["functional_classes"][ec][c][typ]
      for j in range(6):
        _,rr,_=run(c,ab,96,pf(j));m=min(len(base),len(rr))
        div=next((e for e in range(m) if base[e][2]!=rr[e][2]),None)
        unr=next((e for e in range(m) if ((base[e][2] is None)!=(rr[e][2] is None))),None)
        reco=[e for e in range(m) if base[e][3]==rr[e][3]]
        ck(fr["first_output"][j]==rr[0][2],f"pert:{ec}:{c}:{typ}:{j}:out")
        ck(fr["first_BRC_divergence_epoch"][j]==div,f"pert:{ec}:{c}:{typ}:{j}:div")
        ck(fr["first_unresolved_status_difference_epoch"][j]==unr,f"pert:{ec}:{c}:{typ}:{j}:unr")
        ck(fr["exact_full_state_recoalescence_epochs_within_window"][j]==reco,f"pert:{ec}:{c}:{typ}:{j}:reco")
        ck(fr["perturbed_resolved_steps"][j]==sum(1 for r in rr if r[2] is not None),f"pert:{ec}:{c}:{typ}:{j}:steps")
# tie creation/removal
for ec,ab in CAB.items():
    a,b=ab;A=[6]*6;I=[1,2,3,5,0,5];B=[a*A[d]+b*I[d] for d in range(6)]
    ck(umax(B) is None and set(i for i,x in enumerate(B) if x==max(B))=={3,5},f"tiecreate:{ec}")
    ck(pert["tie_creation_from_W_S1_I3_plus1"][ec]["B"]==B,f"tiecreate_art:{ec}")
    for typ in PM:
        outs=[]
        for j in range(6):
            A=[5]*6;I=[1]*6
            if typ=="COUNT_TOKEN": A[j]+=1
            elif typ=="INCIDENCE": I[j]+=1
            else: A[j]-=1;A[(j+1)%6]+=1
            outs.append(umax([a*A[d]+b*I[d] for d in range(6)]))
        ck(outs==pert["unresolved_removal_from_fully_symmetric"][ec][typ],f"tieremove:{ec}:{typ}")

# large N common background
for sm in large["N_entries"]:
    N=int(sm)
    for gid,(a,b) in coeff.items():
        for wid,(A,I) in W.items():
            base=[a*A[d]+b*I[d] for d in range(6)]
            shifted=[a*(N+A[d])+b*I[d] for d in range(6)]
            ck(umax(base)==umax(shifted),f"large:{sm}:{gid}:{wid}")
# leak/firewalls
st={g["id"]:g["status"] for g in kill["gates"]}
ck(st["STAGE_J_K_L_ARTIFACTS_IMMUTABLE"]=="PASS_BY_GITHUB_COMPARE_PRE_MANIFEST","kill:parent")
for k,v in kill["firewalls"].items(): ck(v=="NOT_ESTABLISHED",f"firewall:{k}")
ck(kill["BRC6_NATIVE_CANONICALITY"]=="NOT_ESTABLISHED","native:withheld")

digest=hashlib.sha256("\n".join(f"{lab}:{int(ok)}" for lab,ok in checks).encode()).hexdigest()
out={"schema":"R059D_STAGE_M_DETERMINISTIC_CHECKER_OUTPUT_V1","researcher_id":"EM-R059D-9C6B2A","taskbook_source":TASK,"frozen_parent_head":PARENT,"status":"PASS" if all(v for _,v in checks) else "FAIL","checks_total":len(checks),"checks_passed":sum(v for _,v in checks),"checks_failed":sum(not v for _,v in checks),"checks_digest_sha256":digest,"large_N_method":"exact grammar-specific common-background cancellation only; no huge enumeration","raw_history_method":"exact layered history enumeration on four fixed cells plus CPBC dynamic programming","true_state_method":"exact Stage-K/L O/M/I updates on all three frozen carriers","parent_immutability":"PASS_BY_GITHUB_COMPARE_PRE_MANIFEST"}
(R/"R059D_STAGE_M_DETERMINISTIC_CHECKER_OUTPUT.json").write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
print(json.dumps(out,indent=2))
