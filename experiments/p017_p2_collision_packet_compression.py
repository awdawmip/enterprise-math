"""Finite verifier for P017 P2 collision packet compression.

Research-owner artifact only.  It checks the exact identities in
docs/P017_P2_COLLISION_PACKET_COMPRESSION_20260824.md.  It is finite regression
evidence, not an asymptotic P2 theorem.
"""

from __future__ import annotations

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


def squarefree_divisors(n: int) -> tuple[int, ...]:
    factors = prime_factors_squarefree(n)
    values = [1]
    for prime in factors:
        values += [value * prime for value in tuple(values)]
    return tuple(sorted(values))


def omega(n: int) -> int:
    return len(prime_factors_squarefree(n))


def mu_squarefree(n: int) -> int:
    return -1 if omega(n) % 2 else 1


def lcm(a: int, b: int) -> int:
    return a // gcd(a, b) * b


def lcm_pairs(ell: int) -> tuple[tuple[int, int], ...]:
    divisors = squarefree_divisors(ell)
    return tuple(
        (d1, d2)
        for d1 in divisors
        for d2 in divisors
        if lcm(d1, d2) == ell
    )


def direct_superroot_mobius_coefficient(
    k: int,
    p1: int,
    p2: int,
    ell: int,
    t: int,
) -> tuple[int, tuple[tuple[int, int], ...]]:
    n = p1 * p2 * ell * t
    assert k * k < n < (k + 1) * (k + 1)
    accepted: list[tuple[int, int]] = []
    total = 0
    for d1, d2 in lcm_pairs(ell):
        m1 = p1 * d1
        m2 = p2 * d2
        if m1 <= k or m2 <= k:
            continue
        a1 = n // m1
        a2 = n // m2
        assert n % m1 == 0 and n % m2 == 0
        assert a1 % 2 == 1 and a2 % 2 == 1
        assert a1 <= k and a2 <= k
        assert t < gcd(d1, d2)
        total += mu_squarefree(d1) * mu_squarefree(d2)
        accepted.append((d1, d2))
    return total, tuple(accepted)


def rectangular_mobius_coefficient(
    k: int,
    p1: int,
    p2: int,
    ell: int,
) -> int:
    w = k + 1
    divisors = squarefree_divisors(ell)
    total = 0
    for u1 in divisors:
        if u1 * w > p2 * ell:
            continue
        for u2 in divisors:
            if u2 * w > p1 * ell:
                continue
            if gcd(u1, u2) != 1:
                continue
            total += mu_squarefree(u1 * u2)
    return total


def divisor_window_mobius_coefficient(
    k: int,
    p1: int,
    p2: int,
    ell: int,
) -> int:
    w = k + 1
    total = 0
    for h in squarefree_divisors(ell):
        split_count = 0
        for u in squarefree_divisors(h):
            if u * w <= p2 * ell and (h // u) * w <= p1 * ell:
                split_count += 1
        total += mu_squarefree(h) * split_count
    return total


def untruncated_lcm_mobius_sum(ell: int) -> int:
    return sum(
        mu_squarefree(d1) * mu_squarefree(d2)
        for d1, d2 in lcm_pairs(ell)
    )


def unrestricted_packet_representation_count(q: int) -> int:
    count = 0
    x = q
    radical = 1
    divisor = 3
    while divisor * divisor <= x:
        if x % divisor == 0:
            radical *= divisor
            while x % divisor == 0:
                x //= divisor
        divisor += 2
    if x > 1:
        radical *= x

    for ell in squarefree_divisors(radical):
        if q % ell != 0:
            continue
        t = q // ell
        if t % 2 == 0:
            continue
        for d1, d2 in lcm_pairs(ell):
            if t < gcd(d1, d2):
                count += 1
    return count


def verify() -> None:
    low_prime_sets = (
        (3, 5),
        (3, 5, 7),
        (3, 5, 7, 11),
    )

    for low_primes in low_prime_sets:
        ell_values = [1]
        for prime in low_primes:
            ell_values += [value * prime for value in tuple(ell_values)]
        ell_values = sorted(set(ell_values))
        lifted_primes = tuple(
            prime
            for prime in range(max(low_primes) + 1, 90)
            if is_prime(prime)
        )

        for ell in ell_values:
            assert len(lcm_pairs(ell)) == 3 ** omega(ell)
            assert untruncated_lcm_mobius_sum(ell) == mu_squarefree(ell)

        for p1, p2 in combinations(lifted_primes, 2):
            for ell in ell_values:
                if ell == 1:
                    continue
                t_samples = set(range(1, min(ell, 81), 2))
                if ell > 81:
                    t_samples.update(
                        candidate
                        for candidate in (
                            ell // 5,
                            ell // 3,
                            ell // 2,
                            (2 * ell) // 3,
                        )
                        if 1 <= candidate < ell and candidate % 2 == 1
                    )

                for t in sorted(t_samples):
                    n = p1 * p2 * ell * t
                    k = isqrt(n)
                    if k * k == n:
                        continue

                    direct, accepted = direct_superroot_mobius_coefficient(
                        k, p1, p2, ell, t
                    )
                    rectangular = rectangular_mobius_coefficient(
                        k, p1, p2, ell
                    )
                    divisor_window = divisor_window_mobius_coefficient(
                        k, p1, p2, ell
                    )
                    assert direct == rectangular == divisor_window

                    if accepted:
                        assert t <= k // min(p1, p2)
                        overlap_g = tuple(
                            g
                            for g in squarefree_divisors(ell)
                            if t < g
                            and g * n < t * (k + 1) * (k + 1)
                        )
                        assert len(overlap_g) <= 1

                        p_packet = p1 * p2
                        q_packet = ell * t
                        assert n == p_packet * q_packet
                        assert min(p_packet, q_packet) <= k
                        assert max(p_packet, q_packet) > k
                        low = min(p_packet, q_packet)
                        high = max(p_packet, q_packet)
                        assert k * k // low + 1 <= high
                        assert high <= (k * k + 2 * k) // low
                        if p_packet <= k:
                            assert q_packet > k
                            for d1, d2 in accepted:
                                assert d1 * d2 > k

    # R12 packet multiplicity envelope.
    for q in range(1, 2000, 2):
        count = unrestricted_packet_representation_count(q)
        distinct_prime_divisors = tuple(
            prime
            for prime in range(3, q + 1, 2)
            if is_prime(prime) and q % prime == 0
        )
        assert count <= 4 ** len(distinct_prime_divisors)


if __name__ == "__main__":
    verify()
    print("P017 P2 collision packet compression verifier: PASS")
