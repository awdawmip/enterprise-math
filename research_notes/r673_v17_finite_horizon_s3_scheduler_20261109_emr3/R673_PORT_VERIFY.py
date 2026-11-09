"""Exact minimal orbit-closed four-port license sets for the V29 witness."""
from itertools import permutations, product
import json

P = range(4)
S4 = list(permutations(P))
W = {(0, 0), (2, 2), (3, 3)}
D = {(a, a) for a in P}
FULL = set(product(P, P))

def diagonal_action(H, pi):
    return {(pi[a], pi[b]) for a, b in H}

def independent_action(H, pi, rho):
    return {(pi[a], rho[b]) for a, b in H}

synchronous_closure = set().union(*(diagonal_action(W, pi) for pi in S4))
independent_closure = set().union(*(independent_action(W, pi, rho) for pi in S4 for rho in S4))
assert len(S4) == 24
assert synchronous_closure == D and len(D) == 4
assert independent_closure == FULL and len(FULL) == 16
assert all(diagonal_action(D, pi) == D for pi in S4)
assert all(independent_action(FULL, pi, rho) == FULL for pi in S4 for rho in S4)

out = {
    "schema": "R673_V29_PORT_ORBIT_CLOSURE_V1",
    "native_context": "two adjacent X6 Cells, 4 typed ports per Cell; V29 port permissions parameterized",
    "witness_port_pairs": sorted(map(list, W)),
    "simultaneous_S4_action_count": 24,
    "independent_S4xS4_action_count": 576,
    "minimal_simultaneous_S4_invariant_H": sorted(map(list, D)),
    "minimal_independent_S4xS4_invariant_H_count": 16,
    "minimal_independent_S4xS4_invariant_H": sorted(map(list, FULL)),
    "checked_permission_relation_covariance_only": True,
    "claimed_native_full_rotation_covariance": False,
    "pass": True,
}
print(json.dumps(out, ensure_ascii=False, sort_keys=True, indent=2))
