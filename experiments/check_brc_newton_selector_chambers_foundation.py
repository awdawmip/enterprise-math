#!/usr/bin/env python3
"""Integrity checks for WBRC-T60/T61 split-affine selector chambers Foundation."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FOUNDATION = ROOT / "definitions/ENTERPRISE_BRC_NEWTON_SELECTOR_CHAMBERS_FOUNDATION_20260904.md"
LEDGER = ROOT / "definitions/ENTERPRISE_BRC_NEWTON_SELECTOR_CHAMBERS_THEOREM_LEDGER_20260904.json"
SUBSTRATE = ROOT / "definitions/ENTERPRISE_BRC_WEIGHTED_GLOBAL_SUBSTRATE_20260902.json"
METHOD = ROOT / "research_method_inventory_addenda/20260904_brc_newton_selector_chambers_foundation.json"
SOURCE = ROOT / "src/enterprise_math/brc_newton_selector_chambers.py"

THEOREMS = {
    "WBRC-T60-COMPLETE-SPLIT-AFFINE-SMALLEST-REAL-SELECTOR-CHAMBER",
    "WBRC-T61-COMPLETE-SPLIT-AFFINE-SMALLEST-POSITIVE-SELECTOR-CHAMBER",
}
NEGATIVES = {
    "WBRC-N68-COMPLETE-SPLIT-AFFINE-CERTIFICATE-REQUIRED",
    "WBRC-N69-SPLIT-SELECTOR-CHAMBER-NOT-GENERAL-PARAMETRIC-STURM",
    "WBRC-N70-SELECTOR-VALUE-STABILITY-NOT-MULTIPLICITY-STABILITY",
    "WBRC-N71-SMALLEST-REAL-NOT-SMALLEST-POSITIVE",
    "WBRC-N72-ZERO-ROOT-NOT-POSITIVE",
    "WBRC-N73-AFFINE-ROOT-BRANCHES-NOT-AFFINE-POLYNOMIAL-COEFFICIENTS",
    "WBRC-N74-SELECTOR-CHAMBER-DOES-NOT-REPLACE-T59-SCHEDULE-VALIDITY",
    "WBRC-N75-SPLIT-SELECTOR-CERTIFICATE-NOT-COMPLETE-PUISEUX-OR-MULTIGENERATOR-SOLVER",
}
PUBLIC_API = {
    "SplitAffineRootBranch",
    "SplitAffineRootCertificate",
    "AffineOrderAtom",
    "AffineOrderClause",
    "SplitAffineSelectorChamber",
    "split_affine_fixed_multiplicity_holds",
    "split_affine_smallest_real_chamber",
    "split_affine_smallest_positive_chamber",
    "split_affine_smallest_real_selected",
    "split_affine_smallest_positive_selected",
    "split_affine_materialize_monic_polynomial",
    "split_affine_matches_polynomial",
}


def main() -> int:
    foundation = FOUNDATION.read_text()
    ledger = json.loads(LEDGER.read_text())
    substrate = json.loads(SUBSTRATE.read_text())
    method = json.loads(METHOD.read_text())
    source = SOURCE.read_text()

    assert {item["id"] for item in ledger["theorems"]} == THEOREMS
    assert {item["id"] for item in ledger["negative_boundaries"]} == NEGATIVES
    assert ledger["tool_method_id"] == "t0.weighted_brc_newton_selector_chambers"

    assert "WBRC-T60" in foundation and "WBRC-T61" in foundation
    assert "h_j(lambda)>r" in foundation
    assert "h_j(lambda)<=0 OR h_j(lambda)>r" in foundation
    assert "ZERO_ROOT_IS_NOT_POSITIVE" in foundation

    assert substrate["newton_selector_chambers_foundation"].endswith(
        "ENTERPRISE_BRC_NEWTON_SELECTOR_CHAMBERS_FOUNDATION_20260904.md"
    )
    assert any(
        item.endswith("ENTERPRISE_BRC_NEWTON_SELECTOR_CHAMBERS_THEOREM_LEDGER_20260904.json")
        for item in substrate["theorem_ledger_addenda"]
    )
    assert "t0.weighted_brc_newton_selector_chambers" in substrate["tool_method_addenda"]
    assert "src/enterprise_math/brc_newton_selector_chambers.py" in substrate["tool_module_addenda"]
    commitments = "\n".join(substrate["commitments"]).lower()
    assert "newton_split_selector_stability_is_order_typed" in commitments
    assert "no general non-split parametric sturm chamber is implied" in commitments

    methods = method["methods"]
    assert len(methods) == 1
    entry = methods[0]
    assert entry["method_id"] == "t0.weighted_brc_newton_selector_chambers"
    assert entry["family_id"] == "T0_BRC"
    assert entry["implementation"] == "src/enterprise_math/brc_newton_selector_chambers.py"
    assert "smallest real root stability" in entry["triggers"]
    assert "smallest positive root stability" in entry["triggers"]

    assert "__all__" in source
    for name in PUBLIC_API:
        assert name in source, name

    print("BRC Newton selector chambers Foundation integrity: PASS")
    print(f"theorems={len(THEOREMS)}")
    print(f"negative_boundaries={len(NEGATIVES)}")
    print(f"public_api={len(PUBLIC_API)}")
    print("method=t0.weighted_brc_newton_selector_chambers")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
