"""Exact finite diagnostic for joint legality vs local/pairwise feasibility.
This is a three-bit external CSP, NOT a native six-axis event model.
"""
from itertools import combinations, product

assignments = list(product((0, 1), repeat=3))
constraints = {
    "ab_equal": lambda t: t[0] == t[1],
    "bc_equal": lambda t: t[1] == t[2],
    "ca_unequal": lambda t: t[2] != t[0],
}
counts = {}
for width in range(1, 4):
    for names in combinations(constraints, width):
        allowed = [t for t in assignments if all(constraints[n](t) for n in names)]
        counts[names] = len(allowed)
        assert len(allowed) == (4 if width == 1 else 2 if width == 2 else 0)
assert all({t[i] for t in assignments if predicate(t)} == {0, 1}
           for predicate in constraints.values() for i in range(3))
print('EXACT_3BIT_CSP: 8 states; singles=4 each; pairs=2 each; triple=0; per-site projections=full')
