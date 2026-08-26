#!/usr/bin/env python3
"""Exact fixed-point Rankin-DP certificate for the lower Rosser support.

At the Tier-A full-basin scale, the lower Rosser-Iwaniec support is a strict
subset of all odd squarefree z-smooth moduli.  We use the necessary positional
constraints for descending prime factors p_1>...>p_r:

    p_1...p_{j-1} p_j^3 < D   for every even j.

Hence necessarily p_j^(j+2)<D at every even position j.  A weighted dynamic
program over the 227 odd primes p<=1439, with sigma=97/200 and a common fixed
point denominator 10^9, certifies

    #supp(lambda^-) < (29/10000) K0,

so the sharp-odd base lower-sieve remainder is <0.00145 of the full basin
length 2K0.

This is an upper bound from necessary positional conditions; it does not need
to enumerate the actual Rosser support exactly.
"""

from math import isqrt
from fractions import Fraction as Q

K0 = 116_009_280_740_973_308
W = K0 + 1
SIG_NUM = 97
SIG_DEN = 200
SCALE = 10**9


def primes_up_to(limit: int) -> list[int]:
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    for p in range(2, isqrt(limit) + 1):
        if sieve[p]:
            sieve[p*p:limit+1:p] = b"\x00" * (
                (limit - p*p)//p + 1
            )
    return [n for n in range(2, limit + 1) if sieve[n]]


def ceil_scaled_inverse_power(p: int) -> int:
    """Smallest q with q/SCALE >= p^(-97/200), by integer powers only."""
    lo, hi = 0, SCALE
    target = SCALE**SIG_DEN
    p_pow = p**SIG_NUM
    while lo + 1 < hi:
        mid = (lo + hi)//2
        if mid**SIG_DEN * p_pow >= target:
            hi = mid
        else:
            lo = mid
    assert hi**SIG_DEN * p_pow >= target
    assert lo**SIG_DEN * p_pow < target
    return hi


def main() -> None:
    # Same exact odd prime cutoff as the full-basin remainder certificate.
    assert 1439**27 < W**5 < 1447**27
    primes = [p for p in primes_up_to(1439) if p >= 3]
    assert len(primes) == 227
    primes.sort(reverse=True)

    weights = {p: ceil_scaled_inverse_power(p) for p in primes}

    # dp[k] is an integer numerator over SCALE^k for the weighted sum of
    # selected descending k-tuples satisfying the necessary lower-Rosser
    # positional caps encountered so far.
    dp = [0] * 64
    dp[0] = 1
    max_k = 0
    for p in primes:
        wp = weights[p]
        for k in range(max_k, -1, -1):
            if dp[k] == 0:
                continue
            j = k + 1
            # Lower Rosser condition is imposed at even positions.
            if j % 2 == 0:
                # p_j^(j+2) < D = W^(10/9), clear the denominator 9.
                if not (p**(9*(j+2)) < W**10):
                    continue
            dp[j] += dp[k] * wp
        max_k = min(max_k + 1, len(dp) - 1)

    while dp and dp[-1] == 0:
        dp.pop()
    assert len(dp) - 1 == 18

    weighted_superset = sum(
        Q(dp[k], SCALE**k) for k in range(len(dp))
    )

    # Rankin: support count <= D^sigma * weighted_superset, with
    # D^sigma = (W^(10/9))^(97/200) = W^(97/180).
    # Prove W^(97/180)*U < (29/10000)K by raising to the 180th power.
    target = Q(29*K0, 10000)
    lhs_num = W**97 * weighted_superset.numerator**180
    lhs_den = weighted_superset.denominator**180
    rhs_num = target.numerator**180
    rhs_den = target.denominator**180
    assert lhs_num * rhs_den < rhs_num * lhs_den

    print("P017 full-basin lower Rosser support certificate: PASS")
    print("odd primes =", len(primes))
    print("maximum DP position =", len(dp)-1)
    print("weighted positional superset =", float(weighted_superset))
    print("#supp(lambda^-) < (29/10000) K")
    print("base lower-sieve remainder / (2K) < 29/20000 = 0.00145")


if __name__ == "__main__":
    main()
