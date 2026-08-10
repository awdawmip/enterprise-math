"""R004 activation-aware typed generator basis tools.

Reference-only finite exact tools.  Generic set cover/hitting set, transformation
semigroup generation and algebraic closure are prior mathematics.  This module
packages them for the R004 typed Representation Compiler.
"""
from __future__ import annotations

from itertools import combinations
from typing import Any, Callable, Iterable, Sequence, Tuple

Partition = Tuple[int, ...]
UnaryOperation = Tuple[int, ...]


def normalize_partition(labels: Sequence[Any]) -> Partition:
    mapping = {}
    out = []
    for label in labels:
        if label not in mapping:
            mapping[label] = len(mapping)
        out.append(mapping[label])
    return tuple(out)


def partition_blocks(partition: Sequence[Any]) -> Tuple[Tuple[int, ...], ...]:
    p = normalize_partition(partition)
    if not p:
        return ()
    blocks = [[] for _ in range(max(p) + 1)]
    for state, block in enumerate(p):
        blocks[block].append(state)
    return tuple(tuple(block) for block in blocks)


def partition_refines(finer: Sequence[Any], coarser: Sequence[Any]) -> bool:
    p = normalize_partition(finer)
    q = normalize_partition(coarser)
    if len(p) != len(q):
        return False
    image = {}
    for a, b in zip(p, q):
        if a in image and image[a] != b:
            return False
        image[a] = b
    return True


def all_partitions(n: int) -> Tuple[Partition, ...]:
    if n < 0:
        raise ValueError("n must be nonnegative")
    if n == 0:
        return ((),)
    out = []

    def rec(prefix, largest):
        if len(prefix) == n:
            out.append(tuple(prefix))
            return
        for value in range(largest + 2):
            rec(prefix + (value,), max(largest, value))

    rec((0,), 0)
    return tuple(out)


def forbidden_coarse_partitions(initial: Sequence[Any], target: Sequence[Any]) -> Tuple[Partition, ...]:
    p0 = normalize_partition(initial)
    q = normalize_partition(target)
    if len(p0) != len(q) or not partition_refines(q, p0):
        raise ValueError("target must refine initial partition")
    return tuple(
        p
        for p in all_partitions(len(p0))
        if partition_refines(p, p0) and partition_refines(q, p) and p != q
    )


def unary_operation_stable(partition: Sequence[Any], operation: UnaryOperation) -> bool:
    p = normalize_partition(partition)
    if len(operation) != len(p) or any(y < 0 or y >= len(p) for y in operation):
        raise ValueError("invalid unary operation")
    seen = {}
    for x, source_block in enumerate(p):
        target_block = p[operation[x]]
        if source_block in seen and seen[source_block] != target_block:
            return False
        seen[source_block] = target_block
    return True


def compile_unary_operations(initial: Sequence[Any], operations: Sequence[UnaryOperation]) -> Partition:
    p = normalize_partition(initial)
    while True:
        signatures = [
            (p[x],) + tuple(p[operation[x]] for operation in operations)
            for x in range(len(p))
        ]
        q = normalize_partition(signatures)
        if q == p:
            return p
        p = q


def kill_table(
    initial: Sequence[Any],
    target: Sequence[Any],
    generators: Sequence[Any],
    stable_at: Callable[[Partition, Any], bool],
) -> Tuple[Tuple[Partition, ...], Tuple[int, ...]]:
    """Return forbidden worlds and one integer generator-kill bit mask per world."""
    worlds = forbidden_coarse_partitions(initial, target)
    masks = []
    for world in worlds:
        mask = 0
        for index, generator in enumerate(generators):
            if not stable_at(world, generator):
                mask |= 1 << index
        masks.append(mask)
    return worlds, tuple(masks)


def selection_hits_all_forbidden(selection_mask: int, kill_masks: Sequence[int]) -> bool:
    return all(selection_mask & mask for mask in kill_masks)


