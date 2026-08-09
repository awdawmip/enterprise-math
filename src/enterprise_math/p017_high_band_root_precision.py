"""High-band P017 root precision through dual factor windows.

This module separates two different burdens attached to a retained root index:

* ``raw`` burden: prime labels whose exact quotient windows can hit the root
  bucket, before least-prime / p-rough admissibility is imposed;
* ``realized`` burden: prime labels that actually have a p-rough cofactor in the
  bucket, hence correspond to genuine first-factor shell states.

The distinction is deliberate. Raw window multiplicity is an envelope resource
and can overstate the task-minimal repair needed by the realized shell state.
"""

from __future__ import annotations

from collections import defaultdict
from math import isqrt

from .legendre import primes_up_to
from .p017_cofactor_window import is_p_rough
from .quotient_window import (
    IntegerWindow,
    square_basin_root_factor_window,
    square_basin_window,
)


def root_bucket(root: int) -> IntegerWindow:
    if root < 1:
        raise ValueError("root must be positive")
    return IntegerWindow(root * root, root * (root + 2))


def raw_root_prime_labels(
    k: int, root: int, *, high_band_only: bool = True
) -> tuple[int, ...]:
    """Prime labels whose raw exact cofactor window can hit ``root``.

    This is an exact application of the P007 dual factor-window theorem. It is
    intentionally an envelope calculation: the returned label may disappear
    after the p-rough realizability filter.
    """

    if k < 1:
        raise ValueError("k must be positive")
    bucket = square_basin_root_factor_window(k, root)
    if bucket is None:
        return ()
    hi = min(k, bucket.hi)
    if hi < bucket.lo:
        return ()
    return tuple(
        p
        for p in primes_up_to(hi)
        if p >= bucket.lo and (not high_band_only or p * p >= 2 * k)
    )


def realized_root_shell_labels(
    k: int, root: int, *, high_band_only: bool = True
) -> tuple[int, ...]:
    """Actual least-prime shell labels visible in one retained root fiber."""

    bucket = root_bucket(root)
    result: list[int] = []
    for p in raw_root_prime_labels(k, root, high_band_only=high_band_only):
        window = square_basin_window(k, p)
        if window is None:
            continue
        lo = max(window.lo, bucket.lo)
        hi = min(window.hi, bucket.hi)
        if any(is_p_rough(q, p) for q in range(lo, hi + 1)):
            result.append(p)
    return tuple(result)


def raw_root_split_multiplicity(
    k: int, root: int, *, high_band_only: bool = True
) -> int:
    return len(raw_root_prime_labels(k, root, high_band_only=high_band_only))


def realized_root_split_multiplicity(
    k: int, root: int, *, high_band_only: bool = True
) -> int:
    return len(realized_root_shell_labels(k, root, high_band_only=high_band_only))


def high_band_realized_root_profile(k: int) -> dict[int, tuple[int, ...]]:
    """Return every realized high-band root fiber and its least-prime labels."""

    if k < 1:
        raise ValueError("k must be positive")
    groups: dict[int, set[int]] = defaultdict(set)
    for p in primes_up_to(k):
        if p * p < 2 * k:
            continue
        window = square_basin_window(k, p)
        if window is None:
            continue
        for q in range(window.lo, window.hi + 1):
            if is_p_rough(q, p):
                groups[isqrt(q)].add(p)
    return {root: tuple(sorted(labels)) for root, labels in groups.items()}


def maximum_high_band_realized_root_multiplicity(k: int) -> int:
    profile = high_band_realized_root_profile(k)
    return max((len(labels) for labels in profile.values()), default=0)


def diagonal_raw_root_data(t: int) -> dict[str, object]:
    """Square-of-square diagonal ``k=t^2, root=t`` raw burden.

    For ``t>=6`` the dual factor window, after the least-factor bound ``p<=k``,
    is exactly ``[(t-1)^2+3, t^2]``. Its prime-label count differs by at most one
    from the number of primes in ``((t-1)^2,t^2]``.
    """

    if t < 6:
        raise ValueError("diagonal closed form is stated for t>=6")
    k = t * t
    window = square_basin_root_factor_window(k, t)
    if window is None:
        raise AssertionError("diagonal factor window unexpectedly empty")
    clipped = IntegerWindow(window.lo, min(window.hi, k))
    expected_lo = (t - 1) * (t - 1) + 3
    if clipped.lo != expected_lo or clipped.hi != k:
        raise AssertionError("diagonal dual-window closed form failed")

    raw_labels = raw_root_prime_labels(k, t, high_band_only=True)
    legendre_interval_primes = tuple(
        p
        for p in primes_up_to(k)
        if (t - 1) * (t - 1) < p <= k
    )
    difference = len(legendre_interval_primes) - len(raw_labels)
    if difference not in (0, 1):
        raise AssertionError("diagonal raw burden differs from square-gap count by more than one")
    if any(p * p < 2 * k for p in raw_labels):
        raise AssertionError("diagonal raw label escaped the high band")

    return {
        "t": t,
        "k": k,
        "root": t,
        "factor_window": clipped,
        "raw_prime_labels": raw_labels,
        "raw_multiplicity": len(raw_labels),
        "consecutive_square_primes": legendre_interval_primes,
        "consecutive_square_prime_count": len(legendre_interval_primes),
        "count_difference": difference,
    }


def diagonal_realized_root_data(t: int) -> dict[str, object]:
    """Realized p-rough shell burden on the same square-of-square diagonal."""

    raw = diagonal_raw_root_data(t)
    k = int(raw["k"])
    labels = realized_root_shell_labels(k, t, high_band_only=True)
    if not set(labels).issubset(set(raw["raw_prime_labels"])):
        raise AssertionError("realized diagonal labels escaped the raw envelope")
    return {
        **raw,
        "realized_prime_labels": labels,
        "realized_multiplicity": len(labels),
    }
