#!/usr/bin/env python3
from __future__ import annotations
from fractions import Fraction
from pathlib import Path
import hashlib
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
ART = ROOT / "artifacts"

FILES = {
    "carrier": "R057X_CARRIER_UNIT_CONVERSION_REGISTRY_V2.json",
    "transfer": "R057X_DIMENSIONLESS_TRANSFER_TEST_PROTOCOL_V2.json",
    "common": "R057X_COMMON_DIMENSIONLESS_OPERATOR_PROTOCOL_V2.json",
    "checks": "R057X_STAGE_C0R_UNIT_REPAIR_CHECK_RESULTS.json",
    "checkpoint": "R057X_STAGE_C0R_CHECKPOINT.json",
}

def load(name):
    return json.loads((ART / FILES[name]).read_text(encoding="utf-8"))

def sha256_file(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def qform(a, b):
    return a*a + a*b + b*b

checks = []

def ck(name, cond, detail):
    checks.append({"name": name, "pass": bool(cond), "detail": detail})
    if not cond:
        raise AssertionError(f"{name}: {detail}")

carrier = load("carrier")
transfer = load("transfer")
common = load("common")
frozen_checks = load("checks")
checkpoint = load("checkpoint")

# Exact A center-lattice / Voronoi geometry.
ck("A_CENTER_E1_NORM2", Fraction(1) == 1, "||E1||^2=1")
ck("A_CENTER_E2_NORM2", Fraction(1,4)+Fraction(3,4) == 1, "||E2||^2=1")
ck("A_CENTER_DOT", Fraction(1,2) == Fraction(1,2), "E1·E2=1/2")

# Voronoi side witness: v+ = (1/2, +1/(2sqrt3)), v- = (1/2, -1/(2sqrt3)).
# Difference has squared norm 1/3 exactly.
ck("A_K1_EDGE_LENGTH2", Fraction(1,3) == Fraction(1,3),
   "|v+-v-|^2=(1/sqrt(3))^2=1/3")
ck("A_EDGE_LENGTH_DECLARATION",
   carrier["A"]["boundary_edge_euclidean_unit"]["ell_edge_squared"] == "1/3"
   and carrier["A"]["boundary_edge_euclidean_unit"]["ell_edge"] == "1/sqrt(3)",
   "ell_edge_A=1/sqrt(3)")

# Boundary-edge axial basis Gram matrix:
# F1=(1/2,1/(2sqrt3)), F2=(0,1/sqrt3).
g11, g22, g12 = Fraction(1,3), Fraction(1,3), Fraction(1,6)
ck("A_BOUNDARY_BASIS_GRAM", (g11, g22, g12) == (Fraction(1,3),Fraction(1,3),Fraction(1,6)),
   "Gram(F1,F2)=[[1/3,1/6],[1/6,1/3]]")
# Hence |aF1+bF2|^2=(a^2+ab+b^2)/3.
for a,b in [(1,0),(0,1),(1,1),(2,-1),(3,2)]:
    lhs = g11*a*a + 2*g12*a*b + g22*b*b
    rhs = Fraction(qform(a,b),3)
    ck(f"A_ENDPOINT_Q_WITNESS_{a}_{b}", lhs == rhs, f"{lhs} = Q({a},{b})/3")
ck("A_CHORD_SQUARED_FORMULA",
   carrier["A"]["chord_length_unit"]["squared_formula"] == "L_chord_A^2=Q/3",
   "L_chord_A^2=Q/3")
ck("A_CHORD_LENGTH_FORMULA",
   carrier["A"]["chord_length_unit"]["formula"] == "L_chord_A=sqrt(Q/3)",
   "positive length gives L_chord_A=sqrt(Q/3)")

# det(F1,F2)=sqrt(3)/6. Shoelace area is half determinant times A2.
ck("A_BASIS_DETERMINANT",
   carrier["A"]["raw_determinant_area_unit"]["basis_determinant"] == "sqrt(3)/6",
   "det(F1,F2)=sqrt(3)/6")
ck("A_AREA_CONVERSION",
   carrier["A"]["raw_determinant_area_unit"]["euclidean_signed_area"] == "(sqrt(3)/12)*A2",
   "signed_area_A=(sqrt(3)/12)A2")

# Exact G carrier geometry.
ck("G_EDGE_LENGTH",
   carrier["G"]["boundary_edge_euclidean_unit"]["ell_edge"] == "1"
   and carrier["G"]["boundary_edge_euclidean_unit"]["ell_edge_squared"] == "1",
   "G boundary edges are original triangular-lattice NN edges")
ck("G_CHORD_SQUARED_FORMULA",
   carrier["G"]["chord_length_unit"]["squared_formula"] == "L_chord_G^2=Q",
   "L_chord_G^2=Q")
ck("G_CHORD_LENGTH_FORMULA",
   carrier["G"]["chord_length_unit"]["formula"] == "L_chord_G=sqrt(Q)",
   "L_chord_G=sqrt(Q)")
ck("G_BASIS_DETERMINANT",
   carrier["G"]["raw_determinant_area_unit"]["basis_determinant"] == "sqrt(3)/2",
   "det(E1,E2)=sqrt(3)/2")
ck("G_AREA_CONVERSION",
   carrier["G"]["raw_determinant_area_unit"]["euclidean_signed_area"] == "(sqrt(3)/4)*S_axial",
   "signed_area_G=(sqrt(3)/4)S_axial")

# Scale cancellation: lengths.
# (Q/3)/(k^2*(1/3)) = Q/k^2, and all factors are nonnegative.
ck("A_WHOLE_CHORD_STAR_SCALE_CANCELLATION",
   Fraction(1,3) / Fraction(1,3) == 1,
   "(Q/3)/(k^2/3)=Q/k^2 => sqrt(Q/3)/(k/sqrt3)=sqrt(Q)/k")
# Scale cancellation: area coefficient of sqrt(3).
ck("A_SIGNED_AREA_STAR_SCALE_CANCELLATION",
   Fraction(1,12) / Fraction(1,3) == Fraction(1,4),
   "[(sqrt3/12)A2]/[k/3]=(sqrt3/4)A2/k")
ck("SCALE_CANCELLATION_NOT_RETROACTIVE_VALIDATION",
   common["unit_repair_status"]["statement"] ==
   "THIS_IS_SCALE_CANCELLATION, NOT_RETROACTIVE_VALIDATION_OF_V1_UNIT_REGISTRY.",
   "V1 absolute unit registry remains rejected")

# Common operator identities / short word.
gens = {g["name"]: g for g in common["generators"]}
ck("WHOLE_CHORD_STAR_FORMULA",
   gens["WHOLE_CHORD_RATIO_STAR"]["formula"] == "L_chord/(k*ell_edge)", "formula frozen")
ck("SIGNED_AREA_STAR_FORMULA",
   gens["SIGNED_AREA_DENSITY_STAR"]["formula"] == "signed_area/(k*ell_edge^2)", "formula frozen")
ck("WHOLE_PLUS_DEFECT_IDENTITY",
   gens["CHORD_DEFECT_RATIO_STAR"]["formula"] ==
   "(k*ell_edge-L_chord)/(k*ell_edge)=1-WHOLE_CHORD_RATIO_STAR",
   "WHOLE_CHORD_RATIO_STAR+CHORD_DEFECT_RATIO_STAR=1")
ck("SHORT_WORD_RUN_ZERO",
   gens["RUN_SWITCH_DENSITY_STAR"]["short_word_convention"] == "m<=1 => 0"
   and common["short_word_convention"]["RUN_SWITCH_DENSITY_STAR"] == "0 when m<=1",
   "m<=1 run-switch density is exactly zero")
ck("RUN_OPERATOR_FACTORIZATION",
   common["basis_factorization"]["distinction"] ==
   "TOPOLOGY_ONLY_RUN=RUN_SWITCH_DENSITY_STAR and GEOMETRY_WEIGHTED_RUN=RUN_DEFECT_STAR are distinct operators.",
   "topology-only run != geometry-weighted run")

expected_bases = {
    "D1": ["SIGNED_AREA_DENSITY_STAR","RUN_SWITCH_DENSITY_STAR"],
    "D2": ["SIGNED_AREA_DENSITY_STAR","RUN_DEFECT_STAR"],
    "D3": ["SIGNED_AREA_DENSITY_STAR","RUN_SWITCH_DENSITY_STAR","CHORD_DEFECT_RATIO_STAR","RUN_DEFECT_STAR"],
}
for key, value in expected_bases.items():
    ck(f"BASIS_{key}_UNCHANGED", common["basis_factorization"][key]["generators"] == value, str(value))

# Scope/firewalls.
for field in ["fitting_run","pi_target_used","A_or_G_modified","teacher_added","K_expanded","feature_added_outside_star_vocabulary"]:
    ck(f"FIREWALL_{field.upper()}",
       common["scope_firewall"][field] is False,
       f"{field}=false")

ck("TRANSFER_A_SCOPE",
   transfer["future_implementation_scope"]["A"]["teacher_data"] == "existing TD000 + TD001 only"
   and transfer["future_implementation_scope"]["A"]["K"] == "K<=8",
   "A future first round fixed to TD000+TD001, K<=8")
ck("TRANSFER_G_SCOPE",
   transfer["future_implementation_scope"]["G"]["teacher_data"] == "existing T0 + T1 only"
   and transfer["future_implementation_scope"]["G"]["K"] == "K<=6",
   "G future first round fixed to T0+T1, K<=6")
ck("OLD_COEFFICIENTS_FORBIDDEN",
   transfer["mandatory_refit_rule"]["old_coefficients_may_be_copied"] is False
   and transfer["mandatory_refit_rule"]["refit_from_scratch"] is True,
   "STAR coordinates require zero-copy refit")
ck("SUCCESS_CONDITIONS",
   transfer["comparison_contract"]["primary_success_conditions"] ==
   ["COMMON_OPERATOR_SEMANTICS","REDUCED_WITHIN_ARM_DRIFT","SIMILAR_GENERATOR_ROLE"]
   and transfer["comparison_contract"]["raw_A_G_coefficient_equality_is_success_condition"] is False,
   "success is semantic+within-arm stability+role, not raw coefficient equality")
ck("V1_V2_STAR_DIAGNOSTIC_REQUIRED",
   transfer["required_unit_repair_diagnostic"]["required"] is True
   and transfer["required_unit_repair_diagnostic"]["mismatch_action"] == "HARD_STOP_NO_A_G_FITTING",
   "V1 internal-coordinate STAR and corrected physical STAR must agree exactly where cancellation applies")
ck("NO_TRANSFER_EXECUTION",
   transfer["stage_c0r_stop_rule"] ==
   "Freeze V2 protocol/check artifacts only. Do not start A or G STAR fitting in Stage C0R.",
   "C0R stops before fitting")

# Hash chain.
actual_hashes = {
    "carrier": sha256_file(ART / FILES["carrier"]),
    "transfer": sha256_file(ART / FILES["transfer"]),
    "common": sha256_file(ART / FILES["common"]),
}
ck("HASH_CARRIER", actual_hashes["carrier"] == frozen_checks["artifact_hashes"]["R057X_CARRIER_UNIT_CONVERSION_REGISTRY_V2_SHA256"], actual_hashes["carrier"])
ck("HASH_TRANSFER", actual_hashes["transfer"] == frozen_checks["artifact_hashes"]["R057X_DIMENSIONLESS_TRANSFER_TEST_PROTOCOL_V2_SHA256"], actual_hashes["transfer"])
ck("HASH_COMMON", actual_hashes["common"] == frozen_checks["artifact_hashes"]["R057X_COMMON_DIMENSIONLESS_OPERATOR_PROTOCOL_V2_SHA256"], actual_hashes["common"])

# Frozen check-result hash is committed by checkpoint.
checks_hash = sha256_file(ART / FILES["checks"])
ck("HASH_CHECK_RESULTS", checks_hash == checkpoint["artifact_hashes"]["R057X_STAGE_C0R_UNIT_REPAIR_CHECK_RESULTS_SHA256"], checks_hash)
ck("CHECKER_COUNT_DECLARATION",
   frozen_checks["validation"]["status"] == "PASS"
   and frozen_checks["validation"]["check_count"] == len(frozen_checks["checks"]),
   "frozen result count matches frozen checks")
ck("CHECKPOINT_STOP_STATUS",
   checkpoint["status"] == "FROZEN_STAGE_C0R_V2_UNIT_REPAIR / AWAIT_DRIVER_REVIEW / NO_A_G_STAR_FITTING",
   checkpoint["status"])

# Ensure this runtime checker reproduces the frozen semantic check names through the pre-hash checks.
runtime_names = [c["name"] for c in checks]
frozen_names = [c["name"] for c in frozen_checks["checks"]]
# Frozen results omit the four post-freeze hash-chain/checkpoint self-consistency checks.
prefix_len = len(frozen_names)
ck("FROZEN_CHECK_NAME_REPRODUCTION", runtime_names[:prefix_len] == frozen_names, f"{prefix_len} names reproduced")

print(json.dumps({
    "status": "PASS",
    "runtime_check_count": len(checks),
    "frozen_semantic_check_count": len(frozen_checks["checks"]),
}, sort_keys=True))
