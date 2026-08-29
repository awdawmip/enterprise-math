#!/usr/bin/env python3
"""Exact finite checker for P000 cross-block product prior-art audit V6.

No external packages or network calls.
"""

from itertools import permutations, product
from collections import deque
from math import factorial

ID6 = tuple(range(6))
A = frozenset((0, 1, 2))
B = frozenset((3, 4, 5))
TARGET_B = (0, 3, 4, 1, 2, 5)  # (E2 E4)(E3 E5), E1,E6 fixed

def compose(p, q):
    """p after q."""
    return tuple(p[q[i]] for i in range(len(p)))

# 1. Exact 3+3 block-system stabilizer W = S3 wr S2.
S3 = tuple(permutations(range(3)))
W = set()
for pa in S3:
    for pb in S3:
        keep = [None] * 6
        for i in range(3):
            keep[i] = pa[i]
            keep[3+i] = 3 + pb[i]
        W.add(tuple(keep))

        swap = [None] * 6
        for i in range(3):
            swap[i] = 3 + pa[i]
            swap[3+i] = pb[i]
        W.add(tuple(swap))

assert len(W) == 72

def image_set(p, s):
    return frozenset(p[i] for i in s)

for w in W:
    assert image_set(w, A) in (A, B)
    assert image_set(w, B) in (A, B)

assert image_set(TARGET_B, A) == frozenset((0, 3, 4))
assert TARGET_B not in W
assert compose(TARGET_B, TARGET_B) == ID6

# Axis-type block-pure relation diagnostic: union of the two K3 relation blocks.
BLOCK_REL = {
    frozenset((i,j))
    for block in (A,B)
    for i in block
    for j in block
    if i < j
}
assert len(BLOCK_REL) == 6
mapped_rel = {frozenset((TARGET_B[i], TARGET_B[j])) for i,j in (tuple(e) for e in BLOCK_REL)}
assert mapped_rel != BLOCK_REL
assert frozenset((0,3)) in mapped_rel and frozenset((0,3)) not in BLOCK_REL

# 2. Naive global extension collapse: <W, TARGET_B> = S6.
# A compact generating set for W plus TARGET_B.
GENS = (
    (1,0,2,3,4,5),  # (0 1)
    (1,2,0,3,4,5),  # (0 1 2)
    (0,1,2,4,3,5),  # (3 4)
    (0,1,2,4,5,3),  # (3 4 5)
    (3,4,5,0,1,2),  # whole block swap
    TARGET_B,
)
G = {ID6}
queue = deque((ID6,))
while queue:
    g = queue.popleft()
    for h in GENS:
        x = compose(h, g)
        if x not in G:
            G.add(x)
            queue.append(x)

assert len(G) == factorial(6) == 720
assert G == set(permutations(range(6)))

# 3. Hamming graph H(2,3)=K3 square K3 has exactly 72 automorphisms.
VERTS = tuple(product(range(3), repeat=2))
EDGES = {
    (i,j)
    for i,u in enumerate(VERTS)
    for j,v in enumerate(VERTS)
    if i < j and sum(a != b for a,b in zip(u,v)) == 1
}
assert len(VERTS) == 9
assert len(EDGES) == 18

def is_hamming_aut(p):
    for i,j in EDGES:
        if tuple(sorted((p[i], p[j]))) not in EDGES:
            return False
    return True

aut_count = sum(1 for p in permutations(range(9)) if is_hamming_aut(p))
assert aut_count == 72

# 4. A "partial action" still requires an explicit domain and arrow.
# This is a typing regression, not an external theorem checker.
DOMAIN_JA = frozenset((0,1,2))
TARGET_JB = frozenset((0,3,4))
assert image_set(TARGET_B, DOMAIN_JA) == TARGET_JB
assert DOMAIN_JA != TARGET_JB
assert TARGET_JB not in (A, B)

print("PASS")
print("W_order=72=S3_wr_S2")
print("target_b_in_W=False")
print("target_b_squared=identity")
print("block_pure_axis_relation_preserved_by_b=False")
print("global_extension_<W,b>_order=720=S6")
print("H(2,3)_vertices=9; edges=18; automorphisms=72")
print("minimal_extension_guard=GLOBAL_b_ON_TOP_OF_W_COLLAPSES_TO_S6")
