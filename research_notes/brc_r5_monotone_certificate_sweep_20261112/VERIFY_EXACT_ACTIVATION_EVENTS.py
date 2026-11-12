#!/usr/bin/env python3
"""Independent exact finite 15-weight activation-parameter census, no imports."""
from collections import defaultdict, Counter
from math import gcd

W = (336,184,18,169,64,84,299,126,52,16,-420,-483,-144,-221,-80)
K = (-432,0,0,0,0,-108,0,0,0,0,540,0,0,0,0)
M = 1 << 15
a = [0] * M
b = [0] * M
for mask in range(1, M):
    bit = mask & -mask
    j = bit.bit_length() - 1
    a[mask] = a[mask ^ bit] + W[j]
    b[mask] = b[mask ^ bit] + K[j]

N = {-v for v in a if v <= -3}
candidates = defaultdict(list)
for mask in range(1, M):
    n, v = -a[mask], -b[mask]
    if n in N and v in (36*3, 36*12, 36*15):
        candidates[v // 36, n].append(mask)

groups = defaultdict(list)
for q, n in candidates:
    g = gcd(q, n)
    # Equality of exact rational thresholds iff q/n is equal.
    groups[q // g, n // g].append((q, n))

h = Counter(map(len, groups.values()))
double_families = Counter()
triples = []
for group in groups.values():
    if len(group) == 2:
        double_families[tuple(sorted(q for q, n in group))] += 1
    if len(group) == 3:
        triples.append(dict(group)[3])

assert (len(N), len(candidates),
        sum(map(len, candidates.values()))) == (1144, 1065, 2935)
assert len(groups) == 953
assert h == {1: 869, 2: 56, 3: 28}
assert double_families == {(3, 12):39, (3, 15):14, (12, 15):3}
assert sorted(triples) == [
     3, 5, 6, 7, 9, 10, 13, 15, 17, 18, 19, 22, 23, 26,
     29, 30, 36, 39, 42, 46, 50, 52, 60, 66, 72, 82, 88, 98
]

print("FINITE_MASK_ENUMERATION", M, "FIXED_N", len(N))
print("PAIRS", len(candidates), "MASKS", sum(map(len, candidates.values())))
print("DISTINCT_CERTIFICATE_ACTIVATION_PARAMETERS", len(groups))
print("ACTIVATION_MULTIPLICITIES", dict(sorted(h.items())))
print("DOUBLE_Q_FAMILIES", dict(sorted(double_families.items())))
print("TRIPLE_Q3_N", sorted(triples))
print("PASS_R5_EXACT_CERTIFICATE_ACTIVATION_EVENT_CENSUS")
