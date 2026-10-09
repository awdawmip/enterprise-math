"""Exact positive Weighted-BRC tool layer.

This module promotes the main-backed finite-DAG CWM calculus and the exact
one-state recurrent closure into a reusable library surface.  It deliberately
keeps path accumulation rational/exact.  Logarithms are exposed only as the
existing symbolic BRC ``LN`` readout.

The canonical Boolean R023 BRC base is not mutated by this module.  Signed or
amplitude cancellation is outside this positive-weight carrier.
"""

from __future__ import annotations

from collections.abc import Hashable, Iterable, Mapping
from dataclasses import dataclass
from fractions import Fraction

from .brc_logarithm import LnExpr, ln
from .exact_arithmetic import DivisionExpr, division

RationalInput = int | Fraction
Target = Hashable


def _fraction(value: RationalInput) -> Fraction:
    if isinstance(value, bool) or not isinstance(value, (int, Fraction)):
        raise TypeError("weight must be an int or Fraction")
    return Fraction(value)


def _positive_fraction(name: str, value: RationalInput) -> Fraction:
    result = _fraction(value)
    if result <= 0:
        raise ValueError(f"{name} must be positive")
    return result


@dataclass(frozen=True)
class CWMState:
    """Count / total-mass / dominant-mass state for positive weighted paths.

    ``count`` records supported path multiplicity. ``total`` is the sum of path
    weights and ``dominant`` is the largest individual path weight.

    The constructor accepts the closed algebraic CWM envelope.  Use
    :func:`is_positive_path_realizable` when exact finite positive-path
    realizability is required.
    """

    count: int
    total: Fraction
    dominant: Fraction

    def __post_init__(self) -> None:
        if isinstance(self.count, bool) or not isinstance(self.count, int) or self.count < 0:
            raise ValueError("count must be a non-negative integer")
        if not isinstance(self.total, Fraction) or not isinstance(self.dominant, Fraction):
            raise TypeError("total and dominant must be Fraction values")
        if self.count == 0:
            if self.total != 0 or self.dominant != 0:
                raise ValueError("zero count requires zero total and dominant mass")
            return
        if self.total <= 0 or self.dominant <= 0:
            raise ValueError("live CWM state requires positive total and dominant mass")
        if self.dominant > self.total:
            raise ValueError("dominant path mass cannot exceed total path mass")
        if self.total > self.count * self.dominant:
            raise ValueError("total path mass cannot exceed count times dominant mass")

    @property
    def live(self) -> bool:
        return self.count > 0


CWM_ZERO = CWMState(0, Fraction(0, 1), Fraction(0, 1))
CWM_ONE = CWMState(1, Fraction(1, 1), Fraction(1, 1))


def cwm_edge(weight: RationalInput) -> CWMState:
    """Lift one positive edge/path weight to ``(1,a,a)``."""
    value = _positive_fraction("weight", weight)
    return CWMState(1, value, value)


def cwm_recoalesce(left: CWMState, right: CWMState) -> CWMState:
    """Alternative-branch recoalescence: ``(+,+,max)``."""
    if not left.live:
        return right
    if not right.live:
        return left
    return CWMState(
        left.count + right.count,
        left.total + right.total,
        max(left.dominant, right.dominant),
    )


def cwm_propagate(left: CWMState, right: CWMState) -> CWMState:
    """Serial path propagation: componentwise multiplication."""
    if not left.live or not right.live:
        return CWM_ZERO
    return CWMState(
        left.count * right.count,
        left.total * right.total,
        left.dominant * right.dominant,
    )


def cwm_from_positive_weights(weights: Iterable[RationalInput]) -> CWMState:
    """Return the exact CWM state of one finite positive-weight branch family."""
    values = tuple(_positive_fraction("branch weight", weight) for weight in weights)
    if not values:
        return CWM_ZERO
    return CWMState(len(values), sum(values, Fraction(0, 1)), max(values))


def is_positive_path_realizable(state: CWMState) -> bool:
    """Exact realizability test for a finite family of positive rational weights."""
    if not state.live:
        return state == CWM_ZERO
    if state.count == 1:
        return state.total == state.dominant
    return state.dominant < state.total <= state.count * state.dominant


def boolean_support(state: CWMState) -> bool:
    """Forget positive CWM data to Boolean support."""
    return state.live


def effective_multiplicity(state: CWMState) -> Fraction:
    """Return ``E=W/M`` for a live CWM state."""
    if not state.live:
        raise ValueError("effective multiplicity is undefined on zero support")
    return state.total / state.dominant


