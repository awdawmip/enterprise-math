#!/usr/bin/env python3
"""Exact, finite signed-Z3 vs historical fixed-positive-two-axis PathSqrt scope.

Task RS-X6-LEGACY-PLANE-RECONCILIATION. P000/frozen inputs unchanged.
Author-side certificate only; not independent admission or R063 original rerun.
"""
from collections import Counter
from math import factorial

N = 2500
R = 50

def word_count(d):
    t = sum(abs(v) for v in d)
    result = factorial(t)
    for v in d:
        result //= factorial(abs(v))  # exact division step? see below
    return result

# Multinomial divisions are integral successively: t! / a! / b! / c!.
positive_roots = [(a, b) for a in range(R + 1) for b in range(R + 1)
                  if a*a + b*b == N]
assert positive_roots == [(0, 50), (14, 48), (30, 40),
                          (40, 30), (48, 14), (50, 0)]
sector_mass = sum(word_count((a, b)) for a, b in positive_roots)
assert sector_mass == 110695538274255714208

squares = {k*k: k for k in range(-R, R + 1)}
# Iterate a,b and solve the final square exactly (including signs).
signed_cells = set()
for a in range(-R, R + 1):
    for b in range(-R, R + 1):
        d = N - a*a - b*b
        if d < 0:
            continue
        if d == 0:
            signed_cells.add((a, b, 0))
        else:
            c = squares.get(d)
            if c is not None:
                signed_cells.add((a, b, c))
                signed_cells.add((a, b, -c))
assert len(signed_cells) == 150
shapes = Counter(tuple(sorted(abs(v) for v in d)) for d in signed_cells)
assert shapes == Counter({(0, 0, 50): 6, (0, 14, 48): 24,
                          (0, 30, 40): 24, (18, 24, 40): 48,
                          (24, 30, 32): 48})
signed_mass = sum(word_count(d) for d in signed_cells)
assert signed_mass == 26860799510260072787603759892561716013678
assert word_count((18, 24, 40)) == 146667819424252202137117683587961000
assert word_count((24, 30, 32)) == 559453321977660597511933995509550527400
# A fixed two-generator word cannot have nonzero third coordinate.
assert (18, 24, 40) in signed_cells
assert (18, 24, 40) not in {(a, b, 0) for a, b in positive_roots}
print("PASS_X6_R063_FIXED_SECTOR_VS_SIGNED_THREE_AXIS_EXACT")
print("fixed_positive_root_count", len(positive_roots))
print("fixed_positive_path_mass", sector_mass)
print("signed_three_axis_endpoint_count", len(signed_cells))
print("signed_three_axis_path_mass", signed_mass)
print("signed_shapes", dict(sorted(shapes.items())))
