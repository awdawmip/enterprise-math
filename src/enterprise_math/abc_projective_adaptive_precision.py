"""Adaptive dyadic precision level for the P025 projective observable.

Define level zero for the subunit basin and open one additional refinement level
whenever sigma_proj crosses 1,2,4,8,... .  Thus

    L(sigma) = 0                         if sigma < 1,
               1 + floor(log_2 sigma)   if sigma >= 1.

Equivalently, L(sigma) is the number of dyadic threshold queries
``sigma>=2^k`` answered true.  Stage 64's external de-Bruijn tail then implies
an aggregate O_epsilon(X^(1+epsilon)) refinement budget on a dyadic height
universe containing Theta(X^2) additive states.

The asymptotic theorem uses external prior art; this module stores only the
exact finite level and threshold language.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction

from .abc_projective_capacity_condition import projective_capacity_condition_state


@dataclass(frozen=True)
class AdaptiveProjectivePrecisionState:
    abc: tuple[int, int, int]
    sigma_projective: Fraction
    level: int
    crossed_thresholds: tuple[int, ...]
    next_threshold: int


def dyadic_projective_precision_level_from_fraction(value: Fraction) -> int:
    """Return the exact dyadic refinement level of a positive rational value."""
    if value <= 0:
        raise ValueError("projective value must be positive")
    if value < 1:
        return 0
    level = 0
    threshold = 1
    while value >= threshold:
        level += 1
        threshold *= 2
    return level


def adaptive_projective_precision_state(
    a: int, b: int, c: int
) -> AdaptiveProjectivePrecisionState:
    state = projective_capacity_condition_state(a, b, c)
    level = dyadic_projective_precision_level_from_fraction(state.sigma_projective)
    crossed = tuple(1 << k for k in range(level))
    next_threshold = 1 << level
    if any(state.sigma_projective < threshold for threshold in crossed):
        raise AssertionError("stored crossed projective threshold was not crossed")
    if state.sigma_projective >= next_threshold:
        raise AssertionError("next projective threshold should be the first false query")
    return AdaptiveProjectivePrecisionState(
        abc=(a, b, c),
        sigma_projective=state.sigma_projective,
        level=level,
        crossed_thresholds=crossed,
        next_threshold=next_threshold,
    )


def level_is_sum_of_threshold_bits(value: Fraction) -> bool:
    """Verify the exact finite layer-cake identity for dyadic query bits."""
    level = dyadic_projective_precision_level_from_fraction(value)
    bits = sum(1 for k in range(level + 2) if value >= (1 << k))
    if bits != level:
        raise AssertionError("dyadic level failed threshold-bit identity")
    return True
