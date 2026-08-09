"""Unified prime-square unit shells and Pell +/-1 failure reduction.

There are two unit orientations with a prime-square low-capacity block:

    1 + p^2     = p^2+1,   giving p^2 - k s^2 = -1,
    1 + (p^2-1) = p^2,     giving p^2 - k s^2 = +1.

For odd prime p>=5, the plus shell has

    sigma_proj = m(p^2+1)/2.

For odd prime p>=3, the predecessor shell also has

    sigma_proj = m(p^2-1)/2.

For the predecessor orientation, C(p^2)=2 and

    m(n) C(n) = sum_{q|n} n v_q(n)/q.

Since v_2(p^2-1)>=3, this product is at least 3(p^2-1)/2 >= 2p,
so the competing ratio p/C(p^2-1) is no larger than m(p^2-1)/2.

PCC failure on either shell forces a large square divisor and therefore a Pell
+/-1 equation with a small coefficient k.  The same O(X^(1-eta) log X) union
count applies to both signs.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction

from .abc_prime_square_pell_sparse import (
    pell_coefficient_upper_bound,
    uniform_negative_pell_solution_count_bound,
)
from .abc_prime_square_unit_shell import prime_square_unit_shell
from .abc_projective_capacity_condition import projective_capacity_condition_state
from .abc_projective_sparse_failure import largest_square_divisor_root
from .abc_small_derivative_block import normalized_block_capacity
from .abc_support import multiplicity_residual, prime_factorization


@dataclass(frozen=True)
class PrimeSquarePellShell:
    prime: int
    sign: int
    neighboring_value: int
    neighboring_residual: int
    neighboring_capacity: int
    sigma_projective: Fraction


@dataclass(frozen=True)
class PrimeSquarePellReduction:
    prime: int
    sign: int
    neighboring_value: int
    square_divisor_root: int
    pell_coefficient: int
    pell_identity: int


def _is_prime(n: int) -> bool:
    return n > 1 and prime_factorization(n) == ((n, 1),)


def predecessor_prime_square_shell(prime: int) -> PrimeSquarePellShell:
    """Return exact PCC state for ``1+(p^2-1)=p^2``."""
    if isinstance(prime, bool) or not isinstance(prime, int) or prime < 3 or not _is_prime(prime):
        raise ValueError("prime must be an odd prime >=3")
    b = prime * prime - 1
    c = prime * prime
    if normalized_block_capacity(c) != 2:
        raise AssertionError("prime-square block must have derivative capacity two")
    if b % 8:
        raise AssertionError("odd prime square minus one must be divisible by eight")
    m_b = multiplicity_residual(b)
    C_b = normalized_block_capacity(b)
    if m_b * C_b < 2 * prime:
        raise AssertionError("2-adic derivative term failed predecessor dominance")
    expected = Fraction(m_b, 2)
    actual = projective_capacity_condition_state(1, b, c).sigma_projective
    if actual != expected:
        raise AssertionError("predecessor prime-square projective formula failed")
    return PrimeSquarePellShell(
        prime=prime,
        sign=1,
        neighboring_value=b,
        neighboring_residual=m_b,
        neighboring_capacity=C_b,
        sigma_projective=expected,
    )


def successor_prime_square_shell(prime: int) -> PrimeSquarePellShell:
    """Return the plus-one shell in the unified representation."""
    data = prime_square_unit_shell(prime)
    return PrimeSquarePellShell(
        prime=prime,
        sign=-1,
        neighboring_value=data.successor,
        neighboring_residual=data.successor_residual,
        neighboring_capacity=data.successor_capacity,
        sigma_projective=data.sigma_projective,
    )


def prime_square_shell_failure_pell_reduction(
    prime: int,
    sign: int,
    numerator: int,
    denominator: int,
) -> PrimeSquarePellReduction | None:
    """Return the Pell +/-1 reduction when PCC_eta fails on one shell.

    ``sign=+1`` selects ``p^2-1`` and returns ``p^2-k s^2=+1``.
    ``sign=-1`` selects ``p^2+1`` and returns ``p^2-k s^2=-1``.
    """
    if sign not in (-1, 1):
        raise ValueError("sign must be -1 or +1")
    if not 0 < numerator < denominator:
        raise ValueError("require 0<numerator<denominator")
    shell = (
        predecessor_prime_square_shell(prime)
        if sign == 1
        else successor_prime_square_shell(prime)
    )
    sigma = shell.sigma_projective
    c_height = prime * prime if sign == 1 else prime * prime + 1
    if sigma.numerator**denominator < sigma.denominator**denominator * c_height**numerator:
        return None
    s = largest_square_divisor_root(shell.neighboring_value)
    if shell.neighboring_value % (s * s):
        raise AssertionError("square divisor root failed exact divisibility")
    k = shell.neighboring_value // (s * s)
    identity = prime * prime - k * s * s
    if identity != sign:
        raise AssertionError("unified prime-square shell failed Pell sign identity")
    return PrimeSquarePellReduction(
        prime=prime,
        sign=sign,
        neighboring_value=shell.neighboring_value,
        square_divisor_root=s,
        pell_coefficient=k,
        pell_identity=identity,
    )


def both_prime_square_shells_failure_count_bound(
    X: int, numerator: int, denominator: int
) -> int:
    """Return a simple union bound for both Pell signs through height X."""
    k_bound = pell_coefficient_upper_bound(X, numerator, denominator)
    per_k = uniform_negative_pell_solution_count_bound(X)
    # Two Pell signs; primality restriction can only reduce the count.
    from math import isqrt
    return min(isqrt(X), 2 * k_bound * per_k)
