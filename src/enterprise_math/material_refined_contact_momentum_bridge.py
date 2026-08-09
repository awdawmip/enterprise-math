"""L3 bridge: refined contact impulses -> exact lifted body momentum state.

This module connects two E001 owner families without re-owning either theorem:

* contact-network algebra supplies the signed incidence ``B`` and coupling
  ``K=B^T D B`` for delivered contact impulses;
* response-precision owners may supply one impulse numerator ``a_e`` on a
  declared denominator ``s_e`` for each contact channel.

A refined impulse vector is not yet a body after-state unless body momentum can
represent those denominators.  Let each body currently have coarse whole
momentum ``p_i`` plus signed detail ``eta_i`` on one common momentum denominator
``m``:

    P_i = m*p_i + eta_i,      |eta_i| < m.

Put

    L = lcm(m, s_1, ..., s_E).

The unique least common exact lift is

    P_i^L = P_i * (L/m),
    delta P_i^L = sum_e B_ie * a_e * (L/s_e).

No rounding occurs.  Because every incidence column sums to zero, total lifted
body momentum is preserved.  On the same denominator the contact-score
numerators obey the exact owner-compatible update

    r'^L_e = r^L_e + sum_f K_ef * a_f * (L/s_f).

Thus denominator refinement in branching-contact response becomes an actual
physical-state refinement exactly when the body momentum state is lifted to the
common divisibility lattice.  A numerically larger non-multiple denominator is
not automatically a refinement.

The LCM/divisibility arithmetic and incidence identity are standard mathematics.
This file is only the thin E001 cross-owner state interface; it does not claim
new contact-network, star-response, or rational-arithmetic theory.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import lcm

from .material_contact_network_impulse_1d import (
    ContactNetworkMomentum1D,
    contact_coupling_gram,
    contact_incidence_matrix,
)


def _positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


def _integer(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        raise ValueError(f"{name} must be an integer")


def _signed_toward_zero_divmod(value: int, divisor: int) -> tuple[int, int]:
    _integer("value", value)
    _positive("divisor", divisor)
    quotient = value // divisor if value >= 0 else -((-value) // divisor)
    remainder = value - divisor * quotient
    if abs(remainder) >= divisor:
        raise AssertionError("signed momentum detail escaped denominator cell")
    return quotient, remainder


@dataclass(frozen=True)
class RefinedContactMomentumBridgeReport:
    momentum_denominator_before: int
    impulse_denominators: tuple[int, ...]
    common_denominator: int
    contact_scale_factors: tuple[int, ...]
    body_numerators_before: tuple[int, ...]
    body_delta_numerators: tuple[int, ...]
    body_numerators_after: tuple[int, ...]
    whole_momenta_after: tuple[int, ...]
    momentum_details_after: tuple[int, ...]
    contact_score_numerators_before: tuple[int, ...]
    contact_score_numerators_after: tuple[int, ...]
    contact_score_numerators_expected: tuple[int, ...]
    total_momentum_numerator_before: int
    total_momentum_numerator_after: int

    @property
    def denominator_refined(self) -> bool:
        return self.common_denominator != self.momentum_denominator_before


def minimum_contact_momentum_denominator(
    momentum_denominator: int,
    impulse_denominators: tuple[int, ...] | list[int],
) -> int:
    """Least common body-momentum denominator carrying all contact impulses."""
    _positive("momentum_denominator", momentum_denominator)
    result = momentum_denominator
    for denominator in impulse_denominators:
        _positive("impulse_denominator", denominator)
        result = lcm(result, denominator)
    return result


def apply_refined_contact_impulses_to_lifted_momentum(
    state: ContactNetworkMomentum1D,
    momentum_denominator: int,
    momentum_detail_numerators: tuple[int, ...] | list[int],
    impulse_numerators: tuple[int, ...] | list[int],
    impulse_denominators: tuple[int, ...] | list[int],
) -> RefinedContactMomentumBridgeReport:
    """Apply refined repulsive contact impulses on the unique least common lift."""
    _positive("momentum_denominator", momentum_denominator)
    details = tuple(momentum_detail_numerators)
    impulses = tuple(impulse_numerators)
    denominators = tuple(impulse_denominators)
    if len(details) != len(state.momenta):
        raise ValueError("momentum details must match body count")
    if len(impulses) != len(state.contacts) or len(denominators) != len(state.contacts):
        raise ValueError("impulse numerators/denominators must match contact count")
    for detail in details:
        _integer("momentum_detail", detail)
        if abs(detail) >= momentum_denominator:
            raise ValueError("momentum detail must lie strictly inside one denominator cell")
    for impulse in impulses:
        _integer("impulse_numerator", impulse)
        if impulse < 0:
            raise ValueError("repulsive impulse numerators must be non-negative")
    for denominator in denominators:
        _positive("impulse_denominator", denominator)

    common = minimum_contact_momentum_denominator(
        momentum_denominator,
        denominators,
    )
    momentum_scale = common // momentum_denominator
    contact_scales = tuple(common // denominator for denominator in denominators)
    before = tuple(
        (momentum_denominator * whole + detail) * momentum_scale
        for whole, detail in zip(state.momenta, details)
    )

    incidence = contact_incidence_matrix(state)
    delta = tuple(
        sum(
            incidence[body][edge]
            * impulses[edge]
            * contact_scales[edge]
            for edge in range(len(state.contacts))
        )
        for body in range(len(state.momenta))
    )
    after = tuple(value + change for value, change in zip(before, delta))
    whole_detail = tuple(
        _signed_toward_zero_divmod(value, common)
        for value in after
    )
    whole_after = tuple(item[0] for item in whole_detail)
    detail_after = tuple(item[1] for item in whole_detail)

    weights = state.body_scale_weights
    before_scores = tuple(
        sum(
            incidence[body][edge] * weights[body] * before[body]
            for body in range(len(state.momenta))
        )
        for edge in range(len(state.contacts))
    )
    after_scores = tuple(
        sum(
            incidence[body][edge] * weights[body] * after[body]
            for body in range(len(state.momenta))
        )
        for edge in range(len(state.contacts))
    )
    gram = contact_coupling_gram(state)
    expected_scores = tuple(
        before_scores[row]
        + sum(
            gram[row][col] * impulses[col] * contact_scales[col]
            for col in range(len(state.contacts))
        )
        for row in range(len(state.contacts))
    )
    if after_scores != expected_scores:
        raise AssertionError("lifted contact scores disagree with exact r'=r+Kj scaling")

    total_before = sum(before)
    total_after = sum(after)
    if total_before != total_after:
        raise AssertionError("lifted contact update changed total body momentum numerator")
    for edge in range(len(state.contacts)):
        if sum(incidence[body][edge] for body in range(len(state.momenta))) != 0:
            raise AssertionError("contact incidence column lost zero-sum conservation")

    return RefinedContactMomentumBridgeReport(
        momentum_denominator_before=momentum_denominator,
        impulse_denominators=denominators,
        common_denominator=common,
        contact_scale_factors=contact_scales,
        body_numerators_before=before,
        body_delta_numerators=delta,
        body_numerators_after=after,
        whole_momenta_after=whole_after,
        momentum_details_after=detail_after,
        contact_score_numerators_before=before_scores,
        contact_score_numerators_after=after_scores,
        contact_score_numerators_expected=expected_scores,
        total_momentum_numerator_before=total_before,
        total_momentum_numerator_after=total_after,
    )
