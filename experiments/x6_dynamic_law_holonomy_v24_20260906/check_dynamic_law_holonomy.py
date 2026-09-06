#!/usr/bin/env python3
"""Exact finite checks for X6 upper V24-V25.

Checks:
- local successor-separation threshold in the 30 oriented minimal-field orbit;
- V23 global four-field code count;
- source-neutral separable tie witness;
- explicit rank-2 affine edge-score with unique update and odd V17 holonomy.
"""
from __future__ import annotations

from collections import defaultdict
from itertools import combinations

N = 6
TRIADS = tuple(combinations(range(N), 3))
NEIGH = {
    S: tuple(T for T in TRIADS if len(set(S) & set(T)) == 2)
    for S in TRIADS
}


def perfect_matchings(items):
    items = tuple(items)
    if not items:
        yield ()
        return
    a = items[0]
    for idx in range(1, len(items)):
        b = items[idx]
        rest = items[1:idx] + items[idx + 1 :]
        for m in perfect_matchings(rest):
            yield tuple(sorted(((a, b),) + m))


MATCHINGS = tuple(sorted(set(perfect_matchings(range(N)))))
assert len(MATCHINGS) == 15


def vmatch(M, S):
    S = set(S)
    bits = []
    for a, b in M:
        count = (a in S) + (b in S)
        if count != 1:
            return 0
        bits.append(1 if b in S else 0)
    return 1 if sum(bits) % 2 == 0 else -1


FIELDS = []
for M in MATCHINGS:
    values = tuple(vmatch(M, S) for S in TRIADS)
    FIELDS.append(values)
    FIELDS.append(tuple(-v for v in values))
assert len(FIELDS) == 30
TRIAD_INDEX = {S: i for i, S in enumerate(TRIADS)}


def signature(field_indices, S):
    j = TRIAD_INDEX[S]
    return tuple(FIELDS[i][j] for i in field_indices)


def locally_successor_separating(field_indices):
    for S in TRIADS:
        sigs = {signature(field_indices, T) for T in NEIGH[S]}
        if len(sigs) != 9:
            return False
    return True


def globally_injective(field_indices):
    return len({signature(field_indices, S) for S in TRIADS}) == 20


local_counts = {}
local_four = set()
for r in range(1, 5):
    count = 0
    for combo in combinations(range(30), r):
        if locally_successor_separating(combo):
            count += 1
            if r == 4:
                local_four.add(combo)
    local_counts[r] = count

assert local_counts == {1: 0, 2: 0, 3: 0, 4: 13440}

global_four = {
    combo for combo in combinations(range(30), 4) if globally_injective(combo)
}
assert len(global_four) == 480
assert global_four < local_four
assert len(local_four - global_four) == 12960

# Explicit V23 positive four-field code.
V23_MATCHINGS = (
    ((0, 1), (2, 3), (4, 5)),
    ((0, 2), (1, 4), (3, 5)),
    ((0, 3), (1, 5), (2, 4)),
    ((0, 4), (1, 3), (2, 5)),
)
V23_FIELDS = tuple(2 * MATCHINGS.index(tuple(sorted(M))) for M in V23_MATCHINGS)
CODES = {S: signature(V23_FIELDS, S) for S in TRIADS}
assert len(set(CODES.values())) == 20
assert CODES[(0, 1, 2)] == (0, 0, 1, 1)
assert CODES[(0, 2, 4)] == (1, 0, 0, 0)
assert CODES[(1, 3, 5)] == (-1, 0, 0, 0)
assert CODES[(2, 3, 5)] == (0, 0, 1, 0)
assert CODES[(3, 4, 5)] == (0, 0, -1, -1)

# Source-neutral separable score witness.  If score is
# A*sum(T_i:S_i=-1)+B*sum(T_i:S_i=0)+C*sum(T_i:S_i=+1), then for every
# one-hot current code the nine neighbors remain three triple fibers for all
# choices of A,B,C.
def separable_coeff_class(S, T):
    s = CODES[S]
    t = CODES[T]
    return (
        sum(ti for si, ti in zip(s, t) if si == -1),
        sum(ti for si, ti in zip(s, t) if si == 0),
        sum(ti for si, ti in zip(s, t) if si == 1),
    )


one_hot = [S for S in TRIADS if sum(x * x for x in CODES[S]) == 1]
assert len(one_hot) == 8
for S in one_hot:
    groups = defaultdict(int)
    for T in NEIGH[S]:
        groups[separable_coeff_class(S, T)] += 1
    assert sorted(groups.values()) == [3, 3, 3]

