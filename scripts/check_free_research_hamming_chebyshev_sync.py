#!/usr/bin/env python3
"""Exact finite checks for the Hamming--Chebyshev synchronization frontier.

The checker uses only integers, exact fractions, and formal prime-log symbols.
It verifies finite identities; it does not prove the PNT asymptotic or claim
novelty for the classical Farhi/Kummer/Selberg ingredients.
"""

from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from math import comb, factorial, gcd
from typing import DefaultDict, Dict, Iterable, Tuple

PrimeVector = Dict[int, int]
QuadraticForm = Dict[Tuple[int, int], int]


def lcm(a: int, b: int) -> int:
    assert a >= 0 and b >= 0
    if a == 0 or b == 0:
        return 0
    return a // gcd(a, b) * b


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


def primes_upto(limit: int) -> list[int]:
    return [n for n in range(2, limit + 1) if is_prime(n)]


def factorization(n: int) -> PrimeVector:
    assert n >= 1
    out: PrimeVector = {}
    d = 2
    while d * d <= n:
        if n % d == 0:
            e = 0
            while n % d == 0:
                n //= d
                e += 1
            out[d] = e
        d += 1
    if n > 1:
        out[n] = 1
    return out


def vp(n: int, p: int) -> int:
    assert n >= 1 and is_prime(p)
    e = 0
    while n % p == 0:
        n //= p
        e += 1
    return e


def floor_log_p(n: int, p: int) -> int:
    assert n >= 1 and p >= 2
    q = 0
    power = p
    while power <= n:
        q += 1
        power *= p
    return q


def mobius(n: int) -> int:
    assert n >= 1
    factors = factorization(n)
    if any(e > 1 for e in factors.values()):
        return 0
    return -1 if len(factors) % 2 else 1


def divisors(n: int) -> list[int]:
    assert n >= 1
    return [d for d in range(1, n + 1) if n % d == 0]


def lcm_range(n: int) -> int:
    value = 1
    for k in range(1, n + 1):
        value = lcm(value, k)
    return value


def hamming_row_lcm(m: int) -> int:
    assert m >= 0
    value = 1
    for k in range(m + 1):
        value = lcm(value, comb(m, k))
    return value


def is_prime_power(n: int) -> tuple[bool, int | None, int | None]:
    assert n >= 1
    factors = factorization(n)
    if len(factors) != 1:
        return False, None, None
    p, a = next(iter(factors.items()))
    return True, p, a


def legendre_factorial_vp(n: int, p: int) -> int:
    assert n >= 0 and is_prime(p)
    total = 0
    power = p
    while power <= n:
        total += n // power
        power *= p
    return total


def square_linear_form(v: PrimeVector) -> QuadraticForm:
    out: DefaultDict[Tuple[int, int], int] = defaultdict(int)
    items = sorted(v.items())
    for i, (p, ep) in enumerate(items):
        out[(p, p)] += ep * ep
        for q, eq in items[i + 1 :]:
            out[(p, q)] += 2 * ep * eq
    return dict(out)


def multiply_linear_forms(a: PrimeVector, b: PrimeVector) -> QuadraticForm:
    out: DefaultDict[Tuple[int, int], int] = defaultdict(int)
    for p, ep in a.items():
        for q, eq in b.items():
            key = (p, q) if p <= q else (q, p)
            out[key] += ep * eq
    return dict(out)


def add_quadratic(target: DefaultDict[Tuple[int, int], int], source: QuadraticForm, scale: int = 1) -> None:
    for key, value in source.items():
        target[key] += scale * value
        if target[key] == 0:
            del target[key]


def mangoldt_vector(n: int) -> PrimeVector:
    """Formal version of Lambda(n): X_p on p-powers, zero otherwise."""
    prime_power, p, _a = is_prime_power(n)
    if not prime_power:
        return {}
    assert p is not None
    return {p: 1}


