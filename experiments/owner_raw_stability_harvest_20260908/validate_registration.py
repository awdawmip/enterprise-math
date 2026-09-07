"""Check two paper-only catalog entries; never execute mathematical consumers."""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import sys


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
        "global_knowledge_sync": "main@990d7c1 / GLOBAL_KNOWLEDGE_V1",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("repo", nargs="?", type=Path, default=Path(__file__).resolve().parents[2])
    args = parser.parse_args()
    if not __debug__:
        raise RuntimeError("normal assertions are required; do not use python -O")
    report = validate(args.repo.resolve())
    target = Path(__file__).with_name("validation.json")
    target.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps({"status": report["status"], "methods": len(report["methods"]),
                      "paper_pins": len(report["source_paper_sha256"]),
                      "previous_shard_methods_unchanged": report["protected_previous_shard"]["observed_method_count"]}))


if __name__ == "__main__":
    main()
