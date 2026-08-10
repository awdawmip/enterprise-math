"""Task-relative observability of guarded scheduler terminal relations.

For one prequantized whole-contact budget, guarded consume-until-stuck semantics
can produce a finite terminal relation of applied count vectors

    T = {n^(1),...,n^(m)}.

Scheduler nondeterminism is not automatically visible to every future task.
Choose one reference terminal ``n0`` and let

    L_sched = span_Z { n - n0 : n in T }.

For any integer linear readout ``A n``, the readout is scheduler-deterministic
exactly when

    L_sched subseteq ker A.

This specializes several layers already present in the E001 causal material
world:

* ``A=B`` tests whether body impulse after-state is scheduler-deterministic;
* ``A=C`` tests an applied-history witness;
* stacking rows of ``B`` and ``C`` tests their joint observable;
* exact whole queue ``Q'=U-n`` is injective in ``n``, so it is deterministic
  exactly when the terminal count relation itself is a singleton;
* committed history ``C(n+Q')=C U`` cancels the scheduler lattice structurally.

For a scalar witness row ``c``, terminal output differences generate the subgroup
``g_sched Z`` where

    g_sched = gcd { |c.(n-n0)| }.

Exact scalar history is deterministic iff ``g_sched=0``.  If the future only
observes that history modulo positive ``M``, one tick is deterministic iff every
terminal output has the same residue, equivalently ``M | g_sched`` (with zero
grain satisfying every modulus).  Under repeated composition of the generated
scheduler-difference subgroup, the modular ambiguity closure has exactly

    M / gcd(M, g_sched)

phases.

This is a finite E001 specialization of the same kernel principle used for cycle
history and P023 future-safe quotients: a branch relation survives only through
observables that do not kill its difference lattice.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import gcd
from typing import Sequence

from .contact_cycle_witness_repair import apply_integer_matrix
from .material_contact_causal_history_state import (
    HistoryAwareCausalTickRelation1D,
)
from .material_contact_tick_causal_queue import GuardedTerminalRelation


Vector = tuple[int, ...]
Matrix = tuple[tuple[int, ...], ...]


def _require_int(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f"{name} must be an integer")


def _matrix(values: Sequence[Sequence[int]], width: int) -> Matrix:
    rows = tuple(tuple(row) for row in values)
    if not rows:
        raise ValueError("observable matrix must contain at least one row")
    if any(len(row) != width for row in rows):
        raise ValueError("observable matrix must match terminal count dimension")
    for row in rows:
        for value in row:
            _require_int("observable entry", value)
    return rows


def terminal_applied_counts(
    relation: GuardedTerminalRelation,
) -> tuple[Vector, ...]:
    if not isinstance(relation, GuardedTerminalRelation):
        raise TypeError("relation must be GuardedTerminalRelation")
    return tuple(terminal.applied_counts for terminal in relation.terminals)


def scheduler_difference_generators(
    relation: GuardedTerminalRelation,
) -> tuple[Vector, ...]:
    """Reference-based integer generators of the terminal-difference lattice."""
    terminals = terminal_applied_counts(relation)
    if not terminals:
        raise AssertionError("guarded terminal relation must be nonempty")
    reference = terminals[0]
    return tuple(
        difference
        for terminal in terminals[1:]
        if any(
            difference := tuple(
                value - base
                for value, base in zip(terminal, reference, strict=True)
            )
        )
    )


def linear_terminal_output_relation(
    relation: GuardedTerminalRelation,
    observable_matrix: Sequence[Sequence[int]],
) -> tuple[Vector, ...]:
    """Distinct linear readout values on the causal terminal relation."""
    terminals = terminal_applied_counts(relation)
    if not terminals:
        raise AssertionError("guarded terminal relation must be nonempty")
    matrix = _matrix(observable_matrix, len(terminals[0]))
    return tuple(sorted({apply_integer_matrix(matrix, terminal) for terminal in terminals}))


def observable_is_scheduler_deterministic(
    relation: GuardedTerminalRelation,
    observable_matrix: Sequence[Sequence[int]],
) -> bool:
    """Exact kernel test for one declared linear terminal observable."""
    terminals = terminal_applied_counts(relation)
    matrix = _matrix(observable_matrix, len(terminals[0]))
    generators = scheduler_difference_generators(relation)
    killed = all(
        not any(apply_integer_matrix(matrix, generator))
        for generator in generators
    )
    relation_deterministic = len(
        linear_terminal_output_relation(relation, matrix)
    ) == 1
    if killed != relation_deterministic:
        raise AssertionError("scheduler difference-kernel test disagreed with outputs")
    return killed


def exact_queue_is_scheduler_deterministic(
    relation: GuardedTerminalRelation,
) -> bool:
    """Exact queue ``target-n`` is deterministic iff applied terminal count is."""
    terminals = terminal_applied_counts(relation)
    return len(set(terminals)) == 1


def scalar_scheduler_ambiguity_grain(
    relation: GuardedTerminalRelation,
    witness_row: Sequence[int],
) -> int:
    """Gcd of exact scalar witness differences across terminal branches."""
    terminals = terminal_applied_counts(relation)
    row = tuple(witness_row)
    if len(row) != len(terminals[0]):
        raise ValueError("witness_row must match terminal count dimension")
    for value in row:
        _require_int("witness entry", value)
    values = [sum(a * b for a, b in zip(row, terminal, strict=True)) for terminal in terminals]
    reference = values[0]
    grain = 0
    for value in values[1:]:
        grain = gcd(grain, abs(value - reference))
    return grain


def scalar_modular_terminal_outputs(
    relation: GuardedTerminalRelation,
    witness_row: Sequence[int],
    modulus: int,
) -> tuple[int, ...]:
    _require_int("modulus", modulus)
    if modulus <= 0:
        raise ValueError("modulus must be positive")
    terminals = terminal_applied_counts(relation)
    row = tuple(witness_row)
    if len(row) != len(terminals[0]):
        raise ValueError("witness_row must match terminal count dimension")
    for value in row:
        _require_int("witness entry", value)
    return tuple(
        sorted(
            {
                sum(
                    a * b
                    for a, b in zip(row, terminal, strict=True)
                )
                % modulus
                for terminal in terminals
            }
        )
    )


def scalar_modular_scheduler_deterministic(
    relation: GuardedTerminalRelation,
    witness_row: Sequence[int],
    modulus: int,
) -> bool:
    outputs = scalar_modular_terminal_outputs(
        relation,
        witness_row,
        modulus,
    )
    grain = scalar_scheduler_ambiguity_grain(relation, witness_row)
    expected = grain == 0 or grain % modulus == 0
    actual = len(outputs) == 1
    if actual != expected:
        raise AssertionError("modular scheduler determinism disagreed with grain")
    return actual


def repeated_scalar_modular_ambiguity_phase_count(
    ambiguity_grain: int,
    modulus: int,
) -> int:
    """Size of the subgroup generated by scheduler differences modulo ``M``."""
    _require_int("ambiguity_grain", ambiguity_grain)
    _require_int("modulus", modulus)
    if ambiguity_grain < 0:
        raise ValueError("ambiguity_grain must be nonnegative")
    if modulus <= 0:
        raise ValueError("modulus must be positive")
    if ambiguity_grain == 0:
        return 1
    return modulus // gcd(modulus, ambiguity_grain)


@dataclass(frozen=True)
class HistorySchedulerDeterminismReport:
    terminal_count: int
    applied_history_values: tuple[Vector, ...]
    committed_history_values: tuple[Vector, ...]
    applied_history_scheduler_independent: bool
    committed_history_scheduler_independent: bool
    exact_queue_scheduler_independent: bool


def history_scheduler_determinism_report(
    relation: HistoryAwareCausalTickRelation1D,
) -> HistorySchedulerDeterminismReport:
    """Read scheduler dependence directly from a history-aware causal tick."""
    if not isinstance(relation, HistoryAwareCausalTickRelation1D):
        raise TypeError("relation must be HistoryAwareCausalTickRelation1D")
    applied = tuple(
        sorted({outcome.applied_witness_after for outcome in relation.outcomes})
    )
    committed = tuple(
        sorted({outcome.committed_witness_after for outcome in relation.outcomes})
    )
    queue_states = {
        outcome.after.causal.whole_queue
        for outcome in relation.outcomes
    }
    report = HistorySchedulerDeterminismReport(
        terminal_count=len(relation.outcomes),
        applied_history_values=applied,
        committed_history_values=committed,
        applied_history_scheduler_independent=len(applied) == 1,
        committed_history_scheduler_independent=len(committed) == 1,
        exact_queue_scheduler_independent=len(queue_states) == 1,
    )
    if not report.committed_history_scheduler_independent:
        raise AssertionError("committed history must cancel scheduler allocation")
    return report