def check_maximal_carry_envelope(limit: int = 180) -> None:
    for N in range(1, limit + 1):
        m = N - 1
        for p in primes_upto(N + 5):
            q = floor_log_p(N, p)
            a = vp(N, p)
            expected = q - a
            actual = max(vp(comb(m, k), p) for k in range(m + 1))
            assert actual == expected, (N, p, actual, expected)

            # Explicit maximizing shell from PHC-T01.
            k_star = p**q - p**a
            assert 0 <= k_star <= m
            assert vp(comb(m, k_star), p) == expected, (N, p, k_star)


def check_hamming_sync_identity(limit: int = 180) -> None:
    for N in range(1, limit + 1):
        clock = hamming_row_lcm(N - 1)
        envelope = lcm_range(N)
        assert N * clock == envelope, N

        # Every prime direction splits into top-state occupation plus row carry depth.
        for p in primes_upto(N):
            assert vp(N, p) + vp(clock, p) == floor_log_p(N, p), (N, p)


def check_prime_power_jump_law(limit: int = 250) -> None:
    previous = 1
    for N in range(1, limit + 1):
        current = N * hamming_row_lcm(N - 1)
        assert current % previous == 0
        jump = current // previous
        pp, p, _a = is_prime_power(N)
        if pp:
            assert jump == p, (N, jump, p)
        else:
            assert jump == 1, (N, jump)
        previous = current


def check_dyadic_hamming_sandwich(limit: int = 120) -> None:
    for n in range(1, limit + 1):
        lower = lcm_range(2 * n) // lcm_range(n)
        central = comb(2 * n, n)
        upper = lcm_range(2 * n)
        assert central % lower == 0, n
        assert upper % central == 0, n

        # Target-free central-shell bounds from the row sum.
        assert central * (2 * n + 1) >= 4**n
        assert central < 4**n


def check_chebyshev_lower_bound(limit: int = 220) -> None:
    for N in range(1, limit + 1):
        assert lcm_range(N) >= 2 ** (N - 1), N


def check_mobius_opposite_corner_product(limit: int = 140) -> None:
    """Compare prime exponents instead of constructing a huge signed rational product."""
    for N in range(1, limit + 1):
        for p in primes_upto(N):
            rhs_exp = 0
            for d in range(1, N + 1):
                mu = mobius(d)
                if mu:
                    rhs_exp += mu * legendre_factorial_vp(N // d, p)
            assert rhs_exp == floor_log_p(N, p), (N, p, rhs_exp)

        # Small direct rational replay of the signed path-volume identity.
        if N <= 35:
            product = Fraction(1, 1)
            for d in range(1, N + 1):
                mu = mobius(d)
                path_count = factorial(N // d)
                if mu == 1:
                    product *= path_count
                elif mu == -1:
                    product /= path_count
            assert product.denominator == 1
            assert product.numerator == lcm_range(N), N


def check_selberg_local_formal_identity(limit: int = 180) -> None:
    """Verify mu*log^2 = Lambda log + Lambda*Lambda over formal log-prime symbols."""
    for n in range(1, limit + 1):
        lhs: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        for d in divisors(n):
            add_quadratic(lhs, square_linear_form(factorization(n // d)), mobius(d))

        rhs: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        add_quadratic(rhs, multiply_linear_forms(mangoldt_vector(n), factorization(n)))
        for d in divisors(n):
            add_quadratic(
                rhs,
                multiply_linear_forms(mangoldt_vector(d), mangoldt_vector(n // d)),
            )

        assert dict(lhs) == dict(rhs), (n, dict(lhs), dict(rhs))


def check_mobius_floor_kernel(limit: int = 250) -> None:
    for X in range(1, limit + 1):
        value = sum(mobius(d) * (X // d) for d in range(1, X + 1))
        assert value == 1, X


def main() -> None:
    check_maximal_carry_envelope()
    check_hamming_sync_identity()
    check_prime_power_jump_law()
    check_dyadic_hamming_sandwich()
    check_chebyshev_lower_bound()
    check_mobius_floor_kernel()
    check_mobius_opposite_corner_product()
    check_selberg_local_formal_identity()
    print("Hamming--Chebyshev synchronization finite checks: PASS")


if __name__ == "__main__":
    main()
