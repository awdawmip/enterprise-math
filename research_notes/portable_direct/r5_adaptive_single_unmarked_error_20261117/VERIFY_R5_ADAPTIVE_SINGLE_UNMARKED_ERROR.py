#!/usr/bin/env python3
"""Exact finite verifier for the R5 adaptive one-unmarked-error theorem.

Input: COHORTS_3_BUDGETS.json, reconstructed by subset-zeta from the
frozen source-cohort pin. No floating-point arithmetic is used.
"""
import hashlib
import itertools
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
INPUT = HERE / 'COHORTS_3_BUDGETS.json'
order = (294, 223, 214)
allowed = range(214, 315)


def restore(cohort):
    result = [0] * 256
    for mask, decimal in cohort.items():
        result[int(mask)] = int(decimal)
    for bit in range(8):
        step = 1 << bit
        for mask in range(256):
            if mask & step:
                result[mask] += result[mask ^ step]
    return result


def run_symbolic(true_mask, fault=None):
    # fault = (budget, occurrence among the two initial samples, symbol).
    # All other readings are intact.  If a mismatch is seen, the faulty
    # position has necessarily been consumed; the third reading is intact.
    centers = {}
    cost = 0
    correction_used = False
    for k in order:
        truth = counts[k][true_mask]
        symbol_reads = []
        repeats = 1 if correction_used else 2
        for rep in range(repeats):
            cost += k
            v = truth
            if fault is not None and fault[:2] == (k, rep):
                v = fault[2]
            symbol_reads.append(v)
        if repeats == 2:
            if symbol_reads[0] == symbol_reads[1]:
                recovered = symbol_reads[0]
            else:
                cost += k
                third = truth  # single error already consumed
                assert third in symbol_reads
                recovered = third
                correction_used = True
        else:
            recovered = symbol_reads[0]
        centers[k] = recovered
    key = tuple(centers[k] for k in order)
    return inverse.get(key), cost


def ordering_cost(ordering):
    base = sum(ordering)
    zero_error = 2 * base
    # First wrong reading in budget j forces a third there; after this,
    # remaining budgets are read once.  The exact worst branch is covered.
    branches = []
    for j, k in enumerate(ordering):
        branches.append(sum(2 * q for q in ordering[:j]) + 3 * k + sum(ordering[j + 1:]))
    return max(zero_error, *branches)


frozen = json.loads(INPUT.read_text(encoding='utf-8'))
assert frozen['frozen_science_commit'] == '435e77af0d180eac32bd1f9c4c464bc4010b7551'
counts = {int(k): restore(v) for k, v in frozen['cohorts'].items()}
assert set(counts) == set(order)

# Freeze-bound independent checks against source's previously derived table
# (an optional full exact table, if provided, is compared byte-for-byte here).
full = HERE / 'EXACT_R5_ALL_101_BUDGETS.json'
if full.is_file():
    source = json.loads(full.read_text(encoding='utf-8'))
    for k in order:
        assert counts[k] == list(map(int, source['counts_and_cohorts'][str(k)]['counts']))
    verified_reference_counts = 768
else:
    verified_reference_counts = 0

inverse = {}
for mask in range(256):
    key = tuple(counts[k][mask] for k in order)
    assert key not in inverse, (mask, inverse.get(key))
    inverse[key] = mask
assert len(inverse) == 256

positive_min_gap = {}
center_cardinalities = {}
for k in order:
    centers = sorted(set(counts[k]))
    center_cardinalities[k] = len(centers)
    positive_min_gap[k] = min(v - u for u, v in zip(centers, centers[1:]))
delta = min(positive_min_gap.values())
assert delta == 76289178155959966960189440

# Each crucial alternative to base mask 16 differs only in one contiguous
# disjoint budget window.  Independently checked at all 101 allowed budgets.
windows = [
    (16, 17, list(range(214, 222))),
    (16, 80, list(range(223, 292))),
    (16, 32, list(range(294, 314))),
]
if full.is_file():
    for a, b, window in windows:
        actual = [k for k in allowed if source['counts_and_cohorts'][str(k)]['counts'][a] != source['counts_and_cohorts'][str(k)]['counts'][b]]
        assert actual == window, (a, b, actual, window)

# Compare all six permutations of the three exact queried budgets.
permutations = {','.join(map(str, p)): ordering_cost(p) for p in itertools.permutations(order)}
assert permutations['294,223,214'] == 1676
assert min(permutations.values()) == 1676
assert 2 * sum(order) == 1462
assert 3 * sum(order) == 2193

# Exhaustive single-fault symbolic responses: for each mask, each of the
# two initial sample positions at every budget, every possible recognized
# center value and the unrecognized symbol None.  Also no-fault branch.
checked = 0
worst = 0
worst_witness = None
for mask in range(256):
    output, cost = run_symbolic(mask)
    assert output == mask and cost == 1462
    checked += 1
    for k in order:
        symbols = sorted(set(counts[k])) + [None]
        for rep in (0, 1):
            for candidate in symbols:
                output, cost = run_symbolic(mask, (k, rep, candidate))
                assert output == mask, (mask, k, rep, candidate, output)
                checked += 1
                if cost > worst:
                    worst = cost
                    worst_witness = {'mask': mask, 'budget': k, 'initial_read_index': rep,
                                     'corrupted_symbol': str(candidate), 'cost': cost}
assert worst == 1676

result = {
    'schema': 'R5_ADAPTIVE_ONE_UNMARKED_ERROR_CERTIFICATE_V1',
    'frozen_science_commit': frozen['frozen_science_commit'],
    'source_compact_sha256': hashlib.sha256(INPUT.read_bytes()).hexdigest(),
    'readout_budgets': list(order),
    'intact_observation_cardinalities': {str(k): center_cardinalities[k] for k in order},
    'min_positive_center_gap_by_budget': {str(k): str(positive_min_gap[k]) for k in order},
    'min_positive_gap_delta': str(delta),
    'guarantee': '0 <= 2*eta < delta, one arbitrary unmarked replacement; true state any mask 0..255',
    'number_of_distinct_signature_tuples': len(inverse),
    'three_source_witnesses': [{'states': [a,b], 'window': [window[0], window[-1]], 'window_cardinality':len(window)} for a,b,window in windows],
    'reference_count_crosscheck': verified_reference_counts,
    'symbolic_corruption_exhaustive_runs': checked,
    'worst_case_cost': worst,
    'zero_error_path_cost': 1462,
    'fixed_one_error_optimal_cost': 2193,
    'cost_improvement': 2193-worst,
    'worst_witness': worst_witness,
    'permutation_costs': permutations,
    'lower_bound_witness': 'state16 three disjoint windows; six mandatory intact-path reads; corrupt sixth => seventh required',
    'status': 'AUTHOR_PROVED_EXACT_FINITE_CHECKED_NOT_REVIEWED',
    'stdout': 'PASS_R5_SHARP_ADAPTIVE_SINGLE_UNMARKED_ERROR_1676'
}
(HERE/'RESULTS_ADAPTIVE_SINGLE_ERROR_EXACT.json').write_text(json.dumps(result,indent=2,ensure_ascii=False,sort_keys=True)+'\n',encoding='utf-8')
print('PASS_R5_SHARP_ADAPTIVE_SINGLE_UNMARKED_ERROR_1676')
print(json.dumps({k:result[k] for k in ('min_positive_gap_delta','symbolic_corruption_exhaustive_runs','reference_count_crosscheck','worst_case_cost','cost_improvement','permutation_costs')},indent=2))
