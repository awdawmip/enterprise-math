"""Causal propagation of continuation-type inventories.

If a causal operation respects disjoint LEGO union of witnesses, one witness of
continuation type tau has a fixed output inventory P_tau.  A current inventory
n_tau then evolves by exact integer accumulation

    n'_upsilon = sum_tau n_tau * P_tau(upsilon).

Ordinary nonnegative-integer matrix evolution is a coordinate shadow of this
single-witness profile propagation.  The rule is not valid for operations whose
output contains cross-witness interaction effects.
"""

from __future__ import annotations

from collections import defaultdict
from typing import Hashable

Type = Hashable


def propagate_inventory(
    inventory: dict[Type, int],
    single_witness_profiles: dict[Type, dict[Type, int]],
) -> dict[Type, int]:
    if not isinstance(inventory, dict):
        raise ValueError("inventory must be a dict")
    if not set(inventory) <= set(single_witness_profiles):
        raise ValueError("profiles must define every represented input type")
    result: dict[Type, int] = defaultdict(int)
    for tau, multiplicity in inventory.items():
        if isinstance(multiplicity, bool) or not isinstance(multiplicity, int) or multiplicity < 0:
            raise ValueError("inventory multiplicities must be non-negative integers")
        profile = single_witness_profiles[tau]
        for upsilon, count in profile.items():
            if isinstance(count, bool) or not isinstance(count, int) or count < 0:
                raise ValueError("profile counts must be non-negative integers")
            result[upsilon] += multiplicity * count
    return {tau: count for tau, count in result.items() if count}


def add_inventories(left: dict[Type, int], right: dict[Type, int]) -> dict[Type, int]:
    result: dict[Type, int] = defaultdict(int)
    for inventory in (left, right):
        for tau, count in inventory.items():
            if isinstance(count, bool) or not isinstance(count, int) or count < 0:
                raise ValueError("inventory counts must be non-negative integers")
            result[tau] += count
    return {tau: count for tau, count in result.items() if count}


def additive_propagation_identity(
    left: dict[Type, int],
    right: dict[Type, int],
    single_witness_profiles: dict[Type, dict[Type, int]],
) -> bool:
    """Check T(left+right)=T(left)+T(right) for the profile-generated operation."""
    combined = add_inventories(left, right)
    return propagate_inventory(combined, single_witness_profiles) == add_inventories(
        propagate_inventory(left, single_witness_profiles),
        propagate_inventory(right, single_witness_profiles),
    )


def composition_profiles(
    first: dict[Type, dict[Type, int]],
    second: dict[Type, dict[Type, int]],
) -> dict[Type, dict[Type, int]]:
    """Compose two additive profile systems without raw witness identity."""
    result: dict[Type, dict[Type, int]] = {}
    for tau, middle_inventory in first.items():
        result[tau] = propagate_inventory(middle_inventory, second)
    return result
