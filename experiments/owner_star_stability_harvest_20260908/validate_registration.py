"""Validate two star RESULT_ONLY records and preserve all prior catalog metadata.

This program does not execute mathematical consumers or verify mathematical proofs.
The default is read-only; --write stores the actual metadata validation receipt.
"""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import sys


SHARD_PATH = "research_method_inventory_addenda/20260908_owner_star_stability_results.json"
SCRIPT_PATH = "experiments/owner_star_stability_harvest_20260908/validate_registration.py"
REPORT_PATH = "experiments/owner_star_stability_harvest_20260908/validation.json"
SHARP_ID = "result.x6.three_positive_star_raw_stability"
PROFILE_ID = "result.x6.three_positive_star_fixed_weight_stability"
SHARP = "research_notes/OWNER_THREE_POSITIVE_STAR_SHARP_STABILITY_REVIEW_20260908.md"
STRUCTURE = "research_notes/OWNER_THREE_POSITIVE_EQUAL_MASS_STRUCTURAL_REVIEW_20260908.md"
PROFILE = "research_notes/OWNER_THREE_POSITIVE_STAR_WEIGHT_PROFILE_REVIEW_20260908.md"
PAPER_PINS = {
    SHARP: "6a809986a77a5cc21deb8cdb4062af13d44993fc465b073111eaacf5f7671fe1",
    STRUCTURE: "47f12081c02090cc19de25b2c8ed234b6ed8a5ed300ea4fb13df4d8ff71dcda8",
    PROFILE: "fe5169d2e5e093d21753ad27994825ecf4f58d9ea2fa19d042dd445e78b6e0e6",
}
SPECS = {
    SHARP_ID: {
        "sources": [SHARP],
        "validations": [SHARP],
        "queries": [
            "three positive coordinate star raw stability sharp 7/26 equality",
            "X6 三正坐标星形 raw 稳定性 7/26 七角等幅取等",
        ],
    },
    PROFILE_ID: {
        "sources": [STRUCTURE, PROFILE],
        "validations": [PROFILE],
        "queries": [
            "three positive coordinate star fixed weight equal mass minimum D simplex",
            "X6 三正坐标星形 固定正权 等质量 精确最小 D 单纯形",
        ],
    },
}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def inventory_paths(root):
    """Match the canonical loader's source set, including the base inventory."""
    return [root.joinpath("research_method_inventory.json")] + sorted(
        root.joinpath("research_method_inventory_addenda").glob("*.json")
    )


def snapshot_inventory(root):
    return {
        path.relative_to(root).as_posix(): path.read_bytes()
        for path in inventory_paths(root)
    }


def validate_scopes(by_id):
    for row in by_id.values():
        scope = row["result_scope"]
        for key in (
            "post_jordan_positive_support", "same_anchor_labelled_signed_x6",
            "strictly_positive_rational_positive_weights",
            "arbitrary_finite_original_negative_support",
            "all_twenty_complete_raw_three_axis_norms", "star_subclass_only",
        ):
            require(scope[key] is True, f"{row['method_id']}: {key}")
        for key in (
            "global_all_three_positive_upper_bound", "zero_ratio_defined",
            "recovers_microscopic_brc", "executable_theorem_certificate",
        ):
            require(scope[key] is False, f"{row['method_id']}: {key}")
        require(scope["exact_positive_support"] == 3, "exact star support changed")
        require(
            scope["positive_support_shape"]
            == "q_i=c+d_i*e_(a_i), three distinct axes, each d_i a nonzero integer",
            "original-coordinate star shape changed",
        )
    sharp = by_id[SHARP_ID]["result_scope"]
    require(sharp["requires_equal_total_mass"] is False, "arbitrary mass scope changed")
    require(sharp["integer_bound"] == "21*D >= 78*M", "sharp integer bound changed")
    require(sharp["sharp_constant"] == {"numerator": 7, "denominator": 26},
            "sharp constant changed")
    require(sharp["complete_nonzero_equality_classification"] is True,
            "seven-corner classification missing")
    require(sharp["equality_all_seven_absolute_weights_equal"] is True,
            "equal absolute weights missing")
    require(sharp["equality_jordan_mass_ratio"] == {"positive": 3, "negative": 4},
            "sharp equality mass boundary changed")
    require(sharp["equality_is_equal_mass_example"] is False,
            "arbitrary-mass equality was mislabeled as equal mass")
    fixed = by_id[PROFILE_ID]["result_scope"]
    require(fixed["requires_equal_total_mass"] is True, "N=P missing")
    require(fixed["fixed_positive_weights"] is True, "fixed weights missing")
    require((fixed["P"], fixed["m"], fixed["M"])
            == ("sum(w_i)", "max(w_i)", "2*P"), "weight-profile definitions changed")
    require(fixed["exact_minimum_D"] == "max(8*P,24*m-4*P)",
            "exact minimum metadata changed")
    require(fixed["minimum_is_attained"] is True, "attainment missing")
    require(fixed["structural_bound"] == "D >= 7*P+N+abs(P-N)",
            "structural-paper dependency changed")
    require(fixed["balanced_equality"] == {
        "target": "D=8*P",
        "complete": True,
        "exists_iff": "m<=P/2",
        "T": "P-2*m",
        "parameters": "x_i>=0; X=sum(x_i)<=T",
        "base_mass": "a=(P-X)/2",
        "pair_mass": "v_ij=(w_i+w_j-w_k+X-2*x_k)/2",
        "inverse": "x_i=v_ij+v_ik-w_i",
        "unique_iff": "T=0",
        "zero_pair_negative_weights_allowed": True,
    }, "balanced equality simplex metadata changed")
    require(fixed["all_higher_minimum_distributions_classified"] is False,
            "unbalanced minimizer classification was overstated")


