#!/usr/bin/env python3
"""X6 R063 N=2500: full signed six-axis Cell shell and shortest-path N-BRC.

Exact integer certificate, AUTHOR-VERIFIED / UNREVIEWED / NOT_ADMITTED.
Frozen P000 X6 norm and R063 fixed two-positive-axis result remain unchanged.
No claim of executing R063's original 1<=r<=512 native benchmark.
"""
from collections import defaultdict
from math import comb, factorial, isqrt

N = 2500
R = isqrt(N)

# Independent method A: add one signed primitive native axis per stage.
# C[k,n,t]: endpoint count; W[k,n,t]: summed shortest ordered path words.
states = {(0, 0): (1, 1)}
intermediate = []
for k in range(1, 7):
    nxt = {}
    for (sq, length), (count, words) in states.items():
        for magnitude in range(isqrt(N - sq) + 1):
            new_sq, new_len = sq + magnitude*magnitude, length + magnitude
            signs = 1 if magnitude == 0 else 2
            key = (new_sq, new_len)
            old_count, old_words = nxt.get(key, (0, 0))
            nxt[key] = (
                old_count + signs*count,
                old_words + signs*words*comb(new_len, magnitude),
            )
    states = nxt
    intermediate.append(sum(c for (q, t), (c, w) in states.items() if q == N))

native_shell = {t: (c, w) for (q, t), (c, w) in states.items() if q == N}
endpoint_count = sum(c for c, w in native_shell.values())
path_mass = sum(w for c, w in native_shell.values())
assert intermediate[:3] == [2, 20, 150]
assert intermediate[3:] == [18744, 1360890, 102539052]
assert endpoint_count == 102539052
assert path_mass == 46263931428930653590904265855801056735441499817749479001025131238806458196360489958119492948372
assert len(native_shell) == 32
assert min(native_shell) == 50 and max(native_shell) == 122

# Independent method B: enumerate all unordered magnitudes of signed Z^3
# and recombine two exact triple blocks; each signed endpoint is counted
# by a factor 2 for each nonzero coordinate. Retain path length and words.
fac = [factorial(t) for t in range(151)]
triples = defaultdict(lambda: [0, 0])
for a in range(R + 1):
    for b in range(R + 1):
        prefix = a*a + b*b
        if prefix > N:
            continue
        for c in range(isqrt(N - prefix) + 1):
            square, length = prefix + c*c, a+b+c
            signs = (2 if a else 1)*(2 if b else 1)*(2 if c else 1)
            triple_words = fac[length] // (fac[a]*fac[b]*fac[c])
            sums = triples[(square, length)]
            sums[0] += signs
            sums[1] += signs * triple_words

by_square = defaultdict(list)
for (square, length), (cnt, mass) in triples.items():
    by_square[square].append((length, cnt, mass))

other_count, other_mass = 0, 0
for square, left in by_square.items():
    right = by_square.get(N-square, ())
    for t, a, m in left:
        for u, b, n in right:
            other_count += a*b
            other_mass += m*n*comb(t+u, t)
assert (other_count, other_mass) == (endpoint_count, path_mass)

# Separate prior selected signed-three-axis slice, not observer quotient.
signed_slice_count = intermediate[2]
assert signed_slice_count == 150
assert endpoint_count - signed_slice_count == 102538902
assert sum(z*z for z in (18, 24, 40, 0, 0, 0)) == N  # explicit six-axis lift\nassert (18, 24, 40, 0, 0, 0) != (18, 24, 40, 1, 0, 0)
print("PASS_X6_R063_FULL_SIGNED_SIX_AXIS_N2500_NATIVE_NBRC")
print("signed_native_six_axis_endpoints", endpoint_count)
print("signed_native_six_axis_shortest_NBRC_mass", path_mass)
print("signed_native_three_axis_slice_endpoints", signed_slice_count)
print("endpoints_outside_chosen_three_axis_slice", endpoint_count - signed_slice_count)
print("shortest_path_length_range", min(native_shell), max(native_shell))
print("length_strata", len(native_shell))
print("independent_3plus3_enumeration", "MATCH")
