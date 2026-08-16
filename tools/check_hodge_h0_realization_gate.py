#!/usr/bin/env python3
from pathlib import Path
import json, sys, hashlib

ROOT = Path(__file__).resolve().parents[1]
R = ROOT / "research_results"

required = [
"HODGE_H0_CLASSICAL_TARGET_TYPE_PROTOCOL.json",
"HODGE_H0_REALIZATION_CANDIDATE_REGISTRY.json",
"HODGE_H0_REALIZATION_NONTRIVIALITY_CLASSIFICATION.json",
"HODGE_H0_NONFACTORIZATION_WITNESS_REGISTRY.json",
"HODGE_H0_PRESENTATION_AUTOMORPHISM_GATE.json",
"HODGE_H0_FUNCTORIALITY_TOY_REGISTRY.json",
"HODGE_H0_TARGET_LEAKAGE_LEDGER.json",
"HODGE_H0_H1_ENTRY_CONTRACT.json",
"HODGE_H0_CLAIM_LEDGER.json",
"HODGE_H0_COMPUTATION_REGISTRY.json",
]
errors = []
if not (R/"HODGE_H0_LITERATURE_PRIOR_ART_MATRIX.md").exists():
    errors.append("MISSING:HODGE_H0_LITERATURE_PRIOR_ART_MATRIX.md")
for name in required:
    if not (R/name).exists():
        errors.append(f"MISSING:{name}")

def load(name):
    return json.loads((R/name).read_text())

if not errors:
    t=load(required[0]); c=load(required[1]); d=load(required[2]); w=load(required[3])
    p=load(required[4]); f=load(required[5]); l=load(required[6]); h=load(required[7]); cl=load(required[8]); comp=load(required[9])

    if t["classical_target"].get("coefficients") != "Q":
        errors.append("TARGET_NOT_RATIONAL")
    if t["classical_target"].get("integral_generalization_is_target"):
        errors.append("INTEGRAL_HODGE_MISSTATED")
    if not t.get("hx_types") or not t.get("native_semantics_types"):
        errors.append("MISSING_TYPE_ASSIGNMENTS")
    if cl.get("universal_hodge_proved"):
        errors.append("FINITE_OR_STAGE_RESULT_PROMOTED_TO_GENERAL_HODGE")
    if comp.get("finite_computation_proves_general_hodge"):
        errors.append("FINITE_COMPUTATION_PROMOTED_TO_GENERAL_HODGE")

    ent = c.get("candidate_families", [])
    r2 = [x for x in ent if x.get("strongest_r_class","").startswith(("R2_","R3_")) and x.get("counts_toward_h0_r2")]
    if r2 and not w.get("enterprise_r2_witness",{}).get("required_same_classical_image_witness_produced"):
        errors.append("R2_WITHOUT_NONFACTORIZATION_WITNESS")
    for x in ent:
        if not x.get("source_types") or not x.get("enterprise_types"):
            errors.append("CANDIDATE_MISSING_TYPES:"+x.get("id","?"))

    # Color-only negative control must be rejected as R1.
    colors=[x for x in c.get("negative_controls",[]) if x.get("id")=="NEG-R1-COLOR"]
    if not colors or colors[0].get("expected_class")!="R1_REDUNDANT_ENRICHMENT":
        errors.append("ARBITRARY_COLOR_NOT_REJECTED")

    if d.get("r2_enterprise_candidate_exists") != bool(r2):
        errors.append("R2_CLASSIFICATION_MISMATCH")
    if d.get("h0_disposition")=="H0_PASS_NONTRIVIAL_ENTERPRISE_REALIZATION":
        if not r2:
            errors.append("H0_PASS_WITHOUT_ENTERPRISE_R2")
        if not p.get("enterprise_r2_presentation_gate_passed") or not p.get("enterprise_r2_automorphism_gate_passed"):
            errors.append("H0_PASS_WITHOUT_PRESENTATION_AUTOMORPHISM")
        if not f.get("enterprise_candidate_with_exact_identity_composition_and_nontrivial_morphism_at_r2_level"):
            errors.append("H0_PASS_WITHOUT_FUNCTORIALITY")
        if l.get("target_leakage_gate")!="PASS":
            errors.append("H0_PASS_WITH_TARGET_LEAKAGE")
        if not h.get("h1_admissible"):
            errors.append("H0_PASS_WITHOUT_H1_ENTRY")
    else:
        if h.get("h1_admissible"):
            errors.append("H1_ADMISSIBLE_AFTER_FAILED_H0")
        if d.get("automatic_h1_started"):
            errors.append("AUTOMATIC_H1_STARTED")

    forbidden = [e for e in l.get("entries",[]) if e.get("used_as_generator") is True]
    if forbidden:
        errors.append("FORBIDDEN_TARGET_GENERATOR_USED")
    if not t.get("startup_packet_discrepancy"):
        errors.append("STARTUP_DISCREPANCY_NOT_RECORDED")

status = "PASS" if not errors else "FAIL"
payload = {
    "checker":"HODGE_H0_REALIZATION_GATE_V1",
    "protocol_integrity":status,
    "h0_gate_disposition": None if errors else json.loads((R/"HODGE_H0_REALIZATION_NONTRIVIALITY_CLASSIFICATION.json").read_text())["h0_disposition"],
    "errors":errors,
    "required_json_count":len(required),
}
print(json.dumps(payload, sort_keys=True, separators=(",",":")))
sys.exit(0 if not errors else 1)
