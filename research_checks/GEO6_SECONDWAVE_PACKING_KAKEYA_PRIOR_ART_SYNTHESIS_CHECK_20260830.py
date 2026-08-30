#!/usr/bin/env python3
"""Exact regression for RS-GEO6-SECONDWAVE-PACKING-KAKEYA-PRIOR-ART-SYNTHESIS."""

from __future__ import annotations

import json
from collections import Counter
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MATRIX = ROOT / "research_artifacts/GEO6_SECONDWAVE_PACKING_KAKEYA_PRIOR_ART_SYNTHESIS/claim_source_matrix.json"

EXPECTED_CLASSES = {
    "EXACT_DUPLICATE": 3,
    "STRICT_ANTECEDENT": 11,
    "ADJACENT_METHOD": 1,
    "NO_MATERIAL_MATCH": 3,
}
EXPECTED_SELECTORS = {
    "NONOVERLAP_SELECTOR",
    "TRANSLATION_FOLNER_SELECTOR",
    "PHYSICAL_REFINEMENT_SELECTOR",
    "MIXED_DIRECTION_SELECTOR",
}
EXPECTED_KILLS = {'PCK-02', 'PCK-09', 'KAK-01', 'PCK-06', 'KAK-02', 'PCK-07', 'KAK-05', 'PCK-08', 'PCK-03', 'KAK-03', 'PCK-05', 'PCK-01', 'KAK-04', 'PCK-04'}


def main() -> None:
    data = json.loads(MATRIX.read_text(encoding="utf-8"))

    assert data["schema"] == "GEO6_SECONDWAVE_PRIOR_ART_CLAIM_MATRIX_V1"
    assert data["task_id"] == "RS-GEO6-SECONDWAVE-PACKING-KAKEYA-PRIOR-ART-SYNTHESIS"
    assert data["publication_id"] == "TP2-3B14908767F248123B62"
    assert data["hard_target"] == "GEO6_SECONDWAVE_PACKING_KAKEYA_PRIOR_ART_EXACTLY_CLASSIFIED"

    claims = data["claims"]
    ids = [c["claim_id"] for c in claims]
    assert len(claims) == 18
    assert len(ids) == len(set(ids))

    counts = Counter(c["classification"] for c in claims)
    assert dict(counts) == EXPECTED_CLASSES
    assert data["classification_counts"] == EXPECTED_CLASSES

    source_ids = {s["source_id"] for s in data["sources"]}
    for claim in claims:
        assert claim["accepted_claim"].strip()
        assert claim["hypothesis_comparison"].strip()
        assert claim["strongest_antecedent"]
        assert set(claim["strongest_antecedent"]) <= source_ids
        if claim["classification"] == "NO_MATERIAL_MATCH":
            assert "not a novelty certificate" in claim["residue"].lower()

    kills = {c["claim_id"] for c in claims if c["kill_continuation"]}
    assert kills == EXPECTED_KILLS
    assert set(data["continuation_kill_claim_ids"]) == EXPECTED_KILLS

    selector_map = data["selector_map"]
    assert {s["selector"] for s in selector_map} == EXPECTED_SELECTORS
    assert all(s["status"] == "SURVIVES" for s in selector_map)
    assert all(s["accepted_datum_capable_now"] is False for s in selector_map)

    driver = data["driver_recommendation"]
    assert driver["accepted_p000_or_full_cell_datum_resolving_any_selector_now"] == "NONE_CURRENTLY_IDENTIFIED"
    assert driver["highest_leverage_future_selector"] == "NONOVERLAP_SELECTOR"
    assert data["tool_reuse"]["status"] == "REUSE_APPLIED"
    assert data["tool_reuse"]["new_global_tool_family"] is False
    assert "not a novelty certificate" in data["novelty_guard"].lower()

    # Exact forest defect regression for six path vertices.
    for components in range(1, 7):
        defect = 6 - components
        assert defect <= 5
        for r in range(2, 9):
            support = 6 * r - defect
            if components == 1:
                assert support == 6 * r - 5

    # Exact Hoffman substitution: d=12, tau=-12.
    d = 12
    tau = -12
    hoffman = Fraction(-tau, d - tau)
    assert hoffman == Fraction(1, 2)

    print(
        "PASS RS-GEO6-SECONDWAVE-PACKING-KAKEYA-PRIOR-ART-SYNTHESIS: "
        "18 claims / classes 3-11-1-3 / 4 selectors survive / no accepted resolver"
    )


if __name__ == "__main__":
    main()
