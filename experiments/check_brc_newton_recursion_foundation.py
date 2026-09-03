#!/usr/bin/env python3
"""Integrity checks for the WBRC-T52/T53 Newton-recursion Foundation addendum."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

FOUNDATION = ROOT / "definitions/ENTERPRISE_BRC_NEWTON_RECURSION_FOUNDATION_20260904.md"
LEDGER = ROOT / "definitions/ENTERPRISE_BRC_NEWTON_RECURSION_THEOREM_LEDGER_20260904.json"
SUBSTRATE = ROOT / "definitions/ENTERPRISE_BRC_WEIGHTED_GLOBAL_SUBSTRATE_20260902.json"
METHOD = ROOT / "research_method_inventory_addenda/20260904_brc_newton_recursion_foundation.json"
SOURCE = ROOT / "src/enterprise_math/brc_newton_recursion.py"

THEOREMS = {
    "WBRC-T52-RATIONAL-ROOT-NEWTON-RECURSION-CLOSURE",
    "WBRC-T53-SELECTED-ROOT-EVALUATION-ALGEBRA",
}
NEGATIVES = {
    "WBRC-N36-RATIONAL-VALUATION-SCALE-NOT-FLOATING-RADICAL",
    "WBRC-N37-OLD-CATALOG-ZERO-NOT-NONEXISTENCE",
    "WBRC-N38-POLYNOMIAL-REPRESENTATIVE-NONZERO-NOT-ROOT-VALUE-NONZERO",
    "WBRC-N39-SELECTED-ROOT-EVALUATION-NOT-MINIMAL-FIELD",
    "WBRC-N40-NO-GENERAL-INVERSION-OR-COMPLETE-PUISEUX",
    "WBRC-N41-IRRATIONAL-TRANSLATED-ROOT-MULTIGENERATOR-FRONTIER",
}
PUBLIC_API = {
    "RationalValuationScale",
    "SelectedRootEvaluationAlgebra",
    "RationalNewtonStep",
    "SelectedRootNewtonStep",
    "rational_newton_step",
    "selected_root_first_newton_step",
    "selected_root_rational_newton_step",
    "selected_root_polynomial_vanish_order",
}


def main() -> int:
    foundation = FOUNDATION.read_text()
    ledger = json.loads(LEDGER.read_text())
    substrate = json.loads(SUBSTRATE.read_text())
    method = json.loads(METHOD.read_text())
    source = SOURCE.read_text()

    theorem_ids = {item["id"] for item in ledger["theorems"]}
    negative_ids = {item["id"] for item in ledger["negative_boundaries"]}
    assert theorem_ids == THEOREMS
    assert negative_ids == NEGATIVES
    assert ledger["tool_method_id"] == "t0.weighted_brc_newton_recursion"

    assert "WBRC-T52" in foundation and "WBRC-T53" in foundation
    assert "SEMANTIC ZERO TEST MUST PRECEDE NEWTON SCALE ORDERING" in foundation
    assert "IRRATIONAL_TRANSLATED_ROOT" in foundation
    assert "verified 66 targeted second-edge BRC families" in foundation
    assert "22 irrational-base block families" in foundation

    assert substrate["newton_recursion_foundation"].endswith(
        "ENTERPRISE_BRC_NEWTON_RECURSION_FOUNDATION_20260904.md"
    )
    assert any(
        item.endswith("ENTERPRISE_BRC_NEWTON_RECURSION_THEOREM_LEDGER_20260904.json")
        for item in substrate["theorem_ledger_addenda"]
    )
    assert "t0.weighted_brc_newton_recursion" in substrate["tool_method_addenda"]
    assert "src/enterprise_math/brc_newton_recursion.py" in substrate["tool_module_addenda"]
    commitments = "\n".join(substrate["commitments"])
    assert "semantic zero testing must precede scale ordering" in commitments.lower()
    assert "irrational translated root" in commitments.lower()

    methods = method["methods"]
    assert len(methods) == 1
    assert methods[0]["method_id"] == "t0.weighted_brc_newton_recursion"
    assert methods[0]["parent_method"] if "parent_method" in methods[0] else method["parent_method"] == "T0_BRC"
    assert methods[0]["implementation"] == "src/enterprise_math/brc_newton_recursion.py"

    assert "__all__" in source
    for name in PUBLIC_API:
        assert name in source, name

    print("BRC Newton recursion Foundation integrity: PASS")
    print(f"theorems={len(THEOREMS)}")
    print(f"negative_boundaries={len(NEGATIVES)}")
    print(f"public_api={len(PUBLIC_API)}")
    print("method=t0.weighted_brc_newton_recursion")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
