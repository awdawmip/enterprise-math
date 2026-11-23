"""R284FL finite cross-check of the analytic all-q capacity-graph lemma.
Exact integer arithmetic. The all-q theorem is established by the written proof,
not by the finite enumeration q=0..5.
"""
from itertools import combinations_with_replacement
EDGES_02 = ((2, 2, 5), (3, 2, 4), (6, 3, 5), (7, 3, 4))
EDGES_13 = ((1, 0, 5), (3, 0, 6), (4, 3, 6), (6, 3, 5))
def separable(x, q, edges):
    # An induced-vertex witness can be reduced to an edge-type subset.
    for subset in range(1, 1 << len(edges)):
        vertices = set()
        mass = 0
        for k, (p, a, b) in enumerate(edges):
            if (subset >> k) & 1:
                mass += x[p]
                vertices.update((a, b))
        if mass > q * len(vertices):
            return True
    return False
def verify():
    expected = {0: 0, 1: 266, 2: 3535, 3: 20664, 4: 79926, 5: 239954}
    for q, count in expected.items():
        n = 4*q + 1
        capped = both = 0
        for pats in combinations_with_replacement(range(1, 8), n):
            x = [0]*8
            for p in pats:
                x[p] += 1
            if max(x) > 2*q:
                continue
            capped += 1
            if separable(x, q, EDGES_02) and separable(x, q, EDGES_13):
                both += 1
        assert (capped, both) == (count, 0), (q, capped, both)
        print(f"q={q}: n={n}, capped_vectors={capped}, both_opposites_separable={both}")
    print("PASS: finite cross-check of R284FL lemma, q=0..5")
if __name__ == "__main__":
    verify()
