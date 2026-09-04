#!/usr/bin/env python3
"""Integrity checks for WBRC-T59 affine Newton schedule strata Foundation."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FOUNDATION = ROOT / "definitions/ENTERPRISE_BRC_NEWTON_SCHEDULE_STRATA_FOUNDATION_20260904.md"
LEDGER = ROOT / "definitions/ENTERPRISE_BRC_NEWTON_SCHEDULE_STRATA_THEOREM_LEDGER_20260904.json"
SUBSTRATE = ROOT / "definitions/ENTERPRISE_BRC_WEIGHTED_GLOBAL_SUBSTRATE_20260902.json"
METHOD = ROOT / "research_method_inventory_addenda/20260904_brc_newton_schedule_strata_foundation.json"
SOURCE = ROOT / "src/enterprise_math/brc_newton_schedule_strata.py"

THEOREMS = {"WBRC-T59-AFFINE-CONSTRUCTIBLE-NEWTON-SCHEDULE-VALIDITY"}
NEGATIVES = {
    "WBRC-N61-CONSTRUCTIBLE-STRATUM-NOT-OPEN-STABILITY-NEIGHBORHOOD",
    "WBRC-N62-DECLARED-ROOT-VALIDITY-NOT-GLOBAL-SELECTOR-STABILITY",
    "WBRC-N63-AFFINE-RATIONAL-FAMILY-NOT-ARBITRARY-NONLINEAR-PARAMETERIZATION",
    "WBRC-N64-RATIONAL-DECLARED-ROOTS-NOT-GENERAL-MULTIGENERATOR-ALGEBRAIC-ROOTS",
    "WBRC-N65-FINITE-SCHEDULE-VALIDITY-NOT-COMPLETE-PUISEUX-SOLVER",
    "WBRC-N66-CONSTRUCTIBLE-STRATUM-NOT-NECESSARILY-CONVEX-OR-OPEN",
    "WBRC-N67-AFFINE-CHARACTERISTIC-CANCELLATION-NOT-SIGNED-BRANCH-MASS",
}
PUBLIC_API = {
    "RationalAffineForm",
    "AffinePolynomial",
    "AffineNewtonLayer",
    "AffineRootMultiplicityConstraints",
    "affine_taylor_form",
    "affine_contact_order",
    "affine_selected_newton_scale",
    "affine_edge_polynomial",
    "affine_root_multiplicity_constraints",
    "affine_first_newton_residual",
    "affine_scheduled_newton_substitution",
    "evaluate_affine_layers",
    "evaluate_affine_state",
}


def main() -> int:
    foundation = FOUNDATION.read_text()
    ledger = json.loads(LEDGER.read_text())
    substrate = json.loads(SUBSTRATE.read_text())
    method = json.loads(METHOD.read_text())
    source = SOURCE.read_text()

    assert {item["id"] for item in ledger["theorems"]} == THEOREMS
    assert {item["id"] for item in ledger["negative_boundaries"]} == NEGATIVES
    assert ledger["tool_method_id"] == "t0.weighted_brc_newton_schedule_strata"

    assert "WBRC-T59" in foundation
    assert "finite Boolean combination of rational affine equalities and non-equalities" in foundation
    assert "DECLARED_ROOT_VALIDITY != GLOBAL_ROOT_SELECTOR_STABILITY" in foundation
    assert "u=0, v=1, w=1" in foundation

    assert substrate["newton_schedule_strata_foundation"].endswith(
        "ENTERPRISE_BRC_NEWTON_SCHEDULE_STRATA_FOUNDATION_20260904.md"
    )
    assert any(
        item.endswith("ENTERPRISE_BRC_NEWTON_SCHEDULE_STRATA_THEOREM_LEDGER_20260904.json")
        for item in substrate["theorem_ledger_addenda"]
    )
    assert "t0.weighted_brc_newton_schedule_strata" in substrate["tool_method_addenda"]
    assert "src/enterprise_math/brc_newton_schedule_strata.py" in substrate["tool_module_addenda"]
    commitments = "\n".join(substrate["commitments"]).lower()
    assert "newton_affine_schedule_validity_is_constructible" in commitments
    assert "does not certify stability of a global root-selector rule" in commitments

    methods = method["methods"]
    assert len(methods) == 1
    entry = methods[0]
    assert entry["method_id"] == "t0.weighted_brc_newton_schedule_strata"
    assert entry["family_id"] == "T0_BRC"
    assert entry["implementation"] == "src/enterprise_math/brc_newton_schedule_strata.py"
    assert "constructible schedule" in entry["triggers"]
    assert "declared root validity" in entry["triggers"]

    assert "__all__" in source
    for name in PUBLIC_API:
        assert name in source, name

    print("BRC Newton schedule strata Foundation integrity: PASS")
    print(f"theorems={len(THEOREMS)}")
    print(f"negative_boundaries={len(NEGATIVES)}")
    print(f"public_api={len(PUBLIC_API)}")
    print("method=t0.weighted_brc_newton_schedule_strata")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
