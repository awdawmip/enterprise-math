"""Exact projective formula on the prime-square unit shell ``1+p^2=c``.

For odd prime p, c=p^2+1 is exactly twice an odd integer, so v_2(c)=1.  The
2-coordinate alone gives

    C(c) >= rad(c)/2.

Since C(p^2)=2, the two unit projective cross-ratios are

    m(c)/2 = c/(2 rad(c)),
    p/C(c) <= 2p/rad(c).

For p>=5, c=p^2+1>=4p, hence the first ratio dominates exactly:

    sigma_proj = c/(2 rad(c)) = m(c)/2.

Every odd prime divisor q of p^2+1 satisfies q=1 mod 4 because -1 is a
quadratic residue modulo q.  Thus the strongest current low-capacity unit
branch reduces to the powerfulness/radical of p^2+1.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction

from .abc_projective_capacity_condition import projective_capacity_condition_state
from .abc_small_derivative_block import normalized_block_capacity
from .abc_support import multiplicity_residual, prime_factorization, radical


@dataclass(frozen=True)
class PrimeSquareUnitShell:
    prime: int
    square: int
    successor: int
    successor_radical: int
    successor_residual: int
    successor_capacity: int
    sigma_projective: Fraction


def _is_prime(n: int) -> bool:
    return n > 1 and prime_factorization(n) == ((n, 1),)


def prime_square_unit_shell(prime: int) -> PrimeSquareUnitShell:
    """Return the exact projective state for ``1+p^2=p^2+1``, p prime >=5."""
    if isinstance(prime, bool) or not isinstance(prime, int) or prime < 5 or not _is_prime(prime):
        raise ValueError("prime must be a prime integer >=5")
    b = prime * prime
    c = b + 1
    if c % 2 or c % 4 == 0:
        raise AssertionError("odd prime square plus one must have exact 2-adic valuation one")
    if normalized_block_capacity(b) != 2:
        raise AssertionError("prime-square block must have capacity two")
    factors = prime_factorization(c)
    for q, _exponent in factors:
        if q == 2:
            continue
        if q % 4 != 1:
            raise AssertionError("odd divisor of p^2+1 must be 1 mod 4")
    R = radical(c)
    m = multiplicity_residual(c)
    C = normalized_block_capacity(c)
    if C < R // 2:
        raise AssertionError("2-coordinate capacity lower bound failed")
    expected = Fraction(c, 2 * R)
    state = projective_capacity_condition_state(1, b, c)
    if state.sigma_projective != expected:
        raise AssertionError("prime-square projective shell formula failed")
    return PrimeSquareUnitShell(
        prime=prime,
        square=b,
        successor=c,
        successor_radical=R,
        successor_residual=m,
        successor_capacity=C,
        sigma_projective=expected,
    )


def prime_square_pcc_failure(
    prime: int, numerator: int, denominator: int
) -> bool:
    """Decide ``sigma_proj >= c^(p/q)`` on the prime-square shell exactly."""
    if not 0 < numerator < denominator:
        raise ValueError("require 0<numerator<denominator")
    state = prime_square_unit_shell(prime)
    sigma = state.sigma_projective
    return sigma.numerator**denominator >= sigma.denominator**denominator * state.successor**numerator
