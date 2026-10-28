"""Bounded discovery check only; independent of project methods/catalogs.
All tuples are RAW SIGNED DISPLACEMENTS, never final public Cell addresses.
"""
from itertools import product
from math import comb
import json

D = 6
ZERO = (0,) * D
STEPS = tuple(tuple(sign if j == axis else 0 for j in range(D))
              for axis in range(D) for sign in (-1, 1))
def add(x, y): return tuple(a + b for a, b in zip(x, y))
def norm(x): return sum(abs(a) for a in x)
def C(r):
    return 0 if r < 0 else sum(comb(5, j) * comb(r-j+6, 6)
                              for j in range(min(5, r)+1))
def reachable(t):
    out = {ZERO}
    for _ in range(t):
        out = {add(x, s) for x in out for s in STEPS}
    return out
# Equality of every return output under every suffix of length <= h is
# equivalent to equality of terminal output for every such suffix.
def suffix_displacements(h):
    out = [ZERO]
    for length in range(1, h+1):
        for word in product(STEPS, repeat=length):
            x = ZERO
            for s in word: x = add(x, s)
            out.append(x)
    return tuple(out)

rows = []
for H in range(5):
    counts = []
    for t in range(H+1):
        h = H-t
        population = reachable(t)
        suffixes = suffix_displacements(h)
        # Retain every word, including repeats and cancellation words.
        signatures = {tuple(add(x, w) == ZERO for w in suffixes)
                      for x in population}
        radius = min(t, h)
        radius -= (radius-t) % 2
        expected = C(radius) + int(t > h)
        assert len(signatures) == expected, (H, t, len(signatures), expected)
        # Check the quotient's transition is well-defined on its dead class.
        if t < H:
            for x in population:
                if norm(x) > h:
                    assert all(norm(add(x, s)) > h-1 for s in STEPS)
        counts.append(expected)
        rows.append({'H':H, 't':t, 'reachable_count':len(population),
                     'suffix_word_count':len(suffixes),
                     'distinct_observation_signatures':len(signatures),
                     'predicted_classes':expected})
    assert max(counts) == C(H//2)
# Separate exact count check, using reachable endpoint sets rather than formula.
count_checks = []
for r in range(7):
    actual = len(reachable(r))
    assert actual == C(r), (r, actual, C(r))
    count_checks.append({'r':r,'enumerated':actual,'formula':C(r)})
print(json.dumps({'dimension':D, 'horizons_checked':list(range(5)),
 'checks':rows,'parity_ball_counts':count_checks,
 'status':'PASS_BOUNDED_DISCOVERY_CHECK_NOT_GENERAL_PROOF'},indent=2))
