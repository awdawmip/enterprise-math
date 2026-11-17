#!/usr/bin/env python3
"""R762CU finite exact signed X6 triad parity and S6 Port symmetry verifier."""
import itertools
import json
from collections import Counter

AXES = range(1, 7)
STATES = [
    tuple(x * sign for x, sign in zip(tr, signs))
    for tr in itertools.combinations(AXES, 3)
    for signs in itertools.product((-1, 1), repeat=3)
]
S = set(STATES)
PERMS = list(itertools.permutations(AXES))

def act(state, perm):
    return tuple(sorted(
        (perm[abs(x)-1] * (1 if x > 0 else -1) for x in state),
        key=abs,
    ))

def negative_count(state):
    return sum(x < 0 for x in state)

assert len(STATES) == len(S) == 160
sizes = Counter(map(negative_count, STATES))
assert [sizes[i] for i in range(4)] == [20, 60, 60, 20]

for k in range(4):
    representative = next(x for x in STATES if negative_count(x) == k)
    assert {act(representative, p) for p in PERMS} == {
        x for x in STATES if negative_count(x) == k
    }

covariance_checks = 0
for p in PERMS:
    for state in STATES:
        transformed = act(state, p)
        assert transformed in S
        assert negative_count(transformed) == negative_count(state)
        covariance_checks += 1

parity_checks = 0
for state in STATES:
    displacement = [0] * 6
    for x in state:
        displacement[abs(x)-1] += 1 if x > 0 else -1
    assert sum(x*x for x in displacement) == 3
    for order in itertools.permutations(state):
        position = [0] * 6
        for x in order:
            position[abs(x)-1] += 1 if x > 0 else -1
        assert position == displacement
        assert sum(position) % 2 == 1
        parity_checks += 1

base = (1, 2, 3)
stabilizer = [p for p in PERMS if act(base, p) == base]
assert len(stabilizer) == 36
for port in base:
    assert {p[port-1] for p in stabilizer} == set(base)

marked = [(state, port) for state in STATES for port in state]
assert len(marked) == 480
marked_equivariance_checks = 0
for permutation in PERMS:
    for state, port in marked:
        transformed = act(state, permutation)
        marked_port = permutation[abs(port)-1] * (1 if port > 0 else -1)
        assert marked_port in transformed
        marked_equivariance_checks += 1

# The optimal selector chooses the unique minority-sign Port when one exists.
# Homogeneous-sign triples retain all three equivariant Port branches.
def minimal_options(state):
    k = negative_count(state)
    if k == 1:
        return [x for x in state if x < 0]
    if k == 2:
        return [x for x in state if x > 0]
    return list(state)

minimal_cover = [(s, port) for s in STATES for port in minimal_options(s)]
assert len(minimal_cover) == 240
assert [sum(len(minimal_options(s)) for s in STATES if negative_count(s) == k)
        for k in range(4)] == [60, 60, 60, 60]
minimal_cover_equivariance_checks = 0
for permutation in PERMS:
    for state in STATES:
        transported = {permutation[abs(x)-1] * (1 if x > 0 else -1)
                       for x in minimal_options(state)}
        assert transported == set(minimal_options(act(state, permutation)))
        minimal_cover_equivariance_checks += 1

for mask in range(16):
    accepted = {state for state in STATES if mask & (1 << negative_count(state))}
    for permutation in PERMS:
        for state in STATES:
            assert (act(state, permutation) in accepted) == (state in accepted)

evidence = {
    "schema": "R762CU_EXACT_EVIDENCE_V1",
    "fixed_scope": "distinct-support equal-quantum signed triad candidates at one X6 Cell",
    "states": len(STATES),
    "group_order": len(PERMS),
    "orbit_sizes": [sizes[i] for i in range(4)],
    "orbit_checks": 4,
    "sign_preserving_covariance_checks": covariance_checks,
    "three_step_nonreturn_checks": parity_checks,
    "stabilizer_size_for_+++": len(stabilizer),
    "marked_cover_states": len(marked),
    "optimal_marked_cover_states": len(minimal_cover),
    "minimal_fibers_by_sign_count": [3, 1, 1, 3],
    "minimal_cover_equivariance_checks": minimal_cover_equivariance_checks,
    "marked_equivariance_checks": marked_equivariance_checks,
    "invariant_boolean_candidate_laws": 16,
    "nonempty_boolean_candidate_laws": 15,
    "mark_fiber_size": 3,
    "mark_bits_fixed_length": 2,
    "status": "AUTHOR_EXACT_CHECKED_NOT_INDEPENDENT_REVIEW",
    "boundary": "Candidate incidence/Port selection; native TRIADIC_CLOSURE_E and V17/V29/V39 licensing remain open."
}
print(json.dumps(evidence, ensure_ascii=False, indent=2))
