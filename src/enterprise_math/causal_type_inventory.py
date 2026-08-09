"""Continuation-type inventory as the canonical identity-free finite witness state.

For witnesses already quotiented by complete continuation signature, the exact
identity-free state is the multiplicity of each continuation type.  Two finite
witness families have the same inventory iff they are related by a type-
preserving bijection.  Therefore every future observation invariant under
renaming witnesses inside one continuation type factors through this inventory.

The usual free-commutative-monoid / counting-vector language is a mathematical
shadow of this causal quotient, not the primitive ontology.
"""

from __future__ import annotations

from collections import Counter
from typing import Hashable

Witness = Hashable
ContinuationType = Hashable


def type_inventory(
    witness_to_type: dict[Witness, ContinuationType],
) -> dict[ContinuationType, int]:
    if not isinstance(witness_to_type, dict):
        raise ValueError("witness_to_type must be a dict")
    counts: Counter[ContinuationType] = Counter()
    for witness, tau in witness_to_type.items():
        try:
            hash(witness)
            hash(tau)
        except TypeError as error:
            raise ValueError("witness and continuation type must be hashable") from error
        counts[tau] += 1
    return dict(counts)


def same_identity_free_state(
    left: dict[Witness, ContinuationType],
    right: dict[Witness, ContinuationType],
) -> bool:
    """Equality modulo arbitrary renaming within continuation types."""
    return type_inventory(left) == type_inventory(right)


def inventory_size(inventory: dict[ContinuationType, int]) -> int:
    if any(isinstance(count, bool) or not isinstance(count, int) or count < 0 for count in inventory.values()):
        raise ValueError("inventory counts must be non-negative integers")
    return sum(inventory.values())


def combine_inventories(
    left: dict[ContinuationType, int],
    right: dict[ContinuationType, int],
) -> dict[ContinuationType, int]:
    """Disjointly combine two witness families after identity has been forgotten."""
    result: Counter[ContinuationType] = Counter()
    for inventory in (left, right):
        for tau, count in inventory.items():
            if isinstance(count, bool) or not isinstance(count, int) or count < 0:
                raise ValueError("inventory counts must be non-negative integers")
            result[tau] += count
    return {tau: count for tau, count in result.items() if count}


def additive_type_observation(
    inventory: dict[ContinuationType, int],
    type_response: dict[ContinuationType, int],
) -> int:
    """Integer additive future observation from one response per continuation type."""
    if not set(inventory) <= set(type_response):
        raise ValueError("type_response must define every represented continuation type")
    result = 0
    for tau, count in inventory.items():
        response = type_response[tau]
        if isinstance(count, bool) or not isinstance(count, int) or count < 0:
            raise ValueError("inventory counts must be non-negative integers")
        if isinstance(response, bool) or not isinstance(response, int):
            raise ValueError("type responses must be integers")
        result += count * response
    return result


def inventory_signature(inventory: dict[ContinuationType, int]) -> tuple[tuple[str, int], ...]:
    """Deterministic display-only signature, sorted by repr(type)."""
    return tuple(sorted(((repr(tau), count) for tau, count in inventory.items())))
