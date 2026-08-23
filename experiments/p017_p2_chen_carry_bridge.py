"""Exact finite verifier for P017 P2/Chen carry bridge.

Research owner artifact only.  This script checks finite instances of the exact
identities in docs/P017_P2_CHEN_CARRY_BRIDGE_20260823.md.  It is not an
asymptotic proof and makes no all-K P2 claim.
"""

from __future__ import annotations

from math import isqrt


def hit_count(k: int, m: int) -> int:
    assert k >= 1 and m >= 1
    return (k * k + 2 * k) // m - (k * k) // m


def odd_quotient_count(k: int, m: int) -> int:
    return hit_count(k, m) - hit_count(k, 2 * m)


def centered_odd_incidence_count(k: int, m: int) -> int:
    assert m % 2 == 1
    center = k * (k + 1)
    return sum(
        1
        for s in range(1 - k, k + 1)
        if s % 2 != 0 and (center + s) % m == 0
    )


def standard_remainder_numerator(k: int, q: int) -> int:
    """Return q*r_K(q) exactly as an integer.

    r_K(q)=H_q(K)-2K/q, so q*r_K(q)=q H_q(K)-2K.
    """
    return q * hit_count(k, q) - 2 * k


def binary_remainder_numerator(k: int, m: int) -> int:
    """Return m*(O_m(K)-K/m)=m O_m(K)-K exactly."""
    return m * odd_quotient_count(k, m) - k


def omega_big(n: int) -> int:
    """Number of prime factors with multiplicity, for finite verification."""
    assert n >= 1
    x = n
    total = 0
    p = 2
    while p * p <= x:
        while x % p == 0:
            x //= p
            total += 1
        p += 1 if p == 2 else 2
    if x > 1:
        total += 1
    return total


def visible_factor_data(k: int, n: int) -> tuple[int, int]:
    """Return (visible multiplicity h, visible product v), with p<K+1."""
    w = k + 1
    x = n
    h = 0
    v = 1
    p = 2
    while p * p <= x:
        e = 0
        while x % p == 0:
            x //= p
            e += 1
        if e and p < w:
            h += e
            v *= p**e
        p += 1 if p == 2 else 2
    if x > 1 and x < w:
        h += 1
        v *= x
    return h, v


def root_weight_is_positive_exact(k: int, n: int) -> bool:
    """Sign of 1-h+log_W(v), decided without floating-point logarithms."""
    assert k >= 2 and k * k < n < (k + 1) * (k + 1)
    w = k + 1
    h, v = visible_factor_data(k, n)
    if h == 0:
        return True
    # 1-h+log_W(v)>0 iff v>W^(h-1).
    return v > w ** (h - 1)


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def cofactor_window(k: int, p: int) -> tuple[int, int]:
    return (k * k // p + 1, (k * k + 2 * k) // p)


def semiprime_count_direct(k: int) -> int:
    return sum(1 for n in range(k * k + 1, (k + 1) ** 2) if omega_big(n) == 2)


def semiprime_count_via_windows(k: int) -> int:
    total = 0
    for p in range(2, k + 1):
        if not is_prime(p):
            continue
        lo, hi = cofactor_window(k, p)
        total += sum(1 for q in range(lo, hi + 1) if is_prime(q))
    return total


def verify(limit_k: int = 120, limit_m: int = 500) -> None:
    # P2-R01: exact sign detector.
    for k in range(2, limit_k + 1):
        for n in range(k * k + 1, (k + 1) ** 2):
            assert root_weight_is_positive_exact(k, n) == (omega_big(n) <= 2)

    # P2-R02 and P2-R03.
    for k in range(2, limit_k + 1):
        for m in range(1, limit_m + 1):
            # m*(r_K(m)-r_K(2m))
            # = [mH_m-2K] - [mH_2m-K]
            transferred = (
                m * hit_count(k, m) - 2 * k
                - (m * hit_count(k, 2 * m) - k)
            )
            assert binary_remainder_numerator(k, m) == transferred

            if m % 2 == 1:
                o = odd_quotient_count(k, m)
                assert o == centered_odd_incidence_count(k, m)
                assert o in (k // m, k // m + 1)
                if m > k:
                    assert o in (0, 1)

    # P2-R05: exact semiprime count through cofactor windows.
    for k in range(4, limit_k + 1):
        windows: list[tuple[int, int, int]] = []
        for p in range(2, k + 1):
            if is_prime(p):
                lo, hi = cofactor_window(k, p)
                windows.append((p, lo, hi))
        for i in range(len(windows)):
            p, lo_p, hi_p = windows[i]
            for j in range(i + 1, len(windows)):
                r, lo_r, hi_r = windows[j]
                assert p < r
                assert hi_r < lo_p
        assert semiprime_count_direct(k) == semiprime_count_via_windows(k)


if __name__ == "__main__":
    verify()
    print("P017 P2/Chen carry bridge finite verifier: PASS")
