"""Finite verifier for P017 P2 terminal-prime Möbius core collapse.

Research-owner artifact only.  It checks the identities in
docs/P017_P2_TERMINAL_PRIME_CORE_COLLAPSE_20260824.md.  It is finite regression
evidence, not an asymptotic P2 theorem.
"""

from __future__ import annotations

from functools import lru_cache
from itertools import combinations
from math import gcd, isqrt


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    divisor = 3
    while divisor * divisor <= n:
        if n % divisor == 0:
            return False
        divisor += 2
    return True


@lru_cache(maxsize=None)
def prime_factors_squarefree(n: int) -> tuple[int, ...]:
    if n < 1:
        raise ValueError("n must be positive")
    factors: list[int] = []
    x = n
    divisor = 2
    while divisor * divisor <= x:
        if x % divisor == 0:
            factors.append(divisor)
            x //= divisor
            if x % divisor == 0:
                raise ValueError("n must be squarefree")
        divisor += 1 if divisor == 2 else 2
    if x > 1:
        factors.append(x)
    return tuple(factors)


@lru_cache(maxsize=None)
def divisors_squarefree(n: int) -> tuple[int, ...]:
    values = [1]
    for prime in prime_factors_squarefree(n):
        values += [value * prime for value in tuple(values)]
    return tuple(sorted(values))


@lru_cache(maxsize=None)
def mu(n: int) -> int:
    return -1 if len(prime_factors_squarefree(n)) % 2 else 1


def lcm(a: int, b: int) -> int:
    return a // gcd(a, b) * b


def truncated_mobius(d: int, numerator: int, denominator: int) -> int:
    return sum(
        mu(e)
        for e in divisors_squarefree(d)
        if e * denominator <= numerator
    )


def direct_rectangle(k: int, p1: int, p2: int, ell: int) -> int:
    w = k + 1
    total = 0
    divisors = divisors_squarefree(ell)
    for u1 in divisors:
        if u1 * w > p2 * ell:
            continue
        for u2 in divisors:
            if u2 * w > p1 * ell:
                continue
            if gcd(u1, u2) != 1:
                continue
            total += mu(u1 * u2)
    return total


def covariance_form(k: int, p1: int, p2: int, ell: int) -> int:
    w = k + 1
    return mu(ell) * sum(
        mu(d)
        * truncated_mobius(d, p1 * d, w)
        * truncated_mobius(d, p2 * d, w)
        for d in divisors_squarefree(ell)
    )


def small_divisor_sum(d: int, w: int, p: int) -> int:
    return sum(
        mu(f)
        for f in divisors_squarefree(d)
        if f * p < w
    )


def complemented_covariance(k: int, p1: int, p2: int, ell: int) -> int:
    w = k + 1
    return mu(ell) * sum(
        mu(d)
        * small_divisor_sum(d, w, p1)
        * small_divisor_sum(d, w, p2)
        for d in divisors_squarefree(ell)
        if d > 1
    )


def cover_formula(
    k: int,
    p1: int,
    p2: int,
    ell: int,
) -> tuple[int, tuple[tuple[int, int], ...]]:
    w = k + 1
    covers: list[tuple[int, int]] = []
    correction = 0
    divisors = divisors_squarefree(ell)
    for f1 in divisors:
        if f1 * p1 >= w:
            continue
        for f2 in divisors:
            if f2 * p2 >= w:
                continue
            if lcm(f1, f2) != ell:
                continue
            correction += mu(f1) * mu(f2)
            covers.append((f1, f2))
    return -mu(ell) + correction, tuple(covers)


def accepted_superroot_pairs(
    k: int,
    p1: int,
    p2: int,
    ell: int,
    t: int,
) -> tuple[tuple[int, int], ...]:
    n = p1 * p2 * ell * t
    assert k * k < n < (k + 1) * (k + 1)
    pairs: list[tuple[int, int]] = []
    divisors = divisors_squarefree(ell)
    for d1 in divisors:
        for d2 in divisors:
            if lcm(d1, d2) != ell:
                continue
            if p1 * d1 <= k or p2 * d2 <= k:
                continue
            assert t < gcd(d1, d2)
            pairs.append((d1, d2))
    return tuple(pairs)


def overlap_shell_formula(
    k: int,
    p1: int,
    p2: int,
    ell: int,
    t: int,
) -> int:
    w = k + 1
    n = p1 * p2 * ell * t
    total = 0
    for r in divisors_squarefree(ell):
        if r * n >= t * w * w:
            continue
        split_count = 0
        for a in divisors_squarefree(ell // r):
            if a * w <= p2 * ell:
                continue
            if a * p1 * r >= w:
                continue
            split_count += 1
        total += mu(ell // r) * split_count
    return total


def verify() -> None:
    low_prime_sets = (
        (3, 5),
        (3, 5, 7),
        (3, 5, 7, 11),
        (3, 5, 7, 11, 13),
    )

    for low_primes in low_prime_sets:
        ell_values = [1]
        for prime in low_primes:
            ell_values += [value * prime for value in tuple(ell_values)]
        ell_values = sorted(set(ell_values))
        lifted_primes = tuple(
            prime
            for prime in range(max(low_primes) + 1, 100)
            if is_prime(prime)
        )

        for p1, p2 in combinations(lifted_primes, 2):
            for ell in ell_values:
                if ell == 1:
                    continue
                t_samples = set(range(1, min(ell, 51), 2))
                if ell > 51:
                    t_samples.update(
                        candidate
                        for candidate in (
                            ell // 7,
                            ell // 5,
                            ell // 3,
                            ell // 2,
                        )
                        if 1 <= candidate < ell and candidate % 2 == 1
                    )

                for t in sorted(t_samples):
                    n = p1 * p2 * ell * t
                    k = isqrt(n)
                    if k * k == n:
                        continue
                    if p1 >= k + 1 or p2 >= k + 1:
                        continue

                    direct = direct_rectangle(k, p1, p2, ell)
                    covariance = covariance_form(k, p1, p2, ell)
                    complemented = complemented_covariance(k, p1, p2, ell)
                    covered, covers = cover_formula(k, p1, p2, ell)
                    assert direct == covariance == complemented == covered

                    accepted = accepted_superroot_pairs(k, p1, p2, ell, t)
                    if accepted:
                        for f1, f2 in covers:
                            assert gcd(f1, f2) <= t
                        cover_correction = covered + mu(ell)
                        assert cover_correction == overlap_shell_formula(
                            k, p1, p2, ell, t
                        )

                        w = k + 1
                        if 3 * p1 >= w or 3 * p2 >= w:
                            assert direct == -mu(ell)

                        if t == 1:
                            assert direct in (0, -mu(ell))
                            numerator = w * w - p1 * p2 * ell
                            assert 0 < numerator <= 2 * k
                            assert 3 * numerator < 2 * p1 * w

    # Direct one-high-prime identity, including empty rectangles.
    for k in range(20, 180):
        w = k + 1
        high_primes = tuple(
            p for p in range(3, w) if is_prime(p) and 3 * p >= w
        )
        other_primes = tuple(p for p in range(3, w) if is_prime(p))
        for ell in (3, 5, 7, 15, 21, 35, 105, 1155):
            for high in high_primes[:3]:
                for other in other_primes[:8]:
                    if high == other:
                        continue
                    actual = direct_rectangle(k, high, other, ell)
                    expected = mu(ell) * (int(ell * other < w) - 1)
                    assert actual == expected


if __name__ == "__main__":
    verify()
    print("P017 P2 terminal-prime Möbius core collapse verifier: PASS")
