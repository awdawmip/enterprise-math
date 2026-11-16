#!/usr/bin/env python3
"""Exact fixed-query cost optimizer for the frozen R5 101-budget count observer.

Usage: python VERIFY_R5_FIXED_BUDGET_COST.py path/to/compact_stdout.json
Python standard library only; no recomputation of the original 954-event DP.
"""
import hashlib
import itertools
import json
import sys

SCIENCE_PIN = "435e77af0d180eac32bd1f9c4c464bc4010b7551"
SOURCE_SHA256 = "a781cf89e534587009e207e51bbda2f411e4147746f7d6a0b72a1354e80f0d4d"
D3 = 1744659037213380157479321600000
D4 = 1882951873548292168718745600000
E = tuple(range(214, 222))
M = tuple(range(223, 292))
L = tuple(range(293, 315))
PAIRS = tuple(itertools.combinations(range(256), 2))


def recover(path):
    raw = open(path, "rb").read()
    assert hashlib.sha256(raw).hexdigest() == SOURCE_SHA256
    source = json.loads(raw)
    assert source["scientific_input"] == SCIENCE_PIN
    assert source["status"] == "PASS_R5_101_BUDGET_INTERACTION_HIERARCHY"
    out = {}
    for ks, cs in source["all_budget_coefficients"].items():
        counts = [0] * 256
        for mask, count in cs.items():
            counts[int(mask)] = int(count)
        for bit in range(8):
            h = 1 << bit
            for b in range(256):
                if b & h:
                    counts[b] += counts[b ^ h]
        assert min(counts) > 0
        out[int(ks)] = counts
    assert sorted(out) == list(range(214, 315))
    return out


def unresolved_pairs(counts_by_budget, threshold):
    """Bit i = 1 exactly when pair i remains indistinguishable below threshold."""
    out = {}
    for k, counts in counts_by_budget.items():
        mask = 0
        for i, (b, c) in enumerate(PAIRS):
            if abs(counts[b] - counts[c]) < threshold:
                mask |= 1 << i
        out[k] = mask
    return out


def main(path):
    n = recover(path)
    assert all(len({n[k][b] for b in range(16)}) == 1 for k in n if k not in E)
    # Private switches force one query in each disjoint window.
    for window, bit in ((E, 0), (M, 6), (L, 4)):
        assert all(n[k][b] == n[k][b ^ (1 << bit)]
                   for k in n if k not in window for b in range(256))
        assert any(n[k][0] != n[k][1 << bit] for k in window)

    u3 = unresolved_pairs(n, D3)
    u4 = unresolved_pairs(n, D4)
    fibers = tuple(itertools.combinations(range(16), 2))
    e1_gap = {k: min(abs(n[k][b] - n[k][c]) for b, c in fibers) for k in E}
    assert max(e1_gap.values()) == D3
    assert [k for k in E if e1_gap[k] == D3] == [217]
    e2_gap = {q: min(max(abs(n[k][b] - n[k][c]) for k in q)
                         for b, c in fibers)
              for q in itertools.combinations(E, 2)}
    assert max(e2_gap.values()) == D4
    assert [list(q) for q, value in e2_gap.items() if value == D4] == [
        [217, 218], [217, 219]]

    # Three calls: exact one early, one middle, one late. Two-early calls
    # are compulsory for the D4 target, leaving exactly one middle and late.
    triples = [(e, m, l) for e in E for m in M for l in L
               if not (u3[e] & u3[m] & u3[l])]
    quads = [(e1, e2, m, l) for e1, e2 in itertools.combinations(E, 2)
             for m in M for l in L
             if not (u4[e1] & u4[e2] & u4[m] & u4[l])]

    middle_ok = tuple(range(224, 291))
    late_ok = tuple(range(298, 312))
    expected_triples = {(217, m, l) for m in middle_ok for l in late_ok}
    expected_quads = {(217, e, m, l) for e in (218, 219)
                      for m in middle_ok for l in late_ok}
    assert set(triples) == expected_triples
    assert set(quads) == expected_quads
    assert len(triples) == 938 and len(quads) == 1876
    assert sorted(x for x in triples if sum(x) == min(map(sum, triples))) == [(217, 224, 298)]
    assert sorted(x for x in quads if sum(x) == min(map(sum, quads))) == [(217, 218, 224, 298)]
    # Full-window obstruction: masks 11 and 14 never separate by more than D4.
    assert max(abs(n[k][11] - n[k][14]) for k in n) == D4
    assert [k for k in n if abs(n[k][11] - n[k][14]) == D4] == [217]

    result = {
        "status": "PASS_R5_FIXED_QUERY_ABSOLUTE_NOISE_COST_CLASSIFICATION",
        "scientific_input": SCIENCE_PIN,
        "source_sha256": SOURCE_SHA256,
        "budget_universe": [214, 314],
        "state_masks": 256,
        "state_pairs": len(PAIRS),
        "margin_3": str(D3),
        "margin_4": str(D4),
        "tested_fixed_three_sets": len(E) * len(M) * len(L),
        "three_margin_optimal_count": len(triples),
        "three_early_budget": [217],
        "middle_budget_range_inclusive": [224, 290],
        "late_budget_range_inclusive": [298, 311],
        "three_min_total_budget": min(map(sum, triples)),
        "three_unique_min_budget_witness": [217, 224, 298],
        "tested_four_sets_at_saturation": 28 * len(M) * len(L),
        "four_margin_optimal_count": len(quads),
        "four_early_budget_pairs": [[217, 218], [217, 219]],
        "four_min_total_budget": min(map(sum, quads)),
        "four_unique_min_budget_witness": [217, 218, 224, 298],
        "new_four_min_max_budget": 298,
        "proof_scope": "FIXED_NONADAPTIVE_DISTINCT_INTEGER_BUDGET_QUERIES_WITHIN_214_314",
    }
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main(sys.argv[1])
