#!/usr/bin/env python3
from __future__ import annotations
import json, hashlib, itertools
from pathlib import Path
from copy import deepcopy
R=Path(__file__).resolve().parent
TASK="f1b8cacc607373ea38322853fd1a4c9aff986d12"
PARENT="fc8abf73f67a5793334905b9863cb5f7d2030d94"
checks=[]
def ck(v,label):
    checks.append((label,bool(v)))
    if not v: raise AssertionError(label)
def J(n): return json.loads((R/n).read_text())
def umax(v):
    m=max(v); ids=[i for i,x in enumerate(v) if x==m]
    return ids[0] if len(ids)==1 else None
def umin(v):
    m=min(v); ids=[i for i,x in enumerate(v) if x==m]
    return ids[0] if len(ids)==1 else None
def spec(A,I,K=3): return [[A[d]+n*I[d] for n in range(K+1)] for d in range(6)]
def lex(s,order):
    keys=[tuple(row[n] for n in order) for row in s]
    m=max(keys); ids=[i for i,k in enumerate(keys) if k==m]
    return ids[0] if len(ids)==1 else None

eq=J("R059D_STAGE_L_EQUAL_L_ENDPOINT_PROTOCOL.json")
bp=J("R059D_STAGE_L_ENDPOINT_BRANCH_COUNT_PROTOCOL.json")
ax=J("R059D_STAGE_L_COLLAPSE_AXIOMS.json")
sel=J("R059D_STAGE_L_COUNT_MODE_SELECTOR.json")
rec=J("R059D_STAGE_L_STAGE_K_RECONCILIATION.json")
cov=J("R059D_STAGE_L_SIX_OUTCOME_COVERAGE.json")
dyn=J("R059D_STAGE_L_TRUE_DYNAMICS_ATLAS.json")
pert=J("R059D_STAGE_L_PERTURBATION_RESPONSE.json")
large=J("R059D_STAGE_L_LARGE_N_REGISTRY.json")
bnd=J("R059D_STAGE_L_BOUNDARY_AND_TIE_LEDGER.json")

for name,o in [("eq",eq),("bp",bp),("ax",ax),("sel",sel),("rec",rec),("cov",cov),("dyn",dyn),("pert",pert),("large",large),("bnd",bnd)]:
    ck(o["taskbook_source"]==TASK,f"{name}:task")
    ck(o["frozen_stage_k_head"]==PARENT,f"{name}:parent")

# endpoint index / equal-L gate
ck(eq["ALIGNED_SEGMENT_CELL_COUNT"]=="L=4","L:4")
ck(eq["cell_index_convention"]["next_aligned_endpoint_cell_index"]==3,"L:endpoint_index3")
ck(bp["B_d"]=="A_d+3*I_x[d]","B:formula")
ck(bp["optional_richer_microgrammar"].startswith("NOT_OPENED"),"B:no_richer_grammar")
ck(sel["unresolved_is_seventh_output"] is False,"selector:not7")
ck(sel["native_canonicality"]=="NOT_ESTABLISHED","selector:native_withheld")

# inherited witness reconciliation
expected={
"W_ASYM_BASE":([5,5,5,5,6,5],[1,2,3,4,0,5],[8,11,14,17,6,20],4,5,5,5,0),
"W_CONSENSUS_DOMINANT2":([5,5,10,5,5,5],[1,1,5,1,1,1],[8,8,25,8,8,8],2,2,2,2,None),
"W_FULLY_SYMMETRIC":([5]*6,[1]*6,[8]*6,None,None,None,None,None),
"W_S1_TIE_S2_RESOLVE":([6]*6,[1,2,3,4,0,5],[9,12,15,18,6,21],5,5,5,5,4),
"W_SIGNATURE_INSUFFICIENT_PAIRS":([5,5,6,6,7,7],[1,1,2,2,0,0],[8,8,12,12,7,7],None,None,None,None,None),
}
rows={x["id"]:x for x in rec["rows"]}
for wid,(A,I,B,f1,rev,ep,cm,f2) in expected.items():
    r=rows[wid]
    ck(r["A"]==A and r["I"]==I,f"rec:{wid}:AI")
    ck([A[d]+3*I[d] for d in range(6)]==B==r["B"],f"rec:{wid}:B")
    s=spec(A,I)
    ck(lex(s,[0,1,2,3])==f1,f"rec:{wid}:f1")
    ck(lex(s,[3,2,1,0])==rev,f"rec:{wid}:rev")
    ck(umax(B)==ep==cm,f"rec:{wid}:endpoint")
    scores=[-2*z[0]-2*z[1]-2*z[2]+z[3] for z in s]
    ck(umax(scores)==f2,f"rec:{wid}:f2")

