#!/usr/bin/env python3
"""Exact R043-C6 root-local successor reduction checker.

The structural theorem is proved in the return.  This checker verifies the exact
update identity and exhausts the connected proper subsets of the twelve native
root-contact positions in both frozen FCC/HCP worlds.  Graph comparisons are
exact VF2++ weighted rooted/unrooted isomorphism tests; WL hashes are only safe
candidate buckets.
"""
from __future__ import annotations

from collections import defaultdict
import json
import networkx as nx

Point = tuple[int, int, int]
ROOT: Point = (0, 0, 0)

FCC_DIRS: list[Point] = []
for zero in range(3):
    others = [i for i in range(3) if i != zero]
    for a in (-1, 1):
        for b in (-1, 1):
            v = [0, 0, 0]
            v[others[0]] = a
            v[others[1]] = b
            FCC_DIRS.append(tuple(v))
FCC_DIRS_T = tuple(sorted(FCC_DIRS))
TRI_DIRS = ((1, 0), (-1, 0), (0, 1), (0, -1), (1, -1), (-1, 1))


def fcc_neighbors(p: Point) -> tuple[Point, ...]:
    x, y, z = p
    return tuple((x + dx, y + dy, z + dz) for dx, dy, dz in FCC_DIRS_T)


def hcp_neighbors(p: Point) -> tuple[Point, ...]:
    i, j, k = p
    out = [(i + di, j + dj, k) for di, dj in TRI_DIRS]
    offsets = ((0, 0), (-1, 0), (0, -1)) if k % 2 == 0 else ((0, 0), (1, 0), (0, 1))
    for dk in (-1, 1):
        for di, dj in offsets:
            out.append((i + di, j + dj, k + dk))
    return tuple(out)


WORLDS = {"fcc": fcc_neighbors, "hcp": hcp_neighbors}


def frontier(C, neighbors) -> set[Point]:
    C = set(C)
    out: set[Point] = set()
    for p in C:
        out.update(neighbors(p))
    return out - C


def connected(C, neighbors) -> bool:
    C = set(C)
    if not C:
        return False
    seen = {next(iter(C))}
    stack = list(seen)
    while stack:
        p = stack.pop()
        for q in neighbors(p):
            if q in C and q not in seen:
                seen.add(q)
                stack.append(q)
    return len(seen) == len(C)


def g0_graph(C, neighbors, root: Point | None = None) -> nx.Graph:
    C = set(C)
    F = frontier(C, neighbors)
    G = nx.Graph()
    for x in F:
        w = sum(q in C for q in neighbors(x))
        is_root = x == root
        G.add_node(x, w=w, root=is_root, lab=f"{w}:{int(is_root)}", wlab=str(w))
    for x in F:
        for y in neighbors(x):
            if y in F and x < y:
                G.add_edge(x, y)
    return G


def wl_key(G: nx.Graph, rooted: bool) -> tuple:
    attr = "lab" if rooted else "wlab"
    return (
        len(G),
        G.number_of_edges(),
        nx.weisfeiler_lehman_graph_hash(G, node_attr=attr, iterations=5, digest_size=16),
    )


def root_extension_profile(C, x: Point, neighbors):
    """J_x: zero-weight new vertices plus all successor edges incident to them."""
    C = set(C)
    F = frontier(C, neighbors)
    if x not in F:
        raise ValueError("root must be a current frontier site")
    Z = set(neighbors(x)) - C - F
    old = F - {x}
    z_old = tuple(sorted((z, y) for z in Z for y in neighbors(z) if y in old))
    z_z = tuple(sorted((z, u) for z in Z for u in neighbors(z) if u in Z and z < u))
    return Z, z_old, z_z


