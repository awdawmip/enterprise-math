"""Canonical continuation closure from sufficient readouts to executable state.

For one coefficient semiring K and relation family, let C_K(P) be the unique
coarsest K-stable refinement of partition P.  If

    E = C_K(P_0)

and an intermediate partition T satisfies

    E refines T refines P_0,

then

    C_K(T) = E.

The proof is purely order-theoretic:

* E is K-stable and refines T, so E refines the coarsest stable refinement C_K(T);
* C_K(T) is K-stable and refines P_0, so by coarseness of E=C_K(P_0), C_K(T)
  refines E.

Hence equality.

A terminal trace partition is a canonical intermediate T: stable branching
signatures deterministically project to all terminal traces, so branching state
refines trace equivalence; the empty word keeps trace equivalence inside the
initial observation partition.  Closing the trace answer under the transition
interface therefore recovers the same minimal branching state.

This yields an exact **continuation debt**:

    #blocks(branching state) - #blocks(trace answer).

It measures additional state distinctions required solely to make the answer
recursively executable as a future state.

The theorem is coefficient-interface generic.  Owner regressions instantiate it
for exact natural-count traces and Boolean-support traces, including the existing
correlation/choice-timing witnesses where terminal answers are strictly coarser
than branching state.

Closure operators and stable partition refinement are standard prior
mathematics/CS.  The project value is the exact answer-to-state repair theorem
and continuation-debt interpretation.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Hashable, Mapping, Sequence

from .admissible_support import Relation
from .relation_branching_semiring import SemiringSpec, natural_semiring
from .relation_semiring_stable_refinement import (
    SharedSemiringRefinementReport,
    coarsest_shared_semiring_refinement,
)
from .relation_support_stable_refinement import (
    Partition,
    normalize_partition,
    partition_from_observation,
    partition_refines,
)
from .relation_terminal_count_trace_certificate import (
    exact_infinite_terminal_trace_partition,
)


State = Hashable
Action = Hashable
Observation = Hashable


def partition_between(
    finer: Sequence[Sequence[State] | frozenset[State]],
    middle: Sequence[Sequence[State] | frozenset[State]],
    coarser: Sequence[Sequence[State] | frozenset[State]],
) -> bool:
    fine = normalize_partition(finer)
    mid = normalize_partition(middle)
    coarse = normalize_partition(coarser)
    return partition_refines(fine, mid) and partition_refines(mid, coarse)


def stable_closure_absorbs_intermediate_partition(
    initial_partition: Sequence[Sequence[State] | frozenset[State]],
    intermediate_partition: Sequence[Sequence[State] | frozenset[State]],
    relations: Mapping[Action, Relation],
    semiring: SemiringSpec,
) -> bool:
    initial = normalize_partition(initial_partition)
    intermediate = normalize_partition(intermediate_partition)
    initial_report = coarsest_shared_semiring_refinement(
        initial,
        relations,
        (semiring,),
    )
    final = initial_report.final_partition
    if not partition_between(final, intermediate, initial):
        raise ValueError(
            "intermediate partition must lie between the stable state and initial partition"
        )
    repaired = coarsest_shared_semiring_refinement(
        intermediate,
        relations,
        (semiring,),
    )
    if repaired.final_partition != final:
        raise AssertionError("stable closure failed interval-absorption theorem")
    return True


@dataclass(frozen=True)
class ContinuationDebtReport:
    semiring_name: str
    initial_partition: Partition
    answer_partition: Partition
    executable_state_partition: Partition
    repair_steps: tuple[Partition, ...]

    @property
    def answer_block_count(self) -> int:
        return len(self.answer_partition)

    @property
    def state_block_count(self) -> int:
        return len(self.executable_state_partition)

    @property
    def extra_state_blocks(self) -> int:
        return self.state_block_count - self.answer_block_count

    @property
    def strict_repair_rounds(self) -> int:
        return len(self.repair_steps) - 1

    @property
    def has_continuation_debt(self) -> bool:
        return self.extra_state_blocks > 0


def continuation_debt_report(
    initial_partition: Sequence[Sequence[State] | frozenset[State]],
    answer_partition: Sequence[Sequence[State] | frozenset[State]],
    relations: Mapping[Action, Relation],
    semiring: SemiringSpec,
) -> ContinuationDebtReport:
    initial = normalize_partition(initial_partition)
    answer = normalize_partition(answer_partition)
    state_report = coarsest_shared_semiring_refinement(
        initial,
        relations,
        (semiring,),
    )
    state_partition = state_report.final_partition
    if not partition_between(state_partition, answer, initial):
        raise ValueError(
            "answer partition must be coarser than executable state and refine initial observation"
        )
    repair = coarsest_shared_semiring_refinement(
        answer,
        relations,
        (semiring,),
    )
    if repair.final_partition != state_partition:
        raise AssertionError("answer-to-state repair failed canonical closure theorem")
    return ContinuationDebtReport(
        semiring_name=semiring.name,
        initial_partition=initial,
        answer_partition=answer,
        executable_state_partition=state_partition,
        repair_steps=repair.steps,
    )


def exact_count_trace_to_state_report(
    states: Sequence[State],
    relations: Mapping[Action, Relation],
    observation: Callable[[State], Observation],
) -> ContinuationDebtReport:
    initial = partition_from_observation(states, observation)
    trace = exact_infinite_terminal_trace_partition(
        states,
        relations,
        observation,
    )
    return continuation_debt_report(
        initial,
        trace,
        relations,
        natural_semiring(),
    )
