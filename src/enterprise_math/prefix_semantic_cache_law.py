"""Exact distinct-operation cache sizes through a finite word horizon.

For the prefix observation ladder, cache every distinct semantic operation
realizable by a literal word of length at most H, including identity.

Literal syntax:

    C_lit(k,H)=1+sum_{h=1}^H k^h.

Terminal semantics:

    C_terminal(k,H)=1+sum_{s=1}^{min(k,H)} C(k,s).

Discovery-order semantics:

    C_discovery(k,H)=1+sum_{s=1}^{min(k,H)} P(k,s).

Full timing semantics uses the exact-length count

    P(k,s) C(h-1,s-1).

Summing h=s..H and applying the hockey-stick identity gives

    C_timing(k,H)
      = 1 + sum_{s=1}^{min(k,H)} P(k,s) C(H,s).

For fixed k and H>=k, C_timing is a degree-k polynomial in H.  The top term

    k! C(H,k)

has leading coefficient1, so C_timing(k,H) ~ H^k.

Thus semantic quotienting changes a literal exponential horizon cache into a
polynomial timing-semantic cache, while coarser discovery/terminal caches
saturate at finite monoid sizes.

Hockey-stick identities and falling factorial counts are standard combinatorics.
The Enterprise Math value is the exact Stage131 cache law after semantic word
quotienting.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import comb, factorial


def _positive(name: str, value: int) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value < 1:
        raise ValueError(f"{name} must be a positive integer")
    return value


def _nonnegative(name: str, value: int) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a nonnegative integer")
    return value


def falling_factorial(total: int, selected: int) -> int:
    if not 0 <= selected <= total:
        raise ValueError("selected must lie in 0..total")
    return factorial(total) // factorial(total - selected)


def literal_cache_entries_through_horizon(generator_count: int, horizon: int) -> int:
    k = _positive("generator_count", generator_count)
    h = _nonnegative("horizon", horizon)
    if h == 0:
        return 1
    if k == 1:
        return h + 1
    return 1 + k * (k**h - 1) // (k - 1)


def terminal_cache_entries_through_horizon(generator_count: int, horizon: int) -> int:
    k = _positive("generator_count", generator_count)
    h = _nonnegative("horizon", horizon)
    return 1 + sum(comb(k, s) for s in range(1, min(k, h) + 1))


def discovery_cache_entries_through_horizon(generator_count: int, horizon: int) -> int:
    k = _positive("generator_count", generator_count)
    h = _nonnegative("horizon", horizon)
    return 1 + sum(
        falling_factorial(k, s)
        for s in range(1, min(k, h) + 1)
    )


def timing_cache_entries_through_horizon(generator_count: int, horizon: int) -> int:
    k = _positive("generator_count", generator_count)
    h = _nonnegative("horizon", horizon)
    return 1 + sum(
        falling_factorial(k, s) * comb(h, s)
        for s in range(1, min(k, h) + 1)
    )


def timing_cache_entries_by_exact_length_sum(generator_count: int, horizon: int) -> int:
    """Independent direct sum of exact-length timing counts."""
    k = _positive("generator_count", generator_count)
    h = _nonnegative("horizon", horizon)
    total = 1
    for length in range(1, h + 1):
        total += sum(
            falling_factorial(k, s) * comb(length - 1, s - 1)
            for s in range(1, min(k, length) + 1)
        )
    return total


def timing_cache_hockey_stick_identity(generator_count: int, horizon: int) -> bool:
    closed = timing_cache_entries_through_horizon(generator_count, horizon)
    direct = timing_cache_entries_by_exact_length_sum(generator_count, horizon)
    if closed != direct:
        raise AssertionError("timing semantic cache closed form disagreed with exact-length sum")
    return True


def saturated_terminal_cache_size(generator_count: int) -> int:
    k = _positive("generator_count", generator_count)
    return 1 << k


def saturated_discovery_cache_size(generator_count: int) -> int:
    k = _positive("generator_count", generator_count)
    return 1 + sum(falling_factorial(k, s) for s in range(1, k + 1))


def finite_forward_difference(values: tuple[int, ...], order: int) -> tuple[int, ...]:
    if isinstance(order, bool) or not isinstance(order, int) or order < 0:
        raise ValueError("order must be nonnegative")
    result = tuple(values)
    for _ in range(order):
        if len(result) < 2:
            return ()
        result = tuple(right - left for left, right in zip(result, result[1:], strict=True))
    return result


def timing_cache_top_difference(
    generator_count: int,
    start_horizon: int,
    sample_count: int,
) -> tuple[int, ...]:
    k = _positive("generator_count", generator_count)
    start = _nonnegative("start_horizon", start_horizon)
    count = _positive("sample_count", sample_count)
    if start < k:
        raise ValueError("start_horizon must be at least generator_count")
    values = tuple(
        timing_cache_entries_through_horizon(k, start + offset)
        for offset in range(count)
    )
    return finite_forward_difference(values, k)


@dataclass(frozen=True)
class PrefixSemanticCacheReport:
    generator_count: int
    horizon: int
    literal_entries: int
    timing_entries: int
    discovery_entries: int
    terminal_entries: int

    @property
    def literal_to_timing_ratio(self) -> float:
        return self.literal_entries / self.timing_entries

    @property
    def timing_to_discovery_ratio(self) -> float:
        return self.timing_entries / self.discovery_entries


def prefix_semantic_cache_report(generator_count: int, horizon: int) -> PrefixSemanticCacheReport:
    k = _positive("generator_count", generator_count)
    h = _nonnegative("horizon", horizon)
    return PrefixSemanticCacheReport(
        generator_count=k,
        horizon=h,
        literal_entries=literal_cache_entries_through_horizon(k, h),
        timing_entries=timing_cache_entries_through_horizon(k, h),
        discovery_entries=discovery_cache_entries_through_horizon(k, h),
        terminal_entries=terminal_cache_entries_through_horizon(k, h),
    )
