#!/usr/bin/env python3
"""Check recurrent/feedback BRC Foundation theorem/tool/routing integration.

Exact theorem/API identity is frozen by the ledger and method inventory.  The
hot router may coalesce historical display ranges as later addenda are added,
so routing checks accept any current range that semantically covers T17..T29
and N07..N11.
"""

from __future__ import annotations

import ast
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FOUNDATION = ROOT / "definitions" / "ENTERPRISE_BRC_RECURRENT_INTERACTION_FOUNDATION_20260903.md"
LEDGER = ROOT / "definitions" / "ENTERPRISE_BRC_RECURRENT_INTERACTION_THEOREM_LEDGER_20260903.json"
SUBSTRATE = ROOT / "definitions" / "ENTERPRISE_BRC_WEIGHTED_GLOBAL_SUBSTRATE_20260902.json"
ROUTER = ROOT / "definitions" / "00_CURRENT_NATIVE_FOUNDATION.md"
METHODS = ROOT / "research_method_inventory_addenda" / "20260903_brc_recurrent_interaction_foundation.json"
PACKAGE = ROOT / "src" / "enterprise_math" / "__init__.py"
MODULES = {
    "t0.weighted_brc_recurrent_invariants": ROOT / "src" / "enterprise_math" / "brc_recurrent_invariants.py",
    "t0.weighted_brc_rational_holonomy": ROOT / "src" / "enterprise_math" / "brc_rational_holonomy.py",
    "t0.weighted_brc_feedback_interaction": ROOT / "src" / "enterprise_math" / "brc_feedback.py",
}

