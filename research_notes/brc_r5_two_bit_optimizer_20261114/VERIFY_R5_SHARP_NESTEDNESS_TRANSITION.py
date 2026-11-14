#!/usr/bin/env python3
"""Sharp K=292 pairwise-optimal-center nestedness threshold on frozen R5.

Depends on exact predecessor class table from Draft PR #2379 and the
contemporaneous 954-event center path / insertion gain recurrence.
Scope: integer event positions, radius-two, indexed centers, 28 gap closures.
Scientific input pin: 435e77af0d180eac32bd1f9c4c464bc4010b7551.
"""
import json
import sys
from pathlib import Path

THIS = Path(__file__).resolve().parent
SOURCE = THIS.parent / 'brc_r5_exact_cost_spectrum_20261114'
sys.path.insert(0, str(SOURCE))
from VERIFY_R5_COST_SPECTRA import frozen
from VERIFY_R5_OPTIMAL_WITNESSES import optimum_counts_spectrum
from VERIFY_R5_UNIVERSAL_NESTEDNESS import nested_gain_spectrum

COST_CLASS_DATA = SOURCE / 'EXACT_OUTPUT.json'
PIN = '435e77af0d180eac32bd1f9c4c464bc4010b7551'


def verify():
    report = json.loads(COST_CLASS_DATA.read_text(encoding='utf8'))
    assert len(report['classes']) == 32
    low_comparisons = 0
    bands = {}
    for row in report['classes']:
        D = row['D']
        costs = row['J_D_to_J_D_plus_6']
        assert 207 <= D <= 213
        for k in range(D, 214):
            c = costs[k-D]
            nxt = 1064 if k == 213 else costs[k+1-D]
            assert isinstance(c, int) and isinstance(nxt, int)
            delta = c-nxt
            assert delta >= 4
            bands.setdefault(k, []).append(delta)
            low_comparisons += 1
    assert low_comparisons == 128
    exact_low_ranges = {
        k: [min(values), max(values)]
        for k, values in sorted(bands.items())
    }
    assert exact_low_ranges == {
        207:[14,14],208:[7,14],209:[7,14],210:[7,14],
        211:[6,14],212:[6,14],213:[5,6]}

    x, cuts = frozen()
    assert len(x) == 954 and len(cuts) == 28
    baseline = optimum_counts_spectrum(x)
    assert set(baseline) == set(range(213,955))
    high_low_range = {}
    for k in range(214,292):
        gain = baseline[k][0] - baseline[k+1][0]
        expected = 5 if k <= 221 else 4
        assert gain == expected, (k,gain,expected)
        high_low_range[k] = gain
    assert len(high_low_range) == 78

    # The exact paired min-cost / best insertion-gain recurrence already
    # proved in the companion note shows a nested optimal pair exists for
    # every K in 292..953 in the original indexed-center instance.
    # Previously proved high-budget cost and optimizer-inclusion invariance
    # transfer these pairs to ALL 2^28 gap closure backgrounds.
    h = nested_gain_spectrum(x)
    assert all(h[k][0] == baseline[k][0] for k in baseline)
    assert all(h[k][1] == h[k][0]-h[k+1][0]
               for k in range(292,954))
    assert all(h[k][1] == 3 for k in range(292,315))
    assert all(h[k][1] == 2 for k in range(315,351))
    assert all(h[k][1] == 1 for k in range(351,954))
    assert all(h[k][1] <= 3 for k in range(213,292))

    return dict(
        status='PASS_EXACT_R5_UNIVERSAL_NESTEDNESS_PHASE_TRANSITION',
        scientific_pin=PIN,
        observer='954 indexed integer events, radius 2',
        closure_backgrounds=1<<28,
        local_cost_spectrum_classes=32,
        low_class_transition_checks=low_comparisons,
        low_budget_drop_ranges={str(k): v for k,v in exact_low_ranges.items()},
        common_cost_drop_bands=[
            dict(K_first=214,K_last=221,drop=5,count=8),
            dict(K_first=222,K_last=291,drop=4,count=70),
            dict(K_first=292,K_last=314,drop=3,count=23),
            dict(K_first=315,K_last=350,drop=2,count=36),
            dict(K_first=351,K_last=953,drop=1,count=603)],
        universal_one_insertion_gain_upper_bound=3,
        sharp_threshold=292,
        for_every_closure_mask_and_feasible_adjacent_budget=[
            dict(K_first=207,K_last=291,
                minimum_deleted_old_centers='>=1'),
            dict(K_first=292,K_last=953,
                minimum_deleted_old_centers='=0')],
        theorem_scope='pairwise existence, not one all-K nested chain',
        full_previous_class_data_sha_not_recomputed_here=True,
        independent_review='NOT_REVIEWED')


if __name__ == '__main__':
    print(json.dumps(verify(), ensure_ascii=False, indent=2))