PAIR_ORDER = ((0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3))
U = (-3, -4, 2, 1)
OMEGA = (-1, -1, 0, 0, 0, 0)


def edge_circulation(S, T):
    c = CODES[S]
    d = CODES[T]
    return sum(
        w * (c[i] * d[j] - c[j] * d[i])
        for w, (i, j) in zip(OMEGA, PAIR_ORDER)
    )


def phi(S, T):
    return sum(a * b for a, b in zip(U, CODES[T])) + edge_circulation(S, T)


def successor(S):
    ranked = sorted(((phi(S, T), T) for T in NEIGH[S]), reverse=True)
    assert ranked[0][0] > ranked[1][0]
    return ranked[0][1], ranked[0][0] - ranked[1][0]


UPDATE = {S: successor(S)[0] for S in TRIADS}
GAPS = {S: successor(S)[1] for S in TRIADS}
assert min(GAPS.values()) == 1


def cycles_of_map(f):
    visited = set()
    cycles = []
    for start in TRIADS:
        if start in visited:
            continue
        path = []
        pos = {}
        cur = start
        while cur not in pos and cur not in visited:
            pos[cur] = len(path)
            path.append(cur)
            cur = f[cur]
        if cur in pos:
            cycles.append(tuple(path[pos[cur] :]))
        visited.update(path)
    return cycles


def transport_slots(slotmap, S, T):
    common = set(S) & set(T)
    leave = next(iter(set(S) - common))
    enter = next(iter(set(T) - common))
    out = {a: slotmap[a] for a in common}
    out[enter] = slotmap[leave]
    return out


def holonomy(cycle):
    base = cycle[0]
    slots = {a: i for i, a in enumerate(base)}
    for i, S in enumerate(cycle):
        slots = transport_slots(slots, S, cycle[(i + 1) % len(cycle)])
    perm = tuple(slots[a] for a in base)
    parity = sum(
        perm[i] > perm[j] for i in range(3) for j in range(i + 1, 3)
    ) % 2
    return perm, parity


CYCLES = cycles_of_map(UPDATE)
ODD_CYCLE = (
    (0, 1, 2),
    (0, 1, 5),
    (1, 3, 5),
    (2, 3, 5),
    (2, 4, 5),
    (1, 2, 4),
)
FLAT_TWO = ((0, 3, 4), (0, 4, 5))
assert set(CYCLES) == {ODD_CYCLE, FLAT_TWO}
assert holonomy(ODD_CYCLE) == ((0, 2, 1), 1)
assert holonomy(FLAT_TWO) == ((0, 1, 2), 0)
assert sum(
    edge_circulation(ODD_CYCLE[i], ODD_CYCLE[(i + 1) % 6])
    for i in range(6)
) == 4
assert [
    edge_circulation(ODD_CYCLE[i], ODD_CYCLE[(i + 1) % 6])
    for i in range(6)
] == [0, 1, 1, 0, 1, 1]
assert [
    phi(ODD_CYCLE[i], ODD_CYCLE[(i + 1) % 6])
    for i in range(6)
] == [3, 4, 3, 4, 3, 4]

# Exact rank of the skew matrix: rows 1 and 2 coincide, and the 2x2 minor
# on rows/cols (0,1) is nonzero, so rank is exactly 2.
OMEGA_MATRIX = (
    (0, -1, -1, 0),
    (1, 0, 0, 0),
    (1, 0, 0, 0),
    (0, 0, 0, 0),
)
assert OMEGA_MATRIX[0][1] * OMEGA_MATRIX[1][0] != 0
assert OMEGA_MATRIX[1] == OMEGA_MATRIX[2]

print("PASS_X6_DYNAMIC_LAW_HOLONOMY_V24_V25")
print("local_successor_separating_counts", local_counts)
print("global_four_field_codes", len(global_four))
print("local_only_four_field_sets", len(local_four - global_four))
print("source_neutral_one_hot_tie_states", len(one_hot))
print("edge_circulation_rank", 2)
print("minimum_unique_score_gap", min(GAPS.values()))
print("recurrent_cycle_lengths", sorted(map(len, CYCLES)))
print("odd_cycle", ODD_CYCLE)
print("odd_cycle_holonomy", holonomy(ODD_CYCLE))
print("odd_cycle_edge_circulation", 4)
