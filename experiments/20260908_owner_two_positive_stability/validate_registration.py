"""Register one published p2 executable without replaying its mathematical cases.

Read-only by default; --write stores an actual metadata/import validation receipt.
The frozen author and independent-review receipts remain historical evidence.
"""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import inspect
import json
from pathlib import Path
import sys


SHARD = "research_method_inventory_addenda/20260908_owner_two_positive_stability.json"
REPORT = "experiments/20260908_owner_two_positive_stability/validation.json"
METHOD_ID = "candidate.x6.two_positive_raw_stability_certificate"
SOURCE_COMMIT = "3ac5a5dd0e3b62f489cf1a5a1739b63b90c53b8f"
SOURCE_TREE = "7c0085e8382cf17d4dce61fbf9d3983999a09049"
BASE = "experiments/owner_two_positive_stability_20260908/"
IMPLEMENTATION = BASE + "check_two_positive_stability.py"
INPUT_PINS = BASE + "independent_review_20260908/author_input_pins.json"
FILE_PINS = {
    IMPLEMENTATION: "3fe2fa6c824b7cff1fca4ad9a3f0235fc008c2a00b152893559eed54d2f63da7",
    BASE + "certificate.json": "244e9cd7844e391b3f19cdbebaaad36fd70ddf14c97701252847ca2a50761e7e",
    BASE + "README.md": "929dedf2a8f5ac05b965406ad15eca1ecab27c05d9586fdbdf2406af2843c327",
    BASE + "independent_review_20260908/review_two_positive.py":
        "37c831a0b51dbd6cd16e9657d3f402f7903af7deaa205ce17772639b6af3b51e",
    INPUT_PINS: "57a90c8aa99f22d51cbb8bd905cf9700900ecdb4f56b081cacaf8d713841548c",
    BASE + "independent_review_20260908/README.md":
        "c01d49cd12927db32cb14a515707ebf4e4c72214caf47f2229bc7eaff9e2490a",
    BASE + "independent_review_20260908/validation.json":
        "513f65ccf2c08796adadfd2ebeafb4fd8fb4f2fb6b540d913af537a51df479ac",
}
QUERIES = [
    "two positive support raw X6 stability certificate",
    "X6 双正支点 raw 二十表 稳定性 矩形取等 证书",
]
PRIOR_REUSE_IDS = [
    "candidate.x6.one_positive_raw_stability_certificate",
    "candidate.x6.positive_support_raw_compression_certificate",
    "candidate.x6.raw_joint_observer_recovery",
    "result.x6.two_positive_raw_stability",
    "result.x6.two_positive_equality_rectangle",
]
SOURCE_ONLY_COVERAGE_REUSE_IDS = ["candidate.x6.raw_joint_observer_recovery"]
SCOPE = {
    "post_jordan_positive_support_at_most": 2,
    "positive_integer_population_numerators": True,
    "strict_positive_integer_common_denominator": True,
    "same_external_anchor_and_labelled_raw_x6_chart_required": True,
    "aggregate_then_cancel_before_support_check": True,
    "signed_difference_is_analysis_only": True,
    "complete_ordered_raw_three_axis_tables": 20,
    "joint_can3_plus_common_offset_required": True,
    "integer_bound": "D >= 4*M",
    "nonzero_equality": "original-coordinate equal-weight checkerboard rectangle",
    "literal_unreduced_unevaluated_division_expr": True,
    "zero_difference_ratio": None,
    "p_le_1_uses_existing_audit_case_only_in_its_scope": True,
    "extends_to_three_positive_support": False,
    "recovers_microscopic_branch_history": False,
    "formal_result_created": False,
    "working_truth_granted": False,
    "main_admission_inferred": False,
}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def object_digest(value):
    return digest(json.dumps(value, ensure_ascii=False, sort_keys=True,
                             separators=(",", ":")).encode("utf-8"))


