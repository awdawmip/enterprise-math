"""Validate the weighted-minimum-trade paper registration, not its mathematics.

Read-only by default. --write writes only this package's actual metadata receipt.
Historical checker files are immutable references; no mathematical API is run.
"""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import sys

SHARD = 'research_method_inventory_addenda/20260908_owner_weighted_trade_result.json'
REPORT = 'experiments/20260908_owner_weighted_trade_result/validation.json'
NEW_ID = 'result.x6.weighted_minimum_trade'
SOURCE_COMMIT = '909ed4c3c81adca8d5d653994a83df316faf1365'
SOURCE_TREE = '6f7a6294828c75f27352fea7f32eeb37199abe15'
BASE_COMMIT = 'd4bad54522bc0abf63e11d1ec03977efdb6f57b6'
SOURCE_OBJECT_SHA256 = '741435117ea536ce6da5c014c8b3417a78cece5686eb244970f590e046f73ca9'
ENVELOPE_SHA256 = '17a3c1fa3d6c62a4e17256506489d5982e67a3c58103c1d97a7e87b90bcb3aed'
REQUIRED_SOURCE_PINS = {'research_notes/OWNER_WEIGHTED_TRADE_FRONTIER_20260907.md': '520a41ee878aeb1d1c546a7c088ae1c86f0acbe8292d7356d00436322b6f20be',
 'research_notes/OWNER_WEIGHTED_TRADE_INDEPENDENT_AUDIT_20260907.md': 'bafe071af7d04a7734641410cd5820342ab307ddcef1a0e5cfd89f38bb0d2aa9',
 'research_notes/OWNER_X6_STABILITY_20260907.md': '2915e70210dce5bc136c915e45e96a7c8a1f6dd414fae1590a4687f41bff3127'}
CANONICAL_DEPENDENCY_PINS = {'tools/enterprise_toolbox.py': 'd0f0383a344194133a303f6758142bfd4ecd56deb35a3008f4bf6009ccf6892b',
 'enterprise_toolbox_registry.json': 'd8a0a7e6e2090def201175d9f42da1b1c2a56e80fe5a5220ab5c6c8e12da10e6'}
PAPERS = ['research_notes/OWNER_WEIGHTED_TRADE_FRONTIER_20260907.md',
 'research_notes/OWNER_WEIGHTED_TRADE_INDEPENDENT_AUDIT_20260907.md']


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
        root.joinpath("research_method_inventory_addenda").glob("*.json"))
    return {p.relative_to(root).as_posix(): p.read_bytes() for p in paths}


