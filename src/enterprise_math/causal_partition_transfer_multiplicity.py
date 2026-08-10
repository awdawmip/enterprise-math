"""Partition contraction preserves unit transfer value and creates witness multiplicity.

Start from the complete anonymous transfer law on N fine slots and partition slots
into k coarse blocks of capacities m_alpha.  Block totals are the coarse state.

A fine directed primitive transfer from donor block beta to receiver block alpha
always induces the same coarse displacement e_alpha-e_beta.  Its coarse causal
cost remains one unit; there are exactly m_alpha*m_beta fine endpoint choices that
realize it.  Fine transfers whose two endpoints lie in one coarse block induce
the coarse identity and become hidden primitive witnesses.

Thus coarse kinematics is again complete A_(k-1) transfer geometry, independent
of capacities.  Capacities survive in witness multiplicities rather than changing
the value of the primitive unit.  This is a direct finite bridge to P011 collapse
spectra on operations.
"""

from __future__ import annotations

from collections import Counter

Partition = tuple[tuple[int, ...], ...]
Move = tuple[int, int]  # (receiver, donor)


def canonical_partition(blocks: Partition) -> Partition:
    normalized = tuple(tuple(sorted(set(block))) for block in blocks)
    if not normalized or any(not block for block in normalized):
        raise ValueError("partition must contain nonempty blocks")
    flat = [slot for block in normalized for slot in block]
    if len(flat) != len(set(flat)) or set(flat) != set(range(len(flat))):
        raise ValueError("partition must cover slots 0..N-1 exactly once")
    return tuple(sorted(normalized))


def block_capacities(partition: Partition) -> tuple[int, ...]:
    return tuple(len(block) for block in canonical_partition(partition))


def slot_to_block(partition: Partition) -> tuple[int, ...]:
    blocks = canonical_partition(partition)
    result = [0] * sum(len(block) for block in blocks)
    for block_index, block in enumerate(blocks):
        for slot in block:
            result[slot] = block_index
    return tuple(result)


def fine_primitive_moves(partition: Partition) -> tuple[Move, ...]:
    slot_count = sum(block_capacities(partition))
    return tuple(
        (receiver, donor)
        for receiver in range(slot_count)
        for donor in range(slot_count)
        if receiver != donor
    )


def coarse_image_of_fine_move(move: Move, partition: Partition) -> Move | None:
    mapping = slot_to_block(partition)
    receiver, donor = move
    coarse_receiver = mapping[receiver]
    coarse_donor = mapping[donor]
    if coarse_receiver == coarse_donor:
        return None
    return coarse_receiver, coarse_donor


def coarse_move_witness_multiplicity(
    receiver_block: int,
    donor_block: int,
    partition: Partition,
) -> int:
    capacities = block_capacities(partition)
    if receiver_block == donor_block:
        raise ValueError("coarse primitive transfer requires distinct blocks")
    if any(index < 0 or index >= len(capacities) for index in (receiver_block, donor_block)):
        raise ValueError("block index outside partition")
    return capacities[receiver_block] * capacities[donor_block]


def hidden_identity_move_count(partition: Partition) -> int:
    """Oriented fine primitive transfers internal to coarse blocks."""
    return sum(capacity * (capacity - 1) for capacity in block_capacities(partition))


def coarse_move_multiplicity_table(partition: Partition) -> dict[Move | None, int]:
    histogram = Counter(
        coarse_image_of_fine_move(move, partition)
        for move in fine_primitive_moves(partition)
    )
    return dict(histogram)


def expected_coarse_move_multiplicity_table(partition: Partition) -> dict[Move | None, int]:
    capacities = block_capacities(partition)
    table: dict[Move | None, int] = {None: hidden_identity_move_count(partition)}
    for receiver in range(len(capacities)):
        for donor in range(len(capacities)):
            if receiver == donor:
                continue
            table[(receiver, donor)] = capacities[receiver] * capacities[donor]
    return table


def primitive_operation_projection_identity(partition: Partition) -> bool:
    return coarse_move_multiplicity_table(partition) == expected_coarse_move_multiplicity_table(partition)


def coarse_primitive_direction_count(partition: Partition) -> int:
    block_count = len(block_capacities(partition))
    return block_count * (block_count - 1)


def coarse_relation_rank(partition: Partition) -> int:
    return max(0, len(block_capacities(partition)) - 1)
