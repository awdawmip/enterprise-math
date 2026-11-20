#!/usr/bin/env python3
"""X6 signed Cell cube quotient; exact S6 endpoint covariance only (not full X6 admission)."""
from itertools import product, permutations
from math import factorial
C = list(product((-1,0,1), repeat=6))
q3 = lambda x: tuple(t % 3 for t in x)
assert len(C) == 3**6
assert len({q3(x) for x in C}) == 729
perm_count = 0
for sigma in permutations(range(6)):
    inv = [0]*6
    for i,j in enumerate(sigma): inv[j] = i
    for x in C:
        sx = tuple(x[inv[j]] for j in range(6))
        assert q3(sx) == tuple(q3(x)[inv[j]] for j in range(6))
    perm_count += 1
assert perm_count == factorial(6)
port_images = []
for i in range(6):
    for eps in (-1,1):
        v = [0]*6
        v[i] = eps
        port_images.append(q3(v))
assert len(set(port_images)) == 12
q2 = lambda x: tuple(t % 2 for t in x)
assert len({q2(x) for x in C}) == 64
assert factorial(6) == 720
print({"cube":729,"S6_rotations":720,"covariance_pairs":524880,
       "signed_port_images":12,"mod2_signed_cube_images":64,
       "one_endpoint_order_history_fiber":720})
