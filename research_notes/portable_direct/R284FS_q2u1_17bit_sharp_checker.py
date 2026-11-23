#!/usr/bin/env python3
"""Exact 17-bit obstruction: extends the sibling R284FR integer checker.

Usage from a checkout preserving both sibling files:
    python research_notes/portable_direct/R284FS_q2u1_17bit_sharp_checker.py
"""
from importlib.util import module_from_spec, spec_from_file_location
from math import comb
from pathlib import Path

base = Path(__file__).with_name('R284FR_q2u1_16bit_obstruction_checker.py')
spec = spec_from_file_location('r284fr_exact', base)
m = module_from_spec(spec)
spec.loader.exec_module(m)
m.N = 17

PAIR_TYPES = [tuple(p - 1 for p in range(1, 8)
                    if m.PAT[p][0][i] != m.PAT[p][0][j])
              for i, j in m.PAIRS]
CUTS = [m.cutsets(i, j) for i, j in m.PAIRS]
DIST_THRESHOLDS = (9, 9, 9, 9, 7, 7)

EXPECTED_EDGE0_SURVIVORS = [
    (0, 0, 0, 0, 9, 7, 1),
    (0, 0, 0, 0, 9, 8, 0),
    (0, 0, 0, 0, 10, 7, 0),
    (0, 0, 0, 1, 8, 7, 1),
    (0, 0, 0, 1, 9, 7, 0),
    (0, 0, 1, 0, 8, 7, 1),
    (0, 0, 1, 0, 9, 7, 0),
    (0, 0, 5, 0, 6, 6, 0),
    (0, 1, 0, 0, 8, 7, 1),
    (0, 1, 0, 0, 9, 7, 0),
    (1, 0, 0, 0, 9, 7, 0),
]


def main():
    total = distance_pass = endpoint_pass = 0
    edge0 = []
    for x in m.compositions(17, 7):
        total += 1
        if any(sum(x[p] for p in ps) < threshold
               for ps, threshold in zip(PAIR_TYPES, DIST_THRESHOLDS)):
            continue
        distance_pass += 1
        if not all(any(sum(x[p] for p in ps) >= threshold
                       for ps, threshold in graph)
                   for graph in CUTS):
            continue
        endpoint_pass += 1
        words, positions, stable = m.words_and_phases(x)
        force = m.forced_read_masks(stable)
        if not m.has_locally_safe_order(0, words, positions, stable, force):
            continue
        edge0.append(x)
        assert not m.has_locally_safe_order(1, words, positions, stable, force), x

    assert total == comb(23, 6) == 100947, total
    assert distance_pass == 3955, distance_pass
    assert endpoint_pass == 208, endpoint_pass
    assert edge0 == EXPECTED_EDGE0_SURVIVORS, edge0
    print(f'n=17 histograms: {total}; distance-pass: {distance_pass}')
    print(f'all six stable read cuts pass: {endpoint_pass}')
    print(f'edge 0->1 safe-prefix-path survives: {len(edge0)}')
    print(f'edge 1->2 safe-prefix-path survives: 0')
    print('first-edge survivors:', edge0)
    print('No correct 17-bit q=2,u=1 protocol.')
    print('Using R284FR (n>=17) and R284FE 18-bit construction: n_min(2,1)=18')


if __name__ == '__main__':
    main()
