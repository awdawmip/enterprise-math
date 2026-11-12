#!/usr/bin/env python3
"""Exact S6-equivariant S7-frame holonomy in X6 candidate signed-unit paths."""
from collections import deque
from itertools import combinations, permutations
import json

N = 7  # frame labels: 0=auxiliary mark, 1..6=native spatial axis labels
IDENTITY = tuple(range(N))
PAIRS = tuple(combinations(range(1, 7), 2))

def mul(f, g):
    return tuple(f[g[k]] for k in range(N))

def axis_label(i):
    x = list(IDENTITY)
    x[0], x[i] = x[i], x[0]
    return tuple(x)

T = {i: axis_label(i) for i in range(1, 7)}

def frame(word):
    g = IDENTITY
    for a, sign in word:
        assert a in T and sign in (-1, 1)
        g = mul(T[a], g)  # later steps multiply on the left
    return g

def area(word):
    x = [0]*N
    A = {(a, b): 0 for a, b in PAIRS}
    for a, sign in word:
        for b in range(1, a):
            A[b, a] += x[b]*sign
        x[a] += sign
    assert x == [0]*N
    return tuple(A.values())

def witness(i, j):
    return ((i, 1), (j, 1), (i, -1), (j, -1),
            (i, 1), (j, -1), (i, -1), (j, 1))

def sign(g):
    return (-1)**sum(g[i] > g[j] for i in range(N) for j in range(i+1, N))

G = []
for i, j in PAIRS:
    w = witness(i, j)
    assert area(w) == (0,)*15
    g = frame(w)
    assert g == mul(T[j], T[i])
    assert g != IDENTITY and sign(g) == 1
    G.append(g)

# Exact finite closure: all based flat-loop generators and their products.
seen = {IDENTITY}
queue = deque([IDENTITY])
while queue:
    g = queue.popleft()
    for t in G:
        h = mul(g, t)
        if h not in seen:
            seen.add(h)
            queue.append(h)
assert len(seen) == 2520
assert all(sign(g) == 1 for g in seen)

# Full S6-covariance for all 720 axis permutations and all six axes.
covariance_checks = 0
for p in permutations(range(1, 7)):
    sigma = (0,) + p
    inverse = tuple(sigma.index(k) for k in range(N))
    for i in range(1, 7):
        assert mul(mul(sigma, T[i]), inverse) == T[sigma[i]]
        covariance_checks += 1
assert covariance_checks == 4320

v = witness(1, 2)
assert frame(v) == (1, 2, 0, 3, 4, 5, 6)
print(json.dumps({
    'schema': 'R758P5B_S6_EQUIVARIANT_S7_EXACT_V1',
    'frozen_source': 'a72226e2430ffa4786321ac86e7f0c599d5f0389',
    'frame_labels': ['star', '1', '2', '3', '4', '5', '6'],
    'native_spatial_axes': 6,
    'zero_area_8_step_witnesses': len(G),
    'generated_flat_area_holonomy_group': 'A7',
    'generated_flat_area_holonomy_order': len(seen),
    'all_generated_even_permutations': True,
    'axis_relabeling_covariance_checks': covariance_checks,
    'minimal_fixed_binary_bits_to_recover_full_flat_frame': 12,
    'native_triadic_event': 'NOT_ESTABLISHED',
    'status': 'PASS'
}, indent=2))
