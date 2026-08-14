#!/usr/bin/env python3
"""R046 leakage / double-counting adversarial checker.

Stdlib-only. It validates the frozen artifact invariants; it does not test or
select any native pi/collapse/growth candidate.
"""
from __future__ import annotations
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent

def load(name):
    return json.loads((ROOT / name).read_text(encoding="utf-8"))

atlas = load("R046_ENGINEERING_SUCCESS_ATLAS.json")
stripped = load("R046_DEFINITION_STRIPPED_CONSTRAINTS.json")
quotient = load("R046_DEPENDENCY_QUOTIENT.json")
kernel = load("R046_MINIMAL_SUCCESS_KERNEL.json")
interface = load("R046_NATIVE_EXPLANATION_INTERFACE.json")
graph = load("R046_CLASSICAL_DEPENDENCY_GRAPH.json")
spec = load("R046_ADVERSARIAL_TEST_SPEC.json")
ledger = load("R046_NATIVE_SEMANTICS_CLAIM_LEDGER.json")

checks = []
def check(cid, cond, detail):
    checks.append({"check_id": cid, "pass": bool(cond), "detail": detail})
    if not cond:
        raise AssertionError(f"{cid}: {detail}")

required_row_fields = {
    "success_id","engineering_domain","physical_or_engineering_protocol",
    "controlled_inputs","measured_outputs","scale_regime",
    "tolerance_or_error_envelope","classical_effective_formula","where_pi_appears",
    "classical_definitions_required","unit_or_coordinate_conventions_required",
    "upstream_mathematical_dependencies","empirical_independence_from_other_rows",
    "what_survives_after_definition_stripping","status","sources"
}
rows = atlas["success_rows"]
check("ATLAS_ROW_COUNT", len(rows) == 14, f"expected 14, got {len(rows)}")
check("ATLAS_ROW_FIELDS", all(required_row_fields <= set(r) for r in rows),
      "every success row contains the taskbook-required typed fields")
check("UNIQUE_SUCCESS_IDS", len({r["success_id"] for r in rows}) == len(rows),
      "success_id values are unique")

known_sources = set(atlas["source_ids"])
used_sources = {s for r in rows for s in r["sources"]}
check("SOURCE_REFERENTIAL_INTEGRITY", used_sources <= known_sources,
      f"all row sources resolve in registry; unresolved={sorted(used_sources-known_sources)}")

counts = quotient["counts"]
check("RAW_SUCCESS_COUNT", counts["RAW_SUCCESS_COUNT"] == 14, str(counts))
check("DEFINITION_STRIPPED_COUNT", counts["DEFINITION_STRIPPED_COUNT"] == 10 == len(stripped["constraints"]),
      f"declared={counts['DEFINITION_STRIPPED_COUNT']} actual={len(stripped['constraints'])}")
check("DEPENDENCY_QUOTIENT_COUNT", counts["DEPENDENCY_QUOTIENT_COUNT"] == 5 == len(quotient["evidence_classes"]),
      f"declared={counts['DEPENDENCY_QUOTIENT_COUNT']} actual={len(quotient['evidence_classes'])}")
check("CROSS_DOMAIN_INDEPENDENT_COUNT", counts["CROSS_DOMAIN_INDEPENDENT_COUNT"] == 4 == len(kernel["members"]),
      f"declared={counts['CROSS_DOMAIN_INDEPENDENT_COUNT']} kernel={len(kernel['members'])}")

raw_sum = sum(q["raw_count"] for q in quotient["evidence_classes"])
redundant_sum = sum(q["redundant_pi_bearing_rows_under_primary_attribution"] for q in quotient["evidence_classes"])
check("QUOTIENT_RAW_PARTITION", raw_sum == 14, f"sum raw_count={raw_sum}")
check("SHARED_DEFINITION_DOUBLE_COUNT", redundant_sum == 9 == 14 - 5,
      f"sum(raw_count-1)={redundant_sum}; expected 9")

kernel_ids = {k["kernel_id"] for k in kernel["members"]}
check("KERNEL_FOUR_MEMBERS", len(kernel_ids) == 4, sorted(kernel_ids))
check("KERNEL_DELETION_WITNESSES", all(k.get("deletion_witness") for k in kernel["members"]),
      "each member states what independent pressure is lost if deleted")
check("KERNEL_SCALE_TOLERANCE", all(k.get("scale_tolerance_summary") for k in kernel["members"]),
      "each member has explicit scale/tolerance semantics")
check("NO_SCALAR_KERNEL", kernel["kernel_nature"] == "STRUCTURAL_OPERATIONAL_TARGET_SET / NOT_A_SCALAR / NOT_NATIVE_PI",
      kernel["kernel_nature"])

# Fourier/spectral convention class must not be a pi-specific kernel member.
q3 = next(q for q in quotient["evidence_classes"] if q["evidence_class_id"].startswith("Q03_"))
check("FOURIER_NORMALIZATION_NOT_NATIVE_CONSTANT",
      q3["kernel_eligibility"] == "NO_PI_SPECIFIC_KERNEL_MEMBER" and
      q3["evidence_class_id"] not in {q for k in kernel["members"] for q in k["from_evidence_classes"]},
      "Q03 excluded from pi-specific kernel after convention quotient")

