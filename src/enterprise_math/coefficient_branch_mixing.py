"""Coefficient collapse can erase branch identity through zero divisors.

The intersective ghost polynomial factors as

    F=(x^2-13)(x^2-17)(x^2-221).

Over Z, an integral domain, ``F(x)=0`` is equivalent to one labelled factor being
zero.  After modular collapse this logical reading need not survive.

Two different mechanisms occur.

### Inside one composite modulus

``Z/nZ`` is an integral domain exactly when n is prime.  At composite n, zero
divisors allow a product to vanish without any factor vanishing.  For the ghost
polynomial, x=1 modulo15 is sharp:

    x^2-13 = -12   is zero mod3 but not mod5,
    x^2-221 = -220 is zero mod5 but not mod3,

so the product is zero mod15 although none of the three labelled factors is zero
mod15.

### Across precision components

Even prime moduli are fields and preserve product-zero branch semantics locally,
but the branch selected can depend on p.  The profinite completion

    Z_hat ~= product_p Z_p

therefore permits different factors to vanish in different p-components.  The
product vanishes globally in Z_hat even when no one factor is globally zero.

This is a precision analogue of A4 witness erasure: an unlabeled support/OR can be
locally realizable while no single witness label survives globally.

The result does not say polynomial equations should be interpreted as relations
by default.  It is a diagnostic boundary: if an exact world law uses the
integral-domain equivalence ``product zero <=> one labelled branch zero``, then a
coefficient quotient with zero divisors is not semantics-preserving for that
branch interpretation unless the label is retained separately.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import isqrt

from .nonlinear_profinite_ghost import (
    CONSTANTS,
    chosen_square_factor_for_prime,
    intersective_polynomial,
)


def _modulus(value: int) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError("modulus must be an integer")
    if value <= 0:
        raise ValueError("modulus must be positive")
    return value


def _prime(value: int) -> bool:
    if value < 2:
        return False
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            return False
        divisor += 1
    return True


def factor_values(value: int) -> tuple[int, ...]:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError("value must be an integer")
    square = value * value
    return tuple(square - constant for constant in CONSTANTS)


def labelled_factor_zero_modulus(value: int, constant: int, modulus: int) -> bool:
    M = _modulus(modulus)
    if constant not in CONSTANTS:
        raise ValueError("constant must be one of the declared factor labels")
    return (value * value - constant) % M == 0


def product_zero_modulus(value: int, modulus: int) -> bool:
    M = _modulus(modulus)
    return intersective_polynomial(value) % M == 0


def product_zero_without_labelled_branch(value: int, modulus: int) -> bool:
    M = _modulus(modulus)
    return (
        product_zero_modulus(value, M)
        and not any(
            labelled_factor_zero_modulus(value, constant, M)
            for constant in CONSTANTS
        )
    )


def labelled_branch_has_root_modulus(constant: int, modulus: int) -> bool:
    M = _modulus(modulus)
    if constant not in CONSTANTS:
        raise ValueError("constant must be one of the declared factor labels")
    return any(
        labelled_factor_zero_modulus(value, constant, M)
        for value in range(M)
    )


def modular_ring_is_integral_domain(modulus: int) -> bool:
    """For the nonzero ring Z/nZ, integral-domain iff n is prime."""
    M = _modulus(modulus)
    return _prime(M)


def composite_zero_divisor_witness(modulus: int) -> tuple[int, int] | None:
    """Return nonzero residues a,b with a*b=0 mod n, or None for prime n.

    Modulus1 is the zero ring and is outside the intended branch-semantics
    comparison; it returns ``(0,0)`` only as the trivial precision boundary.
    """
    M = _modulus(modulus)
    if M == 1:
        return (0, 0)
    if _prime(M):
        return None
    divisor = next(
        candidate
        for candidate in range(2, isqrt(M) + 1)
        if M % candidate == 0
    )
    left = divisor % M
    right = (M // divisor) % M
    if left == 0 or right == 0 or (left * right) % M != 0:
        raise AssertionError("composite zero-divisor constructor failed")
    return left, right


@dataclass(frozen=True)
class Mod15BranchMixingWitness:
    residue: int
    modulus: int
    factor_values: tuple[int, ...]
    factor_zero_mod3: tuple[bool, ...]
    factor_zero_mod5: tuple[bool, ...]
    factor_zero_mod15: tuple[bool, ...]
    product_zero_mod15: bool

    @property
    def no_global_mod15_branch(self) -> bool:
        return self.product_zero_mod15 and not any(self.factor_zero_mod15)


def mod15_branch_mixing_witness() -> Mod15BranchMixingWitness:
    residue = 1
    values = factor_values(residue)
    report = Mod15BranchMixingWitness(
        residue=residue,
        modulus=15,
        factor_values=values,
        factor_zero_mod3=tuple(value % 3 == 0 for value in values),
        factor_zero_mod5=tuple(value % 5 == 0 for value in values),
        factor_zero_mod15=tuple(value % 15 == 0 for value in values),
        product_zero_mod15=intersective_polynomial(residue) % 15 == 0,
    )
    if not report.no_global_mod15_branch:
        raise AssertionError("reference mod15 branch-mixing witness failed")
    return report


def branch_blocker_moduli() -> tuple[tuple[int, int], ...]:
    """One finite modulus blocking each labelled square branch entirely."""
    blockers = (
        (13, 5),
        (17, 3),
        (221, 3),
    )
    for constant, modulus in blockers:
        if labelled_branch_has_root_modulus(constant, modulus):
            raise AssertionError("declared branch blocker unexpectedly has a root")
    return blockers


def no_single_label_is_locally_solvable_everywhere() -> bool:
    """Each exact branch is blocked at some finite precision."""
    blockers = dict(branch_blocker_moduli())
    return all(
        not labelled_branch_has_root_modulus(constant, blockers[constant])
        for constant in CONSTANTS
    )


def local_branch_choice(prime: int) -> int:
    """One factor label selected by the parent p-adic ghost construction."""
    return chosen_square_factor_for_prime(prime)
