#!/usr/bin/env python3
"""Exact finite audit of R5 full-background recourse values.

Run beside the committed EXACT_R5_OFFLINE_MAXMIN_ALL_BACKGROUND_VALUES.json.
Python integers are exact. The parametric antichain proof is in the companion
research note; this checker verifies the finite frozen-observer consequences.
"""
import json
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = json.loads((HERE / 'EXACT_R5_OFFLINE_MAXMIN_ALL_BACKGROUND_VALUES.json').read_text())
BITS = tuple(DATA['effective_cut_bits'])
assert BITS == (3, 8, 9, 10, 27)
assert DATA['frozen_science_commit'] == '435e77af0d180eac32bd1f9c4c464bc4010b7551'
assert DATA['verified_transition_count'] == 256
lookup = {}
for key, item in DATA['rows'].items():
    K, cut = map(int, key.split('_'))
    masks, values = item['old_effective_mask_order'], item['recourse_by_old_mask']
    assert len(masks) == len(values) == 16
    assert len(set(masks)) == 16
    assert all((m & (1 << BITS.index(cut))) == 0 for m in masks)
    assert max(values) == item['maximum']
    for m, value in zip(masks, values):
        assert (K, cut, m) not in lookup
        lookup[(K, cut, m)] = value
assert len(lookup) == 256

counts = {8: Counter(), 9: Counter()}
by_toggled_bit = {8: {}, 9: {}}
for cut in (8, 9):
    for extra in BITS:
        if extra == cut:
            continue
        bit = 1 << BITS.index(extra)
        delta_hist = Counter()
        for K in range(214, 222):
            for mask in range(32):
                if mask & (bit | (1 << BITS.index(cut))):
                    continue
                delta = lookup[(K, cut, mask | bit)] - lookup[(K, cut, mask)]
                label = 'increases' if delta > 0 else 'decreases' if delta < 0 else 'unchanged'
                counts[cut][label] += 1
                delta_hist[delta] += 1
        assert sum(delta_hist.values()) == 64
        by_toggled_bit[cut][str(extra)] = dict(sorted(delta_hist.items()))

assert counts[8] == {'increases': 28, 'decreases': 40, 'unchanged': 188}
assert counts[9] == {'decreases': 24, 'unchanged': 232}
assert lookup[(214, 8, 0)] == 7
assert lookup[(214, 8, 4)] == 3
assert lookup[(214, 8, 12)] == 7
assert lookup[(214, 9, 0)] == 7
assert lookup[(214, 9, 2)] == 5

print(json.dumps({
    'status': 'PASS_EXACT_R5_PARETO_SCOPE_AND_BACKGROUND_REVERSALS',
    'scientific_input_commit': DATA['frozen_science_commit'],
    'reference_table_rows': len(lookup),
    'tested_single_background_bit_flips': sum(sum(c.values()) for c in counts.values()),
    'cut8_flip_signs': dict(counts[8]),
    'cut9_flip_signs': dict(counts[9]),
    'delta_histograms_by_toggled_bit': by_toggled_bit,
    'counterexample': {
        'K': 214, 'changed_cut': 8,
        'background_chain': [[], [9], [9, 10]],
        'recourse_values': [7, 3, 7]
    },
    'parametric_antichain_bound': 'proved in companion note; not inferred from finite test',
    'empirical_peak_state_semantics':
        'max over ranks of sum of per-new-node Pareto set sizes'
}, sort_keys=True, ensure_ascii=False, indent=2))
