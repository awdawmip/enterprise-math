#!/usr/bin/env python3
"""Exact checker for the 2/3/5/no-break phase control ladder."""

from __future__ import annotations


def F(B: int, H: int, r: int) -> int:
    return H + (B * r * r + (r & 1)) // 2


def is_prime_64(n: int) -> bool:
    if n < 2:
        return False
    for p in (2,3,5,7,11,13,17,19,23,29,31,37):
        if n % p == 0:
            return n == p
    d = n - 1
    s = 0
    while d % 2 == 0:
        s += 1
        d //= 2
    for a in (2,325,9375,28178,450775,9780504,1795265022):
        if a % n == 0:
            continue
        x = pow(a, d, n)
        if x in (1, n-1):
            continue
        for _ in range(s-1):
            x = x*x % n
            if x == n-1:
                break
        else:
            return False
    return True


def main() -> None:
    # First-breaker-2: B=1 alternates parity, so no two consecutive >2 can both be prime.
    for H in range(8):
        vals = [F(1, H, r) for r in range(1, 20)]
        for a,b in zip(vals, vals[1:]):
            if a > 2 and b > 2:
                assert (a % 2 == 0) or (b % 2 == 0)

    # First-breaker-3: B=7 realizes the sharp 5-prime run.
    vals7 = [F(7, 15, r) for r in range(1, 7)]
    assert vals7 == [19,29,47,71,103,141]
    assert all(is_prime_64(v) for v in vals7[:5])
    assert vals7[5] == 3 * 47

    # First-breaker-5: replay the frozen native B=3 sharp-nine control packet.
    native9 = [
        171283421,171315481,171347543,171379609,171411677,
        171443749,171475823,171507901,171539981,
    ]
    assert all(is_prime_64(v) for v in native9)

    # No-break: B=15 realizes 12 consecutive primes.
    vals15 = [F(15, 977767522784021, 610+j) for j in range(12)]
    assert all(is_prime_64(v) for v in vals15)

    print("PHASE_2_BREAK_CAP1=PASS")
    print("PHASE_3_BREAK_SHARP5=19,29,47,71,103")
    print("PHASE_5_BREAK_NATIVE_SHARP9=PASS")
    print("PHASE_NO_BREAK_B15_PRIME_RUN12=PASS")


if __name__ == "__main__":
    main()
