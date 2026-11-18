#!/usr/bin/env python3
"""Reproduce exact 221..268 S23/AV plateaux on the same PR branch.
Dependency blob 261d7e22da0e62d667009cb50acfe77ac4e35c3f.
The original local test ran the same source's scoped literal port; this runner
imports the upstream checker by path instead of duplicating the 3,983-byte core.
"""
from pathlib import Path
from runpy import run_path
upstream = Path(__file__).resolve().parent.parent / "brc_s23_av_plateau20_20261108_r1" / "VERIFY_PLATEAUX20_200.py"
check = run_path(str(upstream))["check"]
if __name__ == "__main__":
    total = peak_cells = peak_narrow = 0
    for i in range(221, 269):
        result = check(i)
        assert result is not None, ("failed_coverage", i)
        ix, H, M, narrow, beta_bound, cells, witnesses = result[:7]
        assert ix == i
        print("CERTIFIED", i, "H", H, "N", M, "narrow", narrow,
              "beta_bound", beta_bound, "cells", cells,
              "used_witnesses", witnesses, flush=True)
        total += cells
        peak_cells = max(peak_cells, cells)
        peak_narrow = max(peak_narrow, narrow)
    assert i == 268 and H == 101931894 and M == 556486962
    assert total == 1394515 and peak_cells == 34798 and peak_narrow == 82
    print("PASS_S23_AV_PLATEAUX_221_TO_268",
          "count", 48, "total_cells", total,
          "last_H", H, "last_N", M, flush=True)