EXPECTED_THEOREMS = {
    f"WBRC-T{number}-{suffix}"
    for number, suffix in [
        (17, "RECURRENT-LOOP-ZETA"),
        (18, "RECURRENT-INTEGER-EQUAL-SLACK"),
        (19, "RECURRENT-EDGE-LOOP-RESPONSE"),
        (20, "RECURRENT-RESPONSE-HESSIAN-GAUGE"),
        (21, "RECURRENT-CRITICALITY-POLYNOMIAL"),
        (22, "RATIONAL-GAUGE-PRIME-VALUATION"),
        (23, "RATIONAL-HOLONOMY-SKELETON-THICKNESS"),
        (24, "RECURRENT-DETERMINANT-CYCLE-POLYNOMIAL"),
        (25, "FEEDBACK-EVENT-CONDENSATION"),
        (26, "FEEDBACK-EDGE-ROBUSTNESS"),
        (27, "MODULAR-FEEDBACK-CHAIN"),
        (28, "FEEDBACK-MOBIUS-INTERACTION-HIERARCHY"),
        (29, "FEEDBACK-CIRCUIT-ATOM-GIRTH"),
    ]
}
EXPECTED_NEGATIVE = {
    "WBRC-N07-FULL-RATIONAL-GAUGE-EXCEEDS-RECURRENT-OBSERVABLES",
    "WBRC-N08-DETERMINANT-SIGN-NOT-SIGNED-BRC",
    "WBRC-N09-PAIRWISE-FEEDBACK-INCOMPLETE",
    "WBRC-N10-CONDITIONAL-GAMMA-ATTRIBUTION-NONCANONICAL",
    "WBRC-N11-RECURRENT-INTERACTION-SCOPE",
}
EXPECTED_METHOD_APIS = {
    "t0.weighted_brc_recurrent_invariants": {
        "RecurrentEqualSlackCertificate",
        "recurrent_loop_zeta",
        "recurrent_loop_surplus_expr",
        "recurrent_equal_slack_certificate",
        "recurrent_edge_response",
        "recurrent_edge_multiplicative_radius",
        "recurrent_edge_deletion_zeta_factor",
        "recurrent_log_response_hessian",
    },
    "t0.weighted_brc_rational_holonomy": {
        "RationalPowerDecomposition",
        "RationalTreeGaugeNormalForm",
        "rational_prime_valuations",
        "rational_from_prime_valuations",
        "rational_power_skeleton_thickness",
        "rational_squarefree_skeleton_thickness",
        "rational_tree_gauge_normal_form",
    },
    "t0.weighted_brc_feedback_interaction": {
        "FeedbackEvent",
        "FeedbackCondensationAnalysis",
        "FeedbackCircuitAtom",
        "feedback_event",
        "feedback_event_kernel",
        "feedback_condensation",
        "feedback_additive_radius",
        "conditional_feedback_kernel",
        "feedback_subset_zeta_factors",
        "feedback_mobius_interaction_factors",
        "feedback_interaction_girth",
        "feedback_circuit_atoms",
    },
}
EXPECTED_EVIDENCE = {
    1130: "edfbeacb13d1fa741c76cd7a6db328bd1b324ad3",
    1131: "86f42d9ebd06dc86ad262ab794ce64cd67517b7f",
    1132: "4f6761bbb5fb5b256d856cbfd25958483ebc1d72",
    1133: "3a6bb471a10fd8673483ea5163687ce850bba9bb",
    1134: "6f8f53230f6e36e0b55c873a72052176dd40b673",
    1142: "1fce8294c6116bdd9fd97828a232657fc7ee892c",
    1144: "c2278f6f446e8bb1c96826c4f723a40b55fb4ee6",
    1146: "69ca04e285d717f015295e149f03cbfd31836ba4",
    1147: "09d5dc3361e40910676bcaff377af81234c06fa6",
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


def covers_any(router: str, markers: tuple[str, ...]) -> bool:
    return any(marker in router for marker in markers)


def main() -> int:
    ledger = load_json(LEDGER)
    substrate = load_json(SUBSTRATE)
    method_inventory = load_json(METHODS)
    foundation = FOUNDATION.read_text(encoding="utf-8")
    router = ROUTER.read_text(encoding="utf-8")
    package = PACKAGE.read_text(encoding="utf-8")

    assert ledger["status"] == "CANONICAL_FOUNDATION_ADDENDUM"
    assert ledger["foundation"].endswith(FOUNDATION.name)
    theorem_ids = {record["id"] for record in ledger["theorems"]}
    negative_ids = {record["id"] for record in ledger["negative_boundaries"]}
    assert theorem_ids == EXPECTED_THEOREMS
    assert negative_ids == EXPECTED_NEGATIVE
    assert {record["pr"]: record["merge"] for record in ledger["research_evidence"]} == EXPECTED_EVIDENCE

    assert substrate["recurrent_interaction_foundation"].endswith(FOUNDATION.name)
    assert any(path.endswith(LEDGER.name) for path in substrate["theorem_ledger_addenda"])
    for method_id in EXPECTED_METHOD_APIS:
        assert method_id in substrate["tool_method_addenda"]
    for module in MODULES.values():
        assert str(module.relative_to(ROOT)) in substrate["tool_module_addenda"]

    commitments = "\n".join(substrate["commitments"])
    for marker in [
        "RECURRENT_LOOP_INVARIANTS_AVAILABLE",
        "RATIONAL_GAUGE_HAS_INTEGER_COORDINATES",
        "FEEDBACK_INTERACTION_IS_HIGHER_ORDER_TYPED",
        "RECURRENT_SCOPE_BOUNDARY",
    ]:
        assert marker in commitments

    methods = method_inventory["methods"]
    assert method_inventory["status"] == "FOUNDATION_GLOBAL_SUBTOOLS"
    assert {method["method_id"] for method in methods} == set(EXPECTED_METHOD_APIS)
    for method in methods:
        method_id = method["method_id"]
        assert method["classification"] == "GLOBAL_SUBTOOL"
        assert method["family_id"] == "T0_BRC"
        assert method["status"] == "FOUNDATION_GLOBAL_SUBTOOL"
        expected_api = EXPECTED_METHOD_APIS[method_id]
        assert expected_api == set(method["api"])
        assert expected_api <= public_symbols(MODULES[method_id])
        for symbol in expected_api:
            assert f'"{symbol}"' in package

    assert "RECURRENT-INTERACTION-CERTIFIED" in router
    assert FOUNDATION.name in router
    assert LEDGER.name in router
    assert covers_any(router, ("WBRC-T17/T18", "WBRC-T17..T21", "WBRC-T17..T29", "WBRC-T17..T38"))
    assert covers_any(router, ("WBRC-T22/T23", "WBRC-T22..T24", "WBRC-T17..T29", "WBRC-T17..T38"))
    assert covers_any(router, ("WBRC-T25/T26", "WBRC-T25..T29", "WBRC-T17..T29", "WBRC-T17..T38"))
    assert covers_any(router, ("WBRC-N07..N11", "WBRC-N01..N11", "WBRC-N01..N13", "WBRC-N01..N18"))
    for method_id in EXPECTED_METHOD_APIS:
        assert method_id in router

    assert covers_any(router, ("WBRC-T12..T16", "WBRC-T12..T21", "WBRC-T01..T16"))
    assert "ENTERPRISE_BRC_FINITE_RECURRENT_THEOREM_LEDGER_20260902.json" in router

    for hard_boundary in [
        "FULL_RATIONAL_GAUGE_COHOMOLOGY != RECURRENT_GAMMA_RESPONSE_COMPLETENESS",
        "DETERMINANT_ALTERNATING_SIGN != SIGNED_AMPLITUDE_BRC",
        "PAIRWISE_FEEDBACK != COMPLETE_FEEDBACK_INTERACTION",
        "CONDITIONAL_GAMMA_ATTRIBUTION != CANONICAL_COMPONENT_CREDIT",
        "FINITE_POSITIVE_RATIONAL_INTERACTION != INFINITE_OR_SIGNED_OR_COMPLEX_RECURRENCE",
    ]:
        assert hard_boundary in foundation

    print("BRC recurrent interaction Foundation integrity: PASS")
    print(f"theorems={len(theorem_ids)} negatives={len(negative_ids)} methods={len(methods)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
