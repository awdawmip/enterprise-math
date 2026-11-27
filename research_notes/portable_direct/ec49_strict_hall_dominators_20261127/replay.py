"""Exact author check for the strict-Hall residual graph and dominator blocks."""

import json
from collections import Counter, deque
from itertools import combinations_with_replacement, product
from random import Random

SINK = ("sink", 0)


def selected_ports(mask, n):
    return [i for i in range(n) if mask >> i & 1]


def descendants(adjacency, start, skip=None):
    visit = {start}
    queue = deque([start])
    while queue:
        node = queue.popleft()
        for child in adjacency.get(node, ()):
            if child not in visit and (node, child) != skip:
                visit.add(child)
                queue.append(child)
    return visit


def make_residual(capacity, edges, assignment):
    """Reverse the augmented graph and subdivide capacity-one arcs."""
    n = len(capacity)
    slack = list(capacity)
    vertices = [SINK] + [("port", i) for i in range(n)]
    vertices.extend(("target", x) for x in range(len(edges)))
    predecessor = {v: [] for v in vertices}
    successor = {v: [] for v in vertices}
    unit_nodes = []

    def reverse_arc(u, v, unit=False):
        if unit:
            a = ("arc", len(unit_nodes))
            unit_nodes.append(a)
            successor[a] = [u]
            predecessor[a] = [v]
            successor[v].append(a)
            predecessor[u].append(a)
        else:
            successor[v].append(u)
            predecessor[u].append(v)

    for x, matched_port in enumerate(assignment):
        slack[matched_port] -= 1
        reverse_arc(("port", matched_port), ("target", x), unit=True)
        for i in selected_ports(edges[x], n):
            reverse_arc(("target", x), ("port", i))
    for i, empty_slots in enumerate(slack):
        if empty_slots:
            reverse_arc(("port", i), SINK, unit=empty_slots == 1)
    return successor, predecessor, unit_nodes


def dominators(successor, predecessor):
    """Reference fixed-point dominators, for these bounded exact checks."""
    vertices = list(successor)
    index = {v: i for i, v in enumerate(vertices)}
    full = (1 << len(vertices)) - 1
    bit = {v: 1 << i for v, i in index.items()}
    dom = {v: full for v in vertices}
    dom[SINK] = bit[SINK]
    changed = True
    while changed:
        changed = False
        for v in vertices:
            if v == SINK:
                continue
            mask = full
            for u in predecessor[v]:
                mask &= dom[u]
            mask |= bit[v]
            if mask != dom[v]:
                dom[v] = mask
                changed = True
    return {v: {u for u in vertices if mask & bit[u]} for v, mask in dom.items()}


def brute_properties(capacity, masks):
    n = len(capacity)
    differences = {}
    for u in range(1, 1 << n):
        differences[u] = sum(capacity[i] for i in selected_ports(u, n)) - sum(
            edge & u == edge for edge in masks
        )
    tight = {u for u, value in differences.items() if value == 1}
    blocks = {u for u in tight if all(u == v or u & v != u for v in tight)}
    return (
        all(value >= 0 for value in differences.values()),
        all(value >= 1 for value in differences.values()),
        blocks,
    )


def enumerated_assignments(capacity, masks):
    for assignment in product(*(selected_ports(mask, len(capacity)) for mask in masks)):
        if all(assignment.count(i) <= cap for i, cap in enumerate(capacity)):
            yield assignment


def check_instance(capacity, masks, counts, max_assignments=None):
    counts["instances"] += 1
    ordinary, strict, blocks = brute_properties(capacity, masks)
    assignments = enumerated_assignments(capacity, masks)
    found = False
    for j, assignment in enumerate(assignments):
        if max_assignments is not None and j >= max_assignments:
            break
        found = True
        counts["saturating_assignments"] += 1
        forward, backward, unit_nodes = make_residual(capacity, masks, assignment)
        reachable = descendants(forward, SINK)
        assert strict == all(("port", i) in reachable for i in range(len(capacity)))
        if not strict:
            counts["nonstrict_assignments"] += 1
            continue
        assert len(forward) == len(reachable)
        counts["strict_assignments"] += 1
        dom = dominators(forward, backward)
        recovered = {}
        for i in range(len(capacity)):
            port = ("port", i)
            units = {u for u in dom[port] if u[0] == "arc"}
            if units:
                top = min(units, key=lambda u: len(dom[u]))
                recovered[top] = recovered.get(top, 0) | 1 << i
        assert set(recovered.values()) == blocks, (capacity, masks, assignment)
        # A second check uses only each unit-arc deletion and reachability.
        missing_masks = set()
        for a in unit_nodes:
            (parent,) = backward[a]
            visit = descendants(forward, SINK, skip=(parent, a))
            missing = sum(1 << i for i in range(len(capacity)) if ("port", i) not in visit)
            if missing:
                missing_masks.add(missing)
        assert {u for u in missing_masks if all(u == v or u & v != u for v in missing_masks)} == blocks
        for candidate in range(1, 1 << len(capacity)):
            can_insert = all(candidate & block != candidate for block in blocks)
            assert can_insert == brute_properties(capacity, masks + (candidate,))[1]
            counts["insertion_tests"] += 1
    assert ordinary == found, (capacity, masks)


def run():
    counts = dict.fromkeys(
        ["instances", "saturating_assignments", "strict_assignments",
         "nonstrict_assignments", "insertion_tests"], 0
    )
    for n in range(1, 4):
        for capacity in product(range(3), repeat=n):
            for m in range(5):
                for masks in combinations_with_replacement(range(1, 1 << n), m):
                    check_instance(capacity, masks, counts)
    rng = Random(4926112703)
    sample = dict.fromkeys(counts, 0)
    for _ in range(1200):
        n = rng.choice((4, 5, 6))
        capacity = tuple(rng.randrange(5) for _ in range(n))
        masks = tuple(rng.randrange(1, 1 << n) for _ in range(rng.randrange(8)))
        check_instance(capacity, masks, sample, max_assignments=5)
    paired = ((7, 1), (3, 5))
    capacities = (2, 2, 2)
    projections = [Counter((0, j) for mask in masks for j in selected_ports(mask, 3))
                   for masks in paired]
    assert projections[0] == projections[1]
    pair_blocks = []
    for masks in paired:
        assert (0, 0) in enumerated_assignments(capacities, masks)
        ordinary, strict, blocks = brute_properties(capacities, masks)
        assert ordinary and strict
        pair_blocks.append(sorted(blocks))
    assert pair_blocks == [[1], []]
    return {"exhaustive": counts, "seed": 4926112703, "sample": sample,
            "same_port_projection_counterexample": {
                "capacity": capacities, "assignment": [0, 0],
                "masks": paired, "maximal_tight_blocks": pair_blocks,
            }}


if __name__ == "__main__":
    print(json.dumps(run(), indent=2))
