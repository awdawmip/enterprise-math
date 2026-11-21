#!/usr/bin/env python3
"""Exact minimal 2x2x2 underdetermination certificate; no physical model claim."""
from itertools import product

def law(model, x, y, a, b):
    assert model in (0, 1)
    assert all(z in (0, 1) for z in (x, y, a, b))
    return int(a == model and b == model)

for model in (0, 1):
    for x, y in product((0, 1), repeat=2):
        assert sum(law(model, x, y, a, b) for a, b in product((0, 1), repeat=2)) == 1
        for a in (0, 1):
            assert sum(law(model, x, y, a, b) for b in (0, 1)) == int(a == model)
        for b in (0, 1):
            assert sum(law(model, x, y, a, b) for a in (0, 1)) == int(b == model)
for x, y in product((0, 1), repeat=2):
    assert law(0, x, y, 0, 0) != law(1, x, y, 0, 0)
print("DISCCOMPAT_MISSING_READOUT_2X2X2_EXACT_PASS")