# Gaussian normalization must be stripped while diffusion survives.
c9 = next(c for c in stripped["constraints"] if c["constraint_id"] == "C09_DIFFUSIVE_RELAXATION_SCALE")
check("GAUSSIAN_NORMALIZATION_STRIPPED",
      "Gaussian" in " ".join(c9["stripped_dependencies"]) and
      c9["pi_specific_pressure"].endswith("NOT_NORMALIZATION_CONSTANT"),
      c9["pi_specific_pressure"])

# Radian-as-physics control: target is cycle/time language, and radian is forbidden.
k2 = next(k for k in interface["constraints"] if k["constraint_id"] == "KENG-02_CYCLE_CLOSURE_AND_RELATIVE_PHASE")
check("RADIANS_AS_PHYSICS_REJECTED",
      any("radian" in x.lower() for x in k2["forbidden_imported_effective_definitions"]) and
      "radian" not in k2["required_observable_protocol"].lower(),
      "radian is forbidden as native input and absent from required observable protocol")

# Output-copying control.
forbidden_text = " ".join(interface["global_forbidden_imported_effective_definitions"]).lower()
for token in ["center","distance/equidistance","radius","circle/sphere","angle/radian","fourier","gaussian"]:
    check("FORBID_" + token.upper().replace("/","_"),
          token in forbidden_text, f"global forbidden list contains {token}")

check("NATIVE_INPUTS_UNSPECIFIED",
      all(c["allowed_native_inputs"] == "UNSPECIFIED" for c in interface["constraints"]),
      "every interface row leaves native inputs unspecified")

# No numerical pi back-selection.
payload = json.dumps({"stripped":stripped,"kernel":kernel,"interface":interface}, ensure_ascii=False)
check("ONE_NUMBER_FIT_REJECTED",
      "3.14159" not in payload and kernel["one_number_fit_policy"].startswith("REJECTED"),
      "no classical decimal target appears in the target artifacts and policy rejects one-number fitting")

# Directional graph must never point back into a native-input node (none exists).
up_types = {n["node_id"]: n["node_type"] for n in graph["nodes"]["upstream_effective_definitions_conventions_theorems"]}
check("NO_NATIVE_INPUT_NODE", all("NATIVE" not in t for t in up_types.values()),
      "dependency graph has no native-premise node")
check("NO_REVERSE_EFFECTIVE_TO_NATIVE_EDGE",
      all("native" not in e["to"].lower() for e in graph["edges"]),
      "all graph edges terminate in effective evidence/stripped/quotient/kernel nodes, never native input")

# Gate V3 ledger: no native-pi/collapse promotion.
verdicts = {c["claim_id"]: c["admissibility_verdict"] for c in ledger["claims"]}
check("GATE_V3_NO_NATIVE_PI_PROMOTION", verdicts["R046-C03"] == "UNRESOLVED",
      str(verdicts))
check("GATE_V3_NO_COLLAPSE_SELECTION", verdicts["R046-C04"] == "UNRESOLVED",
      str(verdicts))
check("TARGET_LEAKAGE_AUDIT_PASS",
      all(c["target_leakage_audit"].startswith("PASS") for c in ledger["claims"]),
      "all Gate-V3 claim-ledger rows pass target-leakage audit")

# All mandated adversarial attacks are present and expected REJECT.
expected_ids = {
"A_PI_FREQUENCY_IS_EVIDENCE",
"B_SHARED_DEFINITION_DOUBLE_COUNT",
"C_RADIANS_AS_PHYSICS",
"D_FOURIER_NORMALIZATION_AS_NATIVE_CONSTANT",
"E_GAUSSIAN_NORMALIZATION_AS_NATIVE_PI",
"F_OUTPUT_COPYING",
"G_ONE_NUMBER_FIT",
}
spec_ids = {t["test_id"] for t in spec["tests"] if t["expected"] == "REJECT"}
check("MANDATORY_ADVERSARIAL_COVERAGE", expected_ids == spec_ids,
      f"expected={sorted(expected_ids)} actual={sorted(spec_ids)}")

result = {
    "schema":"ENTERPRISE_MATH_R046_ADVERSARIAL_TEST_RESULTS_V1",
    "status":"PASS" if all(c["pass"] for c in checks) else "FAIL",
    "researcher_id":atlas["researcher_id"],
    "summary":{
        "checks_total":len(checks),
        "checks_passed":sum(c["pass"] for c in checks),
        "checks_failed":sum(not c["pass"] for c in checks),
    },
    "counts":counts,
    "checks":checks,
    "ci":"CI_NOT_REQUIRED_FOR_RESEARCH",
}
(ROOT / "R046_ADVERSARIAL_TEST_RESULTS.json").write_text(
    json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
)
print(json.dumps(result["summary"], ensure_ascii=False))
if result["status"] != "PASS":
    sys.exit(1)
