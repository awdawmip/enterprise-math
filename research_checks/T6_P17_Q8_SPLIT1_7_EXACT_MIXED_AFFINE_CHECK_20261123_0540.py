#!/usr/bin/env python3
"""T6 maximal-p17 valuation-one q8 split(1,7) exact global mixed check.
Author standalone exact calculation executed; this compact publication was
not independently run. Reuse the pinned q5 saturated affine q0 solver.
"""
import importlib.util
from pathlib import Path
src=Path(__file__).with_name("T6_P17_Q5_EXACT_MODULAR_LATTICE_CHECK_20261123.py")
sp=importlib.util.spec_from_file_location("t6_p17_q5_exact",src)
old=importlib.util.module_from_spec(sp)
sp.loader.exec_module(old)
for q in (6,7):
    for r in range(1,17):
        u=old.particular_atom(q,r)
        coord=tuple(sum(u[j]*old.N[j][i] for j in range(16)) for i in range(16))
        old.ATOMS[q,r]=(coord,17*(17*q+r)-1)
left=old.STATES[1]
right=list(old.vertical_states(7))
assert len(left)==16 and len(right)==8697
R2=(2331-min(x[1] for x in left))**2+(2331-min(x[1] for x in right))**2
assert R2==4189940 < old.Dmin
stats=dict(raw_pairs=0,shared_vertical_pairs=0,primitive_pairs=0,
           gs_nodes=0,sphere_leaves=0,budget_valid_kernels=0)
for pos in left:
    support=set(pos[0])
    for neg in right:
        stats["raw_pairs"]+=1
        if support.intersection(neg[0]):
            stats["shared_vertical_pairs"]+=1
            continue
        stats["primitive_pairs"]+=1
        nodes,leaves,candidate=old.ball_search(pos,neg)
        stats["gs_nodes"]+=nodes
        stats["sphere_leaves"]+=leaves
        stats["budget_valid_kernels"]+=int(candidate is not None)
assert stats==dict(raw_pairs=139152,shared_vertical_pairs=15360,
                   primitive_pairs=123792,gs_nodes=398646,
                   sphere_leaves=0,budget_valid_kernels=0),stats
print(stats)