def predicted_successor(C, x: Point, neighbors) -> nx.Graph:
    G = g0_graph(C, neighbors, root=x)
    Z, z_old, z_z = root_extension_profile(C, x, neighbors)
    H = nx.Graph()

    for y, data in G.nodes(data=True):
        if y == x:
            continue
        w = data["w"] + int(G.has_edge(x, y))
        H.add_node(y, w=w, root=False, lab=f"{w}:0", wlab=str(w))
    for u, v in G.edges():
        if x not in (u, v):
            H.add_edge(u, v)

    for z in Z:
        H.add_node(z, w=1, root=False, lab="1:0", wlab="1")
    H.add_edges_from(z_old)
    H.add_edges_from(z_z)
    return H


def update_identity_holds(C, x: Point, neighbors) -> bool:
    predicted = predicted_successor(C, x, neighbors)
    actual = g0_graph(set(C) | {x}, neighbors)
    predicted_edges = {frozenset(e) for e in predicted.edges()}
    actual_edges = {frozenset(e) for e in actual.edges()}
    return (
        set(predicted.nodes()) == set(actual.nodes())
        and predicted_edges == actual_edges
        and all(predicted.nodes[v]["w"] == actual.nodes[v]["w"] for v in actual.nodes())
    )


def exact_class_audit(records) -> dict:
    buckets: dict[tuple, list] = defaultdict(list)
    for C, current, successor in records:
        buckets[wl_key(current, True)].append((C, current, successor))

    duplicate_exact_classes = 0
    exact_pair_tests = 0
    for bucket in buckets.values():
        if len(bucket) < 2:
            continue
        reps: list[tuple[nx.Graph, nx.Graph]] = []
        for _, current, successor in bucket:
            matched = False
            for current_rep, successor_rep in reps:
                exact_pair_tests += 1
                if nx.vf2pp_is_isomorphic(current, current_rep, node_label="lab"):
                    if not nx.vf2pp_is_isomorphic(successor, successor_rep, node_label="wlab"):
                        return {
                            "pass": False,
                            "duplicate_exact_classes": duplicate_exact_classes,
                            "exact_pair_tests": exact_pair_tests,
                            "harmful_split_count": 1,
                        }
                    matched = True
                    break
            if not matched:
                reps.append((current, successor))
                duplicate_exact_classes += 1
    return {
        "pass": True,
        "duplicate_exact_classes": duplicate_exact_classes,
        "exact_pair_tests": exact_pair_tests,
        "harmful_split_count": 0,
    }


def enumerate_root_star(neighbors):
    shell = list(neighbors(ROOT))
    out = []
    closed_cage = (1 << 12) - 1
    for mask in range(1, 1 << 12):
        # The all-12 cage makes ROOT a shielded singleton component and is outside C6.
        if mask == closed_cage:
            continue
        C = frozenset(shell[i] for i in range(12) if (mask >> i) & 1)
        if not connected(C, neighbors):
            continue
        if ROOT not in frontier(C, neighbors):
            continue
        if not update_identity_holds(C, ROOT, neighbors):
            raise AssertionError(("update_identity_failure", C))
        out.append((C, g0_graph(C, neighbors, ROOT), g0_graph(set(C) | {ROOT}, neighbors)))
    return out


def run_world(name: str, neighbors) -> dict:
    records = enumerate_root_star(neighbors)
    return {
        "root_star_states": len(records),
        "update_identity_mismatches": 0,
        "rooted_exact_audit": exact_class_audit(records),
    }


def main() -> None:
    results = {name: run_world(name, neighbors) for name, neighbors in WORLDS.items()}
    ok = all(
        row["update_identity_mismatches"] == 0 and row["rooted_exact_audit"]["pass"]
        for row in results.values()
    )
    payload = {
        "schema": "ENTERPRISE_MATH_R043C6_ROOTED_SUCCESSOR_CHECK_V1",
        "theorem_checked": "G0(C+x) is exactly reconstructed from rooted G0(C,x) plus J_x, the root-local zero-weight exposure incidence profile",
        "profile_cardinality_identity": "|Z_x| = 12 - w_G0(x) - deg_G0(x)",
        "finite_root_star_classification": results,
        "pass": ok,
    }
    print(json.dumps(payload, indent=2, sort_keys=True))
    raise SystemExit(0 if ok else 1)


if __name__ == "__main__":
    main()
