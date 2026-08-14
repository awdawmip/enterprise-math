#!/usr/bin/env python3
import hashlib, json, pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parents[1] / "research_outputs" / "R057X_ALGEBRA_GEOMETRY_COLLAPSE_CORRESPONDENCE_20260814" / "artifacts"
FILES = {
    "integrity": ("R057X_STAGE_C1_INPUT_INTEGRITY.json", "1b7419705ccdd67a74400dee444a93ae23e5a29fcfe9d3a9a03d21777490768b"),
    "matrix": ("R057X_STAR_COORDINATE_COMPARISON.json", "5c9e85a4eff73157a2a71fae0c41d0f00927e8be9a74b7b2ac7b28cb96945895"),
    "verdict": ("R057X_COMMON_FACTORIZATION_VERDICT.json", "e3b7e3291111ef3e0ae8fdd448a72c573489ba3f18567a797dfe0e9a16f7305d"),
    "checks": ("R057X_STAGE_C1_CHECK_RESULTS.json", "f316c63b407d35c0743efa87853f1bedf64305fc4c389509f9f8d9544c8823cf"),
    "checkpoint": ("R057X_STAGE_C1_STAR_COMPARISON_CHECKPOINT.json", "1af2df3eefbb1eeee35418d59edf197657d91c1e14c47e8fdf319aab00a9c75d"),
}
def h(p): return hashlib.sha256(p.read_bytes()).hexdigest()
obj = {}
fail = []
for key,(name,want) in FILES.items():
    p=ROOT/name
    if not p.exists(): fail.append(f"missing:{name}"); continue
    got=h(p)
    if got != want: fail.append(f"sha:{name}:{got}")
    obj[key]=json.loads(p.read_text("utf-8"))
if not fail:
    i=obj["integrity"]; m=obj["matrix"]; v=obj["verdict"]; c=obj["checks"]; q=obj["checkpoint"]
    assertions = [
        i["A"]["unit_gate"]["status"]=="PASS" and i["A"]["unit_gate"]["failure_count"]==0,
        i["G"]["unit_gate"]["status"]=="PASS_PERSISTED_BEFORE_FITTING",
        i["A"]["coefficients_refit_from_zero"] and i["G"]["coefficients_refit_from_zero"],
        not i["A"]["legacy_coefficient_copy"] and not i["G"]["legacy_coefficient_copy"],
        not i["cross_arm_firewall"]["new_fitting_in_C1"],
        m["bases"]["D2"]["cross_arm_status"]=="CROSS_ARM_COMPACT_STAR_CANDIDATE",
        m["bases"]["D3"]["cross_arm_status"]=="D3_COMMON_STABLE_BASIS_REJECTED",
        v["primary_verdict"]["normalization"]=="CROSS_ARM_STAR_NORMALIZATION_INSUFFICIENT",
        v["status_separation"]["theorem_status"].startswith("NONE"),
        c["status"]=="PASS" and c["failure_count"]==0 and c["check_count"]==35,
        q["epistemic"]["fit_status"]=="NO_C1_FIT / CONSUMES_FROZEN_ARM_FITS",
    ]
    fail.extend(f"assert:{n+1}" for n,x in enumerate(assertions) if not x)
if fail:
    print("R057X_STAGE_C1_CHECK FAIL", *fail, sep="\n")
    sys.exit(1)
print("R057X_STAGE_C1_CHECK PASS 46/46")
