"""Greedy baseline and counterexample utilities for conditional repair scheduling.

The exact scheduler lives in ``precision_task_scheduling``.  This module keeps a
simple cheapest-next heuristic as an explicitly noncanonical baseline so that
research code can falsify claims that local minimum repair cost implies a
globally minimum task order.
"""

from __future__ import annotations

from collections.abc import Hashable, Iterable, Mapping

from .precision_incidence_geometry import integer_symbol_depth
from .precision_task_scheduling import (
    context_partition,
    incremental_repair_factor,
    order_profile,
)

State = Hashable
Partition = Mapping[State, Hashable]


def greedy_order_by_symbol_depth(
    states: Iterable[State],
    tasks: Mapping[str, Partition],
    base: int = 2,
) -> dict[str, object]:
    """Choose the cheapest current task, breaking ties by factor then name.

    This heuristic is deterministic but not generally optimal.  Its purpose is
    to provide a reproducible baseline against the exact subset dynamic program.
    """

    domain = tuple(states)
    if not domain:
        raise ValueError("state domain must be nonempty")
    if len(domain) != len(set(domain)):
        raise ValueError("state domain must contain distinct states")
    if not tasks:
        raise ValueError("at least one task is required")

    remaining = set(tasks)
    known: list[str] = []
    order: list[str] = []
    while remaining:
        scored = []
        for name in remaining:
            factor = incremental_repair_factor(domain, tasks, known, name)
            depth = integer_symbol_depth(factor, base)
            scored.append((depth, factor, name))
        _depth, _factor, chosen = min(scored)
        order.append(chosen)
        known.append(chosen)
        remaining.remove(chosen)

    return order_profile(domain, tasks, order, base)


def five_state_greedy_counterexample() -> tuple[tuple[int, ...], dict[str, dict[int, int]]]:
    """Return a minimal small witness used by the S13 greedy no-go theorem.

    A and B each cost one binary symbol from the universal context.  C costs two.
    Every cheapest-next greedy rule therefore starts with A or B and pays total
    depth three.  Starting with C costs two symbols once and makes A and B
    redundant, so the global optimum is two.
    """

    states = (0, 1, 2, 3, 4)
    tasks = {
        "A": {0: 0, 1: 0, 2: 0, 3: 0, 4: 1},
        "B": {0: 0, 1: 0, 2: 0, 3: 1, 4: 0},
        "C": {0: 0, 1: 0, 2: 1, 3: 2, 4: 3},
    }
    return states, tasks
