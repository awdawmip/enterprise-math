"""Finite-TTL loss ledger for causal whole-contact material queues.

The causal material tick preserves already-quantized whole impulse in an explicit
queue ``Q``.  The age-precision bridge can additionally declare a finite TTL,
which expires some queued whole quanta.  Expiry is a new physical/accounting
operation: those quanta cannot simply disappear from the exact material ledger.

For one contact with amplitude ``A`` and positive impulse scale ``S``:

* old queued whole count is ``Q``;
* new material response total ``R`` quantizes to ``J`` and new subquantum
  remainder ``delta'``;
* guarded causal application actually applies ``n`` whole quanta;
* an age/source policy then expires ``x`` surviving whole quanta;
* next queued total is ``Q'=Q+J-n-x``.

The exact one-tick identity is

    A*n + A*Q' + A*x + delta'
      = A*Q + delta + S*R.

Thus TTL expiry requires an explicit sink/transfer ledger.  If the world calls
expiry dissipation, ``A*x`` is the exact dissipated whole-numerator amount.  A
different world may route it elsewhere, but silently deleting it breaks the
material telescope by exactly ``A*x``.

Across ticks:

    A*sum(n_t) + A*Q_T + A*sum(x_t) + delta_T
      = A*Q_0 + delta_0 + S*sum(R_t).

This module composes the parent guarded causal count relation with the sibling
finite-TTL age histogram.  It does not choose a contact scheduler.  For each
causal terminal applied-count branch, a declared same-contact token policy
(FIFO or LIFO) updates the age histogram and reports the expired sink.

The immediate body/contact state depends only on the applied count vector ``n``.
FIFO/LIFO can therefore agree on the current physical impulse while disagreeing
on TTL loss and next queued state.  Age/source order is consequently a genuine
world-law choice once TTL exists.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Sequence

from .material_contact_causal_tick_state import (
    CausalMaterialContactState1D,
    CausalMaterialTickOutcome1D,
    causal_material_contact_tick,
)
from .material_contact_network_impulse_1d import ContactNetworkMomentum1D
from .material_contact_network_tick_1d import ContactMaterialImpulseState
from .material_contact_queue_age_precision import (
    ContactWholeQueueAgeState,
    ContactWholeQueueConsumeAgeStep,
    consume_then_age_queue,
)


Vector = tuple[int, ...]


def _policy_vector(policies: Sequence[str], contact_count: int) -> tuple[str, ...]:
    result = tuple(policies)
    if len(result) != contact_count:
        raise ValueError("one FIFO/LIFO policy is required per contact")
    if any(policy not in ("FIFO", "LIFO") for policy in result):
        raise ValueError("TTL token policies must be FIFO or LIFO")
    return result


@dataclass(frozen=True)
class TTLMaterialContactState1D:
    """Causal material state with exact per-contact whole-quantum age histograms."""

    network: ContactNetworkMomentum1D
    reservoirs: tuple[ContactMaterialImpulseState, ...]
    age_queues: tuple[ContactWholeQueueAgeState, ...]

    def __post_init__(self) -> None:
        if not isinstance(self.network, ContactNetworkMomentum1D):
            raise TypeError("network must be ContactNetworkMomentum1D")
        count = len(self.network.contacts)
        if len(self.reservoirs) != count or len(self.age_queues) != count:
            raise ValueError("one reservoir and age queue are required per contact")
        for reservoir in self.reservoirs:
            if not isinstance(reservoir, ContactMaterialImpulseState):
                raise TypeError("reservoir entries must be ContactMaterialImpulseState")
        for queue in self.age_queues:
            if not isinstance(queue, ContactWholeQueueAgeState):
                raise TypeError("age_queues must contain ContactWholeQueueAgeState values")

    @property
    def whole_queue(self) -> Vector:
        return tuple(queue.total for queue in self.age_queues)

    def as_age_blind_causal_state(self) -> CausalMaterialContactState1D:
        return CausalMaterialContactState1D(
            network=self.network,
            reservoirs=self.reservoirs,
            whole_queue=self.whole_queue,
        )


@dataclass(frozen=True)
class TTLMaterialTickOutcome1D:
    causal_outcome: CausalMaterialTickOutcome1D
    age_steps: tuple[ContactWholeQueueConsumeAgeStep, ...]
    expired_whole_vector: Vector
    after: TTLMaterialContactState1D
    local_ledger_residuals: Vector
    omitted_expiry_defects: Vector

    @property
    def applied_impulse_vector(self) -> Vector:
        return self.causal_outcome.applied_impulse_vector

    @property
    def dissipated_whole_numerator_vector(self) -> Vector:
        return tuple(
            reservoir.amplitude * expired
            for reservoir, expired in zip(
                self.causal_outcome.after.reservoirs,
                self.expired_whole_vector,
                strict=True,
            )
        )


@dataclass(frozen=True)
class TTLMaterialTickRelation1D:
    before: TTLMaterialContactState1D
    policies: tuple[str, ...]
    newly_quantized: Vector
    outcomes: tuple[TTLMaterialTickOutcome1D, ...]

    @property
    def deterministic(self) -> bool:
        return len(self.outcomes) == 1


def ttl_material_contact_tick(
    state: TTLMaterialContactState1D,
    response_sequences: Sequence[Iterable[int]],
    policies: Sequence[str],
) -> TTLMaterialTickRelation1D:
    """Run local quantization + guarded consumption + FIFO/LIFO TTL expiry."""
    if not isinstance(state, TTLMaterialContactState1D):
        raise TypeError("state must be TTLMaterialContactState1D")
    contact_count = len(state.network.contacts)
    policy_values = _policy_vector(policies, contact_count)

    causal_relation = causal_material_contact_tick(
        state.as_age_blind_causal_state(),
        response_sequences,
    )
    outcomes: list[TTLMaterialTickOutcome1D] = []
    for causal_outcome in causal_relation.outcomes:
        age_steps = tuple(
            consume_then_age_queue(
                age_queue,
                newly_quantized,
                applied,
                policy=policy,
            )
            for age_queue, newly_quantized, applied, policy in zip(
                state.age_queues,
                causal_relation.newly_quantized,
                causal_outcome.applied_impulse_vector,
                policy_values,
                strict=True,
            )
        )
        expired = tuple(step.expired_quanta for step in age_steps)
        age_after = tuple(step.after for step in age_steps)
        if tuple(queue.total for queue in age_after) != tuple(
            queued - lost
            for queued, lost in zip(
                causal_outcome.after.whole_queue,
                expired,
                strict=True,
            )
        ):
            raise AssertionError("TTL age queue disagreed with causal pre-expiry queue")

        after = TTLMaterialContactState1D(
            network=causal_outcome.after.network,
            reservoirs=causal_outcome.after.reservoirs,
            age_queues=age_after,
        )
        residuals = []
        omission_defects = []
        for index, (
            reservoir_before,
            sequence,
            reservoir_after,
            queue_before,
            applied,
            queue_after,
            lost,
        ) in enumerate(
            zip(
                state.reservoirs,
                causal_relation.channel_sequences,
                causal_outcome.after.reservoirs,
                state.whole_queue,
                causal_outcome.applied_impulse_vector,
                after.whole_queue,
                expired,
                strict=True,
            )
        ):
            amplitude = reservoir_before.amplitude
            lhs = (
                amplitude * applied
                + amplitude * queue_after
                + amplitude * lost
                + reservoir_after.pending_numerator
            )
            rhs = (
                amplitude * queue_before
                + reservoir_before.pending_numerator
                + reservoir_before.impulse_scale * sequence.response_total
            )
            residual = lhs - rhs
            if residual != 0:
                raise AssertionError(f"contact {index} TTL material ledger failed")
            residuals.append(residual)

            omitted_lhs = (
                amplitude * applied
                + amplitude * queue_after
                + reservoir_after.pending_numerator
            )
            defect = rhs - omitted_lhs
            if defect != amplitude * lost:
                raise AssertionError("omitted-expiry defect is not exactly A*x")
            omission_defects.append(defect)

        outcomes.append(
            TTLMaterialTickOutcome1D(
                causal_outcome=causal_outcome,
                age_steps=age_steps,
                expired_whole_vector=expired,
                after=after,
                local_ledger_residuals=tuple(residuals),
                omitted_expiry_defects=tuple(omission_defects),
            )
        )

    return TTLMaterialTickRelation1D(
        before=state,
        policies=policy_values,
        newly_quantized=causal_relation.newly_quantized,
        outcomes=tuple(outcomes),
    )


def accumulated_ttl_material_ledger(
    *,
    initial_queue: int,
    initial_remainder: int,
    amplitude: int,
    impulse_scale: int,
    response_total: int,
    applied_total: int,
    expired_total: int,
    final_queue: int,
    final_remainder: int,
) -> bool:
    """Scalar exact telescope including the explicit expired-whole sink."""
    values = (
        initial_queue,
        initial_remainder,
        amplitude,
        impulse_scale,
        response_total,
        applied_total,
        expired_total,
        final_queue,
        final_remainder,
    )
    if any(isinstance(value, bool) or not isinstance(value, int) for value in values):
        raise TypeError("TTL ledger arguments must be integers")
    if amplitude <= 0 or impulse_scale <= 0:
        raise ValueError("amplitude and impulse_scale must be positive")
    if min(
        initial_queue,
        initial_remainder,
        response_total,
        applied_total,
        expired_total,
        final_queue,
        final_remainder,
    ) < 0:
        raise ValueError("TTL ledger quantities must be nonnegative")
    if initial_remainder >= amplitude or final_remainder >= amplitude:
        raise ValueError("remainders must lie in 0..amplitude-1")
    return (
        amplitude * applied_total
        + amplitude * expired_total
        + amplitude * final_queue
        + final_remainder
        == amplitude * initial_queue
        + initial_remainder
        + impulse_scale * response_total
    )
