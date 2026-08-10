"""De Bruijn bridge for the full P025 projective-capacity tail.

For a dyadic height range X/2<c<=X and threshold T>=1, a non-unit state with
``sigma_proj>=T`` forces a pair of distinct components x,y with

    m(x)m(y) >= T*c/2.

Thus ``rad(xy) <= 2*x*y/(T*c) < 4X/T``.  Classical de Bruijn radical counting,
applied externally to the pair product xy<=X^2, yields the asymptotic tail

    N_X(sigma_proj>=T) <<_epsilon X^(1+epsilon)/T.

The same scale holds in the unit slice using the one-component Stage-50
residual.  De Bruijn counting and the divisor bound are prior art and are not
proved by this module.  We store the exact finite reduction and the resulting
formal moment threshold only.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction

from .abc_projective_capacity_condition import projective_capacity_condition_state
from .abc_support import multiplicity_residual, radical


@dataclass(frozen=True)
class ProjectiveTailPairState:
    abc: tuple[int, int, int]
    threshold: int
    failing_cyclic_index: int
    component_indices: tuple[int, int]
    component_values: tuple[int, int]
    residual_product: int
    pair_radical_product: int


def projective_tail_pair_state(
    a: int, b: int, c: int, threshold: int
) -> ProjectiveTailPairState | None:
    """Return the paired state forced by ``sigma_proj>=threshold`` for a,b>1."""
    if isinstance(threshold, bool) or not isinstance(threshold, int) or threshold < 1:
        raise ValueError("threshold must be an integer >=1")
    if a <= 1 or b <= 1:
        raise ValueError("paired tail state requires a,b>1")
    state = projective_capacity_condition_state(a, b, c)
    if state.sigma_projective < threshold:
        return None

    residuals = tuple(multiplicity_residual(n) for n in (a, b, c))
    values = (a, b, c)
    component_for_ratio = (2, 1, 0)  # cyclic ratio order c,b,a
    for cyclic_index, (ratio, component_index) in enumerate(
        zip(state.cyclic_weighted_defects, component_for_ratio, strict=True)
    ):
        if ratio < threshold:
            continue
        partner = (0 if a >= b else 1) if component_index == 2 else 2
        residual_product = residuals[component_index] * residuals[partner]
        if 2 * residual_product < threshold * c:
            raise AssertionError("projective threshold lost paired residual pressure")
        x, y = values[component_index], values[partner]
        pair_radical = radical(x) * radical(y)
        if pair_radical * residual_product != x * y:
            raise AssertionError("pair radical/residual product identity failed")
        return ProjectiveTailPairState(
            abc=(a, b, c),
            threshold=threshold,
            failing_cyclic_index=cyclic_index,
            component_indices=(component_index, partner),
            component_values=(x, y),
            residual_product=residual_product,
            pair_radical_product=pair_radical,
        )
    raise AssertionError("projective max above threshold exposed no cyclic term")


def dyadic_pair_radical_envelope_holds(
    state: ProjectiveTailPairState, X: int
) -> bool:
    """Verify the exact finite inequality behind ``rad(xy)<4X/T``."""
    if not X // 2 < state.abc[2] <= X:
        raise ValueError("state must lie in the declared dyadic c-range")
    x, y = state.component_values
    # Strong exact form from m(x)m(y)>=T*c/2:
    if state.threshold * state.abc[2] * state.pair_radical_product > 2 * x * y:
        raise AssertionError("pair radical exceeded exact threshold envelope")
    # Coarser dyadic form, cross-multiplied to avoid fractions.
    if state.threshold * state.pair_radical_product >= 4 * X:
        # Strict c>X/2 gives a strict <4X/T bound.
        raise AssertionError("pair radical exceeded dyadic 4X/T envelope")
    return True


def projective_tail_external_power() -> tuple[int, int]:
    """Return formal powers ``X^(1+eps) * T^(-1)`` of the de Bruijn tail."""
    return 1, -1


def normalized_projective_moment_bounded_range(
    numerator: int, denominator: int
) -> bool:
    """Return whether the external tail implies an X^2-normalized theta moment bound.

    The tail ``X^(1+eps)/T`` and trivial ``sigma_proj<=X`` imply uniform
    X^2-normalized moments for every fixed theta<2 after choosing epsilon small
    relative to ``2-theta``.  This records the exponent calculus only.
    """
    if denominator <= 0 or numerator <= 0:
        raise ValueError("moment order must be positive")
    theta = Fraction(numerator, denominator)
    return theta < 2
