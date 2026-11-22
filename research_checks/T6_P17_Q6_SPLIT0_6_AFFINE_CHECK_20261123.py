#!/usr/bin/env python3
"""Exact p17 order-six split (0,6), full signed q0 affine-sphere enumeration.

Imports the already published, pinned saturated q0 lattice and exact rational
ball-search implementation. No lower-prime atoms are deleted from the global
T6 question; this is a necessary p17 congruence exclusion.
"""
import importlib.util
import json
from pathlib import Path

BASE = Path(__file__).with_name("T6_P17_Q5_EXACT_MODULAR_LATTICE_CHECK_20261123.py")
spec = importlib.util.spec_from_file_location("t6_p17_q5_pinned_base", BASE)
q5 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(q5)
assert q5.P == 17 and q5.BUDGET == 2331
assert abs(int(q5.Matrix(q5.U).det())) == 17**21
assert len(q5.STATES[5]) == 30040

atoms = {k:v for k,v in q5.ATOMS.items()}
for r in range(1,17):
    u = q5.particular_atom(6,r)
    atoms[6,r] = (
        tuple(sum(u[j]*q5.N[j][i] for j in range(16)) for i in range(16)),
        17*(17*6+r)-1
    )
named = sorted(atoms)
states = []

def extend(start, order, cost, selections, coordinate):
    if order == 6:
        states.append((tuple(selections), cost, tuple(coordinate)))
        return
    for i in range(start,len(named)):
        q,r = named[i]
        u,w = atoms[q,r]
        if order+q > 6:
            break
        if cost+w > 2331:
            continue
        extend(i, order+q, cost+w, selections+[(q,r)],
               [x+y for x,y in zip(coordinate,u)])

extend(0,0,0,[],[0]*16)
assert len(states) == 47628
minimum_vertical_cost = min(s[1] for s in states)
max_radius_squared = 2331**2+(2331-minimum_vertical_cost)**2
assert minimum_vertical_cost == 1750
assert max_radius_squared == 5771122
assert max_radius_squared < q5.Dmin

positive = ((),0,(0,)*16)
nodes = 0
leaves = 0
survivors = []
histogram = {}
for negative in states:
    cnt, nleaves, u = q5.ball_search(positive, negative)
    nodes += cnt
    leaves += nleaves
    histogram[str(cnt)] = histogram.get(str(cnt),0)+1
    if u is not None:
        survivors.append({"vertical":negative[0],"q0_signed":u})
assert nodes == 224133
assert leaves == 0 and survivors == []
result = {
    "schema":"T6_P17_Q6_SPLIT0_6_EXACT_AFFINE_AUTHOR_V1",
    "source_task_commit":"d84bd940cfb093cdc60e569f15cad58772a51dca",
    "q0_lattice_blob_sha1":"d9ac014355a6a1058cc8a0cf2141a01082628881",
    "q5_checker_blob_sha1":"2c1aa73268aa11300a32b9923e3bdbddb6190813",
    "side_mass_cap":2331,
    "mixed_moduli":[17**j for j in range(1,7)],
    "split":[0,6], "vertical_rosters":len(states),
    "minimum_vertical_mass":minimum_vertical_cost,
    "maximum_sphere_radius_squared":max_radius_squared,
    "minimum_gs_squared":[str(q5.Dmin.numerator),str(q5.Dmin.denominator)],
    "visited_nodes":nodes,"sphere_leaves":leaves,
    "budget_valid_kernels":len(survivors),
    "recursion_histogram":histogram,
    "status":"AUTHOR_EXACT_FINITE_EXECUTED_UNREVIEWED_NOT_ADMITTED"
}
path = Path("T6_P17_Q6_SPLIT0_6_AFFINE_CERT_20261123.json")
path.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n",encoding="utf-8")
print(json.dumps({k:v for k,v in result.items() if k!="recursion_histogram"},indent=2))
