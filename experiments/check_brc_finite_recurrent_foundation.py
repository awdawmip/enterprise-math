#!/usr/bin/env python3
"""Check finite recurrent Weighted-BRC Foundation/tool/theorem integration."""

from __future__ import annotations

import ast
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FOUNDATION = ROOT / "definitions" / "ENTERPRISE_BRC_FINITE_RECURRENT_FOUNDATION_20260902.md"
LEDGER = ROOT / "definitions" / "ENTERPRISE_BRC_FINITE_RECURRENT_THEOREM_LEDGER_20260902.json"
PARENT = ROOT / "definitions" / "ENTERPRISE_BRC_WEIGHTED_LOG_FOUNDATION_20260902.md"
SUBSTRATE = ROOT / "definitions" / "ENTERPRISE_BRC_WEIGHTED_GLOBAL_SUBSTRATE_20260902.json"
ROUTER = ROOT / "definitions" / "00_CURRENT_NATIVE_FOUNDATION.md"
METHOD = ROOT / "research_method_inventory_addenda" / "20260902_brc_weighted_finite_recurrent.json"
MODULE = ROOT / "src" / "enterprise_math" / "brc_weighted_recurrent.py"
PACKAGE = ROOT / "src" / "enterprise_math" / "__init__.py"

EXPECTED_THEOREMS = {
    "WBRC-T12-FINITE-RECURRENT-PATH-MASS-MATRIX",
    "WBRC-T13-FINITE-RECURRENT-RATIONAL-POTENTIAL",
    "WBRC-T14-FINITE-RECURRENT-EXACT-STAR",
    "WBRC-T15-FINITE-RECURRENT-INTEGER-ALTERNATIVE",
    "WBRC-T16-TOTAL-STABILITY-IMPLIES-DOMINANT-CONTRACTION",
}
EXPECTED_NEGATIVE = {"WBRC-N06-RECURRENT-BEYOND-FINITE-RATIONAL"}
EXPECTED_API = {
    "FiniteRecurrentMassAnalysis",
    "finite_recurrent_mass_analysis",
    "recurrent_mass_power",
    "gauge_recurrent_mass_matrix",
    "verify_recurrent_integer_stable_certificate",
    "verify_recurrent_integer_divergence_certificate",
}


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def public_symbols(path: Path) -> set[str]:
    tree = ast.parse(path.read_text(encoding="utf-8"))
    return {
        node.name
        for node in tree.body
        if isinstance(node, (ast.FunctionDef, ast.ClassDef)) and not node.name.startswith("_")
    }


def main() -> int:
    ledger = load_json(LEDGER)
    substrate = load_json(SUBSTRATE)
    method_addendum = load_json(METHOD)
    foundation = FOUNDATION.read_text(encoding="utf-8")
    parent = PARENT.read_text(encoding="utf-8")
    router = ROUTER.read_text(encoding="utf-8")
    package = PACKAGE.read_text(encoding="utf-8")

    assert "CANONICAL FOUNDATION ADDENDUM" in foundation.splitlines()[2]
    assert ledger["status"] == "CANONICAL_FOUNDATION_ADDENDUM"
    assert {item["id"] for item in ledger["theorems"]} == EXPECTED_THEOREMS
    assert {item["id"] for item in ledger["negative_boundaries"]} == EXPECTED_NEGATIVE
    assert ledger["tool_method_id"] == "t0.weighted_brc_finite_recurrent"
    assert ledger["research_evidence"]["merge"] == "9d91c769bd3d3086b6f27a843cbf4341659c9b88"

    assert substrate["finite_recurrent_foundation"].endswith(FOUNDATION.name)
    assert any(path.endswith(LEDGER.name) for path in substrate["theorem_ledger_addenda"])
    assert "t0.weighted_brc_finite_recurrent" in substrate["tool_method_addenda"]
    assert "src/enterprise_math/brc_weighted_recurrent.py" in substrate["tool_module_addenda"]
    commitments = "\n".join(substrate["commitments"])
    assert "FINITE_RATIONAL_RECURRENCE_CERTIFIED" in commitments
    assert "RECURRENT_SCOPE_BOUNDARY" in commitments

    methods = method_addendum["methods"]
    assert method_addendum["status"] == "FOUNDATION_GLOBAL_SUBTOOL"
    assert len(methods) == 1
    method = methods[0]
    assert method["method_id"] == "t0.weighted_brc_finite_recurrent"
    assert method["family_id"] == "T0_BRC"
    assert method["status"] == "FOUNDATION_GLOBAL_SUBTOOL"
    assert EXPECTED_API <= set(method["api"])
    assert EXPECTED_API <= public_symbols(MODULE)

    for symbol in EXPECTED_API:
        assert f'"{symbol}"' in package

    for theorem_id in sorted(EXPECTED_THEOREMS):
        short = theorem_id.split("-", 2)[1]
        assert short in router or theorem_id in router
    assert "WBRC-N06" in router
    assert FOUNDATION.name in router
    assert LEDGER.name in router
    assert "t0.weighted_brc_finite_recurrent" in router

    assert FOUNDATION.name in parent
    assert "FINITE_NONNEGATIVE_RATIONAL_RECURRENCE" in parent
    assert "INFINITE_OR_SIGNED_OR_ARBITRARY_REAL_RECURRENCE" in parent

    print("Finite recurrent Weighted-BRC Foundation integrity: PASS")
    print("theorems=5 negative_boundaries=1 method=t0.weighted_brc_finite_recurrent")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