def validate(root):
    root = root.resolve()
    source_before = snapshot_inventory(root)
    require(SHARD_PATH in source_before, "star shard missing from canonical source set")
    shard_bytes = source_before[SHARD_PATH]
    shard = json.loads(shard_bytes)
    prior_bytes = {path: data for path, data in source_before.items() if path != SHARD_PATH}
    prior_rows = {
        path: json.loads(data).get("methods", [])
        for path, data in prior_bytes.items()
    }
    expected_prior_view = [row for rows in prior_rows.values() for row in rows]
    paper_bytes = {path: root.joinpath(path).read_bytes() for path in PAPER_PINS}
    require({path: digest(data) for path, data in paper_bytes.items()} == PAPER_PINS,
            "one of the three frozen paper sources drifted")
    loader_path = root.joinpath("tools/enterprise_toolbox.py")
    loader_bytes = loader_path.read_bytes()
    script_bytes = Path(__file__).read_bytes()

    require(shard["schema"] == "ENTERPRISE_MATH_RESEARCH_METHOD_INVENTORY_ADDENDUM_V1",
            "wrong inventory schema")
    require(shard["status"] == "TOOLBOX_INTEGRATION_CANDIDATE", "wrong catalog status")
    require(shard["authority"] == "FRONTIER_ROUTING_ONLY_EXACT_SOURCES_CONTROL",
            "catalog authority changed")
    provenance = shard["provenance"]
    for key in ("formal_driver_or_steward_acceptance", "official_claim"):
        require(provenance[key] is None, f"formal authority present: {key}")
    for key in ("foundation_mutation", "new_global_tool_family"):
        require(provenance[key] is False, f"unapproved authority mutation: {key}")
    require(shard["availability"]["formal_acceptance_inferred_from_indexing"] is False,
            "indexing was promoted to acceptance")
    require(shard["availability"]["loader"] == "tools/enterprise_toolbox.py",
            "noncanonical loader")

    rows = shard["methods"]
    require(len(rows) == 2, "this unit must contain exactly its two authorized results")
    require({row["method_id"] for row in rows} == set(SPECS), "wrong or duplicate result IDs")
    by_id = {row["method_id"]: row for row in rows}
    referenced_pins = {}
    for row in rows:
        mid = row["method_id"]
        spec = SPECS[mid]
        require(row["classification"] == "RESULT_ONLY", f"{mid}: executable classification")
        require(row["family_id"] is None and row["api"] == [], f"{mid}: API/family leakage")
        require(row["status"] == "TOOLBOX_INTEGRATION_CANDIDATE", f"{mid}: status changed")
        require(row["owner_review_status"]
                == "INTERNAL_EVIDENCE_REVIEWED_FORMAL_ACCEPTANCE_ABSENT",
                f"{mid}: formal review boundary changed")
        require(row["source_refs"] == spec["sources"], f"{mid}: source list changed")
        require(row["validation_refs"] == spec["validations"], f"{mid}: review list changed")
        expected_pins = {path: PAPER_PINS[path] for path in spec["sources"]}
        require(row["source_sha256"] == expected_pins, f"{mid}: exact paper pins changed")
        referenced_pins.update(row["source_sha256"])
        require(row["triggers"] == spec["queries"], f"{mid}: exact queries changed")
        require(row["triggers"][0].isascii(), f"{mid}: English query missing")
        require(any("\u4e00" <= c <= "\u9fff" for c in row["triggers"][1]),
                f"{mid}: Chinese query missing")
        require(row["reuse_resolution"]["reuse_resolution_state"] == "EXTEND_EXISTING_TOOL",
                f"{mid}: paper reuse boundary changed")
    require(referenced_pins == PAPER_PINS, "source union must be exactly three paper pins")
    validate_scopes(by_id)

    sys.path.insert(0, str(root.joinpath("tools")))
    import enterprise_toolbox as toolbox
    require(Path(toolbox.__file__).resolve() == loader_path.resolve(),
            "canonical loader module origin mismatch")
    require(toolbox.ROOT.resolve() == root, "loader is using a different repository")
    inventory = toolbox.load_method_inventory()
    actual_prior_view = [
        row for row in inventory["methods"] if row["method_id"] not in SPECS
    ]
    require(actual_prior_view == expected_prior_view,
            "loader changed or omitted a prior method object")
    checks = []
    for row in rows:
        mid = row["method_id"]
        require([item for item in inventory["methods"] if item["method_id"] == mid] == [row],
                f"{mid}: not loaded exactly once and unchanged")
        queries = []
        for language, query in zip(("en", "zh-CN"), SPECS[mid]["queries"]):
            hits = toolbox.method_suggestions(query, inventory=inventory)
            matching = [hit for hit in hits if hit["method_id"] == mid]
            require(len(matching) == 1, f"{mid}: exact {language} query missed")
            queries.append({
                "language": language, "query": query, "hit": True,
                "returned_method_ids": [hit["method_id"] for hit in hits],
                "matching_score": matching[0]["score"],
            })
        checks.append({
            "method_id": mid, "loaded_exactly_once": True,
            "classification": "RESULT_ONLY", "family_id": None, "api": [],
            "queries": queries,
        })

    require(snapshot_inventory(root) == source_before,
            "inventory path set or file bytes changed during metadata validation")
    require(all(root.joinpath(path).read_bytes() == data
                for path, data in paper_bytes.items()), "paper bytes changed during validation")
    require(loader_path.read_bytes() == loader_bytes, "loader changed during validation")
    require(Path(__file__).read_bytes() == script_bytes, "validator changed during validation")
    mathematical_modules = sorted(
        name for name in sys.modules
        if name == "x6_signed" or name == "signed_brc"
        or name == "enterprise_math" or name.startswith("enterprise_math.")
    )
    require(not mathematical_modules, "mathematical source module was imported")
    return {
        "schema": "OWNER_STAR_STABILITY_RESULT_REGISTRATION_VALIDATION_V1",
        "status": "PASS_TWO_RESULT_ONLY_STAR_REGISTRATIONS",
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "python": sys.version.split()[0],
        "argv": sys.argv,
        "repository_root": str(root),
        "executed_script_sha256": digest(script_bytes),
        "shard_sha256": digest(shard_bytes),
        "canonical_loader_sha256": digest(loader_bytes),
        "methods": checks,
        "source_paper_sha256": PAPER_PINS,
        "source_papers_unchanged": True,
        "protected_inventory_sources": {
            path: {
                "sha256_before_and_after": digest(data),
                "observed_method_count": len(prior_rows[path]),
                "all_method_objects_and_file_bytes_unchanged": True,
            }
            for path, data in prior_bytes.items()
        },
        "complete_inventory_source_set_unchanged": True,
        "canonical_prior_method_view_unchanged": True,
        "observed_prior_method_count": len(expected_prior_view),
        "observed_total_method_count": len(inventory["methods"]),
        "observed_counts_are_not_permanent_source_or_main_assertions": True,
        "boundary_checks_passed": True,
        "mathematical_source_modules_imported": mathematical_modules,
        "mathematical_consumers_executed": False,
        "mathematical_proof_verified_by_this_program": False,
        "proof_or_formal_acceptance_granted": False,
        "registration_authoring_global_knowledge_sync": "main@eb09a0a / GLOBAL_KNOWLEDGE_V1",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("repo", nargs="?", type=Path,
                        default=Path(__file__).resolve().parents[2])
    parser.add_argument("--write", action="store_true",
                        help="write the actual metadata receipt to validation.json")
    args = parser.parse_args()
    root = args.repo.resolve()
    report = validate(root)
    if args.write:
        root.joinpath(REPORT_PATH).write_text(
            json.dumps(report, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8", newline="\n",
        )
    print(json.dumps({
        "status": report["status"], "mode": "WRITE" if args.write else "READ_ONLY",
        "results": len(report["methods"]), "paper_pins": len(report["source_paper_sha256"]),
        "exact_queries": 4,
        "protected_inventory_sources": len(report["protected_inventory_sources"]),
        "observed_prior_methods_unchanged": report["observed_prior_method_count"],
        "mathematical_consumers_executed": False,
    }, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
