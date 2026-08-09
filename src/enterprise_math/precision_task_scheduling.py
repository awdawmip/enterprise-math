"""Context-derived finite task scheduling for precision acquisition.

A final joint precision is independent of the order in which observations are
added, but the product of worst local repair alphabets -- and therefore the sum
of fixed-base integer symbol depths -- can depend strongly on order.

This module derives the cost of adding each task from the current joint context
itself, then solves the finite ordering problem by subset dynamic programming.
No probabilities, expected values, logarithms, or externally supplied per-task
costs are required.
"""

from __future__ import annotations

from collections.abc import Hashable, Iterable, Mapping
from functools import lru_cache

from .precision_incidence_geometry import integer_symbol_depth
from .precision_incidence_hypergraph import (
    conditional_repair_factor,
    extension_sets,
    joint_partition,
    realized_joint_class_count,
)

State = Hashable
Partition = Mapping[State, Hashable]


def _domain(states: Iterable[State]) -> tuple[State, ...]:
    domain = tuple(states)
    if not domain:
        raise ValueError("state domain must be nonempty")
    if len(domain) != len(set(domain)):
        raise ValueError("state domain must contain distinct states")
    return domain


def _tasks(
    states: tuple[State, ...], tasks: Mapping[str, Partition]
) -> dict[str, Partition]:
    result = dict(tasks)
    if not result:
        raise ValueError("at least one task partition is required")
    state_set = set(states)
    for name, partition in result.items():
        if not isinstance(name, str) or not name:
            raise ValueError("task names must be nonempty strings")
        if set(partition) != state_set:
            raise ValueError("every task partition must cover the state domain exactly")
    return result


def universal_partition(states: Iterable[State]) -> dict[State, int]:
    domain = _domain(states)
    return {state: 0 for state in domain}


def context_partition(
    states: Iterable[State], tasks: Mapping[str, Partition], names: Iterable[str]
) -> dict[State, Hashable]:
    """Joint partition of selected tasks; empty selection is the universal block."""

    domain = _domain(states)
    family = _tasks(domain, tasks)
    selected = tuple(names)
    if any(name not in family for name in selected):
        raise ValueError("context contains an unknown task name")
    if not selected:
        return universal_partition(domain)
    return joint_partition(domain, [family[name] for name in selected])


def incremental_repair_factor(
    states: Iterable[State],
    tasks: Mapping[str, Partition],
    known_names: Iterable[str],
    added_name: str,
) -> int:
    domain = _domain(states)
    family = _tasks(domain, tasks)
    known = tuple(known_names)
    if added_name not in family:
        raise ValueError("added task is unknown")
    if added_name in known:
        return 1
    known_partitions = [family[name] for name in known]
    if not known_partitions:
        known_partitions = [universal_partition(domain)]
    return conditional_repair_factor(domain, known_partitions, family[added_name])


def order_profile(
    states: Iterable[State],
    tasks: Mapping[str, Partition],
    order: Iterable[str],
    base: int = 2,
) -> dict[str, object]:
    """Exact sequential repair capacity and integer-depth profile for one order."""

    domain = _domain(states)
    family = _tasks(domain, tasks)
    sequence = tuple(order)
    if len(sequence) != len(family) or set(sequence) != set(family):
        raise ValueError("order must contain every task name exactly once")

    known: list[str] = []
    factors: list[int] = []
    depths: list[int] = []
    uniform: list[bool] = []
    product_capacity = 1

    for name in sequence:
        known_partitions = [family[item] for item in known]
        if not known_partitions:
            known_partitions = [universal_partition(domain)]
        extensions = extension_sets(domain, known_partitions, family[name])
        degree_values = tuple(len(values) for values in extensions.values())
        factor = max(degree_values)
        factors.append(factor)
        depths.append(integer_symbol_depth(factor, base))
        uniform.append(all(value == factor for value in degree_values))
        product_capacity *= factor
        known.append(name)

    final_count = realized_joint_class_count(domain, list(family.values()))
    if final_count > product_capacity:
        raise AssertionError("joint class count exceeded sequential repair capacity")

    final_depth_lower_bound = integer_symbol_depth(final_count, base)
    total_depth = sum(depths)
    if total_depth < final_depth_lower_bound:
        raise AssertionError("sequential depth fell below final joint-state lower bound")

    product_equality = final_count == product_capacity
    if product_equality != all(uniform):
        raise AssertionError("uniform-branching equality criterion failed")

    return {
        "order": sequence,
        "repair_factors": tuple(factors),
        "repair_depths": tuple(depths),
        "uniform_branching": tuple(uniform),
        "product_capacity": product_capacity,
        "final_joint_class_count": final_count,
        "product_slack": product_capacity - final_count,
        "total_symbol_depth": total_depth,
        "final_depth_lower_bound": final_depth_lower_bound,
        "depth_slack": total_depth - final_depth_lower_bound,
        "product_equality": product_equality,
    }


def optimal_order_by_symbol_depth(
    states: Iterable[State],
    tasks: Mapping[str, Partition],
    base: int = 2,
) -> dict[str, object]:
    """Minimum total context-derived integer symbol depth over all task orders."""

    domain = _domain(states)
    family = _tasks(domain, tasks)
    names = tuple(sorted(family))

    @lru_cache(maxsize=None)
    def solve(known: frozenset[str]) -> tuple[int, tuple[str, ...]]:
        if len(known) == len(names):
            return 0, ()
        best: tuple[int, tuple[str, ...]] | None = None
        known_order = tuple(sorted(known))
        for name in names:
            if name in known:
                continue
            factor = incremental_repair_factor(domain, family, known_order, name)
            step = integer_symbol_depth(factor, base)
            tail_cost, tail_order = solve(known | {name})
            candidate = (step + tail_cost, (name,) + tail_order)
            if best is None or candidate < best:
                best = candidate
        if best is None:
            raise AssertionError("finite task scheduling found no next task")
        return best

    minimum, order = solve(frozenset())
    profile = order_profile(domain, family, order, base)
    if profile["total_symbol_depth"] != minimum:
        raise AssertionError("dynamic-program cost disagreed with reconstructed order")
    return {"minimum_symbol_depth": minimum, **profile}


def optimal_order_by_product_capacity(
    states: Iterable[State], tasks: Mapping[str, Partition]
) -> dict[str, object]:
    """Minimum product of conditional repair factors over all task orders."""

    domain = _domain(states)
    family = _tasks(domain, tasks)
    names = tuple(sorted(family))

    @lru_cache(maxsize=None)
    def solve(known: frozenset[str]) -> tuple[int, tuple[str, ...]]:
        if len(known) == len(names):
            return 1, ()
        best: tuple[int, tuple[str, ...]] | None = None
        known_order = tuple(sorted(known))
        for name in names:
            if name in known:
                continue
            factor = incremental_repair_factor(domain, family, known_order, name)
            tail_product, tail_order = solve(known | {name})
            candidate = (factor * tail_product, (name,) + tail_order)
            if best is None or candidate < best:
                best = candidate
        if best is None:
            raise AssertionError("finite task scheduling found no next task")
        return best

    minimum, order = solve(frozenset())
    profile = order_profile(domain, family, order, base=2)
    if profile["product_capacity"] != minimum:
        raise AssertionError("dynamic-program product disagreed with reconstructed order")
    return {"minimum_product_capacity": minimum, **profile}
