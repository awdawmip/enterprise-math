"""Separation of precision repair from local shortcut compilation.

Executable evidence only; theorem targets are finite transition-system statements.

Fix a finite state set X, an observation partition E, and primitive endomaps A.
The Moore/Nerode repair R_A(E) is the coarsest A-stable refinement of E.

Once a stable quotient Q is fixed, arbitrary source-local shortcut rules that
preserve reachability and bound inference depth by k are exactly k-TC-spanners
of the induced quotient transition graph.

If F refines Q and both are A-stable, the natural quotient map F -> Q projects
every k-TC-spanner of F to a k-TC-spanner of Q. Consequently the coarsest stable
repair simultaneously minimizes state count and the minimum local-shortcut
edge count among all stable refinements of the original observation.

This monotonicity is specific to local edge rules with uniform edge cost.
Global macros are more constrained: one stored endomap bundles transitions
from all source states and leads to a transformation-semigroup generator/
diameter problem instead of an unrestricted TC-spanner problem.
"""

from __future__ import annotations

from collections import deque
from itertools import combinations
from typing import Hashable, Iterable, Sequence

Partition = tuple[int, ...]
Endomap = tuple[int, ...]
Edge = tuple[int, int]


def canonical_partition(labels: Iterable[Hashable]) -> Partition:
    names: dict[Hashable, int] = {}
    out: list[int] = []
    for label in labels:
        if label not in names:
            names[label] = len(names)
        out.append(names[label])
    return tuple(out)


def block_count(partition: Partition) -> int:
    return len(set(partition))


def partition_refines(fine: Partition, coarse: Partition) -> bool:
    if len(fine) != len(coarse):
        return False
    image: dict[int, int] = {}
    for f, c in zip(fine, coarse):
        old = image.setdefault(f, c)
        if old != c:
            return False
    return True


def operation_respects_partition(partition: Partition, operation: Endomap) -> bool:
    if len(partition) != len(operation):
        raise ValueError("partition / operation size mismatch")
    image: dict[int, int] = {}
    for state, block in enumerate(partition):
        target = partition[operation[state]]
        old = image.setdefault(block, target)
        if old != target:
            return False
    return True


def stable_partition(partition: Partition, operations: Sequence[Endomap]) -> bool:
    return all(operation_respects_partition(partition, op) for op in operations)


def repair_step(partition: Partition, operations: Sequence[Endomap]) -> Partition:
    size = len(partition)
    if any(len(op) != size for op in operations):
        raise ValueError("operation size mismatch")
    return canonical_partition(
        (partition[state], *(partition[op[state]] for op in operations))
        for state in range(size)
    )


def repair_partition(partition: Partition, operations: Sequence[Endomap]) -> Partition:
    current = canonical_partition(partition)
    while True:
        nxt = repair_step(current, operations)
        if nxt == current:
            return current
        current = nxt


def quotient_block_map(fine: Partition, coarse: Partition) -> tuple[int, ...]:
    if not partition_refines(fine, coarse):
        raise ValueError("fine partition must refine coarse partition")
    count = block_count(fine)
    result = [-1] * count
    for state, fblock in enumerate(fine):
        result[fblock] = coarse[state]
    if any(value < 0 for value in result):
        raise AssertionError("noncanonical or missing fine block")
    return tuple(result)


def quotient_transition_graph(
    partition: Partition, operations: Sequence[Endomap]
) -> tuple[int, frozenset[Edge]]:
    partition = canonical_partition(partition)
    if not stable_partition(partition, operations):
        raise ValueError("partition is not stable under operations")
    edges: set[Edge] = set()
    for state, source in enumerate(partition):
        for op in operations:
            target = partition[op[state]]
            if source != target:
                edges.add((source, target))
    return block_count(partition), frozenset(edges)


def transitive_closure(vertex_count: int, edges: Iterable[Edge]) -> frozenset[Edge]:
    reach = [set() for _ in range(vertex_count)]
    for source, target in edges:
        if source != target:
            reach[source].add(target)
    for pivot in range(vertex_count):
        for source in range(vertex_count):
            if pivot in reach[source]:
                reach[source].update(reach[pivot])
    return frozenset(
        (source, target)
        for source in range(vertex_count)
        for target in reach[source]
        if source != target
    )


