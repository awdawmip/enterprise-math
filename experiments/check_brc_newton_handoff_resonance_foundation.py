#!/usr/bin/env python3
"""Integrity checks for WBRC-T54/T55 Newton handoff/resonance Foundation."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FOUNDATION = ROOT / "definitions/ENTERPRISE_BRC_NEWTON_HANDOFF_RESONANCE_FOUNDATION_20260904.md"
LEDGER = ROOT / "definitions/ENTERPRISE_BRC_NEWTON_HANDOFF_RESONANCE_THEOREM_LEDGER_20260904.json"
SUBSTRATE = ROOT / "definitions/ENTERPRISE_BRC_WEIGHTED_GLOBAL_SUBSTRATE_20260902.json"
METHOD = ROOT / "research_method_inventory_addenda/20260904_brc_newton_handoff_resonance_foundation.json"
SOURCE = ROOT / "src/enterprise_math/brc_newton_handoff.py"

THEOREMS = {
    "WBRC-T54-SINGLE-GENERATOR-IRRATIONAL-TRANSLATED-ROOT-HANDOFF",
    "WBRC-T55-AFFINE-NEWTON-SCALE-PUSHFORWARD-RESONANCE",
}
NEGATIVES = {
    "WBRC-N42-IRRATIONAL-TRANSLATED-ROOT-NOT-AUTOMATIC-MULTIGENERATOR",
    "WBRC-N43-HANDOFF-CANNOT-DISCARD-LIVE-OLD-ALGEBRAIC-DATA",
    "WBRC-N44-ABSORPTION-CERTIFICATE-NOT-ROOT-EXPRESSION-SEARCH",
    "WBRC-N45-NEWTON-RESONANCE-NOT-SIGNED-BRANCH-INTERFERENCE",
    "WBRC-N46-RESIDUAL-NEWTON-JET-LOSES-SOURCE-PROVENANCE",
    "WBRC-N47-GENERAL-REAL-ROOT-SELECTOR-NOT-T41-REPLACEMENT",
}
PUBLIC_API = {
    "RealRootSelector",
    "RealRootEvaluationAlgebra",
    "RealRootNewtonStep",
    "real_root_handoff_step",
    "real_root_rational_newton_step",
    "real_root_polynomial_vanish_order",
    "evaluate_at_coefficient",
    "verify_absorbed_root_zero",
    "NewtonPushforwardAtom",
    "NewtonResonanceFiber",
    "NewtonPushforwardAnalysis",
    "newton_atoms_resonate",
    "rational_newton_pushforward",
}


def main() -> int:
    foundation = FOUNDATION.read_text()
    ledger = json.loads(LEDGER.read_text())
    substrate = json.loads(SUBSTRATE.read_text())
    method = json.loads(METHOD.read_text())
    source = SOURCE.read_text()

    assert {item["id"] for item in ledger["theorems"]} == THEOREMS
    assert {item["id"] for item in ledger["negative_boundaries"]} == NEGATIVES
    assert ledger["tool_method_id"] == "t0.weighted_brc_newton_handoff_resonance"

    assert "WBRC-T54" in foundation and "WBRC-T55" in foundation
    assert "Taylor expansion" in foundation and "equal-scale aggregation" in foundation
    assert "22 irrational-translated-root" in foundation
    assert "576 synthetic Newton samples" in foundation
    assert "tau_2=1/4" in foundation and "tau_2=3/10" in foundation

    assert substrate["newton_handoff_resonance_foundation"].endswith(
        "ENTERPRISE_BRC_NEWTON_HANDOFF_RESONANCE_FOUNDATION_20260904.md"
    )
    assert any(
        item.endswith("ENTERPRISE_BRC_NEWTON_HANDOFF_RESONANCE_THEOREM_LEDGER_20260904.json")
        for item in substrate["theorem_ledger_addenda"]
    )
    assert "t0.weighted_brc_newton_handoff_resonance" in substrate["tool_method_addenda"]
    assert "src/enterprise_math/brc_newton_handoff.py" in substrate["tool_module_addenda"]
    commitments = "\n".join(substrate["commitments"]).lower()
    assert "first irrational translated root over rational coefficients may hand off" in commitments
    assert "equal residual scales must aggregate first" in commitments

    methods = method["methods"]
    assert len(methods) == 1
    entry = methods[0]
    assert entry["method_id"] == "t0.weighted_brc_newton_handoff_resonance"
    assert entry["family_id"] == "T0_BRC"
    assert entry["implementation"] == "src/enterprise_math/brc_newton_handoff.py"
    assert "newton resonance" in entry["triggers"]
    assert "root handoff" in entry["triggers"]

    assert "__all__" in source
    for name in PUBLIC_API:
        assert name in source, name

    print("BRC Newton handoff/resonance Foundation integrity: PASS")
    print(f"theorems={len(THEOREMS)}")
    print(f"negative_boundaries={len(NEGATIVES)}")
    print(f"public_api={len(PUBLIC_API)}")
    print("method=t0.weighted_brc_newton_handoff_resonance")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
