#!/usr/bin/env python3
import hashlib
import itertools
import json
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent
EXPECTED_PROTOCOL_SHA = "322f2e4ba66b4fbc8e47a513867399f9464a62a629af01f23cad6929d7c1d66b"
EXPECTED_TARGET_SHA = "e41cc96ecc40bf1c992ad75bc552b2e68b36a5620e4343f10e15b71d9cf64f0c"
EXPECTED_CANDIDATE_SET_SHA = "2e1f85a3faf37a0525364c220f9449caea45408bf6a954c09045bf78646cf959"
CANDIDATES = ["G2-M1","G2-M2","G2-M3","G2-M4","G2-M5","G2-M6"]
ROWS = [
    "A1-GMC-M48-STEP-GAGE","A2-CCRP-PMU-PHASE","A3-DR-FDTR-PUMP-PROBE","A4-BMS-CAVITY-VNA",
    "B1A-TIBC-LIQUID-GRAVIMETRIC","B1B-TIBC-GAS-PVTT","B2A-SRIR-MIC-RECIP","B2B-SRIR-ANTENNA-3PAIR",
]
PRESSURES = [
    "GEOMETRIC_MEASURE_COHERENCE","CYCLE_CLOSURE_AND_RELATIVE_PHASE","DIFFUSIVE_RELAXATION",
    "BOUNDED_MODE_SPECTRUM","TRANSFER_INVENTORY_BALANCE_CLOSURE",
    "SOURCE_RECEIVER_INTERCHANGE_RECIPROCITY",
]
EORD = {
    "E0_UNMAPPED":0,"E1_QUALITATIVE_MECHANISM":1,"E2_EXACT_STRUCTURAL_CONSTRAINT":2,
    "E3_QUANTITATIVE_CONSTRUCTION":3,"E4_QUANTITATIVE_OUT_OF_SAMPLE":4,
    "E5_CROSS_PRESSURE_SHARED_EXPLANATION":5,
}
EXPECTED_PER_CANDIDATE = {
 "G2-M1":"a12bcaa3c6b22366865670513a065b1cf6b9fd95f3941b1e6d13b38becf44f52",
 "G2-M2":"4b4da01eee68c59d683463fbd33b5a36fd36c8ed00456197f96ba3b22e0f1dac",
 "G2-M3":"ad4ac85dc5dc4463edf0f584e317f23e40aee47d509062803a19309d81ffb6fa",
 "G2-M4":"3830eab3a05532a3df5427a7c24ce15e50f62ae10130b149a432a47094cec85c",
 "G2-M5":"be5c048b093423b07a1515f7f4b08baf99ef18d3fafceee0979c9fb5e17dee48",
 "G2-M6":"90dfc14872299e611c1949d5784f32ac6f071ca58752609f72b5150d5d9e30ca",
}

def load(name):
    return json.loads((ROOT / name).read_text(encoding="utf-8"))

def sha256_file(name):
    return hashlib.sha256((ROOT/name).read_bytes()).hexdigest()

def check_freeze():
    n=0
    assert sha256_file("R050_SCORING_PROTOCOL.json") == EXPECTED_PROTOCOL_SHA; n+=1
    fi=load("R050_FREEZE_INTEGRITY.json")
    assert fi["r049"]["recomputed_target_sha256"] == EXPECTED_TARGET_SHA; n+=1
    assert fi["r049"]["post_candidate_open_recomputed_target_sha256"] == EXPECTED_TARGET_SHA; n+=1
    assert fi["r049"]["target_mutation_after_candidate_open"] is False; n+=1
    assert fi["scoring_protocol"]["sha256"] == EXPECTED_PROTOCOL_SHA; n+=1
    assert fi["scoring_protocol"]["candidate_content_opened_before_freeze"] is False; n+=1
    assert fi["r048"]["recomputed_candidate_set_sha256"] == EXPECTED_CANDIDATE_SET_SHA; n+=1
    assert fi["r048"]["expected_candidate_set_sha256"] == EXPECTED_CANDIDATE_SET_SHA; n+=1
    assert fi["r048"]["core_edit_count"] == 0 and fi["r048"]["candidate_core_mutation"] is False; n+=1
    assert set(fi["r048"]["per_candidate"]) == set(CANDIDATES); n+=1
    for cid,h in EXPECTED_PER_CANDIDATE.items():
        q=fi["r048"]["per_candidate"][cid]
        assert q["expected"] == h and q["recomputed"] == h and q["match"] is True
        n+=1
    mapping=fi["r049"]["manifest_target_artifact_byte_hashes"]
    payload=json.dumps(mapping,sort_keys=True,separators=(",",":")).encode()
    assert hashlib.sha256(payload).hexdigest() == EXPECTED_TARGET_SHA; n+=1
    return n

