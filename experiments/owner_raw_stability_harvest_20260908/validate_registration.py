"""Check two paper-only catalog entries; never execute mathematical consumers."""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import sys
import subprocess


def digest(data):
    return hashlib.sha256(data).hexdigest()


def validate(root):
    shard_path = root / "research_method_inventory_addenda/20260908_owner_raw_stability_results.json"
    old_path = root / "research_method_inventory_addenda/20260907_owner_native_frontier_candidates.json"
    shard_bytes, old_bytes = shard_path.read_bytes(), old_path.read_bytes()
    shard, old = json.loads(shard_bytes), json.loads(old_bytes)
    compression = "research_notes/OWNER_POSITIVE_SUPPORT_RAW_COMPRESSION_REVIEW_20260908.md"
    author = "research_notes/OWNER_TWO_POSITIVE_RAW_STABILITY_BOUND_REVIEW_20260908.md"
    independent = "research_notes/OWNER_TWO_POSITIVE_RAW_STABILITY_INDEPENDENT_AUDIT_20260908.md"
    expected = {
        "result.x6.positive_support_raw_l1_compression": ([compression], [compression]),
        "result.x6.two_positive_raw_stability": ([author, independent], [independent]),
    }
    assert shard["schema"] == "ENTERPRISE_MATH_RESEARCH_METHOD_INVENTORY_ADDENDUM_V1"
    assert shard["status"] == "TOOLBOX_INTEGRATION_CANDIDATE"
    assert shard["provenance"]["formal_driver_or_steward_acceptance"] is None
    assert shard["provenance"]["official_claim"] is None
    for key in ("foundation_mutation", "new_global_tool_family"):
        assert shard["provenance"][key] is False
    assert shard["availability"]["formal_acceptance_inferred_from_indexing"] is False
    rows = shard["methods"]
    assert len(rows) == 2 and {m["method_id"] for m in rows} == set(expected)
    papers = {}
    for row in rows:
        refs, validations = expected[row["method_id"]]
        assert row["source_refs"] == refs and row["validation_refs"] == validations
        assert set(row["source_sha256"]) == set(refs)
        assert row["classification"] == "RESULT_ONLY" and row["family_id"] is None
        assert row["api"] == [] and row["status"] == "TOOLBOX_INTEGRATION_CANDIDATE"
        assert row["owner_review_status"] == "INTERNAL_EVIDENCE_REVIEWED_FORMAL_ACCEPTANCE_ABSENT"
        assert row["reuse_resolution"]["reuse_resolution_state"] == "EXTEND_EXISTING_TOOL"
        scope = row["result_scope"]
        for key in ("post_jordan_positive_support", "same_anchor_labelled_signed_x6",
                    "all_twenty_complete_raw_three_axis_norms", "p_zero_handled_separately"):
            assert scope[key] is True
        for key in ("zero_ratio_defined", "recovers_microscopic_brc", "executable_theorem_certificate"):
            assert scope[key] is False
        for path, pin in row["source_sha256"].items():
            data = (root / path).read_bytes()
            assert digest(data) == pin, path
            papers[path] = data
    assert len(papers) == 3
    by_id = {row["method_id"]: row for row in rows}
    first, second = (by_id[mid]["result_scope"] for mid in expected)
    assert first["preserves_every_coordinate_marginal_l1"] is True
    assert first["carrier_bound_is_actual_support_count"] is False
    assert second["maximum_positive_support"] == 2
    assert (second["sharp_constant_numerator"], second["sharp_constant_denominator"]) == (1, 4)
    assert second["equal_mass_also_sharp"] is True
    assert second["extends_to_p_ge_3"] is False and second["complete_equality_classification"] is False

    sys.path.insert(0, str(root / "tools"))
    import enterprise_toolbox as toolbox
    assert Path(toolbox.__file__).resolve() == (root / "tools/enterprise_toolbox.py").resolve()
    inventory = toolbox.load_method_inventory()
    checks = []
    for row in rows:
        mid = row["method_id"]
        assert [m for m in inventory["methods"] if m["method_id"] == mid] == [row]
        triggers = row["triggers"]
        assert len(triggers) == 2 and triggers[0].isascii()
        assert any("\u4e00" <= char <= "\u9fff" for char in triggers[1])
        hits = []
        for language, query in zip(("en", "zh-CN"), triggers):
            found = toolbox.method_suggestions(query, inventory=inventory)
            assert mid in {m["method_id"] for m in found}, (mid, query)
            hits.append({"language": language, "query": query, "hit": True})
        checks.append({"method_id": mid, "loaded_exactly_once": True, "api": [], "queries": hits})
    assert shard_path.read_bytes() == shard_bytes
    assert old_path.read_bytes() == old_bytes
    assert json.loads(old_path.read_bytes())["methods"] == old["methods"]
    assert all((root / path).read_bytes() == data for path, data in papers.items())
    return {
        "schema": "OWNER_RAW_STABILITY_PAPER_REGISTRATION_VALIDATION_V1",
        "status": "PASS_TWO_RESULT_ONLY_REGISTRATIONS",
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "python": sys.version.split()[0],
        "argv": sys.argv,
        "executed_script_sha256": digest(Path(__file__).read_bytes()),
        "shard_sha256": digest(shard_bytes),
        "canonical_loader_sha256": digest(Path(toolbox.__file__).read_bytes()),
        "methods": checks,
        "source_paper_sha256": {path: digest(data) for path, data in papers.items()},
        "source_papers_unchanged": True,
        "protected_previous_shard": {
            "path": str(old_path.relative_to(root)),
            "sha256_before_and_after": digest(old_bytes),
            "observed_method_count": len(old["methods"]),
            "all_method_objects_and_file_bytes_unchanged": True,
            "observed_count_is_not_a_permanent_main_assertion": True,
        },
        "boundary_checks_passed": True,
        "mathematical_consumers_executed": False,
        "proof_or_formal_acceptance_granted": False,
        "source_authoring_global_knowledge_sync": "main@990d7c1 / GLOBAL_KNOWLEDGE_V1",
    }