# collapse axioms exact regressions
for B in itertools.product(range(4), repeat=6):
    w=umax(B)
    for c in (0,1,7,10**6):
        ck(umax([x+c for x in B])==w,f"background:{B}:{c}")
    for transform in (lambda x:2*x+1, lambda x:x**3+5):
        ck(umax([transform(x) for x in B])==w,f"monotone_rep:{B}")
    if w is not None:
        for k in (1,2,9):
            C=list(B); C[w]+=k
            ck(umax(C)==w,f"winner_monotone:{B}:{k}")

# six-outcome covariance from base witness
base=[8,11,14,17,6,20]
for t in range(6):
    shifted=[None]*6
    for d,b in enumerate(base): shifted[(d+t)%6]=b
    ck(umax(shifted)==(5+t)%6,f"coverage:{t}")
ck(set(cov["relabeled_outputs"])==set(range(6)),"coverage:surjective")

# boundary negative
h=bnd["hard_controls"]["boundary_contamination"]
ck(umax(h["wrong_truncated_C2"])==0,"boundary:wrong")
ck(umax(h["correct_endpoint_C3"])==1,"boundary:correct")
ck(h["wrong_output"]!=h["correct_output"],"boundary:contaminated")

# true-state machinery
INIT_I=[1,2,3,4,0,5]; INIT_O=[2]*6; INIT_M=[3,3,3,3,4,3]
def blank(): return {"I":[0]*6,"O":[0]*6,"M":[[0]*6 for _ in range(6)]}
def init(c):
    if c in ("A","C"):
        nodes={x:blank() for x in range(6)}; x=0
    else:
        nodes={(a,b):blank() for a in range(6) for b in range(2)}; x=(0,0)
    s=nodes[x]; s["I"]=INIT_I.copy(); s["O"]=INIT_O.copy(); s["M"][0]=INIT_M.copy()
    return {"nodes":nodes,"x":x,"ingress":0}
def tn(c,x,d):
    if c=="A": return d
    if c=="B":
        a,b=x; return (d,b^((d-a)%2))
    return x
def ti(c,x,d):
    return (d+(2 if c=="A" else 3 if c=="B" else 1))%6
def Bvec(p):
    s=p["nodes"][p["x"]]; i=p["ingress"]
    return [s["O"][d]+s["M"][i][d]+3*s["I"][d] for d in range(6)]
def step(p,c,d):
    x=p["x"]; i=p["ingress"]; s=p["nodes"][x]
    s["O"][d]+=1; s["M"][i][d]+=1
    y=tn(c,x,d); j=ti(c,x,d); p["nodes"][y]["I"][j]+=1
    p["x"]=y; p["ingress"]=j
def payload(p):
    data=[]
    for x in sorted(p["nodes"],key=repr):
        s=p["nodes"][x]; data.append([repr(x),s["I"],s["O"],s["M"]])
    return [repr(p["x"]),p["ingress"],data]
def dg(p): return hashlib.sha256(json.dumps(payload(p),separators=(',',':')).encode()).hexdigest()
def totO(p): return sum(sum(s["O"]) for s in p["nodes"].values())
def totI(p): return sum(sum(s["I"]) for s in p["nodes"].values())
def run(c,n=48,perturb=None):
    p=init(c)
    if perturb: perturb(p)
    rows=[]; ds=[]
    for e in range(n):
        b=Bvec(p); d=umax(b)
        rows.append((e,b,d,dg(p),totO(p),totI(p)))
        if d is None: break
        ds.append(d); step(p,c,d)
    return p,rows,ds

for c in "ABC":
    p,rr,ds=run(c,48)
    a=dyn["carriers"][c]
    ck(ds==a["d_sequence"],f"dyn:{c}:dseq")
    ck([(ds[i+1]-ds[i])%6 for i in range(len(ds)-1)]==a["r_sequence"],f"dyn:{c}:rseq")
    ck(dg(p)==a["final_state_digest_sha256"],f"dyn:{c}:digest")
    ck(totO(p)==a["final_TOTAL_O"],f"dyn:{c}:totalO")
    for e,row in enumerate(rr):
        ck(row[4]==12+e,f"dyn:{c}:TOTALO:{e}")

# perturbations
def pc(j):
    def f(p): p["nodes"][p["x"]]["O"][j]+=1
    return f
