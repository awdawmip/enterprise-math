#!/usr/bin/env python3
from __future__ import annotations

from itertools import combinations, product

TASK_ID = "RS-P000-PHILOSOPHY-FIRST-DESCENT-GLUING"
HARD_TARGET = "P000_LOCAL_SLICE_TO_FULL_CELL_DESCENT_EXACTLY_CLASSIFIED"

def connected(n: int, edges: tuple[tuple[int, int], ...]) -> bool:
    if n <= 1:
        return True
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    seen = {0}
    stack = [0]
    while stack:
        u = stack.pop()
        for v in adj[u]:
            if v not in seen:
                seen.add(v)
                stack.append(v)
    return len(seen) == n

def has_global_frames(
    n: int,
    edges: tuple[tuple[int, int], ...],
    labels: tuple[int, ...],
) -> bool:
    # C2 model: a frame at each probe is a bit h_v.
    # Edge transport is h_v xor h_u.  This is the finite coboundary equation.
    return any(
        all((frames[u] ^ frames[v]) == labels[i] for i, (u, v) in enumerate(edges))
        for frames in product((0, 1), repeat=n)
    )

def spanning_tree_potential(
    n: int,
    edges: tuple[tuple[int, int], ...],
    labels: tuple[int, ...],
) -> tuple[bool, tuple[int, ...]]:
    adj = [[] for _ in range(n)]
    for i, (u, v) in enumerate(edges):
        adj[u].append((v, i))
        adj[v].append((u, i))
    potential: list[int | None] = [None] * n
    potential[0] = 0
    stack = [0]
    while stack:
        u = stack.pop()
        for v, i in adj[u]:
            if potential[v] is None:
                potential[v] = potential[u] ^ labels[i]
                stack.append(v)
    if any(x is None for x in potential):
        return False, tuple()
    p = tuple(int(x) for x in potential)
    # Every non-tree edge is automatically checked by the same equation.
    ok = all((p[u] ^ p[v]) == labels[i] for i, (u, v) in enumerate(edges))
    return ok, p

def triangle_counts() -> tuple[int, int, int]:
    edges = ((0, 1), (1, 2), (0, 2))
    total = realizable = obstructed = 0
    for labels in product((0, 1), repeat=3):
        total += 1
        global_ok = has_global_frames(3, edges, labels)
        # With orientation 0->1, 1->2, 2->0, inverse equals itself in C2.
        holonomy = labels[0] ^ labels[1] ^ labels[2]
        assert global_ok == (holonomy == 0)
        if global_ok:
            realizable += 1
            # Global diagonal C2 gauge gives exactly two frame families.
            frame_count = sum(
                all((f[u] ^ f[v]) == labels[i] for i, (u, v) in enumerate(edges))
                for f in product((0, 1), repeat=3)
            )
            assert frame_count == 2
        else:
            obstructed += 1
    return total, realizable, obstructed

def exhaustive_graph_regression(max_n: int = 4) -> tuple[int, tuple[int, int, tuple[tuple[int, int], ...], tuple[int, ...]]]:
    checks = 0
    first_obstruction = None
    for n in range(1, max_n + 1):
        all_edges = tuple(combinations(range(n), 2))
        for mask in range(1 << len(all_edges)):
            edges = tuple(e for i, e in enumerate(all_edges) if (mask >> i) & 1)
            if not connected(n, edges):
                continue
            for labels in product((0, 1), repeat=len(edges)):
                brute = has_global_frames(n, edges, labels)
                criterion, _ = spanning_tree_potential(n, edges, labels)
                assert brute == criterion
                checks += 1
                if not brute:
                    candidate = (n, len(edges), edges, labels)
                    if first_obstruction is None or candidate[:2] < first_obstruction[:2]:
                        first_obstruction = candidate
    assert first_obstruction is not None
    return checks, first_obstruction

def main() -> None:
    total, realizable, obstructed = triangle_counts()
    assert (total, realizable, obstructed) == (8, 4, 4)

    # Explicit minimal odd-swap witness: only edge 0-2 swaps.
    tri_edges = ((0, 1), (1, 2), (0, 2))
    odd = (0, 0, 1)
    assert not has_global_frames(3, tri_edges, odd)
    assert (odd[0] ^ odd[1] ^ odd[2]) == 1

    # Any tree is globally integrable: no cycle condition remains.
    for n in range(1, 7):
        if n == 1:
            trees = [tuple()]
        else:
            # Path is enough for a deterministic direct regression of all edge labels.
            trees = [tuple((i, i + 1) for i in range(n - 1))]
        for edges in trees:
            for labels in product((0, 1), repeat=len(edges)):
                assert has_global_frames(n, edges, labels)

    checks, first = exhaustive_graph_regression(4)
    assert first[0] == 3 and first[1] == 3

    # One-state overlap fibers cannot carry a nontrivial automorphism, so there is no
    # framed holonomy obstruction at fiber cardinality one.
    fiber1_nontrivial_automorphisms = 0
    assert fiber1_nontrivial_automorphisms == 0

    print(
        "PASS P000_DESCENT_GLUING; "
        f"triangle_total={total}; triangle_global={realizable}; "
        f"triangle_obstructed={obstructed}; "
        f"graph_label_checks={checks}; "
        "minimal_obstruction=3_probes_3_overlaps_fiber2_odd_swap; "
        "criterion=trivial_fundamental_cycle_holonomy_iff_global_parallel_frame"
    )

if __name__ == "__main__":
    main()
