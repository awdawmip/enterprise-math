"""Exact finite-horizon defect split for two-sided guarded peak precision.

For a normalized two-sided action alphabet with fastest positive action ``P``,
a prefix horizon ``n`` identifies a candidate nonnegative translation with a
deficit

    delta = n*P - q,        0 <= delta <= n*P.

The deficit generators are the canonical set

    D = {P} union {P-a : a in Abar, P-a>0}.

Let ``lambda_D(delta)`` be the minimum number of positive generators from ``D``
needed to realize ``delta`` (infinity for a numerical-semigroup gap).  Then a
deficit is realized by an action word of length at most ``n`` exactly when

    delta in <D> and lambda_D(delta) <= n.

Thus every missing candidate class has one of two disjoint causes:

* arithmetic gap: ``delta`` is not in the deficit semigroup at all;
* packing defect: ``delta`` belongs to the semigroup but every realization
  needs more than the current ``n`` action slots.

Writing ``g_n`` and ``p_n`` for those counts inside ``[0,nP]`` gives the exact
all-horizon identity

    |M_n intersect N_0| = n*P + 1 - g_n - p_n.

The corresponding guarded word-horizon class count is one larger.

Arithmetic gaps are permanent: ``g_n`` increases to the deficit-semigroup genus
once ``nP`` reaches the Frobenius number ``conductor-1``.  Packing defects are
purely finite-horizon underresolution: the eventual-affine theorem proves they
vanish after a finite certified horizon, but they need not decrease
monotonically before then.

This distinction is structural for Enterprise Math.  A semigroup element with
``lambda_D(delta)>n`` is not impossible; it is representable only by a longer
declared future word.  It should therefore be classified as horizon
underresolution rather than arithmetic impossibility.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

from .two_sided_guarded_peak_growth import (
    two_sided_guard_peak_growth_report,
)


def _require_int(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f"{name} must be an integer")


def _minimum_deficit_lengths(
    generators: tuple[int, ...],
    maximum: int,
) -> tuple[int | None, ...]:
    """Minimum generator count for every deficit through ``maximum``."""
    _require_int("maximum", maximum)
    if maximum < 0:
        raise ValueError("maximum must be non-negative")
    if not generators or any(
        isinstance(value, bool) or not isinstance(value, int) or value <= 0
        for value in generators
    ):
        raise ValueError("generators must be positive integers")

    infinity = maximum + 1
    lengths = [infinity] * (maximum + 1)
    lengths[0] = 0
    for value in range(maximum + 1):
        if lengths[value] == infinity:
            continue
        for generator in generators:
            target = value + generator
            if target <= maximum:
                lengths[target] = min(
                    lengths[target],
                    lengths[value] + 1,
                )
    return tuple(
        None if length == infinity else length
        for length in lengths
    )


@dataclass(frozen=True)
class TwoSidedGuardPeakDefectReport:
    prefix_horizon: int
    action_grain: int
    normalized_actions: tuple[int, ...]
    normalized_fastest_positive: int
    deficit_generators: tuple[int, ...]
    deficit_conductor: int
    deficit_genus: int
    arithmetic_gap_count: int
    packing_defect_count: int
    nonnegative_reachable_count: int
    exact_prefix_affine_onset: int
    gap_saturation_prefix_horizon: int

    @property
    def word_horizon(self) -> int:
        return self.prefix_horizon + 1

    @property
    def total_missing_count(self) -> int:
        return self.arithmetic_gap_count + self.packing_defect_count

    @property
    def guard_only_class_count(self) -> int:
        return self.nonnegative_reachable_count + 1

    @property
    def arithmetic_gaps_are_saturated(self) -> bool:
        return self.arithmetic_gap_count == self.deficit_genus

    @property
    def packing_is_resolved(self) -> bool:
        return self.packing_defect_count == 0

    @property
    def affine_formula_holds_now(self) -> bool:
        expected = (
            self.prefix_horizon * self.normalized_fastest_positive
            + 1
            - self.deficit_genus
        )
        return self.nonnegative_reachable_count == expected


def two_sided_guard_peak_defect_report(
    actions: Iterable[int],
    prefix_horizon: int,
) -> TwoSidedGuardPeakDefectReport:
    """Return the exact arithmetic-gap / packing-defect split at one horizon."""
    _require_int("prefix_horizon", prefix_horizon)
    if prefix_horizon < 0:
        raise ValueError("prefix_horizon must be non-negative")

    growth = two_sided_guard_peak_growth_report(actions)
    fastest = growth.normalized_fastest_positive
    maximum = prefix_horizon * fastest
    lengths = _minimum_deficit_lengths(
        growth.deficit_generators,
        maximum,
    )

    arithmetic_gap_count = sum(length is None for length in lengths)
    packing_defect_count = sum(
        length is not None and length > prefix_horizon
        for length in lengths
    )
    reachable_count = (
        maximum
        + 1
        - arithmetic_gap_count
        - packing_defect_count
    )

    gap_saturation = (
        0
        if growth.deficit_conductor <= 1
        else (
            growth.deficit_conductor
            - 1
            + fastest
            - 1
        )
        // fastest
    )

    return TwoSidedGuardPeakDefectReport(
        prefix_horizon=prefix_horizon,
        action_grain=growth.action_grain,
        normalized_actions=growth.normalized_actions,
        normalized_fastest_positive=fastest,
        deficit_generators=growth.deficit_generators,
        deficit_conductor=growth.deficit_conductor,
        deficit_genus=growth.deficit_genus,
        arithmetic_gap_count=arithmetic_gap_count,
        packing_defect_count=packing_defect_count,
        nonnegative_reachable_count=reachable_count,
        exact_prefix_affine_onset=growth.exact_prefix_affine_onset,
        gap_saturation_prefix_horizon=gap_saturation,
    )


def two_sided_guard_peak_defect_sequence(
    actions: Iterable[int],
    maximum_prefix_horizon: int,
) -> tuple[TwoSidedGuardPeakDefectReport, ...]:
    """Exact defect reports for every prefix horizon from zero through ``maximum``."""
    _require_int("maximum_prefix_horizon", maximum_prefix_horizon)
    if maximum_prefix_horizon < 0:
        raise ValueError("maximum_prefix_horizon must be non-negative")
    return tuple(
        two_sided_guard_peak_defect_report(actions, horizon)
        for horizon in range(maximum_prefix_horizon + 1)
    )


def unique_positive_speed_has_no_packing_defect(
    actions: Iterable[int],
    prefix_horizon: int,
) -> bool:
    """Sufficient no-packing theorem for alphabets with one positive action value.

    After gcd normalization let ``P`` be the only strictly positive action.
    Every positive deficit generator is then at least ``P``.  A semigroup
    deficit ``delta<=nP`` therefore uses at most ``n`` generators in *every*
    representation, so packing underresolution is impossible at every horizon.
    """
    report = two_sided_guard_peak_defect_report(
        actions,
        prefix_horizon,
    )
    positive_actions = tuple(
        value
        for value in report.normalized_actions
        if value > 0
    )
    if len(positive_actions) != 1:
        raise ValueError(
            "the no-packing theorem requires exactly one positive action value"
        )
    if report.packing_defect_count != 0:
        raise AssertionError(
            "unique-positive action alphabet unexpectedly produced packing defects"
        )
    return True
