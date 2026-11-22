#!/usr/bin/env python3
"""T6 maximal p17 valuation-one order8 split(0,8) exact necessary filter.
The standalone exact author execution completed, this small published
reproducer is not separately executed after GitHub publication.
"""
import importlib.util
from pathlib import Path
source=Path(__file__).with_name("T6_P17_Q5_EXACT_MODULAR_LATTICE_CHECK_20261123.py")
spec=importlib.util.spec_from_file_location("t6_p17_q5_exact",source)
old=importlib.util.module_from_spec(spec)
spec.loader.exec_module(old)
for q in (6,7,8):
    for r in range(1,17):
        u=old.particular_atom(q,r)
        coords=tuple(sum(u[j]*old.N[j][i] for j in range(16)) for i in range(16))
        old.ATOMS[q,r]=(coords,17*(17*q+r)-1)
neg=list(old.vertical_states(8))
assert len(neg)==1 and neg[0][0]==((8,1),)
pos=old.STATES[0][0]
max_r2=2331**2+(2331-neg[0][1])**2
assert neg[0][1]==2328 and max_r2==5433570<old.Dmin
nodes,leaves,sol=old.ball_search(pos,neg[0])
assert (nodes,leaves,sol)==(4,0,None)
print({"raw_pairs":1,"primitive_pairs":1,"nodes":nodes,"sphere_leaves":leaves,
       "valid":0,"max_R2":max_r2,"status":"AUTHOR_EXACT_FINITE_UNREVIEWED_NOT_ADMITTED"})
