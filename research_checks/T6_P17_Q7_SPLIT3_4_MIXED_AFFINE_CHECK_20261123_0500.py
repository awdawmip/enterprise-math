#!/usr/bin/env python3
"""T6 p17 valuation-one vertical-order7 split(3,4): exact global mixed test.

Imports published q5 saturated q0 affine solver with unchanged 16D basis,
original mass budgets and exact Fraction Gram-Schmidt. The full original
author run executed in 34 disjoint [i,i+32) chunks over order3 states;
this compact wrapper has not been separately executed after publication.
"""
import importlib.util
from pathlib import Path
src=Path(__file__).with_name("T6_P17_Q5_EXACT_MODULAR_LATTICE_CHECK_20261123.py")
spec=importlib.util.spec_from_file_location("t6_p17_q5_exact",src)
old=importlib.util.module_from_spec(spec)
spec.loader.exec_module(old)
left=old.STATES[3]
right=old.STATES[4]
assert len(left)==1088 and len(right)==6460
max_R2=(2331-min(x[1] for x in left))**2+(2331-min(x[1] for x in right))**2
assert max_R2==3439985 < old.Dmin
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
        counts["budget_valid_kernels"]+=int(u is not None)
assert counts=={"raw_pairs":7028480,"shared_vertical_pairs":2398208,
               "primitive_pairs":4630272,"gs_nodes":9623589,
               "sphere_leaves":0,"budget_valid_kernels":0},counts
print("AUTHOR_EXACT_REPRODUCER",counts)
print("Scope p17 v17=1 primitive order7 split(3,4); T6 mother OPEN")
