#!/usr/bin/env python3
"""Run the predecessor exact-rational endpoint certificate at i=201,...,220.

Dependency: ../brc_s23_av_plateau20_20261108_r1/VERIFY_PLATEAUX20_200.py
on the same immutable commit. Its check(i) includes strict log enclosures,
complete narrow-displacement enumeration and critical-cell coverage.
"""
from pathlib import Path
from runpy import run_path

prior = Path(__file__).resolve().parent.parent / 'brc_s23_av_plateau20_20261108_r1' / 'VERIFY_PLATEAUX20_200.py'
check = run_path(str(prior))['check']

if __name__ == '__main__':
    peak_cells = peak_narrow = 0
    for i in range(201, 221):
        r = check(i)
        assert r is not None, ('uncovered_critical_cell', i)
        ix, H, M, narrow, bmax, cells, used = r[:7]
        assert ix == i and H > 0 and M > 0
        peak_cells = max(peak_cells, cells)
        peak_narrow = max(peak_narrow, narrow)
        print('CERTIFIED', i, 'H', H, 'N', M, 'narrow', narrow,
              'beta_bound', bmax, 'cells', cells,
              'used_witnesses', used, flush=True)
    assert i == 220 and H == 83675522 and M == 456885742
    print('PASS_S23_AV_PLATEAUX_201_TO_220',
          'count', 20, 'last_H', H, 'last_N', M,
          'max_cells', peak_cells, 'max_narrow', peak_narrow)
