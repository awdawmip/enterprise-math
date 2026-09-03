#!/usr/bin/env python3
"""Integrity checks for WBRC-T56 Newton fiber quotient Foundation."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FOUNDATION = ROOT / "definitions/ENTERPRISE_BRC_NEWTON_FIBER_QUOTIENT_FOUNDATION_20260904.md"
LEDGER = ROOT / "definitions/ENTERPRISE_BRC_NEWTON_FIBER_QUOTIENT_THEOREM_LEDGER_20260904.json"
SUBSTRATE = ROOT / "definitions/ENTERPRISE_BRC_WEIGHTED_GLOBAL_SUBSTRATE_20260902.json"
METHOD = ROOT / "research_method_inventory_addenda/20260904_brc_newton_fiber_quotient_foundation.json"
SOURCE = ROOT / "src/enterprise_math/brc_newton_fiber_quotient.py"

THEOREMS = {"WBRC-T56-NEWTON-RESIDUAL-FIBER-SUM-OPERATION-SAFE-QUOTIENT"}
NEGATIVES = {
    "WBRC-N48-FULL-RESIDUAL-MINIMALITY-IS-OBSERVER-SPECIFIC",
    "WBRC-N49-RESIDUAL-QUOTIENT-DOES-NOT-RECOVER-SOURCE-PROVENANCE",
    "WBRC-N50-DIFFERENT-RESIDUAL-SCALES-DO-NOT-MERGE",
    "WBRC-N51-DIFFERENT-TAYLOR-DEGREES-DO-NOT-MERGE",
    "WBRC-N52-ALGEBRAIC-COEFFICIENT-CANCELLATION-NOT-SIGNED-BRANCH-MASS",
    "WBRC-N53-T6-PRINCIPLE-REUSE-NOT-T6-EXECUTABLE-REUSE",
}
PUBLIC_API = {
    "NewtonFiberPosition",
    "NewtonFiberCoordinate",
    "NewtonFiberClass",
    "NewtonFiberQuotientAnalysis",
    "newton_fiber_coordinate",
    "newton_fiber_quotient_analysis",
    "newton_fiber_sum_signature",
    "newton_fiber_equivalent",
    "newton_fiber_edge_signature",
    "apply_newton_fiber_transfer",
}


def main() -> int:
    foundation = FOUNDATION.read_text()
    ledger = json.loads(LEDGER.read_text())
    substrate = json.loads(SUBSTRATE.read_text())
    method = json.loads(METHOD.read_text())
    source = SOURCE.read_text()

    assert {item["id"] for item in ledger["theorems"]} == THEOREMS
    assert {item["id"] for item in ledger["negative_boundaries"]} == NEGATIVES
    assert ledger["tool_method_id"] == "t0.weighted_brc_newton_fiber_quotient"

    assert "WBRC-T56" in foundation
    assert "Q^I/" in foundation or "mathbb Q^I" in foundation
    assert "coarsest exact quotient" in foundation
    assert "edge-only" in foundation.lower()
    assert "T6" in foundation

    assert substrate["newton_fiber_quotient_foundation"].endswith(
        "ENTERPRISE_BRC_NEWTON_FIBER_QUOTIENT_FOUNDATION_20260904.md"
    )
    assert any(
        item.endswith("ENTERPRISE_BRC_NEWTON_FIBER_QUOTIENT_THEOREM_LEDGER_20260904.json")
        for item in substrate["theorem_ledger_addenda"]
    )
    assert "t0.weighted_brc_newton_fiber_quotient" in substrate["tool_method_addenda"]
    assert "src/enterprise_math/brc_newton_fiber_quotient.py" in substrate["tool_module_addenda"]
    commitments = "\n".join(substrate["commitments"]).lower()
    assert "complete residual newton jet" in commitments
    assert "different rho or different k remain distinct" in commitments

    methods = method["methods"]
    assert len(methods) == 1
    entry = methods[0]
    assert entry["method_id"] == "t0.weighted_brc_newton_fiber_quotient"
    assert entry["family_id"] == "T0_BRC"
    assert entry["implementation"] == "src/enterprise_math/brc_newton_fiber_quotient.py"
    assert "newton fiber quotient" in entry["triggers"]
    assert "operation safe quotient" in entry["triggers"]
    assert any("T6" in item for item in entry["reuse"])

    assert "__all__" in source
    for name in PUBLIC_API:
        assert name in source, name

    print("BRC Newton fiber quotient Foundation integrity: PASS")
    print(f"theorems={len(THEOREMS)}")
    print(f"negative_boundaries={len(NEGATIVES)}")
    print(f"public_api={len(PUBLIC_API)}")
    print("method=t0.weighted_brc_newton_fiber_quotient")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
