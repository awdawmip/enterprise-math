#!/usr/bin/env python3
"""Check critical-degeneracy BRC Foundation/tool integration."""

from __future__ import annotations

import ast
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FOUNDATION = ROOT / "definitions" / "ENTERPRISE_BRC_CRITICAL_DEGENERACY_FOUNDATION_20260903.md"
LEDGER = ROOT / "definitions" / "ENTERPRISE_BRC_CRITICAL_DEGENERACY_THEOREM_LEDGER_20260903.json"
PARENT_LEDGER = ROOT / "definitions" / "ENTERPRISE_BRC_UNIVERSAL_HISTOGRAM_THEOREM_LEDGER_20260903.json"
SUBSTRATE = ROOT / "definitions" / "ENTERPRISE_BRC_WEIGHTED_GLOBAL_SUBSTRATE_20260902.json"
ROUTER = ROOT / "definitions" / "00_CURRENT_NATIVE_FOUNDATION.md"
METHOD = ROOT / "research_method_inventory_addenda" / "20260903_brc_critical_degeneracy_foundation.json"
MODULE = ROOT / "src" / "enterprise_math" / "brc_critical_degeneracy.py"
PACKAGE = ROOT / "src" / "enterprise_math" / "__init__.py"

EXPECTED_THEOREMS = {
    "WBRC-T39-CRITICAL-DEGENERACY-MATRIX-ASYMPTOTIC",
    "WBRC-T40-CRITICAL-DEGENERACY-EXACT-GAP",
    "WBRC-T41-CRITICAL-LOG-ROOT-SELECTOR",
    "WBRC-T42-CRITICAL-LOG-ZERO-THRESHOLD-READOUT",
}
EXPECTED_NEGATIVE = {
    "WBRC-N19-ONE-CYCLE-DEGENERACY-NOT-GENERAL-MULTICRITICAL",
    "WBRC-N20-FLOATING-SPECTRAL-NOT-EXACT-CERTIFICATE",
    "WBRC-N21-ALGEBRAIC-CORRECTION-NOT-RATIONAL-LN",
    "WBRC-N22-TOTAL-MASS-NOT-CRITICAL-DEGENERACY-COMPLETE",
}
EXPECTED_EVIDENCE = {
    1166: "0aae8187076c0967e2f2bef7cccaa811d78c93ad",
    1167: "e4d787da5dd4a8411da0a62aca2dec993fd6099e",
    1168: "5c4b70f344586599386c5067264debb790f4e2f7",
}
EXPECTED_API = {
    "CriticalDegeneracyAnalysis",
    "CriticalRootSelector",
    "CriticalLogCorrectionState",
    "critical_degeneracy_analysis",
    "criticality_polynomial",
    "smallest_positive_root_selector",
    "critical_log_correction_state",
    "critical_graph_shaped",
    "critical_log_zero",
    "critical_log_threshold_analysis",
    "critical_log_less_than_rational",
    "critical_log_bounds",
    "critical_log_correction_from_branches",
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
    parent = load_json(PARENT_LEDGER)
    substrate = load_json(SUBSTRATE)
    method_file = load_json(METHOD)
    foundation = FOUNDATION.read_text(encoding="utf-8")
    router = ROUTER.read_text(encoding="utf-8")
    package = PACKAGE.read_text(encoding="utf-8")

    assert ledger["status"] == "CANONICAL_FOUNDATION_ADDENDUM"
    assert ledger["foundation"].endswith(FOUNDATION.name)
    assert ledger["parent_ledger"].endswith(PARENT_LEDGER.name)
    assert {record["id"] for record in ledger["theorems"]} == EXPECTED_THEOREMS
    assert {record["id"] for record in ledger["negative_boundaries"]} == EXPECTED_NEGATIVE
    assert {record["pr"]: record["merge"] for record in ledger["research_evidence"]} == EXPECTED_EVIDENCE
    assert {record["id"] for record in parent["theorems"]} >= {
        "WBRC-T36-UNIVERSAL-WEIGHT-HISTOGRAM-SEMIRING",
        "WBRC-T38-DOMINANT-DEGENERACY-QUOTIENT",
    }

    assert substrate["critical_degeneracy_foundation"].endswith(FOUNDATION.name)
    assert any(path.endswith(LEDGER.name) for path in substrate["theorem_ledger_addenda"])
    assert "t0.weighted_brc_critical_degeneracy" in substrate["tool_method_addenda"]
    assert "src/enterprise_math/brc_critical_degeneracy.py" in substrate["tool_module_addenda"]
    commitments = "\n".join(substrate["commitments"])
    for marker in [
        "EXPLICIT_POSITIVE_RATIONAL_BRANCH_UNIVERSAL_CARRIER",
        "CRITICAL_DEGENERACY_IS_EXPLICIT_BRANCH_TYPED",
        "RECURRENT_SCOPE_BOUNDARY",
    ]:
        assert marker in commitments

    assert method_file["status"] == "FOUNDATION_GLOBAL_SUBTOOL"
    assert len(method_file["methods"]) == 1
    method = method_file["methods"][0]
    assert method["method_id"] == "t0.weighted_brc_critical_degeneracy"
    assert method["classification"] == "GLOBAL_SUBTOOL"
    assert method["family_id"] == "T0_BRC"
    assert method["status"] == "FOUNDATION_GLOBAL_SUBTOOL"
    assert set(method["api"]) == EXPECTED_API
    assert EXPECTED_API <= public_symbols(MODULE)
    for symbol in EXPECTED_API:
        assert f'"{symbol}"' in package

    for marker in [
        "CRITICAL-DEGENERACY-CERTIFIED",
        "WBRC-T39..T42",
        "WBRC-N19..N22",
        LEDGER.name,
        "t0.weighted_brc_critical_degeneracy",
    ]:
        assert marker in router

    for boundary in [
        "ONE_CRITICAL_CYCLE_D_PRODUCT != GENERAL_MULTI_CRITICAL_CORRECTION",
        "FLOATING_EIGENVALUE_OR_ROOT != EXACT_ENTERPRISE_CERTIFICATE",
        "CRITICAL_LOG_EXACT_STATE = INTEGER_POLYNOMIAL + ROOT_SELECTOR",
        "GENERAL_ALGEBRAIC_LN_MATERIALIZER = NOT_PROMOTED",
        "TOTAL_MASS_ONLY != CRITICAL_DEGENERACY_COMPLETE",
    ]:
        assert boundary in foundation

    print("BRC critical-degeneracy Foundation integrity: PASS")
    print("theorems=4 negatives=4 methods=1 api=13")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
