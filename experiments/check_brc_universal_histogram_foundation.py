#!/usr/bin/env python3
"""Check universal histogram/moment BRC Foundation integration."""

from __future__ import annotations

import ast
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FOUNDATION = ROOT / "definitions" / "ENTERPRISE_BRC_UNIVERSAL_HISTOGRAM_FOUNDATION_20260903.md"
LEDGER = ROOT / "definitions" / "ENTERPRISE_BRC_UNIVERSAL_HISTOGRAM_THEOREM_LEDGER_20260903.json"
PORT_FOUNDATION = ROOT / "definitions" / "ENTERPRISE_BRC_RECURRENT_PORT_FOUNDATION_20260903.md"
PORT_LEDGER = ROOT / "definitions" / "ENTERPRISE_BRC_RECURRENT_PORT_THEOREM_LEDGER_20260903.json"
SUBSTRATE = ROOT / "definitions" / "ENTERPRISE_BRC_WEIGHTED_GLOBAL_SUBSTRATE_20260902.json"
ROUTER = ROOT / "definitions" / "00_CURRENT_NATIVE_FOUNDATION.md"
METHODS = ROOT / "research_method_inventory_addenda" / "20260903_brc_universal_histogram_foundation.json"
PACKAGE = ROOT / "src" / "enterprise_math" / "__init__.py"
MODULES = {
    "t0.weighted_brc_histogram": ROOT / "src" / "enterprise_math" / "brc_histogram.py",
    "t0.weighted_brc_moment_transfer": ROOT / "src" / "enterprise_math" / "brc_moment_transfer.py",
}
PORT_MODULE = ROOT / "src" / "enterprise_math" / "brc_recurrent_ports.py"

