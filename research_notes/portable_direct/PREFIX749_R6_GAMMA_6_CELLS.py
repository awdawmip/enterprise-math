#!/usr/bin/env python3
"""PREFIX-749-R6: exact closed-cell envelope, frozen scientific pin f42f2906d77f24085c123f3ccfe9667d41caa96d.
Run alongside the exact GitHub module PREFIX741_R6_INNER_STRIP_194.py.
Usage: python PREFIX749_R6_GAMMA_6_CELLS.py [i,j]
Without arguments, each original cell runs in its own clean Python child process.
"""
import subprocess
import sys
from fractions import Fraction

ROWS = ((10, 50, -78645845, -20639281, 8455657),
        (10, 51, -84950051, -25907227, 3704401),
        (11, 52, -86683906, -26603110, 3524919))

def floor_micro(x):
    y = x * 1000000
    return y.numerator // y.denominator

def check_cell(i, j):
    from PREFIX741_R6_INNER_STRIP_194 import lower_cell, emu, eW, pair, tails
    expected = next(row[2:] for row in ROWS if row[:2] == (i, j))
    observed = []
    for split in (2, 4, 8):
        bound = lower_cell(i, j, split, emu, eW)
        observed.append(floor_micro(bound))
        if split == 8:
            assert bound > Fraction(3, 1)
        pair.cache_clear()
        tails.cache_clear()
    assert tuple(observed) == expected, (i, j, observed, expected)
    print("PASS", i, j, tuple(observed), flush=True)

if __name__ == "__main__":
    if len(sys.argv) == 2:
        i, j = map(int, sys.argv[1].split(","))
        assert (i, j) in {(a, b) for a, b, *_ in ROWS}
        check_cell(i, j)
    elif len(sys.argv) == 1:
        for i, j, *_ in ROWS:
            subprocess.run([sys.executable, __file__, f"{i},{j}"], check=True)
        originals = {(i, j) for i, j, *_ in ROWS}
        reflected = originals | {(j, i) for i, j in originals}
        assert len(reflected) == 6
        print("ALL_CHECKS_PASS PREFIX749-R6 3+3=6", flush=True)
    else:
        raise SystemExit("usage: PREFIX749_R6_GAMMA_6_CELLS.py [i,j]")
