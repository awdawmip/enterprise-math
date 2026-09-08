"""Validate one frozen RESULT_ONLY registration without importing mathematics."""

from __future__ import annotations

import argparse
import copy
import hashlib
import importlib.util
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path


METHOD = "result.pp.finite_power_moment_lift_obstruction"
SHARD = "research_method_inventory_addenda/20260908_owner_pp_moment_result.json"
BASE = "8fe9ae93105c06b1671f971c1f049c1dfa3879d9"
EXPECTED_METHOD_HASH = "5ede9aa0a7b00141789d7da7e0e073ab1541a8551a86df18d64bf17a102f86a8"
EXPECTED_RAW_METHOD_HASH = "2400a224de546fdd0e143a17a06eff122c6a0e7efc2ba4900c910bdd5613501b"
SOURCE_PINS = {
    "research_notes/OWNER_PP_FINITE_MOMENT_CORRECTION_20260907.md": "804d85f5fc34cda940b41b917a684595bd2037e67726e501debbbc494e42a530",
    "research_notes/OWNER_PP_FINITE_MOMENT_INDEPENDENT_AUDIT_20260907.md": "469a388a971adb20e2ef11dcfce02b0fd6314487dbe0cc7cf7332b8054b9cd81",
    "experiments/owner_pp_finite_moment_audit_20260907.py": "3497b9093612a90c69db13f67f7cba3896c7ed4d626c8ebf4ff6699cdce30b00",
    "experiments/owner_pp_finite_moment_audit_20260907.json": "c4722335bee9797064f60a70f8aebd6c8998998ae418cdd0701653ca92d4bd98",
}
LEGACY_PINS = {
    "research_checks/PERFECT_PRIME_AP_RESIDUAL_MOBIUS_BERNSTEIN_COEFFICIENT_POSITIVITY_CHECK_20260903.py": "05f75c3ae61b76ce8194df9a9d6305b1d5615f206fc0647f336e4f2ca0a412f9",
    "research_returns/PERFECT_PRIME_AP_RESIDUAL_MOBIUS_BERNSTEIN_COEFFICIENT_POSITIVITY_RETURN_20260903.md": "617b34abac20d524023933a09777b85aa4220e1962283586c1c2121d3031b28d",
}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def object_hash(value):
    return sha(json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode())


def read_pins(root, pins):
    data = {}
    for relative, expected in pins.items():
        value = root.joinpath(relative).read_bytes()
        require(sha(value) == expected, "source bytes do not match pin: " + relative)
        data[relative] = value
    return data


