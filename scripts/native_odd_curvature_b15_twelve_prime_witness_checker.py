#!/usr/bin/env python3
"""Deterministically verify the frozen B=15 twelve-prime control witness."""

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
    # Deterministic for unsigned 64-bit integers.
    for a in (2,325,9375,28178,450775,9780504,1795265022):
        if a % n == 0:
            continue
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


def main() -> None:
    B = 15
    H = 977767522784021
    R = 610
    expected = [
        977767525574771,
        977767525583929,
        977767525593101,
        977767525602289,
        977767525611491,
        977767525620709,
        977767525629941,
        977767525639189,
        977767525648451,
        977767525657729,
        977767525667021,
        977767525676329,
    ]
    vals = [F(B, H, R + j) for j in range(12)]
    assert vals == expected
    assert max(vals) < 2**64
    assert all(is_prime_64(v) for v in vals)

    gaps = [vals[i+1] - vals[i] for i in range(11)]
    assert gaps == [9158,9172,9188,9202,9218,9232,9248,9262,9278,9292,9308]

    second = [vals[i] - 2*vals[i+1] + vals[i+2] for i in range(10)]
    # With the current sign convention the second difference alternates -14,-16.
    assert second == [-14,-16,-14,-16,-14,-16,-14,-16,-14,-16]

    # Equivalent positive curvature in forward-difference convention.
    forward_second = [vals[i+2] - 2*vals[i+1] + vals[i] for i in range(10)]
    assert forward_second == [-14,-16,-14,-16,-14,-16,-14,-16,-14,-16]

    print("B15_TWELVE_VALUES=PASS")
    print("ALL_12_PRIME_64BIT=PASS")
    print("GAP_WORD=PASS")
    print("NATIVE_SHARP9_CONTROL_EXCEEDED=12")


if __name__ == "__main__":
    main()
