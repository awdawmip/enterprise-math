"""Material-driven finite least action on one weighted 1D contact chain.

The weighted-chain owner proves a unique componentwise-least delivered impulse
``j*`` when the aligned path contact Gram is a Z-matrix.  This module asks how a
finite material channel delivers those integer impulse quanta over time.

Each contact ``i`` has one fixed repulsive material channel

    amplitude A_i > 0,
    response sample r_i in 0..A_i,
    impulse scale S_i > 0,
    raw increment a_i = S_i*r_i,

with the bounded one-event condition ``0 <= a_i <= A_i``.  A contact-local
pending detail ``delta_i`` lies in ``0..A_i-1``.  When that contact is currently
violated, one material evaluation applies the canonical positive quotient

    delta_i + a_i = A_i*q_i + delta_i',

where ``q_i`` is necessarily zero or one.  Only ``q_i`` is delivered to the
contact-network impulse state.

With retained detail and ``a_i>0``, the contact evaluations required to deliver
exactly ``j_i*`` quanta are

    N_i = ceil((A_i*j_i* - delta_i(0)) / a_i)

for ``j_i*>0``.  The value is zero when ``j_i*=0``.  Because every positive
delivery is exactly one legal unit least-action update, arbitrary violated-
contact priorities still terminate at the same ``j*``.  The total number of
material evaluations is ``sum_i N_i`` and is schedule-independent, although the
intermediate score path need not be.

If pending detail is deliberately discarded after every evaluation, a channel
with ``a_i<A_i`` can never deliver even one integer impulse quantum.  If the
least solution needs ``j_i*>0`` on such a contact, the declared lower-precision
policy is exactly ``MATERIAL_CHANNEL_STALLED``.  A full-quantum channel
``a_i=A_i`` still delivers one quantum per selected evaluation without retained
detail.

This result is specific to the aligned Z-path least-action setting.  On a
branching non-Z network, response timing/capacity can select among multiple
minimum responses; schedule-independence is not silently generalized there.
"""

from __future__ import annotations

from dataclasses import dataclass

from .material_contact_network_impulse_1d import (
    ContactNetworkMomentum1D,
    apply_contact_impulse_vector,
    contact_coupling_gram,
    contact_relative_scores,
)
from .material_impulse_world_1d import material_impulse_quantization
from .material_weighted_chain_least_action_1d import (
    solve_weighted_chain_least_action,
    weighted_chain_priority,
)

MATERIAL_CHAIN_RESOLVED = "MATERIAL_CHAIN_RESOLVED"
MATERIAL_CHANNEL_STALLED = "MATERIAL_CHANNEL_STALLED"


def _ceil_div_positive(numerator: int, denominator: int) -> int:
    if numerator <= 0 or denominator <= 0:
        raise ValueError("ceil-div arguments must be positive")
    return (numerator + denominator - 1) // denominator


@dataclass(frozen=True)
class ContactMaterialUnitChannel1D:
    amplitude: int
    response_sample: int
    impulse_scale_magnitude: int
    initial_detail: int = 0

    def __post_init__(self) -> None:
        for name, value in (
            ("amplitude", self.amplitude),
            ("response_sample", self.response_sample),
            ("impulse_scale_magnitude", self.impulse_scale_magnitude),
            ("initial_detail", self.initial_detail),
        ):
            if isinstance(value, bool) or not isinstance(value, int):
                raise ValueError(f"{name} must be an integer")
        if self.amplitude <= 0:
            raise ValueError("amplitude must be positive")
        if not 0 <= self.response_sample <= self.amplitude:
            raise ValueError("response_sample must lie in 0..amplitude")
        if self.impulse_scale_magnitude <= 0:
            raise ValueError("impulse_scale_magnitude must be positive")
        if not 0 <= self.initial_detail < self.amplitude:
            raise ValueError("initial_detail must lie in 0..amplitude-1")
        if self.raw_increment > self.amplitude:
            raise ValueError(
                "unit-channel probe requires response*scale <= amplitude"
            )

    @property
    def raw_increment(self) -> int:
        return self.response_sample * self.impulse_scale_magnitude

    def evaluations_for_delivered_quanta(self, quanta: int) -> int | None:
        """Exact retained-detail evaluation count, or ``None`` if delivery is impossible."""
        if isinstance(quanta, bool) or not isinstance(quanta, int) or quanta < 0:
            raise ValueError("quanta must be a non-negative integer")
        if quanta == 0:
            return 0
        if self.raw_increment == 0:
            return None
        required = self.amplitude * quanta - self.initial_detail
        if required <= 0:
            return 0
        return _ceil_div_positive(required, self.raw_increment)


@dataclass(frozen=True)
class QuantizedLeastActionEvent1D:
    event_index: int
    contact_index: int
    score_before: int
    detail_before: int
    delivered_quanta: int
    detail_after: int
    impulse_vector_after: tuple[int, ...]
    scores_after: tuple[int, ...]


@dataclass(frozen=True)
class QuantizedMaterialLeastActionSolution1D:
    status: str
    before: ContactNetworkMomentum1D
    priority: tuple[int, ...]
    retain_detail: bool
    least_impulse_oracle: tuple[int, ...]
    impulse_vector: tuple[int, ...]
    final_scores: tuple[int, ...]
    final_momenta: tuple[int, ...]
    initial_details: tuple[int, ...]
    final_details: tuple[int, ...]
    evaluations_per_contact: tuple[int, ...]
    expected_evaluations_per_contact: tuple[int | None, ...]
    events: tuple[QuantizedLeastActionEvent1D, ...]
    stalled_contact: int | None = None

    @property
    def resolved(self) -> bool:
        return self.status == MATERIAL_CHAIN_RESOLVED

    @property
    def total_material_evaluations(self) -> int:
        return sum(self.evaluations_per_contact)


