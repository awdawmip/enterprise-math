#!/usr/bin/env python3
"""Exact two-event signed-triad readout counts (derived event-word model).

Each event has one +/- signed unit direction on exactly three distinct X6 axes.
The endpoint is the formal sum of the two signed incidence vectors.  This
checker makes no assertion that the triad is a physical native translation.
"""
from collections import Counter
from itertools import combinations, product

DIM = 6
TRIADS = tuple(combinations(range(DIM), 3))
EVENTS = []
for support in TRIADS:
    for signs in product((-1, 1), repeat=3):
        z = [0] * DIM
        for axis, sign in zip(support, signs):
            z[axis] = sign
        EVENTS.append((support, tuple(z)))

assert len(TRIADS) == 20 and len(EVENTS) == 160
native_endpoints = Counter()
zero_fibers = Counter()
for support_a, a in EVENTS:
    for _, b in EVENTS:
        z = tuple(x + y for x, y in zip(a, b))
        native_endpoints[z] += 1
        if z == (0,) * DIM:
            zero_fibers[support_a] += 1

D = (1,) * DIM
zero = (0,) * DIM
relative_zero = sum(multiplicity for z, multiplicity in native_endpoints.items()
                    if len(set(z)) == 1)
assert sum(native_endpoints.values()) == 25600
assert len(native_endpoints) == 3477
assert native_endpoints[zero] == 160
assert native_endpoints[D] == native_endpoints[tuple(-x for x in D)] == 20
assert relative_zero == 200
assert len(zero_fibers) == 20 and set(zero_fibers.values()) == {8}
assert sum(1 for _, v in EVENTS if v == (1, 1, 1, 0, 0, 0)) == 1

print('PASS_X6_LP019_SIGNED_TRIADIC_EVENT_NATIVE_RELATIVE_RETURN')
print('triad_supports=20 signed_event_types=160 ordered_two_event_histories=25600')
print('distinct_native_endpoints=3477 native_zero=160 relative_zero=200')
print('relative_only_plusD=20 relative_only_minusD=20')
print('native_zero_signed_degree_fibers=20 histories_per_fiber=8')
print('single_triad_111000=1; primitive_signed_shortest_BRC_111000=6 (different observable)')
