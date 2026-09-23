#!/usr/bin/env python3
"""Exact regression for W_p == p (mod p^2) on target primes p<5000.

Regression/falsification only. The all-prime proof is the independent Chan--Liaw
normalization + Chisholm Theorem 1 hypothesis/sign audit.
"""

from math import isqrt


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d <= isqrt(n):
        if n % d == 0:
            return False
        d += 2
    return True


def target_primes(bound: int = 5000):
    return [p for p in range(5, bound) if p % 24 in (13, 19) and is_prime(p)]


def stripped_factorials(p: int):
    """Return unit factorial and p-valuation arrays through 3(p-1).

    All binomial upper indices used below are <3p, so this is enough to compute
    C(n,k) modulo p^2 without ever inverting a multiple of p.
    """
    mod = p * p
    N = 3 * (p - 1)
    unit = [1] * (N + 1)
    vp = [0] * (N + 1)
    for i in range(1, N + 1):
        x = i
        v = 0
        while x % p == 0:
            x //= p
            v += 1
        unit[i] = unit[i - 1] * (x % mod) % mod
        vp[i] = vp[i - 1] + v
    return unit, vp


def binom_mod_p2(n: int, k: int, p: int, unit, vp) -> int:
    if k < 0 or k > n:
        return 0
    mod = p * p
    v = vp[n] - vp[k] - vp[n - k]
    if v >= 2:
        return 0
    den = unit[k] * unit[n - k] % mod
    u = unit[n] * pow(den, -1, mod) % mod
    return u * (p if v == 1 else 1) % mod


def weighted_sum_mod_p2(p: int) -> int:
    """Compute W_p using the exact integer-binomial identity.

    W_p = sum_{k=0}^{p-1} (6k+1) C(2k,k)^2 C(3k,k) / 216^k.
    Since p>3, 216 is a unit modulo p^2.
    """
    mod = p * p
    unit, vp = stripped_factorials(p)
    inv216 = pow(216, -1, mod)
    inv216k = 1
    total = 0
    for k in range(p):
        c2 = binom_mod_p2(2 * k, k, p, unit, vp)
        c3 = binom_mod_p2(3 * k, k, p, unit, vp)
        total = (total + (6 * k + 1) * c2 * c2 * c3 * inv216k) % mod
        inv216k = inv216k * inv216 % mod
    return total


def main() -> None:
    primes = target_primes()
    failures = []
    classes = {13: 0, 19: 0}
    for p in primes:
        classes[p % 24] += 1
        got = weighted_sum_mod_p2(p)
        if got != p:
            failures.append((p, got, p * p))
    print({
        "bound": 5000,
        "target_prime_count": len(primes),
        "class_counts": classes,
        "failure_count": len(failures),
        "failures": failures,
    })
    assert len(primes) == 166
    assert classes == {13: 83, 19: 83}
    assert not failures


if __name__ == "__main__":
    main()
