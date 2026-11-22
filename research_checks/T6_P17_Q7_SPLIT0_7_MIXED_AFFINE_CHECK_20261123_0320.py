#!/usr/bin/env python3
"""T6 maximal-p17 order7 split(0,7): exact global mixed-congruence check.

Extends the published q5 saturated 16D affine-lattice solver without
changing its original kernel, Gram-Schmidt, mass, or modular semantics.
Original standalone exact computation already executed; this compact
repository reproducer is published separately and not yet reexecuted.
"""
import importlib.util
from pathlib import Path
src = Path(__file__).with_name("T6_P17_Q5_EXACT_MODULAR_LATTICE_CHECK_20261123.py")
spec = importlib.util.spec_from_file_location("t6_p17_q5_exact", src)
old = importlib.util.module_from_spec(spec)
spec.loader.exec_module(old)

# Additional vertical atom orders, same q0 affine particular algorithm.
for q in (6, 7):
    for r in range(1, 17):
        u = old.particular_atom(q, r)
        coord = tuple(sum(u[j] * old.N[j][i] for j in range(16)) for i in range(16))
        old.ATOMS[q, r] = (coord, 17 * (17 * q + r) - 1)

left = old.STATES[0][0]
right = list(old.vertical_states(7))
assert len(right) == 8697
max_R2 = 2331**2 + (2331 - min(v[1] for v in right))**2
assert max_R2 == 5518825 < old.Dmin

counts = {"raw_pairs": 0, "primitive_pairs": 0, "gs_nodes": 0,
          "sphere_leaves": 0, "budget_valid_kernels": 0}
for neg in right:
    counts["raw_pairs"] += 1
    counts["primitive_pairs"] += 1  # left side has no vertical atoms
    nodes, leaves, candidate = old.ball_search(left, neg)
    counts["gs_nodes"] += nodes
    counts["sphere_leaves"] += leaves
    if candidate is not None:
        counts["budget_valid_kernels"] += 1

assert counts == {"raw_pairs": 8697, "primitive_pairs": 8697,
                  "gs_nodes": 40799, "sphere_leaves": 0,
                  "budget_valid_kernels": 0}, counts
print("AUTHOR_REPRODUCER_COUNTS", counts)
print("SCOPE: p17 v17=1 primitive order7 split(0,7); not global T6")
