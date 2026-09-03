#!/usr/bin/env python3
"""Check reducible critical-jet BRC Foundation integration."""
from __future__ import annotations

import ast
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FOUNDATION = ROOT / "definitions" / "ENTERPRISE_BRC_REDUCIBLE_CRITICAL_JET_FOUNDATION_20260903.md"
LEDGER = ROOT / "definitions" / "ENTERPRISE_BRC_REDUCIBLE_CRITICAL_JET_THEOREM_LEDGER_20260903.json"
PARENT = ROOT / "definitions" / "ENTERPRISE_BRC_CRITICAL_RATIO_JET_THEOREM_LEDGER_20260903.json"
SUBSTRATE = ROOT / "definitions" / "ENTERPRISE_BRC_WEIGHTED_GLOBAL_SUBSTRATE_20260902.json"
METHODS = ROOT / "research_method_inventory_addenda" / "20260903_brc_reducible_critical_jet_foundation.json"
MODULE = ROOT / "src" / "enterprise_math" / "brc_reducible_critical_jet.py"
PACKAGE = ROOT / "src" / "enterprise_math" / "__init__.py"

THEOREMS = {
    "WBRC-T49-GLOBAL-STRICT-RATIONAL-POWERED-GAUGE",
    "WBRC-T50-ROOT-ACTIVE-CHARACTERISTIC-JET",
    "WBRC-T51-MULTIPLE-ROOT-FIRST-NEWTON-EDGE",
}
NEGATIVES = {
    "WBRC-N31-REDUCIBLE-INTERCLASS-RATIO-NOT-CANONICAL",
    "WBRC-N32-LARGEST-STRICT-RATIO-NOT-GENERAL-SPECTRAL-SCALE",
    "WBRC-N33-MULTIPLE-ROOT-NOT-ORDINARY-FIRST-DERIVATIVE",
    "WBRC-N34-FIRST-NEWTON-EDGE-NOT-COMPLETE-PUISEUX",
    "WBRC-N35-REDUCIBLE-CRITICAL-JET-SCOPE",
}
API = {
    "PoweredBranchRatio",
    "GlobalStrictPoweredGauge",
    "CharacteristicJetLayer",
    "CharacteristicRatioJetState",
    "RootActiveLayer",
    "NewtonCandidateScale",
    "NewtonScaleState",
    "global_strict_powered_gauge",
    "characteristic_ratio_jet",
    "first_root_active_layer",
    "first_newton_edge_state",
}
EVIDENCE = {
    1182: "3e78b80954100d680eadb8eac72a7df092373922",
    1183: "fee3bb0022772087c89d81afbdad38dac1797b31",
    1184: "86bd84522cbd2512b0fee747854b8b85af904a0d",
}


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def symbols(path: Path) -> set[str]:
    tree = ast.parse(path.read_text(encoding="utf-8"))
    return {
        node.name
        for node in tree.body
        if isinstance(node, (ast.FunctionDef, ast.ClassDef)) and not node.name.startswith("_")
    }


def main() -> int:
    ledger = load(LEDGER)
    parent = load(PARENT)
    substrate = load(SUBSTRATE)
    methods = load(METHODS)
    foundation = FOUNDATION.read_text(encoding="utf-8")
    package = PACKAGE.read_text(encoding="utf-8")

    assert ledger["status"] == "CANONICAL_FOUNDATION_ADDENDUM"
    assert ledger["parent_ledger"].endswith(PARENT.name)
    assert {item["id"] for item in ledger["theorems"]} == THEOREMS
    assert {item["id"] for item in ledger["negative_boundaries"]} == NEGATIVES
    assert {item["pr"]: item["merge"] for item in ledger["research_evidence"]} == EVIDENCE
    assert {item["id"] for item in parent["theorems"]} >= {
        "WBRC-T45-POWERED-RATIONAL-CRITICAL-GAUGE",
        "WBRC-T46-CRITICAL-RATIO-HISTOGRAM-FINITE-JET",
        "WBRC-T47-IRREDUCIBLE-RATIO-JET-FIRST-SPECTRAL-RESPONSE",
        "WBRC-T48-FULL-POWERED-BRANCH-RATIO-JET",
    }

    assert substrate["reducible_critical_jet_foundation"].endswith(FOUNDATION.name)
    assert any(path.endswith(LEDGER.name) for path in substrate["theorem_ledger_addenda"])
    assert "t0.weighted_brc_reducible_critical_jet" in substrate["tool_method_addenda"]
    assert "src/enterprise_math/brc_reducible_critical_jet.py" in substrate["tool_module_addenda"]
    commitments = "\n".join(substrate["commitments"])
    assert "REDUCIBLE_CRITICAL_CHARACTERISTIC_JET_IS_CANONICAL" in commitments
    assert "first Newton edge is not a complete Puiseux expansion" in commitments

    assert methods["status"] == "FOUNDATION_GLOBAL_SUBTOOLS"
    assert len(methods["methods"]) == 1
    method = methods["methods"][0]
    assert method["method_id"] == "t0.weighted_brc_reducible_critical_jet"
    assert method["classification"] == "GLOBAL_SUBTOOL"
    assert method["family_id"] == "T0_BRC"
    assert set(method["api"]) == API
    assert API <= symbols(MODULE)
    for symbol in API:
        assert f'"{symbol}"' in package

    for marker in [
        "REDUCIBLE_BRANCH_RATIO_REPRESENTATIVE = NOT_CANONICAL",
        "CLOSED_CHARACTERISTIC_RATIO_JET = CANONICAL_GAUGE_INVARIANT",
        "SIMPLE_SMALLEST_ROOT -> ROOT_ACTIVE_ORDINARY_EXPONENTIAL_RESPONSE",
        "MULTIPLE_SMALLEST_ROOT -> FIRST_NEWTON_EDGE",
        "MULTIPLE_EDGE_ROOT -> LATER_NEWTON_EDGE_REQUIRED",
    ]:
        assert marker in foundation

    print("BRC reducible critical-jet Foundation integrity: PASS")
    print("theorems=3 negatives=5 methods=1 parent_T45_T48=true")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
