"""Derive A_p geometry from a minimal conserved LEGO transfer grammar.

Start with N equivalent integer slots and conserve their total.  The primitive
causal operation moves exactly one unit from donor j to receiver i:

    T_(i<-j)(x) = x + e_i - e_j,  i!=j.

No root system or Euclidean geometry is assumed.  The displacement vectors are
exactly the traditional A_(N-1) roots as a shadow of this grammar.  They generate
the full zero-sum integer state lattice.  Minimum transfer count between states
is the positive mass deficit/excess total, equal to one half of the L1 difference.

Two primitive transfers are first-link related exactly when their displacement
difference is another primitive transfer.  This happens precisely when they
share the same receiver or the same donor.  Hence the local direction link and
the K_(N-2) disjoint K_(N-2) edge context receive a direct causal interpretation
as receiver and donor channels.
"""

from __future__ import annotations

from collections import Counter

State = tuple[int, ...]
Transfer = tuple[int, int]  # (receiver, donor)
Vector = tuple[int, ...]


def require_slot_count(slot_count: int) -> None:
    if isinstance(slot_count, bool) or not isinstance(slot_count, int) or slot_count < 2:
        raise ValueError("slot_count must be an integer at least two")


def primitive_transfer_vector(slot_count: int, receiver: int, donor: int) -> Vector:
    require_slot_count(slot_count)
    if not (0 <= receiver < slot_count and 0 <= donor < slot_count) or receiver == donor:
        raise ValueError("receiver and donor must be distinct valid slots")
    vector = [0] * slot_count
    vector[receiver] = 1
    vector[donor] = -1
    return tuple(vector)


def primitive_transfers(slot_count: int) -> tuple[Transfer, ...]:
    require_slot_count(slot_count)
    return tuple(
        (receiver, donor)
        for receiver in range(slot_count)
        for donor in range(slot_count)
        if receiver != donor
    )


def primitive_transfer_vectors(slot_count: int) -> tuple[Vector, ...]:
    return tuple(
        primitive_transfer_vector(slot_count, receiver, donor)
        for receiver, donor in primitive_transfers(slot_count)
    )


def is_conserved_state(state: State) -> bool:
    return isinstance(state, tuple) and len(state) >= 2 and all(
        isinstance(value, int) and not isinstance(value, bool) for value in state
    )


def apply_transfer(state: State, transfer: Transfer) -> State:
    if not is_conserved_state(state):
        raise ValueError("state must be an integer slot tuple")
    receiver, donor = transfer
    move = primitive_transfer_vector(len(state), receiver, donor)
    result = tuple(value + delta for value, delta in zip(state, move))
    if sum(result) != sum(state):
        raise AssertionError("primitive transfer must conserve total")
    return result


def transfer_distance(left: State, right: State) -> int:
    if not is_conserved_state(left) or not is_conserved_state(right) or len(left) != len(right):
        raise ValueError("states must be same-length integer tuples")
    if sum(left) != sum(right):
        raise ValueError("states with different conserved totals are not transfer-connected")
    delta = tuple(target - source for source, target in zip(left, right))
    positive = sum(value for value in delta if value > 0)
    negative = -sum(value for value in delta if value < 0)
    if positive != negative:
        raise AssertionError("equal-total displacement must balance positive and negative mass")
    return positive


def transfer_distance_half_l1(left: State, right: State) -> int:
    l1 = sum(abs(a - b) for a, b in zip(left, right))
    if l1 % 2 != 0:
        raise AssertionError("equal-total integer states have even L1 difference")
    return l1 // 2


def canonical_transfer_decomposition(left: State, right: State) -> tuple[Transfer, ...]:
    """Construct exactly transfer_distance(left,right) unit moves from left to right."""
    if sum(left) != sum(right) or len(left) != len(right):
        raise ValueError("states must have same length and conserved total")
    delta = [target - source for source, target in zip(left, right)]
    receivers = [[index, value] for index, value in enumerate(delta) if value > 0]
    donors = [[index, -value] for index, value in enumerate(delta) if value < 0]
    moves: list[Transfer] = []
    receiver_index = 0
    donor_index = 0
    while receiver_index < len(receivers) and donor_index < len(donors):
        receiver, need = receivers[receiver_index]
        donor, supply = donors[donor_index]
        amount = min(need, supply)
        moves.extend((receiver, donor) for _ in range(amount))
        receivers[receiver_index][1] -= amount
        donors[donor_index][1] -= amount
        if receivers[receiver_index][1] == 0:
            receiver_index += 1
        if donors[donor_index][1] == 0:
            donor_index += 1
    if len(moves) != transfer_distance(left, right):
        raise AssertionError("canonical decomposition must attain minimum transfer count")
    return tuple(moves)


def transfer_relation_type(left: Transfer, right: Transfer) -> str | None:
    if left == right:
        return None
    if left[0] == right[0]:
        return "same_receiver"
    if left[1] == right[1]:
        return "same_donor"
    return None


def transfer_link_neighbors(slot_count: int, transfer: Transfer) -> tuple[Transfer, ...]:
    if transfer not in primitive_transfers(slot_count):
        raise ValueError("transfer must be primitive")
    return tuple(
        other
        for other in primitive_transfers(slot_count)
        if transfer_relation_type(transfer, other) is not None
    )


def transfer_link_degree(slot_count: int) -> int:
    require_slot_count(slot_count)
    return 2 * (slot_count - 2)


def transfer_edge_context_channel_sizes(slot_count: int, transfer: Transfer) -> tuple[int, int]:
    neighbors = transfer_link_neighbors(slot_count, transfer)
    counts = Counter(transfer_relation_type(transfer, neighbor) for neighbor in neighbors)
    return counts["same_receiver"], counts["same_donor"]


def causal_dimension_from_conserved_slots(slot_count: int) -> int:
    require_slot_count(slot_count)
    return slot_count - 1


def a_p_shadow_identity(slot_count: int) -> bool:
    """Verify the generated primitive vectors are exactly all e_i-e_j roots."""
    generated = set(primitive_transfer_vectors(slot_count))
    expected = {
        tuple(
            1 if index == receiver else -1 if index == donor else 0
            for index in range(slot_count)
        )
        for receiver in range(slot_count)
        for donor in range(slot_count)
        if receiver != donor
    }
    return generated == expected and len(generated) == slot_count * (slot_count - 1)
