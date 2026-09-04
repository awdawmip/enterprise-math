#!/usr/bin/env python3
"""Integrity checks for WBRC-T62 non-split quadratic selector Foundation."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FOUNDATION = ROOT / "definitions/ENTERPRISE_BRC_NEWTON_QUADRATIC_SELECTOR_FOUNDATION_20260904.md"
LEDGER = ROOT / "definitions/ENTERPRISE_BRC_NEWTON_QUADRATIC_SELECTOR_THEOREM_LEDGER_20260904.json"
SUBSTRATE = ROOT / "definitions/ENTERPRISE_BRC_WEIGHTED_GLOBAL_SUBSTRATE_20260902.json"
METHOD = ROOT / "research_method_inventory_addenda/20260904_brc_newton_quadratic_selector_foundation.json"
SOURCE = ROOT / "src/enterprise_math/brc_newton_quadratic_selector.py"

THEOREMS = {"WBRC-T62-NONSPLIT-MONIC-QUADRATIC-SMALLEST-REAL-SELECTOR-CHAMBER"}
NEGATIVES = {
    "WBRC-N76-MONIC-QUADRATIC-COFACTOR-ONLY",
    "WBRC-N77-SMALLEST-REAL-ONLY",
    "WBRC-N78-FIXED-MULTIPLICITY-REQUIRES-R-NONZERO",
    "WBRC-N79-DISCRIMINANT-ZERO-NOT-AUTOMATIC-SELECTOR-CHANGE",
    "WBRC-N80-NO-ROOT-MATERIALIZATION-NOT-FACTORING-ALGORITHM",
    "WBRC-N81-QUADRATIC-CLOSED-FORM-NOT-GENERAL-PARAMETRIC-STURM",
    "WBRC-N82-AFFINE-COEFFICIENT-FAMILY-NOT-ARBITRARY-NONLINEAR-PARAMETERIZATION",
    "WBRC-N83-T62-NOT-COMPLETE-PUISEUX-OR-MULTIGENERATOR-SOLVER",
}
PUBLIC_API = {
    "QuadraticSelectorState",
    "AffineQuadraticSelectorFamily",
    "quadratic_selector_state",
    "quadratic_fixed_multiplicity",
    "quadratic_smallest_real_selected",
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

    assert "WBRC-T62" in foundation
    assert "R!=0 AND [D<0 OR (L>0 AND R>0)]" in foundation
    assert "L^2-D=(-a-2r)^2-(a^2-4b)=4(r^2+ar+b)=4R" in foundation
    assert "D=0 is not by itself a selector boundary" in foundation

    assert substrate["newton_quadratic_selector_foundation"].endswith(
        "ENTERPRISE_BRC_NEWTON_QUADRATIC_SELECTOR_FOUNDATION_20260904.md"
    )
    assert any(
        item.endswith("ENTERPRISE_BRC_NEWTON_QUADRATIC_SELECTOR_THEOREM_LEDGER_20260904.json")
        for item in substrate["theorem_ledger_addenda"]
    )
    assert "t0.weighted_brc_newton_quadratic_selector" in substrate["tool_method_addenda"]
    assert "src/enterprise_math/brc_newton_quadratic_selector.py" in substrate["tool_module_addenda"]
    commitments = "\n".join(substrate["commitments"]).lower()
    assert "newton_nonsplit_quadratic_selector_is_dlr_typed" in commitments
    assert "does not imply smallest-positive or general parametric sturm chambers" in commitments

    methods = method["methods"]
    assert len(methods) == 1
    entry = methods[0]
    assert entry["method_id"] == "t0.weighted_brc_newton_quadratic_selector"
    assert entry["family_id"] == "T0_BRC"
    assert entry["implementation"] == "src/enterprise_math/brc_newton_quadratic_selector.py"
    assert "quadratic selector chamber" in entry["triggers"]
    assert "smallest real quadratic selector" in entry["triggers"]

    assert "__all__" in source
    for name in PUBLIC_API:
        assert name in source, name

    print("BRC Newton quadratic selector Foundation integrity: PASS")
    print(f"theorems={len(THEOREMS)}")
    print(f"negative_boundaries={len(NEGATIVES)}")
    print(f"public_api={len(PUBLIC_API)}")
    print("method=t0.weighted_brc_newton_quadratic_selector")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
