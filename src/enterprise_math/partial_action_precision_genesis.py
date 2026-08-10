"""Finite predictive precision generated purely by partial-action legality.

This module isolates the smallest FQ-006 pressure test in which the *current*
observation carries no information at all but the declared future operation
language generates a strictly finer predictive state.

Fix ``N>=1`` and the finite chain

    X_N = {0,1,...,N}.

Current observation is constant.  Declare one deterministic partial action

    F(x) = x-1       if x>0,
           UNDEFINED if x=0.

Starting from state ``x``, the word ``F^m`` is defined exactly when ``m<=x``.
Hence through horizon ``h`` two states are future-equivalent exactly when

    min(x,h) = min(y,h).

The horizon quotient therefore has exactly

    min(h,N) + 1

classes.  At ``h=0`` every state lies in one current observation class; at
``h=N`` the predictive quotient is fully discrete.  No terminal value
observation was added: all new distinguishability comes from the legality of
future action prefixes.

This is not information creation from nothing.  The state dependence was
already present in the action domain.  FQ-006 says definedness is part of the
future signature; the horizon process reveals that latent domain structure.

A deliberately wrong comparator replaces ``UNDEFINED`` at zero by an identity
self-loop.  That makes the action total.  Under the same constant terminal
observation every future word then has the same observation from every state, so
the quotient remains one class forever.  This locks the boundary that disabled
actions must not be silently interpreted as identity.

Finite partial automata and countdown chains are standard prior mathematics.
The Enterprise Math value is the exact precision-genesis interpretation and the
minimal bridge from FQ-006 back to the project's future-generated precision
worldview.
"""

from __future__ import annotations

from dataclasses import dataclass

from .operation_quotient import family_future_partition_sequence
from .partial_operation_quotient import (
    partial_family_future_partition_sequence,
    partial_word_observation_signature,
)


def countdown_domain(maximum_state: int) -> tuple[int, ...]:
    if isinstance(maximum_state, bool) or not isinstance(maximum_state, int):
        raise TypeError("maximum_state must be an integer")
    if maximum_state < 1:
        raise ValueError("maximum_state must be at least one")
    return tuple(range(maximum_state + 1))


def constant_observation(maximum_state: int) -> dict[int, int]:
    return {state: 0 for state in countdown_domain(maximum_state)}


def partial_countdown_action(maximum_state: int) -> dict[int, int]:
    """Return the partial map ``x->x-1`` on positive states."""
    domain = countdown_domain(maximum_state)
    return {state: state - 1 for state in domain if state > 0}


def totalized_identity_countdown_action(maximum_state: int) -> dict[int, int]:
    """Wrong comparator: replace disabled zero by a self-loop identity."""
    domain = countdown_domain(maximum_state)
    return {state: max(0, state - 1) for state in domain}


def countdown_word_defined(state: int, repetitions: int) -> bool:
    if isinstance(state, bool) or not isinstance(state, int):
        raise TypeError("state must be an integer")
    if isinstance(repetitions, bool) or not isinstance(repetitions, int):
        raise TypeError("repetitions must be an integer")
    if state < 0 or repetitions < 0:
        raise ValueError("state and repetitions must be non-negative")
    return repetitions <= state


def countdown_predictive_key(
    state: int,
    maximum_state: int,
    horizon: int,
) -> int:
    """Exact closed future-equivalence key ``min(state,horizon)``."""
    domain = countdown_domain(maximum_state)
    if state not in domain:
        raise ValueError("state lies outside countdown domain")
    if isinstance(horizon, bool) or not isinstance(horizon, int):
        raise TypeError("horizon must be an integer")
    if horizon < 0:
        raise ValueError("horizon must be non-negative")
    return min(state, horizon)


def countdown_predictive_class_count(maximum_state: int, horizon: int) -> int:
    countdown_domain(maximum_state)
    if isinstance(horizon, bool) or not isinstance(horizon, int):
        raise TypeError("horizon must be an integer")
    if horizon < 0:
        raise ValueError("horizon must be non-negative")
    return min(horizon, maximum_state) + 1


def countdown_partial_partition_sequence(
    maximum_state: int,
) -> tuple[dict[int, int], ...]:
    domain = countdown_domain(maximum_state)
    return partial_family_future_partition_sequence(
        domain,
        {"step": partial_countdown_action(maximum_state)},
        constant_observation(maximum_state),
    )


def countdown_wrong_total_partition_sequence(
    maximum_state: int,
) -> tuple[dict[int, int], ...]:
    """Total-operation comparator with disabled-as-identity semantics."""
    domain = countdown_domain(maximum_state)
    return family_future_partition_sequence(
        domain,
        {"step": totalized_identity_countdown_action(maximum_state)},
        constant_observation(maximum_state),
    )


def countdown_literal_signature(
    state: int,
    maximum_state: int,
    horizon: int,
):
    domain = countdown_domain(maximum_state)
    if state not in domain:
        raise ValueError("state lies outside countdown domain")
    return partial_word_observation_signature(
        state,
        {"step": partial_countdown_action(maximum_state)},
        constant_observation(maximum_state),
        horizon,
    )


@dataclass(frozen=True)
class PrecisionGenesisReport:
    maximum_state: int
    current_class_count: int
    stage_class_counts: tuple[int, ...]
    terminal_class_count: int
    wrong_total_stage_count: int

    @property
    def generated_predictive_classes(self) -> int:
        return self.terminal_class_count - self.current_class_count


def precision_genesis_report(maximum_state: int) -> PrecisionGenesisReport:
    stages = countdown_partial_partition_sequence(maximum_state)
    counts = tuple(len(set(stage.values())) for stage in stages)
    wrong = countdown_wrong_total_partition_sequence(maximum_state)
    wrong_counts = {len(set(stage.values())) for stage in wrong}
    if wrong_counts != {1}:
        raise AssertionError("disabled-as-identity comparator unexpectedly generated precision")
    if counts != tuple(range(1, maximum_state + 2)):
        raise AssertionError("countdown partition sequence lost exact one-class-per-horizon growth")
    return PrecisionGenesisReport(
        maximum_state=maximum_state,
        current_class_count=counts[0],
        stage_class_counts=counts,
        terminal_class_count=counts[-1],
        wrong_total_stage_count=len(wrong),
    )
