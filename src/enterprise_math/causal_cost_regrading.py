"""Exact effects of changing positive integer grades on a fixed causal language.

The unweighted future quotient depends only on which operation words exist.
Positive integer costs grade when those words become available.  If every
primitive cost is increased, transport and distinguishing costs cannot decrease,
and a fixed budget can only see a coarser future partition.

Uniform rescaling c'(g)=m*c(g) is exact: every word cost scales by m, all finite
transport/distinguishing costs scale by m, and the budget-R partition under c'
is the budget-floor(R/m) partition under c.  Thus integer cost units alter the
resolution clock but not the ultimate causal quotient.
"""

from __future__ import annotations

from typing import Hashable, Mapping

from .causal_operation_language import Generators, partition_refines
from .causal_weighted_future import (
    budget_partitions,
    distinguishing_cost,
    transport_cost,
)

State = Hashable
Observation = Hashable


def costs_dominate(
    lower: Mapping[str, int],
    upper: Mapping[str, int],
) -> bool:
    if set(lower) != set(upper):
        raise ValueError("cost maps must have identical generator labels")
    return all(upper[label] >= lower[label] for label in lower)


def finite_cost_order_preserved(
    lower_value: int | None,
    upper_value: int | None,
) -> bool:
    """Check upper>=lower with None interpreted as infinity."""
    if lower_value is None:
        return upper_value is None
    return upper_value is None or upper_value >= lower_value


def regrading_monotonicity(
    states: tuple[State, ...],
    observation: Mapping[State, Observation],
    generators: Generators,
    lower_costs: Mapping[str, int],
    upper_costs: Mapping[str, int],
    maximum_budget: int,
) -> bool:
    """Audit generatorwise cost increase: slower revelation and no cheaper paths."""
    if not costs_dominate(lower_costs, upper_costs):
        raise ValueError("upper_costs must dominate lower_costs generatorwise")
    lower_partitions = budget_partitions(
        states, observation, generators, lower_costs, maximum_budget
    )
    upper_partitions = budget_partitions(
        states, observation, generators, upper_costs, maximum_budget
    )
    # More expensive operations expose fewer distinctions at the same budget, so
    # the lower-cost partition refines the upper-cost partition.
    for budget in range(maximum_budget + 1):
        if not partition_refines(lower_partitions[budget], upper_partitions[budget]):
            return False
    for left in states:
        for right in states:
            if not finite_cost_order_preserved(
                distinguishing_cost(
                    states, observation, generators, lower_costs, left, right
                ),
                distinguishing_cost(
                    states, observation, generators, upper_costs, left, right
                ),
            ):
                return False
            if not finite_cost_order_preserved(
                transport_cost(states, generators, lower_costs, left, right),
                transport_cost(states, generators, upper_costs, left, right),
            ):
                return False
    return True


def uniformly_scaled_costs(
    costs: Mapping[str, int],
    multiplier: int,
) -> dict[str, int]:
    if isinstance(multiplier, bool) or not isinstance(multiplier, int) or multiplier <= 0:
        raise ValueError("multiplier must be a positive integer")
    if any(
        isinstance(value, bool) or not isinstance(value, int) or value <= 0
        for value in costs.values()
    ):
        raise ValueError("costs must be positive integers")
    return {label: multiplier * value for label, value in costs.items()}


def uniform_regrading_exact(
    states: tuple[State, ...],
    observation: Mapping[State, Observation],
    generators: Generators,
    costs: Mapping[str, int],
    multiplier: int,
    maximum_budget: int,
) -> bool:
    """Audit exact uniform cost rescaling on paths and budget partitions."""
    scaled = uniformly_scaled_costs(costs, multiplier)
    base_partitions = budget_partitions(
        states,
        observation,
        generators,
        costs,
        maximum_budget // multiplier,
    )
    scaled_partitions = budget_partitions(
        states,
        observation,
        generators,
        scaled,
        maximum_budget,
    )
    for budget in range(maximum_budget + 1):
        base = base_partitions[budget // multiplier]
        scaled_partition = scaled_partitions[budget]
        # Canonical class ids may be compared by equivalence structure only.
        if not (
            partition_refines(base, scaled_partition)
            and partition_refines(scaled_partition, base)
        ):
            return False
    for left in states:
        for right in states:
            base_d = distinguishing_cost(
                states, observation, generators, costs, left, right
            )
            scaled_d = distinguishing_cost(
                states, observation, generators, scaled, left, right
            )
            if base_d is None:
                if scaled_d is not None:
                    return False
            elif scaled_d != multiplier * base_d:
                return False
            base_t = transport_cost(states, generators, costs, left, right)
            scaled_t = transport_cost(states, generators, scaled, left, right)
            if base_t is None:
                if scaled_t is not None:
                    return False
            elif scaled_t != multiplier * base_t:
                return False
    return True