def validate(root):
    root = root.resolve()
    before = snapshot(root)
    require(SHARD in before, "weighted-trade registration shard absent")
    shard = json.loads(before[SHARD])
    require(isinstance(shard.get("methods"), list) and len(shard["methods"]) == 1,
            "exactly one weighted-trade result object is required")
    row = shard["methods"][0]
    require(row.get("method_id") == NEW_ID, "weighted-trade method ID changed")
    require(row.get("classification") == "RESULT_ONLY" and row.get("api") == []
            and row.get("family_id") is None, "paper result gained API/family or changed classification")
    require(row.get("status") == "TOOLBOX_INTEGRATION_CANDIDATE"
            and row.get("owner_review_status") == "INTERNAL_EVIDENCE_REVIEWED_FORMAL_ACCEPTANCE_ABSENT",
            "ungranted formal acceptance/status")
    require(object_digest(row) == SOURCE_OBJECT_SHA256, "original source method object changed")
    require(object_digest({k: v for k, v in shard.items() if k != "methods"}) == ENVELOPE_SHA256,
            "source/main provenance, support bridge, scope or historical pins changed")
    prior_bytes = {p: data for p, data in before.items() if p != SHARD}
    prior = [item for data in prior_bytes.values() for item in json.loads(data).get("methods", [])]
    require(all(item["method_id"] != NEW_ID for item in prior), "duplicate weighted-trade method ID")
    require(all(not set(PAPERS).intersection(item.get("source_refs", [])) for item in prior),
            "weighted-trade paper already registered under another method ID")
    expected_pins = {**REQUIRED_SOURCE_PINS, **CANONICAL_DEPENDENCY_PINS}
    source_bytes = {p: root.joinpath(p).read_bytes() for p in expected_pins}
    require({p: digest(data) for p, data in source_bytes.items()} == expected_pins,
            "required paper/support/canonical dependency bytes drifted")
    script_bytes = Path(__file__).read_bytes()
    before_modules = set(sys.modules)
    sys.path.insert(0, str(root.joinpath("tools")))
    import enterprise_toolbox as toolbox
    require(Path(toolbox.__file__).resolve() == root.joinpath("tools/enterprise_toolbox.py").resolve()
            and toolbox.ROOT.resolve() == root, "noncanonical inventory loader origin")
    inventory = toolbox.load_method_inventory()
    loaded = inventory["methods"]
    require([item for item in loaded if item["method_id"] != NEW_ID] == prior,
            "prior method objects/order changed")
    require([item for item in loaded if item["method_id"] == NEW_ID] == [row],
            "new result must load exactly once and unchanged")
    queries = []
    for query in row["triggers"]:
        hits = toolbox.method_suggestions(query, inventory=inventory)
        matches = [hit for hit in hits if hit["method_id"] == NEW_ID]
        require(len(matches) == 1, "exact weighted-trade query missed")
        queries.append({"query": query, "matching_score": matches[0]["score"],
                        "returned_method_ids": [hit["method_id"] for hit in hits]})
    coverage = toolbox.coverage(row["triggers"][0])
    require(any(hit["method_id"] == NEW_ID for hit in coverage["methods"]),
            "canonical coverage lookup missed weighted-trade result")
    require(snapshot(root) == before, "inventory path set/bytes changed during validation")
    require(all(root.joinpath(p).read_bytes() == data for p, data in source_bytes.items()),
            "source/canonical dependency bytes changed during validation")
    require(Path(__file__).read_bytes() == script_bytes, "validator changed during execution")
    new_math_modules = sorted(name for name in set(sys.modules) - before_modules
                              if name == "enterprise_math" or name.startswith("enterprise_math.")
                              or name in {"x6_signed", "signed_brc"}
                              or name.startswith("owner_weighted_trade"))
    require(not new_math_modules, "metadata validation imported mathematical source modules")
    return {
        "schema": "OWNER_WEIGHTED_TRADE_RESULT_METADATA_VALIDATION_V1",
        "status": "PASS_ONE_EXACT_RESULT_ONLY_REGISTRATION",
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "repository_root": str(root), "python": sys.version.split()[0], "argv": sys.argv,
        "source_commit": SOURCE_COMMIT, "source_tree": SOURCE_TREE,
        "composition_base_commit": BASE_COMMIT,
        "executed_script_sha256": digest(script_bytes), "shard_sha256": digest(before[SHARD]),
        "method_id": NEW_ID, "method_object_sha256": object_digest(row),
        "classification": "RESULT_ONLY", "api": [], "family_id": None,
        "source_and_canonical_dependency_sha256": expected_pins,
        "required_local_pins_checked": len(expected_pins),
        "historical_source_pin_declarations_checked": shard["historical_source_pins"],
        "historical_remote_bytes_reverified_in_this_run": False,
        "queries": queries,
        "coverage": {"query": coverage["query"], "verdict": coverage["verdict"],
                     "method_ids": [x["method_id"] for x in coverage["methods"]],
                     "tool_family_ids": [x["id"] for x in coverage["tool_families"]],
                     "boundary": "Catalog/text lookup only; matched tools or source modules were not invoked."},
        "protected_prior_inventory_sources": {p: digest(data) for p, data in prior_bytes.items()},
        "protected_prior_method_object_sha256": {item["method_id"]: object_digest(item) for item in prior},
        "prior_bytes_objects_and_order_unchanged": True,
        "observed_prior_method_count": len(prior), "observed_total_method_count": len(loaded),
        "counts_are_execution_observations_not_fixed_future_catalog_requirements": True,
        "new_mathematical_source_modules_imported_in_this_process_window": new_math_modules,
        "mathematical_api_or_historical_checker_executed": False,
        "proof_or_native_arithmetic_runtime_certified_by_this_validator": False,
        "formal_task_result_review_working_truth_or_main_admission_granted": False,
        "registration_authoring_global_knowledge_sync": "main@519a3b5 / GLOBAL_KNOWLEDGE_V1",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--write", action="store_true", help="write only this package's actual metadata receipt")
    args = parser.parse_args()
    report = validate(args.root)
    if args.write:
        args.root.joinpath(REPORT).write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n",
                                        encoding="utf-8", newline="\n")
    print(json.dumps({"status": report["status"], "mode": "WRITE" if args.write else "READ_ONLY",
                      "new_results": 1, "exact_method_queries": len(report["queries"]),
                      "coverage_queries": 1, "required_local_pins": report["required_local_pins_checked"],
                      "observed_prior_methods": report["observed_prior_method_count"],
                      "mathematical_consumers_executed": False}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
