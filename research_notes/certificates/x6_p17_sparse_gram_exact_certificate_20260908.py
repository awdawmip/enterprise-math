#!/usr/bin/env python3
"""Exact certificate for min_{|det A|=17} Delta_6(A)=72.

This is the first continuation requiring minimum Gram diagonal 3 in the finite
window. It reuses the exact integer enumeration primitives from the p=7
certificate and extends the diagonal window by one layer.
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

BOUND = 72
TARGET_DET = 289


def min_det_four_I_plus_E():
    # Delta<72 gives M<=5. Enumerate every admissible off-diagonal E and
    # verify the minimum determinant at diagonal 4. The same spectral argument
    # used in the p=7 note makes 4I+E positive definite; larger diagonals only
    # increase determinant.
    best = None
    for mass in range(6):
        for conf in CONFIGS[mass]:
            det = det_bareiss(matrix_from((4, 4, 4, 4, 4, 4), conf))
            if best is None or det < best:
                best = det
    assert best == 2560
    return best


def low_window_no_det_289():
    # Pairwise diagonal range is at most 4 because the minimum D for range 5 is
    # 77, already above the bound. Since 4I+E has determinant >=2560>289, a
    # determinant-289 candidate below 72 has minimum diagonal 1,2,or3.
    diagonal_patterns = []
    for minimum in (1, 2, 3):
        for diag in combinations_with_replacement(range(minimum, minimum + 5), D):
            if diag[0] != minimum:
                continue
            dd = diagonal_defect(diag)
            if dd < BOUND:
                diagonal_patterns.append((diag, dd))

    checked = 0
    hits = 0
    for diag, dd in diagonal_patterns:
        max_mass = min(5, (BOUND - 1 - dd) // 12)
        for mass in range(max_mass + 1):
            if dd + 12 * mass >= BOUND:
                continue
            for conf in CONFIGS[mass]:
                checked += 1
                if det_bareiss(matrix_from(diag, conf)) == TARGET_DET:
                    hits += 1

    assert checked == 3_057_843
    assert hits == 0
    return checked


def explicit_det17_delta72():
    # Exact equality representative obtained in the research derivation.
    a17 = [
        [-1, -1,  0,  0,  0, -1],
        [ 1, -1, -1,  0,  0,  0],
        [ 0,  0,  0, -1,  1,  1],
        [ 0,  1, -1,  0,  1, -1],
        [ 0,  0,  0,  1,  1,  0],
        [ 0,  0,  1, -1,  0, -1],
    ]
    assert abs(det_bareiss(a17)) == 17

    g = [[sum(a17[k][i] * a17[k][j] for k in range(D)) for j in range(D)] for i in range(D)]
    assert det_bareiss(g) == TARGET_DET

    tr = sum(g[i][i] for i in range(D))
    tr_g2 = sum(g[i][j] * g[j][i] for i in range(D) for j in range(D))
    delta = 6 * tr_g2 - tr * tr
    assert delta == 72
    return g


if __name__ == "__main__":
    floor4 = min_det_four_I_plus_E()
    checked = low_window_no_det_289()
    explicit_det17_delta72()
    print({
        "status": "EXACT_CERTIFICATE_PASSED",
        "min_det_4I_plus_E": floor4,
        "low_window_matrices_checked": checked,
        "det289_candidates_with_delta_lt_72": 0,
        "explicit_det17_delta": 72,
        "conclusion": "min_{|det A|=17} Delta_6(A)=72",
        "boundary": "Result-specific exact finite certificate; no Foundation promotion.",
    })
