#!/usr/bin/env python3
"""Integrity checks for the WBRC-T57/T58 Newton observer-lattice Foundation."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FOUNDATION = ROOT / "definitions/ENTERPRISE_BRC_NEWTON_OBSERVER_LATTICE_FOUNDATION_20260904.md"
LEDGER = ROOT / "definitions/ENTERPRISE_BRC_NEWTON_OBSERVER_LATTICE_THEOREM_LEDGER_20260904.json"
SUBSTRATE = ROOT / "definitions/ENTERPRISE_BRC_WEIGHTED_GLOBAL_SUBSTRATE_20260902.json"
METHOD = ROOT / "research_method_inventory_addenda/20260904_brc_newton_observer_lattice_foundation.json"
SOURCE = ROOT / "src/enterprise_math/brc_newton_observer_lattice.py"

THEOREMS = {
    "WBRC-T57-COORDINATE-OBSERVER-KERNEL-ANTI-LATTICE",
    "WBRC-T58-FROZEN-NEWTON-FINITE-HORIZON-OBSERVABILITY",
}
NEGATIVES = {
    "WBRC-N54-FULL-RESIDUAL-NOT-UNIVERSAL-OBSERVER",
    "WBRC-N55-EDGE-ONLY-NOT-FULL-RESIDUAL",
    "WBRC-N56-COORDINATE-LATTICE-NOT-ALL-NONLINEAR-OBSERVERS",
    "WBRC-N57-FROZEN-SCHEDULE-NOT-AUTONOMOUS-SELECTION",
    "WBRC-N58-LONGER-HORIZON-NOT-COARSER",
    "WBRC-N59-SCHEDULED-LINEARITY-NOT-CHAMBER-STABILITY",
    "WBRC-N60-TAYLOR-PROVENANCE-NOT-BRANCH-PROVENANCE",
}
PUBLIC_API = {
    "NewtonCoordinateObserver",
    "FrozenNewtonScheduleStep",
    "FrozenNewtonObservabilityAnalysis",
    "full_coordinate_observer",
    "edge_coordinate_observer",
    "coordinate_observer_signature",
    "coordinate_observer_equivalent",
    "coordinate_observer_kernel_dimension",
    "frozen_newton_substitution",
    "residual_edge_signature",
    "frozen_horizon_edge_signature",
    "frozen_horizon_observability_analysis",
    "frozen_horizon_rank_profile",
    "frozen_horizon_kernel_profile",
}


def main() -> int:
    foundation = FOUNDATION.read_text()
    ledger = json.loads(LEDGER.read_text())
    substrate = json.loads(SUBSTRATE.read_text())
    method = json.loads(METHOD.read_text())
    source = SOURCE.read_text()

    assert {item["id"] for item in ledger["theorems"]} == THEOREMS
    assert {item["id"] for item in ledger["negative_boundaries"]} == NEGATIVES
    assert ledger["tool_method_id"] == "t0.weighted_brc_newton_observer_lattice"

    assert "WBRC-T57" in foundation and "WBRC-T58" in foundation
    assert "K_(O1 union O2) = K_O1 intersection K_O2" in foundation
    assert "K_(h+1) subset K_h" in foundation
    assert "AUTONOMOUS NEWTON CHAMBER STABILITY" not in foundation
    assert "AUTONOMOUSLY RESELECT ROOT/MULTIPLICITY/SCALE" in foundation

    assert substrate["newton_observer_lattice_foundation"].endswith(
        "ENTERPRISE_BRC_NEWTON_OBSERVER_LATTICE_FOUNDATION_20260904.md"
    )
    assert any(
        item.endswith("ENTERPRISE_BRC_NEWTON_OBSERVER_LATTICE_THEOREM_LEDGER_20260904.json")
        for item in substrate["theorem_ledger_addenda"]
    )
    assert "t0.weighted_brc_newton_observer_lattice" in substrate["tool_method_addenda"]
    assert "src/enterprise_math/brc_newton_observer_lattice.py" in substrate["tool_module_addenda"]
    commitments = "\n".join(substrate["commitments"]).lower()
    assert "safe newton compression is relative to the declared residual observer" in commitments
    assert "does not certify autonomous schedule stability" in commitments

    methods = method["methods"]
    assert len(methods) == 1
    entry = methods[0]
    assert entry["method_id"] == "t0.weighted_brc_newton_observer_lattice"
    assert entry["family_id"] == "T0_BRC"
    assert entry["implementation"] == "src/enterprise_math/brc_newton_observer_lattice.py"
    assert "newton observer lattice" in entry["triggers"]
    assert "frozen newton schedule" in entry["triggers"]

    assert "__all__" in source
    for name in PUBLIC_API:
        assert name in source, name

    print("BRC Newton observer lattice Foundation integrity: PASS")
    print(f"theorems={len(THEOREMS)}")
    print(f"negative_boundaries={len(NEGATIVES)}")
    print(f"public_api={len(PUBLIC_API)}")
    print("method=t0.weighted_brc_newton_observer_lattice")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
