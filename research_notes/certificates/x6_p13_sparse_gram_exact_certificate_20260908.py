#!/usr/bin/env python3
"""Exact companion certificate for min_{|det A|=13} Delta_6(A)=56.

Reuses exact integer enumeration primitives from the p=7 certificate. The
smaller target bound 56 leaves only 215,558 matrices after analytic reduction.
"""
from itertools import combinations_with_replacement
from pathlib import Path
import runpy

HERE = Path(__file__).resolve().parent
BASE = runpy.run_path(str(HERE / "x6_p7_sparse_gram_exact_certificate_20260908.py"))

D = BASE["D"]
CONFIGS = BASE["CONFIGS"]
diagonal_defect = BASE["diagonal_defect"]
matrix_from = BASE["matrix_from"]
det_bareiss = BASE["det_bareiss"]

BOUND = 56
TARGET_DET = 169


def low_window_no_det_169():
    # Delta<56 implies M<=4 and diagonal range <=4. As in the p=7 proof,
    # minimum diagonal >=3 can be excluded: for M<=4 the all-3 determinant
    # lower bound is even larger than in the M<=5 scan, hence >169.
    diagonal_patterns = []
    for minimum in (1, 2):
        for diag in combinations_with_replacement(range(minimum, minimum + 5), D):
            if diag[0] != minimum:
                continue
            dd = diagonal_defect(diag)
            if dd < BOUND:
                diagonal_patterns.append((diag, dd))

    checked = 0
    hits = 0
    for diag, dd in diagonal_patterns:
        max_mass = min(4, (BOUND - 1 - dd) // 12)
        for mass in range(max_mass + 1):
            if dd + 12 * mass >= BOUND:
                continue
            for conf in CONFIGS[mass]:
                checked += 1
                if det_bareiss(matrix_from(diag, conf)) == TARGET_DET:
                    hits += 1

    assert checked == 215_558
    assert hits == 0
    return checked


def explicit_det13_delta56():
    a13 = [
        [1,0,0,0,-1,-1],
        [0,1,1,-1,0,0],
        [1,0,0,0,1,0],
        [0,1,-1,0,0,0],
        [0,0,1,1,0,1],
        [0,0,0,1,1,-1],
    ]
    assert abs(det_bareiss(a13)) == 13
    g = [[sum(a13[k][i] * a13[k][j] for k in range(D)) for j in range(D)] for i in range(D)]
    assert det_bareiss(g) == TARGET_DET
    tr = sum(g[i][i] for i in range(D))
    tr_g2 = sum(g[i][j] * g[j][i] for i in range(D) for j in range(D))
    delta = 6 * tr_g2 - tr * tr
    assert delta == 56
    return g


if __name__ == "__main__":
    checked = low_window_no_det_169()
    g = explicit_det13_delta56()
    print({
        "status": "EXACT_CERTIFICATE_PASSED",
        "low_window_matrices_checked": checked,
        "det169_candidates_with_delta_lt_56": 0,
        "explicit_det13_delta": 56,
        "conclusion": "min_{|det A|=13} Delta_6(A)=56",
        "boundary": "Result-specific exact finite certificate; no Foundation promotion.",
    })
