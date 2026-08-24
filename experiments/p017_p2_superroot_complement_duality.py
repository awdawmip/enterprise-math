"""Finite verifier for P017 P2 super-root complement duality.

Research-owner artifact only.  It checks the exact identities in
docs/P017_P2_SUPERROOT_COMPLEMENT_DUALITY_20260824.md.  The finite replay is
not an asymptotic sieve theorem and makes no all-K P2 claim.
"""

from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from itertools import combinations
from math import gcd


def hit_count(k: int, m: int) -> int:
    assert k >= 1 and m >= 1
    return (k * k + 2 * k) // m - (k * k) // m


def odd_quotient_count(k: int, m: int) -> int:
    return hit_count(k, m) - hit_count(k, 2 * m)


def complement_window(k: int, a: int) -> tuple[int, int]:
    assert k >= 1 and 1 <= a <= k
    return (k * k // a + 1, (k * k + 2 * k) // a)


def superroot_complement(k: int, m: int) -> int | None:
    """Return the unique odd quotient a<=k counted by O_m, if it exists."""
    assert k >= 1 and m > k and m % 2 == 1
    lower = k * k // m + 1
    upper = (k * k + 2 * k) // m
    first_odd = lower if lower % 2 == 1 else lower + 1
    if first_odd > upper:
        return None
    if first_odd + 2 <= upper:
        raise AssertionError("a super-root odd modulus acquired two odd quotients")
    if first_odd > k:
        raise AssertionError("super-root quotient exceeded the root")
    return first_odd


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


def squarefree_products(primes: tuple[int, ...], ceiling: int) -> tuple[int, ...]:
    values = [1]
    for prime in primes:
        values += [value * prime for value in tuple(values) if value * prime <= ceiling]
    return tuple(sorted(set(value for value in values if value <= ceiling)))


def deterministic_coeff(k: int, m: int) -> int:
    return ((17 * m + 13 * k) % 11) - 5


def verify(limit_k: int = 160) -> None:
    # R06-R08 and R10: complement duality, separation, cutoff defect,
    # mass reciprocity, and weighted reindexing.
    for k in range(2, limit_k + 1):
        upper_state = k * k + 2 * k
        odd_complements = tuple(a for a in range(1, k + 1) if a % 2 == 1)
        odd_superroot_moduli = tuple(
            m for m in range(k + 1, upper_state + 1) if m % 2 == 1
        )

        for m in odd_superroot_moduli:
            complement = superroot_complement(k, m)
            incidence = odd_quotient_count(k, m)
            assert incidence in (0, 1)
            assert incidence == int(complement is not None)
            if complement is not None:
                lo, hi = complement_window(k, complement)
                assert lo <= m <= hi
                assert k * k < complement * m <= upper_state

        windows = tuple((a, *complement_window(k, a)) for a in odd_complements)
        for (a, lo_a, hi_a), (b, lo_b, hi_b) in combinations(windows, 2):
            assert a < b
            assert hi_b < lo_a

        superroot_mass = sum(
            odd_quotient_count(k, m) for m in odd_superroot_moduli
        )
        subroot_mass = sum(odd_quotient_count(k, a) for a in odd_complements)
        assert superroot_mass == subroot_mass

        cutoff_samples = set(range(k + 1, min(upper_state, k + 60) + 1))
        cutoff_samples.update(
            {
                min(upper_state, max(k + 1, int(k**1.02))),
                min(upper_state, max(k + 1, int(k**1.05))),
                min(upper_state, max(k + 1, int(k**1.10))),
                upper_state,
            }
        )
        for cutoff in sorted(cutoff_samples):
            full_labels: list[int] = []
            straddling_labels: list[int] = []
            for a, lo, hi in windows:
                assert (lo <= cutoff) == (a > Fraction(k * k, cutoff))
                assert (hi <= cutoff) == (
                    a > Fraction(upper_state, cutoff + 1)
                )
                if lo > cutoff:
                    continue
                if hi <= cutoff:
                    full_labels.append(a)
                else:
                    straddling_labels.append(a)
            assert len(straddling_labels) <= 1

            left_mass = sum(
                odd_quotient_count(k, m)
                for m in range(k + 1, cutoff + 1)
                if m % 2 == 1
            )
            full_mass = sum(odd_quotient_count(k, a) for a in full_labels)
            boundary_mass = 0
            if straddling_labels:
                a = straddling_labels[0]
                lo, _ = complement_window(k, a)
                boundary_mass = sum(
                    1 for m in range(lo, cutoff + 1) if m % 2 == 1
                )
            assert left_mass == full_mass + boundary_mass

        coefficient_cutoff = min(upper_state, max(k + 1, int(k**1.20) + 5))
        coefficients = {
            m: deterministic_coeff(k, m)
            for m in range(k + 1, coefficient_cutoff + 1)
            if m % 2 == 1
        }
        direct = sum(
            Fraction(coefficient)
            * (Fraction(odd_quotient_count(k, m)) - Fraction(k, m))
            for m, coefficient in coefficients.items()
        )
        window_incidence = sum(
            coefficient
            for _a, lo, hi in windows
            for m, coefficient in coefficients.items()
            if lo <= m <= hi
        )
        reindexed = Fraction(window_incidence) - sum(
            Fraction(k * coefficient, m)
            for m, coefficient in coefficients.items()
        )
        assert direct == reindexed

    # R09: exact distinct-prime factor-exchange collision kernel.
    for k in range(10, min(limit_k, 120) + 1):
        upper_state = k * k + 2 * k
        for z in (5, 7, 11, 13):
            low_primes = tuple(prime for prime in range(3, z) if is_prime(prime))
            lifted_primes = tuple(
                prime for prime in range(z + 1, k + 1) if is_prime(prime)
            )
            small_cores = squarefree_products(low_primes, upper_state)
            states: dict[int, list[tuple[int, int, int, int]]] = defaultdict(list)

            for prime in lifted_primes:
                for core in small_cores:
                    modulus = prime * core
                    if modulus <= k or modulus > upper_state:
                        continue
                    complement = superroot_complement(k, modulus)
                    if complement is None:
                        continue
                    state = modulus * complement
                    states[state].append((prime, core, modulus, complement))

            for state, representations in states.items():
                for left, right in combinations(representations, 2):
                    p1, d1, m1, a1 = left
                    p2, d2, m2, a2 = right
                    if p1 == p2:
                        continue

                    common = gcd(d1, d2)
                    assert common > 1
                    u1 = d1 // common
                    u2 = d2 // common
                    assert gcd(u1, u2) == 1
                    assert a1 % (p2 * u2) == 0
                    assert a2 % (p1 * u1) == 0
                    t1 = a1 // (p2 * u2)
                    t2 = a2 // (p1 * u1)
                    assert t1 == t2
                    t = t1
                    assert t % 2 == 1
                    assert 1 <= t < common

                    collision_scale = p1 * p2 * (d1 * d2 // common)
                    assert state == collision_scale * t
                    assert state * common == m1 * m2 * t
                    assert collision_scale * collision_scale > p1 * p2 * k * k
                    assert 2 * k < collision_scale

                    kernel_terms = tuple(
                        candidate
                        for candidate in range(1, common, 2)
                        if k * k < collision_scale * candidate <= upper_state
                    )
                    assert kernel_terms == (t,)


if __name__ == "__main__":
    verify()
    print("P017 P2 super-root complement duality verifier: PASS")
