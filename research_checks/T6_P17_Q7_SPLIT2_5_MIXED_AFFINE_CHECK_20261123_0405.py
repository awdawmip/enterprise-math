#!/usr/bin/env python3
"""T6 p17 valuation-one q7 split(2,5) exact global mixed-congruence search.
This compact reproducer uses the published, pinned q5 saturated q0 lattice
and exact Fraction Gram-Schmidt solver without modifying their semantics.
Original standalone author computation ran in ten disjoint ranges.
This compact wrapper has not itself been separately executed.
"""
import importlib.util
from pathlib import Path
src=Path(__file__).with_name("T6_P17_Q5_EXACT_MODULAR_LATTICE_CHECK_20261123.py")
spec=importlib.util.spec_from_file_location("t6_p17_q5_exact",src)
old=importlib.util.module_from_spec(spec)
spec.loader.exec_module(old)
left=old.STATES[2]; right=old.STATES[5]
assert len(left)==152 and len(right)==30040
Rmax=(2331-min(x[1] for x in left))**2+(2331-min(x[1] for x in right))**2
assert Rmax==3774069 < old.Dmin
counts=dict(raw_pairs=0,shared_vertical_pairs=0,primitive_pairs=0,
            gs_nodes=0,sphere_leaves=0,budget_valid_kernels=0)
for pos in left:
    v=set(pos[0])
    for neg in right:
        counts["raw_pairs"]+=1
        if v.intersection(neg[0]):
            counts["shared_vertical_pairs"]+=1
            continue
        counts["primitive_pairs"]+=1
        nodes,leaves,u=old.ball_search(pos,neg)
        counts["gs_nodes"]+=nodes
        counts["sphere_leaves"]+=leaves
        counts["budget_valid_kernels"]+=int(u is not None)
assert counts=={
    "raw_pairs":4566080,"shared_vertical_pairs":1359386,
    "primitive_pairs":3206694,"gs_nodes":7848081,
    "sphere_leaves":0,"budget_valid_kernels":0},counts
print("AUTHOR_EXACT_REPRODUCER",counts)
print("Scope: maximal p17 v17=1 q7 (2,5), global T6 remains OPEN")
