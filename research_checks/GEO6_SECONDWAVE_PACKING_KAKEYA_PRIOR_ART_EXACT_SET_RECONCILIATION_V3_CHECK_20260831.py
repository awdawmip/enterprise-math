#!/usr/bin/env python3
from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MATRIX = ROOT / "research_artifacts/GEO6_SECONDWAVE_PACKING_KAKEYA_PRIOR_ART_EXACT_SET_RECONCILIATION_V3/reconciliation_matrix_v3.json"
SOURCES = ROOT / "research_artifacts/GEO6_SECONDWAVE_PACKING_KAKEYA_PRIOR_ART_EXACT_SET_RECONCILIATION_V3/source_manifest_exact_set_v3.json"

A = "RR-830A587B1588DFB21AB1"
B = "RR-4DC6467AD05A1E3CA824"
EXPECTED_RESULTS = {A, B}
EXPECTED_A_ROWS = {*[f"PCK-{i:02d}" for i in range(1, 12)], *[f"KAK-{i:02d}" for i in range(1, 8)]}
EXPECTED_B_ROWS = {*[f"P{i:02d}" for i in range(1, 9)], *[f"K{i:02d}" for i in range(1, 7)]}
EXPECTED_A_SOURCES = {
    "EXT-GRAPH-INDEPENDENCE", "EXT-KONIG", "EXT-HOFFMAN", "EXT-FOLNER-COSSETS",
    "EXT-CARTESIAN-BIPARTITE", "EXT-CAYLEY-CHARACTERS", "EXT-BERGE-ACYCLIC",
    "EXT-CYCLOMATIC", "EXT-MATROID-CIRCUIT", "EXT-DVIR-KAKEYA",
    "EXT-BALL-BLOKHUIS-DOMENZAIN", "INT-PACK-GEN2", "INT-KAK-GEN2",
}
EXPECTED_B_SOURCES = {f"S{i:02d}" for i in range(1, 13)}
EXPECTED_ATOMS = {*[f"U-P{i:02d}" for i in range(1, 12)], *[f"U-K{i:02d}" for i in range(1, 11)]}
EXPECTED_CLASSES = {
    "EXACT_DUPLICATE": 4,
    "STRICT_ANTECEDENT": 11,
    "ADJACENT_METHOD": 3,
    "NO_MATERIAL_MATCH": 3,
}
EXPECTED_SELECTORS = {
    "NONOVERLAP_SELECTOR",
    "TRANSLATION_FOLNER_SELECTOR",
    "PHYSICAL_REFINEMENT_SELECTOR",
    "MIXED_DIRECTION_SELECTOR",
}

def load(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    assert isinstance(value, dict), path
    return value

def main() -> None:
    matrix = load(MATRIX)
    sources = load(SOURCES)

    assert matrix["schema"] == "GEO6_SECONDWAVE_PRIOR_ART_EXACT_SET_RECONCILIATION_V3"
    assert sources["schema"] == "GEO6_SECONDWAVE_PRIOR_ART_EXACT_SET_SOURCE_MANIFEST_V3"
    assert set(matrix["exact_historical_result_set"]) == EXPECTED_RESULTS
    assert set(sources["exact_historical_result_set"]) == EXPECTED_RESULTS

    rows = matrix["comparison_rows"]
    assert len(rows) == 32
    by_result = {A: set(), B: set()}
    seen_pairs = set()
    for row in rows:
        key = (row["origin_result"], row["origin_row"])
        assert key not in seen_pairs
        seen_pairs.add(key)
        by_result[row["origin_result"]].add(row["origin_row"])
        assert row["canonical_atoms"]
        assert row["classification"] in EXPECTED_CLASSES
        assert row["kill_decision"]
        assert row["hypothesis_comparison"].strip()
        assert row["source_refs"]
    assert by_result[A] == EXPECTED_A_ROWS
    assert by_result[B] == EXPECTED_B_ROWS
    assert matrix["origin_row_counts"] == {A: 18, B: 14}

    entries = sources["source_entries"]
    assert len(entries) == 25
    by_source_result = {A: set(), B: set()}
    source_refs = set()
    for entry in entries:
        source_refs.add(entry["source_ref"])
        by_source_result[entry["origin_result"]].add(entry["origin_source_id"])
        assert entry["citation"].strip()
        assert entry["locator"].strip()
        assert entry["supports"]
    assert by_source_result[A] == EXPECTED_A_SOURCES
    assert by_source_result[B] == EXPECTED_B_SOURCES
    assert sources["branch_source_counts"] == {A: 13, B: 12}

    result_level_ref = sources["branch_b_result_level_selector_provenance"]["source_ref"]
    allowed_refs = source_refs | {result_level_ref}
    for row in rows:
        assert set(row["source_refs"]) <= allowed_refs

    atoms = matrix["canonical_atoms"]
    assert {row["atom_id"] for row in atoms} == EXPECTED_ATOMS
    assert len(atoms) == 21
    classes = Counter(row["classification"] for row in atoms)
    assert dict(classes) == EXPECTED_CLASSES
    assert matrix["canonical_classification_counts"] == EXPECTED_CLASSES
    for atom in atoms:
        assert set(atom["source_refs"]) <= allowed_refs
        assert atom["kill_decision"]
        assert atom["hypothesis_comparison"].strip()
        for rid, origin_rows in atom["origin_rows"].items():
            assert rid in EXPECTED_RESULTS
            expected = EXPECTED_A_ROWS if rid == A else EXPECTED_B_ROWS
            assert set(origin_rows) <= expected

    assert len(matrix["label_and_granularity_resolutions"]) == 5
    assert matrix["substantive_conflicts"] == []

    selector_rows = matrix["selectors"]
    assert {row["selector"] for row in selector_rows} == EXPECTED_SELECTORS
    assert set(matrix["surviving_selector_set"]) == EXPECTED_SELECTORS
    for row in selector_rows:
        assert row["status"] == "SURVIVES"
        assert row["accepted_resolver_present"] is False
        assert row["missing_native_datum"].strip()

    guard = matrix["no_successor_guard"]
    assert guard["accepted_resolver_present"] is False
    assert guard["successor_authorized"] is False
    assert guard["highest_leverage_future_selector"] == "NONOVERLAP_SELECTOR"
    assert "not a novelty certificate" in guard["novelty_guard"]

    assert matrix["reconciliation_disposition"] == "EXACT_SET_RECONCILED_WITHOUT_TIMESTAMP_SELECTION_OR_BRANCH_DISCARD"
    assert matrix["hard_target"] == "GEO6_SECONDWAVE_PACKING_KAKEYA_PRIOR_ART_EXACT_SET_RECONCILED_AND_WRITER_CONFORMANT"
    assert "not a novelty certificate" in sources["novelty_guard"].lower()

    aligned = set()
    for group in sources["cross_branch_alignment"]:
        aligned.update(group["branch_a"])
        aligned.update(group["branch_b"])
    assert source_refs <= aligned

    print(
        "PASS: exact 2-Result set; 18+14 origin rows; 13+12 source provenance; "
        "21 canonical atoms with 4/11/3/3 classes; four selectors survive; no successor."
    )

if __name__ == "__main__":
    main()
