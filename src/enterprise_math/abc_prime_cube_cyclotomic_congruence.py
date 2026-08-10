"""Root-of-unity congruence signature of repeated prime-cube cyclotomic factors.

For r != 3 dividing Phi_3(p,q), the ratio x=p*q^{-1} modulo r^e has exact
order three whenever r^e divides the factor.  For Phi_6 it has exact order six.
The two polynomial roots modulo every r^e are x and x^{-1}; Hensel uniqueness
follows from the nonzero discriminant -3 modulo r.

Consequently k distinct repeated cyclotomic primes restrict the labelled prime
ratio to exactly 2^k CRT root choices modulo the product of their full prime-
power divisors.  The module records this exact finite congruence state; it does
not claim root-of-unity/Hensel/CRT mathematics as new.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import prod

from .abc_prime_cube_cyclotomic_support import prime_cube_cyclotomic_support


@dataclass(frozen=True)
class CyclotomicPrimeConstraint:
    prime: int
    exponent: int
    modulus: int
    order: int
    observed_ratio: int
    inverse_ratio: int
    canonical_root_pair: tuple[int, int]


@dataclass(frozen=True)
class CyclotomicCongruenceSignature:
    left_prime: int
    right_prime: int
    mode: str
    constraints: tuple[CyclotomicPrimeConstraint, ...]
    repeated_modulus: int
    root_choice_count: int


def _constraint(q: int, p: int, r: int, exponent: int, order: int) -> CyclotomicPrimeConstraint:
    modulus = r**exponent
    inverse_q = pow(q, -1, modulus)
    x = (p * inverse_q) % modulus
    if pow(x, order, modulus) != 1:
        raise AssertionError("cyclotomic ratio lost declared root-of-unity order")
    proper = (1, 2, 3) if order == 6 else (1,)
    if any(pow(x, d, modulus) == 1 for d in proper):
        raise AssertionError("cyclotomic ratio order collapsed modulo prime power")
    inv = pow(x, -1, modulus)
    roots = tuple(sorted((x, inv)))
    if x not in roots:
        raise AssertionError("observed ratio escaped root pair")
    return CyclotomicPrimeConstraint(
        prime=r,
        exponent=exponent,
        modulus=modulus,
        order=order,
        observed_ratio=x,
        inverse_ratio=inv,
        canonical_root_pair=(roots[0], roots[1]),
    )


def prime_cube_cyclotomic_congruence_signature(
    q: int, p: int, mode: str
) -> CyclotomicCongruenceSignature:
    """Return full repeated-prime congruence data for Phi_3 or Phi_6.

    ``mode='sum'`` uses Phi_6=p^2-pq+q^2 and order six.
    ``mode='difference'`` uses Phi_3=p^2+pq+q^2 and order three.
    Only exponent>=2 primes are retained; prime 3 never occurs here by Stage76.
    """
    support = prime_cube_cyclotomic_support(q, p)
    if mode == "sum":
        factorization = support.phi6_factorization
        order = 6
    elif mode == "difference":
        factorization = support.phi3_factorization
        order = 3
    else:
        raise ValueError("mode must be 'sum' or 'difference'")

    repeated = tuple((r, e) for r, e in factorization if e >= 2)
    constraints = tuple(_constraint(q, p, r, e, order) for r, e in repeated)
    repeated_modulus = prod((item.modulus for item in constraints), start=1)
    choice_count = 1 << len(constraints)

    # Every chosen local root pair is independent under CRT because the prime-
    # power moduli are pairwise coprime.
    if any(item.prime % 6 != 1 for item in constraints):
        raise AssertionError("repeated congruence support escaped 1 mod 6")
    return CyclotomicCongruenceSignature(
        left_prime=q,
        right_prime=p,
        mode=mode,
        constraints=constraints,
        repeated_modulus=repeated_modulus,
        root_choice_count=choice_count,
    )


def ratio_space_compression_factor(signature: CyclotomicCongruenceSignature) -> tuple[int, int]:
    """Return ``(modulus,allowed_root_choices)`` for the repeated congruence state."""
    return signature.repeated_modulus, signature.root_choice_count
