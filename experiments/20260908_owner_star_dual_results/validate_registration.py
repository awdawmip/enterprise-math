"""Validate one new paper result and two reused star result registrations.

Metadata only: no mathematical imports, consumers, carrier enumeration or proof
execution. Read-only by default; --write records the actual validation receipt.
"""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import sys


SHARD = "research_method_inventory_addenda/20260908_owner_star_dual_results.json"
REPORT = "experiments/20260908_owner_star_dual_results/validation.json"
OLD_SHARD = "research_method_inventory_addenda/20260908_owner_star_stability_results.json"
OLD_SHARD_SHA256 = "2ab6c7249446ae4c258f19e2a38104633213eeeed7289ea4d53a0fc2e0bbbe82"
SOURCE_COMMIT = "df8dec38cf081737aa7ae2fbdf515504dbed1c20"
SOURCE_TREE = "bb94cb04e075b853b794da98c701e460c1780a00"
NEW_ID = "result.x6.compressed_raw_dual_certificate"
REUSED_IDS = ["result.x6.three_positive_star_raw_stability",
              "result.x6.three_positive_star_fixed_weight_stability"]
DUAL = "research_notes/OWNER_COMPRESSED_RAW_DUAL_CERTIFICATE_REVIEW_20260908.md"
SHARP = "research_notes/OWNER_THREE_POSITIVE_STAR_SHARP_STABILITY_REVIEW_20260908.md"
PROFILE = "research_notes/OWNER_THREE_POSITIVE_STAR_WEIGHT_PROFILE_REVIEW_20260908.md"
STRUCTURE = "research_notes/OWNER_THREE_POSITIVE_EQUAL_MASS_STRUCTURAL_REVIEW_20260908.md"
COMPRESSION = "research_notes/OWNER_POSITIVE_SUPPORT_RAW_COMPRESSION_REVIEW_20260908.md"
CONSUMER = "experiments/owner_positive_support_compression_20260908/check_positive_support_compression.py"
PROBE = "research_notes/OWNER_THREE_POSITIVE_RAW_STABILITY_PROBE_20260908.md"
SOURCE_PINS = {
    DUAL: "193e5833b3d59e434ff656779839501af6ddd6ece9a40b6fe36aad406071bbdc",
    SHARP: "6a809986a77a5cc21deb8cdb4062af13d44993fc465b073111eaacf5f7671fe1",
    PROFILE: "fe5169d2e5e093d21753ad27994825ecf4f58d9ea2fa19d042dd445e78b6e0e6",
    STRUCTURE: "47f12081c02090cc19de25b2c8ed234b6ed8a5ed300ea4fb13df4d8ff71dcda8",
    COMPRESSION: "2cb061262e713859fd419871d0be9e4d5041698a01a46a55bd5ef5fc3f7e38b4",
    CONSUMER: "f7e31ef40a2af4da1eaf0726068b212bb5efd66e82056ef91c8ee29581853660",
    PROBE: "53f56fe00300a38690de9fc831353f5b24623bf1982f6ba4113d7aac602a6a59",
}
DUAL_DEPENDENCIES = [COMPRESSION, CONSUMER, STRUCTURE, SHARP, PROFILE]
QUERIES = [
    "compressed raw X6 integer dual certificate positive support finite carrier",
    "X6 正支撑压缩 raw 有限整数对偶证书 原空间取等纤维",
]
DUAL_SCOPE = {
    "post_jordan_positive_support_fixed_finite_nonempty": True,
    "same_external_anchor_and_labelled_raw_x6_chart": True,
    "positive_rational_population_weights": True,
    "arbitrary_finite_original_negative_support_disjoint_from_S": True,
    "signed_difference_is_analysis_not_negative_brc_primitive": True,
    "coordinate_carrier": "A_i={s_i:s in S}; c_i=max(A_i)+1; C=product_i(A_i union {c_i})",
    "compression_preserves_P_N_and_each_raw_marginal_L1": True,
    "table_contract": "all twenty complete b_I:C_I->Z; integer L>0; |b_I|<=L",
    "potential_contract": "F=sum_I b_I; integer B>=0; F(z)<=-B for every z in C minus S",
    "positive_potentials": "a_s=F(s); signed and nonuniform values allowed",
    "linear_bound": "L*D >= sum_s(a_s*w_s)+B*N",
    "B_zero_allowed": True,
    "uniform_M_bound_requires": "integer A>0; every a_s>=A; B>=A",
    "uniform_bound": "L*D >= A*M",
    "uniform_coefficient": "native unevaluated DIV(L,A) only after A>0",
    "full_linear_gap": "sum_(I,t)(L*abs(h'_I(t))-b_I(t)*h'_I(t))+sum_(z in C minus S)((-F(z)-B)*n'(z))",
    "linear_equality_iff": "all table-address gaps vanish and every actual negative compressed point has F=-B",
    "original_negative_support": "subset phi^(-1)(Z), where Z={z in C minus S:F(z)=-B}",
    "singleton_fiber_iff": "every coordinate of the compressed point belongs to its A_i",
    "all_tight_fibers_singleton_sufficient_condition": "Z subset product_i A_i",
    "support_condition_alone_classifies_equality": False,
    "uniform_equality_extra_conditions": "all a_s=A; if N>0 also B=A, in addition to the linear equality conditions",
    "empty_positive_support_branch": "D=20*N=20*M; no max(empty set)",
    "zero_difference_ratio_defined": False,
    "budget_exhaustion_means_mathematical_falsehood": False,
    "finite_carrier_complete_check_required_for_future_certificate": True,
    "generic_dual_verifier_implemented": False,
    "all_three_positive_sharp_bound_proved": False,
    "optimal_certificate_search_provided": False,
    "main_question_closed": False,
    "formal_result_or_working_truth_granted": False,
}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def object_digest(value):
    return digest(json.dumps(value, ensure_ascii=False, sort_keys=True,
                             separators=(",", ":")).encode("utf-8"))


