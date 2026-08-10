"""Cyclotomic prime-support rigidity for centered (3,3) prime-cube atoms.

For distinct odd primes p>q define the homogeneous quadratic factors

    E = p^2 - p*q + q^2 = Phi_6(p,q),
    D = p^2 + p*q + q^2 = Phi_3(p,q).

They are coprime.  Every prime divisor other than 3 is congruent to 1 modulo 6,
and the prime 3 occurs with exponent at most one.  Hence every repeated prime
factor of E or D is 1 mod 6.

The facts are elementary cyclotomic/order arithmetic and are used only as a
P025 precision/support specialization.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import gcd

from .abc_support import prime_factorization


@dataclass(frozen=True)
class PrimeCubeCyclotomicSupport:
    left_prime: int
    right_prime: int
    phi6_factor: int
    phi3_factor: int
    phi6_factorization: tuple[tuple[int, int], ...]
    phi3_factorization: tuple[tuple[int, int], ...]
    phi6_repeated_primes: tuple[int, ...]
    phi3_repeated_primes: tuple[int, ...]
    phi6_has_three: bool
    phi3_has_three: bool


def _require_odd_prime(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 3:
        raise ValueError(f"{name} must be an odd prime")
    if prime_factorization(value) != ((value, 1),):
        raise ValueError(f"{name} must be prime")


def prime_cube_cyclotomic_support(q: int, p: int) -> PrimeCubeCyclotomicSupport:
    """Return exact factor-support data and assert the cyclotomic restrictions."""
    _require_odd_prime("q", q)
    _require_odd_prime("p", p)
    if p <= q:
        raise ValueError("require p>q")

    E = p * p - p * q + q * q
    D = p * p + p * q + q * q
    if gcd(E, D) != 1:
        raise AssertionError("Phi_6/Phi_3 factors for distinct odd primes must be coprime")
    if gcd(E, p * q) != 1 or gcd(D, p * q) != 1:
        raise AssertionError("cyclotomic factors must be coprime to prime bases")

    facE = prime_factorization(E)
    facD = prime_factorization(D)
    for factorization in (facE, facD):
        for r, exponent in factorization:
            if r == 3:
                if exponent > 1:
                    raise AssertionError("prime 3 cannot repeat in the cube cyclotomic factor")
            elif r % 6 != 1:
                raise AssertionError("non-3 cube cyclotomic prime must be 1 mod 6")

    repeatedE = tuple(r for r, exponent in facE if exponent >= 2)
    repeatedD = tuple(r for r, exponent in facD if exponent >= 2)
    if any(r % 6 != 1 for r in repeatedE + repeatedD):
        raise AssertionError("repeated cyclotomic prime escaped 1 mod 6 support")

    return PrimeCubeCyclotomicSupport(
        left_prime=q,
        right_prime=p,
        phi6_factor=E,
        phi3_factor=D,
        phi6_factorization=facE,
        phi3_factorization=facD,
        phi6_repeated_primes=repeatedE,
        phi3_repeated_primes=repeatedD,
        phi6_has_three=any(r == 3 for r, _e in facE),
        phi3_has_three=any(r == 3 for r, _e in facD),
    )


def cube_sum_activation_requires_repeated_one_mod_six(q: int, p: int) -> bool:
    """Verify the Stage-75 sum activation support necessity on one prime pair."""
    from .abc_prime_cube_centered import prime_cube_sum_centered_state

    state = prime_cube_sum_centered_state(q, p)
    support = prime_cube_cyclotomic_support(q, p)
    if state.projective_atom_value >= 1 and not support.phi6_repeated_primes:
        raise AssertionError("activated cube sum lost repeated 1 mod 6 cyclotomic prime")
    return True


def cube_difference_quadratic_multiplicity_support(q: int, p: int) -> tuple[int, ...]:
    """Return repeated primes contributed by the Phi_3 quadratic factor."""
    support = prime_cube_cyclotomic_support(q, p)
    return support.phi3_repeated_primes
