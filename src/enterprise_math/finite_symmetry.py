"""Finite symmetry/orbit/equivariance calculus for Enterprise Math.

The module is intentionally representation-light: a finite group action is supplied
as a complete finite set of permutations.  It supports orbit/stabilizer analysis,
canonical-choice obstructions, equivariance checks, and exact enumeration of
finite equivariant maps from orbit representatives.

This is standard finite group-action mathematics packaged as a reusable Enterprise
Math tool.  It is especially useful for relabeling audits such as the three-axis
S3 calculations, but it contains no Enterprise-specific target table.
"""
from __future__ import annotations

from itertools import product
from collections.abc import Hashable, Mapping, Sequence
from typing import TypeVar

Element = TypeVar("Element", bound=Hashable)
Target = TypeVar("Target", bound=Hashable)
Action = Mapping[Element, Element]


def _elements(values: Sequence[Element]) -> tuple[Element, ...]:
    result = tuple(values)
    if not result:
        raise ValueError("finite action requires at least one element")
    if len(set(result)) != len(result):
        raise ValueError("elements must be distinct")
    return result


def _action_signature(elements: tuple[Element, ...], action: Action[Element]) -> tuple[Element, ...]:
    if set(action) != set(elements):
        raise ValueError("every action must be total on exactly the declared elements")
    image = tuple(action[element] for element in elements)
    if set(image) != set(elements) or len(set(image)) != len(elements):
        raise ValueError("every action must be a permutation")
    return image


def validate_finite_group_action(
    elements: Sequence[Element], actions: Mapping[Hashable, Action[Element]]
) -> tuple[Element, ...]:
    """Validate that the supplied permutation image is a finite group.

    Non-faithful duplicate group elements are intentionally quotient out: callers
    should supply the distinct permutation image of the action.  Closure and an
    identity permutation are checked exactly.
    """
    elems = _elements(elements)
    if not actions:
        raise ValueError("at least one action is required")
    signatures = {}
    for name, action in actions.items():
        signature = _action_signature(elems, action)
        if signature in signatures:
            raise ValueError(
                f"duplicate permutation actions {signatures[signature]!r} and {name!r}; "
                "supply the distinct permutation image"
            )
        signatures[signature] = name
    identity = tuple(elems)
    if identity not in signatures:
        raise ValueError("finite action set must contain the identity permutation")
    signature_set = set(signatures)
    for left in actions.values():
        for right in actions.values():
            composed = tuple(left[right[element]] for element in elems)
            if composed not in signature_set:
                raise ValueError("supplied action permutations are not closed under composition")
    return elems


def orbit(
    elements: Sequence[Element], actions: Mapping[Hashable, Action[Element]], seed: Element
) -> frozenset[Element]:
    elems = validate_finite_group_action(elements, actions)
    if seed not in elems:
        raise ValueError("seed is outside the action set")
    return frozenset(action[seed] for action in actions.values())


def orbit_partition(
    elements: Sequence[Element], actions: Mapping[Hashable, Action[Element]]
) -> tuple[frozenset[Element], ...]:
    elems = validate_finite_group_action(elements, actions)
    unseen = set(elems)
    result: list[frozenset[Element]] = []
    for element in elems:
        if element not in unseen:
            continue
        current = frozenset(action[element] for action in actions.values())
        unseen.difference_update(current)
        result.append(current)
    return tuple(result)


def stabilizer(
    elements: Sequence[Element], actions: Mapping[Hashable, Action[Element]], point: Element
) -> tuple[Hashable, ...]:
    elems = validate_finite_group_action(elements, actions)
    if point not in elems:
        raise ValueError("point is outside the action set")
    return tuple(name for name, action in actions.items() if action[point] == point)


def global_fixed_points(
    elements: Sequence[Element], actions: Mapping[Hashable, Action[Element]]
) -> frozenset[Element]:
    elems = validate_finite_group_action(elements, actions)
    return frozenset(
        element for element in elems if all(action[element] == element for action in actions.values())
    )


def canonical_choice_obstruction(
    elements: Sequence[Element], actions: Mapping[Hashable, Action[Element]]
) -> bool:
    """Whether full relabeling symmetry forbids an invariant singleton choice.

    ``True`` means there is no element fixed by every supplied symmetry.  Any
    canonical single-valued choice from the bare carrier would therefore require
    additional symmetry-breaking structure.
    """
    return not global_fixed_points(elements, actions)


