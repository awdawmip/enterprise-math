"""Centered-coordinate formulas for cutoff-five (3,3) prime-cube atoms.

For distinct odd primes p>q write

    B=(p+q)/2,  A=(p-q)/2.

Then

    p^3+q^3 = 2B (B^2+3A^2),
    p^3-q^3 = 2A (3B^2+A^2).

The quadratic factors are odd.  Their gcd with B or A is only the possible
prime 3.  Tracking whether the leading centered coordinate already contains
the factor 2 yields exact projective formulas for both the sum and difference
(3,3) atom shells.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import gcd

from .abc_projective_capacity_condition import projective_capacity_condition_state
from .abc_support import multiplicity_residual, prime_factorization, radical


@dataclass(frozen=True)
class PrimeCubeCenteredState:
    left_prime: int
    right_prime: int
    center: int
    radius: int
    mode: str
    abc: tuple[int, int, int]
    quadratic_factor: int
    overlap_three: int
    parity_multiplier: int
    projective_atom_value: Fraction
    cheap_squarefree_guard: bool


def _require_odd_prime(name: str, n: int) -> None:
    if isinstance(n, bool) or not isinstance(n, int) or n < 3:
        raise ValueError(f"{name} must be an odd prime")
    if prime_factorization(n) != ((n, 1),):
        raise ValueError(f"{name} must be prime")


def _center_radius(q: int, p: int) -> tuple[int, int]:
    _require_odd_prime("q", q)
    _require_odd_prime("p", p)
    if p <= q:
        raise ValueError("require p>q")
    B=(p+q)//2
    A=(p-q)//2
    if gcd(A,B) != 1 or A % 2 == B % 2:
        raise AssertionError("odd-prime centered coordinates lost coprime opposite parity")
    return B,A


def prime_cube_sum_centered_state(q: int, p: int) -> PrimeCubeCenteredState:
    """Return exact c-oriented formula for ``q^3+p^3``."""
    B,A = _center_radius(q,p)
    E = B*B + 3*A*A
    if E % 2 == 0:
        raise AssertionError("centered cube-sum quadratic factor must be odd")
    g = gcd(B,E)
    if g != gcd(B,3) or g not in (1,3):
        raise AssertionError("cube-sum overlap must be exactly gcd(B,3)")
    epsilon = 2 if B % 2 == 0 else 1
    N = p**3 + q**3
    if N != 2*B*E:
        raise AssertionError("centered cube-sum factorization failed")
    triple=(q**3,p**3,N)
    exact=projective_capacity_condition_state(*triple).cyclic_weighted_defects[0]
    closed=Fraction(epsilon*g*multiplicity_residual(E), 6*radical(B))
    if exact != closed:
        raise AssertionError("centered cube-sum projective formula failed")
    guard = radical(E) == E
    if guard and exact >= 1:
        raise AssertionError("squarefree cube-sum quadratic factor unexpectedly activated")
    return PrimeCubeCenteredState(
        left_prime=q,
        right_prime=p,
        center=B,
        radius=A,
        mode="sum",
        abc=triple,
        quadratic_factor=E,
        overlap_three=g,
        parity_multiplier=epsilon,
        projective_atom_value=closed,
        cheap_squarefree_guard=guard,
    )


def prime_cube_difference_centered_state(q: int, p: int) -> PrimeCubeCenteredState:
    """Return exact side-oriented formula for ``q^3 + (p^3-q^3) = p^3``."""
    B,A = _center_radius(q,p)
    D = 3*B*B + A*A
    if D % 2 == 0:
        raise AssertionError("centered cube-difference quadratic factor must be odd")
    g = gcd(A,D)
    if g != gcd(A,3) or g not in (1,3):
        raise AssertionError("cube-difference overlap must be exactly gcd(A,3)")
    epsilon = 2 if A % 2 == 0 else 1
    N = p**3 - q**3
    if N != 2*A*D:
        raise AssertionError("centered cube-difference factorization failed")
    triple=(q**3,N,p**3)
    exact=projective_capacity_condition_state(*triple).cyclic_weighted_defects[1]
    closed=Fraction(
        epsilon*g*multiplicity_residual(A)*multiplicity_residual(D),
        6*B,
    )
    if exact != closed:
        raise AssertionError("centered cube-difference projective formula failed")
    guard = radical(A) == A and radical(D) == D
    if guard and exact >= 1:
        raise AssertionError("double-squarefree cube-difference state unexpectedly activated")
    return PrimeCubeCenteredState(
        left_prime=q,
        right_prime=p,
        center=B,
        radius=A,
        mode="difference",
        abc=triple,
        quadratic_factor=D,
        overlap_three=g,
        parity_multiplier=epsilon,
        projective_atom_value=closed,
        cheap_squarefree_guard=guard,
    )