BASE_COMMIT = 'fb83bcbe252f19f36961ad8fc80090c1806b6f6a'
FROZEN_SOURCE_SHA256 = {'research_notes/OWNER_POSITIVE_SUPPORT_RAW_COMPRESSION_REVIEW_20260908.md': '2cb061262e713859fd419871d0be9e4d5041698a01a46a55bd5ef5fc3f7e38b4', 'research_notes/OWNER_TWO_POSITIVE_RAW_STABILITY_BOUND_REVIEW_20260908.md': '1bb732a50cccbbec6c8c11950104c62eed9afc15f326fcc39d9142bd13b24a35', 'research_notes/OWNER_TWO_POSITIVE_RAW_STABILITY_INDEPENDENT_AUDIT_20260908.md': 'f610e3d642b53279efa91dec15ad3b392270768f73ad0a31edf38212b60be61c', 'research_method_inventory_addenda/20260908_owner_raw_stability_results.json': 'b1d4d216f76bde3fa2964912db68c96d5ff68b661ce793054e18df44048e95eb'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base-commit", required=True)
    parser.add_argument("--global-knowledge-sync", required=True)
    parser.add_argument("--receipt", type=Path, default=Path(__file__).with_name("validation.json"))
    args = parser.parse_args()
    if not __debug__:
        raise RuntimeError("normal assertions are required; do not use python -O")
    root = Path(__file__).resolve().parents[2]
    assert args.base_commit == BASE_COMMIT, "reassess a changed main explicitly"

    def git(*words):
        return subprocess.check_output(["git", "-C", str(root), *words])

    def entries(ref):
        return {line.split("\t", 1)[1]: line.split("\t", 1)[0]
                for line in git("ls-tree", "-r", ref).decode().splitlines()}

    subprocess.run(["git", "-C", str(root), "merge-base", "--is-ancestor", args.base_commit, "HEAD"], check=True)
    assert not git("diff", "--name-only").strip() and not git("diff", "--cached", "--name-only").strip()
    head = git("rev-parse", "HEAD").decode().strip()
    tree = git("rev-parse", "HEAD^{tree}").decode().strip()
    baseline, current = entries(args.base_commit), entries(head)
    assert all(current.get(path) == entry for path, entry in baseline.items()), "existing main entry changed"
    for path, pin in FROZEN_SOURCE_SHA256.items():
        assert digest((root / path).read_bytes()) == pin, path
    old_path = "research_method_inventory_addenda/20260907_owner_native_frontier_candidates.json"
    old_bytes = (root / old_path).read_bytes()
    assert old_bytes == git("show", args.base_commit + ":" + old_path)
    old = json.loads(old_bytes)
    assert len(old["methods"]) == 2
    old_pins = old["provenance"]["frozen_source_files_sha256"]
    assert len(old_pins) == 20
    assert all(digest((root / path).read_bytes()) == pin for path, pin in old_pins.items())

    report = validate(root)
    assert report["protected_previous_shard"]["observed_method_count"] == 2
    prior_path = root / "experiments/owner_native_tools_l4_20260908/validate_integration.py"
    sys.path.insert(0, str(prior_path.parent))
    import validate_integration as prior
    assert Path(prior.__file__).resolve() == prior_path.resolve()
    result = subprocess.run([sys.executable, "-X", "utf8", "-B", "-c", prior.API_CHECK, str(root)],
                            capture_output=True, text=True, encoding="utf-8", timeout=60)
    assert result.returncode == 0, result.stderr
    api_report = json.loads(result.stdout)
    assert api_report["status"] == "PASS_TWO_SELECTED_METHODS"
    assert sum(len(row["api_signatures"]) for row in api_report["methods"]) == 7
    assert (root / old_path).read_bytes() == old_bytes
    assert all(digest((root / path).read_bytes()) == pin for path, pin in FROZEN_SOURCE_SHA256.items())
    assert all(digest((root / path).read_bytes()) == pin for path, pin in old_pins.items())
    input_paths = sorted(set(current) - set(baseline) - {"experiments/owner_raw_stability_harvest_20260908/validation.json"})
    assert len(input_paths) == 6
    report["source_registration_schema"] = report["schema"]
    report["schema"] = "OWNER_RAW_STABILITY_PAPER_MAIN_VALIDATION_V1"
    report["main_execution"] = {
        "base_commit": args.base_commit, "base_tree": git("rev-parse", args.base_commit + "^{tree}").decode().strip(),
        "tested_input_commit": head, "tested_input_tree": tree,
        "unchanged_baseline_entries": len(baseline), "all_baseline_entries_unchanged": True,
        "frozen_source_sha256": FROZEN_SOURCE_SHA256,
        "input_sha256": {path: digest((root / path).read_bytes()) for path in input_paths},
        "old_two_method_objects_and_twenty_sources_unchanged": True,
        "prior_api_checker_sha256": digest(prior_path.read_bytes()),
        "prior_api_check": api_report, "prior_api_check_returncode": result.returncode,
        "prior_api_check_stdout_sha256": digest(result.stdout.encode()),
        "prior_api_check_stderr": result.stderr,
        "prior_api_check_kind": "Existing API_CHECK imports canonical modules and inspects callable signatures; no consumer replay is invoked. Module initialization is outside any arithmetic observation claim.",
        "mathematical_consumers_invoked": False,
        "current_main_freshness_or_promotion_authority_asserted": False,
        "global_knowledge_sync_recorded_for_this_execution": args.global_knowledge_sync,
    }
    args.receipt.parent.mkdir(parents=True, exist_ok=True)
    args.receipt.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps({"status": report["status"], "new_results": len(report["methods"]),
                      "old_methods": 2, "old_api_signatures": 7,
                      "baseline_entries_unchanged": len(baseline), "tested_input_commit": head,
                      "receipt_sha256": digest(args.receipt.read_bytes())}))


if __name__ == "__main__":
    main()
