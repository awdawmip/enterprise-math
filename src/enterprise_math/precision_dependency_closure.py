"""Zero-cost task dependency closure for finite precision systems.

For a finite family of task partitions, a task belongs to the closure of an
already retained task set when its partition is a function of the current joint
context.  Equivalently its conditional P023 repair factor is one, so the task
can be added without changing the represented precision state.

The closure is extensive, monotone and idempotent.  It need not satisfy matroid
exchange; higher-order functional dependencies therefore support closure-state
compression but not a generic greedy theorem.
"""

from __future__ import annotations

from collections.abc import Hashable, Iterable, Mapping
from functools import lru_cache

from .precision_incidence_geometry import integer_symbol_depth
from .precision_task_scheduling import (
    context_partition,
    incremental_repair_factor,
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


def _validate_tasks(domain: tuple[State, ...], tasks: Mapping[str, Partition]) -> dict[str, Partition]:
    family = dict(tasks)
    if not family:
        raise ValueError("at least one task partition is required")
    state_set = set(domain)
    for name, partition in family.items():
        if not isinstance(name, str) or not name:
            raise ValueError("task names must be nonempty strings")
        if set(partition) != state_set:
            raise ValueError("every task partition must cover the state domain exactly")
    return family


def task_dependency_closure(
    states: Iterable[State], tasks: Mapping[str, Partition], known_names: Iterable[str]
) -> frozenset[str]:
    """Tasks already determined by the joint context of ``known_names``."""

    domain = _domain(states)
    family = _validate_tasks(domain, tasks)
    known = frozenset(known_names)
    if not known.issubset(family):
        raise ValueError("known_names contains an unknown task")

    context = context_partition(domain, family, tuple(sorted(known)))
    closure = set(known)
    for name in family:
        if name in closure:
            continue
        # A task is free exactly when current context already refines it.
        factor = incremental_repair_factor(domain, family, tuple(sorted(known)), name)
        if factor == 1:
            closure.add(name)
            # Adding a factor-one task does not refine context, so no iteration
            # is needed.  Still, the result is exactly the full closure.
    return frozenset(closure)


def all_closed_task_sets(
    states: Iterable[State], tasks: Mapping[str, Partition]
) -> tuple[frozenset[str], ...]:
    """Enumerate the finite closure system of task sets."""

    domain = _domain(states)
    family = _validate_tasks(domain, tasks)
    names = tuple(sorted(family))
    closed: set[frozenset[str]] = set()
    for mask in range(1 << len(names)):
        subset = frozenset(name for index, name in enumerate(names) if mask & (1 << index))
        closed.add(task_dependency_closure(domain, family, subset))
    return tuple(sorted(closed, key=lambda value: (len(value), tuple(sorted(value)))))


def is_task_basis(
    states: Iterable[State], tasks: Mapping[str, Partition], names: Iterable[str]
) -> bool:
    """Whether selected tasks already generate the full joint precision."""

    domain = _domain(states)
    family = _validate_tasks(domain, tasks)
    return task_dependency_closure(domain, family, names) == frozenset(family)


def minimal_task_bases(
    states: Iterable[State], tasks: Mapping[str, Partition]
) -> tuple[frozenset[str], ...]:
    """Inclusion-minimal task sets whose closure is the whole task family."""

    domain = _domain(states)
    family = _validate_tasks(domain, tasks)
    names = tuple(sorted(family))
    bases: list[frozenset[str]] = []
    for mask in range(1 << len(names)):
        subset = frozenset(name for index, name in enumerate(names) if mask & (1 << index))
        if not is_task_basis(domain, family, subset):
            continue
        if any(existing.issubset(subset) for existing in bases):
            continue
        bases = [existing for existing in bases if not subset.issubset(existing)]
        bases.append(subset)
    return tuple(sorted(bases, key=lambda value: (len(value), tuple(sorted(value)))))


def optimal_closed_context_schedule(
    states: Iterable[State], tasks: Mapping[str, Partition], base: int = 2
) -> dict[str, object]:
    """Exact DP over closure states rather than all raw task subsets.

    Choosing one nonclosed task pays its current conditional repair depth and is
    followed immediately by zero-cost closure.  The optimum equals the ordinary
    subset DP optimum, but the number of DP states is the number of closed task
    sets rather than ``2**m``.
    """

    domain = _domain(states)
    family = _validate_tasks(domain, tasks)
    all_names = frozenset(family)
    start = task_dependency_closure(domain, family, ())

    visited: set[frozenset[str]] = set()

    @lru_cache(maxsize=None)
    def solve(closed: frozenset[str]) -> tuple[int, tuple[str, ...]]:
        visited.add(closed)
        if closed == all_names:
            return 0, ()
        best: tuple[int, tuple[str, ...]] | None = None
        known = tuple(sorted(closed))
        for name in sorted(all_names - closed):
            factor = incremental_repair_factor(domain, family, known, name)
            if factor <= 1:
                raise AssertionError("closed context left a zero-cost task outside closure")
            step = integer_symbol_depth(factor, base)
            next_closed = task_dependency_closure(domain, family, (*closed, name))
            tail_cost, tail_generators = solve(next_closed)
            candidate = (step + tail_cost, (name,) + tail_generators)
            if best is None or candidate < best:
                best = candidate
        if best is None:
            raise AssertionError("closed-context scheduler found no next task")
        return best

    minimum, generators = solve(start)
    return {
        "minimum_symbol_depth": minimum,
        "positive_cost_generators": generators,
        "initial_closure": start,
        "closed_states_visited": len(visited),
        "all_closed_state_count": len(all_closed_task_sets(domain, family)),
        "raw_subset_state_count": 1 << len(family),
    }


def closure_exchange_holds(
    states: Iterable[State],
    tasks: Mapping[str, Partition],
    known: Iterable[str],
    x: str,
    y: str,
) -> bool:
    """Check the matroid-closure exchange implication for one proposed witness."""

    domain = _domain(states)
    family = _validate_tasks(domain, tasks)
    known_set = frozenset(known)
    if x not in family or y not in family:
        raise ValueError("x and y must name supplied tasks")
    base = task_dependency_closure(domain, family, known_set)
    with_y = task_dependency_closure(domain, family, (*known_set, y))
    antecedent = x in with_y and x not in base
    if not antecedent:
        return True
    with_x = task_dependency_closure(domain, family, (*known_set, x))
    return y in with_x
