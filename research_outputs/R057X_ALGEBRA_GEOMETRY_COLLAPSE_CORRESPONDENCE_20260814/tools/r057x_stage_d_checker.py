#!/usr/bin/env python3
import json, hashlib, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]/"artifacts"
EXPECTED={
  "R057X_COMMON_UNEXPLAINED_RESIDUAL_LEDGER.json": "246be6b794b2b6264ec644f784e70910b50fd7dedee6ab4b0719364d024b7e1b",
  "R057X_NORMALIZED_RESIDUAL_TRAJECTORY_COMPARISON.json": "b27f67a5ff5460e6ab9088f97b5a57b6851daa11fcd27fff56eb8febf2b16366",
  "R057X_STAGE_D_INPUT_REGISTRY.json": "dc770e6c2902f5dbf2821093ba9f7f2ecc7eceb12158c42b865bb00ca5ac5e5c",
  "R057X_STAGE_D_REPORT.md": "d350ce6877a2670e73673c9c2bd62b96150721f416a79b8e60a308bec9d4fa3d",
  "R057X_STAGE_D_RESIDUAL_STRUCTURE_CHECKPOINT.json": "7059ec68f6ace7cb46360476b7378b12b06dbb5a426269c20ae598e6bde1e771",
  "R057X_STAR_RESIDUAL_CAUSE_CROSSWALK.json": "2d2ac928213595d420248976afbd53160362a4ab7b752c9de9a53e51db1a95f3",
  "R057X_STAR_RESIDUAL_COORDINATE_COMPARISON.json": "f71e38b12866e2f3f2154d8d678ef76c7d3b8dac7ea91b062c4be0ea3159cf6b"
}
checks=[]
def ck(name, cond):
    checks.append((name,bool(cond)))
def load(n):
    return json.loads((ROOT/n).read_text(encoding="utf-8"))
for n,h in EXPECTED.items():
    ck("sha256:"+n, hashlib.sha256((ROOT/n).read_bytes()).hexdigest()==h)
inp=load("R057X_STAGE_D_INPUT_REGISTRY.json")
cw=load("R057X_STAR_RESIDUAL_CAUSE_CROSSWALK.json")
tr=load("R057X_NORMALIZED_RESIDUAL_TRAJECTORY_COMPARISON.json")
co=load("R057X_STAR_RESIDUAL_COORDINATE_COMPARISON.json")
un=load("R057X_COMMON_UNEXPLAINED_RESIDUAL_LEDGER.json")
cp=load("R057X_STAGE_D_RESIDUAL_STRUCTURE_CHECKPOINT.json")
ck("input_gate_pass",inp["gate_result"]=="PASS")
ck("A_checkpoint",inp["A"]["residual_diagnostic_checkpoint_sha256"]=="4f2280c85a831b0270b03a15f377f7dbb51569351b513d9b79bd7aaac35ea0f0")
ck("G_checkpoint",inp["G"]["residual_diagnostic_checkpoint_sha256"]=="21f051e5f2cfe276a1a746112968ca7d8ca6dedee2efe9fe006da94e47f9726b")
ck("C1_checkpoint",inp["cross_arm_semantic_anchor"]["checkpoint_sha256"]=="1af2df3eefbb1eeee35418d59edf197657d91c1e14c47e8fdf319aab00a9c75d")
ck("A_repro_exact",inp["A"]["reproduction_gate"]["exact_difference_zero"] is True)
ck("G_repro_204",inp["G"]["reproduction_gate"]["checks"]==204)
ck("G_repro_max",inp["G"]["reproduction_gate"]["max_abs_difference"]==8.881784197001252e-16)
ck("G_bytes",inp["G"]["byte_reproduction"]=="PASS_8_OF_8")
ck("R057Y_false",inp["taskbook"]["R057Y_consumed"] is False)
rows={r["cause"]:r for r in cw["rows"]}
ck("assembly_A",rows["ASSEMBLY_ACTIVE_SET_SWITCHING"]["A_rating"]=="NOT_SUPPORTED")
ck("assembly_G",rows["ASSEMBLY_ACTIVE_SET_SWITCHING"]["G_rating"]=="NOT_SUPPORTED")
ck("feature_A_weak",rows["FEATURE_COVARIANCE_DRIFT"]["A_rating"]=="WEAK_SUPPORT")
ck("feature_G_supported",rows["FEATURE_COVARIANCE_DRIFT"]["G_rating"]=="SUPPORTED")
ck("packet_A_weak",rows["PACKET_MIXTURE_EVOLUTION"]["A_rating"]=="WEAK_SUPPORT")
ck("packet_G_supported",rows["PACKET_MIXTURE_EVOLUTION"]["G_rating"]=="SUPPORTED")
ck("phase_A_weak",rows["PHASE_MIXTURE"]["A_rating"]=="WEAK_SUPPORT")
ck("phase_G_supported",rows["PHASE_MIXTURE"]["G_rating"]=="SUPPORTED")
ck("orientation_specific",rows["ORIENTATION_MIXTURE"]["crosswalk_classification"]=="ARM_SPECIFIC_OBSERVABLE")
ck("finite_common",rows["FINITE_SCALE_EFFECT"]["crosswalk_classification"]=="COMMON_SUPPORTED")
ck("unexplained_common",rows["UNEXPLAINED_RESIDUAL_STRUCTURE"]["crosswalk_classification"]=="COMMON_SUPPORTED")
ck("A_rebound",tr["A"]["RESIDUAL_REBOUND_AFTER_MIXTURE_CONTRACTION"]=="SUPPORTED")
ck("G_rebound_insufficient",tr["G"]["RESIDUAL_REBOUND_AFTER_MIXTURE_CONTRACTION"]=="INSUFFICIENT")
ck("common_rebound_insufficient",tr["cross_arm"]["post_mixture_rebound_signature"]=="INSUFFICIENT")
ck("G_rank",tr["G"]["D2_RMSE_rank_low_to_high"]==[47,113,181,71,29,17,11,7])
ck("corr_sign_changes",co["G"]["correlation_sign_change_count_by_sorted_radius"]==4)
ck("run_stability_not_established",co["questions"]["RUN_DEFECT_more_stable_than_AREA_in_both_arms"]=="NOT_ESTABLISHED")
ck("assembly_exclusion",un["D4"]["assembly_exclusion"]["status"]=="COMMON_ASSEMBLY_SWITCHING_EXCLUSION")
ck("finite_component",un["D4"]["finite_scale_commonality"]["status"]=="COMMON_FINITE_SCALE_RESIDUAL_COMPONENT")
ck("G_burden",un["D4"]["carrier_specific_mixture_burden"]["status"]=="G_CARRIER_MIXTURE_BURDEN_STRONGER")
ck("primary_disposition",un["primary_disposition"]=="MIXED_COMMON_AND_CARRIER_SPECIFIC_RESIDUAL_STRUCTURE")
ck("cp_disposition",cp["primary_disposition"]=="MIXED_COMMON_AND_CARRIER_SPECIFIC_RESIDUAL_STRUCTURE")
ck("no_fit",cp["epistemic"]["fit_status"]=="NO_STAGE_D_FIT")
for k,v in cp["prohibitions_verified"].items():
    ck("prohibition:"+k, v is False)
failed=[n for n,v in checks if not v]
print(json.dumps({"status":"PASS" if not failed else "FAIL","pass_count":sum(v for _,v in checks),"check_count":len(checks),"failures":failed},sort_keys=True))
sys.exit(1 if failed else 0)
