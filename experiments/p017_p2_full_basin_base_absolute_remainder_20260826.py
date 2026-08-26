#!/usr/bin/env python3
"""Exact-rational certificate for the P017 full-basin base absolute remainder.

At the conservative splice K0, set W=K0+1 and x=W^2.  For the a6 level
D=x^(5/9)=W^(10/9) and odd sifting cutoff z=x^(5/54)=W^(5/27), the sharp odd
interval has length 2K0 and each conventional linear-sieve remainder has
absolute value <1.  Rankin's trick with sigma=4/7 certifies

    #{d<D : d squarefree, d|prod_{3<=p<z}p} < (57/10000) K0,

hence the conventional base error is <0.00285 times the full basin length.

This checker does not transfer the previously frozen source-decimal G_* main
coefficient to the full-basin normalization and does not control prime-lift W1
errors.
"""

from fractions import Fraction as Q
from math import factorial, isqrt

K0 = 116_009_280_740_973_308
W = K0 + 1


def primes_up_to(limit: int) -> list[int]:
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    for p in range(2, isqrt(limit) + 1):
        if sieve[p]:
            sieve[p*p : limit + 1 : p] = b"\x00" * (
                (limit - p*p)//p + 1
            )
    return [n for n in range(2, limit + 1) if sieve[n]]


def integer_nth_root_floor(n: int, degree: int) -> int:
    lo, hi = 0, 1
    while hi**degree <= n:
        hi *= 2
    while lo + 1 < hi:
        mid = (lo + hi)//2
        if mid**degree <= n:
            lo = mid
        else:
            hi = mid
    return lo


def log_lower_atanh(x: Q, terms: int) -> Q:
    assert x >= 1
    z = (x - 1)/(x + 1)
    return sum(
        2*z**(2*j + 1)/Q(2*j + 1) for j in range(terms)
    )


def main() -> None:
    # Exact cutoff: 1439 < z < 1447, and these are consecutive primes.
    assert 1439**27 < W**5 < 1447**27
    primes = [p for p in primes_up_to(1439) if p >= 3]
    assert len(primes) == 227 and primes[-1] == 1439

    # Rankin sigma=4/7:
    # N(D,z) <= D^(4/7) prod_{3<=p<z}(1+p^(-4/7)).
    # Since D=W^(10/9), D^(4/7)=W^(40/63).
    # Upper-enclose t=p^(-4/7) by SCALE/floor(SCALE*p^(4/7)),
    # using exact seventh roots, then the odd fifth alternating partial sum
    # log(1+t) <= t-t^2/2+t^3/3-t^4/4+t^5/5.
    scale = 10**7
    log_product_upper = Q(0)
    for p in primes:
        root = integer_nth_root_floor(scale**7 * p**4, 7)
        assert root**7 <= scale**7 * p**4 < (root + 1)**7
        t = Q(scale, root)
        assert 0 < t < 1
        log_product_upper += (
            t - t*t/2 + t**3/3 - t**4/4 + t**5/5
        )

    # Keep a simple certified decimal envelope for diagnostics.
    assert log_product_upper < Q(916811, 100000)  # 9.16811

    # Lower bound log W by atanh series, decomposing W=10^17*(W/10^17).
    log10_lower = log_lower_atanh(Q(10), 31)
    log_ratio_lower = log_lower_atanh(Q(W, 10**17), 12)
    logW_lower = 17*log10_lower + log_ratio_lower

    # N/K <= exp[-(23/63)log W + log(W/(W-1)) + log_product].
    # Since log(W/(W-1))=log(1+1/K)<1/K, it suffices to prove
    # B=(23/63)logW_lower-1/K-log_product_upper > log(10000/57).
    B = Q(23, 63)*logW_lower - Q(1, K0) - log_product_upper
    assert B > 5

    # exp(B) is lower-bounded by its positive Taylor partial sum.
    exp_lower = sum(B**j/Q(factorial(j)) for j in range(12))
    assert exp_lower > Q(10000, 57)

    # Hence N/K <57/10000 and N/(2K)<57/20000.
    assert Q(57, 20000) < Q(3, 1000)

    print("P017 full-basin base absolute-remainder certificate: PASS")
    print("odd prime cutoff count =", len(primes), "(largest 1439)")
    print("log product upper <", float(log_product_upper))
    print("log W lower >", float(logW_lower))
    print("B lower >", float(B))
    print("exp(B) Taylor lower >", float(exp_lower))
    print("base conventional error / K < 57/10000")
    print("base conventional error / (2K) < 57/20000 = 0.00285")


if __name__ == "__main__":
    main()
