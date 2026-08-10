"""Negative-Pell sparse bound for PCC failures on ``1+p^2=p^2+1``.

On the prime-square shell, ``sigma_proj=m(c)/2``.  If PCC_eta fails then

    m(c) >= 2*c^eta.

Let ``s^2`` be the largest square divisor of c and write ``c=k*s^2``.  Since
``s^2>=m(c)``, for c<=X:

    k <= (1/2) X^(1-eta),

and the defining relation becomes the negative Pell equation

    p^2 - k*s^2 = -1.

For fixed nonsquare k, positive solutions ordered by size differ by a positive
nontrivial norm-one unit in Z[sqrt(k)].  Such a unit is >3, so the number with
p<=sqrt(X) is O(log X) uniformly.  This yields

    O_eta(X^(1-eta) log X)

candidate p values, with a power saving versus the sqrt(X) shell when
eta>1/2.  No primality is used in the count, so it also bounds prime p.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import isqrt

from .abc_prime_square_unit_shell import prime_square_pcc_failure, prime_square_unit_shell
from .abc_projective_sparse_failure import largest_square_divisor_root


@dataclass(frozen=True)
class PrimeSquarePellWitness:
    prime: int
    successor: int
    square_divisor_root: int
    pell_coefficient: int
    pell_identity: int


def prime_square_failure_pell_witness(
    prime: int, numerator: int, denominator: int
) -> PrimeSquarePellWitness | None:
    """Return ``p^2-k*s^2=-1`` data when the prime-square PCC condition fails."""
    if not prime_square_pcc_failure(prime, numerator, denominator):
        return None
    state = prime_square_unit_shell(prime)
    s = largest_square_divisor_root(state.successor)
    if s <= 0 or state.successor % (s * s):
        raise AssertionError("largest square-divisor root failed exact divisibility")
    k = state.successor // (s * s)
    identity = prime * prime - k * s * s
    if identity != -1:
        raise AssertionError("prime-square failure did not produce negative Pell identity")
    return PrimeSquarePellWitness(
        prime=prime,
        successor=state.successor,
        square_divisor_root=s,
        pell_coefficient=k,
        pell_identity=identity,
    )


def pell_coefficient_upper_bound(X: int, numerator: int, denominator: int) -> int:
    """Return floor((1/2) X^(1-p/q)) by exact integer comparison.

    This is the largest integer k satisfying

        (2k)^q <= X^(q-p).
    """
    if isinstance(X, bool) or not isinstance(X, int) or X < 2:
        raise ValueError("X must be an integer >=2")
    if not 0 < numerator < denominator:
        raise ValueError("require 0<numerator<denominator")
    power = X ** (denominator - numerator)
    lower = 0
    upper = 1
    while (2 * upper) ** denominator <= power:
        upper *= 2
    while lower < upper:
        middle = (lower + upper + 1) // 2
        if (2 * middle) ** denominator <= power:
            lower = middle
        else:
            upper = middle - 1
    return lower


def uniform_negative_pell_solution_count_bound(X: int) -> int:
    """Return a simple uniform O(log X) bound per Pell coefficient.

    A positive solution x+y*sqrt(k) is < 2*sqrt(X+1) when x<=sqrt(X).
    Ratios of distinct positive norm-minus-one solutions are nontrivial positive
    norm-one units and hence exceed 3.  Therefore a geometric progression with
    ratio >3 gives a valid count bound.
    """
    if isinstance(X, bool) or not isinstance(X, int) or X < 2:
        raise ValueError("X must be an integer >=2")
    ceiling = 2 * isqrt(X + 1) + 2
    count = 1
    power = 1
    while power <= ceiling:
        power *= 3
        count += 1
    return count


def prime_square_pcc_failure_count_bound(
    X: int, numerator: int, denominator: int
) -> int:
    """Return an explicit Pell-union bound for prime-square PCC failures <=X."""
    k_bound = pell_coefficient_upper_bound(X, numerator, denominator)
    per_k = uniform_negative_pell_solution_count_bound(X)
    pell_bound = k_bound * per_k
    # There are at most sqrt(X) positive p values in the shell at all.
    return min(isqrt(X), pell_bound)
