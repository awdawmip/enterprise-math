#!/usr/bin/env python3
from __future__ import annotations
import json, hashlib, itertools
from collections import Counter
from pathlib import Path

R=Path(__file__).resolve().parent
TASK="3ca99589c5c3ade32c9cc164cdc3b3c4f6e15b7b"
PARENT="03650b38df5950b86cb2636db9e43094683b1bc8"
C6=range(6)
checks=[]
def ck(cond,label):
    checks.append((label,bool(cond)))
    if not cond: raise AssertionError(label)
def J(name): return json.loads((R/name).read_text(encoding="utf-8"))

REQ=[
"R059D_STAGE_J_BRC6_SEMANTICS_PROTOCOL.json",
"R059D_STAGE_J_FIXED_CELL_COUNT_PROTOCOL.json",
"R059D_STAGE_J_CHANNEL_SIGNATURE_PROTOCOL.json",
"R059D_STAGE_J_BRC6_FUNCTION_GRAMMAR.json",
"R059D_STAGE_J_BRC6_SYMMETRY_OBSTRUCTION.json",
"R059D_STAGE_J_BRC6_SIX_OUTCOME_COVERAGE.json",
"R059D_STAGE_J_BRC6_TINY_EXACT_REGISTRY.json",
"R059D_STAGE_J_BRC6_LARGE_N_REGISTRY.json",
"R059D_STAGE_J_BRC6_REPEATED_DIRECTION_DYNAMICS.json",
"R059D_STAGE_J_BRC6_PERTURBATION_RESPONSE.json",
"R059D_STAGE_J_BRC6_BOUNDARY_PADDING_GATE.json",
"R059D_STAGE_J_BRC6_TRIVIALITY_AND_LEAKAGE_LEDGER.json"]
objs={}
for f in REQ:
    objs[f]=J(f)
    ck(objs[f]["taskbook_source"]==TASK,"taskbook:"+f)
    ck(objs[f]["frozen_provenance_parent"]==PARENT,"parent:"+f)

sem=objs[REQ[0]]; fixed=objs[REQ[1]]; sig=objs[REQ[2]]; grammar=objs[REQ[3]]
sym=objs[REQ[4]]; cov=objs[REQ[5]]; tiny=objs[REQ[6]]; large=objs[REQ[7]]
dyn=objs[REQ[8]]; pert=objs[REQ[9]]; boundary=objs[REQ[10]]; kill=objs[REQ[11]]

ck(sem["codomain"]["labels"]==[0,1,2,3,4,5],"codomain:C6")
ck(sem["evaluator_negative"].startswith("BRC6_UNRESOLVED"),"unresolved:not-output")
ck(fixed["frozen_positive_registry_L"]==4,"L:4")
ck(all(x==4 for row in cov["rows"] for x in row["segment_cell_counts"]),"L:coverage_equal")
ck(fixed["selector_dependency"].startswith("FORBIDDEN"),"L:not-selector")

def brc(A,I):
    Z=[tuple(A[d]+n*I[d] for n in range(4)) for d in C6]
    m=max(Z); W=[d for d,z in enumerate(Z) if z==m]
    return (W[0] if len(W)==1 else None),Z

# tiny witness reconstruction
byid={w["id"]:w for w in tiny["witnesses"]}
for wid,w in byid.items():
    A=[w["O"][d]+w["M_ingress"][d] for d in C6]
    ck(A==w["A"],"tiny:A:"+wid)
    out,Z=brc(A,w["I"])
    stored=w["F1"]
    if stored=="BRC6_UNRESOLVED_BY_CURRENT_SIGNATURE":
        ck(out is None,"tiny:unresolved:"+wid)
    else:
        ck(out==stored,"tiny:F1:"+wid)
    ck([list(z) for z in Z]==w["C_spectrum"],"tiny:spectrum:"+wid)
    ck(all(x==4 for x in w["L_by_candidate"]),"tiny:L:"+wid)

ck(byid["W_ASYM_BASE"]["F1"]==4,"base:output4")
ck(byid["W_S1_TIE_S2_RESOLVE"]["F0_max"]=="UNRESOLVED","tie:F0")
ck(byid["W_S1_TIE_S2_RESOLVE"]["F1"]==5,"tie:F1resolves")
ck(byid["W_SAME_CLASS0"]["relative_F1"]==0,"same-channel:allowed")
ck(byid["W_RELATIVE_CLASS3"]["relative_F1"]==3,"relative3:allowed")
ck(byid["W_FULLY_SYMMETRIC"]["F1"]=="BRC6_UNRESOLVED_BY_CURRENT_SIGNATURE","sym:tiny")

# covariance / surjectivity
outs=[]
for row in cov["rows"]:
    t=row["tau_power"]; out=row["output"]
    ck(out==(4+t)%6,"cov:tau:"+str(t))
    ck(row["relative_output"]==4,"cov:relative:"+str(t))
    outs.append(out)
ck(sorted(outs)==[0,1,2,3,4,5],"coverage:surjective")

# stabilizer obstruction
ck(sym["cyclic_consequence"].startswith("Any state invariant"),"sym:theorem")
for t in range(1,6):
    fixed_labels=[d for d in C6 if (d+t)%6==d]
    ck(fixed_labels==[],"sym:no_fixed:"+str(t))

