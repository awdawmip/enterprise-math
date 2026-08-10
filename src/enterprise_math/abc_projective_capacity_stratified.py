"""Complement-capacity stratification of the P025 projective tail.

If one cyclic projective term for component i is at least an integer threshold
T and j,k are its complementary components, then

    m_i >= T * (R_k C_j + R_j C_k).

Consequently

    R_i R_j <= n_i / (T C_k),
    R_i R_k <= n_i / (T C_j).

Thus, with H_i=max(C_j,C_k), one of the two pair radicals involving the
failing component is at most n_i/(T H_i) <= c/(T H_i).

This refines Stage 64, which used only H_i>=1.  At a fixed low-capacity cutoff,
Stage 51 classifies both complementary blocks into a finite core plus bounded-
exponent prime powers; below cutoff five both complements are prime powers with
exponents in {1,2,3,4}.
"""

from __future__ import annotations

from dataclasses import dataclass

from .abc_low_capacity_rigidity import (
    LowCapacityClassification,
    classify_low_capacity_integer,
)
from .abc_projective_capacity_condition import projective_capacity_condition_state
from .abc_small_derivative_block import normalized_block_capacity
from .abc_support import abc_support_state, radical


@dataclass(frozen=True)
class ActiveCapacityPairBound:
    abc: tuple[int, int, int]
    threshold: int
    cyclic_index: int
    active_component_index: int
    active_component_value: int
    complement_indices: tuple[int, int]
    complement_capacities: tuple[int, int]
    complement_capacity_max: int
    controlling_complement_index: int
    controlled_pair_indices: tuple[int, int]
    controlled_pair_values: tuple[int, int]
    controlled_pair_radical: int


@dataclass(frozen=True)
class LowCapacityActiveSlice:
    active_bound: ActiveCapacityPairBound
    cutoff: int
    complement_classifications: tuple[LowCapacityClassification, LowCapacityClassification]
    both_prime_powers_below_five: bool


def _active_component_for_cyclic_index(cyclic_index: int) -> int:
    # P025 stored cyclic ratio order is c,b,a.
    return (2, 1, 0)[cyclic_index]


def active_capacity_pair_bounds(
    a: int, b: int, c: int, threshold: int
) -> tuple[ActiveCapacityPairBound, ...]:
    """Return exact capacity-refined pair-radical bounds for every active term."""
    abc_support_state(a, b, c)
    if isinstance(threshold, bool) or not isinstance(threshold, int) or threshold < 1:
        raise ValueError("threshold must be an integer >=1")

    values = (a, b, c)
    radicals = tuple(radical(n) for n in values)
    capacities = tuple(normalized_block_capacity(n) for n in values)
    state = projective_capacity_condition_state(a, b, c)
    results: list[ActiveCapacityPairBound] = []

    for cyclic_index, ratio in enumerate(state.cyclic_weighted_defects):
        if ratio < threshold:
            continue
        active = _active_component_for_cyclic_index(cyclic_index)
        complements = tuple(index for index in range(3) if index != active)
        j, k = complements
        Cj, Ck = capacities[j], capacities[k]
        if Cj <= 0 or Ck <= 0:
            # Unit blocks have capacity zero.  Stage 71's two-complement gain is
            # a non-unit-complement statement; the unit slice remains governed
            # by the Stage-49/51 one-block formulas.
            continue

        # If Cj is larger, use the term R_k*Cj and control pair (i,k).
        # If Ck is larger, use R_j*Ck and control pair (i,j).
        if Cj >= Ck:
            controlling = j
            partner = k
            H = Cj
        else:
            controlling = k
            partner = j
            H = Ck

        pair_radical = radicals[active] * radicals[partner]
        if threshold * H * pair_radical > values[active]:
            raise AssertionError("active projective term lost complement-capacity pair bound")

        results.append(
            ActiveCapacityPairBound(
                abc=(a, b, c),
                threshold=threshold,
                cyclic_index=cyclic_index,
                active_component_index=active,
                active_component_value=values[active],
                complement_indices=complements,
                complement_capacities=(Cj, Ck),
                complement_capacity_max=H,
                controlling_complement_index=controlling,
                controlled_pair_indices=(active, partner),
                controlled_pair_values=(values[active], values[partner]),
                controlled_pair_radical=pair_radical,
            )
        )
    return tuple(results)


def low_capacity_active_slices(
    a: int, b: int, c: int, threshold: int, cutoff: int
) -> tuple[LowCapacityActiveSlice, ...]:
    """Classify active orientations whose two complement capacities are < cutoff.

    Stage 51 is applied with horizon ``cutoff-1``.  At ``cutoff=5`` both
    complements must be prime powers of exponents 1..4.
    """
    if isinstance(cutoff, bool) or not isinstance(cutoff, int) or cutoff < 2:
        raise ValueError("cutoff must be an integer >=2")
    values = (a, b, c)
    horizon = cutoff - 1
    result: list[LowCapacityActiveSlice] = []
    for bound in active_capacity_pair_bounds(a, b, c, threshold):
        if bound.complement_capacity_max >= cutoff:
            continue
        classifications = tuple(
            classify_low_capacity_integer(values[index], horizon)
            for index in bound.complement_indices
        )
        if any(item.capacity > horizon for item in classifications):
            raise AssertionError("low-capacity active slice escaped Stage-51 horizon")
        both_pp = cutoff == 5 and all(item.prime_power for item in classifications)
        if cutoff == 5 and not both_pp:
            raise AssertionError("C<5 complements must be prime powers")
        result.append(
            LowCapacityActiveSlice(
                active_bound=bound,
                cutoff=cutoff,
                complement_classifications=(classifications[0], classifications[1]),
                both_prime_powers_below_five=both_pp,
            )
        )
    return tuple(result)


def high_capacity_active_bounds(
    a: int, b: int, c: int, threshold: int, capacity_floor: int
) -> tuple[ActiveCapacityPairBound, ...]:
    """Return active terms with complement-capacity gain at least ``capacity_floor``."""
    if (
        isinstance(capacity_floor, bool)
        or not isinstance(capacity_floor, int)
        or capacity_floor < 1
    ):
        raise ValueError("capacity_floor must be a positive integer")
    return tuple(
        bound
        for bound in active_capacity_pair_bounds(a, b, c, threshold)
        if bound.complement_capacity_max >= capacity_floor
    )
