#!/usr/bin/env python3
"""Independent exact replication checker for P000 Gen21 PF10/connection moduli.

This checker rebuilds the finite tetra/K4 model from vertex permutations and does
not import the frozen Gen21 checker as a derivation engine.  It retains raw seed
identity through gauge compression so flatness/holonomy information is not lost.
"""
from __future__ import annotations

from collections import defaultdict, deque
from itertools import permutations

CELLS = tuple(range(4))
EDGES = tuple((i, j) for i in CELLS for j in CELLS if i < j)
EDGE_INDEX = {e: i for i, e in enumerate(EDGES)}
EDGE_NAMES = tuple(f"E{i+1}" for i in range(6))
ID4 = tuple(range(4))
ID6 = tuple(range(6))
S4 = tuple(permutations(range(4)))
S6 = tuple(permutations(range(6)))
ORIENTED = tuple((x, y) for x in CELLS for y in CELLS if x != y)
NON_TREE = ((1, 2), (1, 3), (2, 3))
LOOPS = ((0, 1, 2, 0), (0, 1, 3, 0), (0, 2, 3, 0))


def comp(p, q):
    return tuple(p[q[i]] for i in range(len(q)))


def inv(p):
    out = [0] * len(p)
    for i, j in enumerate(p):
        out[j] = i
    return tuple(out)


def conj(g, h):
    return comp(comp(g, h), inv(g))


def edge_action(g):
    out = []
    for i, j in EDGES:
        a, b = sorted((g[i], g[j]))
        out.append(EDGE_INDEX[(a, b)])
    return tuple(out)


RHO = {g: edge_action(g) for g in S4}
assert len(set(RHO.values())) == 24


def action_orbits(group, objects, action):
    unseen = set(objects)
    result = []
    while unseen:
        x = next(iter(unseen))
        orb = {action(g, x) for g in group}
        result.append(frozenset(orb))
        unseen -= orb
    return result


def cycle_form(p):
    seen = [False] * len(p)
    cycles = []
    for i in range(len(p)):
        if seen[i]:
            continue
        c = []
        j = i
        while not seen[j]:
            seen[j] = True
            c.append(j)
            j = p[j]
        if len(c) > 1:
            cycles.append(tuple(c))
    if not cycles:
        return "id"
    return "".join("(" + " ".join(EDGE_NAMES[i] for i in c) + ")" for c in cycles)


def cycle_type(p):
    seen = [False] * len(p)
    sizes = []
    for i in range(len(p)):
        if seen[i]:
            continue
        j, n = i, 0
        while not seen[j]:
            seen[j] = True
            n += 1
            j = p[j]
        sizes.append(n)
    return tuple(sorted(sizes, reverse=True))


def subgroup_order(gens):
    gens = tuple(gens) + tuple(inv(g) for g in gens)
    seen = {ID6}
    q = deque([ID6])
    while q:
        x = q.popleft()
        for g in gens:
            y = comp(g, x)
            if y not in seen:
                seen.add(y)
                q.append(y)
    return len(seen)


def connection_from_seed(t):
    reps = {}
    for x, y in ORIENTED:
        reps[(x, y)] = min(g for g in S4 if g[0] == x and g[1] == y)
    T = {(x, y): conj(RHO[reps[(x, y)]], t) for x, y in ORIENTED}
    for x, y in ORIENTED:
        vals = {conj(RHO[g], t) for g in S4 if g[0] == x and g[1] == y}
        assert len(vals) == 1
        assert T[(x, y)] in vals
        assert T[(y, x)] == inv(T[(x, y)])
    return T


def gauge_triple(T):
    gauges = {0: ID6}
    for x in (1, 2, 3):
        gauges[x] = inv(T[(0, x)])
    Tp = {}
    for x, y in ORIENTED:
        Tp[(x, y)] = comp(comp(gauges[y], T[(x, y)]), inv(gauges[x]))
    assert all(Tp[(0, x)] == ID6 for x in (1, 2, 3))
    return tuple(Tp[e] for e in NON_TREE)


def canonical_triple(triple):
    return min(tuple(conj(h, p) for p in triple) for h in S6)


def holonomy(T, loop):
    h = ID6
    for x, y in zip(loop, loop[1:]):
        h = comp(T[(x, y)], h)
    return h


def incidence_vector(x):
    return tuple(1 if x in e else 0 for e in EDGES)


def permute_vector(p, v):
    out = [0] * len(v)
    for i, j in enumerate(p):
        out[j] = v[i]
    return tuple(out)


