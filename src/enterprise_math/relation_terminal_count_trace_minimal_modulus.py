"""Finite search for the least modulus reproducing exact terminal-trace state precision.

The companion finite-certificate theorem provides one guaranteed modulus

    M > Delta^h_*

where h_* is the rational trace-closure horizon.  That is a safe coefficient
reflection bound, not necessarily the least modulus whose **state partition**
agrees with the infinite exact natural-count trace language.

For one fixed finite relation system, search from M=2 up to the guaranteed bound
and return the first modular trace partition through h_* equal to the exact
infinite partition.  The search is finite by theorem.

A small modulus can suffice even if some exact path-count coefficients collide
modulo M, provided those collisions never merge two states that exact traces need
to distinguish.  This is the terminal-trace analogue of realized versus uniform
precision in the count-branching cutoff generation.
"""

from __future__ import annotations

from typing import Callable, Hashable, Mapping, Sequence

from .admissible_support import Relation
from .relation_branching_vs_trace_cutoff import modular_terminal_trace_partition
from .relation_terminal_count_trace_certificate import (
    exact_infinite_terminal_trace_partition,
    finite_trace_certificate_modulus,
    rational_terminal_trace_closure_report,
)


State = Hashable
Action = Hashable
Observation = Hashable


def minimal_exact_terminal_trace_modulus(
    states: Sequence[State],
    relations: Mapping[Action, Relation],
    observation: Callable[[State], Observation],
) -> int:
    closure = rational_terminal_trace_closure_report(
        states,
        relations,
        observation,
    )
    exact = exact_infinite_terminal_trace_partition(
        states,
        relations,
        observation,
    )
    upper = finite_trace_certificate_modulus(
        states,
        relations,
        observation,
    )
    for modulus in range(2, upper + 1):
        modular = modular_terminal_trace_partition(
            states,
            relations,
            observation,
            closure.stabilization_horizon,
            modulus,
        )
        if modular == exact:
            return modulus
    raise AssertionError("guaranteed terminal trace modulus failed finite search")