def reachable_within(
    vertex_count: int, edges: Iterable[Edge], source: int, target: int, depth: int
) -> bool:
    if source == target:
        return True
    adjacency = [[] for _ in range(vertex_count)]
    for left, right in edges:
        if left != right:
            adjacency[left].append(right)
    frontier = {source}
    seen = {source}
    for _ in range(depth):
        nxt: set[int] = set()
        for node in frontier:
            for right in adjacency[node]:
                if right == target:
                    return True
                if right not in seen:
                    seen.add(right)
                    nxt.add(right)
        frontier = nxt
        if not frontier:
            break
    return False


def is_k_tc_spanner(
    vertex_count: int, base_edges: Iterable[Edge], spanner_edges: Iterable[Edge], k: int
) -> bool:
    if k < 1:
        raise ValueError("k must be positive")
    base_closure = transitive_closure(vertex_count, base_edges)
    spanner = frozenset(edge for edge in spanner_edges if edge[0] != edge[1])
    if not spanner.issubset(base_closure):
        return False
    if transitive_closure(vertex_count, spanner) != base_closure:
        return False
    return all(
        reachable_within(vertex_count, spanner, source, target, k)
        for source, target in base_closure
    )


def project_edges(
    edges: Iterable[Edge], fine_to_coarse: Sequence[int]
) -> frozenset[Edge]:
    return frozenset(
        (fine_to_coarse[source], fine_to_coarse[target])
        for source, target in edges
        if fine_to_coarse[source] != fine_to_coarse[target]
    )


def project_tc_spanner(
    operations: Sequence[Endomap],
    fine: Partition,
    coarse: Partition,
    fine_spanner: Iterable[Edge],
    k: int,
) -> frozenset[Edge]:
    if not stable_partition(fine, operations) or not stable_partition(coarse, operations):
        raise ValueError("both partitions must be operation-stable")
    block_map = quotient_block_map(canonical_partition(fine), canonical_partition(coarse))
    fine_n, fine_graph = quotient_transition_graph(fine, operations)
    coarse_n, coarse_graph = quotient_transition_graph(coarse, operations)
    if not is_k_tc_spanner(fine_n, fine_graph, fine_spanner, k):
        raise ValueError("input is not a fine k-TC-spanner")
    projected = project_edges(fine_spanner, block_map)
    if not is_k_tc_spanner(coarse_n, coarse_graph, projected, k):
        raise AssertionError("TC-spanner projection theorem failed")
    return projected


def minimum_k_tc_spanner(
    vertex_count: int, base_edges: Iterable[Edge], k: int
) -> frozenset[Edge]:
    """Exact brute-force oracle for tiny graphs."""
    closure = tuple(sorted(transitive_closure(vertex_count, base_edges)))
    for size in range(len(closure) + 1):
        for candidate in combinations(closure, size):
            if is_k_tc_spanner(vertex_count, base_edges, candidate, k):
                return frozenset(candidate)
    raise AssertionError("transitive closure itself must be a valid 1-TC-spanner")


def all_partitions(size: int) -> tuple[Partition, ...]:
    if size < 0:
        raise ValueError("size must be nonnegative")
    if size == 0:
        return (tuple(),)
    out: list[Partition] = []
    prefix = [0]

    def rec() -> None:
        if len(prefix) == size:
            out.append(tuple(prefix))
            return
        upper = max(prefix) + 1
        for value in range(upper + 1):
            prefix.append(value)
            rec()
            prefix.pop()

    rec()
    return tuple(out)


def comparable_pair_count_for_box(exponents: Sequence[int]) -> int:
    """Number of reflexive comparable pairs in product_p [0,alpha_p]."""
    result = 1
    for alpha in exponents:
        if alpha < 0:
            raise ValueError("exponents must be nonnegative")
        result *= (alpha + 1) * (alpha + 2) // 2
    return result


def state_count_for_box(exponents: Sequence[int]) -> int:
    result = 1
    for alpha in exponents:
        result *= alpha + 1
    return result


def cap_shift_semantic_count(exponents: Sequence[int]) -> int:
    """Same interval count: product_p binom(alpha_p+2,2)."""
    return comparable_pair_count_for_box(exponents)
