#!/usr/bin/env python3
"""Task-local exact regression for PCF7 complexity/failure certificate.

This checker intentionally validates only the load-bearing finite algebra behind the
PCF7 classification. It is not a general-purpose Enterprise Math tool.
"""

from fractions import Fraction
from math import comb, gcd


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


def primes(lo: int, hi: int):
    return [p for p in range(max(2, lo), hi) if is_prime(p)]


def A_direct(n: int) -> int:
    return comb(2*n, n) ** 2 * comb(3*n, n)


def A_sequence(L: int):
    a = 1
    out = [a]
    for n in range(L - 1):
        num = a * 6 * (2*n + 1) * (3*n + 1) * (3*n + 2)
        den = (n + 1) ** 3
        assert num % den == 0
        a = num // den
        out.append(a)
    return out


def F_values(B: int):
    A = A_sequence(B)
    f = 0
    out = []
    # F_{L+1}=216 F_L + (6L+1)A_L, with F_0=0.
    for L in range(1, B + 1):
        n = L - 1
        f = 216 * f + (6*n + 1) * A[n]
        out.append(f)
    return A, out


def G_mod(N: int, L: int, A):
    inv216 = pow(216, -1, N)
    p = 1
    s = 0
    for n in range(L):
        s = (s + (6*n + 1) * (A[n] % N) * p) % N
        p = (p * inv216) % N
    return s


def support_primes(x: int):
    # Full factorization is only used on small regression values.
    x = abs(x)
    out = set()
    d = 2
    while d * d <= x:
        if x % d == 0:
            out.add(d)
            while x % d == 0:
                x //= d
        d += 1 if d == 2 else 2
    if x > 1:
        out.add(x)
    return out


def fixed_probe_values():
    vals = []
    for s in range(64):
        vals.extend([s*s + 1, s*s + s + 1, abs(s**6 - 1), s**6 + 1])
    return [v for v in vals if v != 0]


def main():
    B = 18
    A, Fs = F_values(B)

    # Independent recurrence/binomial agreement.
    for n, a in enumerate(A):
        assert a == A_direct(n)

    # PCF4 support-size bound and denominator-clearing equivalence.
    gcd_cases = 0
    for L, f in enumerate(Fs, start=1):
        assert 0 < f < 6 * L * L * (216 ** (L - 1))
        for N in (35, 77, 143, 221, 437, 667):
            if gcd(N, 6) != 1:
                continue
            g = G_mod(N, L, A)
            assert (pow(216, L - 1, N) * g - f) % N == 0
            assert gcd(g, N) == gcd(f, N)
            gcd_cases += 1

    # Exact finite-prefix balanced failure witness.
    prefix_support = set()
    for f in Fs:
        prefix_support |= support_primes(f)
    cand = [p for p in primes(1000, 6000) if p not in prefix_support]
    assert len(cand) >= 2
    p, q = cand[0], cand[1]
    if p > q:
        p, q = q, p
    assert q < 2 * p
    N = p * q
    for f in Fs:
        assert gcd(f, N) == 1

    # Frozen public quadratic/sixth probes are finite fixed-integer probes.
    fixed_support = set()
    for v in fixed_probe_values():
        fixed_support |= support_primes(v)
    cand2 = [r for r in primes(10000, 30000) if r not in fixed_support]
    assert len(cand2) >= 2
    p2, q2 = cand2[0], cand2[1]
    if p2 > q2:
        p2, q2 = q2, p2
    assert q2 < 2 * p2
    N2 = p2 * q2
    for s in range(64):
        vals = [s*s + 1, s*s + s + 1, abs(s**6 - 1), s**6 + 1]
        for v in vals:
            if v:
                assert gcd(N2, v) == 1

    # Exact independent-trial amplification identity.
    theta = Fraction(3, 17)
    T = 5
    amplified = 1 - (1 - theta) ** T
    direct = Fraction(17**T - 14**T, 17**T)
    assert amplified == direct
    assert 1 - (1 - Fraction(0, 1)) ** T == 0

    # Input-length regime ordering used in the pending PCF5 appendix.
    for n in range(6, 121, 6):
        assert 2 ** (n // 3) < 2 ** (n // 2) < 2 ** ((2*n) // 3)

    print(
        "PCF7_CHECK_PASS "
        f"recurrence_terms={B} gcd_cases={gcd_cases} "
        f"pcf4_balanced_zero={p}x{q} "
        f"fixed_probe_balanced_zero={p2}x{q2} "
        "amplification=PASS regime_order=PASS"
    )


if __name__ == "__main__":
    main()
