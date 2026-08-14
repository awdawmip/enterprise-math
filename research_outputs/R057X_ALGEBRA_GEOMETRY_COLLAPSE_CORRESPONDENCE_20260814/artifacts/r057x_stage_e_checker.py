#!/usr/bin/env python3
import hashlib, json, pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parent
EXPECTED = {
  "R057X_STAGE_E_INPUT_REGISTRY.json": "dd483e56c308f0192b101e94a12aa4d3346238fbf65c8304c9c57eb7f821871f",
  "R057X_COMMON_SCALE_PAIR_REGISTRY.json": "4a5295e142a53d361dd867ba28226f4c953e0276852e278750b54147fb29957d",
  "R057X_NUISANCE_LIGHT_STRATA_REGISTRY.json": "9bf75f66620a9a49cb867cb2242f83a0ac30083908f90b4ad02774d184b457de",
  "R057X_FINITE_SCALE_NUISANCE_ISOLATION.json": "e78d09bf9eaeeeec155b669b63c91945df86336deb11cc6f7797c8e668fb8d63",
  "R057X_MATCHED_MOTIF_RESIDUAL_ENRICHMENT.json": "24c593f0222697c9949d208a2febb80f017fdfb4bb5c76cd937c8bc6f5322ce8",
  "R057X_NUISANCE_LIGHT_RESIDUAL_GEOMETRY.json": "6f1a8e46046058c0f15bd5ac67a11d8fda35178fe2528e8871caf3de078d24af",
  "R057X_COMMON_RESIDUAL_COMPONENT_VERDICT.json": "b30b407282ff00bdd205515780fa093c97540691709bcfa00a4fe9312ec306d8",
  "R057X_STAGE_E_EXACT_CHECK_RESULTS.json": "64a53dcfe714e10251c7dd2a1c6ce946095129b6190772d6824efaaaf5bc7971",
  "R057X_STAGE_E_COMMON_COMPONENT_CHECKPOINT.json": "3937572b2f8099f9ce125a86ccf90ec9aad6f9470b0af9ec4b8026df67796385",
}

def load(name):
    return json.loads((ROOT/name).read_text(encoding="utf-8"))

checks=[]
def ck(name, cond):
    checks.append((name, bool(cond)))

for name, h in EXPECTED.items():
    ck("sha256:"+name, hashlib.sha256((ROOT/name).read_bytes()).hexdigest() == h)

inp=load("R057X_STAGE_E_INPUT_REGISTRY.json")
scale=load("R057X_COMMON_SCALE_PAIR_REGISTRY.json")
nuis=load("R057X_NUISANCE_LIGHT_STRATA_REGISTRY.json")
fin=load("R057X_FINITE_SCALE_NUISANCE_ISOLATION.json")
motif=load("R057X_MATCHED_MOTIF_RESIDUAL_ENRICHMENT.json")
geom=load("R057X_NUISANCE_LIGHT_RESIDUAL_GEOMETRY.json")
ver=load("R057X_COMMON_RESIDUAL_COMPONENT_VERDICT.json")
res=load("R057X_STAGE_E_EXACT_CHECK_RESULTS.json")
cp=load("R057X_STAGE_E_COMMON_COMPONENT_CHECKPOINT.json")

ck("input_gate", inp["gate_result"]=="PASS")
ck("stage_d_anchor", inp["frozen_checkpoints"]["R057X_STAGE_D_RESIDUAL_STRUCTURE_CHECKPOINT_SHA256"]=="7059ec68f6ace7cb46360476b7378b12b06dbb5a426269c20ae598e6bde1e771")
ck("scale_pairs_8", len(scale["tolerance_pairs"])==8)
ck("scale_no_fit", scale["pairing_rule"]["fitted_rescaling"] is False)
ck("G_early_unmatched", scale["unmatched_scale_regions"]["G_early_no_A_partner"]==[7,11,17,29])
ck("A_late_unmatched", scale["unmatched_scale_regions"]["A_late_no_G_partner"]==[160,224,320,448,640])
ck("nuisance_residual_blind", nuis["selection_contract"]["residual_blind"] is True)
ck("G_strict_transitions", nuis["G"]["strict_nuisance_light_transitions"]==["71->113","113->181"])
ck("A_strict_unavailable", nuis["A"]["strict_rank_stratum_status"].startswith("NOT_INSTANTIABLE"))
ck("finite_insufficient", fin["cross_arm_classification"]=="INSUFFICIENT")
ck("motif_62", len(motif["motif_semantic_catalog"])==62)
ck("motif_no_false_negative", motif["motif_classifications"]==[] and motif["lane_disposition"]=="INSUFFICIENT")
ck("geometry_insufficient", geom["primary_status"]=="INSUFFICIENT")
ck("verdict_insufficient", ver["primary_disposition"]=="INSUFFICIENT")
ck("semantic_checks_71", res["check_count"]==71 and res["pass_count"]==71 and res["failure_count"]==0)
ck("checkpoint_insufficient", cp["primary_disposition"]=="INSUFFICIENT")
ck("no_R057Y", all(x.get("R057Y_read") is False for x in [ver["prohibitions_verified"], cp["prohibitions_verified"]]))
ck("no_refit", ver["prohibitions_verified"]["coefficient_refit"] is False and cp["prohibitions_verified"]["coefficient_refit"] is False)

failed=[n for n,v in checks if not v]
print(json.dumps({"status":"PASS" if not failed else "FAIL","pass_count":sum(v for _,v in checks),"check_count":len(checks),"failures":failed}, sort_keys=True))
sys.exit(1 if failed else 0)
