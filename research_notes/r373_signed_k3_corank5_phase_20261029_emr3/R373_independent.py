#!/usr/bin/env python3
"""Independent R369 diagonal-vs-raw-D symbolic verification of R373 eleven polynomials."""
import sys
from pathlib import Path
from sympy import expand
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
sys.path.insert(0,str(HERE.parent/'r369_signed_k3_branch_top_catalan_20261029_emr3'))
from R373_reproduce import coeffs, x
from R369_check import compute_rows
expected=coeffs()
rows,_=compute_rows(x,5)
assert len(rows[5])==11
for j in range(11):
    assert expand(rows[5][j]-expected[j])==0, j
print('R373_INDEPENDENT_RAW_D_CROSSCHECK_11_OF_11_PASS')
