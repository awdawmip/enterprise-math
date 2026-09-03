#!/usr/bin/env python3
"""Check critical ratio-jet BRC Foundation integration."""
from __future__ import annotations

import ast
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FOUNDATION = ROOT / "definitions" / "ENTERPRISE_BRC_CRITICAL_RATIO_JET_FOUNDATION_20260903.md"
LEDGER = ROOT / "definitions" / "ENTERPRISE_BRC_CRITICAL_RATIO_JET_THEOREM_LEDGER_20260903.json"
PARENT = ROOT / "definitions" / "ENTERPRISE_BRC_CRITICAL_ORBIT_THEOREM_LEDGER_20260903.json"
SUBSTRATE = ROOT / "definitions" / "ENTERPRISE_BRC_WEIGHTED_GLOBAL_SUBSTRATE_20260902.json"
METHODS = ROOT / "research_method_inventory_addenda" / "20260903_brc_critical_ratio_jet_foundation.json"
MODULE = ROOT / "src" / "enterprise_math" / "brc_critical_ratio_jet.py"
PACKAGE = ROOT / "src" / "enterprise_math" / "__init__.py"

THEOREMS = {
    "WBRC-T45-POWERED-RATIONAL-CRITICAL-GAUGE",
    "WBRC-T46-CRITICAL-RATIO-HISTOGRAM-FINITE-JET",
    "WBRC-T47-IRREDUCIBLE-RATIO-JET-FIRST-SPECTRAL-RESPONSE",
    "WBRC-T48-FULL-POWERED-BRANCH-RATIO-JET",
}
NEGATIVES = {
    "WBRC-N26-ALGEBRAIC-MEAN-NOT-ALGEBRAIC-CERTIFICATE",
    "WBRC-N27-K-NOT-SUBDOMINANT-RATIO-COMPLETE",
    "WBRC-N28-RATIO-JET-NOT-ABSOLUTE-PROVENANCE",
    "WBRC-N29-IRREDUCIBLE-SCOPE-NOT-REDUCIBLE-CRITICAL-CLASSES",
    "WBRC-N30-POSITIVE-RATIO-RESPONSE-NOT-SIGNED-CANCELLATION",
}
API = {
    "PoweredCriticalGauge",
    "CriticalRatioJet",
    "FullPoweredRatioJet",
    "CriticalRatioResponseState",
    "powered_critical_gauge",
    "critical_ratio_jet",
    "full_powered_ratio_jet",
    "critical_ratio_first_response",
}
EVIDENCE = {
    1177: "872c33f8834dd1c2d282cafe6704e69ef011addb",
    1178: "6543b8c4ce11af0fc043d95e183dc35261510786",
    1179: "2021cd0f17b43e880dc531491a882b892cb7bffe",
    1180: "ab09cd839f8a348075a2756477484e82325b5328",
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
        "WBRC-T43-CRITICAL-MULTIPLICITY-AUTOMATON",
        "WBRC-T44-CRITICAL-PRIMITIVE-ORBIT-EULER",
    }

    assert substrate["critical_ratio_jet_foundation"].endswith(FOUNDATION.name)
    assert any(path.endswith(LEDGER.name) for path in substrate["theorem_ledger_addenda"])
    assert "t0.weighted_brc_critical_ratio_jet" in substrate["tool_method_addenda"]
    assert "src/enterprise_math/brc_critical_ratio_jet.py" in substrate["tool_module_addenda"]
    commitments = "\n".join(substrate["commitments"])
    assert "CRITICAL_RATIO_JET_IS_EXPLICIT_BRANCH_TYPED" in commitments
    assert "reducible critical classes" in commitments.lower()

    assert methods["status"] == "FOUNDATION_GLOBAL_SUBTOOLS"
    assert len(methods["methods"]) == 1
    method = methods["methods"][0]
    assert method["method_id"] == "t0.weighted_brc_critical_ratio_jet"
    assert method["classification"] == "GLOBAL_SUBTOOL"
    assert method["family_id"] == "T0_BRC"
    assert set(method["api"]) == API
    assert API <= symbols(MODULE)
    for symbol in API:
        assert f'"{symbol}"' in package

    for marker in [
        "T40_GLOBAL_GAP = MAX_STRICT_FULL_POWERED_BRANCH_RATIO",
        "FULL_POWERED_RATIO_JET_REQUIRES_IRREDUCIBLE_CRITICAL_GRAPH",
        "POSITIVE_RATIO_JET_RESPONSE != SIGNED_CANCELLATION",
        "REDUCIBLE_CRITICAL_CLASSES = SEPARATE_RESEARCH_FRONTIER",
    ]:
        assert marker in foundation

    print("BRC critical ratio-jet Foundation integrity: PASS")
    print("theorems=4 negatives=5 methods=1 parent_T43_T44=true")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
