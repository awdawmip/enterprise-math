#!/usr/bin/env python3
"""Exact finite checks for X6 upper V26-V27 channel/triadic circulation bridge."""
from __future__ import annotations

from collections import Counter
from itertools import combinations, permutations

N = 6
TRIADS = tuple(combinations(range(N), 3))
NEIGH = {S: tuple(T for T in TRIADS if len(set(S) & set(T)) == 2) for S in TRIADS}

# Explicit V23 positive four-field code.
MATCHINGS = (
    ((0, 1), (2, 3), (4, 5)),
    ((0, 2), (1, 4), (3, 5)),
    ((0, 3), (1, 5), (2, 4)),
    ((0, 4), (1, 3), (2, 5)),
)


def vmatch(M, S):
    S = set(S)
    bits = []
    for a, b in M:
        if (a in S) + (b in S) != 1:
            return 0
        bits.append(1 if b in S else 0)
    return 1 if sum(bits) % 2 == 0 else -1


CODES = {S: tuple(vmatch(M, S) for M in MATCHINGS) for S in TRIADS}
assert len(set(CODES.values())) == 20

# One unit atomic passage 0->1->2->0 on four typed source/ports.
M = (
    (0, 1, 0, 0),
    (0, 0, 1, 0),
    (1, 0, 0, 0),
    (0, 0, 0, 0),
)
assert all(x >= 0 for row in M for x in row)
OMEGA = tuple(
    tuple(M[i][j] - M[j][i] for j in range(4)) for i in range(4)
)
assert OMEGA == (
    (0, 1, -1, 0),
    (-1, 0, 1, 0),
    (1, -1, 0, 0),
    (0, 0, 0, 0),
)
# rank exactly two: (1,1,1,0) lies in the kernel; a 2x2 minor is nonzero.
assert all(sum(OMEGA[i][j] * (1, 1, 1, 0)[j] for j in range(4)) == 0 for i in range(4))
assert OMEGA[0][1] * OMEGA[1][0] != 0


def matvec(A, v):
    return tuple(sum(A[i][j] * v[j] for j in range(len(v))) for i in range(len(A)))


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def edge_a(S, T, omega=OMEGA):
    return dot(CODES[S], matvec(omega, CODES[T]))


def score(S, T, u):
    return dot(u, CODES[T]) + edge_a(S, T)


# Pure circulation is branched: 18 states have 3 tied maxima, 2 have 9.
def tie_count(S, u):
    vals = [score(S, T, u) for T in NEIGH[S]]
    m = max(vals)
    return sum(v == m for v in vals)


assert Counter(tie_count(S, (0, 0, 0, 0)) for S in TRIADS) == Counter({3: 18, 9: 2})

# PF-10 nonnegative ingress/egress contrast supplying deterministic bias.
I = (0, 0, 0, 10)
O = (2, 4, 3, 0)
U = tuple(i - o for i, o in zip(I, O))
assert U == (-2, -4, -3, 10)
assert all(x >= 0 for x in I + O)


def successor(S):
    ranked = sorted(((score(S, T, U), T) for T in NEIGH[S]), reverse=True)
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
    parity = sum(perm[i] > perm[j] for i in range(3) for j in range(i + 1, 3)) % 2
    return perm, parity


ODD = (
    (0, 1, 2),
    (1, 2, 3),
    (2, 3, 4),
    (0, 3, 4),
    (0, 3, 5),
    (0, 2, 5),
)
FLAT = ((1, 4, 5), (2, 4, 5))
CYCLES = cycles_of_map(UPDATE)
assert set(CYCLES) == {ODD, FLAT}
assert holonomy(ODD) == ((2, 1, 0), 1)
assert holonomy(FLAT) == ((0, 1, 2), 0)
assert [edge_a(ODD[i], ODD[(i + 1) % 6]) for i in range(6)] == [1] * 6
assert sum(edge_a(ODD[i], ODD[(i + 1) % 6]) for i in range(6)) == 6

# Port-relabel covariance: simultaneously relabel code coordinates and PF-10 state.
def perm_vec(v, p):
    out = [0] * len(v)
    for old, new in enumerate(p):
        out[new] = v[old]
    return tuple(out)


def perm_mat(A, p):
    n = len(p)
    out = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            out[p[i]][p[j]] = A[i][j]
    return tuple(tuple(row) for row in out)


for p in permutations(range(4)):
    up = perm_vec(U, p)
    op = perm_mat(OMEGA, p)
    for S in TRIADS:
        cs = perm_vec(CODES[S], p)
        for T in NEIGH[S]:
            ct = perm_vec(CODES[T], p)
            lhs = dot(up, ct) + dot(cs, matvec(op, ct))
            rhs = score(S, T, U)
            assert lhs == rhs

print("PASS_X6_CHANNEL_CIRCULATION_BRIDGE_V26_V27")
print("atomic_passage_skew_rank", 2)
print("pure_circulation_tie_census", {3: 18, 9: 2})
print("minimum_biased_score_gap", min(GAPS.values()))
print("recurrent_cycle_lengths", sorted(map(len, CYCLES)))
print("odd_cycle", ODD)
print("odd_cycle_holonomy", holonomy(ODD))
print("odd_cycle_atomic_circulation", 6)
print("port_relabelings_checked", 24)
