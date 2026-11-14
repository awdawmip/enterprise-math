#!/usr/bin/env python3
"""Exact eight-endpoint certificate for frozen R5 high-budget optimizer families.

Reuses the predecessor's exact 954-coordinate generator and indexed-center
min-cost/tie-count recurrence from PR #2379. Standard-library only.
Frozen scientific input: 435e77af0d180eac32bd1f9c4c464bc4010b7551.
"""
import json
import random
import sys
from itertools import combinations
from pathlib import Path

SOURCE = Path(__file__).resolve().parents[1] / 'brc_r5_exact_cost_spectrum_20261114'
sys.path.insert(0, str(SOURCE))
from VERIFY_R5_COST_SPECTRA import frozen, closed_points
from VERIFY_R5_OPTIMAL_WITNESSES import optimum_counts_spectrum

PIVOTS = (15, 17)
ALL = (1 << 28) - 1
OTHER = ALL ^ sum(1 << i for i in PIVOTS)
PIN = '435e77af0d180eac32bd1f9c4c464bc4010b7551'


def brute_spectrum(y):
    out = {}
    for k in range(1, len(y) + 1):
        costs = []
        for chosen in combinations(range(len(y)), k):
            distances = [min(abs(y[j] - y[t]) for t in chosen)
                         for j in range(len(y))]
            if max(distances) <= 2:
                costs.append(sum(distances))
        if costs:
            best = min(costs)
            out[k] = (best, costs.count(best))
    return out


def verify():
    x, cuts = frozen()
    assert len(x) == 954 and len(cuts) == 28
    assert cuts[15] == 194 and cuts[17] == 245
    spectra = {}
    for pivots in (0, 1 << 15, 1 << 17, (1 << 15) | (1 << 17)):
        lower = optimum_counts_spectrum(closed_points(x, cuts, pivots))
        upper = optimum_counts_spectrum(closed_points(x, cuts, OTHER | pivots))
        # For all 662 high budgets, both the optimum cost and the exact
        # number of indexed optimal subsets coincide at sandwich endpoints.
        assert all(lower[k] == upper[k] for k in range(293, 955))
        spectra[pivots] = lower
    a = spectra[0]
    b = spectra[1 << 15]
    c = spectra[1 << 17]
    d = spectra[(1 << 15) | (1 << 17)]
    assert all(a[k][0] == b[k][0] == c[k][0] == d[k][0]
               for k in range(293, 955))
    assert all(a[k] == b[k] == c[k] == d[k]
               for k in range(315, 955))
    assert a[292] == b[292] == c[292] == d[292]

    rows = []
    for k in range(293, 315):
        n0, n15, n17, n2 = (t[k][1] for t in (a, b, c, d))
        joint = n2 - n15 - n17 + n0
        assert n15 > n0 and n17 > n0 and joint >= 0
        rows.append(dict(K=k, cost=a[k][0],
            none=str(n0), only15=str(n15), only17=str(n17),
            both=str(n2), both_only=str(joint)))
    assert [r['K'] for r in rows if int(r['both_only']) > 0] == list(range(294, 314))
    assert rows[0]['cost'] == 741 and rows[-1]['cost'] == 678
    assert a[292] == (744, 247939829006869892620615680)
    assert a[315] == (675, 402907218691036544772341760000)

    # An independent subset enumeration checks the imported path DP
    # for bounded inputs; it is not an exhaustive check of 2^28 masks.
    rng = random.Random(20261114)
    for n in range(3, 9):
        for _ in range(12):
            y = [0]
            for _ in range(n - 1):
                y.append(y[-1] + rng.randint(1, 4))
            assert optimum_counts_spectrum(y) == brute_spectrum(y)

    return dict(status='PASS_EXACT_R5_TWO_BIT_HIGH_BUDGET_OPTIMIZER',
        scientific_pin=PIN, event_count=954, original_cut_count=28,
        theorem_domain='all 2^28 closure masks, every K=293..954',
        endpoint_cases=8, checked_full_budget_endpoint_equalities=4 * 662,
        exact_optimal_index_family_effective_cut_indices=[15, 17],
        singleton_strict_budget_band=[293, 314],
        simultaneously_required_budget_band=[294, 313],
        sample_rows=[r for r in rows if r['K'] in (293, 294, 300, 313, 314)],
        all_twenty_two_rows=rows,
        small_independent_exhaustive_instances=72,
        mathematical_review='NOT_REVIEWED')


if __name__ == '__main__':
    print(json.dumps(verify(), ensure_ascii=False, indent=2))
