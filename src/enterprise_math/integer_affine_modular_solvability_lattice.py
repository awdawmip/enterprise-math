"""Divisibility-lattice structure of modular affine solvability.

For fixed integer affine equation

    A x = b,

let S contain positive moduli M for which

    A x == b (mod M)

is solvable.  In cokernel language this is

    [b] in M coker(A).

For any finitely generated abelian group G,

    M G intersection N G = lcm(M,N) G.

Therefore S has two exact lattice properties:

* downward: N in S and M|N imply M in S;
* join-closed: M,N in S imply lcm(M,N) in S.

Equivalently there is one supernatural modulus

    Q = product_p p^e_p,     e_p in N_0 union {infinity},

such that S is exactly the set of finite positive divisors of Q.  Here e_p is
the largest prime-power exponent for which the equation remains solvable modulo
p^e, possibly infinity.

This differs from the modular indistinguishability region of two fixed linear
maps, which is a finite principal divisor down-set ``divisors(g)`` unless the
maps are exactly equal.

For one scalar equation ``a x=b`` the prime threshold is explicit.  Write
``alpha=v_p(a)`` and ``beta=v_p(b)`` with the zero coefficient handled
separately.  If ``beta >= alpha`` (including alpha=0), all p-power levels are
solvable.  Otherwise the maximal solvable exponent is beta.  Thus ``2x=1`` is
solvable modulo every odd prime power and no positive power of two: its region is
all odd moduli, not the divisors of one finite integer.

These are standard congruence / finitely-generated abelian group facts.  The
project value is the IMAGE-layer precision geometry and its contrast with model
equality precision.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import lcm
from typing import Sequence

from .integer_affine_fiber_diagnostic import modularly_reachable
from .integer_future_padic_precision import p_adic_valuation


INFINITE = "INFINITE"


def _modulus(value: int, *, name: str = "modulus") -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f"{name} must be an integer")
    if value <= 0:
        raise ValueError(f"{name} must be positive")
    return value


def affine_solvability_is_downward(
    matrix: Sequence[Sequence[int]],
    target: Sequence[int],
    finer_modulus: int,
    coarser_modulus: int,
) -> bool:
    finer = _modulus(finer_modulus, name="finer_modulus")
    coarser = _modulus(coarser_modulus, name="coarser_modulus")
    if finer % coarser != 0:
        raise ValueError("coarser_modulus must divide finer_modulus")
    if modularly_reachable(matrix, target, finer) and not modularly_reachable(
        matrix,
        target,
        coarser,
    ):
        raise AssertionError("modular affine solvability failed downward closure")
    return True


def affine_solvability_is_lcm_closed(
    matrix: Sequence[Sequence[int]],
    target: Sequence[int],
    left_modulus: int,
    right_modulus: int,
) -> bool:
    left = _modulus(left_modulus, name="left_modulus")
    right = _modulus(right_modulus, name="right_modulus")
    if modularly_reachable(matrix, target, left) and modularly_reachable(
        matrix,
        target,
        right,
    ):
        joined = lcm(left, right)
        if not modularly_reachable(matrix, target, joined):
            raise AssertionError("modular affine solvability failed lcm closure")
    return True


def scalar_prime_power_solvability_threshold(
    coefficient: int,
    target: int,
    prime: int,
) -> int | str:
    """Largest e with ``a x=b mod p^e`` solvable, or INFINITE."""
    for name, value in (("coefficient", coefficient), ("target", target)):
        if isinstance(value, bool) or not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
    # Validate prime through p-adic utility.
    p_adic_valuation(1, prime)
    if coefficient == 0:
        if target == 0:
            return INFINITE
        return p_adic_valuation(target, prime)
    if target == 0:
        return INFINITE
    alpha = p_adic_valuation(coefficient, prime)
    beta = p_adic_valuation(target, prime)
    return INFINITE if beta >= alpha else beta


def scalar_modulus_solvable_from_prime_thresholds(
    coefficient: int,
    target: int,
    modulus: int,
) -> bool:
    M = _modulus(modulus)
    remaining = M
    prime = 2
    while prime * prime <= remaining:
        if remaining % prime == 0:
            exponent = 0
            while remaining % prime == 0:
                remaining //= prime
                exponent += 1
            threshold = scalar_prime_power_solvability_threshold(
                coefficient,
                target,
                prime,
            )
            if threshold != INFINITE and exponent > threshold:
                return False
        prime = 3 if prime == 2 else prime + 2
    if remaining > 1:
        threshold = scalar_prime_power_solvability_threshold(
            coefficient,
            target,
            remaining,
        )
        if threshold != INFINITE and 1 > threshold:
            return False
    return True


@dataclass(frozen=True)
class BoundedSolvabilityLatticeReport:
    maximum_modulus: int
    solvable_moduli: tuple[int, ...]
    downward_closed: bool
    lcm_closed_within_bound: bool


def bounded_affine_solvability_lattice_report(
    matrix: Sequence[Sequence[int]],
    target: Sequence[int],
    maximum_modulus: int,
) -> BoundedSolvabilityLatticeReport:
    maximum = _modulus(maximum_modulus, name="maximum_modulus")
    solvable = tuple(
        modulus
        for modulus in range(1, maximum + 1)
        if modularly_reachable(matrix, target, modulus)
    )
    solvable_set = set(solvable)
    downward = all(
        divisor in solvable_set
        for modulus in solvable
        for divisor in range(1, modulus + 1)
        if modulus % divisor == 0
    )
    lcm_closed = all(
        lcm(left, right) > maximum
        or lcm(left, right) in solvable_set
        for left in solvable
        for right in solvable
    )
    if not downward or not lcm_closed:
        raise AssertionError("bounded modular solvability failed lattice ideal laws")
    return BoundedSolvabilityLatticeReport(
        maximum_modulus=maximum,
        solvable_moduli=solvable,
        downward_closed=downward,
        lcm_closed_within_bound=lcm_closed,
    )
