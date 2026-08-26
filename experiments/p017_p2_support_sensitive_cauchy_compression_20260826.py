#!/usr/bin/env python3
"""Exact certificate for P017 support-sensitive cross-state Cauchy compression.

This checker exploits the source condition m,n | P(z) retained by the
Iwaniec linear-sieve factorable remainder.  At the conservative Tier-A splice
it certifies:

* p<z means exactly p<=1439;
* the top N-block contains exactly 325 squarefree z-smooth integers;
* the positive Fourier cutoff is H_+=814;
* the exact (n,h)-diagonal energy is Delta=314078;
* a Rankin product gives A_M < M/100 for the top M-block;
* the supported truncated block is <0.039*y;
* after the already-certified order-4 tail <0.019*y, one block is <0.058*y.

It does not sum the Rosser/Iwaniec factorization pieces or all geometric
sub-blocks, and it does not prove a finite P2 threshold.
"""

from collections import Counter
from fractions import Fraction as Q
from math import isqrt


K0 = 116_009_280_740_973_308
X0 = K0 * K0

THETA = Q(4999, 10000)
D_EXP = Q(5, 9)
MU = Q(161777, 360000)
NU = Q(4247, 40000)
ETA = Q(1, 40)
RHO = Q(6, 5)


def primes_up_to(limit: int) -> list[int]:
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    for p in range(2, isqrt(limit) + 1):
        if sieve[p]:
            sieve[p * p : limit + 1 : p] = b"\x00" * (
                (limit - p * p) // p + 1
            )
    return [n for n in range(2, limit + 1) if sieve[n]]


def integer_nth_root_floor(n: int, degree: int) -> int:
    if n < 2:
        return n
    lo, hi = 1, 2
    while hi**degree <= n:
        hi *= 2
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if mid**degree <= n:
            lo = mid
        else:
            hi = mid
    return lo


def squarefree_z_smooth(n: int, primes: list[int], pmax: int) -> bool:
    """Whether n is squarefree and all prime factors are <=pmax."""
    x = n
    for p in primes:
        if p * p > x:
            break
        if x % p == 0:
            x //= p
            if x % p == 0:
                return False
    return x == 1 or x <= pmax


def main() -> None:
    # z = X^(5/54).  The adjacent primes 1439,1447 pin the prime support.
    assert 1439**54 < X0**5 < 1447**54
    primes = primes_up_to(1439)
    assert len(primes) == 228 and primes[-1] == 1439

    # Rigorous Rankin-product input.  For every p<=1439 we upper-bound
    # p^(-3/5) by SCALE/floor(SCALE*p^(3/5)) using integer fifth roots.
    scale = 10**12
    reciprocal_power_sum_upper = Q(0)
    for p in primes:
        root = integer_nth_root_floor(scale**5 * p**3, 5)
        assert root**5 <= scale**5 * p**3 < (root + 1) ** 5
        reciprocal_power_sum_upper += Q(scale, root)
    assert reciprocal_power_sum_upper < Q(1819, 200)  # 9.095

    # Elementary exact proof exp(9.095)<10^4: ln(10)>2.3 from the first
    # 11 positive terms of the atanh expansion with z=(10-1)/(10+1)=9/11.
    z10 = Q(9, 11)
    ln10_lower = sum(
        2 * z10 ** (2 * j + 1) / Q(2 * j + 1) for j in range(11)
    )
    assert ln10_lower > Q(23, 10)
    assert Q(1819, 200) < Q(46, 5)  # 9.095 < 9.2 = 4*2.3

    # Rankin count for active m in (M, rho M]:
    # A_M <= (rho M)^(3/5) prod_{p<z}(1+p^(-3/5)) < M/100.
    # It is enough that M^(2/5)>1.2e6.
    m_two_fifths_exp = Q(2, 5) * MU
    assert m_two_fifths_exp == Q(161777, 900000)
    assert X0 > 10**34
    assert 34 * m_two_fifths_exp > Q(61, 10)
    assert 6**10 < 10 * 5**10  # 10^(1/10)>6/5

    # N=X^nu lies strictly between 4203 and 4204, while rho*N lies
    # strictly between 5044 and 5045.  Thus the integer block is exact.
    assert 4203**40000 < X0**4247 < 4204**40000
    assert (5044 * 5) ** 40000 < 6**40000 * X0**4247
    assert 6**40000 * X0**4247 < (5045 * 5) ** 40000

    active_n = [
        n for n in range(4204, 5045) if squarefree_z_smooth(n, primes, 1439)
    ]
    assert len(active_n) == 325
    assert Q(len(active_n), 841) < Q(387, 1000)

    # H = rho^2 X^(d-theta+eta) is between 814 and 815, so the positive
    # frequencies 1<=h<H are exactly h=1,...,814.
    h_exp = D_EXP - THETA + ETA
    assert h_exp == Q(7259, 90000)
    assert (814 * 25) ** 90000 < 36**90000 * X0**7259
    assert 36**90000 * X0**7259 < (815 * 25) ** 90000
    h_max = 814

    # Exact supported Fourier diagonal: Delta=sum_s multiplicity(s)^2,
    # s=hn, n in active N-block, 1<=h<=814.
    product_multiplicity = Counter(
        n * h for n in active_n for h in range(1, h_max + 1)
    )
    delta = sum(mult * mult for mult in product_multiplicity.values())
    assert len(active_n) * h_max == 264_550
    assert max(product_multiplicity.values()) == 5
    assert delta == 314_078

    # Supported positive-frequency Cauchy bound.  Write r for the final
    # signed-frequency truncated block divided by y.  With A_M<M/100 and
    # L_M<=(201/1000)M, the diagonal part of r^2 is below 143e-6.
    diag_r2 = Q(804 * delta, 100_000 * 4203**2)
    assert diag_r2 < Q(143, 10**6)

    # For the off-diagonal use the explicit reciprocal-block constant 15,
    # |k|<=rho*H*N, and sqrt(rho*H)<32.  After inserting A_M<M/100,
    # the X exponent in r^2 is -52741/120000.
    assert RHO * h_max < 32**2
    off_decay = -(MU + Q(1, 2) - Q(5, 2) * D_EXP)
    assert off_decay == Q(52741, 120000)
    off_constant = Q(96, 5) * len(active_n) ** 2 * h_max**2
    off_target = Q(27, 20_000)  # 0.00135
    ratio = off_constant / off_target
    assert ratio.numerator**off_decay.denominator < (
        ratio.denominator**off_decay.denominator * X0**off_decay.numerator
    )

    # Therefore r^2 < 0.039^2, hence |R_trunc^block|<0.039*y.
    assert Q(143, 10**6) + off_target < Q(39, 1000) ** 2

    # Combine with the separately certified order-4 block tail <0.019*y.
    assert Q(39, 1000) + Q(19, 1000) == Q(58, 1000)

    print("P017 support-sensitive Cauchy compression certificate: PASS")
    print("prime support p<z: p<=1439; count =", len(primes))
    print("Rankin sum upper < 1819/200; hence A_M < M/100")
    print("active N-block count =", len(active_n), "/ 841")
    print("positive H max =", h_max)
    print("(n,h) diagonal Delta =", delta)
    print("max product multiplicity =", max(product_multiplicity.values()))
    print("truncated supported block / y < 39/1000")
    print("with certified tail: full supported block / y < 58/1000")


if __name__ == "__main__":
    main()
