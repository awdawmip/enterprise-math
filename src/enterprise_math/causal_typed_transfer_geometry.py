"""Typed conservative one-unit geometry generated directly by charge labels.

Assign each slot i an integer charge-label vector q_i.  A primitive one-unit move
is e_i-e_j.  Exact conservation of all declared charges requires

    Q(e_i-e_j)=q_i-q_j=0,

so a direct transfer is allowed exactly between slots with equal charge labels.
If slots remain anonymous inside each charge class, full exchange symmetry forces
one complete transfer component K_(n_a) per label class.  The relation geometry is
a direct sum of A_(n_a-1) components and rank N-s, where s is the number of charge
classes.

Thus exact type/species marks can generate disconnected primitive kinematics
rather than merely annotate an already-fixed space.
"""

from __future__ import annotations

from collections import defaultdict

Charge = tuple[int, ...]
Edge = tuple[int, int]


def _validate_charges(charges: tuple[Charge, ...]) -> None:
    if not charges:
        raise ValueError("charges must be nonempty")
    width = len(charges[0])
    if any(len(charge) != width for charge in charges):
        raise ValueError("all charge labels must have equal dimension")
    if any(any(isinstance(value, bool) or not isinstance(value, int) for value in charge) for charge in charges):
        raise ValueError("charge labels must be integer tuples")


def charge_classes(charges: tuple[Charge, ...]) -> tuple[tuple[int, ...], ...]:
    _validate_charges(charges)
    groups: dict[Charge, list[int]] = defaultdict(list)
    for slot, charge in enumerate(charges):
        groups[charge].append(slot)
    return tuple(sorted(tuple(slots) for slots in groups.values()))


def charge_preserving_transfer_edges(charges: tuple[Charge, ...]) -> tuple[Edge, ...]:
    classes = charge_classes(charges)
    edges = []
    for block in classes:
        for index, left in enumerate(block):
            for right in block[index + 1:]:
                edges.append((left, right))
    return tuple(sorted(edges))


def primitive_transfer_preserves_charges(charges: tuple[Charge, ...], receiver: int, donor: int) -> bool:
    _validate_charges(charges)
    if receiver == donor or any(index < 0 or index >= len(charges) for index in (receiver, donor)):
        raise ValueError("receiver/donor must be distinct valid slots")
    return charges[receiver] == charges[donor]


def typed_relation_rank(charges: tuple[Charge, ...]) -> int:
    classes = charge_classes(charges)
    return sum(max(0, len(block) - 1) for block in classes)


def typed_relation_rank_closed_form(charges: tuple[Charge, ...]) -> int:
    return len(charges) - len(charge_classes(charges))


def typed_a_component_ranks(charges: tuple[Charge, ...]) -> tuple[int, ...]:
    return tuple(sorted((len(block) - 1 for block in charge_classes(charges)), reverse=True))


def charge_class_direction_counts(charges: tuple[Charge, ...]) -> tuple[int, ...]:
    """Signed primitive direction count n_a(n_a-1) in each complete type component."""
    return tuple(sorted((len(block) * (len(block) - 1) for block in charge_classes(charges)), reverse=True))


def full_anonymous_single_charge_geometry(slot_count: int, charge_dimension: int = 1) -> tuple[Charge, ...]:
    if slot_count < 1 or charge_dimension < 0:
        raise ValueError("invalid dimensions")
    label = (1,) + (0,) * max(0, charge_dimension - 1) if charge_dimension else ()
    return tuple(label for _ in range(slot_count))
