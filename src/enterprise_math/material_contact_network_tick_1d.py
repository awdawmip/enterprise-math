"""Exact multi-contact material-response tick for the E001 integer momentum world.

This bridge composes two already-established layers without changing either:

1. every named contact owns its own retained material impulse reservoir;
2. delivered nonnegative contact impulse quanta act on the body network by
   ``p' = p+Bj`` and ``r' = r+Kj``.

One contact channel ``e`` carries a ``MaterialImpulseState`` with amplitude
``A_e``, positive impulse scale ``S_e`` and pending numerator ``delta_e``.  A
finite nonnegative response sequence on that contact satisfies the exact ledger

    A_e * J_e + delta'_e
      = delta_e + S_e * sum(response_e),

where ``J_e`` is the total integer impulse delivered by that channel during the
tick.  Each contact is quantized independently; only the delivered integer
vector ``J`` enters the contact network.

After all local reservoirs have been processed, one declared **batched material
tick** applies the complete delivered vector at once:

    p' = p + B J,
    r' = r + K J.

This policy keeps three operations distinct:

    raw material response
      -> contact-local retained detail
      -> integer delivered contact impulse
      -> network momentum update.

No raw/pending numerators are pooled across contacts.  Splitting one contact's
response into subevents does not change its final reservoir state or total
integer impulse, provided all detail is retained.  Consequently the batched
network after-state is also invariant under such within-channel segmentation.

The batched policy is intentionally unguarded at the network-application stage.
Linear contact impulse additions commute there.  If one instead re-checks
state-dependent contact guards between delivered units, that is the different
causal action language studied by the guarded-contact owner and may be
order-sensitive.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Sequence

from .material_contact_network_impulse_1d import (
    ContactNetworkImpulseStep1D,
    ContactNetworkMomentum1D,
    apply_contact_impulse_vector,
)
from .material_impulse_accounting import (
    MaterialImpulseEvent,
    MaterialImpulseState,
    apply_material_response,
)


@dataclass(frozen=True)
class ContactMaterialChannelSequence:
    before: MaterialImpulseState
    responses: tuple[int, ...]
    events: tuple[MaterialImpulseEvent, ...]
    delivered_impulse_total: int
    after: MaterialImpulseState

    @property
    def response_total(self) -> int:
        return sum(self.responses)


@dataclass(frozen=True)
class ContactMaterialNetworkTick1D:
    before: ContactNetworkMomentum1D
    reservoir_before: tuple[MaterialImpulseState, ...]
    channel_sequences: tuple[ContactMaterialChannelSequence, ...]
    delivered_impulse_vector: tuple[int, ...]
    network_step: ContactNetworkImpulseStep1D
    reservoir_after: tuple[MaterialImpulseState, ...]

    @property
    def after(self) -> ContactNetworkMomentum1D:
        return self.network_step.after


def _require_int(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f"{name} must be an integer")


def _validate_contact_reservoir(
    state: MaterialImpulseState,
) -> None:
    if not isinstance(state, MaterialImpulseState):
        raise TypeError("reservoir entries must be MaterialImpulseState")
    if state.impulse_scale <= 0:
        raise ValueError(
            "contact material tick requires positive repulsive impulse_scale"
        )
    if not 0 <= state.pending_numerator < state.amplitude:
        raise ValueError(
            "contact material tick requires canonical nonnegative local remainder"
        )


def _response_sequence(
    responses: Iterable[int],
) -> tuple[int, ...]:
    values = tuple(responses)
    for response in values:
        _require_int("response", response)
        if response < 0:
            raise ValueError("contact material responses must be nonnegative")
    return values


def apply_contact_material_response_sequence(
    state: MaterialImpulseState,
    responses: Iterable[int],
) -> ContactMaterialChannelSequence:
    """Apply one retained response sequence entirely inside one contact channel."""
    _validate_contact_reservoir(state)
    values = _response_sequence(responses)
    current = state
    events = []
    delivered_total = 0
    for response in values:
        event = apply_material_response(current, response)
        if event.delivered_impulse < 0:
            raise AssertionError(
                "positive contact channel unexpectedly delivered negative impulse"
            )
        events.append(event)
        delivered_total += event.delivered_impulse
        current = event.after

    if (
        state.amplitude * delivered_total
        + current.pending_numerator
        != state.pending_numerator
        + state.impulse_scale * sum(values)
    ):
        raise AssertionError("contact-local material impulse ledger failed")
    if not 0 <= current.pending_numerator < current.amplitude:
        raise AssertionError("contact-local remainder left canonical range")

    return ContactMaterialChannelSequence(
        before=state,
        responses=values,
        events=tuple(events),
        delivered_impulse_total=delivered_total,
        after=current,
    )


def apply_contact_material_response_sequences(
    network: ContactNetworkMomentum1D,
    reservoirs: Sequence[MaterialImpulseState],
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

    channel_sequences = tuple(
        apply_contact_material_response_sequence(
            reservoir,
            responses,
        )
        for reservoir, responses in zip(
            reservoir_values,
            sequences,
            strict=True,
        )
    )
    delivered = tuple(
        sequence.delivered_impulse_total
        for sequence in channel_sequences
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
        reservoir_after=tuple(
            sequence.after
            for sequence in channel_sequences
        ),
    )


def apply_contact_material_tick(
    network: ContactNetworkMomentum1D,
    reservoirs: Sequence[MaterialImpulseState],
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
    reservoirs: Sequence[MaterialImpulseState],
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
        for left, right in zip(
            left_values,
            right_values,
            strict=True,
        )
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
        left_tick.delivered_impulse_vector
        == right_tick.delivered_impulse_vector
        and left_tick.reservoir_after
        == right_tick.reservoir_after
        and left_tick.after == right_tick.after
        and left_tick.network_step.relative_scores_after
        == right_tick.network_step.relative_scores_after
    )
    if not same:
        raise AssertionError(
            "retained contact-local detail failed segmentation invariance"
        )
    return True
