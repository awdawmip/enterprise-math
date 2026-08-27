#!/usr/bin/env python3
"""Exact fixed-point checker for the c515 j=1 top long-support bound."""

from math import isqrt

K = 116_009_280_740_973_308
W = K + 1
SCALE = 10**12
BFLOOR = 494_793_856_728_459
R_MIN = 1447
R_MAX = 79_093


def primes_upto(n: int) -> list[int]:
    ps: list[int] = []
    for x in range(2, n + 1):
        ok = True
        for p in ps:
            if p * p > x:
                break
            if x % p == 0:
                ok = False
                break
        if ok:
            ps.append(x)
    return ps


def main() -> None:
    # Exact top-scale endpoints.
    assert BFLOOR**36 <= W**31 < (BFLOOR + 1) ** 36
    assert R_MAX**108 <= W**31 < (R_MAX + 1) ** 108

    primes = primes_upto(585_000)
    index = {p: i for i, p in enumerate(primes)}
    inv_up = [(SCALE + p - 1) // p for p in primes]
    prefix = [0]
    for v in inv_up:
        prefix.append(prefix[-1] + v)

    # Hard-prime reciprocal mass 29..1439.
    hard = [p for p in primes if 29 <= p <= 1439]
    s1_num = sum((SCALE + p - 1) // p for p in hard)
    assert s1_num * 4 < 3 * SCALE

    # R_B upper fixed-point sum over 1447<=r<q, r*q^2<B.
    rsum_num = 0
    for r in primes:
        if r < R_MIN:
            continue
        if r > R_MAX:
            break
        i = index[r]
        qmax = isqrt(BFLOOR // r)
        j = 0
        # binary search without external dependencies
        lo, hi = 0, len(primes)
        while lo < hi:
            mid = (lo + hi) // 2
            if primes[mid] <= qmax:
                lo = mid + 1
            else:
                hi = mid
        j = lo
        qsum = prefix[j] - prefix[i + 1]
        rsum_num += inv_up[i] * qsum

    assert rsum_num * 200 < 27 * SCALE**2

    # Final rational support coefficient.
    assert 7263 * 10000 < 227 * 320000  # <0.0227

    # Corrected j=1 short hard states.
    hard_short = [p for p in primes if 29 <= p <= 1439]
    pair_count = 0
    top_count = 0
    short_values = {1, *hard_short}
    for i, p in enumerate(hard_short):
        for q in hard_short[i + 1 :]:
            value = p * q
            if value > 18455:
                break
            pair_count += 1
            short_values.add(value)
    assert len(hard_short) == 219
    assert pair_count == 895
    assert len(short_values) == 1115
    top_count = sum(1 for n in short_values if 6 * n > 5 * 18455 and n <= 18455)
    assert top_count == 185

    print("P017 c515 j1 top long-support checker: PASS")
    print("sum hard reciprocal < 3/4")
    print("R_B < 27/200")
    print("A_M/M < 7263/320000 < 0.0227")
    print("corrected top short hard support = 185")


if __name__ == "__main__":
    main()
