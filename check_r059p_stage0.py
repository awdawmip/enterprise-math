#!/usr/bin/env python3
from __future__ import annotations
import copy
import hashlib
import json
import sys
from pathlib import Path

FILES = {
    "path": "R059P_PATH_SPECTRUM_PROTOCOL.json",
    "pair": "R059P_PAIR_COUPLING_MODEL_REGISTRY.json",
    "dynamic": "R059P_DYNAMIC_UPDATE_MODEL_REGISTRY.json",
    "firewall": "R059P_SEMANTIC_FIREWALL.json",
    "computation": "R059P_COMPUTATION_REGISTRY.json",
}

def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    h.update(path.read_bytes())
    return h.hexdigest()

def load_bundle(root: Path):
    return {k: json.loads((root / v).read_text(encoding="utf-8")) for k, v in FILES.items()}

def validate(bundle):
    errors = []
    path = bundle["path"]
    pair = bundle["pair"]
    dyn = bundle["dynamic"]
    fw = bundle["firewall"]
    comp = bundle["computation"]

    if path["semantic_typing"].get("path_count_is_geometric_length") is not False:
        errors.append("PATH_COUNT_CALLED_LENGTH")
    if path["semantic_typing"].get("shortest_path_only") is not False:
        errors.append("SHORTEST_PATH_ONLY_SPECTRUM")
    if pair["forbidden_premises"].get("euclidean_distance") is not False:
        errors.append("EUCLIDEAN_DISTANCE_PAIR_PREMISE")
    forbidden_n0 = {"ATOM", "ATTRACTION", "PHYSICAL_ENERGY", "ZERO_POINT_MOTION"}
    promoted = set(fw.get("declared_n0_promotions", []))
    if forbidden_n0 & promoted:
        errors.append("PHYSICAL_TARGET_PROMOTED_TO_N0")
    if fw.get("r059l_consumed") is not False:
        errors.append("R059L_ARTIFACT_CONSUMPTION")
    if path["independent_lane_firewall"].get("consumed_r059l_artifacts"):
        errors.append("R059L_ARTIFACT_CONSUMPTION")
    if fw.get("zero_point_motion_status") != "FUTURE_CALIBRATION_TARGET_NOT_EXPLAINED":
        errors.append("ZERO_POINT_MOTION_ASSUMED_EXPLAINED")
    if dyn.get("strict_descent_cycle_claim") is not False:
        errors.append("STRICT_DESCENT_CYCLE_ASSERTED")
    m0 = next((m for m in dyn["models"] if m["model_id"] == "M0_SYMMETRIC_STATE_ONLY_STRICT_DESCENT"), None)
    if not m0:
        errors.append("M0_MISSING")
    else:
        if m0.get("acceptance") != "E(S') < E(S)":
            errors.append("M0_STRICT_DESCENT_SEMANTICS_CHANGED")
        if m0.get("persistent_cycle_asserted") is not False:
            errors.append("STRICT_DESCENT_CYCLE_ASSERTED")
    if comp["stage0"].get("regression_or_fitting_permitted") is not False:
        errors.append("STAGE0_FITTING_ENABLED")
    if path["declared_n0"].get("path_semantics") != "ADJACENCY_WALK":
        errors.append("PATH_NOT_ADJACENCY_WALK")
    for flag in ("revisit_allowed", "loop_allowed", "immediate_reversal_allowed", "adjacency_reuse_allowed"):
        if path["declared_n0"].get(flag) is not True:
            errors.append("NATIVE_WALK_RESTRICTION_" + flag.upper())
    return sorted(set(errors))

def negative_tests(bundle):
    cases = []

    def run_case(name, mutate, expected):
        b = copy.deepcopy(bundle)
        mutate(b)
        errors = validate(b)
        cases.append({
            "case": name,
            "expected_rejection": expected,
            "errors": errors,
            "rejected": expected in errors,
        })

    run_case(
        "path_count_called_length",
        lambda b: b["path"]["semantic_typing"].__setitem__("path_count_is_geometric_length", True),
        "PATH_COUNT_CALLED_LENGTH",
    )
    run_case(
        "shortest_path_only_spectrum",
        lambda b: b["path"]["semantic_typing"].__setitem__("shortest_path_only", True),
        "SHORTEST_PATH_ONLY_SPECTRUM",
    )
    run_case(
        "euclidean_distance_pair_premise",
        lambda b: b["pair"]["forbidden_premises"].__setitem__("euclidean_distance", True),
        "EUCLIDEAN_DISTANCE_PAIR_PREMISE",
    )
    run_case(
        "physical_target_promoted_to_n0",
        lambda b: b["firewall"].__setitem__("declared_n0_promotions", ["ATOM", "PHYSICAL_ENERGY"]),
        "PHYSICAL_TARGET_PROMOTED_TO_N0",
    )
    def consume_r059l(b):
        b["firewall"]["r059l_consumed"] = True
        b["path"]["independent_lane_firewall"]["consumed_r059l_artifacts"] = ["R059L_FORBIDDEN.json"]
    run_case(
        "r059l_artifact_consumption",
        consume_r059l,
        "R059L_ARTIFACT_CONSUMPTION",
    )
    run_case(
        "zero_point_motion_assumed_explained",
        lambda b: b["firewall"].__setitem__("zero_point_motion_status", "EXPLAINED"),
        "ZERO_POINT_MOTION_ASSUMED_EXPLAINED",
    )
    run_case(
        "strict_descent_cycle_asserted",
        lambda b: b["dynamic"].__setitem__("strict_descent_cycle_claim", True),
        "STRICT_DESCENT_CYCLE_ASSERTED",
    )
    return cases

def main():
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
    bundle = load_bundle(root)
    base_errors = validate(bundle)
    neg = negative_tests(bundle)
    output = {
        "schema": "R059P_STAGE0_CHECKER_OUTPUT_V1",
        "generation": "R059P",
        "researcher_id": "EM-R059P-8A2C7D",
        "status": "PASS" if not base_errors and all(x["rejected"] for x in neg) else "FAIL",
        "base_errors": base_errors,
        "negative_tests": neg,
        "input_sha256": {v: sha256_file(root / v) for v in FILES.values()},
    }
    print(json.dumps(output, sort_keys=True, indent=2))

if __name__ == "__main__":
    main()