def _validate_channels(
    state: ContactNetworkMomentum1D,
    channels: tuple[ContactMaterialUnitChannel1D, ...] | list[ContactMaterialUnitChannel1D],
) -> tuple[ContactMaterialUnitChannel1D, ...]:
    result = tuple(channels)
    if len(result) != len(state.contacts):
        raise ValueError("channels must contain one material channel per contact")
    if any(not isinstance(channel, ContactMaterialUnitChannel1D) for channel in result):
        raise ValueError("channels must contain ContactMaterialUnitChannel1D values")
    return result


def solve_weighted_chain_quantized_least_action(
    state: ContactNetworkMomentum1D,
    channels: tuple[ContactMaterialUnitChannel1D, ...] | list[ContactMaterialUnitChannel1D],
    priority: tuple[int, ...] | list[int] | None = None,
    retain_detail: bool = True,
) -> QuantizedMaterialLeastActionSolution1D:
    """Drive the Z-path least action through finite contact-local material quantizers."""
    if not isinstance(retain_detail, bool):
        raise ValueError("retain_detail must be boolean")
    channel_tuple = _validate_channels(state, channels)
    order = weighted_chain_priority(len(state.contacts), priority)
    oracle = solve_weighted_chain_least_action(state, order)
    least = oracle.impulse_vector
    gram = contact_coupling_gram(state)
    scores = list(contact_relative_scores(state))
    impulses = [0] * len(state.contacts)
    details = [channel.initial_detail for channel in channel_tuple]
    evaluations = [0] * len(state.contacts)
    expected = tuple(
        channel.evaluations_for_delivered_quanta(least[index])
        for index, channel in enumerate(channel_tuple)
    )

    # Under the dropped-detail unit-channel policy, a subquantum channel can
    # never deliver.  Z off-diagonal entries are non-positive, so other contacts
    # cannot repair a coordinate that itself can never fire enough.
    if not retain_detail:
        for index, required in enumerate(least):
            if required > 0 and channel_tuple[index].raw_increment < channel_tuple[index].amplitude:
                step = apply_contact_impulse_vector(state, tuple(impulses))
                return QuantizedMaterialLeastActionSolution1D(
                    status=MATERIAL_CHANNEL_STALLED,
                    before=state,
                    priority=order,
                    retain_detail=False,
                    least_impulse_oracle=least,
                    impulse_vector=tuple(impulses),
                    final_scores=step.relative_scores_after,
                    final_momenta=step.after.momenta,
                    initial_details=tuple(channel.initial_detail for channel in channel_tuple),
                    final_details=(0,) * len(channel_tuple),
                    evaluations_per_contact=tuple(evaluations),
                    expected_evaluations_per_contact=expected,
                    events=(),
                    stalled_contact=index,
                )

    events: list[QuantizedLeastActionEvent1D] = []
    while True:
        violated = {index for index, score in enumerate(scores) if score < 0}
        if not violated:
            break
        chosen = next(index for index in order if index in violated)
        channel = channel_tuple[chosen]
        if impulses[chosen] >= least[chosen]:
            raise AssertionError("violated contact reached its least feasible impulse")

        detail_before = details[chosen] if retain_detail else 0
        report = material_impulse_quantization(
            channel.response_sample,
            channel.amplitude,
            channel.impulse_scale_magnitude,
            detail_before,
        )
        if report.impulse_quanta not in (0, 1):
            raise AssertionError("unit material channel delivered more than one impulse quantum")
        evaluations[chosen] += 1
        details[chosen] = report.detail_after if retain_detail else 0

        if report.impulse_quanta == 1:
            impulses[chosen] += 1
            if impulses[chosen] > least[chosen]:
                raise AssertionError("material delivery overshot least-action impulse")
            for row in range(len(scores)):
                scores[row] += gram[row][chosen]

        events.append(
            QuantizedLeastActionEvent1D(
                event_index=len(events),
                contact_index=chosen,
                score_before=events[-1].scores_after[chosen] if events else contact_relative_scores(state)[chosen],
                detail_before=detail_before,
                delivered_quanta=report.impulse_quanta,
                detail_after=details[chosen],
                impulse_vector_after=tuple(impulses),
                scores_after=tuple(scores),
            )
        )

        if retain_detail:
            bound = sum(value for value in expected if value is not None)
            if len(events) > bound:
                raise AssertionError("retained material scheduler exceeded exact evaluation bound")

    result = tuple(impulses)
    if result != least:
        raise AssertionError("quantized material scheduler did not reach least-action impulse")
    if retain_detail and tuple(evaluations) != expected:
        raise AssertionError("per-contact material evaluation count disagrees with exact formula")
    step = apply_contact_impulse_vector(state, result)
    if step.relative_scores_after != tuple(scores):
        raise AssertionError("quantized material score ledger drifted from network oracle")
    return QuantizedMaterialLeastActionSolution1D(
        status=MATERIAL_CHAIN_RESOLVED,
        before=state,
        priority=order,
        retain_detail=retain_detail,
        least_impulse_oracle=least,
        impulse_vector=result,
        final_scores=step.relative_scores_after,
        final_momenta=step.after.momenta,
        initial_details=tuple(channel.initial_detail for channel in channel_tuple),
        final_details=tuple(details),
        evaluations_per_contact=tuple(evaluations),
        expected_evaluations_per_contact=expected,
        events=tuple(events),
        stalled_contact=None,
    )
