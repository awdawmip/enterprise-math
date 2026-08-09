"""Exact kinematic aliasing of distinct finite material response samples.

The E001 scalar material-to-motion coupling maps a response sample ``r`` on
amplitude ``A`` and incoming budget ``B`` to

    K_B(r) = floor(B*r/A).

Therefore distinct material responses need not remain distinguishable after the
kinematic quotient.  For ``r_lo <= r_hi`` write

    B*r_lo = A*q + rho,
    Delta = r_hi-r_lo.

Then exactly

    K_B(r_hi)-K_B(r_lo) = floor((rho + B*Delta)/A).

Hence two distinct responses alias to one returned budget iff

    rho + B*Delta < A.

The aliasing pattern below the eventual separation threshold can be nonmonotone
in ``B`` because ``rho`` cycles through quotient remainders.  If ``Delta>0``,
``B>=ceil(A/Delta)`` guarantees permanent pair separation.  For a finite set of
response samples, ``B>=ceil(A/min_gap)`` guarantees the kinematic map is
injective on the whole set.

These are exact finite quotient statements.  ``K_B`` is a bookkeeping map, not
a claim that the samples or budgets are physical energy or momentum units.
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass


def _require_nonnegative(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a non-negative integer")


def _require_amplitude(amplitude: int) -> None:
    if isinstance(amplitude, bool) or not isinstance(amplitude, int) or amplitude <= 0:
        raise ValueError("amplitude must be a positive integer")


@dataclass(frozen=True)
class MaterialResponseAliasReport:
    lower_response: int
    upper_response: int
    incoming_budget: int
    amplitude: int
    response_gap: int
    lower_returned_budget: int
    upper_returned_budget: int
    lower_product_remainder: int
    returned_budget_gap: int
    expected_gap_from_remainder: int
    aliased: bool
    permanent_separation_threshold: int | None


def material_response_alias_report(
    lower_response: int,
    upper_response: int,
    incoming_budget: int,
    amplitude: int,
) -> MaterialResponseAliasReport:
    """Return the exact quotient remainder controlling one response pair."""
    _require_amplitude(amplitude)
    _require_nonnegative("lower_response", lower_response)
    _require_nonnegative("upper_response", upper_response)
    _require_nonnegative("incoming_budget", incoming_budget)
    if lower_response > upper_response:
        raise ValueError("lower_response must not exceed upper_response")
    if upper_response > amplitude:
        raise ValueError("material responses must not exceed amplitude")

    gap = upper_response - lower_response
    lower_product = incoming_budget * lower_response
    lower_return, remainder = divmod(lower_product, amplitude)
    upper_return = incoming_budget * upper_response // amplitude
    returned_gap = upper_return - lower_return
    expected = (remainder + incoming_budget * gap) // amplitude
    if returned_gap != expected:
        raise AssertionError("material response alias gap disagrees with remainder formula")
    threshold = None if gap == 0 else (amplitude + gap - 1) // gap
    return MaterialResponseAliasReport(
        lower_response=lower_response,
        upper_response=upper_response,
        incoming_budget=incoming_budget,
        amplitude=amplitude,
        response_gap=gap,
        lower_returned_budget=lower_return,
        upper_returned_budget=upper_return,
        lower_product_remainder=remainder,
        returned_budget_gap=returned_gap,
        expected_gap_from_remainder=expected,
        aliased=returned_gap == 0,
        permanent_separation_threshold=threshold,
    )


@dataclass(frozen=True, order=True)
class KinematicResponseClass:
    returned_budget: int
    material_responses: tuple[int, ...]


@dataclass(frozen=True)
class KinematicResponsePartition:
    material_responses: tuple[int, ...]
    incoming_budget: int
    amplitude: int
    classes: tuple[KinematicResponseClass, ...]
    class_count: int
    material_class_count: int
    merged_material_classes: int
    injective: bool
    guaranteed_injective_budget: int | None


def guaranteed_injective_budget(
    responses: tuple[int, ...] | list[int],
    amplitude: int,
) -> int | None:
    """Sufficient budget from the minimum positive response gap; None for <=1 class."""
    _require_amplitude(amplitude)
    values = tuple(sorted(set(responses)))
    for value in values:
        _require_nonnegative("response", value)
        if value > amplitude:
            raise ValueError("material response must not exceed amplitude")
    if len(values) <= 1:
        return None
    minimum_gap = min(right - left for left, right in zip(values, values[1:]))
    return (amplitude + minimum_gap - 1) // minimum_gap


def kinematic_response_partition(
    responses: tuple[int, ...] | list[int],
    incoming_budget: int,
    amplitude: int,
) -> KinematicResponsePartition:
    """Collapse a finite response alphabet through the scalar motion quotient."""
    _require_amplitude(amplitude)
    _require_nonnegative("incoming_budget", incoming_budget)
    values = tuple(sorted(set(responses)))
    if not values:
        raise ValueError("at least one material response is required")
    for value in values:
        _require_nonnegative("response", value)
        if value > amplitude:
            raise ValueError("material response must not exceed amplitude")

    by_budget: dict[int, list[int]] = defaultdict(list)
    for response in values:
        by_budget[incoming_budget * response // amplitude].append(response)
    classes = tuple(
        KinematicResponseClass(returned_budget=budget, material_responses=tuple(group))
        for budget, group in sorted(by_budget.items())
    )
    class_count = len(classes)
    threshold = guaranteed_injective_budget(values, amplitude)
    if threshold is not None and incoming_budget >= threshold and class_count != len(values):
        raise AssertionError("minimum-gap injectivity threshold failed")
    return KinematicResponsePartition(
        material_responses=values,
        incoming_budget=incoming_budget,
        amplitude=amplitude,
        classes=classes,
        class_count=class_count,
        material_class_count=len(values),
        merged_material_classes=len(values) - class_count,
        injective=class_count == len(values),
        guaranteed_injective_budget=threshold,
    )
