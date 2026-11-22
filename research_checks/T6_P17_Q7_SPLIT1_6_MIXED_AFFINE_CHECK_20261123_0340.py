#!/usr/bin/env python3
"""T6 maximal-p17 order7 split(1,6): exact global mixed-congruence check.
Reuses the pinned saturated q0 affine solver from the published q5 source.
The standalone exact author experiment executed in two disjoint chunks.
This compact reproducer has not itself been separately run.
"""
import importlib.util
from pathlib import Path
src=Path(__file__).with_name("T6_P17_Q5_EXACT_MODULAR_LATTICE_CHECK_20261123.py")
spec=importlib.util.spec_from_file_location("t6_p17_q5_exact",src)
old=importlib.util.module_from_spec(spec)
spec.loader.exec_module(old)
for r in range(1,17):
    u=old.particular_atom(6,r)
    coord=tuple(sum(u[j]*old.N[j][i] for j in range(16)) for i in range(16))
    old.ATOMS[6,r]=(coord,17*(17*6+r)-1)
left=old.STATES[1]
right=list(old.vertical_states(6))
assert len(left)==16 and len(right)==47628
max_R2=(2331-min(s[1] for s in left))**2+(2331-min(s[1] for s in right))**2
assert max_R2==4442237 < old.Dmin
counts={"raw_pairs":0,"shared_vertical_pairs":0,"primitive_pairs":0,
        "gs_nodes":0,"sphere_leaves":0,"budget_valid_kernels":0}
for pos in left:
    support=set(pos[0])
    for neg in right:
        counts["raw_pairs"]+=1
        if support.intersection(neg[0]):
            counts["shared_vertical_pairs"]+=1
            continue
        counts["primitive_pairs"]+=1
        nodes,leaves,u=old.ball_search(pos,neg)
        counts["gs_nodes"]+=nodes
        counts["sphere_leaves"]+=leaves
        if u is not None:
            counts["budget_valid_kernels"]+=1
assert counts=={"raw_pairs":762048,"shared_vertical_pairs":128023,
               "primitive_pairs":634025,"gs_nodes":2052835,
               "sphere_leaves":0,"budget_valid_kernels":0},counts
print("AUTHOR_EXACT_REPRODUCER", counts)
print("UNREVIEWED_NOT_ADMITTED; global T6 OPEN")
