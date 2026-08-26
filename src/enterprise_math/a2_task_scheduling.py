"""Context-derived task scheduling for finite A2 precision systems.

Task costs are not external weights.  At each context, the exact cost of adding a
new partition is the minimum repair alphabet required by the current joint
precision.  The module provides exact scheduling profiles, subset DP, dependency
closure, and two-stage normalization diagnostics.
"""

from __future__ import annotations

from collections.abc import Hashable, Iterable, Mapping
from functools import lru_cache
from itertools import combinations
from math import prod
from typing import TypeAlias

from .a2_precision_incidence import (
    Partition,
    block_count,
    conditional_repair_factor,
    extension_sets,
    integer_symbol_depth,
    realized_joint_class_count,
)

State = Hashable
TaskFamily: TypeAlias = Mapping[str, Partition]


def _domain(states: Iterable[State]) -> tuple[State, ...]:
    domain = tuple(states)
    if not domain:
        raise ValueError("state domain must be nonempty")
    if len(domain) != len(set(domain)):
        raise ValueError("state domain must contain distinct states")
    return domain


def _tasks(domain: tuple[State, ...], tasks: TaskFamily) -> dict[str, Partition]:
    family = dict(tasks)
    if not family:
        raise ValueError("at least one task is required")
    target = set(domain)
    for name, partition in family.items():
        if not name:
            raise ValueError("task names must be nonempty")
        if set(partition) != target:
            raise ValueError("every task partition must cover the domain")
    return family


def universal_partition(states: Iterable[State]) -> dict[State, int]:
    domain = _domain(states)
    return {state: 0 for state in domain}


def context_partitions(tasks: TaskFamily, names: Iterable[str]) -> list[Partition]:
    selected = tuple(names)
    return [tasks[name] for name in selected]


def incremental_repair_factor(
    states: Iterable[State],
    tasks: TaskFamily,
    known_names: Iterable[str],
    added_name: str,
) -> int:
    domain = _domain(states)
    family = _tasks(domain, tasks)
    known = tuple(known_names)
    if added_name not in family:
        raise ValueError("added task is unknown")
    if any(name not in family for name in known):
        raise ValueError("known task is unknown")
    if added_name in known:
        return 1
    return conditional_repair_factor(
        domain, [family[name] for name in known], family[added_name]
    )


def task_dependency_closure(
    states: Iterable[State], tasks: TaskFamily, selected: Iterable[str]
) -> frozenset[str]:
    """Close a task set under zero-extra-repair functional dependence."""
    domain = _domain(states)
    family = _tasks(domain, tasks)
    closure = set(selected)
    if any(name not in family for name in closure):
        raise ValueError("selected task is unknown")
    changed = True
    while changed:
        changed = False
        known_parts = [family[name] for name in sorted(closure)]
        for name in sorted(family):
            if name in closure:
                continue
            if conditional_repair_factor(domain, known_parts, family[name]) == 1:
                closure.add(name)
                changed = True
    return frozenset(closure)


def all_closed_task_sets(
    states: Iterable[State], tasks: TaskFamily
) -> tuple[frozenset[str], ...]:
    domain = _domain(states)
    family = _tasks(domain, tasks)
    names = tuple(sorted(family))
    closed = set()
    for size in range(len(names) + 1):
        for subset in combinations(names, size):
            closed.add(task_dependency_closure(domain, family, subset))
    return tuple(sorted(closed, key=lambda item: (len(item), tuple(sorted(item)))))


def minimal_task_bases(
    states: Iterable[State], tasks: TaskFamily
) -> tuple[frozenset[str], ...]:
    domain = _domain(states)
    family = _tasks(domain, tasks)
    names = tuple(sorted(family))
    full = frozenset(names)
    bases = []
    for size in range(1, len(names) + 1):
        for subset in combinations(names, size):
            chosen = frozenset(subset)
            if task_dependency_closure(domain, family, chosen) != full:
                continue
            if any(
                task_dependency_closure(domain, family, chosen - {name}) == full
                for name in chosen
            ):
                continue
            bases.append(chosen)
    return tuple(bases)


