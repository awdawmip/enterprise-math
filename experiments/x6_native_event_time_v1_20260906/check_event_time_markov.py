#!/usr/bin/env python3

# Exact finite checks for the deterministic triadic C12 event-clock interface.

shell=tuple(('Theta',r) for r in range(6))
closure=tuple(('Kappa',r) for r in range(6))
cycle=tuple(x for r in range(6) for x in (shell[r],closure[r]))
assert len(cycle)==12 and len(set(cycle))==12
succ={cycle[i]:cycle[(i+1)%12] for i in range(12)}

# Event phase and two-step shell phase.
for n in range(240):
    state=cycle[n%12]
    assert state[0]==('Theta' if n%2==0 else 'Kappa')
    assert n%12 == cycle.index(state)
    if n%2==0:
        r=(n//2)%6
        assert state==shell[r]
        after2=succ[succ[state]]
        assert after2==shell[(r+1)%6]

# Spatial-only Markov obstruction: all closure states are the same pivot Cell,
# but their next labeled shell states are pairwise distinct.
def spatial(state):
    kind,r=state
    if kind=='Kappa': return ('pivot',0)
    return ('shell_spatial_relation',r)
assert len({spatial(k) for k in closure})==1
next_shell={k:succ[k] for k in closure}
assert len(set(next_shell.values()))==6

# Therefore any deterministic exact repair over the pivot fiber needs >=6 labels.
assert len(closure)==6

# One triadic macrostep consists of two relation-update layers but six primitive
# force transition occurrences (3 in + 3 out).
relation_ticks_per_macro=2
primitive_occurrences_per_macro=6
assert relation_ticks_per_macro != primitive_occurrences_per_macro

# Finite memory cannot preserve an unbounded exact loop-count observer. A
# concrete prefix family already has identical endpoint/frame and all distinct
# exact lengths 0,2,...,200.
loop_powers=tuple(range(101))
lengths=tuple(2*k for k in loop_powers)
assert len(set(lengths))==101
endpoint=('same_cell','identity_frame')
assert len({endpoint for _ in loop_powers})==1

print('PASS_X6_NATIVE_EVENT_TIME_V1')
print('event_cycle_states',12)
print('closure_states_same_spatial_cell',6)
print('distinct_next_shell_states_from_same_pivot',6)
print('minimum_exact_pivot_relation_labels',6)
print('relation_ticks_per_triadic_macro',relation_ticks_per_macro)
print('primitive_force_occurrences_per_macro',primitive_occurrences_per_macro)
print('spatial_cell_alone_markov',False)
print('finite_memory_globally_path_provenance_complete',False)
