#!/usr/bin/env python3
"""Regenerate the pinned r463 F7 B12 rational table, then check it exactly.

Run from anywhere with Python, SciPy and NumPy. The old r462 linear model
is reused unchanged; only rationalization denominator and frozen output differ.
"""
import argparse
import hashlib
import json
from pathlib import Path
import numpy as np
from scipy.optimize import linprog

import CBRC_F7_R462_BOX12_IPM_INTEGER_ROUND_CHECK_20261122 as old
from CBRC_F7_R463_B12_FIXED_INTEGER_CERT_20261122 import verify

M = 10**13
EXPECTED_SHA256 = "5026e4e8d9ccecd26806d95a096af4f41ff3c4507ea5ec7a43552e1a1edf68b6"

def regenerate(path):
    A, rhs = old.build_linear_inequalities()
    assert len(old.coordinates) == 3046 and A.shape[0] == 341492
    result = linprog(
        np.zeros(A.shape[1]), A_ub=A, b_ub=rhs, bounds=(0, None),
        method="highs-ipm", options={"time_limit":120}
    )
    if not result.success:
        raise RuntimeError(result.message)
    increments = {
        key: int(round(float(result.x[i])*M))
        for key,i in old.coordinates.items()
    }
    triples = sorted((a,b,n) for (a,b),n in increments.items() if n != 0)
    raw = json.dumps(triples,separators=(",",":")).encode()
    digest = hashlib.sha256(raw).hexdigest()
    if digest != EXPECTED_SHA256:
        raise RuntimeError(
            "LP generated a different candidate; retain the fixed artifact. "
            f"Observed {digest}; expected {EXPECTED_SHA256}."
        )
    Path(path).write_bytes(raw)
    verify(path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("output_json")
    regenerate(parser.parse_args().output_json)
