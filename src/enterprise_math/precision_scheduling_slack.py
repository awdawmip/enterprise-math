"""Exact decomposition of finite precision task-scheduling slack.

For one task order, the S14 product capacity P is the product of conditional
repair factors and N is the final realized joint-class count.  Base-B symbol
cost exceeds the final class-cardinality lower bound for two independent
reasons:

1. radix packing: separate integer ceilings at each stage;
2. incidence capacity: stagewise worst-case product exceeds realized classes.

The two nonnegative integer depth gaps add exactly to total scheduling slack.
"""

from __future__ import annotations

from collections.abc import Hashable, Iterable, Mapping, Sequence

from .precision_incidence_geometry import integer_symbol_depth
from .precision_task_scheduling import order_profile, optimal_order_by_symbol_depth

State = Hashable
Partition = Mapping[State, Hashable]


def schedule_slack_decomposition(
    states: Iterable[State],
    tasks: Mapping[str, Partition],
    order: Sequence[str],
    base: int = 2,
) -> dict[str, object]:
    """Split total depth slack into radix and incidence-capacity components."""

    profile = order_profile(states, tasks, order, base)
    product_capacity = int(profile["product_capacity"])
    final_count = int(profile["final_joint_class_count"])
    total_depth = int(profile["total_symbol_depth"])
    final_lower = int(profile["final_depth_lower_bound"])

    product_depth = integer_symbol_depth(product_capacity, base)
    radix_packing_slack = total_depth - product_depth
    incidence_capacity_slack = product_depth - final_lower
    total_slack = total_depth - final_lower

    if radix_packing_slack < 0 or incidence_capacity_slack < 0:
        raise AssertionError("scheduling slack components must be nonnegative")
    if total_slack != radix_packing_slack + incidence_capacity_slack:
        raise AssertionError("scheduling slack failed exact two-term decomposition")

    return {
        **profile,
        "product_depth": product_depth,
        "radix_packing_slack": radix_packing_slack,
        "incidence_capacity_slack": incidence_capacity_slack,
        "total_slack": total_slack,
    }


def optimal_interface_overhead(
    states: Iterable[State], tasks: Mapping[str, Partition], base: int = 2
) -> dict[str, object]:
    """Minimum schedule depth minus the final joint-class lower bound."""

    optimal = optimal_order_by_symbol_depth(states, tasks, base)
    overhead = int(optimal["total_symbol_depth"]) - int(optimal["final_depth_lower_bound"])
    if overhead < 0:
        raise AssertionError("optimal interface overhead cannot be negative")
    return {**optimal, "interface_overhead": overhead}


def incidence_only_slack_witness() -> tuple[tuple[int, ...], dict[str, dict[int, str]]]:
    """Five-state two-task family with incidence slack but no radix slack.

    Each task has three blocks and each direction has repair factor three, so
    product capacity is nine.  Only five incidence edges are realized.  In base
    two, stage depths total four, product depth is four, but final depth is three.
    """

    states = (0, 1, 2, 3, 4)
    tasks = {
        "E": {0: "A", 1: "A", 2: "A", 3: "B", 4: "C"},
        "F": {0: "X", 1: "Y", 2: "Z", 3: "X", 4: "X"},
    }
    return states, tasks


def radix_only_slack_witness() -> tuple[tuple[int, ...], dict[str, dict[int, int]]]:
    """Complete 3x5 incidence with one bit of radix packing slack in base two."""

    states = tuple(range(15))
    tasks = {
        "E": {state: state // 5 for state in states},
        "F": {state: state % 5 for state in states},
    }
    return states, tasks
