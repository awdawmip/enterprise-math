"""Derive A_p geometry from a minimal conserved LEGO-transfer law.

Primitive state change is not chosen from a root-system catalogue. Start with N
integer relation slots and one indivisible unit. A primitive conservative move
transfers exactly one unit from one donor slot to one distinct receiver slot. Its
displacement is therefore e_receiver-e_donor. Under full slot-exchange symmetry
all ordered pairs occur, the generated difference lattice is exactly the zero-sum
lattice A_(N-1), and shortest primitive-operation count gives the A_p word metric.

At p=3 a pure-integer change of coordinates identifies A3 with
D3={y in Z^3: sum(y) even}, the standard integer FCC lattice presentation. This
bridge uses exact parity division only; densest-sphere-packing is not needed to
obtain the nearest-neighbor relation graph.
"""

from __future__ import annotations

from dataclasses import dataclass

Vector = tuple[int, ...]


def primitive_transfer(slot_count: int, receiver: int, donor: int) -> Vector:
    if isinstance(slot_count, bool) or not isinstance(slot_count, int) or slot_count < 2:
        raise ValueError("slot_count must be an integer at least two")
    if any(
        isinstance(index, bool)
        or not isinstance(index, int)
        or not (0 <= index < slot_count)
        for index in (receiver, donor)
    ):
        raise ValueError("receiver and donor must be valid slot indices")
    if receiver == donor:
        raise ValueError("primitive transfer requires distinct receiver and donor")
    vector = [0] * slot_count
    vector[receiver] = 1
    vector[donor] = -1
    return tuple(vector)


def primitive_transfers(slot_count: int) -> tuple[Vector, ...]:
    return tuple(
        primitive_transfer(slot_count, receiver, donor)
        for receiver in range(slot_count)
        for donor in range(slot_count)
        if receiver != donor
    )


def is_primitive_conserved_unit_transfer(vector: Vector) -> bool:
    return (
        bool(vector)
        and sum(vector) == 0
        and vector.count(1) == 1
        and vector.count(-1) == 1
        and all(value in (-1, 0, 1) for value in vector)
    )


def zero_sum_relation_rank(slot_count: int) -> int:
    if isinstance(slot_count, bool) or not isinstance(slot_count, int) or slot_count < 1:
        raise ValueError("slot_count must be positive")
    return max(0, slot_count - 1)


def zero_sum_basis(slot_count: int) -> tuple[Vector, ...]:
    if slot_count < 2:
        return ()
    return tuple(
        primitive_transfer(slot_count, receiver=index, donor=slot_count - 1)
        for index in range(slot_count - 1)
    )


def transfer_distance(left: Vector, right: Vector) -> int:
    if len(left) != len(right) or not left:
        raise ValueError("states must have equal nonzero slot counts")
    if any(isinstance(value, bool) or not isinstance(value, int) for value in left + right):
        raise ValueError("states must be integer vectors")
    if sum(left) != sum(right):
        raise ValueError("conservative transfer requires equal total unit count")
    delta = tuple(target - source for source, target in zip(left, right))
    positive = sum(value for value in delta if value > 0)
    negative = -sum(value for value in delta if value < 0)
    if positive != negative:
        raise AssertionError("equal totals must balance deficits and surpluses")
    return positive


@dataclass(frozen=True)
class TransferStep:
    receiver: int
    donor: int


def minimum_transfer_plan(left: Vector, right: Vector) -> tuple[TransferStep, ...]:
    distance = transfer_distance(left, right)
    delta = [target - source for source, target in zip(left, right)]
    receivers = [[index, amount] for index, amount in enumerate(delta) if amount > 0]
    donors = [[index, -amount] for index, amount in enumerate(delta) if amount < 0]
    plan = []
    receiver_index = 0
    donor_index = 0
    while receiver_index < len(receivers):
        receiver, need = receivers[receiver_index]
        donor, supply = donors[donor_index]
        moved = min(need, supply)
        plan.extend(TransferStep(receiver, donor) for _ in range(moved))
        receivers[receiver_index][1] -= moved
        donors[donor_index][1] -= moved
        if receivers[receiver_index][1] == 0:
            receiver_index += 1
        if donors[donor_index][1] == 0:
            donor_index += 1
    if len(plan) != distance:
        raise AssertionError("constructed plan must attain the transfer lower bound")
    return tuple(plan)


def apply_transfer_plan(state: Vector, plan: tuple[TransferStep, ...]) -> Vector:
    values = list(state)
    for step in plan:
        values[step.donor] -= 1
        values[step.receiver] += 1
    return tuple(values)


def a_flag_extension_count(p: int, flag_size: int) -> int:
    if isinstance(p, bool) or not isinstance(p, int) or p < 1:
        raise ValueError("p must be positive")
    if (
        isinstance(flag_size, bool)
        or not isinstance(flag_size, int)
        or not (1 <= flag_size <= p)
    ):
        raise ValueError("flag_size must lie in 1..p")
    if flag_size == 1:
        return 2 * (p - 1)
    return p - flag_size


def a_full_rank_flag_law(p: int) -> tuple[int, ...]:
    return tuple(a_flag_extension_count(p, size) for size in range(1, p + 1))


def d_triangle_split_extension_counts(rank: int) -> tuple[int, ...]:
    if isinstance(rank, bool) or not isinstance(rank, int) or rank < 5:
        raise ValueError("rank must be at least five")
    return (0, 2 * (rank - 4))


def a3_to_d3_fcc(state: Vector) -> Vector:
    """Integer bijection A3 -> D3, where D3 is the integer FCC presentation."""
    if len(state) != 4 or any(isinstance(value, bool) or not isinstance(value, int) for value in state):
        raise ValueError("A3 state must be a four-coordinate integer vector")
    if sum(state) != 0:
        raise ValueError("A3 state must have zero total")
    a, b, c, _ = state
    return (a + b, a + c, b + c)


def d3_fcc_to_a3(state: Vector) -> Vector:
    if len(state) != 3 or any(isinstance(value, bool) or not isinstance(value, int) for value in state):
        raise ValueError("D3/FCC state must be a three-coordinate integer vector")
    u, v, w = state
    if (u + v + w) % 2 != 0:
        raise ValueError("D3/FCC state must have even coordinate sum")
    numerators = (u + v - w, u + w - v, v + w - u)
    if any(value % 2 != 0 for value in numerators):
        raise AssertionError("D3 parity condition must make inverse divisions exact")
    a, b, c = (value // 2 for value in numerators)
    d = -(a + b + c)
    return (a, b, c, d)


def is_d3_fcc_state(state: Vector) -> bool:
    return (
        len(state) == 3
        and all(not isinstance(value, bool) and isinstance(value, int) for value in state)
        and sum(state) % 2 == 0
    )


def a3_primitive_images() -> tuple[Vector, ...]:
    return tuple(a3_to_d3_fcc(root) for root in primitive_transfers(4))