def main():
    # PF10 orbit parameterization.
    HA = tuple(g for g in S4 if g[0] == 0)
    pairs = tuple((i, j) for i in range(6) for j in range(6))
    full_vec = action_orbits(S4, range(6), lambda g, i: RHO[g][i])
    full_pair = action_orbits(S4, pairs, lambda g, ij: (RHO[g][ij[0]], RHO[g][ij[1]]))
    base_vec = action_orbits(HA, range(6), lambda g, i: RHO[g][i])
    base_pair = action_orbits(HA, pairs, lambda g, ij: (RHO[g][ij[0]], RHO[g][ij[1]]))
    assert len(full_vec) == 1
    assert len(full_pair) == 3
    assert {frozenset(o) for o in base_vec} == {frozenset({0, 1, 2}), frozenset({3, 4, 5})}
    assert len(base_pair) == 8
    assert 2 + 2 + 8 == 12

    # Explicit nonconstant PF10 witness and exact S4 transport.
    I = {x: incidence_vector(x) for x in CELLS}
    O = {x: tuple(1 - z for z in I[x]) for x in CELLS}
    assert len(set(I.values())) == 4
    for g in S4:
        p = RHO[g]
        for x in CELLS:
            assert permute_vector(p, I[x]) == I[g[x]]
            assert permute_vector(p, O[x]) == O[g[x]]

    # Legal seed locus from oriented-edge stabilizer and reverse-edge law.
    kappa = RHO[(0, 1, 3, 2)]  # (CD) on channels
    lam = RHO[(1, 0, 2, 3)]    # (AB) on channels
    assert comp(kappa, lam) == comp(lam, kappa)
    centralizer = tuple(s for s in S6 if comp(s, kappa) == comp(kappa, s))
    involutions = tuple(s for s in centralizer if comp(s, s) == ID6)
    legal = tuple(
        t for t in S6
        if comp(t, kappa) == comp(kappa, t)
        and comp(comp(lam, t), lam) == inv(t)
    )
    assert len(centralizer) == 16
    assert len(involutions) == 12
    assert {comp(lam, t) for t in legal} == set(involutions)
    assert len(legal) == 12

    expected_forms = (
        "id",
        "(E2 E3)(E4 E5)",
        "(E2 E4)(E3 E5)",
        "(E2 E4 E3 E5)",
        "(E2 E5 E3 E4)",
        "(E2 E5)(E3 E4)",
        "(E1 E6)",
        "(E1 E6)(E2 E3)(E4 E5)",
        "(E1 E6)(E2 E4)(E3 E5)",
        "(E1 E6)(E2 E4 E3 E5)",
        "(E1 E6)(E2 E5 E3 E4)",
        "(E1 E6)(E2 E5)(E3 E4)",
    )
    assert tuple(cycle_form(t) for t in legal) == expected_forms

    connections = tuple(connection_from_seed(t) for t in legal)

    # Full carrier naturality and holonomy conjugacy.
    for T in connections:
        for g in S4:
            pg = RHO[g]
            for x, y in ORIENTED:
                assert T[(g[x], g[y])] == conj(pg, T[(x, y)])
            for loop in LOOPS:
                moved = tuple(g[v] for v in loop)
                assert holonomy(T, moved) == conj(pg, holonomy(T, loop))

    # Gauge quotient retains raw provenance before simultaneous-conjugacy compression.
    classes = defaultdict(list)
    triples = []
    for i, T in enumerate(connections):
        tr = gauge_triple(T)
        triples.append(tr)
        classes[canonical_triple(tr)].append(i)
    raw_partition = sorted(classes.values(), key=min)
    assert raw_partition == [[0, 5], [1], [2], [3, 4], [6, 11], [7], [8], [9, 10]]
    assert len(raw_partition) == 8

    expected_fingerprints = (
        ((1, 1, 1, 1, 1, 1), 1, True),
        ((4, 2), 24, False),
        ((2, 2, 1, 1), 6, False),
        ((2, 1, 1, 1, 1), 6, False),
        ((2, 2, 2), 2, False),
        ((2, 2, 2), 6, False),
        ((4, 1, 1), 24, False),
        ((5, 1), 60, False),
    )
    raw_flat = 0
    class_rows = []
    for ci, members in enumerate(raw_partition):
        rep = members[0]
        hs = tuple(holonomy(connections[rep], loop) for loop in LOOPS)
        types = tuple(cycle_type(h) for h in hs)
        assert len(set(types)) == 1
        flat = all(h == ID6 for h in hs)
        order = subgroup_order(hs)
        assert (types[0], order, flat) == expected_fingerprints[ci]
        class_rows.append((members, cycle_form(legal[rep]), types[0], order, flat))
    for T in connections:
        if all(holonomy(T, loop) == ID6 for loop in LOOPS):
            raw_flat += 1
    assert raw_flat == 2
    assert len(connections) - raw_flat == 10
    assert sum(1 for row in class_rows if row[-1]) == 1
    assert sum(1 for row in class_rows if not row[-1]) == 7

    # Same-model nonconstant PF10 + Gen18 edge/opposite nonflat connection witness.
    witness_index = expected_forms.index("(E1 E6)")
    W = connections[witness_index]
    opposite = {}
    for i, e in enumerate(EDGES):
        complement = tuple(sorted(set(CELLS) - set(e)))
        opposite[i] = EDGE_INDEX[complement]
    for x, y in ORIENTED:
        i = EDGE_INDEX[tuple(sorted((x, y)))]
        j = opposite[i]
        expected = list(ID6)
        expected[i], expected[j] = expected[j], expected[i]
        assert W[(x, y)] == tuple(expected)
    omega = (5, 4, 3, 2, 1, 0)
    assert all(holonomy(W, loop) == omega for loop in LOOPS)

    # Frozen carrier presentation relations; PF10 and connection were checked equivariant for all S4.
    a = (0, 2, 3, 1)  # (BCD)
    b = (1, 0, 2, 3)  # (AB)
    def power(p, n):
        r = tuple(range(len(p)))
        for _ in range(n):
            r = comp(p, r)
        return r
    assert power(a, 3) == ID4
    assert power(b, 2) == ID4
    assert power(comp(a, b), 4) == ID4

    print("PASS: independent Gen21 replication; PF10 slots=12, seeds=12, gauge classes=8, flat/nonflat classes=1/7.")


if __name__ == "__main__":
    main()