def minimum_carrier_basis_masks(generator_count: int, kill_masks: Sequence[int]) -> Tuple[int, ...]:
    if generator_count < 0:
        raise ValueError("generator_count must be nonnegative")
    for size in range(generator_count + 1):
        hits = []
        for indices in combinations(range(generator_count), size):
            mask = sum(1 << i for i in indices)
            if selection_hits_all_forbidden(mask, kill_masks):
                hits.append(mask)
        if hits:
            return tuple(hits)
    return ()


def selected_indices(mask: int, generator_count: int) -> Tuple[int, ...]:
    return tuple(i for i in range(generator_count) if mask & (1 << i))


def inclusion_minimal_private_witnesses(
    selection_mask: int,
    worlds: Sequence[Partition],
    kill_masks: Sequence[int],
    generator_count: int,
) -> Tuple[Tuple[int, Partition], ...]:
    """For each selected generator, find a forbidden world uniquely killed inside the selection."""
    witnesses = []
    for i in selected_indices(selection_mask, generator_count):
        private = None
        bit = 1 << i
        for world, kill_mask in zip(worlds, kill_masks):
            if (kill_mask & selection_mask) == bit:
                private = world
                break
        if private is None:
            return ()
        witnesses.append((i, private))
    return tuple(witnesses)


def maximum_generator_disjoint_forbidden_packing(
    worlds: Sequence[Partition],
    kill_masks: Sequence[int],
    generator_count: int,
) -> Tuple[Partition, ...]:
    """Exact small-instance integer lower-bound certificate.

    A packing is generator-disjoint when no generator kills two selected forbidden
    worlds.  Every carrier basis must then contain at least one distinct generator
    per packed world.
    """
    best = ()
    for size in range(len(worlds) + 1):
        for indices in combinations(range(len(worlds)), size):
            if all(
                sum(bool(kill_masks[j] & (1 << g)) for j in indices) <= 1
                for g in range(generator_count)
            ):
                best = indices
    return tuple(worlds[j] for j in best)


def quotient_unary_map(partition: Sequence[Any], operation: UnaryOperation) -> Tuple[int, ...]:
    p = normalize_partition(partition)
    if not unary_operation_stable(p, operation):
        raise ValueError("operation does not descend to this partition")
    return tuple(p[operation[block[0]]] for block in partition_blocks(p))


def _compose(left: Tuple[int, ...], right: Tuple[int, ...]) -> Tuple[int, ...]:
    return tuple(left[right[i]] for i in range(len(right)))


def transformation_monoid_closure(
    generators: Sequence[Tuple[int, ...]], carrier_size: int
) -> frozenset[Tuple[int, ...]]:
    identity = tuple(range(carrier_size))
    closure = {identity, *generators}
    while True:
        snapshot = tuple(closure)
        new = {_compose(left, right) for left in snapshot for right in snapshot}
        if new <= closure:
            return frozenset(closure)
        closure.update(new)


def quotient_operation_reconstructible(
    target: Sequence[Any],
    retained: Sequence[UnaryOperation],
    omitted: UnaryOperation,
) -> bool:
    q = normalize_partition(target)
    retained_maps = tuple(quotient_unary_map(q, op) for op in retained)
    omitted_map = quotient_unary_map(q, omitted)
    return omitted_map in transformation_monoid_closure(retained_maps, len(partition_blocks(q)))


def minimum_semantic_operation_basis_masks(
    target: Sequence[Any], operations: Sequence[UnaryOperation]
) -> Tuple[int, ...]:
    """Minimum subsets whose descended unary transformation monoid reconstructs all requested operations.

    Identity is treated as a free structural term.  The returned minimum semantic
    bases are therefore execution/reconstruction bases, not merely carrier bases.
    """
    q = normalize_partition(target)
    quotient_maps = tuple(quotient_unary_map(q, op) for op in operations)
    k = len(partition_blocks(q))
    for size in range(len(operations) + 1):
        answers = []
        for indices in combinations(range(len(operations)), size):
            closure = transformation_monoid_closure(tuple(quotient_maps[i] for i in indices), k)
            if all(item in closure for item in quotient_maps):
                answers.append(sum(1 << i for i in indices))
        if answers:
            return tuple(answers)
    return ()
