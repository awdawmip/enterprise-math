#!/usr/bin/env python3
"""R284CQ full-population independent enumeration cross-check (4,194,304 distances).

Run beside R284CO_spectral_witness_checker.py, the two earlier JSON
certificates and R284CQ_third_spectrum_checker.py. This reuses the frozen
codeword generator but checks the third-order spectrum independently of
the interval-event sweep.
"""
import time
from R284CO_spectral_witness_checker import words, arcs, dist
from R284CQ_third_spectrum_checker import compute

expected = compute()
A, W = arcs(), words()
top = [[] for _ in range(64)]
t0 = time.perf_counter()
for x in W:
    ordered = sorted(dist(x, a) for a in A)
    for j, d in enumerate(ordered):
        row = top[j]
        if len(row) < 3:
            row.append((d, x))
            row.sort(reverse=True)
        elif d > row[-1][0]:
            row[-1] = (d, x)
            row.sort(reverse=True)
for j in range(1, 64):
    assert top[j][2] == (
        expected['third_values_k2_to_k64'][j - 1],
        expected['third_witness_residues_k2_to_k64'][j - 1]
    )
    assert top[j][0][0] > top[j][1][0] > top[j][2][0]
print({
    'verified_third_rank_levels': 63,
    'all_population_distance_evaluations': len(W) * len(A),
    'exact_agreement': True,
    'seconds_single_host': round(time.perf_counter() - t0, 6)
})
