"""Material-driven finite least action on one weighted 1D contact chain.

The weighted-chain owner proves a unique componentwise-least delivered impulse
``j*`` for the aligned Z-path.  This module asks how finite contact-local
material quantizers deliver those integer impulse quanta over time.

Contact ``i`` has one fixed repulsive channel with amplitude ``A_i``, response
sample ``r_i``, scale ``S_i`` and pending detail ``delta_i``.  We restrict the
one-evaluation numerator increment

    a_i = S_i*r_i

to ``0 <= a_i <= A_i``.  One evaluation on a currently violated contact uses the
canonical positive quotient

    delta_i + a_i = A_i*q_i + delta_i',

so ``q_i`` is zero or one.  Only ``q_i`` enters the contact impulse vector.

With retained detail and ``a_i>0``, exactly ``j_i*`` delivered quanta require

    N_i = ceil((A_i*j_i* - delta_i(0))/a_i)

evaluations (zero when ``j_i*=0``).  Every positive delivery is one legal unit
least-action update, hence arbitrary violated-contact priorities still terminate
at the same ``j*``.  The per-contact and total material evaluation counts are
therefore schedule-independent even though intermediate score histories need
not be.

Two explicit lower-precision stalls are kept separate:

* ``a_i=0`` cannot deliver a required positive quantum even with retained detail;
* if detail is discarded each evaluation, any subquantum ``0<a_i<A_i`` channel
  also delivers zero forever.

Both return ``MATERIAL_CHANNEL_STALLED`` rather than looping or fabricating a
response.  A full-quantum channel ``a_i=A_i`` still delivers one quantum per
selected evaluation without retained detail.

This result is specific to the aligned Z-path least-action setting.  Branching
non-Z networks can have several incomparable minimum responses, so timing and
material asymmetry can become outcome-determining there.
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
            raise ValueError("unit-channel probe requires response*scale <= amplitude")

    @property
    def raw_increment(self) -> int:
        return self.response_sample * self.impulse_scale_magnitude

    def evaluations_for_delivered_quanta(self, quanta: int) -> int | None:
        """Exact retained-detail evaluations needed to deliver ``quanta``."""
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
    channels: tuple[ContactMaterialUnitChannel1D, ...]
    | list[ContactMaterialUnitChannel1D],
) -> tuple[ContactMaterialUnitChannel1D, ...]:
    result = tuple(channels)
    if len(result) != len(state.contacts):
        raise ValueError("channels must contain one material channel per contact")
    if any(not isinstance(channel, ContactMaterialUnitChannel1D) for channel in result):
        raise ValueError("channels must contain ContactMaterialUnitChannel1D values")
    return result


def _stalled_result(
    state: ContactNetworkMomentum1D,
    order: tuple[int, ...],
    retain_detail: bool,
    least: tuple[int, ...],
    channels: tuple[ContactMaterialUnitChannel1D, ...],
    expected: tuple[int | None, ...],
    stalled_contact: int,
) -> QuantizedMaterialLeastActionSolution1D:
    step = apply_contact_impulse_vector(state, (0,) * len(state.contacts))
    return QuantizedMaterialLeastActionSolution1D(
        status=MATERIAL_CHANNEL_STALLED,
        before=state,
        priority=order,
        retain_detail=retain_detail,
        least_impulse_oracle=least,
        impulse_vector=(0,) * len(state.contacts),
        final_scores=step.relative_scores_after,
        final_momenta=step.after.momenta,
        initial_details=tuple(channel.initial_detail for channel in channels),
        final_details=(
            tuple(channel.initial_detail for channel in channels)
            if retain_detail
            else (0,) * len(channels)
        ),
        evaluations_per_contact=(0,) * len(channels),
        expected_evaluations_per_contact=expected,
        events=(),
        stalled_contact=stalled_contact,
    )


def solve_weighted_chain_quantized_least_action(
    state: ContactNetworkMomentum1D,
    channels: tuple[ContactMaterialUnitChannel1D, ...]
    | list[ContactMaterialUnitChannel1D],
    priority: tuple[int, ...] | list[int] | None = None,
    retain_detail: bool = True,
) -> QuantizedMaterialLeastActionSolution1D:
    """Drive Z-path least action through contact-local finite material channels."""
    if not isinstance(retain_detail, bool):
        raise ValueError("retain_detail must be boolean")
    channel_tuple = _validate_channels(state, channels)
    order = weighted_chain_priority(len(state.contacts), priority)
    oracle = solve_weighted_chain_least_action(state, order)
    least = oracle.impulse_vector
    initial_scores = contact_relative_scores(state)
    gram = contact_coupling_gram(state)
    expected = tuple(
        channel.evaluations_for_delivered_quanta(least[index])
        for index, channel in enumerate(channel_tuple)
    )

    for index, required in enumerate(least):
        if required == 0:
            continue
        channel = channel_tuple[index]
        if channel.raw_increment == 0:
            return _stalled_result(
                state, order, retain_detail, least, channel_tuple, expected, index
            )
        if not retain_detail and channel.raw_increment < channel.amplitude:
            return _stalled_result(
                state, order, False, least, channel_tuple, expected, index
            )

    scores = list(initial_scores)
    impulses = [0] * len(state.contacts)
    details = [channel.initial_detail for channel in channel_tuple]
    evaluations = [0] * len(state.contacts)
    events: list[QuantizedLeastActionEvent1D] = []

    while True:
        violated = {index for index, score in enumerate(scores) if score < 0}
        if not violated:
            break
        chosen = next(index for index in order if index in violated)
        channel = channel_tuple[chosen]
        if impulses[chosen] >= least[chosen]:
            raise AssertionError("violated contact reached its least feasible impulse")

        score_before = scores[chosen]
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

        if report.impulse_quanta:
            impulses[chosen] += 1
            if impulses[chosen] > least[chosen]:
                raise AssertionError("material delivery overshot least-action impulse")
            for row in range(len(scores)):
                scores[row] += gram[row][chosen]

        events.append(
            QuantizedLeastActionEvent1D(
                event_index=len(events),
                contact_index=chosen,
                score_before=score_before,
                detail_before=detail_before,
                delivered_quanta=report.impulse_quanta,
                detail_after=details[chosen],
                impulse_vector_after=tuple(impulses),
                scores_after=tuple(scores),
            )
        )

        if retain_detail:
            exact_bound = sum(value for value in expected if value is not None)
            if len(events) > exact_bound:
                raise AssertionError("retained material scheduler exceeded exact event count")

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
