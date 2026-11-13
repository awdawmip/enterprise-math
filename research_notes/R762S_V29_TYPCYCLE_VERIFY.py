#!/usr/bin/env python3
"""Exact local candidate V29 PASS bridge to R762R ordered signed X6 triads.
No native TRIADIC_CLOSURE_E admission or physical transport is inferred.
Only Python stdlib, integer operations and exhaustive finite permutations.
"""
from collections import defaultdict
from itertools import combinations, product, permutations
from json import dumps

AXES = range(6)
triads = [(tuple((i, s) for i, s in zip(S, signs)))
          for S in combinations(AXES, 3)
          for signs in product((-1, 1), repeat=3)]
assert len(triads) == 160


def cycle_passes(order):
    return tuple((order[i], order[(i+1) % 3]) for i in range(3))


def matrix(order):
    # We fix T separately; signed port identities are canonically enumerated 0,1,2.
    M = [[0]*3 for _ in range(3)]
    for a, b in cycle_passes(order):
        assert a != b
        M[a][b] += 1
    return tuple(tuple(row) for row in M)


def skew(M):
    return tuple(tuple(M[i][j] - M[j][i] for j in range(3)) for i in range(3))


def contrast(M):
    return tuple(sum(M[i]) - sum(M[j][i] for j in range(3)) for i in range(3))

orders = tuple(permutations(range(3)))
assert len(orders) == 6
local_classes = defaultdict(list)
phase_joint = {}
first_pass_joint = {}
for order in orders:
    M = matrix(order)
    om = skew(M)
    u = contrast(M)
    local_classes[om].append(order)
    assert u == (0,0,0)
    assert sum(sum(row) for row in M) == 3
    assert set(cycle_passes(order)) == set(cycle_passes(order[1:]+order[:1]))
    assert matrix(order) == matrix(order[1:]+order[:1])
    assert om == skew(matrix(order[1:]+order[:1]))
    assert (om, order[0]) not in phase_joint
    phase_joint[(om,order[0])] = order
    first_pass = cycle_passes(order)[0]
    assert first_pass not in first_pass_joint
    first_pass_joint[first_pass] = order

assert len(local_classes)==2
assert sorted(map(len,local_classes.values()))==[3,3]
assert len(phase_joint) == 6
assert len(first_pass_joint) == 6
for m, os in local_classes.items():
    rev = tuple(reversed(os[0]))
    assert skew(matrix(rev)) == tuple(tuple(-x for x in row) for row in m)
    assert all(matrix(o) == matrix(os[0]) for o in os)
    assert sum(abs(x) for row in m for x in row) == 6
    assert any(x for row in m for x in row)

n_ordered = n_oriented = n_full = n_firstpass = 0
for T in triads:
    Taxis = [p[0] for p in T]
    assert len(set(Taxis)) == 3
    signed_orders = [tuple(T[i] for i in o) for o in orders]
    sig = defaultdict(list)
    sigfirst = set()
    sigpass = set()
    for order, signed_order in zip(orders, signed_orders):
        # The retained signed T and a chosen injection beta_T into 3 local ports
        # distinguish T; compare source-order signatures within each T.
        M = matrix(order)
        sig[skew(M)].append(order)
        sigfirst.add((skew(M), signed_order[0]))
        sigpass.add(tuple(T[i] for i in cycle_passes(order)[0]))
        for k in range(1, 8):
            rot = order[k%3:]+order[:k%3]
            assert matrix(rot) == M
            cumul = tuple(tuple(k*v for v in row) for row in M)
            assert skew(cumul) == tuple(tuple(k*v for v in row) for row in skew(M))
    assert sorted(map(len,sig.values())) == [3,3]
    assert len(sigfirst)==6
    assert len(sigpass)==6
    n_ordered+=len(signed_orders)
    n_oriented+=len(sig)
    n_full+=len(sigfirst)
    n_firstpass+=len(sigpass)
assert (n_ordered,n_oriented,n_full,n_firstpass)==(960,320,960,960)

# Explicit arithmetic realization: V29 PASS increments each M[a,b] by one,
# and TRANSFER increments no M; hence three passes are both necessary and sufficient
# to realize the positive adjacency matrix of a directed three-cycle.
output = {
 "research_unit": "R762S",
 "arithmetic": "exact integers",
 "finite_domain": {"spatial_axes":6,"signed_distinct_axis_triads":160,"orders_each":6,"ordered_states":960},
 "candidate_bridge": "three internal V29 PASS increments on a fixed declared 3-port token injection beta_T; zero TRANSFER",
 "pass_count_per_event":3,
 "cumulative_pass_count_after_k_events":"3k",
 "unique_oriented_signatures_retaining_T":n_oriented,
 "oriented_signature_fiber_size":3,
 "unobserved_phase_repair_min_bits":2,
 "unique_signatures_retaining_T_skew_and_first_token":n_full,
 "unique_first_directed_pass_increments_retaining_T":n_firstpass,
 "first_directed_pass_increment_order_fiber":1,
 "v29_u_per_complete_event":[0,0,0],
 "v29_total_charge_change":0,
 "skew_rank_each":2,
 "spatial_endpoint_and_rooted_edge_current":"zero (R762R candidate)",
 "repeated_pass_omega_signature":"k times initial Omega, hidden C3 phase unchanged for all k>=1",
 "validation":"all finite asserts passed",
 "scope":"candidate typed lift; native event admission / actual V39 transport not established"
}
print(dumps(output,sort_keys=True,indent=2))
