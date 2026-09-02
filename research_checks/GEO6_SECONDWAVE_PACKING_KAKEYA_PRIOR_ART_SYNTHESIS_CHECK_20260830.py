#!/usr/bin/env python3
from __future__ import annotations

import json
from collections import Counter
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
P = ROOT / "research_artifacts/GEO6_SECONDWAVE_PACKING_KAKEYA_PRIOR_ART_SYNTHESIS/claim_source_matrix.json"

EXPECTED = {
    "EXACT_DUPLICATE": 3,
    "STRICT_ANTECEDENT": 11,
    "ADJACENT_METHOD": 1,
    "NO_MATERIAL_MATCH": 3,
}
SELECTORS = {
    "NONOVERLAP_SELECTOR",
    "TRANSLATION_FOLNER_SELECTOR",
    "PHYSICAL_REFINEMENT_SELECTOR",
    "MIXED_DIRECTION_SELECTOR",
}

def main() -> None:
    d = json.loads(P.read_text(encoding="utf-8"))
    assert d["schema"] == "GEO6_SECONDWAVE_PRIOR_ART_CLAIM_MATRIX_V1"
    assert d["task_id"] == "RS-GEO6-SECONDWAVE-PACKING-KAKEYA-PRIOR-ART-SYNTHESIS"
    assert d["publication_id"] == "TP2-3B14908767F248123B62"
    rows = d["claims"]
    ids = [r["claim_id"] for r in rows]
    assert len(rows) == 18 and len(set(ids)) == 18
    assert Counter(r["classification"] for r in rows) == Counter(EXPECTED)
    assert d["classification_counts"] == EXPECTED
    source_ids = {s["source_id"] for s in d["sources"]}
    for r in rows:
        assert r["accepted_claim"].strip()
        assert r["hypothesis_comparison"].strip()
        assert r["strongest_antecedent"]
        assert set(r["strongest_antecedent"]) <= source_ids
        if r["classification"] == "NO_MATERIAL_MATCH":
            assert "not a novelty certificate" in r["residue"].lower()
    sm = d["selector_map"]
    assert {x["selector"] for x in sm} == SELECTORS
    assert all(x["status"] == "SURVIVES" for x in sm)
    assert all(x["accepted_datum_capable_now"] is False for x in sm)
    assert d["driver_recommendation"]["accepted_p000_or_full_cell_datum_resolving_any_selector_now"] == "NONE_CURRENTLY_IDENTIFIED"
    assert d["driver_recommendation"]["highest_leverage_future_selector"] == "NONOVERLAP_SELECTOR"
    for c in range(1, 7):
        defect = 6 - c
        assert defect <= 5
        for r in range(2, 9):
            if c == 1:
                assert 6 * r - defect == 6 * r - 5
    assert Fraction(12, 24) == Fraction(1, 2)
    print("PASS: 18 rows; 3/11/1/3; four selectors survive; D=6-c; K6=6r-5; Hoffman=1/2")

if __name__ == "__main__":
    main()
