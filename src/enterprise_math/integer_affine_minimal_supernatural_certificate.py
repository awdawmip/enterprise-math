"""Minimal supernatural precision profiles for exact affine IMAGE certification.

Let

    coker(A) ~= Z^f direct_sum T,
    E = exp(T) = product_q q^a_q.

If ``f=0``, the unique least complete supernatural precision is the ordinary
finite integer E.

If ``f>0``, no finite precision is complete and there is no unique least
supernatural profile.  The inclusion-minimal complete profiles are indexed by an
arbitrary choice of one prime p:

    Q_p has p-exponent infinity,
    Q_p has q-exponent a_q for every q!=p.

Equivalently, Q_p is the torsion requirement E with exactly one prime direction
promoted from its finite required depth (possibly zero) to infinity.

A concrete experiment family realizing Q_p is

    M_e = E * p^e,    e=0,1,2,... .

The first level M_0=E already kills every nonzero torsion IMAGE class.  If the
target still passes, any remaining obstruction lies in the free cokernel; the
unbounded p-adic factor then separates every nonzero free integer coordinate.

Minimality is exact:

* an infinite-support profile is not minimal because finite extra primes can be
  removed while infinite support remains;
* a profile with two or more infinite-depth primes is not minimal because all
  but one can be lowered to their finite torsion-required depths;
* any finite depth above a_q is not minimal because it can be lowered to a_q.

Thus the only minimal complete profiles have exactly one infinite prime depth and
all other depths exactly at the torsion requirement.

This sharpens a generic power ladder R^e, which often sends several torsion
primes to unnecessary infinite depth.  The result is standard supernatural-number
order theory plus finite abelian-group decomposition; the project value is the
minimal precision interpretation.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence

from .integer_affine_local_global import cokernel_torsion_exponent
from .integer_affine_prime_local_global import prime_power_depths_required_by_torsion
from .integer_future_smith_precision import integer_smith_precision_profile


Matrix = tuple[tuple[int, ...], ...]


def _matrix(values: Sequence[Sequence[int]]) -> Matrix:
    rows = tuple(tuple(row) for row in values)
    if not rows:
        raise ValueError("matrix must contain at least one row")
    width = len(rows[0])
    if width == 0 or any(len(row) != width for row in rows):
        raise ValueError("matrix rows must have one common positive width")
    for row in rows:
        for value in row:
            if isinstance(value, bool) or not isinstance(value, int):
                raise TypeError("matrix entries must be integers")
    return rows


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


def free_cokernel_rank(matrix: Sequence[Sequence[int]]) -> int:
    A = _matrix(matrix)
    return len(A) - integer_smith_precision_profile(A).rational_rank


@dataclass(frozen=True)
class MinimalSupernaturalCertificate:
    torsion_exponent: int
    free_cokernel_rank: int
    infinite_prime: int | None
    finite_required_prime_depths: tuple[tuple[int, int], ...]

    @property
    def finite(self) -> bool:
        return self.infinite_prime is None

    def finite_depth_at(self, prime: int) -> int:
        p = _prime(prime)
        if self.infinite_prime == p:
            raise ValueError("chosen prime has infinite rather than finite depth")
        for current, depth in self.finite_required_prime_depths:
            if current == p:
                return depth
        return 0


def minimal_supernatural_certificate(
    matrix: Sequence[Sequence[int]],
    *,
    infinite_prime: int | None = None,
) -> MinimalSupernaturalCertificate:
    A = _matrix(matrix)
    free_rank = free_cokernel_rank(A)
    exponent = cokernel_torsion_exponent(A)
    depths = prime_power_depths_required_by_torsion(A)

    if free_rank == 0:
        if infinite_prime is not None:
            raise ValueError("full-row-rank map has a finite least certificate")
        return MinimalSupernaturalCertificate(
            torsion_exponent=exponent,
            free_cokernel_rank=0,
            infinite_prime=None,
            finite_required_prime_depths=depths,
        )

    if infinite_prime is None:
        raise ValueError("free cokernel requires choosing one infinite prime direction")
    p = _prime(infinite_prime)
    finite_depths = tuple(
        (prime, depth) for prime, depth in depths if prime != p
    )
    return MinimalSupernaturalCertificate(
        torsion_exponent=exponent,
        free_cokernel_rank=free_rank,
        infinite_prime=p,
        finite_required_prime_depths=finite_depths,
    )


def minimal_single_prime_ladder_modulus(
    matrix: Sequence[Sequence[int]],
    prime: int,
    level: int,
) -> int:
    """Concrete level ``E*p^level`` realizing one minimal supernatural profile."""
    A = _matrix(matrix)
    p = _prime(prime)
    if isinstance(level, bool) or not isinstance(level, int):
        raise TypeError("level must be an integer")
    if level < 0:
        raise ValueError("level must be nonnegative")
    return cokernel_torsion_exponent(A) * (p ** level)
