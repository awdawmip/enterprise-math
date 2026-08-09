"""Exact zero-score plastic precision lattice for a closing weighted contact path.

For a canonical 1D path of positive masses and a state whose contact scores are
all non-positive, the exact rational impulse that makes every final contact score
zero can be written without matrix inversion.

Let

    M = sum_i m_i,          P = sum_i p_i,

and for contact k (prefix bodies 0..k)

    M_k = sum_{i<=k} m_i,
    P_k = sum_{i<=k} p_i,
    N_k = P_k*M - M_k*P.

Zero final relative scores mean one common final velocity, so final body momentum
is ``m_i*P/M``.  Contact k transfers exactly the excess prefix momentum

    j_k* = P_k - M_k*P/M = N_k/M.

For a closing path these transfers are non-negative.  A denominator ``s`` carries
the exact zero-score response iff every ``s*N_k/M`` is integral.  Therefore the
least exact denominator is

    g = gcd(M,N_1,...,N_n),
    s_plastic = M/g,

and the exact impulse numerators there are simply ``a_k=N_k/g``.

Every divisibility refinement ``m*s_plastic`` carries the same physical response
by multiplying all numerators by ``m``.  At ``s_plastic`` the integer
least-action solver must return this exact vector and all final contact scores are
zero.  The kinetic metric is non-increasing because this is the common-velocity
projection; algebraically ``r=-Kj`` and

    Delta E = 2 j^T r + j^T K j = -j^T K j <= 0.

This exact-plastic denominator is not necessarily the *first* passive denominator.
Coarser nonzero-score responses can already be passive; the separate single-contact
passivity threshold records that distinction.

The center-of-mass/common-velocity construction and gcd arithmetic are standard.
This file is an E001 precision specialization joining weighted-path response,
passivity and the divisibility-lattice view.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import gcd

from .material_contact_network_impulse_1d import (
    ContactChannel1D,
    ContactNetworkMomentum1D,
    apply_contact_impulse_vector,
    contact_coupling_gram,
    contact_relative_scores,
)
from .material_weighted_chain_least_action_1d import solve_weighted_chain_least_action


def _validate_closing_path(state: ContactNetworkMomentum1D) -> None:
    contact_count = len(state.contacts)
    if contact_count < 1 or len(state.masses) != contact_count + 1:
        raise ValueError("plastic precision theorem requires a nonempty path")
    expected = tuple(
        ContactChannel1D(index, index + 1, 1)
        for index in range(contact_count)
    )
    if state.contacts != expected:
        raise ValueError("plastic precision theorem requires canonical consecutive +1 contacts")
    if any(score > 0 for score in contact_relative_scores(state)):
        raise ValueError("plastic precision theorem requires no initially separating contact")


@dataclass(frozen=True)
class WeightedPathPlasticPrecisionReport:
    total_mass: int
    total_momentum: int
    prefix_mass_momentum_numerators: tuple[int, ...]
    gcd_resource: int
    minimum_exact_denominator: int
    exact_impulse_numerators: tuple[int, ...]
    final_momentum_numerators: tuple[int, ...]
    final_contact_score_numerators: tuple[int, ...]
    kinetic_change_numerator: int

    @property
    def passive(self) -> bool:
        return self.kinetic_change_numerator <= 0


def weighted_path_plastic_precision_report(
    state: ContactNetworkMomentum1D,
) -> WeightedPathPlasticPrecisionReport:
    """Return the least denominator carrying the exact zero-score path response."""
    _validate_closing_path(state)
    total_mass = sum(state.masses)
    total_momentum = sum(state.momenta)
    prefix_mass = 0
    prefix_momentum = 0
    numerators: list[int] = []
    for mass, momentum in zip(state.masses[:-1], state.momenta[:-1]):
        prefix_mass += mass
        prefix_momentum += momentum
        numerator = prefix_momentum * total_mass - prefix_mass * total_momentum
        if numerator < 0:
            raise AssertionError("closing path produced negative plastic prefix transfer")
        numerators.append(numerator)

    resource = total_mass
    for numerator in numerators:
        resource = gcd(resource, numerator)
    denominator = total_mass // resource
    impulses = tuple(numerator // resource for numerator in numerators)

    scaled_state = ContactNetworkMomentum1D(
        masses=state.masses,
        momenta=tuple(denominator * value for value in state.momenta),
        contacts=state.contacts,
    )
    step = apply_contact_impulse_vector(scaled_state, impulses)
    if any(step.relative_scores_after):
        raise AssertionError("exact plastic denominator failed zero final contact scores")
    least = solve_weighted_chain_least_action(scaled_state)
    if least.impulse_vector != impulses:
        raise AssertionError("exact plastic vector disagrees with integer least-action response")

    weights = state.body_scale_weights
    before_energy = sum(
        weight * value * value
        for weight, value in zip(weights, scaled_state.momenta)
    )
    after_energy = sum(
        weight * value * value
        for weight, value in zip(weights, step.after.momenta)
    )
    energy_change = after_energy - before_energy
    gram = contact_coupling_gram(state)
    quadratic_loss = -sum(
        impulses[row] * gram[row][col] * impulses[col]
        for row in range(len(impulses))
        for col in range(len(impulses))
    )
    if energy_change != quadratic_loss:
        raise AssertionError("exact path plastic response lost kinetic projection identity")
    if energy_change > 0:
        raise AssertionError("exact zero-score path response injected kinetic energy")

    expected_final = tuple(
        mass * total_momentum // resource
        for mass in state.masses
    )
    # ``resource`` divides every mass*P by the exact integrality construction.
    if step.after.momenta != expected_final:
        raise AssertionError("exact plastic response disagrees with common-velocity momentum")

    return WeightedPathPlasticPrecisionReport(
        total_mass=total_mass,
        total_momentum=total_momentum,
        prefix_mass_momentum_numerators=tuple(numerators),
        gcd_resource=resource,
        minimum_exact_denominator=denominator,
        exact_impulse_numerators=impulses,
        final_momentum_numerators=step.after.momenta,
        final_contact_score_numerators=step.relative_scores_after,
        kinetic_change_numerator=energy_change,
    )


def exact_plastic_response_at_refinement(
    state: ContactNetworkMomentum1D,
    refinement_multiplier: int,
) -> tuple[int, tuple[int, ...]]:
    """Return denominator/numerators at one true divisibility refinement."""
    if (
        isinstance(refinement_multiplier, bool)
        or not isinstance(refinement_multiplier, int)
        or refinement_multiplier <= 0
    ):
        raise ValueError("refinement_multiplier must be a positive integer")
    report = weighted_path_plastic_precision_report(state)
    return (
        report.minimum_exact_denominator * refinement_multiplier,
        tuple(
            refinement_multiplier * value
            for value in report.exact_impulse_numerators
        ),
    )
