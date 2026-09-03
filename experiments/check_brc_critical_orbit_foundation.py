#!/usr/bin/env python3
"""Check critical orbit BRC Foundation/tool integration."""
from __future__ import annotations
import ast
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FOUNDATION = ROOT / "definitions" / "ENTERPRISE_BRC_CRITICAL_ORBIT_FOUNDATION_20260903.md"
LEDGER = ROOT / "definitions" / "ENTERPRISE_BRC_CRITICAL_ORBIT_THEOREM_LEDGER_20260903.json"
PARENT = ROOT / "definitions" / "ENTERPRISE_BRC_CRITICAL_DEGENERACY_THEOREM_LEDGER_20260903.json"
SUBSTRATE = ROOT / "definitions" / "ENTERPRISE_BRC_WEIGHTED_GLOBAL_SUBSTRATE_20260902.json"
ROUTER = ROOT / "definitions" / "00_CURRENT_NATIVE_FOUNDATION.md"
METHOD = ROOT / "research_method_inventory_addenda" / "20260903_brc_critical_orbit_foundation.json"
MODULE = ROOT / "src" / "enterprise_math" / "brc_critical_orbits.py"
PACKAGE = ROOT / "src" / "enterprise_math" / "__init__.py"

EXPECTED_THEOREMS = {
    "WBRC-T43-CRITICAL-MULTIPLICITY-AUTOMATON",
    "WBRC-T44-CRITICAL-PRIMITIVE-ORBIT-EULER",
}
EXPECTED_NEGATIVE = {
    "WBRC-N23-PRIMITIVE-PERIODIC-ORBIT-NOT-T29-SIMPLE-CIRCUIT",
    "WBRC-N24-CRITICAL-RESIDUAL-GROWTH-NOT-SHANNON-ENTROPY",
    "WBRC-N25-PRIMITIVE-ORBIT-EULER-NOT-ARITHMETIC-PRIME-EULER",
}
EXPECTED_EVIDENCE = {
    1173: "c8b42da536eee2a1b14635405a8ecdce76fa4658",
    1174: "4daf62373665843928c0ea69fe9b5398dabdd63b",
}
EXPECTED_API = {
    "CriticalOrbitPrefix",
    "critical_word_counts",
    "critical_primitive_orbit_counts",
    "critical_zeta_coefficients",
    "critical_euler_coefficients",
    "critical_orbit_prefix",
}


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def public(path: Path) -> set[str]:
    tree = ast.parse(path.read_text(encoding="utf-8"))
    return {
        node.name for node in tree.body
        if isinstance(node, (ast.FunctionDef, ast.ClassDef)) and not node.name.startswith("_")
    }


def main() -> int:
    ledger = load(LEDGER)
    parent = load(PARENT)
    substrate = load(SUBSTRATE)
    method_file = load(METHOD)
    foundation = FOUNDATION.read_text(encoding="utf-8")
    package = PACKAGE.read_text(encoding="utf-8")
    router = ROUTER.read_text(encoding="utf-8")

    assert ledger["status"] == "CANONICAL_FOUNDATION_ADDENDUM"
    assert ledger["foundation"].endswith(FOUNDATION.name)
    assert ledger["parent_ledger"].endswith(PARENT.name)
    assert ledger["tool_method_id"] == "t0.weighted_brc_critical_orbits"
    assert ledger["parent_tool_method_id"] == "t0.weighted_brc_critical_degeneracy"
    assert {item["id"] for item in ledger["theorems"]} == EXPECTED_THEOREMS
    assert {item["id"] for item in ledger["negative_boundaries"]} == EXPECTED_NEGATIVE
    assert {item["pr"]: item["merge"] for item in ledger["research_evidence"]} == EXPECTED_EVIDENCE
    assert {item["id"] for item in parent["theorems"]} >= {
        "WBRC-T39-CRITICAL-DEGENERACY-MATRIX-ASYMPTOTIC",
        "WBRC-T41-CRITICAL-LOG-ROOT-SELECTOR",
        "WBRC-T42-CRITICAL-LOG-ZERO-THRESHOLD-READOUT",
    }

    assert substrate["critical_orbit_foundation"].endswith(FOUNDATION.name)
    assert any(path.endswith(LEDGER.name) for path in substrate["theorem_ledger_addenda"])
    assert "t0.weighted_brc_critical_orbits" in substrate["tool_method_addenda"]
    assert "src/enterprise_math/brc_critical_orbits.py" in substrate["tool_module_addenda"]
    commitments = "\n".join(substrate["commitments"])
    assert "CRITICAL_ORBIT_INVENTORY_IS_K_TYPED" in commitments
    assert "RECURRENT_SCOPE_BOUNDARY" in commitments

    method = method_file["methods"][0]
    assert method_file["status"] == "FOUNDATION_GLOBAL_SUBTOOL"
    assert method["method_id"] == "t0.weighted_brc_critical_orbits"
    assert method["family_id"] == "T0_BRC"
    assert method["classification"] == "GLOBAL_SUBTOOL"
    assert set(method["api"]) == EXPECTED_API
    assert EXPECTED_API <= public(MODULE)
    for symbol in EXPECTED_API:
        assert f'"{symbol}"' in package

    # Later addenda are routed by the universal substrate rather than forcing
    # every theorem ID into the hot router.
    assert "ENTERPRISE_BRC_WEIGHTED_GLOBAL_SUBSTRATE_20260902.json" in router
    assert "GLOBAL_FOUNDATION_CAPABILITY != FORCED_BRC_INTERPRETATION" in router

    for marker in [
        "CRITICAL_MULTIPLICITY_AUTOMATON = INTEGER_K",
        "PRIMITIVE_PERIODIC_ORBIT_COUNT = P_n",
        "PRIMITIVE_PERIODIC_ORBIT != WBRC_T29_SIMPLE_SUPPORT_CIRCUIT",
        "P_n != ARITHMETIC_PRIME_COUNT",
    ]:
        assert marker in foundation

    print("BRC critical orbit Foundation integrity: PASS")
    print("theorems=2 negatives=3 methods=1 api=6")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
