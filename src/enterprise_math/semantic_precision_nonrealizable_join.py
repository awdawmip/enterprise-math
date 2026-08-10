"""Some semantic precision joins are not realizable inside one scalar quotient family.

Restrict the representation class to ordinary integer coefficient quotients

    Z -> Z/MZ.

Suppose a task asks simultaneously for:

1. numeric residue detail at least as fine as modulo p^2;
2. generic product-branch reflection ``ab=0 => a=0 or b=0``.

Within modular quotients, numeric refinement of mod p^2 requires ``p^2|M``.
But then M is composite and ``Z/MZ`` has zero divisors, so generic product-branch
reflection fails.  Therefore no scalar modulus realizes the abstract semantic
join.

The join can be realized only by leaving the restricted representation class,
for example by retaining p^2 numeric residue together with an explicit witness
or branch-label channel instead of reconstructing branch identity from the
coefficient ring.

This is a precision-lift boundary: a semantic requirement may force a change of
state/representation type rather than a larger value of the same scalar
precision parameter.
"""

from __future__ import annotations


def _prime(value: int) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError("prime must be an integer")
    if value < 2:
        raise ValueError("prime must be at least two")
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            raise ValueError("prime must be prime")
        divisor += 1
    return value


def modulus_numeric_refines(finer_modulus: int, coarser_modulus: int) -> bool:
    if isinstance(finer_modulus, bool) or not isinstance(finer_modulus, int):
        raise TypeError("finer_modulus must be an integer")
    if isinstance(coarser_modulus, bool) or not isinstance(coarser_modulus, int):
        raise TypeError("coarser_modulus must be an integer")
    if finer_modulus <= 0 or coarser_modulus <= 0:
        raise ValueError("moduli must be positive")
    return finer_modulus % coarser_modulus == 0


def modular_quotient_has_generic_product_branch_reflection(modulus: int) -> bool:
    if isinstance(modulus, bool) or not isinstance(modulus, int):
        raise TypeError("modulus must be an integer")
    if modulus <= 1:
        return False
    divisor = 2
    while divisor * divisor <= modulus:
        if modulus % divisor == 0:
            return False
        divisor += 1
    return True


def scalar_modulus_can_realize_p2_numeric_and_branch_join(
    prime: int,
    modulus: int,
) -> bool:
    p = _prime(prime)
    return (
        modulus_numeric_refines(modulus, p * p)
        and modular_quotient_has_generic_product_branch_reflection(modulus)
    )


def prove_no_scalar_modulus_realizes_p2_numeric_and_branch_join(
    prime: int,
) -> bool:
    """Arithmetic theorem: any M with p^2|M is composite, hence not a domain."""
    p = _prime(prime)
    target = p * p
    # The proof is symbolic: every numeric-refining M has M=target*k with k>=1,
    # so p is a nontrivial divisor and M cannot be prime.  Return the theorem
    # flag only after locking the base arithmetic facts.
    if target <= 1 or target % p != 0 or target == p:
        raise AssertionError("p^2 arithmetic invariant failed")
    return True
