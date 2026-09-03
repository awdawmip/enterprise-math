#!/usr/bin/env python3
"""Check recurrent BRC port-collapse Foundation/tool integration."""

from __future__ import annotations

import ast
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FOUNDATION = ROOT / "definitions" / "ENTERPRISE_BRC_RECURRENT_PORT_FOUNDATION_20260903.md"
LEDGER = ROOT / "definitions" / "ENTERPRISE_BRC_RECURRENT_PORT_THEOREM_LEDGER_20260903.json"
SUBSTRATE = ROOT / "definitions" / "ENTERPRISE_BRC_WEIGHTED_GLOBAL_SUBSTRATE_20260902.json"
PARENT_LEDGER = ROOT / "definitions" / "ENTERPRISE_BRC_RECURRENT_INTERACTION_THEOREM_LEDGER_20260903.json"
METHOD = ROOT / "research_method_inventory_addenda" / "20260903_brc_recurrent_port_foundation.json"
MODULE = ROOT / "src" / "enterprise_math" / "brc_recurrent_ports.py"
PACKAGE = ROOT / "src" / "enterprise_math" / "__init__.py"
ROUTER = ROOT / "definitions" / "00_CURRENT_NATIVE_FOUNDATION.md"

EXPECTED_THEOREMS = {
    "WBRC-T30-RECURRENT-SCHUR-BOUNDARY-COLLAPSE",
    "WBRC-T31-RECURRENT-PORT-CONTEXT-SAFETY",
    "WBRC-T32-RECURRENT-MINIMAL-PORT-SIGNATURE",
}
EXPECTED_NEGATIVE = {
    "WBRC-N12-RECURRENT-PORT-COLLAPSE-NOT-CWM-SAFE",
    "WBRC-N13-RECURRENT-PORT-LEASE-BOUNDARY",
}
EXPECTED_API = {
    "RecurrentPortSignature",
    "recurrent_port_signature",
    "recurrent_port_dynamic_equivalent",
    "recurrent_port_zeta_equivalent",
    "recurrent_port_context_matrix",
}
EXPECTED_EVIDENCE = {
    1152: "40d3ec9e7786bafddb6e10694e2d60137a65850b",
    1153: "48659591c3d51dcb3fdaf9585789a1d49eadfdf1",
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
    parent = load_json(PARENT_LEDGER)
    methods = load_json(METHOD)
    foundation = FOUNDATION.read_text(encoding="utf-8")
    package = PACKAGE.read_text(encoding="utf-8")
    router = ROUTER.read_text(encoding="utf-8")

    assert ledger["status"] == "CANONICAL_FOUNDATION_ADDENDUM"
    assert ledger["foundation"].endswith(FOUNDATION.name)
    assert ledger["parent_ledger"].endswith(PARENT_LEDGER.name)
    assert {record["id"] for record in ledger["theorems"]} == EXPECTED_THEOREMS
    assert {record["id"] for record in ledger["negative_boundaries"]} == EXPECTED_NEGATIVE
    assert {record["pr"]: record["merge"] for record in ledger["research_evidence"]} == EXPECTED_EVIDENCE
    assert {record["id"] for record in parent["theorems"]} >= {
        "WBRC-T25-FEEDBACK-EVENT-CONDENSATION",
        "WBRC-T28-FEEDBACK-MOBIUS-INTERACTION-HIERARCHY",
        "WBRC-T29-FEEDBACK-CIRCUIT-ATOM-GIRTH",
    }

    assert substrate["recurrent_port_foundation"].endswith(FOUNDATION.name)
    assert any(path.endswith(LEDGER.name) for path in substrate["theorem_ledger_addenda"])
    assert "t0.weighted_brc_recurrent_port_collapse" in substrate["tool_method_addenda"]
    assert "src/enterprise_math/brc_recurrent_ports.py" in substrate["tool_module_addenda"]
    commitments = "\n".join(substrate["commitments"])
    assert "RECURRENT_PORT_COLLAPSE_IS_CONTEXT_TYPED" in commitments
    assert "RECURRENT_SCOPE_BOUNDARY" in commitments

    assert methods["status"] == "FOUNDATION_GLOBAL_SUBTOOL"
    assert len(methods["methods"]) == 1
    method = methods["methods"][0]
    assert method["method_id"] == "t0.weighted_brc_recurrent_port_collapse"
    assert method["classification"] == "GLOBAL_SUBTOOL"
    assert method["family_id"] == "T0_BRC"
    assert method["status"] == "FOUNDATION_GLOBAL_SUBTOOL"
    assert set(method["api"]) == EXPECTED_API
    assert EXPECTED_API <= public_symbols(MODULE)
    for symbol in EXPECTED_API:
        assert f'"{symbol}"' in package

    # Current router points at the universal substrate; exact new theorem/tool
    # routing is intentionally carried by that substrate rather than by inflating
    # the hot router with every later addendum.
    assert "ENTERPRISE_BRC_WEIGHTED_GLOBAL_SUBSTRATE_20260902.json" in router
    assert "GLOBAL_FOUNDATION_CAPABILITY != FORCED_BRC_INTERPRETATION" in router

    for boundary in [
        "RECURRENT_PORT_COLLAPSE != CWM_COUNT_DOMINANT_PROVENANCE_SAFE",
        "PORT_SIGNATURE_LEASE -> NO_DIRECT_FUTURE_HIDDEN_STATE_ACCESS",
        "VISIBLE_DYNAMIC_SIGNATURE = W_EFF",
        "VISIBLE_DYNAMIC_PLUS_ABSOLUTE_ZETA_SIGNATURE = (W_EFF,Z_INT)",
    ]:
        assert boundary in foundation

    print("BRC recurrent port Foundation integrity: PASS")
    print("theorems=3 negatives=2 methods=1")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
