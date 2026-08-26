"""Fibered equivariant-section calculus for finite permutation actions.

This module extends the T7 finite-symmetry toolbox family.  It treats a declared
surjective equivariant projection ``pi:E->B`` and answers the exact section
question:

    does there exist a G-equivariant section s:B->E with pi∘s=id_B?

For each base-orbit representative b, existence is equivalent to the fiber over
b containing a point fixed by the full stabilizer G_b.  The global section count
is therefore the product of these local fixed-lift counts.

The module intentionally works with the *finite permutation image* of an action.
If an abstract symmetry group is infinite, callers must first prove that the
relevant action factors through the supplied finite image.  The calculus does
not decide whether a projection, symmetry group, realization, or naturality
requirement is semantically native.
"""
from __future__ import annotations

from collections.abc import Hashable, Mapping, Sequence
from itertools import product
from typing import TypeVar

from .finite_symmetry import orbit_partition, validate_finite_group_action

Total = TypeVar("Total", bound=Hashable)
Base = TypeVar("Base", bound=Hashable)


def validate_equivariant_projection(
    total: Sequence[Total],
    base: Sequence[Base],
    total_actions: Mapping[Hashable, Mapping[Total, Total]],
    base_actions: Mapping[Hashable, Mapping[Base, Base]],
    projection: Mapping[Total, Base],
) -> tuple[tuple[Total, ...], tuple[Base, ...]]:
    """Validate a surjective equivariant projection between finite G-sets."""
    total_elements = validate_finite_group_action(total, total_actions)
    base_elements = validate_finite_group_action(base, base_actions)
    if set(total_actions) != set(base_actions):
        raise ValueError("total and base actions must use the same group labels")
    if set(projection) != set(total_elements):
        raise ValueError("projection must be total on exactly the declared total space")
    if any(projection[element] not in base_elements for element in total_elements):
        raise ValueError("projection takes a value outside the declared base")
    if set(projection.values()) != set(base_elements):
        raise ValueError("projection must be surjective for a section problem")
    for name, total_action in total_actions.items():
        base_action = base_actions[name]
        for element in total_elements:
            if projection[total_action[element]] != base_action[projection[element]]:
                raise ValueError("projection is not equivariant for the supplied actions")
    return total_elements, base_elements


def stabilizer_fixed_lifts(
    total: Sequence[Total],
    base: Sequence[Base],
    total_actions: Mapping[Hashable, Mapping[Total, Total]],
    base_actions: Mapping[Hashable, Mapping[Base, Base]],
    projection: Mapping[Total, Base],
) -> tuple[tuple[Base, tuple[Hashable, ...], tuple[Total, ...], tuple[Total, ...]], ...]:
    """Return fiber/stabilizer/fixed-lift data for one representative per base orbit.

    Each returned tuple is ``(b, stabilizer_labels, fiber, fixed_lifts)``.
    ``fixed_lifts`` consists of the points of ``fiber`` fixed by every element of
    the stabilizer of ``b``.
    """
    total_elements, base_elements = validate_equivariant_projection(
        total, base, total_actions, base_actions, projection
    )
    result = []
    for current_orbit in orbit_partition(base_elements, base_actions):
        representative = next(value for value in base_elements if value in current_orbit)
        stabilizer_labels = tuple(
            name for name, action in base_actions.items() if action[representative] == representative
        )
        fiber = tuple(
            element for element in total_elements if projection[element] == representative
        )
        fixed_lifts = tuple(
            element
            for element in fiber
            if all(total_actions[name][element] == element for name in stabilizer_labels)
        )
        result.append((representative, stabilizer_labels, fiber, fixed_lifts))
    return tuple(result)


def equivariant_section_obstructions(
    total: Sequence[Total],
    base: Sequence[Base],
    total_actions: Mapping[Hashable, Mapping[Total, Total]],
    base_actions: Mapping[Hashable, Mapping[Base, Base]],
    projection: Mapping[Total, Base],
) -> tuple[tuple[Base, tuple[Hashable, ...], tuple[Total, ...]], ...]:
    """Return local no-section certificates ``(base_point, stabilizer, fiber)``."""
    return tuple(
        (representative, stabilizer_labels, fiber)
        for representative, stabilizer_labels, fiber, fixed_lifts in stabilizer_fixed_lifts(
            total, base, total_actions, base_actions, projection
        )
        if not fixed_lifts
    )


def equivariant_section_count(
    total: Sequence[Total],
    base: Sequence[Base],
    total_actions: Mapping[Hashable, Mapping[Total, Total]],
    base_actions: Mapping[Hashable, Mapping[Base, Base]],
    projection: Mapping[Total, Base],
) -> int:
    """Count exact equivariant sections by stabilizer-fixed fiber choices."""
    count = 1
    for _, _, _, fixed_lifts in stabilizer_fixed_lifts(
        total, base, total_actions, base_actions, projection
    ):
        count *= len(fixed_lifts)
    return count


def enumerate_equivariant_sections(
    total: Sequence[Total],
    base: Sequence[Base],
    total_actions: Mapping[Hashable, Mapping[Total, Total]],
    base_actions: Mapping[Hashable, Mapping[Base, Base]],
    projection: Mapping[Total, Base],
    *,
    max_sections: int = 100_000,
) -> tuple[dict[Base, Total], ...]:
    """Enumerate exact equivariant sections without brute-forcing all maps."""
    if isinstance(max_sections, bool) or not isinstance(max_sections, int) or max_sections < 1:
        raise ValueError("max_sections must be a positive integer")
    validate_equivariant_projection(total, base, total_actions, base_actions, projection)
    local_choices: list[list[dict[Base, Total]]] = []
    for representative, _, _, fixed_lifts in stabilizer_fixed_lifts(
        total, base, total_actions, base_actions, projection
    ):
        choices = []
        for seed in fixed_lifts:
            local: dict[Base, Total] = {}
            for name, base_action in base_actions.items():
                target_base = base_action[representative]
                target_total = total_actions[name][seed]
                if target_base in local and local[target_base] != target_total:
                    raise AssertionError("stabilizer-fixed lift failed equivariant propagation")
                local[target_base] = target_total
            choices.append(local)
        local_choices.append(choices)

    total_count = 1
    for choices in local_choices:
        total_count *= len(choices)
    if total_count > max_sections:
        raise ValueError(
            f"equivariant section family has {total_count} sections; "
            "raise max_sections to enumerate"
        )

    result: list[dict[Base, Total]] = []
    for selection in product(*local_choices):
        section: dict[Base, Total] = {}
        for local in selection:
            if set(section) & set(local):
                raise AssertionError("distinct base orbits overlapped")
            section.update(local)
        if any(projection[lift] != base_point for base_point, lift in section.items()):
            raise AssertionError("constructed map is not a section")
        for name, base_action in base_actions.items():
            total_action = total_actions[name]
            for base_point, lift in section.items():
                if section[base_action[base_point]] != total_action[lift]:
                    raise AssertionError("constructed section failed equivariance")
        result.append(section)
    return tuple(result)
