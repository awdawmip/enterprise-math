#!/usr/bin/env python3
"""R762HG independent positive integer BRC source-state recurrences.
Signed displacement is a coordinate label, NEVER a negative BRC weight.
"""
from collections import defaultdict
from itertools import combinations

ports = list(combinations(range(6), 2))
transitions = []
for p in ports:
    transitions.append([
        (j, tuple(int(a in set(p) | set(q)) for a in range(6)),
         sum(1 << a for a in (set(p) | set(q))))
        for j, q in enumerate(ports) if len(set(p) & set(q)) == 1
    ])

parity = {(0, 0): 1}
signed = {(0, (0,) * 6): 1}
expected = {
    2: (8, 8, 16),
    4: (288, 168, 624),
    6: (17536, 4960, 34688),
    8: (1118720, 177536, 2413424),
    10: (71583744, 7289184, 200986368),
    12: (4581302272, 333869824, 19705107552),
}
for n in range(1, 7):
    next_parity = defaultdict(int)
    for (p, mask), count in parity.items():
        for q, _, supmask in transitions[p]:
            next_parity[(q, mask ^ supmask)] += count
    parity = dict(next_parity)
    next_signed = defaultdict(int)
    for (p, vec), count in signed.items():
        for q, support, _ in transitions[p]:
            for eps in (-1, 1):
                next_signed[(q, tuple(v + eps * s for v, s in zip(vec, support)))] += count
    signed = dict(next_signed)
    # These Gram identities use the n-step half-path tables to count
    # all 2n-step positive BRC return histories exactly.
    b = sum(count * count for count in parity.values())
    a = sum(count * count for count in signed.values())
    # Unsigned all-Port return: b_n(p) summed over mask, then squared.
    by_port = defaultdict(int)
    for (p, _), count in parity.items():
        by_port[p] += count
    u = sum(v * v for v in by_port.values())
    assert (u, b, a) == expected[2*n], (n, u, b, a)
    print(f"m={2*n} U={u} H={b} Z={a} "
          f"parity_states={len(parity)} signed_states={len(signed)}")
print("PASS")