def inventory_snapshot(root):
    paths = [root.joinpath("research_method_inventory.json")] + sorted(
        root.joinpath("research_method_inventory_addenda").glob("*.json")
    )
    return {path.relative_to(root).as_posix(): path.read_bytes() for path in paths}


def validate(root, catalog_context="source"):
    require(catalog_context in {"source", "main"}, "unknown catalog context")
    root = root.resolve()
    before = inventory_snapshot(root)
    require(SHARD in before, "candidate shard missing")
    shard = json.loads(before[SHARD])
    prior_bytes = {path: data for path, data in before.items() if path != SHARD}
    prior = [row for data in prior_bytes.values()
             for row in json.loads(data).get("methods", [])]
    require(all(row["method_id"] != METHOD_ID for row in prior), "duplicate method ID")
    require(all("audit_two_positive_stability" not in row.get("api", []) for row in prior),
            "the same executable API is already registered elsewhere")

    source_bytes = {path: root.joinpath(path).read_bytes() for path in FILE_PINS}
    require({path: digest(data) for path, data in source_bytes.items()} == FILE_PINS,
            "one of the seven published source files drifted")
    runtime_pins = json.loads(source_bytes[INPUT_PINS])["sources_sha256"]
    require(len(runtime_pins) == 16 and not set(runtime_pins).intersection(FILE_PINS),
            "the frozen runtime/proof dependency set changed")
    source_bytes.update({path: root.joinpath(path).read_bytes() for path in runtime_pins})
    expected_pins = {**FILE_PINS, **runtime_pins}
    require({path: digest(data) for path, data in source_bytes.items()} == expected_pins,
            "one of the sixteen runtime/proof pins drifted")
    loader = root.joinpath("tools/enterprise_toolbox.py")
    loader_bytes = loader.read_bytes()
    registry = root.joinpath("enterprise_toolbox_registry.json")
    registry_bytes = registry.read_bytes()
    script_bytes = Path(__file__).read_bytes()

    require(shard["schema"] == "ENTERPRISE_MATH_RESEARCH_METHOD_INVENTORY_ADDENDUM_V1",
            "wrong schema")
    require(shard["status"] == "TOOLBOX_INTEGRATION_CANDIDATE", "wrong shard status")
    require(shard["authority"] == "FRONTIER_ROUTING_ONLY_EXACT_SOURCES_CONTROL",
            "index authority changed")
    provenance = shard["provenance"]
    require((provenance["source_commit"], provenance["source_tree"])
            == (SOURCE_COMMIT, SOURCE_TREE), "published source provenance changed")
    for key in ("formal_driver_or_steward_acceptance", "official_claim", "formal_result"):
        require(provenance[key] is None, f"ungranted formal authority: {key}")
    for key in ("foundation_mutation", "new_global_tool_family", "working_truth_granted"):
        require(provenance[key] is False, f"ungranted authority: {key}")
    require(shard["availability"]["loader"] == "tools/enterprise_toolbox.py"
            and shard["availability"]["formal_acceptance_inferred_from_indexing"] is False,
            "canonical loading or acceptance boundary changed")
    require(len(shard["methods"]) == 1, "this unit contains exactly one candidate")
    row = shard["methods"][0]
    require(row["method_id"] == METHOD_ID, "wrong method ID")
    require((row["classification"], row["family_id"], row["api"])
            == ("DOMAIN_OPERATOR", "T0_BRC", ["audit_two_positive_stability"]),
            "classification/family/sole API changed")
    require(row["status"] == "TOOLBOX_INTEGRATION_CANDIDATE"
            and row["owner_review_status"]
            == "INTERNAL_EVIDENCE_REVIEWED_FORMAL_ACCEPTANCE_ABSENT", "status changed")
    require(row["source_refs"] == list(FILE_PINS), "seven-file source set changed")
    require(row["runtime_refs"] == sorted(runtime_pins), "runtime/proof reference set changed")
    require(row["source_sha256"] == expected_pins, "source pin registration changed")
    require(row["implementation_ref"] == IMPLEMENTATION, "API implementation changed")
    require(row["validation_refs"] == [BASE + "certificate.json",
            BASE + "independent_review_20260908/README.md",
            BASE + "independent_review_20260908/validation.json"], "evidence references changed")
    require(row["triggers"] == QUERIES, "exact bilingual queries changed")
    require(row["executable_scope"] == SCOPE, "mathematical scope metadata changed")
    require(row["reuse_resolution"]["reuse_resolution_state"] == "EXTEND_EXISTING_TOOL"
            and row["reuse_resolution"]["matched_method_ids"] == PRIOR_REUSE_IDS,
            "reuse/dedup boundary changed")

    sys.path.insert(0, str(root.joinpath("tools")))
    import enterprise_toolbox as toolbox
    require(Path(toolbox.__file__).resolve() == loader.resolve()
            and toolbox.ROOT.resolve() == root, "noncanonical inventory loader origin")
    inventory = toolbox.load_method_inventory()
    loaded = inventory["methods"]
    require([item for item in loaded if item["method_id"] == METHOD_ID] == [row],
            "candidate not loaded exactly once and unchanged")
    actual_prior = [item for item in loaded if item["method_id"] != METHOD_ID]
    require(actual_prior == prior, "prior method object/order changed")
    prior_by_id = {item["method_id"]: item for item in prior}
    missing_reuse_ids = [mid for mid in PRIOR_REUSE_IDS if mid not in prior_by_id]
    source_only_coverage_ids = SOURCE_ONLY_COVERAGE_REUSE_IDS if catalog_context == "main" else []
    unexpected_missing = [mid for mid in missing_reuse_ids if mid not in source_only_coverage_ids]
    require(not unexpected_missing, "expected reused method absent: " + ", ".join(unexpected_missing))
    family_before = [item for item in prior if item.get("family_id") == "T0_BRC"]
    require([item for item in actual_prior if item.get("family_id") == "T0_BRC"]
            == family_before, "prior BRC family changed")
    query_results = []
    for language, query in zip(("en", "zh-CN"), QUERIES):
        hits = toolbox.method_suggestions(query, inventory=inventory)
        matching = [hit for hit in hits if hit["method_id"] == METHOD_ID]
        require(len(matching) == 1, f"{language} query missed the candidate")
        query_results.append({"language": language, "query": query,
                              "matching_score": matching[0]["score"],
                              "returned_method_ids": [hit["method_id"] for hit in hits]})

    # Canonical imports only. Inspect the public function without invoking any
    # audit/certificate consumer; retain the historical package initialization.
    blocked_paths = {root.joinpath(IMPLEMENTATION).resolve(),
                     root.joinpath("experiments/owner_one_positive_stability_20260908/"
                                   "check_one_positive_stability.py").resolve()}
    forbidden_calls = []

    def no_consumer_calls(frame, event, arg):
        if event == "call" and frame.f_code.co_name in {
                "audit_two_positive_stability", "audit_case", "_build_certificate", "main"}:
            if Path(frame.f_code.co_filename).resolve() in blocked_paths:
                forbidden_calls.append(frame.f_code.co_name)
                raise AssertionError("registration attempted a mathematical consumer call")

    saved_profile = sys.getprofile()
    sys.setprofile(no_consumer_calls)
    try:
        sys.path.insert(0, str(root.joinpath(IMPLEMENTATION).parent))
        import check_two_positive_stability as consumer
        require(Path(consumer.__file__).resolve() == root.joinpath(IMPLEMENTATION).resolve(),
                "noncanonical p2 consumer origin")
        require(consumer.SOURCE_SHA256 == runtime_pins, "imported consumer dependency pins changed")
        require(consumer.__all__ == ["audit_two_positive_stability"], "public export set changed")
        function = consumer.audit_two_positive_stability
        signature = str(inspect.signature(function))
        require(signature == "(case_id, mu_atoms, nu_atoms, denominator=1)", "API signature changed")
        require(row["api_signatures"] == {"audit_two_positive_stability": signature},
                "registered API signature differs from actual callable")
    finally:
        sys.setprofile(saved_profile)
    require(not forbidden_calls, "a mathematical consumer was executed")
    require(inventory_snapshot(root) == before, "inventory paths/bytes changed during validation")
    require(all(root.joinpath(path).read_bytes() == data for path, data in source_bytes.items()),
            "published source/dependency bytes changed during validation")
    require(loader.read_bytes() == loader_bytes and registry.read_bytes() == registry_bytes,
            "canonical inventory/registry implementation changed")
    require(Path(__file__).read_bytes() == script_bytes, "validator changed during execution")
    return {
        "schema": "OWNER_TWO_POSITIVE_EXECUTABLE_REGISTRATION_VALIDATION_V1",
        "status": "PASS_ONE_PUBLISHED_P2_EXECUTABLE_REGISTRATION",
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "python": sys.version.split()[0], "argv": sys.argv, "repository_root": str(root),
        "method_id": METHOD_ID, "source_commit": SOURCE_COMMIT, "source_tree": SOURCE_TREE,
        "catalog_context": catalog_context,
        "source_only_coverage_reference_ids": source_only_coverage_ids,
        "missing_reuse_ids": missing_reuse_ids,
        "executed_script_sha256": digest(script_bytes), "shard_sha256": digest(before[SHARD]),
        "canonical_loader_sha256": digest(loader_bytes), "tool_registry_sha256": digest(registry_bytes),
        "loaded_exactly_once": True, "actual_api_signature": signature,
        "public_exports": consumer.__all__, "canonical_api_origin": IMPLEMENTATION,
        "queries": query_results, "source_files_sha256": FILE_PINS,
        "runtime_and_proof_sha256": runtime_pins, "all_twenty_three_source_pins_unchanged": True,
        "protected_inventory_sources": {
            path: {"sha256_before_and_after": digest(data),
                   "observed_method_count": len(json.loads(data).get("methods", []))}
            for path, data in prior_bytes.items()},
        "protected_reused_method_object_sha256": {
            mid: object_digest(prior_by_id[mid]) for mid in PRIOR_REUSE_IDS if mid in prior_by_id},
        "prior_brc_family_object_view_sha256": object_digest(family_before),
        "observed_prior_brc_family_count": len(family_before),
        "observed_prior_method_count": len(prior), "observed_total_method_count": len(loaded),
        "observed_counts_are_not_permanent_source_or_main_assertions": True,
        "complete_prior_inventory_bytes_and_objects_unchanged": True,
        "mathematical_consumers_executed": False, "historical_case_datasets_replayed": False,
        "guarded_consumer_calls": forbidden_calls,
        "import_observation_boundary": "Canonical public modules were imported for signature inspection. Historical enterprise_math/Fraction initialization remains; this is not a transitive arithmetic migration or a mathematical proof run.",
        "formal_result_or_working_truth_or_main_admission_granted": False,
        "registration_authoring_global_knowledge_sync": "main@31d06a1 / GLOBAL_KNOWLEDGE_V1",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--catalog-context", choices=("source", "main"), default="source",
                        help="main permits only the declared source-only coverage reference to be absent")
    parser.add_argument("--write", action="store_true", help="write the actual registration receipt")
    args = parser.parse_args()
    report = validate(args.root, args.catalog_context)
    if args.write:
        args.root.joinpath(REPORT).write_text(
            json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps({"status": report["status"], "mode": "WRITE" if args.write else "READ_ONLY",
                      "method_id": METHOD_ID, "source_pins": len(FILE_PINS), "runtime_pins": 16,
                      "exact_queries": len(report["queries"]),
                      "actual_api_signature": report["actual_api_signature"],
                      "catalog_context": report["catalog_context"],
                      "source_only_coverage_reference_ids": report["source_only_coverage_reference_ids"],
                      "missing_reuse_ids": report["missing_reuse_ids"],
                      "observed_prior_methods": report["observed_prior_method_count"],
                      "mathematical_consumers_executed": False}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
