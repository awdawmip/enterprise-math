"""Selective rooted-circuit materialization for Stage131 AND-tree workloads.

The complete rooted-circuit table is exponentially large, but exact minimal
premise queries for one root have a useful independence property: distinct
inclusion-minimal premise sets form an antichain.  Therefore, when the workload
consists of exact minimal-premise queries, materializing circuit P benefits only
that query among the minimal-premise workload; it cannot make another distinct
minimal premise Q fire because P is not a subset of Q.

For a circuit P with base local-basis depth d(P) and query frequency f(P), direct
one-round materialization has additive gross benefit

    f(P) * (d(P)-1).

This gives exact selective-compilation problems:

* unit rule cost -> take highest-benefit circuits;
* premise-literal cost |P| -> bounded 0/1 knapsack;
* max fan-in W -> discard candidates with |P|>W.

For a balanced AND tree, circuits are aggregated by (width,base_depth), so one
does not need to enumerate the exponential premise table when workload weights
are type-symmetric.

A sharp fan-in law follows from the parent spectrum: exact depth-d circuits have
minimum width d+1.  Hence max fan-in W can realize at most base depth W-1, and
there are exactly 2^(d-1) minimum-width depth-d circuits at width d+1.

Knapsack and antichain selection are standard prior optimization/combinatorics.
The project value is the exact Stage131 compiler interpretation of rooted-circuit
materialization value.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import Mapping

from .stage131_rooted_circuit_table_explosion import (
    enumerate_rooted_circuit_premises,
    rooted_circuit_count,
)
from .stage131_rooted_circuit_value_spectrum import (
    materialization_round_saving,
    rooted_circuit_width_depth_spectrum,
)
from .stage131_horn_hyperedge_presentation import AndTree

CircuitType = tuple[int, int]  # (premise_width, base_depth)


def _positive_int(value: int, *, name: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")
    return value


def rooted_circuit_types(host_height: int) -> dict[CircuitType, int]:
    h = _positive_int(host_height, name="host_height")
    return rooted_circuit_width_depth_spectrum(h)


def minimum_width_circuit_count_at_depth(depth: int) -> int:
    d = _positive_int(depth, name="depth")
    return 1 << (d - 1)


def maximum_exact_base_depth_under_fan_in(host_height: int, max_fan_in: int) -> int:
    h = _positive_int(host_height, name="host_height")
    width = _positive_int(max_fan_in, name="max_fan_in")
    if width < 2:
        return 0
    return min(h, width - 1)


def maximum_round_saving_under_fan_in(host_height: int, max_fan_in: int) -> int:
    depth = maximum_exact_base_depth_under_fan_in(host_height, max_fan_in)
    if depth <= 0:
        return 0
    return materialization_round_saving(depth)


def available_circuit_count_under_fan_in(host_height: int, max_fan_in: int) -> int:
    h = _positive_int(host_height, name="host_height")
    width_limit = _positive_int(max_fan_in, name="max_fan_in")
    return sum(
        count
        for (width, _depth), count in rooted_circuit_types(h).items()
        if width <= width_limit
    )


def type_frequency_map(
    host_height: int,
    frequencies: Mapping[CircuitType, int | Fraction] | None = None,
) -> dict[CircuitType, Fraction]:
    types = rooted_circuit_types(host_height)
    if frequencies is None:
        return {key: Fraction(1) for key in types}
    result: dict[CircuitType, Fraction] = {}
    for key in types:
        value = Fraction(frequencies.get(key, 0))
        if value < 0:
            raise ValueError("type frequencies must be nonnegative")
        result[key] = value
    extras = set(frequencies) - set(types)
    if extras:
        raise ValueError("frequency map contains a circuit type absent from the host tree")
    return result


def per_circuit_benefit(
    circuit_type: CircuitType,
    frequency: int | Fraction,
) -> Fraction:
    width, depth = circuit_type
    if width <= 0 or depth <= 0:
        raise ValueError("circuit type must have positive width and depth")
    f = Fraction(frequency)
    if f < 0:
        raise ValueError("frequency must be nonnegative")
    return f * materialization_round_saving(depth)


@dataclass(frozen=True)
class MaterializedCircuitType:
    premise_width: int
    base_depth: int
    available_count: int
    selected_count: int
    frequency_per_circuit: Fraction
    benefit_per_circuit: Fraction

    @property
    def rule_storage(self) -> int:
        return self.selected_count

    @property
    def premise_literal_storage(self) -> int:
        return self.premise_width * self.selected_count

    @property
    def total_benefit(self) -> Fraction:
        return self.benefit_per_circuit * self.selected_count


@dataclass(frozen=True)
class SelectiveMaterializationPlan:
    host_height: int
    selected: tuple[MaterializedCircuitType, ...]
    total_available_circuits: int
    selected_circuits: int
    total_rule_storage: int
    total_premise_literal_storage: int
    gross_weighted_round_saving: Fraction
    max_selected_fan_in: int

    @property
    def selected_fraction(self) -> Fraction:
        if self.total_available_circuits == 0:
            return Fraction(0)
        return Fraction(self.selected_circuits, self.total_available_circuits)


def _build_plan(
    host_height: int,
    selected_counts: Mapping[CircuitType, int],
    frequencies: Mapping[CircuitType, Fraction],
    *,
    eligible_types: Mapping[CircuitType, int],
) -> SelectiveMaterializationPlan:
    chosen = []
    for (width, depth), available in sorted(
        eligible_types.items(),
        key=lambda item: (item[0][1], item[0][0]),
    ):
        selected = int(selected_counts.get((width, depth), 0))
        if selected < 0 or selected > available:
            raise AssertionError("selected circuit count escaped type capacity")
        if selected == 0:
            continue
        frequency = frequencies[(width, depth)]
        chosen.append(
            MaterializedCircuitType(
                premise_width=width,
                base_depth=depth,
                available_count=available,
                selected_count=selected,
                frequency_per_circuit=frequency,
                benefit_per_circuit=per_circuit_benefit((width, depth), frequency),
            )
        )
    return SelectiveMaterializationPlan(
        host_height=host_height,
        selected=tuple(chosen),
        total_available_circuits=sum(eligible_types.values()),
        selected_circuits=sum(item.selected_count for item in chosen),
        total_rule_storage=sum(item.rule_storage for item in chosen),
        total_premise_literal_storage=sum(item.premise_literal_storage for item in chosen),
        gross_weighted_round_saving=sum((item.total_benefit for item in chosen), Fraction(0)),
        max_selected_fan_in=max((item.premise_width for item in chosen), default=0),
    )


def optimal_unit_rule_budget_plan(
    host_height: int,
    rule_budget: int,
    *,
    max_fan_in: int | None = None,
    frequencies: Mapping[CircuitType, int | Fraction] | None = None,
) -> SelectiveMaterializationPlan:
    h = _positive_int(host_height, name="host_height")
    budget = _positive_int(rule_budget, name="rule_budget")
    types = rooted_circuit_types(h)
    if max_fan_in is not None:
        width_limit = _positive_int(max_fan_in, name="max_fan_in")
        types = {key: count for key, count in types.items() if key[0] <= width_limit}
    freq = type_frequency_map(h, frequencies)
    ranked = sorted(
        types.items(),
        key=lambda item: (
            -per_circuit_benefit(item[0], freq[item[0]]),
            item[0][0],      # narrower premise first on benefit ties
            -item[0][1],     # then deeper base circuit
        ),
    )
    remaining = budget
    selected: dict[CircuitType, int] = {}
    for key, available in ranked:
        if remaining <= 0:
            break
        benefit = per_circuit_benefit(key, freq[key])
        if benefit <= 0:
            break
        count = min(available, remaining)
        selected[key] = count
        remaining -= count
    return _build_plan(h, selected, freq, eligible_types=types)


def _bounded_knapsack_items(
    types: Mapping[CircuitType, int],
    frequencies: Mapping[CircuitType, Fraction],
) -> tuple[tuple[int, Fraction, CircuitType, int], ...]:
    """Binary-decompose identical candidates into O(log multiplicity) bundles."""
    bundles = []
    for key, multiplicity in types.items():
        width, _depth = key
        benefit = per_circuit_benefit(key, frequencies[key])
        if benefit <= 0:
            continue
        remaining = multiplicity
        chunk = 1
        while remaining > 0:
            take = min(chunk, remaining)
            bundles.append((width * take, benefit * take, key, take))
            remaining -= take
            chunk <<= 1
    return tuple(bundles)


def optimal_premise_literal_budget_plan(
    host_height: int,
    premise_literal_budget: int,
    *,
    max_fan_in: int | None = None,
    frequencies: Mapping[CircuitType, int | Fraction] | None = None,
) -> SelectiveMaterializationPlan:
    h = _positive_int(host_height, name="host_height")
    budget = _positive_int(premise_literal_budget, name="premise_literal_budget")
    types = rooted_circuit_types(h)
    if max_fan_in is not None:
        width_limit = _positive_int(max_fan_in, name="max_fan_in")
        types = {key: count for key, count in types.items() if key[0] <= width_limit}
    freq = type_frequency_map(h, frequencies)
    bundles = _bounded_knapsack_items(types, freq)

    # dp[cost] = (benefit, selected_counts).  Keep the best exact-cost state;
    # later select the best benefit over all costs <= budget, breaking ties by
    # lower cost and then narrower selected maximum fan-in through plan ordering.
    dp: dict[int, tuple[Fraction, dict[CircuitType, int]]] = {0: (Fraction(0), {})}
    for bundle_cost, bundle_benefit, key, take in bundles:
        previous = tuple(dp.items())
        for cost, (benefit, counts) in previous:
            new_cost = cost + bundle_cost
            if new_cost > budget:
                continue
            new_benefit = benefit + bundle_benefit
            current = dp.get(new_cost)
            if current is not None and current[0] >= new_benefit:
                continue
            updated = dict(counts)
            updated[key] = updated.get(key, 0) + take
            dp[new_cost] = (new_benefit, updated)

    best_cost, (best_benefit, best_counts) = min(
        dp.items(),
        key=lambda item: (-item[1][0], item[0]),
    )
    plan = _build_plan(h, best_counts, freq, eligible_types=types)
    if plan.total_premise_literal_storage != best_cost:
        raise AssertionError("knapsack plan cost disagreed with selected premise literals")
    if plan.gross_weighted_round_saving != best_benefit:
        raise AssertionError("knapsack plan benefit disagreed with DP objective")
    return plan


def rooted_circuit_minimal_premises_form_antichain(tree: AndTree, node: str) -> bool:
    circuits = enumerate_rooted_circuit_premises(tree, node)
    for index, left in enumerate(circuits):
        for right in circuits[index + 1 :]:
            if left < right or right < left:
                raise AssertionError("distinct rooted circuits violated inclusion antichain property")
    return True
