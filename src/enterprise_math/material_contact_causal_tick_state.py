"""Relation-valued causal material tick with retained whole-quantum queue.

A causal multi-contact world needs two different retained material details:

* ``delta_e`` — subquantum numerator remainder inside one contact quantizer;
* ``Q_e`` — whole impulse quanta already quantized but not yet causally applied.

Let a current state contain body/contact network ``X``, local reservoirs
``delta`` and whole queue ``Q``.  New material response quantizes independently
per contact to delivered vector ``J`` and new subquantum remainder ``delta'``.
If whole quanta on the same named contact are age/source blind under the declared
future language, old and new whole quanta have the exact combined budget

    U = Q + J.

Guarded unit actions then consume a reachable terminal prefix ``n<=U`` and leave

    Q' = U - n.

The next body state is the exact additive update by ``n``.  When the terminal
prefix relation has several members, the tick is relation-valued unless an
explicit scheduler/selector is declared.

The local conservation law survives causal blocking exactly.  If contact ``e``
has amplitude ``A_e``, scale ``S_e`` and response total ``R_e``, then

    A_e*n_e + A_e*Q'_e + delta'_e
      = A_e*Q_e + delta_e + S_e*R_e.

Across repeated ticks this telescopes to

    A_e*sum(applied_e) + A_e*Q_T,e + delta_T,e
      = A_e*Q_0,e + delta_0,e + S_e*sum(response_e).

So the guard does not destroy material accounting; it transfers whole delivered
impulse between the applied ledger and the explicit causal queue.

Queue age erasure is task-relative.  The coordinatewise sum ``Q+J`` is exact
only when future laws treat old/new whole quanta on one contact identically.  A
future law that reads age, source tick, fatigue attribution or priority must
retain that additional witness instead of using this quotient.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Sequence

from .material_contact_network_impulse_1d import (
    ContactNetworkMomentum1D,
    apply_contact_impulse_vector,
    contact_coupling_gram,
    contact_relative_scores,
)
from .material_contact_network_tick_1d import (
    ContactMaterialChannelSequence,
    ContactMaterialImpulseState,
    apply_contact_material_response_sequence,
)
from .material_contact_tick_causal_queue import (
    GuardedTerminalPrefix,
    guarded_terminal_prefix_relation,
)


Vector = tuple[int, ...]


def _nonnegative_vector(
    values: Sequence[int],
    length: int,
    *,
    name: str,
) -> Vector:
    result = tuple(values)
    if len(result) != length:
        raise ValueError(f"{name} must match contact count")
    for value in result:
        if isinstance(value, bool) or not isinstance(value, int) or value < 0:
            raise ValueError(f"{name} entries must be nonnegative integers")
    return result


@dataclass(frozen=True)
class CausalMaterialContactState1D:
    network: ContactNetworkMomentum1D
    reservoirs: tuple[ContactMaterialImpulseState, ...]
    whole_queue: Vector

    def __post_init__(self) -> None:
        if not isinstance(self.network, ContactNetworkMomentum1D):
            raise TypeError("network must be ContactNetworkMomentum1D")
        contact_count = len(self.network.contacts)
        if len(self.reservoirs) != contact_count:
            raise ValueError("one reservoir is required per contact")
        for reservoir in self.reservoirs:
            if not isinstance(reservoir, ContactMaterialImpulseState):
                raise TypeError("reservoir entries must be ContactMaterialImpulseState")
        _nonnegative_vector(
            self.whole_queue,
            contact_count,
            name="whole_queue",
        )


@dataclass(frozen=True)
class CausalMaterialTickOutcome1D:
    terminal: GuardedTerminalPrefix
    after: CausalMaterialContactState1D
    local_ledger_residuals: Vector

    @property
    def applied_impulse_vector(self) -> Vector:
        return self.terminal.applied_counts


@dataclass(frozen=True)
class CausalMaterialTickRelation1D:
    before: CausalMaterialContactState1D
    channel_sequences: tuple[ContactMaterialChannelSequence, ...]
    newly_quantized: Vector
    available_whole_budget: Vector
    outcomes: tuple[CausalMaterialTickOutcome1D, ...]

    @property
    def deterministic(self) -> bool:
        return len(self.outcomes) == 1

    @property
    def every_outcome_consumes_all_budget(self) -> bool:
        return all(not any(outcome.after.whole_queue) for outcome in self.outcomes)


def causal_material_contact_tick(
    state: CausalMaterialContactState1D,
    response_sequences: Sequence[Iterable[int]],
) -> CausalMaterialTickRelation1D:
    """Quantize locally, merge same-contact whole budget, then consume until stuck."""
    if not isinstance(state, CausalMaterialContactState1D):
        raise TypeError("state must be CausalMaterialContactState1D")
    sequences = tuple(response_sequences)
    contact_count = len(state.network.contacts)
    if len(sequences) != contact_count:
        raise ValueError("one response sequence is required per contact")

    channel_sequences = tuple(
        apply_contact_material_response_sequence(reservoir, responses)
        for reservoir, responses in zip(
            state.reservoirs,
            sequences,
            strict=True,
        )
    )
    new_delivered = tuple(
        sequence.delivered_impulse_total for sequence in channel_sequences
    )
    available = tuple(
        queued + delivered
        for queued, delivered in zip(
            state.whole_queue,
            new_delivered,
            strict=True,
        )
    )

    terminal_relation = guarded_terminal_prefix_relation(
        contact_relative_scores(state.network),
        contact_coupling_gram(state.network),
        available,
    )

    reservoir_after = tuple(sequence.after for sequence in channel_sequences)
    outcomes: list[CausalMaterialTickOutcome1D] = []
    for terminal in terminal_relation.terminals:
        step = apply_contact_impulse_vector(
            state.network,
            terminal.applied_counts,
        )
        next_state = CausalMaterialContactState1D(
            network=step.after,
            reservoirs=reservoir_after,
            whole_queue=terminal.queued_counts,
        )

        residuals = []
        for index, (
            before_reservoir,
            sequence,
            after_reservoir,
            queue_before,
            applied,
            queue_after,
        ) in enumerate(
            zip(
                state.reservoirs,
                channel_sequences,
                reservoir_after,
                state.whole_queue,
                terminal.applied_counts,
                terminal.queued_counts,
                strict=True,
            )
        ):
            lhs = (
                before_reservoir.amplitude * applied
                + before_reservoir.amplitude * queue_after
                + after_reservoir.pending_numerator
            )
            rhs = (
                before_reservoir.amplitude * queue_before
                + before_reservoir.pending_numerator
                + before_reservoir.impulse_scale * sequence.response_total
            )
            residual = lhs - rhs
            if residual != 0:
                raise AssertionError(
                    f"contact {index} causal material telescope failed"
                )
            residuals.append(residual)

        outcomes.append(
            CausalMaterialTickOutcome1D(
                terminal=terminal,
                after=next_state,
                local_ledger_residuals=tuple(residuals),
            )
        )

    return CausalMaterialTickRelation1D(
        before=state,
        channel_sequences=channel_sequences,
        newly_quantized=new_delivered,
        available_whole_budget=available,
        outcomes=tuple(outcomes),
    )


def accumulated_causal_material_ledger(
    initial_queue: int,
    initial_remainder: int,
    amplitude: int,
    impulse_scale: int,
    response_total: int,
    applied_total: int,
    final_queue: int,
    final_remainder: int,
) -> bool:
    """Scalar telescope identity for one contact across any number of ticks."""
    values = (
        initial_queue,
        initial_remainder,
        amplitude,
        impulse_scale,
        response_total,
        applied_total,
        final_queue,
        final_remainder,
    )
    if any(isinstance(value, bool) or not isinstance(value, int) for value in values):
        raise TypeError("causal material ledger arguments must be integers")
    if amplitude <= 0 or impulse_scale <= 0:
        raise ValueError("amplitude and impulse_scale must be positive")
    if min(initial_queue, initial_remainder, response_total, applied_total, final_queue, final_remainder) < 0:
        raise ValueError("causal material ledger quantities must be nonnegative")
    if initial_remainder >= amplitude or final_remainder >= amplitude:
        raise ValueError("remainders must lie in 0..amplitude-1")
    return (
        amplitude * applied_total
        + amplitude * final_queue
        + final_remainder
        == amplitude * initial_queue
        + initial_remainder
        + impulse_scale * response_total
    )
