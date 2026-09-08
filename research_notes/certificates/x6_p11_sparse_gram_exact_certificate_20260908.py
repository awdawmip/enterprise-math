#!/usr/bin/env python3
"""Exact companion certificate for min_{|det A|=11} Delta_6(A)=68.

Reuses the finite low-Delta enumeration primitives from the p=7 result-specific
certificate rather than duplicating a general mechanism. No floating point is
used in determinant decisions.
"""
from itertools import combinations_with_replacement
from pathlib import Path
import runpy

HERE = Path(__file__).resolve().parent
BASE = runpy.run_path(str(HERE / "x6_p7_sparse_gram_exact_certificate_20260908.py"))

D = BASE["D"]
BOUND = BASE["BOUND"]
CONFIGS = BASE["CONFIGS"]
diagonal_defect = BASE["diagonal_defect"]
matrix_from = BASE["matrix_from"]
det_bareiss = BASE["det_bareiss"]
delta_from = BASE["delta_from"]


def low_window_no_det_121():
    # Same analytic reduction as p=7: Delta<68 implies off-diagonal mass <=5,
    # diagonal range <=4, and minimum diagonal 1 or 2. The p=7 certificate
    # independently verifies min det(3I+E)=216 for every admissible E, so
    # minimum diagonal >=3 cannot produce determinant 121 either.
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
        max_mass = min(5, (BOUND - 1 - dd) // 12)
        for mass in range(max_mass + 1):
            if dd + 12 * mass >= BOUND:
                continue
            for conf in CONFIGS[mass]:
                checked += 1
                if det_bareiss(matrix_from(diag, conf)) == 121:
                    hits += 1

    assert checked == 1_150_826
    assert hits == 0
    return checked


def explicit_det11_delta68():
    a11 = [
        [-1, -1, 0, 0, 0, 1],
        [ 1,  0, 0,-1, 0, 1],
        [ 0,  1, 0, 0, 0, 1],
        [ 0,  0,-1, 0, 1, 0],
        [ 0,  0, 1, 1, 1, 0],
        [ 0,  0, 1,-1, 0,-1],
    ]
    assert abs(det_bareiss(a11)) == 11

    g = [[sum(a11[k][i] * a11[k][j] for k in range(D)) for j in range(D)] for i in range(D)]
    assert det_bareiss(g) == 121

    diag = tuple(g[i][i] for i in range(D))
    # Compute Delta directly from Gram, preserving exact integers.
    tr = sum(g[i][i] for i in range(D))
    tr_g2 = sum(g[i][j] * g[j][i] for i in range(D) for j in range(D))
    delta = 6 * tr_g2 - tr * tr
    assert delta == 68

    return g


if __name__ == "__main__":
    checked = low_window_no_det_121()
    g = explicit_det11_delta68()
    print({
        "status": "EXACT_CERTIFICATE_PASSED",
        "low_window_matrices_checked": checked,
        "det121_candidates_with_delta_lt_68": 0,
        "explicit_det11_delta": 68,
        "conclusion": "min_{|det A|=11} Delta_6(A)=68",
        "boundary": "Result-specific exact finite certificate; no Foundation promotion.",
    })
