#!/usr/bin/env python3
from itertools import product

# Abstract exact cycle check: six labeled shell triad phases Theta_r and six
# closure relation states Kappa_r all share one spatial Cell but retain distinct
# port-matching labels.

shell = tuple(('Theta', r) for r in range(6))
closure = tuple(('Kappa', r) for r in range(6))
cycle=[]
for r in range(6):
    cycle.extend((shell[r], closure[r]))
cycle=tuple(cycle)
assert len(cycle)==12 and len(set(cycle))==12

succ={cycle[i]:cycle[(i+1)%12] for i in range(12)}
for x in cycle:
    y=x
    for _ in range(12): y=succ[y]
    assert y==x

# All Kappa states have same spatial projection but distinct relation labels.
def spatial_projection(state):
    kind,r=state
    return ('pivot_cell',0) if kind=='Kappa' else ('shell_relation',r)
assert len({spatial_projection(k) for k in closure})==1
assert len(set(closure))==6

# Event phase hierarchy.
for n in range(120):
    state=cycle[n%12]
    assert (state[0]=='Theta') == (n%2==0)
    if n%2==0:
        assert state==shell[(n//2)%6]
    else:
        assert state==closure[((n-1)//2)%6]

# Forget ordered token matching on a sign-coherent shell gives two sign sheets;
# model their exact C6 -> C2 quotient and C3 repair fiber.
sheet={r:r%2 for r in range(6)}
assert len(set(sheet.values()))==2
fibers={s:[r for r in range(6) if sheet[r]==s] for s in (0,1)}
assert all(len(v)==3 for v in fibers.values())

print('PASS_X6_TRIADIC_INNER_C12_V2')
print('decorated_cycle_order',12)
print('closure_states_at_same_spatial_cell',6)
print('shell_phase_order',6)
print('static_sheet_order',2)
print('matching_repair_fiber_size',3)
print('spatial_cell_determines_interaction_phase',False)
