#!/usr/bin/env python3
"""Deterministic checker for P000 Philosophy-First Q13 branching path-return stress.

No external packages. It verifies:
1) the exact smallest 4-Cell branching-core class by exhaustive enumeration;
2) scalar/set-valued return collisions K4 vs K4-e;
3) multiplicity packet separation and exact B4 representability image;
4) an explicit 10-Cell cubic collision showing set-support failure persists
   even when every Cell has the same native degree;
5) the exact missing multiplicity witness: 2 versus 3 simple 4-returns.
"""

from __future__ import annotations
from collections import Counter
from itertools import combinations

checks = 0


def check(cond, msg):
    global checks
    checks += 1
    if not cond:
        raise AssertionError(msg)


def make_graph(n, edges):
    adj = [set() for _ in range(n)]
    norm = set()
    for a, b in edges:
        if a == b:
            raise ValueError("loops forbidden")
        u, v = sorted((a, b))
        if (u, v) in norm:
            raise ValueError("duplicate edge")
        norm.add((u, v))
        adj[u].add(v)
        adj[v].add(u)
    return adj


def connected(adj):
    seen = {0}
    stack = [0]
    while stack:
        u = stack.pop()
        for v in adj[u]:
            if v not in seen:
                seen.add(v)
                stack.append(v)
    return len(seen) == len(adj)


def canonical_cycle(path):
    path = list(path)
    m = len(path)
    forms = []
    for seq in (path, list(reversed(path))):
        for i in range(m):
            forms.append(tuple(seq[i:] + seq[:i]))
    return min(forms)


def simple_cycles(adj):
    """All undirected simple cycles, with orientation and basepoint quotiented."""
    n = len(adj)
    seen = set()
    for start in range(n):
        stack = [(start, (start,))]
        while stack:
            u, path = stack.pop()
            for v in adj[u]:
                if v == start:
                    if len(path) >= 3:
                        seen.add(canonical_cycle(path))
                    continue
                if v in path:
                    continue
                if len(path) < n:
                    stack.append((v, path + (v,)))
    return tuple(sorted(seen))


def return_packets(adj):
    cycles = simple_cycles(adj)
    by_root = [Counter() for _ in adj]
    for cyc in cycles:
        k = len(cyc)
        for v in cyc:
            by_root[v][k] += 1

    support_hist = tuple(sorted(tuple(sorted(c)) for c in by_root))
    min_hist = tuple(sorted(min(c) for c in by_root))
    mult_hist = tuple(
        sorted(tuple(sorted(counter.items())) for counter in by_root)
    )
    cycle_count = Counter(map(len, cycles))
    return min_hist, support_hist, mult_hist, cycle_count


def all_graphs_on_four():
    vertices = range(4)
    all_edges = list(combinations(vertices, 2))
    for mask in range(1 << len(all_edges)):
        edges = [e for i, e in enumerate(all_edges) if (mask >> i) & 1]
        yield edges, make_graph(4, edges)


# Frozen smallest branching-core class:
# connected, simple, |V|=4, min degree >=2, max degree <=3, some degree 3.
b4 = []
for edges, adj in all_graphs_on_four():
    deg = tuple(sorted(len(adj[v]) for v in range(4)))
    if connected(adj) and min(deg) >= 2 and max(deg) <= 3 and 3 in deg:
        b4.append((edges, adj, deg, return_packets(adj)))

check(len(b4) == 7, f"expected 7 labeled B4 graphs, got {len(b4)}")
check(Counter(len(edges) for edges, *_ in b4) == Counter({5: 6, 6: 1}),
      "B4 must be six labeled diamonds plus K4")
check({deg for _, _, deg, _ in b4} == {(2, 2, 3, 3), (3, 3, 3, 3)},
      "unexpected B4 degree types")

min_packets = {packets[0] for *_, packets in b4}
set_packets = {packets[1] for *_, packets in b4}
mult_packets = {packets[2] for *_, packets in b4}

expected_min = (3, 3, 3, 3)
expected_set = ((3, 4),) * 4
diamond_mult = (
    ((3, 1), (4, 1)),
    ((3, 1), (4, 1)),
    ((3, 2), (4, 1)),
    ((3, 2), (4, 1)),
)
k4_mult = (((3, 3), (4, 3)),) * 4

check(min_packets == {expected_min}, "minimum-return packet should collide on all B4")
check(set_packets == {expected_set}, "set-valued return packet should collide on all B4")
check(mult_packets == {diamond_mult, k4_mult},
      "multiplicity packet should have exactly the two B4 isomorphism images")

# Exact representability image on declared B4.
packet_counts = Counter(packets[2] for *_, packets in b4)
check(packet_counts[diamond_mult] == 6, "diamond multiplicity packet labeled count")
check(packet_counts[k4_mult] == 1, "K4 multiplicity packet labeled count")
check(len(packet_counts) == 2, "B4 multiplicity representability image must have size two")

# Minimal scalar ambiguity: branch degree 3 is impossible below 4 vertices.
for n in range(1, 4):
    check(n - 1 < 3, "degree-3 vertex impossible below four vertices")

# Explicit cubic 10-Cell support collision.
H_EDGES = [
    (0,1),(0,3),(0,8),(1,4),(1,8),
    (2,4),(2,6),(2,9),(3,5),(3,9),
    (4,7),(5,7),(5,8),(6,7),(6,9),
]
G_EDGES = [
    (0,3),(0,5),(0,6),(1,2),(1,3),
    (1,6),(2,6),(2,9),(3,4),(4,5),
    (4,8),(5,7),(7,8),(7,9),(8,9),
]
H = make_graph(10, H_EDGES)
G = make_graph(10, G_EDGES)
check(connected(H) and connected(G), "cubic witnesses must be connected")
check(all(len(H[v]) == 3 for v in range(10)), "H must be cubic")
check(all(len(G[v]) == 3 for v in range(10)), "G must be cubic")

H_min, H_set, H_mult, H_cycles = return_packets(H)
G_min, G_set, G_mult, G_cycles = return_packets(G)

expected_cubic_set = tuple(sorted(
    [tuple(range(3, 11))] * 4
    + [(3,5,6,7,8,9,10)] * 2
    + [tuple(range(4, 11))] * 4
))
check(H_set == expected_cubic_set, f"H support packet drifted: {H_set}")
check(G_set == expected_cubic_set, f"G support packet drifted: {G_set}")
check(H_min == G_min == (3,3,3,3,3,3,4,4,4,4),
      "cubic witnesses must also collide under minimum return")
check(H_cycles[3] == G_cycles[3] == 2, "both cubic witnesses should have two triangles")
check(H_cycles[4] == 2 and G_cycles[4] == 3,
      "4-return multiplicity must split H and G")
check(H_mult != G_mult, "multiplicity packet must split cubic support collision")

# Different total 4-cycle count is an isomorphism invariant, so H and G are nonisomorphic.
check(H_cycles[4] != G_cycles[4], "nonisomorphism certificate failed")

print(
    "PASS P000_Q13_BRANCHING_PATH_RETURN; "
    f"checks={checks}; "
    "B4_labeled=7; B4_iso_types=2; "
    "scalar_and_set_packet_collision=YES; "
    "B4_multiplicity_image=2; "
    "cubic10_set_support_collision=YES; "
    f"cubic10_C4_counts={H_cycles[4]}_vs_{G_cycles[4]}"
)