def generator_number(states: Iterable[State], tasks: TaskFamily) -> int:
    return min(len(basis) for basis in minimal_task_bases(states, tasks))


def order_profile(
    states: Iterable[State],
    tasks: TaskFamily,
    order: Iterable[str],
    base: int = 2,
) -> dict[str, object]:
    """Exact sequential worst-case repair profile for one task order."""
    domain = _domain(states)
    family = _tasks(domain, tasks)
    sequence = tuple(order)
    if len(sequence) != len(family) or set(sequence) != set(family):
        raise ValueError("order must contain every task exactly once")

    known: list[str] = []
    factors: list[int] = []
    depths: list[int] = []
    uniform: list[bool] = []
    product_capacity = 1

    for name in sequence:
        extensions = extension_sets(
            domain, [family[item] for item in known], family[name]
        )
        degrees = tuple(len(values) for values in extensions.values())
        factor = max(degrees)
        factors.append(factor)
        depths.append(integer_symbol_depth(factor, base))
        uniform.append(all(value == factor for value in degrees))
        product_capacity *= factor
        known.append(name)

    final_count = realized_joint_class_count(domain, list(family.values()))
    if final_count > product_capacity:
        raise AssertionError("joint class count exceeded staged repair capacity")
    total_depth = sum(depths)
    final_depth = integer_symbol_depth(final_count, base)
    packed_depth = integer_symbol_depth(product_capacity, base)
    if total_depth < packed_depth or packed_depth < final_depth:
        raise AssertionError("symbol-depth ordering violated")
    equality = final_count == product_capacity
    if equality != all(uniform):
        raise AssertionError("uniform-branching equality criterion failed")

    return {
        "order": sequence,
        "repair_factors": tuple(factors),
        "repair_depths": tuple(depths),
        "uniform_branching": tuple(uniform),
        "product_capacity": product_capacity,
        "final_joint_class_count": final_count,
        "final_state_depth": final_depth,
        "packed_product_depth": packed_depth,
        "total_symbol_depth": total_depth,
        "radix_packing_slack": total_depth - packed_depth,
        "incidence_capacity_slack": packed_depth - final_depth,
        "total_depth_slack": total_depth - final_depth,
        "product_equality": equality,
    }


def optimal_order_by_symbol_depth(
    states: Iterable[State], tasks: TaskFamily, base: int = 2
) -> dict[str, object]:
    domain = _domain(states)
    family = _tasks(domain, tasks)
    names = tuple(sorted(family))

    @lru_cache(maxsize=None)
    def solve(known: frozenset[str]) -> tuple[int, tuple[str, ...]]:
        closed = task_dependency_closure(domain, family, known)
        if len(closed) == len(names):
            return 0, ()
        best: tuple[int, tuple[str, ...]] | None = None
        known_parts = [family[name] for name in sorted(closed)]
        for name in names:
            if name in closed:
                continue
            factor = conditional_repair_factor(domain, known_parts, family[name])
            step = integer_symbol_depth(factor, base)
            tail_cost, tail_order = solve(closed | {name})
            candidate = (step + tail_cost, (name,) + tail_order)
            if best is None or candidate < best:
                best = candidate
        if best is None:
            raise AssertionError("no scheduling transition found")
        return best

    cost, generators = solve(frozenset())
    closure: frozenset[str] = frozenset()
    full_order: list[str] = []
    for generator in generators:
        newly_free = sorted(task_dependency_closure(domain, family, closure) - closure)
        full_order.extend(name for name in newly_free if name not in full_order)
        if generator not in full_order:
            full_order.append(generator)
        closure = task_dependency_closure(domain, family, closure | {generator})
    full_order.extend(name for name in names if name not in full_order)
    profile = order_profile(domain, family, full_order, base)
    if profile["total_symbol_depth"] != cost:
        closure = frozenset()
        full_order = []
        for generator in generators:
            full_order.append(generator)
            old = closure | {generator}
            new = task_dependency_closure(domain, family, old)
            for name in sorted(new - old):
                full_order.append(name)
            closure = new
        full_order.extend(name for name in names if name not in full_order)
        profile = order_profile(domain, family, full_order, base)
    if profile["total_symbol_depth"] != cost:
        raise AssertionError("DP cost disagreed with reconstructed full order")
    return {
        "minimum_symbol_depth": cost,
        "positive_cost_generators": generators,
        **profile,
    }


