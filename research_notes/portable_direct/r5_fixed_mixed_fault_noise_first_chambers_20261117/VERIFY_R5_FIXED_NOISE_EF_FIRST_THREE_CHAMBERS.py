#!/usr/bin/env python3
"""Exact 256-mask certification of first three fixed mixed-fault noise chambers.
Usage: python VERIFY_R5_FIXED_NOISE_EF_FIRST_THREE_CHAMBERS.py INPUT_COHORTS.json [EXACT_R5_ALL_101_BUDGETS.json]
Uses only the Python standard library, integer arithmetic and subset-zeta counts.
"""
import hashlib
import json
import sys
from pathlib import Path

PIN = '435e77af0d180eac32bd1f9c4c464bc4010b7551'
COHORT_SHA256 = 'a781cf89e534587009e207e51bbda2f411e4147746f7d6a0b72a1354e80f0d4d'
FULL_SHA256 = '50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b'
EXPECTED_GAPS = [
    76289178155959966960189440,
    3133722521542003559403356160,
    13883516118328421520506880000,
]
TRIPLES = [(214, 223, 294), (214, 223, 295), (214, 223, 296)]
WITNESSES = [(16, 17, list(range(214, 222))),
             (16, 80, list(range(223, 292))),
             (16, 32, list(range(294, 314)))]

def checked_json(path, expected_sha):
    data = Path(path).read_bytes()
    assert hashlib.sha256(data).hexdigest() == expected_sha, 'input SHA256 mismatch'
    return json.loads(data)

def load_table(coefficients):
    assert len(coefficients) == 101
    table = {}
    for k in range(214, 315):
        coeff = [0] * 256
        for m, n in coefficients[str(k)].items():
            coeff[int(m)] = int(n)
        for bit in range(8):
            for mask in range(256):
                if mask & (1 << bit):
                    coeff[mask] += coeff[mask ^ (1 << bit)]
        table[k] = coeff
    return table

def main():
    if len(sys.argv) not in (2, 3):
        raise SystemExit(__doc__)
    compact = checked_json(sys.argv[1], COHORT_SHA256)
    assert compact['scientific_input'] == PIN
    table = load_table(compact['all_budget_coefficients'])
    if len(sys.argv) == 3:
        full = checked_json(sys.argv[2], FULL_SHA256)
        assert [214, 314] == full['budget_range']
        for k, counts in table.items():
            assert counts == list(map(int, full['counts_and_cohorts'][str(k)]['counts']))
    for a, b, support in WITNESSES:
        assert [k for k in table if table[k][a] != table[k][b]] == support
    gaps, saturating = [], []
    for q in TRIPLES:
        minimum, pairs = None, []
        for a in range(256):
            for b in range(a + 1, 256):
                d = max(abs(table[k][a] - table[k][b]) for k in q)
                if minimum is None or d < minimum:
                    minimum, pairs = d, [(a, b)]
                elif d == minimum:
                    pairs.append((a, b))
        gaps.append(minimum)
        saturating.append(len(pairs))
    assert gaps == EXPECTED_GAPS
    assert saturating == [64, 64, 16], saturating
    for lower_tau, first_late in [(0, 294), (gaps[0], 295), (gaps[1], 296)]:
        assert [next(k for k in table if abs(table[k][a] - table[k][b]) > lower_tau)
                for a, b, _ in WITNESSES] == [214, 223, first_late]
    assert abs(table[294][16]-table[294][32]) == gaps[0]
    assert abs(table[295][16]-table[295][32]) == gaps[1]
    result = {
        'status': 'PASS_R5_FIXED_MIXED_FAULT_THREE_NOISE_CHAMBERS',
        'frozen_science_pin': PIN,
        'budget_domain': [214, 314], 'mask_count': 256,
        'exact_zeta_values_checked': 25856,
        'exact_unordered_pair_triple_checks': 3 * 32640,
        'triples': [list(q) for q in TRIPLES],
        'minimax_gaps_decimal': list(map(str, gaps)),
        'saturating_pair_counts': saturating,
        'first_strong_witness_budgets_at_left_boundaries':
            [[214, 223, 294], [214, 223, 295], [214, 223, 296]],
        'robust_cost_formula': 'sum(triple)*(e+2f+1) in each half-open tau chamber',
        'independent_full_table_crosscheck': len(sys.argv) == 3,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
