"""Exact versus task-specific observables on unlabeled branching-star response shapes.

After leaf identity is quotiented out, one minimum response of the symmetric star
is an integer partition of the residue ``R`` (plus a uniform baseline that is
irrelevant to shape).  The full sorted partition, equivalently its value-count
histogram, is an exact identity-free response state.

Coarser statistics can be useful for a declared downstream task, but they are
not generally exact shape states.  In particular, no fixed finite number of
power sums, even when augmented by active-part count and maximum excess, can
recover all star response shapes as branching size grows.

For any requested moment order ``d>=1``, put ``n=d+1``.  The standard finite-
difference identity

    sum_i (-1)^i C(n,i) i^m = 0,    m < n,

implies that the even-index and odd-index binomial multisets have equal power
sums through degree ``d`` and equal cardinality.  Shift every entry by one so
all parts are positive, then append the same new largest part ``d+3`` to both
multisets.  The resulting distinct positive partitions have:

* equal active-part count;
* equal maximum part;
* equal total response;
* equal power sums of orders ``1,...,d``.

Their common total ``R`` can be used as the star leaf count ``k=R`` and closing
score ``q=R``.  Then ``q mod (k+1)=R`` and every positive partition of ``R`` is a
valid unlabeled minimum-response shape in the zero-baseline residue shell.
Thus the alias pairs occur inside the actual E001 star response family, not in
an unrelated partition space.

This is a P024-style application statement about task observables.  Finite
differences, binomial identities, integer partitions and moment methods are
standard mathematics; no novelty claim is made for those tools.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import comb


def _require_partition(shape: tuple[int, ...] | list[int]) -> tuple[int, ...]:
    values = tuple(shape)
    if not values:
        raise ValueError("response shape must be nonempty")
    if any(
        isinstance(value, bool) or not isinstance(value, int) or value <= 0
        for value in values
    ):
        raise ValueError("response-shape parts must be positive integers")
    if tuple(sorted(values, reverse=True)) != values:
        raise ValueError("response shape must be sorted in non-increasing order")
    return values


def response_shape_histogram(
    shape: tuple[int, ...] | list[int],
) -> tuple[tuple[int, int], ...]:
    """Return the exact identity-free value-count representation of one partition."""
    values = _require_partition(shape)
    histogram: list[tuple[int, int]] = []
    current = values[0]
    count = 0
    for value in values:
        if value == current:
            count += 1
            continue
        histogram.append((current, count))
        current = value
        count = 1
    histogram.append((current, count))
    return tuple(histogram)


def response_shape_from_histogram(
    histogram: tuple[tuple[int, int], ...] | list[tuple[int, int]],
) -> tuple[int, ...]:
    """Invert ``response_shape_histogram`` exactly."""
    entries = tuple(histogram)
    if not entries:
        raise ValueError("histogram must be nonempty")
    result: list[int] = []
    previous: int | None = None
    for value, count in entries:
        if (
            isinstance(value, bool)
            or not isinstance(value, int)
            or value <= 0
            or isinstance(count, bool)
            or not isinstance(count, int)
            or count <= 0
        ):
            raise ValueError("histogram entries require positive integer value/count")
        if previous is not None and value >= previous:
            raise ValueError("histogram values must be strictly decreasing")
        result.extend((value,) * count)
        previous = value
    return tuple(result)


def response_shape_power_signature(
    shape: tuple[int, ...] | list[int],
    maximum_power: int,
) -> tuple[int, int, tuple[int, ...]]:
    """Return ``(active_count, maximum_part, power_sums_1..d)``.

    This is only a declared task observable.  It is intentionally not advertised
    as an exact response-shape state.
    """
    values = _require_partition(shape)
    if (
        isinstance(maximum_power, bool)
        or not isinstance(maximum_power, int)
        or maximum_power < 0
    ):
        raise ValueError("maximum_power must be a non-negative integer")
    sums = tuple(
        sum(value**power for value in values)
        for power in range(1, maximum_power + 1)
    )
    return len(values), values[0], sums


@dataclass(frozen=True)
class StarShapeMomentAlias:
    maximum_power: int
    left_shape: tuple[int, ...]
    right_shape: tuple[int, ...]
    active_count: int
    maximum_part: int
    common_total: int
    common_power_sums: tuple[int, ...]
    star_leaf_count: int
    star_closing_score: int


def finite_difference_shape_alias(maximum_power: int) -> StarShapeMomentAlias:
    """Construct two distinct star-response partitions aliased through order ``d``."""
    if (
        isinstance(maximum_power, bool)
        or not isinstance(maximum_power, int)
        or maximum_power < 1
    ):
        raise ValueError("maximum_power must be a positive integer")

    order = maximum_power + 1
    shift = 1
    left: list[int] = []
    right: list[int] = []
    for index in range(order + 1):
        target = left if index % 2 == 0 else right
        target.extend((shift + index,) * comb(order, index))

    # The shared cap makes maximum part identical without disturbing equality of
    # any moment: the same addend is inserted on both sides.
    shared_cap = shift + order + 1
    left.append(shared_cap)
    right.append(shared_cap)
    left_shape = tuple(sorted(left, reverse=True))
    right_shape = tuple(sorted(right, reverse=True))
    if left_shape == right_shape:
        raise AssertionError("finite-difference alias construction collapsed")

    left_signature = response_shape_power_signature(left_shape, maximum_power)
    right_signature = response_shape_power_signature(right_shape, maximum_power)
    if left_signature != right_signature:
        raise AssertionError("finite-difference alias lost its declared task signature")

    common_total = sum(left_shape)
    if common_total != sum(right_shape):
        raise AssertionError("moment alias lost equal total response")
    # Choosing k=q=R places the two positive partitions in the zero-baseline
    # residue-R star shell because R mod (R+1)=R and every partition has <=R parts.
    if len(left_shape) > common_total or len(right_shape) > common_total:
        raise AssertionError("response partition cannot fit its constructed star shell")

    return StarShapeMomentAlias(
        maximum_power=maximum_power,
        left_shape=left_shape,
        right_shape=right_shape,
        active_count=left_signature[0],
        maximum_part=left_signature[1],
        common_total=common_total,
        common_power_sums=left_signature[2],
        star_leaf_count=common_total,
        star_closing_score=common_total,
    )


def response_shape_fits_zero_baseline_star_shell(
    shape: tuple[int, ...] | list[int],
    leaf_count: int,
    closing_score: int,
) -> bool:
    """Check the zero-baseline residue shell used by the alias construction."""
    values = _require_partition(shape)
    if (
        isinstance(leaf_count, bool)
        or not isinstance(leaf_count, int)
        or leaf_count < 2
        or isinstance(closing_score, bool)
        or not isinstance(closing_score, int)
        or closing_score <= 0
    ):
        raise ValueError("leaf_count>=2 and positive closing_score are required")
    baseline, residue = divmod(closing_score, leaf_count + 1)
    return baseline == 0 and sum(values) == residue and len(values) <= leaf_count
