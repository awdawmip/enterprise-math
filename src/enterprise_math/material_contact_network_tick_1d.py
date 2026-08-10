"""Exact multi-contact material-response tick for the E001 integer momentum world.

This bridge composes two already-established layers without changing either:

1. canonical retained-detail material impulse quantization;
2. delivered nonnegative contact impulse quanta acting through
   ``p' = p+Bj`` and ``r' = r+Kj``.

Each named contact owns an independent bridge-local reservoir state with positive
amplitude ``A_e``, positive impulse scale ``S_e`` and canonical nonnegative
pending numerator ``delta_e``.  One response sample is quantized by the canonical
``material_impulse_quantization`` function; this module does not duplicate that
integer quotient/remainder law.

For a finite nonnegative response sequence on contact ``e`` the exact local
ledger is

    A_e * J_e + delta'_e
      = delta_e + S_e * sum(response_e),

where ``J_e`` is the integer impulse delivered by that contact during the tick.
Only after every contact has quantized locally is the delivered vector ``J``
applied to the network in one declared batched step.

No raw or pending numerator is pooled across contacts.  Splitting one contact's
response into subevents leaves its final reservoir and delivered total unchanged
when detail is retained, so the batched network after-state is also invariant.

The batched network application is intentionally unguarded.  A world that
re-checks ``r_i<0`` between delivered units uses the distinct guarded-sequential
policy studied by ``material_contact_tick_policy``.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Sequence

from .material_contact_network_impulse_1d import (
    ContactNetworkImpulseStep1D,
    ContactNetworkMomentum1D,
    apply_contact_impulse_vector,
)
from .material_impulse_world_1d import (
    MaterialImpulseQuantization,
    material_impulse_quantization,
)


def _require_int(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f"{name} must be an integer")


def _require_positive(name: str, value: int) -> None:
    _require_int(name, value)
    if value <= 0:
        raise ValueError(f"{name} must be positive")


@dataclass(frozen=True)
class ContactMaterialImpulseState:
    """One contact-local retained numerator reservoir."""

    amplitude: int
    impulse_scale: int
    pending_numerator: int = 0

    def __post_init__(self) -> None:
        _require_positive("amplitude", self.amplitude)
        _require_positive("impulse_scale", self.impulse_scale)
        _require_int("pending_numerator", self.pending_numerator)
        if not 0 <= self.pending_numerator < self.amplitude:
            raise ValueError(
                "pending_numerator must lie in the canonical nonnegative amplitude fiber"
            )


@dataclass(frozen=True)
class ContactMaterialImpulseEvent:
    before: ContactMaterialImpulseState
    response_sample: int
    quantization: MaterialImpulseQuantization
    after: ContactMaterialImpulseState

    @property
    def delivered_impulse(self) -> int:
        return self.quantization.impulse_quanta


@dataclass(frozen=True)
class ContactMaterialChannelSequence:
    before: ContactMaterialImpulseState
    responses: tuple[int, ...]
    events: tuple[ContactMaterialImpulseEvent, ...]
    delivered_impulse_total: int
    after: ContactMaterialImpulseState

    @property
    def response_total(self) -> int:
        return sum(self.responses)


@dataclass(frozen=True)
class ContactMaterialNetworkTick1D:
    before: ContactNetworkMomentum1D
    reservoir_before: tuple[ContactMaterialImpulseState, ...]
    channel_sequences: tuple[ContactMaterialChannelSequence, ...]
    delivered_impulse_vector: tuple[int, ...]
    network_step: ContactNetworkImpulseStep1D
    reservoir_after: tuple[ContactMaterialImpulseState, ...]

    @property
    def after(self) -> ContactNetworkMomentum1D:
        return self.network_step.after


def _validate_contact_reservoir(state: ContactMaterialImpulseState) -> None:
    if not isinstance(state, ContactMaterialImpulseState):
        raise TypeError("reservoir entries must be ContactMaterialImpulseState")


def _response_sequence(responses: Iterable[int]) -> tuple[int, ...]:
    values = tuple(responses)
    for response in values:
        _require_int("response", response)
        if response < 0:
            raise ValueError("contact material responses must be nonnegative")
    return values


def apply_contact_material_response(
    state: ContactMaterialImpulseState,
    response: int,
) -> ContactMaterialImpulseEvent:
    """Quantize one contact response through the canonical retained-detail kernel."""
    _validate_contact_reservoir(state)
    _require_int("response", response)
    if response < 0:
        raise ValueError("contact material response must be nonnegative")

    quantization = material_impulse_quantization(
        response_sample=response,
        amplitude=state.amplitude,
        signed_impulse_scale=state.impulse_scale,
        detail=state.pending_numerator,
    )
    if quantization.impulse_quanta < 0:
        raise AssertionError("positive contact channel delivered negative impulse")
    if not 0 <= quantization.detail_after < state.amplitude:
        raise AssertionError("positive contact detail left canonical nonnegative fiber")

    after = ContactMaterialImpulseState(
        amplitude=state.amplitude,
        impulse_scale=state.impulse_scale,
        pending_numerator=quantization.detail_after,
    )
    return ContactMaterialImpulseEvent(
        before=state,
        response_sample=response,
        quantization=quantization,
        after=after,
    )


def apply_contact_material_response_sequence(
    state: ContactMaterialImpulseState,
    responses: Iterable[int],
) -> ContactMaterialChannelSequence:
    """Apply one retained response sequence entirely inside one contact channel."""
    _validate_contact_reservoir(state)
    values = _response_sequence(responses)
    current = state
    events: list[ContactMaterialImpulseEvent] = []
    delivered_total = 0
    for response in values:
        event = apply_contact_material_response(current, response)
        events.append(event)
        delivered_total += event.delivered_impulse
        current = event.after

    if (
        state.amplitude * delivered_total + current.pending_numerator
        != state.pending_numerator + state.impulse_scale * sum(values)
    ):
        raise AssertionError("contact-local material impulse ledger failed")

    return ContactMaterialChannelSequence(
        before=state,
        responses=values,
        events=tuple(events),
        delivered_impulse_total=delivered_total,
        after=current,
    )


def apply_contact_material_response_sequences(
    network: ContactNetworkMomentum1D,
    reservoirs: Sequence[ContactMaterialImpulseState],
    response_sequences: Sequence[Iterable[int]],
) -> ContactMaterialNetworkTick1D:
    """Quantize every contact locally, then apply one integer impulse vector."""
    if not isinstance(network, ContactNetworkMomentum1D):
        raise TypeError("network must be ContactNetworkMomentum1D")
    reservoir_values = tuple(reservoirs)
    sequences = tuple(response_sequences)
    contact_count = len(network.contacts)
    if len(reservoir_values) != contact_count:
        raise ValueError("one material reservoir is required per contact")
    if len(sequences) != contact_count:
        raise ValueError("one response sequence is required per contact")
    for reservoir in reservoir_values:
        _validate_contact_reservoir(reservoir)

    channel_sequences = tuple(
        apply_contact_material_response_sequence(reservoir, responses)
        for reservoir, responses in zip(
            reservoir_values,
            sequences,
            strict=True,
        )
    )
    delivered = tuple(
        sequence.delivered_impulse_total for sequence in channel_sequences
    )
    if any(value < 0 for value in delivered):
        raise AssertionError("repulsive contact tick produced negative impulse")

    network_step = apply_contact_impulse_vector(network, delivered)
    if network_step.after.total_momentum != network.total_momentum:
        raise AssertionError("material contact tick changed total body momentum")

    return ContactMaterialNetworkTick1D(
        before=network,
        reservoir_before=reservoir_values,
        channel_sequences=channel_sequences,
        delivered_impulse_vector=delivered,
        network_step=network_step,
        reservoir_after=tuple(sequence.after for sequence in channel_sequences),
    )


def apply_contact_material_tick(
    network: ContactNetworkMomentum1D,
    reservoirs: Sequence[ContactMaterialImpulseState],
    responses: Sequence[int],
) -> ContactMaterialNetworkTick1D:
    """One response sample per contact, using the same local-first batched law."""
    response_values = tuple(responses)
    if len(response_values) != len(network.contacts):
        raise ValueError("one response value is required per contact")
    for response in response_values:
        _require_int("response", response)
        if response < 0:
            raise ValueError("contact material responses must be nonnegative")
    return apply_contact_material_response_sequences(
        network,
        reservoirs,
        tuple((response,) for response in response_values),
    )


def contact_material_segmentation_invariant(
    network: ContactNetworkMomentum1D,
    reservoirs: Sequence[ContactMaterialImpulseState],
    left_sequences: Sequence[Iterable[int]],
    right_sequences: Sequence[Iterable[int]],
) -> bool:
    """Exact invariance under per-contact response repartition with equal totals."""
    left_values = tuple(tuple(sequence) for sequence in left_sequences)
    right_values = tuple(tuple(sequence) for sequence in right_sequences)
    if len(left_values) != len(right_values):
        raise ValueError("response sequence families must have equal length")
    if any(
        sum(left) != sum(right)
        for left, right in zip(left_values, right_values, strict=True)
    ):
        raise ValueError(
            "segmentation comparison requires equal response total per contact"
        )

    left_tick = apply_contact_material_response_sequences(
        network,
        reservoirs,
        left_values,
    )
    right_tick = apply_contact_material_response_sequences(
        network,
        reservoirs,
        right_values,
    )
    same = (
        left_tick.delivered_impulse_vector == right_tick.delivered_impulse_vector
        and left_tick.reservoir_after == right_tick.reservoir_after
        and left_tick.after == right_tick.after
        and left_tick.network_step.relative_scores_after
        == right_tick.network_step.relative_scores_after
    )
    if not same:
        raise AssertionError(
            "retained contact-local detail failed segmentation invariance"
        )
    return True
