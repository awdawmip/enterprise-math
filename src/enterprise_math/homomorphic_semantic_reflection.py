"""Quotient homomorphisms preserve polynomial evaluation but not exact reflection.

For the integer quotient ``phi_M:Z->Z/MZ`` and any polynomial term t,

    phi_M(t(x)) = t(phi_M(x)).

Hence exact equation truth always maps forward:

    t(x)=0 over Z  =>  t(x)=0 mod M.

The converse is false for every finite positive M because quotient truth means
only ``t(x) in MZ``.  Even the identity term t(x)=x has false positive x=M.

Logical semantics that require reflection — exact zero, nonzeroness, uniqueness,
branch identity, cancellation, etc. — therefore need an additional theorem.

For a product encoding of disjunction, local reflection is exactly the prime-ideal
criterion already developed in the coefficient branch-mixing line:

    ab=0 mod M  =>  a=0 mod M or b=0 mod M

for all residues iff M is prime (excluding the trivial zero ring M=1 from the
faithful-world comparison).
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence


def _modulus(value: int) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError("modulus must be an integer")
    if value <= 0:
        raise ValueError("modulus must be positive")
    return value


def evaluate_integer_polynomial(coefficients: Sequence[int], value: int) -> int:
    """Evaluate coefficients in ascending degree order exactly over Z."""
    coeffs = tuple(coefficients)
    if not coeffs:
        raise ValueError("polynomial must contain at least one coefficient")
    for coefficient in coeffs:
        if isinstance(coefficient, bool) or not isinstance(coefficient, int):
            raise TypeError("polynomial coefficients must be integers")
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError("value must be an integer")
    result = 0
    for coefficient in reversed(coeffs):
        result = result * value + coefficient
    return result


def polynomial_evaluation_commutes_with_modulus(
    coefficients: Sequence[int],
    value: int,
    modulus: int,
) -> bool:
    M = _modulus(modulus)
    exact = evaluate_integer_polynomial(coefficients, value)
    reduced_coefficients = tuple(coefficient % M for coefficient in coefficients)
    reduced_value = value % M
    reduced_evaluation = evaluate_integer_polynomial(
        reduced_coefficients,
        reduced_value,
    ) % M
    if exact % M != reduced_evaluation:
        raise AssertionError("polynomial evaluation failed quotient homomorphism law")
    return True


def exact_zero_implies_modular_zero(value: int, modulus: int) -> bool:
    M = _modulus(modulus)
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError("value must be an integer")
    if value != 0:
        raise ValueError("forward-soundness witness must be exactly zero")
    return value % M == 0


def modular_zero_false_positive(modulus: int) -> int:
    """Return nonzero integer M whose quotient class is zero modulo M."""
    M = _modulus(modulus)
    value = M
    if value == 0 or value % M != 0:
        raise AssertionError("quotient-reflection false-positive constructor failed")
    return value


def modular_zero_reflects_exactly_on_interval(
    modulus: int,
    absolute_bound: int,
) -> bool:
    """Whether z==0 mod M reflects z=0 for every |z|<=absolute_bound."""
    M = _modulus(modulus)
    if isinstance(absolute_bound, bool) or not isinstance(absolute_bound, int):
        raise TypeError("absolute_bound must be an integer")
    if absolute_bound < 0:
        raise ValueError("absolute_bound must be nonnegative")
    return M > absolute_bound


def product_branch_reflection_for_all_residues(modulus: int) -> bool:
    """Exhaustive finite-ring check of ab=0 => a=0 or b=0."""
    M = _modulus(modulus)
    if M == 1:
        return False
    return all(
        (a * b) % M != 0 or a % M == 0 or b % M == 0
        for a in range(M)
        for b in range(M)
    )


@dataclass(frozen=True)
class HomomorphicSemanticReflectionReport:
    modulus: int
    polynomial_syntax_preserved: bool
    exact_zero_forward_sound: bool
    exact_zero_reflected_on_unbounded_integers: bool
    product_branch_reflection: bool


def homomorphic_semantic_reflection_report(
    modulus: int,
) -> HomomorphicSemanticReflectionReport:
    M = _modulus(modulus)
    # One nontrivial polynomial regression is sufficient as a mechanical surface;
    # the generic term-homomorphism theorem is algebraic, not inferred from it.
    syntax = polynomial_evaluation_commutes_with_modulus((3, -2, 5), 7, M)
    forward = exact_zero_implies_modular_zero(0, M)
    false_positive = modular_zero_false_positive(M)
    return HomomorphicSemanticReflectionReport(
        modulus=M,
        polynomial_syntax_preserved=syntax,
        exact_zero_forward_sound=forward,
        exact_zero_reflected_on_unbounded_integers=(false_positive == 0),
        product_branch_reflection=product_branch_reflection_for_all_residues(M),
    )