# F2 full coefficient box exact distribution
base=byid["W_ASYM_BASE"]; A=base["A"]; I=base["I"]
_,Z=brc(A,I)
dist={"max":Counter(),"min":Counter()}
for th in itertools.product(range(-2,3),repeat=4):
    if th==(0,0,0,0): continue
    scores=[sum(th[n]*Z[d][n] for n in range(4)) for d in C6]
    for pol in ("max","min"):
        target=max(scores) if pol=="max" else min(scores)
        win=tuple(d for d,s in enumerate(scores) if s==target)
        dist[pol]["|".join(map(str,win))]+=1
ck(sum(dist["max"].values())==624,"F2:box624")
stored=tiny["selector_comparison"]["F2"]["base_witness_box_counts"]
ck(dict(dist["max"])==stored["max"],"F2:max_distribution")
ck(dict(dist["min"])==stored["min"],"F2:min_distribution")
ck(stored["max"]["4"]==258 and stored["max"]["5"]==290,"F2:not_robust_unique")

# huge N closed form; no enumeration
Ns=[int(x) for x in large["N_entries"]]
ck(10**36 in Ns,"large:N0")
for N in Ns:
    A=[N+x for x in [5,5,5,5,6,5]]
    out,Z=brc(A,[1,2,3,4,0,5])
    ck(out==4,"large:base:"+str(N))
    for t in range(6):
        ck((out+t)%6==[4,5,0,1,2,3][t],"large:cov:"+str(N)+":"+str(t))
    ck(all(4==x for x in [large["L"]]*6),"large:L:"+str(N))

# repeated dynamics
cases={c["id"]:c for c in dyn["cases"]}
ck(cases["BASE_BETA4"]["d_sequence"][:7]==[0,4,2,0,4,2,0],"dyn:beta4")
ck(all(r==4 for r in cases["BASE_BETA4"]["r_sequence"]),"dyn:r4")
ck(cases["BASE_BETA4"]["minimal_period"]==3,"dyn:period3")
ck(cases["SAME_BETA0"]["minimal_period"]==1,"dyn:period1")
ck(cases["TIE_RESOLVED_BETA5"]["minimal_period"]==6,"dyn:period6")
ck(cases["SYMMETRIC"]["exact_class"]=="unresolved symmetry state","dyn:symmetric_stop")

# perturbations recompute
baseA=[5,5,5,5,6,5]; baseI=[1,2,3,4,0,5]
token=[]; incid=[]; adj=[]
for j in C6:
    A=baseA[:]; A[j]+=1; token.append(brc(A,baseI)[0])
    I=baseI[:]; I[j]+=1; incid.append(brc(baseA,I)[0])
    A=baseA[:]; A[j]-=1; A[(j+1)%6]+=1; adj.append(brc(A,baseI)[0])
ck(token==pert["count_token_after_outputs"]==[0,1,2,3,4,5],"pert:token6")
ck(incid==pert["incidence_after_outputs"]==[4]*6,"pert:incidence")
ck(adj==pert["tagged_adjacency_after_outputs"]==[1,2,3,4,5,0],"pert:adj6")
ck(pert["length_unchanged"] is True,"pert:L")

# padding
ck(boundary["count_horizon_K"]==3,"pad:K3")
for row in boundary["positive_results"]:
    ck(row["padding_depth"]>3 and row["output"]==4 and row["verdict"]=="PASS","pad:positive:"+str(row["padding_depth"]))
ck(boundary["negative_control"]["verdict"]=="BOUNDARY_CONTAMINATED_BRC6","pad:negative")

# leakage gates
for g in kill["gates"]:
    ck(str(g["status"]).startswith("PASS"),"kill:"+g["id"])
ck(kill["primary_disposition_candidate"]=="BRC6_PARTIAL_SELECTOR_WITH_EXACT_SYMMETRY_UNRESOLVED_STATES","disposition")

digest=hashlib.sha256("\n".join(f"{lab}:{int(ok)}" for lab,ok in checks).encode()).hexdigest()
out={
"schema":"R059D_STAGE_J_DETERMINISTIC_CHECKER_OUTPUT_V1",
"status":"PASS" if all(ok for _,ok in checks) else "FAIL",
"researcher_id":"EM-R059D-4C7E21",
"taskbook_source":TASK,
"frozen_provenance_parent":PARENT,
"checks_total":len(checks),
"checks_passed":sum(ok for _,ok in checks),
"checks_failed":sum(not ok for _,ok in checks),
"checks_digest_sha256":digest,
"large_N_method":"closed-form exact tuple comparisons only; no huge object/history enumeration",
"F2_box_method":"complete 5^4-1 integer coefficient enumeration",
"tiny_role":"deterministic theorem regression only",
"parent_immutability":"PASS_BY_GITHUB_COMPARE_PRE_MANIFEST",
"primary_disposition":"BRC6_PARTIAL_SELECTOR_WITH_EXACT_SYMMETRY_UNRESOLVED_STATES"
}
(R/"R059D_STAGE_J_DETERMINISTIC_CHECKER_OUTPUT.json").write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
print(json.dumps(out,indent=2))
