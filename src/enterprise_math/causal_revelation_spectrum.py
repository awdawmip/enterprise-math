"""P011-style revelation spectrum for graded causal future partitions.

For positive-integer graded operations, let P_R be the partition of states that
no future word of total cost <=R can distinguish.  Its collision coordinates

    J_k(R)=sum_(C in P_R) C(|C|,k)

decrease with R.  The exact split spectrum

    Lambda_k(R)=J_k(R-1)-J_k(R)

counts k-subsets that remain wholly future-indistinguishable through budget R-1
but are first split at budget R.  For k=2 this is exactly the histogram of
finite distinguishing costs.
"""

from __future__ import annotations

from collections import defaultdict
from math import comb
from typing import Hashable, Mapping

from .causal_operation_language import Generators, Partition
from .causal_weighted_future import budget_partitions, distinguishing_cost

State = Hashable
Observation = Hashable


def partition_collision_coordinate(
    states: tuple[State, ...],
    partition: Partition,
    order: int,
) -> int:
    if set(partition) != set(states):
        raise ValueError("partition must cover every state")
    if isinstance(order, bool) or not isinstance(order, int) or order < 1:
        raise ValueError("order must be a positive integer")
    sizes: dict[int, int] = defaultdict(int)
    for state in states:
        sizes[partition[state]] += 1
    return sum(comb(size, order) for size in sizes.values() if size >= order)


def collision_profile_by_budget(
    states: tuple[State, ...],
    observation: Mapping[State, Observation],
    generators: Generators,
    costs: Mapping[str, int],
    maximum_budget: int,
    maximum_order: int,
) -> tuple[tuple[int, ...], ...]:
    if isinstance(maximum_order, bool) or not isinstance(maximum_order, int) or maximum_order < 1:
        raise ValueError("maximum_order must be a positive integer")
    partitions = budget_partitions(
        states, observation, generators, costs, maximum_budget
    )
    return tuple(
        tuple(
            partition_collision_coordinate(states, partition, order)
            for order in range(1, maximum_order + 1)
        )
        for partition in partitions
    )


def revelation_spectrum(
    states: tuple[State, ...],
    observation: Mapping[State, Observation],
    generators: Generators,
    costs: Mapping[str, int],
    maximum_budget: int,
    maximum_order: int,
) -> tuple[tuple[int, ...], ...]:
    """Rows R=1..B of Lambda_k(R), columns k=1..K."""
    profile = collision_profile_by_budget(
        states,
        observation,
        generators,
        costs,
        maximum_budget,
        maximum_order,
    )
    return tuple(
        tuple(before - after for before, after in zip(profile[budget - 1], profile[budget]))
        for budget in range(1, len(profile))
    )


def revelation_spectrum_is_nonnegative(
    states: tuple[State, ...],
    observation: Mapping[State, Observation],
    generators: Generators,
    costs: Mapping[str, int],
    maximum_budget: int,
    maximum_order: int,
) -> bool:
    return all(
        value >= 0
        for row in revelation_spectrum(
            states,
            observation,
            generators,
            costs,
            maximum_budget,
            maximum_order,
        )
        for value in row
    )


def pair_distinguishing_histogram(
    states: tuple[State, ...],
    observation: Mapping[State, Observation],
    generators: Generators,
    costs: Mapping[str, int],
) -> dict[int, int]:
    """Histogram of finite pair distinguishing costs, including cost zero."""
    histogram: dict[int, int] = {}
    for index, left in enumerate(states):
        for right in states[index + 1 :]:
            cost = distinguishing_cost(
                states, observation, generators, costs, left, right
            )
            if cost is None:
                continue
            histogram[cost] = histogram.get(cost, 0) + 1
    return dict(sorted(histogram.items()))


def pair_revelation_matches_cost_histogram(
    states: tuple[State, ...],
    observation: Mapping[State, Observation],
    generators: Generators,
    costs: Mapping[str, int],
) -> bool:
    """Check Lambda_2(R)=#{pairs with distinguishing cost R} for every finite R>=1.

    Pairs already distinguished by the current observation have cost zero and are
    absent from P_0, so they are handled separately by the histogram.
    """
    histogram = pair_distinguishing_histogram(
        states, observation, generators, costs
    )
    positive_costs = tuple(cost for cost in histogram if cost > 0)
    maximum_budget = max(positive_costs, default=0)
    if maximum_budget == 0:
        return True
    spectrum = revelation_spectrum(
        states,
        observation,
        generators,
        costs,
        maximum_budget,
        2,
    )
    return all(
        spectrum[budget - 1][1] == histogram.get(budget, 0)
        for budget in range(1, maximum_budget + 1)
    )


def telescoping_revelation_total(
    states: tuple[State, ...],
    observation: Mapping[State, Observation],
    generators: Generators,
    costs: Mapping[str, int],
    maximum_budget: int,
    order: int,
) -> tuple[int, int]:
    """Return `(sum_R Lambda_k(R), J_k(0)-J_k(B))` for audit."""
    profile = collision_profile_by_budget(
        states,
        observation,
        generators,
        costs,
        maximum_budget,
        order,
    )
    spectrum = revelation_spectrum(
        states,
        observation,
        generators,
        costs,
        maximum_budget,
        order,
    )
    summed = sum(row[order - 1] for row in spectrum)
    telescoped = profile[0][order - 1] - profile[-1][order - 1]
    return summed, telescoped