def is_equivariant_map(
    domain: Sequence[Element],
    codomain: Sequence[Target],
    domain_actions: Mapping[Hashable, Mapping[Element, Element]],
    codomain_actions: Mapping[Hashable, Mapping[Target, Target]],
    mapping: Mapping[Element, Target],
) -> bool:
    dom = validate_finite_group_action(domain, domain_actions)
    cod = validate_finite_group_action(codomain, codomain_actions)
    if set(domain_actions) != set(codomain_actions):
        raise ValueError("domain and codomain actions must use the same group labels")
    if set(mapping) != set(dom) or any(value not in cod for value in mapping.values()):
        raise ValueError("mapping must be total from the declared domain to codomain")
    return all(
        mapping[domain_action[x]] == codomain_actions[name][mapping[x]]
        for name, domain_action in domain_actions.items()
        for x in dom
    )


def equivariant_map_count(
    domain: Sequence[Element],
    codomain: Sequence[Target],
    domain_actions: Mapping[Hashable, Mapping[Element, Element]],
    codomain_actions: Mapping[Hashable, Mapping[Target, Target]],
) -> int:
    """Count equivariant maps via orbit representatives and stabilizer-fixed targets."""
    dom = validate_finite_group_action(domain, domain_actions)
    cod = validate_finite_group_action(codomain, codomain_actions)
    if set(domain_actions) != set(codomain_actions):
        raise ValueError("domain and codomain actions must use the same group labels")
    count = 1
    for current_orbit in orbit_partition(dom, domain_actions):
        representative = next(element for element in dom if element in current_orbit)
        stable_names = [
            name for name, action in domain_actions.items() if action[representative] == representative
        ]
        allowed = [
            value
            for value in cod
            if all(codomain_actions[name][value] == value for name in stable_names)
        ]
        count *= len(allowed)
    return count


def enumerate_equivariant_maps(
    domain: Sequence[Element],
    codomain: Sequence[Target],
    domain_actions: Mapping[Hashable, Mapping[Element, Element]],
    codomain_actions: Mapping[Hashable, Mapping[Target, Target]],
    *,
    max_maps: int = 100_000,
) -> tuple[dict[Element, Target], ...]:
    """Enumerate exact equivariant maps without brute-forcing all functions.

    Each domain orbit contributes one target seed fixed by the stabilizer of an
    orbit representative.  The seed is propagated equivariantly across the orbit.
    """
    if isinstance(max_maps, bool) or not isinstance(max_maps, int) or max_maps < 1:
        raise ValueError("max_maps must be a positive integer")
    dom = validate_finite_group_action(domain, domain_actions)
    cod = validate_finite_group_action(codomain, codomain_actions)
    if set(domain_actions) != set(codomain_actions):
        raise ValueError("domain and codomain actions must use the same group labels")

    orbit_choices: list[list[dict[Element, Target]]] = []
    for current_orbit in orbit_partition(dom, domain_actions):
        representative = next(element for element in dom if element in current_orbit)
        stable_names = [
            name for name, action in domain_actions.items() if action[representative] == representative
        ]
        allowed = [
            value
            for value in cod
            if all(codomain_actions[name][value] == value for name in stable_names)
        ]
        choices: list[dict[Element, Target]] = []
        for seed in allowed:
            local: dict[Element, Target] = {}
            for name, action in domain_actions.items():
                x = action[representative]
                y = codomain_actions[name][seed]
                if x in local and local[x] != y:
                    raise AssertionError("stabilizer-fixed seed failed equivariant propagation")
                local[x] = y
            if set(local) != set(current_orbit):
                raise AssertionError("group action did not cover the declared orbit")
            choices.append(local)
        orbit_choices.append(choices)

    total = 1
    for choices in orbit_choices:
        total *= len(choices)
    if total > max_maps:
        raise ValueError(f"equivariant map family has {total} maps; raise max_maps to enumerate")

    result: list[dict[Element, Target]] = []
    for selection in product(*orbit_choices):
        mapping: dict[Element, Target] = {}
        for local in selection:
            if set(mapping) & set(local):
                raise AssertionError("distinct domain orbits overlapped")
            mapping.update(local)
        if not is_equivariant_map(dom, cod, domain_actions, codomain_actions, mapping):
            raise AssertionError("constructed map failed equivariance")
        result.append(mapping)
    return tuple(result)