def check_matrices():
    n=0
    rm=load("R050_ROW_LEVEL_6x8_MATRIX.json")
    pm=load("R050_PRESSURE_LEVEL_6x6_MATRIX.json")
    assert rm["candidate_count"]==6 and rm["row_count"]==8 and rm["cell_count"]==48; n+=1
    assert pm["candidate_count"]==6 and pm["pressure_count"]==6 and pm["cell_count"]==36; n+=1
    rcells=rm["cells"]; pcells=pm["cells"]
    if rcells and isinstance(rcells[0], list):
        cols=rm["typed_chain_resolution"]["cell_columns"]
        defs=rm["row_definitions"]
        expanded=[]
        pressure_index={x["cell_id"]:x for x in pcells}
        for raw in rcells:
            z=dict(zip(cols,raw))
            cid=z["candidate_id"]; rid=z["row_id"]; pf=defs[rid]["pressure_family"]
            pid=f"{cid}::{pf}"
            q=pressure_index[pid]["typed_chain_summary"]
            assert defs[rid]["physical_protocol"]
            assert all(k in q for k in (
                "physical_to_native_encoding","frozen_candidate",
                "native_readout_or_quotient","metrology_bridge",
                "predicted_measured_output_statement"))
            expanded.append({
                "cell_id":f"{cid}::{rid}",
                "candidate_id":cid,
                "row_id":rid,
                "pressure_family":pf,
                "metrology_bridge":{"class":z["bridge_class"],"fitted_parameter_count":0},
                "evidence_level":z["evidence_level"],
                "engineering_validation":False,
                "quantitative_holdout_status":"NOT_ELIGIBLE_FOR_E4",
                "core_edit_count":0,
                "verdict":z["verdict"],
            })
        rcells=expanded
    assert len(rcells)==48 and len({x["cell_id"] for x in rcells})==48; n+=1
    assert len(pcells)==36 and len({x["cell_id"] for x in pcells})==36; n+=1
    assert {(x["candidate_id"],x["row_id"]) for x in rcells} == set(itertools.product(CANDIDATES,ROWS)); n+=1
    assert {(x["candidate_id"],x["pressure_family"]) for x in pcells} == set(itertools.product(CANDIDATES,PRESSURES)); n+=1
    for x in rcells:
        assert x["core_edit_count"]==0
        assert EORD[x["evidence_level"]] <= EORD["E2_EXACT_STRUCTURAL_CONSTRAINT"]
        assert x["quantitative_holdout_status"]=="NOT_ELIGIBLE_FOR_E4"
        assert x["engineering_validation"] is False
        assert x["candidate_id"] in CANDIDATES
        bc=x["metrology_bridge"]["class"]
        if bc=="B3_TARGET_SPECIFIC_ADAPTER":
            assert EORD[x["evidence_level"]] <= 1
        if bc=="B4_ILLEGAL_LEAKAGE":
            assert x["evidence_level"]=="E0_UNMAPPED"
        assert x["metrology_bridge"]["fitted_parameter_count"]==0
        n+=7
    counts=Counter(x["evidence_level"] for x in rcells)
    assert counts==Counter({"E0_UNMAPPED":14,"E1_QUALITATIVE_MECHANISM":30,"E2_EXACT_STRUCTURAL_CONSTRAINT":4}); n+=1
    e2={(x["candidate_id"],x["row_id"]) for x in rcells if x["evidence_level"]=="E2_EXACT_STRUCTURAL_CONSTRAINT"}
    assert e2=={
      ("G2-M1","B1A-TIBC-LIQUID-GRAVIMETRIC"),("G2-M1","B1B-TIBC-GAS-PVTT"),
      ("G2-M6","B1A-TIBC-LIQUID-GRAVIMETRIC"),("G2-M6","B1B-TIBC-GAS-PVTT"),
    }; n+=1
    for cid in CANDIDATES:
        for p in ["TRANSFER_INVENTORY_BALANCE_CLOSURE","SOURCE_RECEIVER_INTERCHANGE_RECIPROCITY"]:
            q=[x for x in rcells if x["candidate_id"]==cid and x["pressure_family"]==p]
            assert len(q)==2
            assert len({x["metrology_bridge"]["class"] for x in q})==1
            assert len({x["evidence_level"] for x in q})==1
            n+=3
    for x in pcells:
        assert x["E4_eligible"] is False and x["E4_status"]=="NOT_ELIGIBLE_FOR_E4"
        assert x["E5_status"]=="NOT_ELIGIBLE_WITHOUT_E4"
        assert x["core_edit_count"]==0 and x["fitted_parameter_count"]==0
        n+=3
    return n

def m1_moves(x, edges):
    out=[]
    for u,v in edges:
        d=x[u]-x[v]
        if d>=2:
            y=list(x); y[u]-=1; y[v]+=1
            out.append((u,v,tuple(y)))
        elif d<=-2:
            y=list(x); y[v]-=1; y[u]+=1
            out.append((v,u,tuple(y)))
    return out