EXPECTED_THEOREMS = {
    "WBRC-T33-EXPLICIT-BRANCH-MOMENT-CHARACTERS",
    "WBRC-T34-FINITE-MOMENT-COMPLETENESS",
    "WBRC-T35-MOMENT-LENGTH-PORT-TRANSFER",
    "WBRC-T36-UNIVERSAL-WEIGHT-HISTOGRAM-SEMIRING",
    "WBRC-T37-PRIME-VALUATION-UNIVERSAL-TRANSFER",
    "WBRC-T38-DOMINANT-DEGENERACY-QUOTIENT",
}
EXPECTED_NEGATIVE = {
    "WBRC-N14-TOTAL-MASS-NOT-MOMENT-COMPLETE",
    "WBRC-N15-CONSTANT-PORT-NOT-LENGTH-SAFE",
    "WBRC-N16-PRIMITIVE-MOMENT-CUTOFF-NOT-PORT-COMPLETE",
    "WBRC-N17-HISTOGRAM-NOT-LABELED-PROVENANCE",
    "WBRC-N18-FORMAL-EVALUATION-NOT-MASS-OUTSIDE-STABILITY",
}
EXPECTED_EVIDENCE = {
    1155: "7d1183113331fc81cf85512ad99722230cf084d6",
    1156: "e3af4a9726fad024dd3f2aa5e8abefd7135d3a8c",
    1157: "6fa1b46886b89d508f93f830c5134850bc2fc748",
}
EXPECTED_METHOD_APIS = {
    "t0.weighted_brc_histogram": {
        "LeadingPair",
        "WeightHistogram",
        "weight_histogram",
        "histogram_recoalesce",
        "histogram_serial",
        "leading_recoalesce",
        "leading_serial",
        "dominant_degeneracy_error_bound",
        "power_sum_root_polynomial",
    },
    "t0.weighted_brc_moment_transfer": {
        "FiniteMomentSignature",
        "moment_transition_matrix",
        "moment_matrix_power",
        "moment_walk_series_coefficients",
        "finite_moment_signature",
        "moment_star_at_z",
        "moment_port_kernel_at_z",
        "equal_loop_moment_critical_z",
    },
}
PORT_API = {
    "RecurrentPortSignature",
    "recurrent_port_signature",
    "recurrent_port_dynamic_equivalent",
    "recurrent_port_zeta_equivalent",
    "recurrent_port_context_matrix",
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
    port_ledger = load_json(PORT_LEDGER)
    substrate = load_json(SUBSTRATE)
    methods = load_json(METHODS)
    foundation = FOUNDATION.read_text(encoding="utf-8")
    router = ROUTER.read_text(encoding="utf-8")
    package = PACKAGE.read_text(encoding="utf-8")

    assert ledger["status"] == "CANONICAL_FOUNDATION_ADDENDUM"
    assert ledger["foundation"].endswith(FOUNDATION.name)
    assert ledger["parent_ledger"].endswith(PORT_LEDGER.name)
    assert {record["id"] for record in ledger["theorems"]} == EXPECTED_THEOREMS
    assert {record["id"] for record in ledger["negative_boundaries"]} == EXPECTED_NEGATIVE
    assert {record["pr"]: record["merge"] for record in ledger["research_evidence"]} == EXPECTED_EVIDENCE
    assert {record["id"] for record in port_ledger["theorems"]} >= {
        "WBRC-T30-RECURRENT-SCHUR-BOUNDARY-COLLAPSE",
        "WBRC-T31-RECURRENT-PORT-CONTEXT-SAFETY",
        "WBRC-T32-RECURRENT-MINIMAL-PORT-SIGNATURE",
    }

    assert substrate["recurrent_port_foundation"].endswith(PORT_FOUNDATION.name)
    assert substrate["universal_histogram_foundation"].endswith(FOUNDATION.name)
    assert any(path.endswith(PORT_LEDGER.name) for path in substrate["theorem_ledger_addenda"])
    assert any(path.endswith(LEDGER.name) for path in substrate["theorem_ledger_addenda"])
    for method_id in [
        "t0.weighted_brc_recurrent_port_collapse",
        *EXPECTED_METHOD_APIS,
    ]:
        assert method_id in substrate["tool_method_addenda"]
    for module in [
        "src/enterprise_math/brc_recurrent_ports.py",
        "src/enterprise_math/brc_histogram.py",
        "src/enterprise_math/brc_moment_transfer.py",
    ]:
        assert module in substrate["tool_module_addenda"]

    commitments = "\n".join(substrate["commitments"])
    for marker in [
        "EXPLICIT_POSITIVE_RATIONAL_BRANCH_UNIVERSAL_CARRIER",
        "CWM_SHARED_LOW_COST_SUMMARY",
        "RECURRENT_PORT_COLLAPSE_IS_CONTEXT_TYPED",
        "LENGTH_AND_MOMENT_OBSERVERS_REQUIRE_STRONGER_PORT_STATE",
    ]:
        assert marker in commitments

    assert methods["status"] == "FOUNDATION_GLOBAL_SUBTOOLS"
    assert {method["method_id"] for method in methods["methods"]} == set(EXPECTED_METHOD_APIS)
    for method in methods["methods"]:
        method_id = method["method_id"]
        assert method["classification"] == "GLOBAL_SUBTOOL"
        assert method["family_id"] == "T0_BRC"
        assert method["status"] == "FOUNDATION_GLOBAL_SUBTOOL"
        expected = EXPECTED_METHOD_APIS[method_id]
        assert set(method["api"]) == expected
        assert expected <= public_symbols(MODULES[method_id])
        for symbol in expected:
            assert f'"{symbol}"' in package

    assert PORT_API <= public_symbols(PORT_MODULE)
    for symbol in PORT_API:
        assert f'"{symbol}"' in package

    for marker in [
        "RECURRENT-PORT-CERTIFIED",
        "UNIVERSAL-HISTOGRAM-CERTIFIED",
        "WBRC-T30..T32",
        "WBRC-T33..T35",
        "WBRC-T36..T38",
        PORT_LEDGER.name,
        LEDGER.name,
        "t0.weighted_brc_recurrent_port_collapse",
        "t0.weighted_brc_histogram",
        "t0.weighted_brc_moment_transfer",
    ]:
        assert marker in router

    for boundary in [
        "TOTAL_MASS_W1 != MOMENT_OR_HISTOGRAM_COMPLETENESS",
        "CONSTANT_W_EFF != LENGTH_SAFE_PORT_SIGNATURE",
        "WEIGHT_HISTOGRAM != LABELED_SEMANTIC_PROVENANCE",
        "ALGEBRAIC_DETERMINANT_SIGNS != SIGNED_AMPLITUDE_BRC",
    ]:
        assert boundary in foundation

    print("BRC universal histogram Foundation integrity: PASS")
    print("theorems=6 negatives=5 methods=2 port_routing_repaired=true")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