def snapshot(root):
    paths = [root.joinpath("research_method_inventory.json")] + sorted(
        root.joinpath("research_method_inventory_addenda").glob("*.json")
    )
    return {p.relative_to(root).as_posix(): p.read_bytes() for p in paths}


def validate(root):
    root = root.resolve()
    before = snapshot(root)
    require(SHARD in before and OLD_SHARD in before, "required registration shard absent")
    require(digest(before[OLD_SHARD]) == OLD_SHARD_SHA256, "frozen star shard drifted")
    shard = json.loads(before[SHARD])
    prior_bytes = {p: data for p, data in before.items() if p != SHARD}
    prior = [row for data in prior_bytes.values() for row in json.loads(data).get("methods", [])]
    require(all(row["method_id"] != NEW_ID for row in prior), "duplicate compressed result ID")
    require(all(DUAL not in row.get("source_refs", []) for row in prior),
            "the same compressed-dual paper is already registered elsewhere")
    prior_by_id = {row["method_id"]: row for row in prior}
    require(all(mid in prior_by_id for mid in REUSED_IDS), "a reused star result is absent")
    sources = {p: root.joinpath(p).read_bytes() for p in SOURCE_PINS}
    require({p: digest(data) for p, data in sources.items()} == SOURCE_PINS,
            "published paper/dependency source drifted")
    loader = root.joinpath("tools/enterprise_toolbox.py")
    loader_bytes = loader.read_bytes()
    registry = root.joinpath("enterprise_toolbox_registry.json")
    registry_bytes = registry.read_bytes()
    script_bytes = Path(__file__).read_bytes()

    require(shard["schema"] == "ENTERPRISE_MATH_RESEARCH_METHOD_INVENTORY_ADDENDUM_V1",
            "wrong inventory schema")
    require(shard["status"] == "TOOLBOX_INTEGRATION_CANDIDATE"
            and shard["authority"] == "FRONTIER_ROUTING_ONLY_EXACT_SOURCES_CONTROL",
            "source-candidate authority changed")
    provenance = shard["provenance"]
    require((provenance["source_commit"], provenance["source_tree"])
            == (SOURCE_COMMIT, SOURCE_TREE), "published source snapshot changed")
    for key in ("official_claim", "formal_result", "formal_driver_or_steward_acceptance"):
        require(provenance[key] is None, f"ungranted formal authority: {key}")
    for key in ("foundation_mutation", "working_truth_granted", "new_global_tool_family"):
        require(provenance[key] is False, f"ungranted authority: {key}")
    require(shard["availability"]["loader"] == "tools/enterprise_toolbox.py"
            and shard["availability"]["formal_acceptance_inferred_from_indexing"] is False,
            "canonical loading/acceptance boundary changed")
    require(shard["bundle_source_sha256"] == SOURCE_PINS, "bundle source pins changed")
    require(len(shard["methods"]) == 1 and shard["methods"][0]["method_id"] == NEW_ID,
            "only the absent compressed result may be newly registered")
    row = shard["methods"][0]
    require(row["source_refs"] == [DUAL] and row["dependency_refs"] == DUAL_DEPENDENCIES,
            "compressed proof/dependency references changed")
    require(row["source_sha256"] == {p: SOURCE_PINS[p] for p in [DUAL, *DUAL_DEPENDENCIES]},
            "compressed proof/dependency pins changed")
    require(row["validation_refs"] == [DUAL], "paper review source changed")
    require(row["triggers"] == QUERIES, "compressed bilingual queries changed")
    require(row["result_scope"] == DUAL_SCOPE, "compressed paper scope changed")
    require(row["reuse_resolution"]["reuse_resolution_state"] == "EXTEND_EXISTING_TOOL"
            and row["reuse_resolution"]["matched_toolsets"] == ["T0_BRC"],
            "existing BRC reuse boundary changed")
    require([item["method_id"] for item in shard["reused_existing_results"]] == REUSED_IDS,
            "the two prior star IDs must be referenced without duplication")
    for item in shard["reused_existing_results"]:
        old = prior_by_id[item["method_id"]]
        require(item == {"method_id": old["method_id"], "catalog_ref": OLD_SHARD,
                         "catalog_sha256": OLD_SHARD_SHA256,
                         "method_object_sha256": object_digest(old),
                         "source_refs": old["source_refs"], "source_sha256": old["source_sha256"]},
                "a reused result reference differs from its frozen original")
    for item in [row, *(prior_by_id[mid] for mid in REUSED_IDS)]:
        require(item["classification"] == "RESULT_ONLY" and item["api"] == []
                and item["family_id"] is None, "paper result gained executable API/family")
        require(item["status"] == "TOOLBOX_INTEGRATION_CANDIDATE"
                and item["owner_review_status"]
                == "INTERNAL_EVIDENCE_REVIEWED_FORMAL_ACCEPTANCE_ABSENT", "formal status changed")

    sys.path.insert(0, str(root.joinpath("tools")))
    import enterprise_toolbox as toolbox
    require(Path(toolbox.__file__).resolve() == loader.resolve()
            and toolbox.ROOT.resolve() == root, "noncanonical inventory loader origin")
    inventory = toolbox.load_method_inventory()
    loaded = inventory["methods"]
    require([item for item in loaded if item["method_id"] != NEW_ID] == prior,
            "prior method objects/order changed")
    require([item for item in loaded if item["method_id"] == NEW_ID] == [row],
            "new result is not loaded exactly once and unchanged")
    checks = []
    for expected in [*(prior_by_id[mid] for mid in REUSED_IDS), row]:
        mid = expected["method_id"]
        require([item for item in loaded if item["method_id"] == mid] == [expected],
                f"{mid}: duplicate or changed result object")
        require(len(expected["triggers"]) == 2 and expected["triggers"][0].isascii()
                and any("\u4e00" <= c <= "\u9fff" for c in expected["triggers"][1]),
                f"{mid}: exact English/Chinese query missing")
        queries = []
        for language, query in zip(("en", "zh-CN"), expected["triggers"]):
            hits = toolbox.method_suggestions(query, inventory=inventory)
            matches = [hit for hit in hits if hit["method_id"] == mid]
            require(len(matches) == 1, f"{mid}: {language} lookup missed")
            queries.append({"language": language, "query": query,
                            "matching_score": matches[0]["score"],
                            "returned_method_ids": [hit["method_id"] for hit in hits]})
        checks.append({"method_id": mid, "newly_registered": mid == NEW_ID,
                       "classification": "RESULT_ONLY", "api": [], "family_id": None,
                       "method_object_sha256": object_digest(expected), "queries": queries})
    require(snapshot(root) == before, "inventory path set/bytes changed during validation")
    require(all(root.joinpath(p).read_bytes() == data for p, data in sources.items()),
            "source bytes changed during validation")
    require(loader.read_bytes() == loader_bytes and registry.read_bytes() == registry_bytes,
            "canonical loader/tool registry changed")
    require(Path(__file__).read_bytes() == script_bytes, "validator changed during execution")
    math_modules = sorted(name for name in sys.modules if name in {"x6_signed", "signed_brc"}
                          or name == "enterprise_math" or name.startswith("enterprise_math.")
                          or name.startswith("check_positive_support_compression"))
    require(not math_modules, "metadata registration imported mathematical modules")
    return {
        "schema": "OWNER_STAR_DUAL_RESULT_REGISTRATION_VALIDATION_V1",
        "status": "PASS_ONE_NEW_AND_TWO_REUSED_RESULT_ONLY_REGISTRATIONS",
        "created_utc": datetime.now(timezone.utc).isoformat(), "python": sys.version.split()[0],
        "argv": sys.argv, "repository_root": str(root),
        "source_commit": SOURCE_COMMIT, "source_tree": SOURCE_TREE,
        "executed_script_sha256": digest(script_bytes), "shard_sha256": digest(before[SHARD]),
        "canonical_loader_sha256": digest(loader_bytes), "tool_registry_sha256": digest(registry_bytes),
        "results": checks, "source_sha256": SOURCE_PINS, "source_bytes_unchanged": True,
        "reused_star_catalog_sha256": OLD_SHARD_SHA256,
        "reused_star_objects_unchanged_and_not_duplicated": True,
        "protected_inventory_sources": {
            p: {"sha256_before_and_after": digest(data),
                "observed_method_count": len(json.loads(data).get("methods", []))}
            for p, data in prior_bytes.items()},
        "complete_prior_inventory_bytes_and_objects_unchanged": True,
        "observed_prior_method_count": len(prior), "observed_total_method_count": len(loaded),
        "observed_counts_are_not_permanent_source_or_main_assertions": True,
        "mathematical_source_modules_imported": math_modules,
        "mathematical_consumers_or_historical_cases_executed": False,
        "generic_dual_verifier_implemented": False,
        "mathematical_proof_verified_by_this_program": False,
        "formal_result_or_working_truth_or_main_admission_granted": False,
        "registration_authoring_global_knowledge_sync": "main@31d06a1 / GLOBAL_KNOWLEDGE_V1",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--write", action="store_true", help="write an actual metadata receipt")
    args = parser.parse_args()
    report = validate(args.root)
    if args.write:
        args.root.joinpath(REPORT).write_text(json.dumps(report, ensure_ascii=False, indent=2)
                                             + "\n", encoding="utf-8", newline="\n")
    print(json.dumps({"status": report["status"], "mode": "WRITE" if args.write else "READ_ONLY",
                      "new_results": 1, "reused_results": len(REUSED_IDS),
                      "source_pins": len(SOURCE_PINS), "exact_queries": 6,
                      "observed_prior_methods": report["observed_prior_method_count"],
                      "mathematical_consumers_executed": False}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
