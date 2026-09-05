"""Binary branch first-return / predictive-memory calculus.

Research-harvest extension of the existing Enterprise Math BRC, predictive-quotient,
and graded-precision tool families.

The declared process has two concrete branch witnesses. A branch-resolved history
is summarized by the signed multiplicity imbalance z=#A-#B. Swapping the two
witnesses sends z to -z; an unlabeled first-balance-return observer therefore sees
only d=|z|.

For remaining horizon h the exact unlabeled predictive quotient is

    Q_h = {0,1,...,h,FAR_h}.

One branch step lowers the remaining horizon, so the operation-safe finite dynamics
is graded: K_h : Q_h -> Prob(Q_{h-1}). The full nonnegative counter factors
exactly through every Q_h, and the horizon projections commute with the kernels.

This module deliberately does not promote the process to native/G0 semantics.
It is a derived branch/path-memory tool. Positive/unlabeled projection forgets
the sign of the branch majority.
"""
from __future__ import annotations

from fractions import Fraction
from math import comb
from typing import Final

FAR: Final[str] = "FAR"
PredictiveState = int | str


def _require_nonnegative(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a nonnegative integer")


def _require_positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


def catalan(n: int) -> int:
    """Return the exact nth Catalan number."""
    _require_nonnegative("n", n)
    return comb(2 * n, n) // (n + 1)


def first_balance_return_count(n: int) -> int:
    """Two-letter words whose first nonempty balance occurs at length 2n."""
    _require_positive("n", n)
    return 2 * catalan(n - 1)


def first_return_mass(n: int) -> Fraction:
    """Normalized first-balance-return mass under equal branch mass 1/2."""
    _require_positive("n", n)
    return Fraction(catalan(n - 1), 2 ** (2 * n - 1))


def signed_memory(left_count: int, right_count: int) -> int:
    """Coordinate of Z^D/Z*1 after temporarily labeling the two witnesses."""
    _require_nonnegative("left_count", left_count)
    _require_nonnegative("right_count", right_count)
    return left_count - right_count


def swap_memory(z: int) -> int:
    """Witness-swap action on the signed memory coordinate."""
    if isinstance(z, bool) or not isinstance(z, int):
        raise TypeError("z must be an integer")
    return -z


def unlabeled_memory(z: int) -> int:
    """Canonical swap-orbit predictive coordinate |z|."""
    if isinstance(z, bool) or not isinstance(z, int):
        raise TypeError("z must be an integer")
    return abs(z)


def first_hit_count(distance: int, steps: int) -> int:
    """Number of +/-1 continuations first hitting zero exactly after steps.

    State zero is terminal. For distance d>0, the ballot/reflection count is

        d/steps * C(steps, (steps-d)/2)

    when parity/range permit it.
    """
    _require_nonnegative("distance", distance)
    _require_nonnegative("steps", steps)
    if distance == 0:
        return int(steps == 0)
    if steps == 0 or steps < distance or (steps - distance) % 2:
        return 0
    numerator = distance * comb(steps, (steps - distance) // 2)
    if numerator % steps:
        raise AssertionError("ballot count lost integrality")
    return numerator // steps


def first_hit_mass(distance: int, steps: int) -> Fraction:
    """Equal-branch mass of first hitting zero after steps."""
    return Fraction(first_hit_count(distance, steps), 2**steps)


def predictive_signature(distance: int, horizon: int) -> tuple[int, ...]:
    """Unlabeled first-hit count signature through one future horizon."""
    _require_nonnegative("distance", distance)
    _require_nonnegative("horizon", horizon)
    return tuple(first_hit_count(distance, steps) for steps in range(horizon + 1))


def finite_horizon_unlabeled_class_count(horizon: int) -> int:
    """Exact unlabeled predictive classes: 0..h plus one far class."""
    _require_nonnegative("horizon", horizon)
    return horizon + 2


def finite_horizon_resolved_class_count(horizon: int) -> int:
    """Exact labeled-future classes: z=-h..h plus one beyond-horizon class."""
    _require_nonnegative("horizon", horizon)
    return 2 * horizon + 2


def quotient_label(horizon: int, distance: int) -> PredictiveState:
    """Project a nonnegative counter to Q_h={0,...,h,FAR}."""
    _require_nonnegative("horizon", horizon)
    _require_nonnegative("distance", distance)
    return distance if distance <= horizon else FAR


def quotient_states(horizon: int) -> tuple[PredictiveState, ...]:
    """Enumerate Q_h in canonical order."""
    _require_nonnegative("horizon", horizon)
    return tuple(range(horizon + 1)) + (FAR,)


def project_label(high: int, low: int, state: PredictiveState) -> PredictiveState:
    """Precision projection Q_high -> Q_low for 0<=low<=high."""
    _require_nonnegative("high", high)
    _require_nonnegative("low", low)
    if low > high:
        raise ValueError("require low <= high")
    if state == FAR:
        return FAR
    if isinstance(state, bool) or not isinstance(state, int) or not 0 <= state <= high:
        raise ValueError("state is outside Q_high")
    return state if state <= low else FAR


def full_counter_kernel(distance: int) -> dict[int, Fraction]:
    """One-step equal-branch kernel on the absorbing nonnegative counter."""
    _require_nonnegative("distance", distance)
    if distance == 0:
        return {0: Fraction(1)}
    return {distance - 1: Fraction(1, 2), distance + 1: Fraction(1, 2)}


def graded_kernel(horizon: int, state: PredictiveState) -> dict[PredictiveState, Fraction]:
    """Exact weighted transition Q_h -> Q_{h-1}, for h>=1."""
    _require_positive("horizon", horizon)
    if state == 0:
        return {0: Fraction(1)}
    if state == FAR:
        return {FAR: Fraction(1)}
    if isinstance(state, bool) or not isinstance(state, int) or not 1 <= state <= horizon:
        raise ValueError("state is outside Q_h")
    result: dict[PredictiveState, Fraction] = {}
    for target in (state - 1, state + 1):
        label = quotient_label(horizon - 1, target)
        result[label] = result.get(label, Fraction(0)) + Fraction(1, 2)
    return result


def pushforward_kernel(distribution: dict[int | str, Fraction], mapping) -> dict[int | str, Fraction]:
    """Push a finite rational distribution through one deterministic map."""
    result: dict[int | str, Fraction] = {}
    for state, mass in distribution.items():
        target = mapping(state)
        result[target] = result.get(target, Fraction(0)) + mass
    return result


def counter_factorization_holds(horizon: int, distance: int) -> bool:
    """Check q_{h-1} K = K_h q_h for one exact counter state."""
    _require_positive("horizon", horizon)
    _require_nonnegative("distance", distance)
    lhs = pushforward_kernel(
        full_counter_kernel(distance),
        lambda target: quotient_label(horizon - 1, target),
    )
    rhs = graded_kernel(horizon, quotient_label(horizon, distance))
    return lhs == rhs


def graded_naturality_holds(high: int, low: int, state: PredictiveState) -> bool:
    """Check projection/dynamics commutation from horizon high to low."""
    _require_positive("high", high)
    _require_positive("low", low)
    if low > high:
        raise ValueError("require low <= high")
    lhs = pushforward_kernel(
        graded_kernel(high, state),
        lambda target: project_label(high - 1, low - 1, target),
    )
    rhs = graded_kernel(low, project_label(high, low, state))
    return lhs == rhs


def first_return_polynomial(activity: Fraction, depth: int) -> Fraction:
    """Finite first-return series F_N(s)=sum_{n<=N} f_n s^(2n)."""
    if not isinstance(activity, Fraction):
        activity = Fraction(activity)
    if activity < 0 or activity >= 1:
        raise ValueError("activity must lie in [0,1)")
    _require_nonnegative("depth", depth)
    return sum(
        (first_return_mass(n) * activity ** (2 * n) for n in range(1, depth + 1)),
        Fraction(0),
    )


def renewal_coefficient_identity(n: int) -> bool:
    """Coefficient form of the formal renewal law F(2-F)=s^2."""
    _require_positive("n", n)
    if n == 1:
        return 2 * first_return_mass(1) == 1
    convolution = sum(
        (first_return_mass(i) * first_return_mass(n - i) for i in range(1, n)),
        Fraction(0),
    )
    return 2 * first_return_mass(n) == convolution
