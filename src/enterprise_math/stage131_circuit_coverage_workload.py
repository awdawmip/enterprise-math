"""Weighted coverage interaction for rooted-circuit materialization workloads.

For arbitrary seed-set queries S, several rooted-circuit premises can be
contained in S simultaneously.  If selected circuits all conclude the same root
and are used only as one-round root shortcuts, total materialization value is
exact weighted coverage:

    F(A) = sum_S f(S) * max(d0(S)-1, 0)
                     * 1{exists P in A with P subseteq S}.

Thus F is monotone submodular.  Exact minimal-premise workloads are the modular
special case for positive-saving queries: distinct inclusion-minimal premises
form an antichain, so a query of depth>1 is covered only by its own circuit.
Depth-one local rules have zero materialization value and therefore no positive
coverage item.

This v2 replay makes that zero-benefit boundary explicit in the API.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations
from typing import Iterable, Mapping

from .stage131_horn_hyperedge_presentation import AndTree, horn_atom_set, horn_target_round
from .stage131_rooted_circuit_table_explosion import enumerate_rooted_circuit_premises

SeedSet = frozenset[str]
Circuit = frozenset[str]


@dataclass(frozen=True)
class RootSeedQuery:
    seeds: SeedSet
    frequency: Fraction
    base_root_depth: int

    @property
    def one_round_saving(self) -> int:
        return max(0, self.base_root_depth - 1)

    @property
    def weighted_cover_value(self) -> Fraction:
        return self.frequency * self.one_round_saving


def _tree_atoms(tree: AndTree) -> frozenset[str]:
    return horn_atom_set(tree.local_rules, tree.leaves)


def normalize_root_seed_workload(
    tree: AndTree,
    workload: Mapping[Iterable[str], int | Fraction],
) -> tuple[RootSeedQuery, ...]:
    atoms = _tree_atoms(tree)
    combined: dict[SeedSet, Fraction] = {}
    for raw_seeds, raw_frequency in workload.items():
        seeds = frozenset(raw_seeds)
        if not seeds.issubset(atoms):
            raise ValueError("workload seed set contains an atom outside the AND tree")
        frequency = Fraction(raw_frequency)
        if frequency < 0:
            raise ValueError("workload frequencies must be nonnegative")
        if frequency == 0:
            continue
        combined[seeds] = combined.get(seeds, Fraction(0)) + frequency
    if not combined:
        raise ValueError("workload must have positive total frequency")

    queries = []
    for seeds, frequency in sorted(
        combined.items(),
        key=lambda item: tuple(sorted(item[0])),
    ):
        depth = horn_target_round(tree.local_rules, seeds, tree.root)
        if depth is None:
            raise ValueError("every workload seed set must derive the declared root in the base law")
        queries.append(RootSeedQuery(seeds=seeds, frequency=frequency, base_root_depth=depth))
    return tuple(queries)


def rooted_circuit_candidates(tree: AndTree) -> tuple[Circuit, ...]:
    return tuple(enumerate_rooted_circuit_premises(tree, tree.root))


def circuit_covers_query(circuit: Circuit, query: RootSeedQuery) -> bool:
    return query.one_round_saving > 0 and circuit.issubset(query.seeds)


def circuit_coverage_indices(circuit: Circuit, queries: tuple[RootSeedQuery, ...]) -> frozenset[int]:
    return frozenset(index for index, query in enumerate(queries) if circuit_covers_query(circuit, query))


def covered_query_indices(selected: Iterable[Circuit], queries: tuple[RootSeedQuery, ...]) -> frozenset[int]:
    selected_values = tuple(selected)
    return frozenset(
        index
        for index, query in enumerate(queries)
        if any(circuit_covers_query(circuit, query) for circuit in selected_values)
    )


def coverage_benefit(selected: Iterable[Circuit], queries: tuple[RootSeedQuery, ...]) -> Fraction:
    return sum(
        (queries[index].weighted_cover_value for index in covered_query_indices(selected, queries)),
        Fraction(0),
    )


def marginal_coverage_gain(selected: Iterable[Circuit], candidate: Circuit, queries: tuple[RootSeedQuery, ...]) -> Fraction:
    selected_values = frozenset(selected)
    if candidate in selected_values:
        return Fraction(0)
    return coverage_benefit((*selected_values, candidate), queries) - coverage_benefit(selected_values, queries)


@dataclass(frozen=True)
class CoverageMaterializationPlan:
    selected: tuple[Circuit, ...]
    rule_budget: int
    gross_weighted_round_saving: Fraction
    covered_query_count: int
    total_query_count: int

    @property
    def selected_rule_count(self) -> int:
        return len(self.selected)


def greedy_coverage_materialization(
    tree: AndTree,
    workload: Mapping[Iterable[str], int | Fraction],
    rule_budget: int,
) -> CoverageMaterializationPlan:
    if isinstance(rule_budget, bool) or not isinstance(rule_budget, int) or rule_budget <= 0:
        raise ValueError("rule_budget must be a positive integer")
    queries = normalize_root_seed_workload(tree, workload)
    remaining = set(rooted_circuit_candidates(tree))
    selected: list[Circuit] = []

    for _ in range(min(rule_budget, len(remaining))):
        if not remaining:
            break
        scored = [
            (marginal_coverage_gain(selected, candidate, queries), len(candidate), tuple(sorted(candidate)), candidate)
            for candidate in remaining
        ]
        scored.sort(key=lambda item: (-item[0], item[1], item[2]))
        gain, _width, _label, best = scored[0]
        if gain <= 0:
            break
        selected.append(best)
        remaining.remove(best)

    covered = covered_query_indices(selected, queries)
    return CoverageMaterializationPlan(
        selected=tuple(selected),
        rule_budget=rule_budget,
        gross_weighted_round_saving=coverage_benefit(selected, queries),
        covered_query_count=len(covered),
        total_query_count=len(queries),
    )


def exact_coverage_materialization_small(
    tree: AndTree,
    workload: Mapping[Iterable[str], int | Fraction],
    rule_budget: int,
) -> CoverageMaterializationPlan:
    if isinstance(rule_budget, bool) or not isinstance(rule_budget, int) or rule_budget <= 0:
        raise ValueError("rule_budget must be a positive integer")
    queries = normalize_root_seed_workload(tree, workload)
    candidates = rooted_circuit_candidates(tree)
    if len(candidates) > 30 or rule_budget > 6:
        raise ValueError("exact coverage enumeration is limited to <=30 circuits and budget<=6")

    best_selected: tuple[Circuit, ...] = ()
    best_benefit = Fraction(0)
    for count in range(min(rule_budget, len(candidates)) + 1):
        for chosen in combinations(candidates, count):
            benefit = coverage_benefit(chosen, queries)
            if benefit > best_benefit or (benefit == best_benefit and len(chosen) < len(best_selected)):
                best_benefit = benefit
                best_selected = chosen
    covered = covered_query_indices(best_selected, queries)
    return CoverageMaterializationPlan(
        selected=tuple(best_selected),
        rule_budget=rule_budget,
        gross_weighted_round_saving=best_benefit,
        covered_query_count=len(covered),
        total_query_count=len(queries),
    )


def minimal_premise_workload(tree: AndTree, frequency: int | Fraction = 1) -> dict[Circuit, Fraction]:
    f = Fraction(frequency)
    if f <= 0:
        raise ValueError("frequency must be positive")
    return {circuit: f for circuit in rooted_circuit_candidates(tree)}


def positive_minimal_premise_workload_is_modular(tree: AndTree) -> bool:
    queries = normalize_root_seed_workload(tree, minimal_premise_workload(tree))
    by_seed = {query.seeds: index for index, query in enumerate(queries)}
    for circuit in rooted_circuit_candidates(tree):
        query = queries[by_seed[circuit]]
        covered = circuit_coverage_indices(circuit, queries)
        expected = frozenset() if query.one_round_saving == 0 else frozenset({by_seed[circuit]})
        if covered != expected:
            raise AssertionError("minimal-premise workload failed positive-value modular boundary")
    return True


def coverage_objective_is_monotone_submodular_exhaustive(
    tree: AndTree,
    workload: Mapping[Iterable[str], int | Fraction],
) -> bool:
    queries = normalize_root_seed_workload(tree, workload)
    candidates = rooted_circuit_candidates(tree)
    if len(candidates) > 12:
        raise ValueError("exhaustive submodularity audit is limited to <=12 circuits")
    subsets = tuple(
        frozenset(candidates[index] for index in range(len(candidates)) if (mask >> index) & 1)
        for mask in range(1 << len(candidates))
    )
    for left in subsets:
        for right in subsets:
            if not left.issubset(right):
                continue
            if coverage_benefit(left, queries) > coverage_benefit(right, queries):
                raise AssertionError("weighted coverage lost monotonicity")
            for candidate in candidates:
                if candidate in right:
                    continue
                if marginal_coverage_gain(left, candidate, queries) < marginal_coverage_gain(right, candidate, queries):
                    raise AssertionError("weighted coverage lost diminishing returns")
    return True
