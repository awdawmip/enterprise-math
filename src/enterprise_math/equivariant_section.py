"""Fibered equivariant-section calculus for finite permutation actions.

This module extends the T7 finite-symmetry toolbox family. It treats a declared
surjective equivariant projection ``pi:E->B`` and answers the exact section
question:

    does there exist a G-equivariant section s:B->E with pi∘s=id_B?

For each base-orbit representative b, existence is equivalent to the fiber over
b containing a point fixed by the full stabilizer G_b. The global section count
is therefore the product of these local fixed-lift counts.

The total-space action is supplied as the distinct finite permutation image of
G. The induced base action may be nonfaithful: distinct group elements can act
identically on B while acting differently on a fiber. This kernel is essential
for stabilizer obstructions and is validated label-by-label against the group
multiplication reconstructed from the total-space permutation image.

If an abstract symmetry group is infinite, callers must first prove that the
relevant total action factors through the supplied finite image. The calculus
does not decide whether a projection, symmetry group, realization, or naturality
requirement is semantically native.
"""
from __future__ import annotations

from collections.abc import Hashable, Mapping, Sequence
from itertools import product
from typing import TypeVar

from .finite_symmetry import validate_finite_group_action

Total = TypeVar("Total", bound=Hashable)
Base = TypeVar("Base", bound=Hashable)


def _validate_base_action_against_total_group(
    total_elements: tuple[Total, ...],
    total_actions: Mapping[Hashable, Mapping[Total, Total]],
    base: Sequence[Base],
    base_actions: Mapping[Hashable, Mapping[Base, Base]],
) -> tuple[Base, ...]:
    """Validate a possibly nonfaithful base representation of the same group.

    ``validate_finite_group_action`` intentionally requires a distinct
    permutation image, which is appropriate for the total-space carrier used to
    reconstruct the finite group multiplication. A quotient/base G-set may have
    a kernel, so duplicate base permutations are legal provided the labeled
    actions respect the multiplication table determined on the total space.
    """
    base_elements = tuple(base)
    if not base_elements:
        raise ValueError("finite action requires at least one element")
    if len(set(base_elements)) != len(base_elements):
        raise ValueError("elements must be distinct")
    if set(total_actions) != set(base_actions):
        raise ValueError("total and base actions must use the same group labels")

    base_set = set(base_elements)
    for action in base_actions.values():
        if set(action) != base_set:
            raise ValueError("every base action must be total on exactly the declared elements")
        image = tuple(action[element] for element in base_elements)
        if set(image) != base_set or len(set(image)) != len(base_elements):
            raise ValueError("every base action must be a permutation")

    total_signatures = {
        tuple(action[element] for element in total_elements): name
        for name, action in total_actions.items()
    }
    identity_label = total_signatures.get(tuple(total_elements))
    if identity_label is None:
        raise ValueError("total action set must contain the identity permutation")
    if any(base_actions[identity_label][element] != element for element in base_elements):
        raise ValueError("the total-space identity label must act identically on the base")

    # The total action is a distinct permutation image, so every composite has
    # one unique label. Require the base maps to realize that same multiplication
    # table; this permits a kernel without losing group-label semantics.
    for left_name, left in total_actions.items():
        for right_name, right in total_actions.items():
            composed_total = tuple(left[right[element]] for element in total_elements)
            result_name = total_signatures.get(composed_total)
            if result_name is None:
                raise ValueError("supplied total action permutations are not closed under composition")
            base_left = base_actions[left_name]
            base_right = base_actions[right_name]
            base_result = base_actions[result_name]
            if any(
                base_left[base_right[element]] != base_result[element]
                for element in base_elements
            ):
                raise ValueError("base actions do not respect the total-space group multiplication")
    return base_elements


def _orbit_partition_labeled(
    elements: tuple[Base, ...],
    actions: Mapping[Hashable, Mapping[Base, Base]],
) -> tuple[frozenset[Base], ...]:
    """Orbit partition for a validated labeled action that may have a kernel."""
    unseen = set(elements)
    result: list[frozenset[Base]] = []
    for element in elements:
        if element not in unseen:
            continue
        current = frozenset(action[element] for action in actions.values())
        unseen.difference_update(current)
        result.append(current)
    return tuple(result)


def validate_equivariant_projection(
    total: Sequence[Total],
    base: Sequence[Base],
    total_actions: Mapping[Hashable, Mapping[Total, Total]],
    base_actions: Mapping[Hashable, Mapping[Base, Base]],
    projection: Mapping[Total, Base],
) -> tuple[tuple[Total, ...], tuple[Base, ...]]:
    """Validate a surjective equivariant projection between finite G-sets."""
    total_elements = validate_finite_group_action(total, total_actions)
    base_elements = _validate_base_action_against_total_group(
        total_elements, total_actions, base, base_actions
    )
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
    for current_orbit in _orbit_partition_labeled(base_elements, base_actions):
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
