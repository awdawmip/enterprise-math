"""Branching-state count precision versus accumulated terminal path-count precision.

For maximum raw outdegree Delta, exact count-branching refinement only ever
inspects one-step target-block counts in ``0..Delta``.  Hence any modulus
M>Delta reproduces the exact branching-state refinement at every depth.

Terminal path-count traces accumulate multiplicatively along a word.  Through
word horizon h, the total number of paths from one source is at most Delta^h
(for h=0 the empty path contributes one).  Therefore the simple uniform
coefficient-reflection bound for exact natural terminal count traces is

    M > max(1, Delta^h).

This is sufficient, not claimed minimal for a fixed world.  It can grow
exponentially with horizon even though the exact branching-state cutoff remains
Delta+1.

A sharp finite-world separation occurs already at Delta=2 and M=3.  Two sources
both have two first-step successors.  One source's children each have outdegree
2, giving four length-two paths; the other's children have outdegrees 1 and 0,
giving one length-two path.  Exact terminal counts distinguish 4 from 1, while
mod3 traces merge them forever in the acyclic fixture.  Nevertheless mod3
branching signatures distinguish the different successor behavioural types and
exactly match natural-count branching.

This shows that arithmetic precision for a compositional state and arithmetic
precision for an accumulated trace value are different resources.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Hashable, Mapping, Sequence

from .admissible_support import Relation
from .relation_branching_count_cutoff import (
    count_branching_cutoff_report,
    relation_max_outdegree,
    universal_exact_count_branching_modulus,
)
from .relation_branching_semiring import (
    modular_semiring,
    natural_semiring,
    raw_semiring_word_trace,
    words_through_horizon,
)
from .relation_support_stable_refinement import Partition, normalize_partition


State = Hashable
Action = Hashable
Observation = Hashable


def finite_horizon_path_count_bound(max_outdegree: int, horizon: int) -> int:
    if isinstance(max_outdegree, bool) or not isinstance(max_outdegree, int):
        raise TypeError("max_outdegree must be an integer")
    if max_outdegree < 0:
        raise ValueError("max_outdegree must be nonnegative")
    if isinstance(horizon, bool) or not isinstance(horizon, int):
        raise TypeError("horizon must be an integer")
    if horizon < 0:
        raise ValueError("horizon must be nonnegative")
    return max(1, max_outdegree**horizon)


def universal_finite_horizon_trace_modulus(
    max_outdegree: int,
    horizon: int,
) -> int:
    """One modulus reflecting every possible terminal count through horizon h."""
    bound = finite_horizon_path_count_bound(max_outdegree, horizon)
    return max(2, bound + 1)


def semiring_terminal_trace_partition(
    states: Sequence[State],
    relations: Mapping[Action, Relation],
    observation: Callable[[State], Observation],
    horizon: int,
    semiring,
) -> Partition:
    order = tuple(states)
    if not order or len(set(order)) != len(order):
        raise ValueError("states must be a nonempty distinct sequence")
    if not relations:
        raise ValueError("relation family must be nonempty")
    if isinstance(horizon, bool) or not isinstance(horizon, int):
        raise TypeError("horizon must be an integer")
    if horizon < 0:
        raise ValueError("horizon must be nonnegative")
    words = words_through_horizon(tuple(relations), horizon)
    groups: dict[tuple[object, ...], set[State]] = {}
    for source in order:
        signature = tuple(
            (
                word,
                frozenset(
                    raw_semiring_word_trace(
                        order,
                        relations,
                        observation,
                        source,
                        word,
                        semiring,
                    ).items()
                ),
            )
            for word in words
        )
        groups.setdefault(signature, set()).add(source)
    return normalize_partition(tuple(groups.values()))


def natural_terminal_trace_partition(
    states: Sequence[State],
    relations: Mapping[Action, Relation],
    observation: Callable[[State], Observation],
    horizon: int,
) -> Partition:
    return semiring_terminal_trace_partition(
        states,
        relations,
        observation,
        horizon,
        natural_semiring(),
    )


def modular_terminal_trace_partition(
    states: Sequence[State],
    relations: Mapping[Action, Relation],
    observation: Callable[[State], Observation],
    horizon: int,
    modulus: int,
) -> Partition:
    if isinstance(modulus, bool) or not isinstance(modulus, int):
        raise TypeError("modulus must be an integer")
    if modulus <= 1:
        raise ValueError("modulus must exceed one")
    return semiring_terminal_trace_partition(
        states,
        relations,
        observation,
        horizon,
        modular_semiring(modulus),
    )


def finite_horizon_trace_exact_above_path_count_bound(
    states: Sequence[State],
    relations: Mapping[Action, Relation],
    observation: Callable[[State], Observation],
    horizon: int,
    modulus: int,
) -> bool:
    delta = relation_max_outdegree(states, relations)
    bound = finite_horizon_path_count_bound(delta, horizon)
    if isinstance(modulus, bool) or not isinstance(modulus, int):
        raise TypeError("modulus must be an integer")
    if modulus <= bound:
        raise ValueError("the theorem requires modulus above the finite-horizon path-count bound")
    exact = natural_terminal_trace_partition(
        states,
        relations,
        observation,
        horizon,
    )
    modular = modular_terminal_trace_partition(
        states,
        relations,
        observation,
        horizon,
        modulus,
    )
    if exact != modular:
        raise AssertionError("M>Delta^h failed finite-horizon exact trace reflection")
    return True


def branching_trace_gap_fixture() -> tuple[
    tuple[str, ...],
    dict[str, Relation],
    Callable[[str], str],
]:
    """Delta=2 world: mod3 exact for branching state, not exact for count traces."""
    states = (
        "p",
        "q",
        "u1",
        "u2",
        "v1",
        "v0",
        "z1",
        "z2",
    )
    relation = frozenset(
        {
            ("p", "u1"),
            ("p", "u2"),
            ("q", "v1"),
            ("q", "v0"),
            ("u1", "z1"),
            ("u1", "z2"),
            ("u2", "z1"),
            ("u2", "z2"),
            ("v1", "z1"),
            # v0 and terminals have no outgoing a-edge.
        }
    )
    return states, {"a": relation}, lambda _state: "visible"


@dataclass(frozen=True)
class BranchingVersusTraceCutoffReport:
    maximum_outdegree: int
    branching_cutoff_modulus: int
    trace_horizon: int
    simple_trace_cutoff_modulus: int
    tested_modulus: int
    exact_branching_partition: Partition
    modular_branching_partition: Partition
    exact_trace_partition: Partition
    modular_trace_partition: Partition

    @property
    def branching_exact(self) -> bool:
        return self.exact_branching_partition == self.modular_branching_partition

    @property
    def trace_exact(self) -> bool:
        return self.exact_trace_partition == self.modular_trace_partition


def branching_versus_trace_cutoff_report(
    states: Sequence[State],
    relations: Mapping[Action, Relation],
    observation: Callable[[State], Observation],
    trace_horizon: int,
    modulus: int,
) -> BranchingVersusTraceCutoffReport:
    delta = relation_max_outdegree(states, relations)
    branch_report = count_branching_cutoff_report(
        states,
        relations,
        observation,
        modulus,
    )
    exact_trace = natural_terminal_trace_partition(
        states,
        relations,
        observation,
        trace_horizon,
    )
    modular_trace = modular_terminal_trace_partition(
        states,
        relations,
        observation,
        trace_horizon,
        modulus,
    )
    return BranchingVersusTraceCutoffReport(
        maximum_outdegree=delta,
        branching_cutoff_modulus=universal_exact_count_branching_modulus(delta),
        trace_horizon=trace_horizon,
        simple_trace_cutoff_modulus=universal_finite_horizon_trace_modulus(
            delta,
            trace_horizon,
        ),
        tested_modulus=modulus,
        exact_branching_partition=branch_report.exact_steps[-1],
        modular_branching_partition=branch_report.modular_steps[-1],
        exact_trace_partition=exact_trace,
        modular_trace_partition=modular_trace,
    )
