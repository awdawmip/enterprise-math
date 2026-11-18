#!/usr/bin/env python3
"""Exact S23/AV auxiliary plateaux 269–300; upstream core blob 261d7e22da0e62d667009cb50acfe77ac4e35c3f."""
from pathlib import Path
from runpy import run_path
core = Path(__file__).resolve().parent.parent / "brc_s23_av_plateau20_20261108_r1" / "VERIFY_PLATEAUX20_200.py"
check = run_path(str(core))["check"]
if __name__ == "__main__":
    total, peak_narrow, peak_cells = 0, 0, 0
    for i in range(269, 301):
        result = check(i)
        assert result is not None, ("exact_coverage_failed", i)
        ix, H, M, narrow, bmax, cells, used = result[:7]
        assert ix == i
        total += cells
        peak_narrow = max(peak_narrow, narrow)
        peak_cells = max(peak_cells, cells)
        print("CERTIFIED", i, "H", H, "N", M, "narrow", narrow,
              "beta_bound", bmax, "cells", cells, "used_witnesses", used,
              flush=True)
    assert i == 300 and H == 114102835 and M == 622887919
    assert total == 1256627 and peak_narrow == 92 and peak_cells == 43635
    print("PASS_S23_AV_PLATEAUX_269_TO_300", "count", 32,
          "total_cells", total, "last_H", H, "last_N", M, flush=True)