def greedy_order_by_symbol_depth(
    states: Iterable[State], tasks: TaskFamily, base: int = 2
) -> dict[str, object]:
    domain = _domain(states)
    family = _tasks(domain, tasks)
    remaining = set(family)
    known: list[str] = []
    order: list[str] = []
    while remaining:
        scored = []
        for name in remaining:
            factor = incremental_repair_factor(domain, family, known, name)
            scored.append((integer_symbol_depth(factor, base), factor, name))
        _, _, chosen = min(scored)
        order.append(chosen)
        known.append(chosen)
        remaining.remove(chosen)
    return order_profile(domain, family, order, base)


def local_digit_codes(
    states: Iterable[State], tasks: TaskFamily, order: Iterable[str]
) -> dict[State, tuple[int, ...]]:
    """Assign deterministic local repair digits for a fixed schedule."""
    domain = _domain(states)
    family = _tasks(domain, tasks)
    sequence = tuple(order)
    if len(sequence) != len(family) or set(sequence) != set(family):
        raise ValueError("order must contain every task exactly once")
    known: list[str] = []
    digits: dict[State, list[int]] = {state: [] for state in domain}
    for name in sequence:
        ext = extension_sets(domain, [family[item] for item in known], family[name])
        ranks = {
            prefix: {label: index for index, label in enumerate(sorted(values, key=repr))}
            for prefix, values in ext.items()
        }
        for state in domain:
            prefix = tuple(family[item][state] for item in known)
            digits[state].append(ranks[prefix][family[name][state]])
        known.append(name)
    return {state: tuple(values) for state, values in digits.items()}


def pack_mixed_radix(digits: Iterable[int], radices: Iterable[int]) -> int:
    ds = tuple(digits)
    rs = tuple(radices)
    if len(ds) != len(rs):
        raise ValueError("digits and radices must have equal length")
    value = 0
    for digit, radix in zip(ds, rs, strict=True):
        if radix < 1 or not 0 <= digit < radix:
            raise ValueError("digit outside radix")
        value = value * radix + digit
    return value


def normalize_schedule_codes(
    states: Iterable[State], tasks: TaskFamily, order: Iterable[str], base: int = 2
) -> dict[str, object]:
    """Two exact normalizations: mixed-radix pack, then realized-code rank."""
    domain = _domain(states)
    family = _tasks(domain, tasks)
    profile = order_profile(domain, family, order, base)
    radices = tuple(profile["repair_factors"])
    digits = local_digit_codes(domain, family, order)
    packed = {state: pack_mixed_radix(digits[state], radices) for state in domain}
    if len(set(packed.values())) != int(profile["final_joint_class_count"]):
        raise AssertionError("packed schedule code failed to represent joint classes")
    realized_codes = sorted(set(packed.values()))
    rank = {code: index for index, code in enumerate(realized_codes)}
    normalized = {state: rank[packed[state]] for state in domain}
    if len(set(normalized.values())) != int(profile["final_joint_class_count"]):
        raise AssertionError("realized support ranking changed joint class count")
    return {
        **profile,
        "local_digits": digits,
        "packed_codes": packed,
        "realized_packed_codes": tuple(realized_codes),
        "normalized_codes": normalized,
    }


def five_state_greedy_counterexample() -> tuple[tuple[int, ...], dict[str, dict[int, int]]]:
    states = (0, 1, 2, 3, 4)
    tasks = {
        "A": {0: 0, 1: 0, 2: 0, 3: 0, 4: 1},
        "B": {0: 0, 1: 0, 2: 0, 3: 1, 4: 0},
        "C": {0: 0, 1: 0, 2: 1, 3: 2, 4: 3},
    }
    return states, tasks
