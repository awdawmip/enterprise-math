"""A_p partition contraction and surviving response probes are the same quotient.

In complete anonymous transfer geometry K_N, contracting an independent forest
partitions the N slots into k coarse components.  The primal quotient is the
complete transfer geometry K_k / relation lattice A_(k-1).  On the dual side,
unit-response probes must be constant inside every coarse block.

A primitive-response/Voronoi extreme of A_(N-1) is a nontrivial oriented slot
cut S|S^c.  It survives the partition quotient iff S is a union of whole coarse
blocks.  Therefore the contracted response cell has exactly 2^k-2 extreme cut
probes, precisely the A_(k-1) response cell.

Thus dimension contraction deletes exactly those unit-resolution probes that try
to distinguish slots already identified by the coarse partition.
"""

from __future__ import annotations

from itertools import combinations

Partition = tuple[tuple[int, ...], ...]
Subset = tuple[int, ...]


def canonical_partition(blocks: Partition) -> Partition:
    if not blocks:
        raise ValueError("partition must contain at least one block")
    normalized = tuple(tuple(sorted(set(block))) for block in blocks)
    if any(not block for block in normalized):
        raise ValueError("partition blocks must be nonempty")
    flattened = [item for block in normalized for item in block]
    if len(flattened) != len(set(flattened)):
        raise ValueError("partition blocks must be disjoint")
    if set(flattened) != set(range(len(flattened))):
        raise ValueError("partition must cover slots 0..N-1 exactly")
    return tuple(sorted(normalized))


def coarse_block_count(partition: Partition) -> int:
    return len(canonical_partition(partition))


def relation_rank_after_partition(partition: Partition) -> int:
    return coarse_block_count(partition) - 1


def relation_rank_lost_by_partition(partition: Partition) -> int:
    blocks = canonical_partition(partition)
    slot_count = sum(len(block) for block in blocks)
    return slot_count - len(blocks)


def subset_is_union_of_blocks(subset: Subset, partition: Partition) -> bool:
    blocks = canonical_partition(partition)
    chosen = set(subset)
    slot_count = sum(len(block) for block in blocks)
    if not chosen or len(chosen) == slot_count or not chosen <= set(range(slot_count)):
        return False
    return all(set(block) <= chosen or set(block).isdisjoint(chosen) for block in blocks)


def surviving_cut_subsets(partition: Partition) -> tuple[Subset, ...]:
    blocks = canonical_partition(partition)
    slot_count = sum(len(block) for block in blocks)
    survivors = []
    for size in range(1, slot_count):
        for subset in combinations(range(slot_count), size):
            if subset_is_union_of_blocks(subset, blocks):
                survivors.append(subset)
    return tuple(survivors)


def surviving_extreme_probe_count(partition: Partition) -> int:
    return len(surviving_cut_subsets(partition))


def expected_surviving_probe_count(partition: Partition) -> int:
    blocks = canonical_partition(partition)
    return 2 ** len(blocks) - 2


def cut_to_coarse_subset(subset: Subset, partition: Partition) -> Subset:
    blocks = canonical_partition(partition)
    if not subset_is_union_of_blocks(subset, blocks):
        raise ValueError("cut does not descend through the partition")
    chosen = set(subset)
    return tuple(index for index, block in enumerate(blocks) if set(block) <= chosen)


def coarse_subset_to_cut(coarse_subset: Subset, partition: Partition) -> Subset:
    blocks = canonical_partition(partition)
    chosen_blocks = set(coarse_subset)
    if not chosen_blocks or len(chosen_blocks) == len(blocks):
        raise ValueError("coarse subset must be nonempty and proper")
    if not chosen_blocks <= set(range(len(blocks))):
        raise ValueError("coarse block index outside partition")
    return tuple(sorted(item for index in chosen_blocks for item in blocks[index]))


def cut_probe_bijection_holds(partition: Partition) -> bool:
    blocks = canonical_partition(partition)
    survivors = surviving_cut_subsets(blocks)
    coarse = []
    for size in range(1, len(blocks)):
        coarse.extend(combinations(range(len(blocks)), size))
    images = {cut_to_coarse_subset(subset, blocks) for subset in survivors}
    return images == set(coarse) and len(images) == len(survivors)


def probe_loss_count(partition: Partition) -> int:
    blocks = canonical_partition(partition)
    slot_count = sum(len(block) for block in blocks)
    return (2 ** slot_count - 2) - expected_surviving_probe_count(blocks)


def one_dimension_contraction_probe_loss(coarse_block_count_before: int) -> int:
    """When k coarse blocks become k-1, exactly 2^(k-1) extreme cut probes disappear."""
    if (
        isinstance(coarse_block_count_before, bool)
        or not isinstance(coarse_block_count_before, int)
        or coarse_block_count_before < 2
    ):
        raise ValueError("coarse_block_count_before must be at least two")
    k = coarse_block_count_before
    return (2 ** k - 2) - (2 ** (k - 1) - 2)
