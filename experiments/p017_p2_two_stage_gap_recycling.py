"""Exact verifier for P017 two-stage prime-gap recycling.

This research-owner experiment proves all integer algebra/endpoints in
docs/P017_P2_TWO_STAGE_GAP_RECYCLING_20260824.md and validates the full
construction in a self-contained small model. It does not reprove the large
external prime-gap or finite Legendre inputs.
"""

from __future__ import annotations

from bisect import bisect_right
from math import isqrt


def gap_recycling_margin(
    k: int,
    *,
    cofactor_bound: int,
    cofactor_gap: int,
    selector_gap: int,
) -> int:
    """Integer numerator of the strict P2-R06 sufficient inequality."""
    if min(k, cofactor_bound, cofactor_gap, selector_gap) <= 0:
        raise ValueError("all parameters must be positive integers")
    return (
        cofactor_bound * (2 * k + 1 - cofactor_gap * selector_gap)
        - cofactor_gap * k * k
    )


def gap_recycling_interval(
    *,
    cofactor_bound: int,
    cofactor_gap: int,
    selector_gap: int,
) -> tuple[int, int]:
    """Return the positive integer interval on which the margin is positive."""
    b = cofactor_bound
    gq = cofactor_gap
    gp = selector_gap
    discriminant = b * b - b * gq * (gq * gp - 1)
    if discriminant <= 0:
        raise ValueError("the strict quadratic inequality has no positive interval")
    root_floor = isqrt(discriminant)

    lo = max(1, (b - root_floor) // gq - 3)
    while gap_recycling_margin(
        lo,
        cofactor_bound=b,
        cofactor_gap=gq,
        selector_gap=gp,
    ) <= 0:
        lo += 1

    hi = (b + root_floor) // gq + 3
    while gap_recycling_margin(
        hi,
        cofactor_bound=b,
        cofactor_gap=gq,
        selector_gap=gp,
    ) <= 0:
        hi -= 1

    assert gap_recycling_margin(
        lo - 1,
        cofactor_bound=b,
        cofactor_gap=gq,
        selector_gap=gp,
    ) <= 0
    assert gap_recycling_margin(
        hi + 1,
        cofactor_bound=b,
        cofactor_gap=gq,
        selector_gap=gp,
    ) <= 0
    return lo, hi


def feasibility_margin(k: int, *, cofactor_bound: int, cofactor_gap: int) -> int:
    """Necessary selector-window margin for the one-global-gap construction."""
    return cofactor_bound * (2 * k + 1) - cofactor_gap * k * k


def largest_feasible_k(*, cofactor_bound: int, cofactor_gap: int) -> int:
    """Largest k with K^2/B < (2K+1)/G."""
    b = cofactor_bound
    g = cofactor_gap
    root_floor = isqrt(b * b + b * g)
    k = (b + root_floor) // g + 3
    while feasibility_margin(k, cofactor_bound=b, cofactor_gap=g) <= 0:
        k -= 1
    while feasibility_margin(k + 1, cofactor_bound=b, cofactor_gap=g) > 0:
        k += 1
    return k


def primes_up_to(limit: int) -> list[int]:
    """Deterministic Eratosthenes sieve."""
    if limit < 2:
        return []
    flags = bytearray(b"\x01") * (limit + 1)
    flags[0:2] = b"\x00\x00"
    for p in range(2, isqrt(limit) + 1):
        if flags[p]:
            start = p * p
            flags[start : limit + 1 : p] = b"\x00" * (
                (limit - start) // p + 1
            )
    return [n for n, flag in enumerate(flags) if flag]


def operational_max_gap(primes: list[int], bound: int) -> tuple[int, int, int]:
    """Maximum next-prime distance needed for all real 0<x<bound."""
    if not primes or primes[0] != 2 or primes[-1] <= bound:
        raise ValueError("prime list must start at 2 and extend beyond bound")
    best = (2, 0, 2)
    for left, right in zip(primes, primes[1:]):
        if left >= bound:
            break
        candidate = (right - left, left, right)
        if candidate > best:
            best = candidate
    return best


def next_prime_after_fraction(
    numerator: int, denominator: int, primes: list[int]
) -> int:
    """Least listed prime strictly greater than numerator/denominator."""
    if numerator < 0 or denominator <= 0:
        raise ValueError("fraction must be nonnegative with positive denominator")
    index = bisect_right(primes, numerator // denominator)
    if index >= len(primes):
        raise ValueError("prime table does not extend far enough")
    return primes[index]


def verify_small_model() -> None:
    """Prove a small GAP(B,G) input and replay every k in its theorem interval."""
    bound = 5_000_000
    gap = 154
    primes = primes_up_to(bound + gap)

    assert operational_max_gap(primes, bound) == (154, 4_652_353, 4_652_507)
    lo, hi = gap_recycling_interval(
        cofactor_bound=bound,
        cofactor_gap=gap,
        selector_gap=gap,
    )
    assert (lo, hi) == (15_611, 49_324)

    for k in range(lo, hi + 1):
        # p > (2K+1-G^2)/G and, since G is even, p < (2K+1)/G.
        selector_numerator = 2 * k + 1 - gap * gap
        p = next_prime_after_fraction(selector_numerator, gap, primes)
        assert p * gap > selector_numerator
        assert p * gap < 2 * k + 1
        assert p * bound > k * k

        # q is the first prime after K^2/p.
        q = next_prime_after_fraction(k * k, p, primes)
        assert k * k < p * q
        assert p * q <= k * k + p * gap
        assert p * q < (k + 1) * (k + 1)


def verify_campbell_endpoints() -> None:
    """Check the exact large constants without asserting their external premise."""
    bound = 68_000_000_000_000_000_000
    gap = 1_724

    lo, hi = gap_recycling_interval(
        cofactor_bound=bound,
        cofactor_gap=gap,
        selector_gap=gap,
    )
    assert lo == 1_486_088
    assert hi == 78_886_310_903_386_302

    assert gap_recycling_margin(
        lo - 1,
        cofactor_bound=bound,
        cofactor_gap=gap,
        selector_gap=gap,
    ) == -68_003_807_375_681_384_956
    assert gap_recycling_margin(
        lo,
        cofactor_bound=bound,
        cofactor_gap=gap,
        selector_gap=gap,
    ) == 67_996_192_619_194_585_344
    assert gap_recycling_margin(
        hi,
        cofactor_bound=bound,
        cofactor_gap=gap,
        selector_gap=gap,
    ) == 39_597_120_694_510_508_304
    assert gap_recycling_margin(
        hi + 1,
        cofactor_bound=bound,
        cofactor_gap=gap,
        selector_gap=gap,
    ) == -96_402_879_300_365_462_716

    # 0 < (2K+1)/G-G < B at both extremes.
    for k in (lo, hi):
        selector_numerator = 2 * k + 1 - gap * gap
        assert 0 < selector_numerator < bound * gap

    feasible = largest_feasible_k(cofactor_bound=bound, cofactor_gap=gap)
    assert feasible == 78_886_310_904_872_390
    assert feasibility_margin(
        feasible, cofactor_bound=bound, cofactor_gap=gap
    ) == 39_600_928_074_245_939_600
    assert feasibility_margin(
        feasible + 1, cofactor_bound=bound, cofactor_gap=gap
    ) == -96_399_071_925_754_062_844
    assert feasible - hi == 1_486_088

    campbell_direct_root = isqrt(10**31)
    assert campbell_direct_root == 3_162_277_660_168_379
    assert campbell_direct_root**2 <= 10**31 < (campbell_direct_root + 1) ** 2
    assert hi * hi == 6_223_050_047_945_724_554_758_050_641_235_204


def verify() -> None:
    verify_campbell_endpoints()
    verify_small_model()


if __name__ == "__main__":
    verify()
    print("P017 two-stage prime-gap recycling verifier: PASS")
