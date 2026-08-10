"""Weighted coverage interaction for rooted-circuit materialization workloads.

The parent selective compiler is additive when the workload consists exactly of
inclusion-minimal rooted-circuit premise sets.  Distinct minimal premises form an
antichain, so one circuit cannot fire on another minimal premise query.

For arbitrary seed-set queries S, several rooted circuits can satisfy P subseteq
S simultaneously.  If every materialized circuit concludes the same root and is
used only as a one-round root shortcut, then selecting any one applicable
circuit reduces that query's root depth to one.  The total materialization value
is therefore the weighted coverage function

    F(A) = sum_S f(S) * (d0(S)-1)
                     * 1{ exists P in A with P subseteq S }.

Here d0(S) is the root depth under the local Horn basis.  Weighted coverage is
monotone and submodular.  The exact-minimal-premise workload is the modular
special case in which every query is covered by exactly one circuit.

This layer deliberately keeps circuits root-only.  If macros can derive
intermediate nodes and compose with one another, the objective moves beyond
ordinary coverage into reusable proof-DAG / closure interactions.
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
    for seeds, frequency in sorted(combined.items(), key=lambda item: tuple(sorted(item[0]))):
        depth = horn_target_round(tree.local_rules, seeds, tree.root)
        if depth is None:
            raise ValueError("every workload seed set must derive the declared root in the base law")
        queries.append(RootSeedQuery(seeds=seeds, frequency=frequency, base_root_depth=depth))
    return tuple(queries)


def rooted_circuit_candidates(tree: AndTree) -> tuple[Circuit, ...]:
    return tuple(enumerate_rooted_circuit_premises(tree, tree.root))


def circuit_covers_query(circuit: Circuit, query: RootSeedQuery) -> bool:
    return circuit.issubset(query.seeds) and query.one_round_saving > 0


def circuit_coverage_indices(
    circuit: Circuit,
    queries: tuple[RootSeedQuery, ...],
) -> frozenset[int]:
    return frozenset(index for index, query in enumerate(queries) if circuit_covers_query(circuit, query))


def covered_query_indices(
    selected: Iterable[Circuit],
    queries: tuple[RootSeedQuery, ...],
) -> frozenset[int]:
    selected_values = tuple(selected)
    return frozenset(
        index
        for index, query in enumerate(queries)
        if any(circuit_covers_query(circuit, query) for circuit in selected_values)
    )


def coverage_benefit(
    selected: Iterable[Circuit],
    queries: tuple[RootSeedQuery, ...],
) -> Fraction:
    return sum(
        (queries[index].weighted_cover_value for index in covered_query_indices(selected, queries)),
        Fraction(0),
    )


def marginal_coverage_gain(
    selected: Iterable[Circuit],
    candidate: Circuit,
    queries: tuple[RootSeedQuery, ...],
) -> Fraction:
    selected_values = frozenset(selected)
    if candidate in selected_values:
        return Fraction(0)
    before = coverage_benefit(selected_values, queries)
    after = coverage_benefit((*selected_values, candidate), queries)
    return after - before


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
    candidates = rooted_circuit_candidates(tree)
    selected: list[Circuit] = []
    remaining = set(candidates)

    for _ in range(min(rule_budget, len(candidates))):
        scored = tuple(
            (marginal_coverage_gain(selected, candidate, queries), len(candidate), tuple(sorted(candidate)), candidate)
            for candidate in remaining
        )
        if not scored:
            break
        gain, _width, _label, best = max(
            scored,
            key=lambda item: (item[0], -item[1], tuple(reversed(item[2]))),
        )
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
    max_count = min(rule_budget, len(candidates))
    for count in range(max_count + 1):
        for chosen in combinations(candidates, count):
            benefit = coverage_benefit(chosen, queries)
            key = (benefit, -len(chosen), tuple(sorted((tuple(sorted(c)) for c in chosen))))
            best_key = (best_benefit, -len(best_selected), tuple(sorted((tuple(sorted(c)) for c in best_selected))))
            if key > best_key:
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


def minimal_premise_workload_is_modular(tree: AndTree) -> bool:
    queries = normalize_root_seed_workload(tree, minimal_premise_workload(tree))
    candidates = rooted_circuit_candidates(tree)
    for circuit in candidates:
        covered = circuit_coverage_indices(circuit, queries)
        if len(covered) != 1:
            raise AssertionError("minimal-premise antichain workload failed singleton coverage")
    return True


def coverage_objective_is_monotone_submodular_exhaustive(
    tree: AndTree,
    workload: Mapping[Iterable[str], int | Fraction],
) -> bool:
    """Exhaustive finite check on tiny candidate families; theorem is weighted coverage."""
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
            if left.issubset(right):
                if coverage_benefit(left, queries) > coverage_benefit(right, queries):
                    raise AssertionError("weighted coverage lost monotonicity")
                for candidate in candidates:
                    if candidate in right:
                        continue
                    if marginal_coverage_gain(left, candidate, queries) < marginal_coverage_gain(right, candidate, queries):
                        raise AssertionError("weighted coverage lost diminishing returns")
    return True
