"""Divisibility-refinement monotonicity of weighted-path least-action passivity.

For a closing weighted contact path, let ``K`` be the nonsingular path
M-matrix and ``r<=0`` its coarse contact score.  At impulse denominator ``s``
the integer least-action owner solves

    s*r + K*j_s >= 0

with the unique componentwise-least non-negative integer vector ``j_s``.

Let the exact rational zero-score response be

    x_s = -K^{-1}(s*r),

and write the integer overshoot error

    e_s = j_s - x_s.

Because ``K^{-1}>=0`` for this path M-matrix, every feasible response is
componentwise at least ``x_s``; hence ``e_s>=0``.  Its final score is

    K e_s = s*r + K*j_s >= 0.

Now take a true precision refinement ``s' = m*s``.  The scaled coarse response
``m*j_s`` is feasible at ``s'``, so least action gives

    j_{m s} <= m*j_s.

Since ``x_{m s}=m*x_s``:

    0 <= e_{m s} <= m*e_s,
    K e_{m s} >= 0,
    K(m e_s) >= 0.

Put ``d=m e_s-e_{m s}>=0``.  Then

    (m e_s)^T K(m e_s) - e_{m s}^T K e_{m s}
      = d^T K(m e_s+e_{m s}) >= 0.

The common-denominator kinetic numerator change is

    Delta_s = 2 j_s^T(s r) + j_s^T K j_s
            = -x_s^T K x_s + e_s^T K e_s.

Therefore exactly

    Delta_{m s} <= m^2 Delta_s.

Dividing by the positive squared momentum denominator shows normalized kinetic
change is non-increasing along the divisibility refinement order.  In
particular, once the least-action path response is passive at one denominator,
every true refinement multiple remains passive.

This statement is specific to the weighted path Z/M-matrix least-action
structure.  It is not claimed for arbitrary contact topology or for numerically
larger non-multiple denominators.
"""

from __future__ import annotations

from dataclasses import dataclass

from .material_contact_network_impulse_1d import (
    ContactNetworkMomentum1D,
    contact_coupling_gram,
    contact_relative_scores,
)
from .material_weighted_chain_least_action_1d import solve_weighted_chain_least_action


def _positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


def _scaled_state(
    state: ContactNetworkMomentum1D,
    denominator: int,
) -> ContactNetworkMomentum1D:
    return ContactNetworkMomentum1D(
        masses=state.masses,
        momenta=tuple(denominator * value for value in state.momenta),
        contacts=state.contacts,
    )


def _kinetic_change_from_contact_data(
    scores: tuple[int, ...],
    gram: tuple[tuple[int, ...], ...],
    impulses: tuple[int, ...],
) -> int:
    return (
        2 * sum(value * score for value, score in zip(impulses, scores))
        + sum(
            impulses[row] * gram[row][col] * impulses[col]
            for row in range(len(impulses))
            for col in range(len(impulses))
        )
    )


@dataclass(frozen=True)
class WeightedPathPassivityRefinementReport:
    coarse_denominator: int
    refinement_multiplier: int
    fine_denominator: int
    coarse_impulse_numerators: tuple[int, ...]
    fine_impulse_numerators: tuple[int, ...]
    scaled_coarse_impulse_numerators: tuple[int, ...]
    coarse_final_score_numerators: tuple[int, ...]
    fine_final_score_numerators: tuple[int, ...]
    coarse_kinetic_change_numerator: int
    fine_kinetic_change_numerator: int
    normalized_change_cross_inequality_holds: bool
    coarse_passive: bool
    fine_passive: bool


def weighted_path_passivity_refinement_report(
    state: ContactNetworkMomentum1D,
    coarse_denominator: int,
    refinement_multiplier: int,
) -> WeightedPathPassivityRefinementReport:
    """Verify exact normalized passivity monotonicity on one divisibility step."""
    _positive("coarse_denominator", coarse_denominator)
    _positive("refinement_multiplier", refinement_multiplier)
    fine_denominator = coarse_denominator * refinement_multiplier

    coarse_state = _scaled_state(state, coarse_denominator)
    fine_state = _scaled_state(state, fine_denominator)
    coarse = solve_weighted_chain_least_action(coarse_state)
    fine = solve_weighted_chain_least_action(fine_state)
    scaled_coarse = tuple(
        refinement_multiplier * value
        for value in coarse.impulse_vector
    )
    if any(
        fine_value > scaled_value
        for fine_value, scaled_value in zip(fine.impulse_vector, scaled_coarse)
    ):
        raise AssertionError("fine least-action response exceeded scaled coarse feasible response")

    gram = contact_coupling_gram(state)
    coarse_scores = contact_relative_scores(coarse_state)
    fine_scores = contact_relative_scores(fine_state)
    coarse_change = _kinetic_change_from_contact_data(
        coarse_scores, gram, coarse.impulse_vector
    )
    fine_change = _kinetic_change_from_contact_data(
        fine_scores, gram, fine.impulse_vector
    )
    inequality = (
        fine_change
        <= refinement_multiplier * refinement_multiplier * coarse_change
    )
    if not inequality:
        raise AssertionError("weighted-path normalized passivity worsened under true refinement")
    coarse_passive = coarse_change <= 0
    fine_passive = fine_change <= 0
    if coarse_passive and not fine_passive:
        raise AssertionError("weighted-path passivity was lost under divisibility refinement")

    return WeightedPathPassivityRefinementReport(
        coarse_denominator=coarse_denominator,
        refinement_multiplier=refinement_multiplier,
        fine_denominator=fine_denominator,
        coarse_impulse_numerators=coarse.impulse_vector,
        fine_impulse_numerators=fine.impulse_vector,
        scaled_coarse_impulse_numerators=scaled_coarse,
        coarse_final_score_numerators=coarse.final_scores,
        fine_final_score_numerators=fine.final_scores,
        coarse_kinetic_change_numerator=coarse_change,
        fine_kinetic_change_numerator=fine_change,
        normalized_change_cross_inequality_holds=inequality,
        coarse_passive=coarse_passive,
        fine_passive=fine_passive,
    )