def pi(j):
    def f(p): p["nodes"][p["x"]]["I"][j]+=1
    return f
def pt(j):
    def f(p):
        s=p["nodes"][p["x"]]; s["O"][j]-=1; s["O"][(j+1)%6]+=1
    return f
pmap={"COUNT_TOKEN":pc,"INCIDENCE":pi,"TAGGED_ADJ":pt}
for typ,pf in pmap.items():
    first=[]
    for j in range(6):
        _,rr,_=run("A",1,pf(j)); first.append(rr[0][2])
    ck(first==pert["first_decision_tables"][typ],f"pert:first:{typ}")
# perturbation trajectory regression against frozen artifact
for typ,pf in pmap.items():
    for c in "ABC":
        _,base_rows,_=run(c,96)
        frozen_rows=pert["classes"][typ][c]
        for j in range(6):
            _,pr,_=run(c,96,pf(j))
            first_div=None; first_unr=None; reco=[]
            for e in range(min(len(base_rows),len(pr))):
                if base_rows[e][2]!=pr[e][2] and first_div is None: first_div=e
                if ((base_rows[e][2] is None)!=(pr[e][2] is None)) and first_unr is None: first_unr=e
                if base_rows[e][3]==pr[e][3]: reco.append(e)
            fr=frozen_rows[j]
            ck(first_div==fr["first_BRC_divergence_epoch"],f"perttraj:{typ}:{c}:{j}:div")
            ck(first_unr==fr["first_unresolved_status_difference_epoch"],f"perttraj:{typ}:{c}:{j}:unr")
            ck(reco==fr["exact_full_state_recoalescence_epochs_within_window"],f"perttraj:{typ}:{c}:{j}:reco")
            ck(pr[0][2]==fr["first_output"],f"perttraj:{typ}:{c}:{j}:first")
            ck(sum(1 for row in pr if row[2] is not None)==fr["perturbed_resolved_steps"],f"perttraj:{typ}:{c}:{j}:steps")

# unresolved create/remove
A=[6]*6; I=[1,2,3,4,0,5]; I[3]+=1
ck([A[d]+3*I[d] for d in range(6)]==pert["unresolved_creation"]["after_B"],"pert:tiecreate:B")
ck(umax(pert["unresolved_creation"]["after_B"]) is None,"pert:tiecreate:unres")
symA=[5]*6; symI=[1]*6
for typ in pmap:
    outs=[]
    for j in range(6):
        A=symA.copy(); I=symI.copy()
        if typ=="COUNT_TOKEN": A[j]+=1
        elif typ=="INCIDENCE": I[j]+=1
        else: A[j]-=1; A[(j+1)%6]+=1
        outs.append(umax([A[d]+3*I[d] for d in range(6)]))
    ck(outs==pert["unresolved_removal_from_symmetric"][typ]["outputs"],f"pert:remove:{typ}")

# large N symbolic cancellation
for sm in large["N_entries"]:
    N=int(sm)
    for r in rec["rows"]:
        B=r["B"]; ck(umax([N+x for x in B])==umax(B),f"large:{sm}:{r['id']}")

# firewalls / source discipline
for k,v in bnd["firewalls"].items(): ck(v=="NOT_ESTABLISHED",f"firewall:{k}")
ck(rec["summary"].startswith("Stage-L count-mode equals Stage-K ENDPOINT-MAX"),"reconcile:semantic")
ck(dyn["freeze"]=="BRC6_ENDPOINT_COUNT_TRUE_STATE_DYNAMICS_ESTABLISHED","dyn:freeze")

digest=hashlib.sha256("\n".join(f"{lab}:{int(ok)}" for lab,ok in checks).encode()).hexdigest()
out={
"schema":"R059D_STAGE_L_DETERMINISTIC_CHECKER_OUTPUT_V1",
"researcher_id":"EM-R059D-9C6B2A","taskbook_source":TASK,"frozen_parent_head":PARENT,
"status":"PASS" if all(v for _,v in checks) else "FAIL",
"checks_total":len(checks),"checks_passed":sum(v for _,v in checks),"checks_failed":sum(not v for _,v in checks),
"checks_digest_sha256":digest,
"large_N_method":"exact common-background cancellation only; no huge object/history enumeration",
"true_state_method":"exact O/M/I event update on all three frozen Stage-K carriers",
"parent_immutability":"PASS_BY_GITHUB_COMPARE_PRE_MANIFEST"
}
(R/"R059D_STAGE_L_DETERMINISTIC_CHECKER_OUTPUT.json").write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
print(json.dumps(out,indent=2))
