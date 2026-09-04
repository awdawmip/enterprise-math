#!/usr/bin/env python3
"""Integrity checks for WBRC-T63 quadratic smallest-positive selector Foundation."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FOUNDATION = ROOT / "definitions/ENTERPRISE_BRC_NEWTON_QUADRATIC_POSITIVE_SELECTOR_FOUNDATION_20260904.md"
LEDGER = ROOT / "definitions/ENTERPRISE_BRC_NEWTON_QUADRATIC_POSITIVE_SELECTOR_THEOREM_LEDGER_20260904.json"
SUBSTRATE = ROOT / "definitions/ENTERPRISE_BRC_WEIGHTED_GLOBAL_SUBSTRATE_20260902.json"
METHOD = ROOT / "research_method_inventory_addenda/20260904_brc_newton_quadratic_selector_foundation.json"
SOURCE = ROOT / "src/enterprise_math/brc_newton_quadratic_selector.py"

THEOREMS = {"WBRC-T63-NONSPLIT-MONIC-QUADRATIC-SMALLEST-POSITIVE-SELECTOR-CHAMBER"}
NEGATIVES = {
    "WBRC-N84-SMALLEST-POSITIVE-NOT-SMALLEST-REAL",
    "WBRC-N85-ZERO-ROOT-NOT-POSITIVE",
    "WBRC-N86-FIXED-SELECTOR-VALUE-NOT-FIXED-MULTIPLICITY-AT-R-ZERO",
    "WBRC-N87-OPEN-INTERVAL-SEMANTICS-ARE-ESSENTIAL",
    "WBRC-N88-MONIC-QUADRATIC-COFACTOR-ONLY",
    "WBRC-N89-DEGREE-TWO-STURM-VARIATION-NOT-GENERAL-PARAMETRIC-CAD",
    "WBRC-N90-COMPACT-CHAMBER-IS-DEGREE-TWO-SPECIALIZATION",
    "WBRC-N91-T63-NOT-COMPLETE-PUISEUX-OR-MULTIGENERATOR-SOLVER",
}
PUBLIC_API = {
    "QuadraticSelectorState",
    "AffineQuadraticSelectorFamily",
    "quadratic_sturm_variation",
    "quadratic_selector_state",
    "quadratic_fixed_multiplicity",
    "quadratic_smallest_real_selected",
    "quadratic_positive_interval_root_count",
    "quadratic_smallest_positive_selected",
    "quadratic_smallest_positive_compact_selected",
    "evaluate_affine_quadratic_selector",
}


def main() -> int:
    foundation = FOUNDATION.read_text()
    ledger = json.loads(LEDGER.read_text())
    substrate = json.loads(SUBSTRATE.read_text())
    method = json.loads(METHOD.read_text())
    source = SOURCE.read_text()

    assert {item["id"] for item in ledger["theorems"]} == THEOREMS
    assert {item["id"] for item in ledger["negative_boundaries"]} == NEGATIVES
    assert ledger["tool_method_id"] == "t0.weighted_brc_newton_quadratic_selector"

    assert "WBRC-T63" in foundation
    assert "N_(0,r)=V(b,a,D)-V(R,2r+a,D)" in foundation
    assert "b*R>=0" in foundation
    assert "ZERO_ROOT_IS_NOT_POSITIVE" in foundation
    assert "The Sturm-variation form is canonical for future degree extensions" in foundation

    assert substrate["newton_quadratic_positive_selector_foundation"].endswith(
        "ENTERPRISE_BRC_NEWTON_QUADRATIC_POSITIVE_SELECTOR_FOUNDATION_20260904.md"
    )
    assert any(
        item.endswith("ENTERPRISE_BRC_NEWTON_QUADRATIC_POSITIVE_SELECTOR_THEOREM_LEDGER_20260904.json")
        for item in substrate["theorem_ledger_addenda"]
    )
    assert "t0.weighted_brc_newton_quadratic_selector" in substrate["tool_method_addenda"]
    assert "src/enterprise_math/brc_newton_quadratic_selector.py" in substrate["tool_module_addenda"]
    commitments = "\n".join(substrate["commitments"]).lower()
    assert "newton_nonsplit_quadratic_positive_selector_is_interval_typed" in commitments
    assert "open interval (0,r)" in commitments

    methods = method["methods"]
    assert len(methods) == 1
    entry = methods[0]
    assert entry["method_id"] == "t0.weighted_brc_newton_quadratic_selector"
    assert entry["implementation"] == "src/enterprise_math/brc_newton_quadratic_selector.py"
    assert entry["extension_foundation"].endswith(
        "ENTERPRISE_BRC_NEWTON_QUADRATIC_POSITIVE_SELECTOR_FOUNDATION_20260904.md"
    )
    assert "smallest positive quadratic selector" in entry["triggers"]
    assert "quadratic sturm variation" in entry["triggers"]

    assert "__all__" in source
    for name in PUBLIC_API:
        assert name in source, name

    print("BRC Newton quadratic positive selector Foundation integrity: PASS")
    print(f"theorems={len(THEOREMS)}")
    print(f"negative_boundaries={len(NEGATIVES)}")
    print(f"public_api={len(PUBLIC_API)}")
    print("method=t0.weighted_brc_newton_quadratic_selector")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
