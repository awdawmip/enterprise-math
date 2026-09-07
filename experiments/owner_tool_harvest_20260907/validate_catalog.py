"""Verify this candidate catalog's routing and exact source binding, not its mathematics."""
from __future__ import annotations

import ast
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from tools import enterprise_toolbox as router

SHARD = "research_method_inventory_addenda/20260907_owner_native_frontier_candidates.json"
STATUS = "TOOLBOX_INTEGRATION_CANDIDATE"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def validate():
    catalog = json.loads((ROOT / SHARD).read_text(encoding="utf-8"))
    assert catalog["status"] == STATUS
    assert catalog["authority"] == "FRONTIER_ROUTING_ONLY_EXACT_SOURCES_CONTROL"
    assert catalog["provenance"]["formal_driver_or_steward_acceptance"] is None
    assert catalog["provenance"]["official_claim"] is None
    assert not catalog["provenance"]["foundation_mutation"]
    assert not catalog["provenance"]["new_global_tool_family"]
    inventory = router.load_method_inventory()  # Existing duplicate-ID guard is executed.
    assert SHARD in [path.replace("\\", "/") for path in inventory["loaded_addenda"]]
    loaded = {m["method_id"]: m for m in inventory["methods"]}
    family_ids = {m["id"] for m in router.load_json(router.REGISTRY_PATH)["tools"]}
    vocabulary = set(router.load_json(router.METHOD_INVENTORY_PATH)["classification_vocabulary"])
    policy = router.load_json(ROOT / "tool_invocation_policy.json")
    states = set(policy["reuse_resolution"]["states"])
    coverage_verdicts = set(policy["coverage_verdicts"])
    required_reuse = set(policy["reuse_resolution"]["minimum_record"])
    checked_paths = {}
    query_results = []
    api_count = 0
    for method in catalog["methods"]:
        key = method["method_id"]
        assert loaded[key] == method, key
        assert method["status"] == STATUS, key
        assert method["classification"] in vocabulary, key
        assert method["owner_review_status"] == "INTERNAL_EVIDENCE_REVIEWED_FORMAL_ACCEPTANCE_ABSENT"
        assert method["family_id"] is None or method["family_id"] in family_ids, key
        assert set(method.get("supporting_family_ids", [])) <= family_ids, key
        for field in ("input_contract", "output_contract", "core_law", "hard_boundary"):
            assert isinstance(method[field], str) and method[field].strip(), (key, field)
        reuse = method["reuse_resolution"]
        assert required_reuse <= set(reuse), key
        assert reuse["reuse_resolution_state"] in states, key
        assert reuse["coverage_verdict"] in coverage_verdicts, key
        assert set(reuse["matched_tool_or_method_ids"]) <= (family_ids | loaded.keys()), key
        refs = set(method["source_refs"]) | set(method["validation_refs"])
        assert refs == set(method["source_sha256"]), key
        definitions = set()
        for ref in sorted(refs):
            path = (ROOT / ref).resolve()
            assert path.is_relative_to(ROOT.resolve()) and path.is_file(), (key, ref)
            digest = sha(path)
            assert digest == method["source_sha256"][ref], (key, ref, "source drift")
            checked_paths[ref] = digest
            if ref.endswith(".py") and ref in method["source_refs"]:
                tree = ast.parse(path.read_text(encoding="utf-8"), filename=ref)
                definitions |= {node.name for node in tree.body
                                if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef))}
        assert set(method["api"]) <= definitions, (key, "missing declared API")
        if method["classification"] == "RESULT_ONLY":
            assert not method["api"], (key, "result is not an executable oracle")
        api_count += len(method["api"])
        query = method["triggers"][0]
        hits = router.method_suggestions(query)
        ids = [item["method_id"] for item in hits]
        assert key in ids, (key, query, "not in default search window", ids)
        hit = hits[ids.index(key)]
        assert hit["status"] == STATUS and hit["hard_boundary"] == method["hard_boundary"]
        query_results.append({"query": query, "expected_id": key, "rank": ids.index(key) + 1})
    # Independently discovered discoverability gap: this user phrase previously ranked 14.
    path_query = "finite path reverse step port monitor"
    path_hits = [m["method_id"] for m in router.method_suggestions(path_query)]
    assert "candidate.x6.finite_reverse_step_port_monitor" in path_hits
    return {"status": "PASS", "scope": "CATALOG_ROUTING_SOURCE_BINDING_AND_DECLARED_API_ONLY",
            "catalog_sha256": sha(ROOT / SHARD), "catalog_status": STATUS,
            "formal_acceptance_asserted": False, "method_count": len(catalog["methods"]),
            "unique_source_paths_checked": len(checked_paths), "declared_api_count": api_count,
            "natural_language_queries": query_results,
            "extra_path_query_rank": path_hits.index("candidate.x6.finite_reverse_step_port_monitor") + 1,
            "source_sha256": checked_paths,
            "limitations": ["Pure Chinese queries are not indexed by the current ASCII tokenizer.",
                            "This check does not prove source theorems or assert main admission.",
                            "External runtimes and complete source dependencies remain caller requirements."]}


if __name__ == "__main__":
    result = validate()
    output = Path(__file__).with_name("catalog_validation.json")
    output.write_bytes((json.dumps(result, ensure_ascii=False, indent=2) + "\n").encode("utf-8"))
    print(json.dumps({key: result[key] for key in ("status", "method_count", "unique_source_paths_checked",
                                                "declared_api_count", "extra_path_query_rank")}))