def validate(root, document=None):
    shard_data = root.joinpath(SHARD).read_bytes()
    actual = json.loads(shard_data)
    shard = actual if document is None else document
    require(shard["schema"] == "ENTERPRISE_MATH_RESEARCH_METHOD_INVENTORY_ADDENDUM_V1", "schema")
    require(shard["status"] == "TOOLBOX_INTEGRATION_CANDIDATE", "candidate status")
    rows = shard["methods"]
    require(len(rows) == 1 and rows[0]["method_id"] == METHOD, "one exact result ID")
    method = rows[0]
    require(method["classification"] == "RESULT_ONLY" and method["family_id"] is None, "RESULT_ONLY family boundary")
    require(method["api"] == [], "RESULT_ONLY API must be empty")
    require(object_hash(method) == EXPECTED_METHOD_HASH, "original method object changed")
    text = shard_data.decode("utf-8")
    start = text.index("[", text.index('"methods"')) + 1
    while text[start].isspace():
        start += 1
    _, end = json.JSONDecoder().raw_decode(text, start)
    require(sha(text[start:end].encode()) == EXPECTED_RAW_METHOD_HASH, "original method object bytes changed")
    provenance = shard["provenance"]
    require(provenance["source_commit"] == "b506f92a117ec4f2e9b9b1a792fddb349a74b24d", "source commit")
    require(provenance["integration_base_main"] == BASE, "declared preparation base")
    require(provenance["formal_acceptance"] is None and provenance["official_claim"] is None, "no formal authority")
    require(provenance["foundation_mutation"] is False and provenance["new_global_family"] is False, "no Foundation/family mutation")
    require(shard["historical_evidence"]["source_pins"] == SOURCE_PINS, "source pin manifest changed")
    require(shard["existing_main_dependencies"] == LEGACY_PINS, "legacy dependency pins changed")
    source_data = read_pins(root, SOURCE_PINS)
    read_pins(root, LEGACY_PINS)
    for relative, expected in method["source_sha256"].items():
        require(sha(source_data[relative]) == expected, "method source pin")
    history = shard["historical_evidence"]
    require(history["classification"] == "FROZEN_CLASSICAL_EXACT_RATIONAL_EVIDENCE", "historical evidence type")
    require(history["native_runtime_certified"] is False and history["reexecute_during_metadata_validation"] is False, "no native or execution claim")
    require(history["serialized_positive_beta_values"] == 7 and history["serialized_individual_difference_cells"] == 0, "seven beta versus 28 cells")
    frozen = json.loads(source_data["experiments/owner_pp_finite_moment_audit_20260907.json"])
    require(frozen["status"] == "PASS" and frozen["arithmetic"] == "Python standard-library fractions.Fraction; no floating point", "historical receipt identity")
    require(frozen["provenance"]["audit_source_sha256"] == SOURCE_PINS["experiments/owner_pp_finite_moment_audit_20260907.py"], "historical script binding")
    require(frozen["provenance"]["legacy_check_sha256"] == next(iter(LEGACY_PINS.values())), "historical legacy checker binding")
    require(len(frozen["finite_branch_repair"]["beta"]) == 7, "historical beta count")
    require(frozen["positive_power_moment_obstruction"]["normalized_L_h_p_squared"] == "-7205915063/2893645755000", "historical witness identity")
    require(shard["consumer_boundary"]["included_or_promoted"] is False, "consumer must remain source-only")
    protected_pins = shard["protected_main_inventory_files"]
    protected_data = read_pins(root, protected_pins)
    old_rows = [row for data in protected_data.values() for row in json.loads(data)["methods"]]
    require(len({row["method_id"] for row in old_rows}) == len(old_rows), "baseline inventory duplicate")
    require(METHOD not in {row["method_id"] for row in old_rows}, "result already in protected baseline")
    read_pins(root, shard["metadata_dependency_pins"])
    loader_path = root.joinpath("tools/enterprise_toolbox.py")
    spec = importlib.util.spec_from_file_location("pp_result_metadata_toolbox", loader_path)
    toolbox = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(toolbox)
    inventory = toolbox.load_method_inventory()
    expected_rows = {row["method_id"]: row for row in [*old_rows, method]}
    loaded_rows = {row["method_id"]: row for row in inventory["methods"]}
    require(loaded_rows == expected_rows and len(inventory["methods"]) == len(expected_rows), "canonical inventory changed beyond this one result")
    queries = []
    for query in (method["triggers"][0], METHOD + " " + method["triggers"][-1]):
        hits = toolbox.method_suggestions(query, inventory=inventory)
        require(METHOD in {row["method_id"] for row in hits}, "canonical exact query miss")
        queries.append({"query": query, "target_hit": True})
    registry = json.loads(root.joinpath("enterprise_toolbox_registry.json").read_bytes())
    family = "T1_SCALE_ENUMERATION_VALUATION"
    require(len([row for row in registry["tools"] if row["id"] == family]) == 1, "existing T1 family missing or duplicated")
    require(family in {row["id"] for row in toolbox.tool_suggestions(family + " finite differences", registry=registry)}, "T1 context lookup miss")
    require(method["reuse_resolution"]["reuse_resolution_state"] == "NOT_APPLICABLE", "do not convert T1 context into claimed execution")
    require(not any(name == "fractions" or name.startswith("enterprise_math") or name.startswith("legacy_pp") for name in sys.modules), "mathematics module was imported")
    return {
        "status": "PASS_METADATA_ONLY_NO_NATIVE_RUNTIME_CERTIFICATION",
        "source_files": SOURCE_PINS, "legacy_files": LEGACY_PINS,
        "protected_inventory_files": protected_pins,
        "protected_old_method_objects": len(old_rows), "current_method_objects": len(inventory["methods"]),
        "source_method_object_sha256": EXPECTED_METHOD_HASH, "source_raw_method_object_sha256": EXPECTED_RAW_METHOD_HASH,
        "queries": queries, "T1_coverage": "EXISTING_FAMILY_CONTEXT_ONLY; original NOT_APPLICABLE unchanged",
        "historical_receipt_reexecuted": False, "historical_receipt_native_certified": False,
        "serialized_positive_beta_values": 7, "individual_28_cell_table_present": False,
        "math_modules_imported": False, "formal_acceptance": None,
    }


def rejection_checks(root):
    original = json.loads(root.joinpath(SHARD).read_bytes())
    result = []
    bad_pin = copy.deepcopy(original)
    bad_pin["historical_evidence"]["source_pins"][next(iter(SOURCE_PINS))] = "0" * 64
    bad_api = copy.deepcopy(original)
    bad_api["methods"][0]["api"] = ["run"]
    for label, document, expected in (
        ("forged_source_pin", bad_pin, "source pin manifest changed"),
        ("forbidden_result_api", bad_api, "RESULT_ONLY API must be empty"),
    ):
        try:
            validate(root, document)
        except ValueError as error:
            require(str(error) == expected, "unexpected rejection signature")
            result.append({"case": label, "status": "REJECTED_AS_REQUIRED", "message": str(error)})
        else:
            raise AssertionError("invalid metadata was accepted: " + label)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    root = args.root.resolve()
    require(not args.output.exists(), "refusing to overwrite an existing receipt")
    result = validate(root)
    result["rejection_checks"] = rejection_checks(root)
    result["executed_utc"] = datetime.now(timezone.utc).isoformat()
    result["argv"] = [sys.executable, "-B", "-X", "utf8", str(Path(__file__).resolve()), "--root", str(root), "--output", str(args.output)]
    result["actual_git_HEAD"] = subprocess.check_output(["git", "-C", str(root), "rev-parse", "HEAD"], text=True).strip()
    result["input_state"] = "Seven additive uncommitted input files over the declared base; HEAD alone does not contain the new payload."
    inputs = [*SOURCE_PINS, SHARD, "experiments/20260908_owner_pp_moment_result/validator.py", "experiments/20260908_owner_pp_moment_result/ADMISSION.md"]
    result["actual_input_sha256"] = {path: sha(root.joinpath(path).read_bytes()) for path in inputs}
    result["global_knowledge_sync"] = "main@a624e4d / GLOBAL_KNOWLEDGE_V1"
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps({"status": result["status"], "old_objects": result["protected_old_method_objects"],
                      "new_objects": result["current_method_objects"], "queries": len(result["queries"]),
                      "rejections": len(result["rejection_checks"]), "receipt_sha256": sha(args.output.read_bytes())}))


if __name__ == "__main__":
    main()