def multiplicity_surplus_expr(state: CWMState) -> LnExpr:
    """Return symbolic BRC ``LN(W/M)`` without numerical logarithm evaluation."""
    ratio = effective_multiplicity(state)
    return ln(division(ratio.numerator, ratio.denominator))


def dominant_log_expr(state: CWMState) -> LnExpr:
    """Return symbolic BRC ``LN(M)`` for a live state."""
    if not state.live:
        raise ValueError("dominant log is undefined on zero support")
    return ln(division(state.dominant.numerator, state.dominant.denominator))


def total_log_expr(state: CWMState) -> LnExpr:
    """Return symbolic BRC ``LN(W)`` for a live state."""
    if not state.live:
        raise ValueError("total log is undefined on zero support")
    return ln(division(state.total.numerator, state.total.denominator))


def future_cwm_equivalent(
    left: Mapping[Target, CWMState], right: Mapping[Target, CWMState]
) -> bool:
    """All-prefix safe equality of complete declared-target CWM transfers."""
    return set(left) == set(right) and all(left[target] == right[target] for target in left)


def projective_scale(
    left: Mapping[Target, CWMState], right: Mapping[Target, CWMState]
) -> Fraction | None:
    """Return common positive ``lambda`` when ``right = G_lambda(left)``.

    Counts must agree targetwise.  For each live target both total and dominant
    masses must scale by the same common factor.  All-zero signatures use the
    canonical scale ``1``.
    """
    if set(left) != set(right):
        return None
    scale: Fraction | None = None
    for target in left:
        a = left[target]
        b = right[target]
        if a.count != b.count:
            return None
        if not a.live or not b.live:
            if a.live != b.live or a != CWM_ZERO or b != CWM_ZERO:
                return None
            continue
        candidate = b.total / a.total
        if candidate <= 0:
            return None
        if b.dominant != candidate * a.dominant:
            return None
        if scale is None:
            scale = candidate
        elif scale != candidate:
            return None
    return Fraction(1, 1) if scale is None else scale


def gauge_scale(state: CWMState, factor: RationalInput) -> CWMState:
    """Apply ``G_lambda(c,w,m)=(c,lambda*w,lambda*m)``."""
    value = _positive_fraction("factor", factor)
    if not state.live:
        return CWM_ZERO
    return CWMState(state.count, value * state.total, value * state.dominant)


def compensate_incoming_weight(weight: RationalInput, factor: RationalInput) -> Fraction:
    """Move a future projective factor onto an incoming transition weight."""
    return _positive_fraction("weight", weight) * _positive_fraction("factor", factor)


@dataclass(frozen=True)
class OneStateRecurrentCWM:
    """Exact closure summary for one state with finitely many positive loops."""

    loop_count: int
    total_one_step: Fraction
    dominant_one_step: Fraction
    total_mass_stable: bool
    dominant_bounded: bool
    total_mass_closure: Fraction | None

    def depth(self, traversals: int) -> CWMState:
        if isinstance(traversals, bool) or not isinstance(traversals, int) or traversals < 0:
            raise ValueError("traversals must be a non-negative integer")
        if traversals == 0:
            return CWM_ONE
        return CWMState(
            self.loop_count**traversals,
            self.total_one_step**traversals,
            self.dominant_one_step**traversals,
        )

    def total_mass_closure_expr(self) -> DivisionExpr:
        if self.total_mass_closure is None:
            raise ValueError("total recurrent mass diverges when one-step total mass is >= 1")
        return division(
            self.total_mass_closure.numerator,
            self.total_mass_closure.denominator,
        )

    def log_stability_expr(self) -> LnExpr:
        return ln(division(self.total_one_step.numerator, self.total_one_step.denominator))

    def log_multiplicity_correction_expr(self) -> LnExpr:
        ratio = self.total_one_step / self.dominant_one_step
        return ln(division(ratio.numerator, ratio.denominator))


def one_state_recurrent_cwm(loop_weights: Iterable[RationalInput]) -> OneStateRecurrentCWM:
    """Classify exact one-state recurrent positive-branch stability."""
    values = tuple(_positive_fraction("loop weight", value) for value in loop_weights)
    if not values:
        raise ValueError("at least one positive loop weight is required")
    total = sum(values, Fraction(0, 1))
    dominant = max(values)
    stable = total < 1
    closure = Fraction(1, 1) / (1 - total) if stable else None
    return OneStateRecurrentCWM(
        loop_count=len(values),
        total_one_step=total,
        dominant_one_step=dominant,
        total_mass_stable=stable,
        dominant_bounded=dominant <= 1,
        total_mass_closure=closure,
    )