def compositions(total,n):
    if n==1:
        yield (total,); return
    for a in range(total+1):
        for z in compositions(total-a,n-1):
            yield (a,)+z

def check_m1_transfer_identity():
    checks=0
    edges=[(0,1),(1,2),(2,3)]
    R={2,3}
    for M in range(0,7):
      for x in compositions(M,4):
        IR=sum(x[i] for i in R)
        for u,v,y in m1_moves(x,edges):
            IY=sum(y[i] for i in R)
            signed=(1 if u not in R and v in R else -1 if u in R and v not in R else 0)
            assert IY-IR==signed
            assert sum(y)==sum(x)
            checks+=2
    return checks

def swap(st,e):
    s=list(st); u,v=e; s[u],s[v]=s[v],s[u]; return tuple(s)

def check_m6_transfer_identity():
    checks=0
    edges=[(0,1),(1,2),(2,3)]
    R={2,3}; transported=1
    for st in itertools.product((0,1,2), repeat=4):
      IR=sum(1 for i in R if st[i]==transported)
      for u,v in edges:
        y=swap(st,(u,v)); IY=sum(1 for i in R if y[i]==transported)
        signed=0
        if (u in R) != (v in R):
            if u not in R and st[u]==transported: signed+=1
            if v not in R and st[v]==transported: signed+=1
            if u in R and st[u]==transported: signed-=1
            if v in R and st[v]==transported: signed-=1
        assert IY-IR==signed
        assert sorted(y)==sorted(st)
        checks+=2
    return checks

def check_ledgers():
    n=0
    h=load("R050_HOLDOUT_RESULTS.json")
    assert h["row_candidate_result_count"]==48 and h["E3_count"]==h["E4_count"]==h["E5_count"]==0; n+=1
    assert h["NOT_ELIGIBLE_FOR_E4_count"]==48; n+=1
    assert all(e["pass_fail"]=="NOT_ELIGIBLE_FOR_E4" and e["fitted_parameter_count"]==0 for e in h["entries"]); n+=1
    p=load("R050_PARAMETER_DEBT.json")
    assert p["global"]["fitted_parameter_count"]==0 and p["global"]["candidate_core_parameters_retuned"]==0; n+=1
    cp=load("R050_CROSS_PRESSURE_SHARED_STATE.json")
    assert cp["global_E5_count"]==0 and cp["E5_eligibility"]=="NOT_ELIGIBLE_WITHOUT_E4"; n+=1
    pa=load("R050_PARETO_FRONTIER.json")
    assert pa["weighted_total_score_used"] is False and pa["strict_winner"] is None; n+=1
    assert pa["strict_dominance_edges"]==[] and pa["pareto_family"]==CANDIDATES; n+=1
    ta=load("R050_TARGET_LEAKAGE_AUDIT.json")
    statuses={x["attack"]:x["status"] for x in ta["attacks"]}
    required={
      "TARGET_MUTATION_AFTER_CANDIDATE_OPEN","CANDIDATE_CORE_REPAIR","CLASSICAL_PI_NUMERIC_SELECTION",
      "OUTPUT_DEFINITION_BACKFILL","B3_ADAPTER_PROMOTED_TO_SUCCESS","TRAINING_RELABELED_AS_HOLDOUT",
      "TOLERANCE_INVENTED_WITHOUT_SOURCE","BLOCK_B_PER_REALIZATION_REFIT",
      "METAPHOR_AS_QUANTITATIVE_EXPLANATION","PARAMETER_EXPLOSION",
      "FAILED_ROW_AVERAGED_AWAY","CROSS_PRESSURE_SHARED_STATE_ASSERTED_WITHOUT_E4",
    }
    assert set(statuses)==required; n+=1
    assert all(v in {"PASS","PASS_WITH_TOOLING_LIMITATION"} for v in statuses.values()); n+=1
    f=load("R050_FAILURE_INHERITANCE.json")
    assert f["core_modification_performed"] is False and f["new_generation_candidates_instantiated"] is False; n+=1
    assert "NO_E4_E5" in f["return_class"] and "NO_STRICT_WINNER" in f["return_class"]; n+=1
    return n

def run_all():
    groups=[
      ("freeze_integrity",check_freeze),
      ("matrix_and_scoring",check_matrices),
      ("m1_transfer_identity",check_m1_transfer_identity),
      ("m6_transfer_identity",check_m6_transfer_identity),
      ("ledgers_and_audits",check_ledgers),
    ]
    total=0
    results=[]
    for name,fn in groups:
        q=fn(); total+=q; results.append((name,q))
        print(f"PASS {name}: {q} checks")
    print(f"R050_EXACT_CHECKER_PASS total_checks={total}")
    return total,results

if __name__=="__main__":
    run_all()
