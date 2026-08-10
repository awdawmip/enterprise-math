"""Exact activation bit for the P025 projective capacity observable.

The threshold query ``sigma_proj >= 1`` is much coarser than the projective
value itself.  Stage 64 plus de Bruijn radical counting shows externally that
this activated state is sparse: O_epsilon(X^(1+epsilon)) on a dyadic height
range, against Theta(X^2) ambient additive triples.

This module stores only exact finite classification and the equivalent cyclic
subunit inequalities.  It does not implement or re-prove the external counting
theorem.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction

from .abc_projective_capacity_condition import projective_capacity_condition_state


@dataclass(frozen=True)
class ProjectiveActivationState:
    abc: tuple[int, int, int]
    sigma_projective: Fraction
    activated: bool
    cyclic_subunit: tuple[bool, bool, bool]
    active_cyclic_indices: tuple[int, ...]


def projective_activation_state(a: int, b: int, c: int) -> ProjectiveActivationState:
    """Return the exact threshold-one projective state.

    Cyclic indices use the P025 stored order ``(c,b,a)``.
    """
    state = projective_capacity_condition_state(a, b, c)
    subunit = tuple(value < 1 for value in state.cyclic_weighted_defects)
    active = tuple(i for i, value in enumerate(state.cyclic_weighted_defects) if value >= 1)
    activated = state.sigma_projective >= 1
    if activated != bool(active):
        raise AssertionError("projective activation bit disagrees with cyclic thresholds")
    if (not activated) != all(subunit):
        raise AssertionError("subunit basin equivalence failed")
    return ProjectiveActivationState(
        abc=(a, b, c),
        sigma_projective=state.sigma_projective,
        activated=activated,
        cyclic_subunit=subunit,
        active_cyclic_indices=active,
    )


def same_activation_different_projective_value() -> dict[str, object]:
    """Show activation is strictly coarser than the full projective scalar."""
    first = projective_activation_state(1, 2, 3)
    second = projective_activation_state(1, 3, 4)
    if not first.activated or not second.activated:
        raise AssertionError("activation collision changed")
    if first.sigma_projective == second.sigma_projective:
        raise AssertionError("activation failed to erase projective value")
    return {
        "first": first,
        "second": second,
        "shared_activation": True,
        "projective_values": (first.sigma_projective, second.sigma_projective),
    }
