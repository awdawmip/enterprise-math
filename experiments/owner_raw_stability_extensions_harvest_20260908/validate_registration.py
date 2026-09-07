"""Validate three bounded registrations; inspect one API without executing it."""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import importlib
import inspect
import json
from pathlib import Path
import sys


SHARD = "research_method_inventory_addenda/20260908_owner_raw_stability_extensions.json"
PREFIX = "experiments/owner_positive_support_compression_20260908/"
COMPRESS = "candidate.x6.positive_support_raw_compression_certificate"
EQUALITY = "result.x6.two_positive_equality_rectangle"
MASS = "result.x6.three_positive_raw_mass_boundary"
PAPER_EQUALITY = "research_notes/OWNER_TWO_POSITIVE_EQUALITY_CLASSIFICATION_REVIEW_20260908.md"
PAPER_MASS = "research_notes/OWNER_THREE_POSITIVE_RAW_STABILITY_PROBE_20260908.md"


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def read_pinned(root, pins):
    data = {path: (root / path).read_bytes() for path in pins}
    require({path: digest(value) for path, value in data.items()} == pins, "source pin mismatch")
    return data


def validate(root):
    shard_bytes = (root / SHARD).read_bytes()
    shard = json.loads(shard_bytes)
    require(shard["schema"] == "ENTERPRISE_MATH_RESEARCH_METHOD_INVENTORY_ADDENDUM_V1", "schema")
    require(shard["status"] == "TOOLBOX_INTEGRATION_CANDIDATE", "candidate shard status")
    provenance = shard["provenance"]
    require(provenance["published_source_commit"] == "c0495fd71a557ed78eef7ab62a8b2bf08feee535", "published source")
    require(provenance["published_source_tree"] == "738656dd4d2c1f9a5d5f1175b151be7ed83f2772", "source tree")
    require(provenance["formal_driver_or_steward_acceptance"] is None
            and provenance["official_claim"] is None, "formal authority absent")
    require(provenance["foundation_mutation"] is False and provenance["new_global_tool_family"] is False,
            "no Foundation or family mutation")
    require(shard["availability"]["formal_acceptance_inferred_from_indexing"] is False, "index authority")
    rows = shard["methods"]
    require(len(rows) == 3 and {m["method_id"] for m in rows} == {COMPRESS, EQUALITY, MASS}, "three exact unique IDs")
    by_id = {row["method_id"]: row for row in rows}
    pins = {}
    for row in rows:
        require(row["family_id"] is None and row["formal_acceptance"] is None, "candidate has no formal family acceptance")
        require(row["status"] == "TOOLBOX_INTEGRATION_CANDIDATE"
                and row["owner_review_status"] == "INTERNAL_EVIDENCE_REVIEWED_FORMAL_ACCEPTANCE_ABSENT", "entry status")
        require(row["reuse_resolution"]["reuse_resolution_state"] == "EXTEND_EXISTING_TOOL", "reuse scope")
        scope = row["result_scope"]
        require(scope["post_jordan_positive_support"] is True and scope["same_anchor_labelled_signed_x6"] is True,
                "shared raw/Jordan contract")
        require(set(row["source_sha256"]) == set(row["source_refs"] + row["validation_refs"]), "exact source/evidence closure")
        for path, pin in row["source_sha256"].items():
            require(path not in pins or pins[path] == pin, "inconsistent shared pin")
            pins[path] = pin
    require(len(pins) == 9, "six-file consumer/review package and three papers")
    source_data = read_pinned(root, pins)
    comp = by_id[COMPRESS]
    require(comp["classification"] == "DOMAIN_OPERATOR" and comp["api"] == ["audit_compression"], "single public API")
    require(comp["api_binding"] == {"module_path": PREFIX + "check_positive_support_compression.py",
            "callable": "audit_compression", "signature": "(case_id, mu_atoms, nu_atoms, denominator=1)"}, "exact API binding")
    scope = comp["result_scope"]
    require(scope["generic_finite_positive_support"] is True and scope["raw_table_count_per_case"] == 20, "generic p/all20")
    for key in ("all_coordinate_subsets_executed", "carrier_enumerated", "carrier_bound_is_actual_support_count",
                "zero_ratio_defined", "arbitrary_low_level_pushforward_norm_guarantee", "recovers_microscopic_brc",
                "new_two_positive_sharp_bound_checker"):
        require(scope[key] is False, key)
    require(scope["p_zero_handled_separately"] is True and scope["retains_symbolic_div_mass_unit"] is True, "zero and DIV scope")
    for mid, paper in ((EQUALITY, PAPER_EQUALITY), (MASS, PAPER_MASS)):
        row = by_id[mid]
        require(row["classification"] == "RESULT_ONLY" and row["api"] == [] and "api_binding" not in row, "paper-only API")
        require(row["source_refs"] == row["validation_refs"] == [paper], "one actual paper source")
        require(row["result_scope"]["all_twenty_complete_raw_three_axis_norms"] is True, "all20 norm definition")
        require(row["result_scope"]["executable_theorem_certificate"] is False, "no executable paper proof")
    eq = by_id[EQUALITY]["result_scope"]
    require(eq["maximum_positive_support"] == 2 and eq["nonzero_required"] is True
            and eq["norm_equality_condition"] == "D=4*M" and eq["iff_original_coordinate_equal_weight_rectangle"] is True
            and eq["equal_total_mass_forced"] is True, "exact equality scope")
    require(all(eq[key] is False for key in ("unit_axis_spacing_required", "zero_difference_classified", "extends_to_p_ge_3")), "equality exclusions")
    mass = by_id[MASS]["result_scope"]
    require([mass[key] for key in ("example_positive_support", "example_total_support", "example_P", "example_N", "example_M", "example_D")]
            == [3, 7, 3, 4, 7, 26], "seven-point witness fields")
    require((mass["arbitrary_mass_lower_bound_numerator"], mass["arbitrary_mass_lower_bound_denominator"]) == (7, 26), "lower bound only")
    require(mass["equal_mass_bound_only_for_specified_symmetric_family"] is True
            and mass["equal_mass_family_equality"] == "c=0; 1/2<=b<=2/3; a=3-3*b; M=6; D=24", "restricted family equality")
    require(all(mass[key] is False for key in ("sharp_or_global_upper_bound_claimed", "all_equal_mass_p3_upper_bound_claimed",
                                             "arbitrary_mass_family_optimized")), "no global p3 upper bound")

    runtime = comp["runtime_dependency_manifest"]
    require(runtime == {"path": PREFIX + "certificate.json", "field": "source_sha256", "count": 14,
                        "all_transitive_arithmetic_compliance_claimed": False}, "runtime pin manifest scope")
    author = json.loads(source_data[runtime["path"]])
    runtime_pins = author[runtime["field"]]
    require(len(runtime_pins) == 14, "fourteen runtime dependencies")
    runtime_data = read_pinned(root, runtime_pins)
    independent = json.loads(source_data[PREFIX + "independent_review_20260908/review.json"])
    require(author["status"] == "PASS" and len(author["cases"]) == 18
            and sum(len(case["raw_tables"]) for case in author["cases"]) == 360, "historical author evidence")
    require(independent["status"] == "PASS_BOUNDED_CONSUMER_REVIEW_NO_FORMAL_ACCEPTANCE"
            and len(independent["independent_cases"]) == 5 and independent["independent_raw_tables"] == 100
            and len(independent["independent_rejections"]) == 3, "historical independent evidence")
    require(author["checker_sha256"] == pins[PREFIX + "check_positive_support_compression.py"]
            and independent["executed_script_sha256"] == pins[PREFIX + "independent_review_20260908/review.py"], "executed-source binding")

    prior_paths = provenance["protected_prior_shards"]
    require(prior_paths == ["research_method_inventory_addenda/20260907_owner_native_frontier_candidates.json",
                           "research_method_inventory_addenda/20260908_owner_raw_stability_results.json"], "two prior shards")
    prior_bytes = {path: (root / path).read_bytes() for path in prior_paths}
    prior_objects = {path: json.loads(data)["methods"] for path, data in prior_bytes.items()}
    sys.path.insert(0, str(root / "tools"))
    import enterprise_toolbox as toolbox
    require(Path(toolbox.__file__).resolve() == (root / "tools/enterprise_toolbox.py").resolve(), "canonical loader")
    inventory = toolbox.load_method_inventory()
    query_checks = []
    for row in rows:
        require([m for m in inventory["methods"] if m["method_id"] == row["method_id"]] == [row], "unique exact loaded row")
        require(len(row["triggers"]) == 2 and row["triggers"][0].isascii()
                and any("\u4e00" <= char <= "\u9fff" for char in row["triggers"][1]), "English and Chinese triggers")
        for language, query in zip(("en", "zh-CN"), row["triggers"]):
            hits = toolbox.method_suggestions(query, inventory=inventory)
            require(row["method_id"] in {m["method_id"] for m in hits}, "query miss")
            query_checks.append({"method_id": row["method_id"], "language": language, "query": query, "hit": True})
    for objects in prior_objects.values():
        for row in objects:
            require([m for m in inventory["methods"] if m["method_id"] == row["method_id"]] == [row], "prior object changed")

    sys.path.insert(0, str(root / PREFIX))
    module = importlib.import_module("check_positive_support_compression")
    module_path = root / comp["api_binding"]["module_path"]
    require(Path(module.__file__).resolve() == module_path.resolve(), "canonical API module")
    api = getattr(module, "audit_compression")
    require(callable(api) and inspect.isfunction(api), "real callable API")
    require(Path(api.__code__.co_filename).resolve() == module_path.resolve(), "API code origin")
    require(str(inspect.signature(api)) == comp["api_binding"]["signature"], "exact callable signature")
    require(module.SOURCE_SHA256 == runtime_pins, "effective API runtime pins")
    # Inspection ends here: audit_compression, build_certificate and old consumers are never called.
    for path, data in {**source_data, **runtime_data, **prior_bytes, SHARD: shard_bytes}.items():
        require((root / path).read_bytes() == data, "input file changed during metadata validation")
    return {
        "schema": "OWNER_RAW_STABILITY_EXTENSIONS_REGISTRATION_VALIDATION_V1",
        "status": "PASS_THREE_CANDIDATE_REGISTRATIONS",
        "created_utc": datetime.now(timezone.utc).isoformat(), "python": sys.version.split()[0], "argv": sys.argv,
        "executed_script_sha256": digest(Path(__file__).read_bytes()), "shard_sha256": digest(shard_bytes),
        "published_evidence_source_commit": provenance["published_source_commit"],
        "canonical_loader_sha256": digest(Path(toolbox.__file__).read_bytes()),
        "method_ids_unique": [row["method_id"] for row in rows], "queries": query_checks,
        "source_sha256": pins, "source_files_unchanged": True, "runtime_dependency_sha256": runtime_pins,
        "runtime_dependency_count": len(runtime_pins), "runtime_dependencies_unchanged": True,
        "api_inspection": {"method_id": COMPRESS, "module_path": comp["api_binding"]["module_path"],
                           "callable": "audit_compression", "signature": str(inspect.signature(api)),
                           "exact_code_origin": True, "mathematical_api_invocations": 0},
        "protected_previous_shards": [{"path": path, "sha256_before_and_after": digest(data),
            "observed_method_count": len(prior_objects[path]), "all_objects_and_file_bytes_unchanged": True,
            "observed_count_is_not_a_permanent_main_assertion": True} for path, data in prior_bytes.items()],
        "historical_consumer_evidence_read_not_reexecuted": True,
        "mathematical_consumers_executed": False, "formal_acceptance_or_family_created": False,
        "registration_authoring_global_knowledge_sync": "main@eb09a0a / GLOBAL_KNOWLEDGE_V1",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("repo", nargs="?", type=Path, default=Path(__file__).resolve().parents[2])
    args = parser.parse_args()
    report = validate(args.repo.resolve())
    target = Path(__file__).with_name("validation.json")
    target.write_bytes((json.dumps(report, ensure_ascii=False, indent=2) + "\n").encode("utf-8"))
    print(json.dumps({"status": report["status"], "methods": len(report["method_ids_unique"]),
        "queries": len(report["queries"]), "runtime_pins": report["runtime_dependency_count"],
        "prior_method_counts": [row["observed_method_count"] for row in report["protected_previous_shards"]]}))


if __name__ == "__main__":
    main()
