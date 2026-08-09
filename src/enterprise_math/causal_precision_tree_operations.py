"""Exact count of zero-semantic-grade endomaps from a nested precision tree.

Compress a finite future-budget tower to its distinct nested partitions.  A raw
endomap has semantic grade zero exactly when it preserves every partition in the
tower.  Such maps can be counted recursively without enumerating raw maps.

For source/target blocks A,B at the same tree level, let N(A->B) count maps from
A into B preserving all deeper splits.  At terminal blocks,

    N(A->B)=|B|^|A|.

If A_i are the next-level children of A and B_j the children of B,

    N(A->B)=product_i sum_j N(A_i->B_j).

At the top level, each source root independently chooses a target root, so the
total is product_A sum_B N(A->B).

For a one-level tower this reduces to the ordinary Safe(E) count.  For a full
future tower it counts exactly the semantic-grade-zero dynamics.
"""

from __future__ import annotations

from functools import lru_cache
from typing import Hashable

from .causal_operation_language import Partition, same_partition

State = Hashable
Block = frozenset[State]


def compress_partition_tower(
    states: tuple[State, ...],
    partitions: tuple[Partition, ...],
) -> tuple[Partition, ...]:
    if not partitions:
        raise ValueError("partitions must be non-empty")
    if any(set(partition) != set(states) for partition in partitions):
        raise ValueError("every partition must cover the same state set")
    result = [partitions[0]]
    for partition in partitions[1:]:
        if not same_partition(result[-1], partition):
            result.append(partition)
    return tuple(result)


def partition_blocks(states: tuple[State, ...], partition: Partition) -> tuple[Block, ...]:
    grouped: dict[int, set[State]] = {}
    for state in states:
        grouped.setdefault(partition[state], set()).add(state)
    return tuple(
        frozenset(grouped[class_id])
        for class_id in sorted(grouped)
    )


def precision_tree_levels(
    states: tuple[State, ...],
    partitions: tuple[Partition, ...],
) -> tuple[tuple[Block, ...], ...]:
    compressed = compress_partition_tower(states, partitions)
    levels = tuple(partition_blocks(states, partition) for partition in compressed)
    for coarse, fine in zip(levels, levels[1:]):
        if any(not any(child <= parent for parent in coarse) for child in fine):
            raise ValueError("partition tower must refine monotonically")
    return levels


def zero_grade_map_count_from_tower(
    states: tuple[State, ...],
    partitions: tuple[Partition, ...],
) -> int:
    levels = precision_tree_levels(states, partitions)

    @lru_cache(maxsize=None)
    def count_between(level: int, source: Block, target: Block) -> int:
        if level == len(levels) - 1:
            return len(target) ** len(source)
        source_children = tuple(block for block in levels[level + 1] if block <= source)
        target_children = tuple(block for block in levels[level + 1] if block <= target)
        if not source_children or not target_children:
            raise AssertionError("nested partition blocks must have next-level children")
        return _product(
            sum(count_between(level + 1, child, target_child) for target_child in target_children)
            for child in source_children
        )

    roots = levels[0]
    return _product(
        sum(count_between(0, source, target) for target in roots)
        for source in roots
    )


def _product(values) -> int:
    result = 1
    for value in values:
        result *= value
    return result


def one_level_safe_count_formula(
    states: tuple[State, ...],
    partition: Partition,
) -> int:
    blocks = partition_blocks(states, partition)
    return _product(
        sum(len(target) ** len(source) for target in blocks)
        for source in blocks
    )


def terminal_identity_tower_count(states: tuple[State, ...]) -> int:
    """Discrete-only tower: every raw map preserves equality, so count is n^n."""
    n = len(states)
    return n ** n
