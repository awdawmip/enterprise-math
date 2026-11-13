#!/usr/bin/env python3
"""PREFIX-749-R6; exact Gamma 8x8 closed-cell checks under frozen science.
Run next to PREFIX741_R6_INNER_STRIP_194.py (standard library only).
"""
import subprocess
import sys
from fractions import Fraction

CASES = ((10, 50, (-78645845, -20639281, 8455657), -194688514),
         (10, 51, (-84950051, -25907227, 3704401), -203076218))

def microfloor(value):
    u = value * 1000000
    return u.numerator // u.denominator

def check_one(i, j):
    from PREFIX741_R6_INNER_STRIP_194 import (lower_cell, emu, eW, oldmu, oldW, pair, tails)
    case = next((c for c in CASES if c[:2] == (i, j)), None)
    assert case is not None, (i, j)
    expected, old_expected = case[2:]
    values = []
    for s in (2, 4, 8):
        lower = lower_cell(i, j, s, emu, eW)
        values.append(microfloor(lower))
        pair.cache_clear()
        tails.cache_clear()
    assert tuple(values) == expected, (i, j, values, expected)
    assert lower > Fraction(3)
    old = lower_cell(i, j, 1, oldmu, oldW)
    assert microfloor(old) == old_expected, (i, j, microfloor(old))
    print("PASS", i, j, tuple(values), "old", microfloor(old), flush=True)

if __name__ == "__main__":
    if len(sys.argv) == 1:
        for i, j, *_ in CASES:
            subprocess.run([sys.executable, __file__, f"{i},{j}"], check=True)
        originals = {(i, j) for i, j, *_ in CASES}
        certified = originals | {(j, i) for i, j in originals}
        assert len(certified) == 4
        assert 141980 + len(certified) == 141984
        print("ALL_CHECKS_PASS PREFIX749-R6 2+2=4", flush=True)
    elif len(sys.argv) == 2:
        i, j = map(int, sys.argv[1].split(","))
        check_one(i, j)
    else:
        raise SystemExit("usage: checker.py [10,50 | 10,51]")
