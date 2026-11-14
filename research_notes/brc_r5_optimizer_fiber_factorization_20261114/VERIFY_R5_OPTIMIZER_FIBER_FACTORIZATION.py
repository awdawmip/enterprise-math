#!/usr/bin/env python3
"""Full-budget interval-factorization certificate for frozen R5 indexed optimizers.

Run from the repository root, or with these two inherited source modules intact:
 research_notes/brc_r5_exact_cost_spectrum_20261114/VERIFY_R5_COST_SPECTRA.py
 research_notes/brc_r5_exact_cost_spectrum_20261114/VERIFY_R5_OPTIMAL_WITNESSES.py
Frozen science input: 435e77af0d180eac32bd1f9c4c464bc4010b7551.
"""
import json
import sys
from pathlib import Path
from itertools import combinations
from random import Random

SOURCE = Path(__file__).resolve().parents[1] / "brc_r5_exact_cost_spectrum_20261114"
sys.path.insert(0, str(SOURCE))
from VERIFY_R5_COST_SPECTRA import frozen
from VERIFY_R5_OPTIMAL_WITNESSES import optimum_counts_spectrum

INERT_COST = (0, 1, 7, 14, 15, 17, 18, 19, 20, 21, 22, 23, 24)
ACTIVE_OPT = (15, 17)
INERT_OPT = tuple(i for i in INERT_COST if i not in ACTIVE_OPT)
PIN = '435e77af0d180eac32bd1f9c4c464bc4010b7551'

def minplus_tie_product(p, q):
    """Convolution of (minimum cost, number of indexed minimizers)."""
    out = {}
    for a, (cost_a, ways_a) in p.items():
        for b, (cost_b, ways_b) in q.items():
            k = a + b
            candidate = cost_a + cost_b
            old = out.get(k)
            if old is None or candidate < old[0]:
                out[k] = (candidate, ways_a * ways_b)
            elif candidate == old[0]:
                out[k] = (candidate, old[1] + ways_a * ways_b)
    return out

def brute_spectrum(y):
    out = {}
    for k in range(1, len(y) + 1):
        values = []
        for chosen in combinations(range(len(y)), k):
            distances = [min(abs(y[t] - y[j]) for j in chosen)
                         for t in range(len(y))]
            if max(distances) <= 2:
                values.append(sum(distances))
        if values:
            best = min(values)
            out[k] = (best, values.count(best))
    return out

def verify():
    x, cut_locations = frozen()
    assert len(x) == 954 and len(cut_locations) == 28
    starts = [0] + [q + 1 for q in cut_locations]
    ends = [q + 1 for q in cut_locations] + [len(x)]
    profiles = {}
    for a in range(29):
        for b in range(a, 29):
            local_cuts = set(cut_locations[a:b])
            shift = 0
            y = []
            for t in range(starts[a], ends[b]):
                y.append(x[t] - shift)
                if t in local_cuts:
                    shift += 1
            profiles[a, b] = optimum_counts_spectrum(y)
    assert len(profiles) == 435
    summary = {}
    checked_intervals = 0
    checked_budget_slices = 0
    for i in INERT_COST:
        strictly_new = 0
        changed_costs = 0
        new_budget = 0
        comparisons = 0
        first_difference = None
        for a in range(i + 1):
            for b in range(i + 1, 29):
                comparisons += 1
                joined = profiles[a, b]
                split = minplus_tie_product(profiles[a, i], profiles[i + 1, b])
                # An unclosed gap is length 3; joining preserves every
                # previously feasible center-index set and its cost.
                assert set(split).issubset(joined), (i, a, b, set(split)-set(joined))
                for k, (old_cost, old_count) in split.items():
                    new_cost, new_count = joined[k]
                    assert new_cost <= old_cost
                    checked_budget_slices += 1
                    if new_cost != old_cost:
                        changed_costs += 1
                    if new_cost == old_cost:
                        assert new_count >= old_count
                    if new_count != old_count:
                        strictly_new += 1
                        if first_difference is None:
                            first_difference = dict(run=[a, b], K=k,
                                unclosed_cost=old_cost, closed_cost=new_cost,
                                unclosed_count=str(old_count),
                                closed_count=str(new_count))
                new_budget += len(set(joined)-set(split))
        checked_intervals += comparisons
        summary[str(i)] = dict(straddling_intervals=comparisons,
            differing_existing_budget_pairs=strictly_new,
            differing_cost_pairs=changed_costs,
            newly_feasible_budget_pairs=new_budget,
            first_difference=first_difference)
        if i in INERT_OPT:
            assert strictly_new == changed_costs == new_budget == 0
        else:
            assert strictly_new > 0 and changed_costs == new_budget == 0
    assert checked_intervals == 1916
    assert sum(summary[str(i)]['straddling_intervals'] for i in INERT_OPT)==1510
    assert (summary['15']['differing_existing_budget_pairs'],
            summary['17']['differing_existing_budget_pairs']) == (2198, 2183)
    rng = Random(20261114)
    small_cases = 0
    for n in range(3, 9):
        for trial in range(24):
            y = [0]
            for _ in range(n-1):
                y.append(y[-1] + rng.randint(1, 4))
            assert optimum_counts_spectrum(y) == brute_spectrum(y)
            small_cases += 1
    return dict(status='PASS_EXACT_R5_GLOBAL_OPTIMIZER_FIBER_FACTORIZATION',
        science_pin=PIN,
        scope='954 indexed 1D integer event centers; radius 2',
        total_closure_patterns=1<<28,
        local_interval_profiles=len(profiles),
        local_join_split_interval_checks=checked_intervals,
        exact_full_budget_join_split_comparisons=checked_budget_slices,
        globally_cost_and_optimizer_inert_cut_indices=list(INERT_OPT),
        globally_cost_inert_but_optimizer_active_cut_indices=list(ACTIVE_OPT),
        local_counts=summary,
        independently_bruteforced_small_coordinate_instances=small_cases,
        mathematical_review='NOT_REVIEWED')

if __name__ == '__main__':
    result = verify()
    print(json.dumps(result, ensure_ascii=False, indent=2))
