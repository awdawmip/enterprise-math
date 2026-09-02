#!/usr/bin/env python3
"""Check the global Weighted-BRC Foundation theorem/tool/routing contract."""

from __future__ import annotations

import ast
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SUBSTRATE = ROOT / "definitions" / "ENTERPRISE_BRC_WEIGHTED_GLOBAL_SUBSTRATE_20260902.json"
LEDGER = ROOT / "definitions" / "ENTERPRISE_BRC_WEIGHTED_LOG_THEOREM_LEDGER_20260902.json"
FOUNDATION = ROOT / "definitions" / "ENTERPRISE_BRC_WEIGHTED_LOG_FOUNDATION_20260902.md"
FREE_ROUTER = ROOT / "definitions" / "00_FREE_AXIOM_DISCOVERY_SUBSTRATE.md"
CURRENT_ROUTER = ROOT / "definitions" / "00_CURRENT_NATIVE_FOUNDATION.md"
METHOD_ADDENDUM = ROOT / "research_method_inventory_addenda" / "20260902_brc_weighted_foundation.json"
TOOL_MODULE = ROOT / "src" / "enterprise_math" / "brc_weighted.py"

EXPECTED_THEOREMS = {
    "WBRC-T01-CWM-SEMIRING",
    "WBRC-T02-POSITIVE-REALIZABILITY",
    "WBRC-T03-BOOLEAN-SUPPORT-HOMOMORPHISM",
    "WBRC-T04-MULTIPLICITY-SURPLUS",
    "WBRC-T05-MAX-TOTAL-DECOMPOSITION",
    "WBRC-T06-ALL-PREFIX-SAFE-QUOTIENT",
    "WBRC-T07-PROJECTIVE-GAUGE-QUOTIENT",
    "WBRC-T08-ONE-STATE-RECURRENT-POWER",
    "WBRC-T09-ONE-STATE-TOTAL-MASS-STABILITY",
    "WBRC-T10-EQUAL-LOOP-LOG-THRESHOLD",
    "WBRC-T11-DETERMINISTIC-DEGENERATION",
}
EXPECTED_NEGATIVE = {
    "WBRC-N01-SIGNED-CANCELLATION",
    "WBRC-N02-ZERO-DIVISOR-SUPPORT",
    "WBRC-N03-BOOLEAN-QUOTIENT-TOO-COARSE",
    "WBRC-N04-LOCAL-BISIMULATION-NOT-NECESSARY",
    "WBRC-N05-GENERAL-SCC-NOT-PROMOTED",
}
EXPECTED_API = {
    "CWMState",
    "cwm_edge",
    "cwm_recoalesce",
    "cwm_propagate",
    "cwm_from_positive_weights",
    "is_positive_path_realizable",
    "boolean_support",
    "effective_multiplicity",
    "multiplicity_surplus_expr",
    "future_cwm_equivalent",
    "projective_scale",
    "gauge_scale",
    "compensate_incoming_weight",
    "OneStateRecurrentCWM",
    "one_state_recurrent_cwm",
}


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def public_symbols(path: Path) -> set[str]:
    tree = ast.parse(path.read_text(encoding="utf-8"))
    result: set[str] = set()
    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.ClassDef)) and not node.name.startswith("_"):
            result.add(node.name)
    return result


def main() -> int:
    substrate = load_json(SUBSTRATE)
    ledger = load_json(LEDGER)
    addendum = load_json(METHOD_ADDENDUM)
    foundation = FOUNDATION.read_text(encoding="utf-8")
    free_router = FREE_ROUTER.read_text(encoding="utf-8")
    current_router = CURRENT_ROUTER.read_text(encoding="utf-8")

    assert substrate["status"] == "ACTIVE_USER_PROMOTED_ALL_RESEARCH_FOUNDATION"
    assert set(substrate["scope"]) == {
        "FREE_AXIOM_DISCOVERY_PHASE_A",
        "FREE_AXIOM_DISCOVERY_PHASE_B",
        "TASK_RESEARCH",
        "RESEARCH_DRIVER",
        "FOUNDATION_STEWARD",
    }
    assert substrate["theorem_ledger"].endswith(LEDGER.name)
    assert substrate["tool_method_id"] == "t0.weighted_brc_cwm"

    theorem_ids = [item["id"] for item in ledger["theorems"]]
    negative_ids = [item["id"] for item in ledger["negative_boundaries"]]
    assert len(theorem_ids) == len(set(theorem_ids))
    assert len(negative_ids) == len(set(negative_ids))
    assert set(theorem_ids) == EXPECTED_THEOREMS
    assert set(negative_ids) == EXPECTED_NEGATIVE

    methods = addendum["methods"]
    assert len(methods) == 1
    method = methods[0]
    assert method["method_id"] == "t0.weighted_brc_cwm"
    assert method["family_id"] == "T0_BRC"
    assert method["classification"] == "GLOBAL_SUBTOOL"
    assert EXPECTED_API <= set(method["api"])
    assert EXPECTED_API <= public_symbols(TOOL_MODULE)

    required_refs = [
        "ENTERPRISE_BRC_WEIGHTED_GLOBAL_SUBSTRATE_20260902.json",
        "ENTERPRISE_BRC_WEIGHTED_LOG_THEOREM_LEDGER_20260902.json",
        "t0.weighted_brc_cwm",
    ]
    for ref in required_refs:
        assert ref in foundation
        assert ref in current_router
    assert "ENTERPRISE_BRC_WEIGHTED_GLOBAL_SUBSTRATE_20260902.json" in free_router
    assert "GLOBAL_BRANCH_TYPING != SUGGESTED_BRC_QUESTION" in free_router
    assert "DETERMINISTIC_SINGLE_PATH -> DELTA=0" in foundation
    assert "POSITIVE_WEIGHTED_BRC != SIGNED_AMPLITUDE_CANCELLATION" in foundation

    print("Weighted-BRC global Foundation integrity: PASS")
    print(f"theorems={len(theorem_ids)} negative_boundaries={len(negative_ids)} method={method['method_id']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
