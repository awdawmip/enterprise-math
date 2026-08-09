"""Correct stabilization criteria for positive-integer graded future budgets.

The unit-word-length theorem 'P_(L+1)=P_L implies permanent stability' does not
extend to arbitrary generator costs: a generator of cost five can leave budgets
0..4 unchanged and split the partition at budget five.

Let Cmax be the largest primitive cost.  Because budget partitions are nested,
if R>=Cmax and P_R=P_(R-Cmax), then the whole Cmax-wide window is constant.  The
budget-R signature then shows that every generator preserves that common
partition, so the partition is stable for all larger budgets.

The exact weighted composition horizon is the maximum finite pair distinguishing
cost.  At that budget every ultimately distinguishable pair has already split.
"""

from __future__ import annotations

from typing import Hashable, Mapping

from .causal_operation_language import Generators, same_partition
from .causal_weighted_future import budget_partitions, distinguishing_cost

State = Hashable
Observation = Hashable


def maximum_primitive_cost(costs: Mapping[str, int]) -> int:
    if not costs:
        return 0
    if any(
        isinstance(value, bool) or not isinstance(value, int) or value <= 0
        for value in costs.values()
    ):
        raise ValueError("primitive costs must be positive integers")
    return max(costs.values())


def weighted_composition_horizon(
    states: tuple[State, ...],
    observation: Mapping[State, Observation],
    generators: Generators,
    costs: Mapping[str, int],
) -> int:
    finite = []
    for left in states:
        for right in states:
            depth = distinguishing_cost(
                states, observation, generators, costs, left, right
            )
            if depth is not None:
                finite.append(depth)
    return max(finite, default=0)


def horizon_partition_is_ultimate(
    states: tuple[State, ...],
    observation: Mapping[State, Observation],
    generators: Generators,
    costs: Mapping[str, int],
) -> bool:
    horizon = weighted_composition_horizon(
        states, observation, generators, costs
    )
    partitions = budget_partitions(
        states, observation, generators, costs, horizon
    )
    final = partitions[horizon]
    return all(
        (final[left] == final[right])
        == (
            distinguishing_cost(
                states, observation, generators, costs, left, right
            )
            is None
        )
        for left in states
        for right in states
    )


def weighted_window_stability_certificate(
    states: tuple[State, ...],
    observation: Mapping[State, Observation],
    generators: Generators,
    costs: Mapping[str, int],
    budget: int,
) -> bool:
    """Sufficient exact certificate P_R=P_(R-Cmax) for permanent stabilization."""
    cmax = maximum_primitive_cost(costs)
    if budget < cmax:
        return False
    partitions = budget_partitions(
        states, observation, generators, costs, budget
    )
    return same_partition(partitions[budget], partitions[budget - cmax])


def weighted_window_certificate_is_sound(
    states: tuple[State, ...],
    observation: Mapping[State, Observation],
    generators: Generators,
    costs: Mapping[str, int],
    budget: int,
) -> bool:
    if not weighted_window_stability_certificate(
        states, observation, generators, costs, budget
    ):
        return False
    horizon = weighted_composition_horizon(
        states, observation, generators, costs
    )
    partitions = budget_partitions(
        states,
        observation,
        generators,
        costs,
        max(budget, horizon),
    )
    return same_partition(partitions[budget], partitions[-1])
