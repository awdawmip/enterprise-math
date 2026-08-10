"""Structure-first compiler from local branching precision to exact infinite traces.

Exact count-stable branching equivalence is an equitable weighted quotient.  If
E is stable, then for every action a, source block D and target block C the
number

    B_a[C,D] = #{ y in C : x R_a y },  x in D,

is independent of the representative x.  The matrices B_a therefore define an
exact finite weighted quotient transition system.

Every raw natural path-count trace factors exactly through this quotient.  The
full infinite terminal trace-equivalence problem can consequently be solved on
b quotient states instead of n raw states.

The finite count-branching cutoff theorem adds a stronger compiler fact.  If M
exceeds the maximum raw outdegree Delta, mod-M branching refinement is identical
to exact-N branching.  Every modular target-block coefficient is the residue of
an integer in 0..Delta, so it uniquely lifts back to that exact local count.
Hence one can recover the exact weighted quotient from small local modular
precision and then perform arbitrary exact integer/rational trace calculations
offline.

This yields two different exact routes:

* direct flattened trace observation: coefficient modulus may need to reflect
  counts as large as Delta^h;
* structure-first branching compiler: local modulus only needs M>Delta, after
  which exact weighted continuation reconstructs the entire infinite trace
  language.

Equitable partitions, lumping and weighted automata quotients are standard prior
mathematics/CS.  The project value is the exact arithmetic-range/structural-state
tradeoff and the finite compiler between the two interfaces.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Hashable, Mapping, Sequence

from .admissible_support import Relation
from .relation_branching_count_cutoff import (
    relation_max_outdegree,
    universal_exact_count_branching_modulus,
)
from .relation_branching_semiring import modular_semiring, natural_semiring
from .relation_semiring_stable_refinement import (
    coarsest_shared_semiring_refinement,
    semiring_target_block_weights,
)
from .relation_support_stable_refinement import (
    Partition,
    normalize_partition,
    partition_from_observation,
)
from .relation_terminal_count_trace_certificate import (
    independent_integer_rows,
    observation_indicator_rows,
    partition_from_row_basis,
    rational_matrix_rank,
    row_times_matrix,
    exact_infinite_terminal_trace_partition,
)


State = Hashable
Action = Hashable
Observation = Hashable
Vector = tuple[int, ...]
Matrix = tuple[Vector, ...]


def _states(values: Sequence[State]) -> tuple[State, ...]:
    result = tuple(values)
    if not result or len(set(result)) != len(result):
        raise ValueError("states must be a nonempty distinct sequence")
    return result


def _family(
    states: tuple[State, ...],
    relations: Mapping[Action, Relation],
) -> dict[Action, Relation]:
    if not relations:
        raise ValueError("relation family must be nonempty")
    state_set = set(states)
    result: dict[Action, Relation] = {}
    for name, relation in relations.items():
        if not isinstance(relation, frozenset):
            raise TypeError("every relation must be a frozenset of ordered pairs")
        if any(source not in state_set or target not in state_set for source, target in relation):
            raise ValueError("relation contains state outside declared state set")
        result[name] = relation
    return result


def observation_labels_for_blocks(
    partition: Partition,
    observation: Callable[[State], Observation],
) -> tuple[Observation, ...]:
    current = normalize_partition(partition)
    labels = []
    for block in current:
        values = {observation(state) for state in block}
        if len(values) != 1:
            raise ValueError("quotient partition must refine current observation")
        label = next(iter(values))
        hash(label)
        labels.append(label)
    return tuple(labels)


def exact_count_branching_partition(
    states: Sequence[State],
    relations: Mapping[Action, Relation],
    observation: Callable[[State], Observation],
) -> Partition:
    order = _states(states)
    family = _family(order, relations)
    initial = partition_from_observation(order, observation)
    return coarsest_shared_semiring_refinement(
        initial,
        family,
        (natural_semiring(),),
    ).final_partition


def exact_weighted_quotient_matrices(
    states: Sequence[State],
    relations: Mapping[Action, Relation],
    partition: Sequence[Sequence[State] | frozenset[State]],
) -> dict[Action, Matrix]:
    order = _states(states)
    family = _family(order, relations)
    current = normalize_partition(partition)
    if frozenset().union(*current) != frozenset(order):
        raise ValueError("partition must cover exactly the declared states")
    block_count = len(current)
    matrices: dict[Action, Matrix] = {}
    for name in sorted(family, key=repr):
        relation = family[name]
        columns: list[Vector] = []
        for source_block in current:
            representatives = tuple(source_block)
            if not representatives:
                raise AssertionError("normalized partition contained empty block")
            vectors = []
            for source in representatives:
                sparse = dict(
                    semiring_target_block_weights(
                        current,
                        relation,
                        source,
                        natural_semiring(),
                    )
                )
                vectors.append(
                    tuple(int(sparse.get(target_block, 0)) for target_block in range(block_count))
                )
            if len(set(vectors)) != 1:
                raise ValueError("partition is not exact-count stable for this relation")
            columns.append(vectors[0])
        matrices[name] = tuple(
            tuple(columns[source][target] for source in range(block_count))
            for target in range(block_count)
        )
    return matrices


def lift_modular_weight(residue: int, modulus: int, max_outdegree: int) -> int:
    if isinstance(residue, bool) or not isinstance(residue, int):
        raise TypeError("residue must be an integer")
    if isinstance(modulus, bool) or not isinstance(modulus, int):
        raise TypeError("modulus must be an integer")
    if isinstance(max_outdegree, bool) or not isinstance(max_outdegree, int):
        raise TypeError("max_outdegree must be an integer")
    if modulus <= max_outdegree:
        raise ValueError("unique local lift requires modulus > maximum outdegree")
    if not 0 <= residue < modulus:
        raise ValueError("residue must be the canonical representative modulo modulus")
    if residue > max_outdegree:
        raise ValueError("residue cannot arise from one raw target-block count under the bound")
    return residue


def lifted_modular_weighted_quotient_matrices(
    states: Sequence[State],
    relations: Mapping[Action, Relation],
    observation: Callable[[State], Observation],
    modulus: int,
) -> tuple[Partition, dict[Action, Matrix]]:
    """Recover exact local quotient weights from an M>Delta modular branching world."""
    order = _states(states)
    family = _family(order, relations)
    delta = relation_max_outdegree(order, family)
    if isinstance(modulus, bool) or not isinstance(modulus, int):
        raise TypeError("modulus must be an integer")
    if modulus <= delta:
        raise ValueError("structure-first exact lift requires modulus > maximum outdegree")

    initial = partition_from_observation(order, observation)
    modular_partition = coarsest_shared_semiring_refinement(
        initial,
        family,
        (modular_semiring(modulus),),
    ).final_partition
    block_count = len(modular_partition)
    matrices: dict[Action, Matrix] = {}

    for name in sorted(family, key=repr):
        relation = family[name]
        columns: list[Vector] = []
        for source_block in modular_partition:
            vectors = []
            for source in source_block:
                sparse = dict(
                    semiring_target_block_weights(
                        modular_partition,
                        relation,
                        source,
                        modular_semiring(modulus),
                    )
                )
                vector = tuple(
                    lift_modular_weight(
                        int(sparse.get(target_block, 0)),
                        modulus,
                        delta,
                    )
                    for target_block in range(block_count)
                )
                vectors.append(vector)
            if len(set(vectors)) != 1:
                raise AssertionError("modular stable quotient lost representative independence")
            columns.append(vectors[0])
        matrices[name] = tuple(
            tuple(columns[source][target] for source in range(block_count))
            for target in range(block_count)
        )

    exact_partition = exact_count_branching_partition(order, family, observation)
    if modular_partition != exact_partition:
        raise AssertionError("M>Delta modular branching partition failed exact count cutoff")
    exact_matrices = exact_weighted_quotient_matrices(order, family, exact_partition)
    if matrices != exact_matrices:
        raise AssertionError("small-modulus local lift failed to reconstruct exact quotient weights")
    return modular_partition, matrices


def quotient_observation_indicator_rows(
    partition: Partition,
    observation: Callable[[State], Observation],
) -> Matrix:
    labels = observation_labels_for_blocks(partition, observation)
    ordered_labels: list[Observation] = []
    seen: set[Observation] = set()
    for label in labels:
        if label not in seen:
            seen.add(label)
            ordered_labels.append(label)
    return tuple(
        tuple(int(label == observed) for label in labels)
        for observed in ordered_labels
    )


@dataclass(frozen=True)
class QuotientTraceClosureReport:
    quotient_state_count: int
    observation_rank: int
    theorem_horizon_bound: int
    stabilization_horizon: int
    final_basis_rows: Matrix


def quotient_trace_closure_report(
    quotient_matrices: Mapping[Action, Matrix],
    observation_rows: Matrix,
) -> QuotientTraceClosureReport:
    if not quotient_matrices:
        raise ValueError("quotient matrix family must be nonempty")
    actions = tuple(quotient_matrices[name] for name in sorted(quotient_matrices, key=repr))
    dimension = len(actions[0])
    if dimension == 0 or any(
        len(matrix) != dimension
        or any(len(row) != dimension for row in matrix)
        for matrix in actions
    ):
        raise ValueError("quotient action matrices must share one positive square dimension")
    if not observation_rows or any(len(row) != dimension for row in observation_rows):
        raise ValueError("quotient observation rows must match quotient dimension")

    basis = independent_integer_rows(observation_rows)
    initial_rank = len(basis)
    horizon_bound = dimension - initial_rank
    horizon = 0
    while True:
        previous = basis
        generated = list(previous)
        generated.extend(
            row_times_matrix(row, action)
            for row in previous
            for action in actions
        )
        basis = independent_integer_rows(generated)
        if len(basis) == len(previous):
            if horizon > horizon_bound:
                raise AssertionError("quotient trace closure exceeded dimension bound")
            return QuotientTraceClosureReport(
                quotient_state_count=dimension,
                observation_rank=initial_rank,
                theorem_horizon_bound=horizon_bound,
                stabilization_horizon=horizon,
                final_basis_rows=previous,
            )
        horizon += 1
        if horizon > horizon_bound:
            raise AssertionError("quotient trace row space exceeded finite rank budget")


def pullback_quotient_partition(
    raw_partition: Partition,
    quotient_partition: Partition,
) -> Partition:
    raw = normalize_partition(raw_partition)
    quotient = normalize_partition(quotient_partition)
    quotient_indices = frozenset().union(*quotient)
    if quotient_indices != frozenset(range(len(raw))):
        raise ValueError("quotient partition must be a partition of raw block indices")
    result = []
    for quotient_block in quotient:
        states: set[State] = set()
        for index in quotient_block:
            states.update(raw[index])
        result.append(states)
    return normalize_partition(tuple(result))


@dataclass(frozen=True)
class StructureFirstTraceCompilerReport:
    raw_state_count: int
    maximum_outdegree: int
    local_exact_modulus: int
    branching_partition: Partition
    branching_state_count: int
    raw_trace_horizon_bound: int
    quotient_trace_horizon_bound: int
    quotient_trace_stabilization_horizon: int
    exact_trace_partition_from_quotient: Partition
    direct_exact_trace_partition: Partition
    exact_quotient_matrices: tuple[tuple[Action, Matrix], ...]

    @property
    def structure_first_exact(self) -> bool:
        return self.exact_trace_partition_from_quotient == self.direct_exact_trace_partition

    @property
    def dimension_reduction(self) -> int:
        return self.raw_state_count - self.branching_state_count


def structure_first_trace_compiler_report(
    states: Sequence[State],
    relations: Mapping[Action, Relation],
    observation: Callable[[State], Observation],
    modulus: int | None = None,
) -> StructureFirstTraceCompilerReport:
    order = _states(states)
    family = _family(order, relations)
    delta = relation_max_outdegree(order, family)
    local_modulus = (
        universal_exact_count_branching_modulus(delta)
        if modulus is None
        else modulus
    )
    branching_partition, quotient_matrices = lifted_modular_weighted_quotient_matrices(
        order,
        family,
        observation,
        local_modulus,
    )
    quotient_observations = quotient_observation_indicator_rows(
        branching_partition,
        observation,
    )
    quotient_closure = quotient_trace_closure_report(
        quotient_matrices,
        quotient_observations,
    )
    quotient_trace_partition = partition_from_row_basis(
        tuple(range(len(branching_partition))),
        quotient_closure.final_basis_rows,
    )
    pulled_back = pullback_quotient_partition(
        branching_partition,
        quotient_trace_partition,
    )
    direct = exact_infinite_terminal_trace_partition(order, family, observation)
    if pulled_back != direct:
        raise AssertionError("exact terminal trace partition failed weighted quotient factorization")

    raw_observation_rank = len(observation_indicator_rows(order, observation))
    return StructureFirstTraceCompilerReport(
        raw_state_count=len(order),
        maximum_outdegree=delta,
        local_exact_modulus=local_modulus,
        branching_partition=branching_partition,
        branching_state_count=len(branching_partition),
        raw_trace_horizon_bound=len(order) - raw_observation_rank,
        quotient_trace_horizon_bound=quotient_closure.theorem_horizon_bound,
        quotient_trace_stabilization_horizon=quotient_closure.stabilization_horizon,
        exact_trace_partition_from_quotient=pulled_back,
        direct_exact_trace_partition=direct,
        exact_quotient_matrices=tuple(
            (name, quotient_matrices[name])
            for name in sorted(quotient_matrices, key=repr)
        ),
    )
