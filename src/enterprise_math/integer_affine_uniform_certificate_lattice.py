"""Optimal modulus lattice for uniform exact-reachability certification.

Fix ``A:Z^n->Z^m`` and restrict to targets already known to lie in
``im_Q(A)``.  Their cokernel classes range over the finite torsion subgroup

    T = Tor(coker(A)).

A modulus M decides exact reachability correctly for **every** such target iff

    M T = 0.

If ``E=exp(T)`` is the torsion exponent, this is equivalent to

    E | M.

Hence the complete modular certificate precisions form the principal up-set

    {M>0 : E divides M}

in the positive-integer divisibility lattice, and E is its unique least element.
For a full-row-rank matrix the rational-image promise is automatic, so E is the
least uniform all-target certificate modulus.

The necessity is sharp.  If ``E`` does not divide M then ``M T`` is nonzero.
Choose a nonzero class ``t=M u`` in that image.  A rationally reachable integer
target representing t is not exactly reachable, but is solvable modulo M.  Thus
any modulus below the torsion exponent in at least one p-primary direction admits
a false positive.

This up-set is different from two other modular precision regions already used
in the project: fixed-target solvability is a downward/lcm-closed ideal, while
static model indistinguishability is normally a principal divisor down-set.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence

from .integer_affine_local_global import cokernel_torsion_exponent
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


def uniform_rational_image_certificate_modulus(
    matrix: Sequence[Sequence[int]],
) -> int:
    """Least modulus complete for all rationally reachable targets."""
    return cokernel_torsion_exponent(_matrix(matrix))


def modulus_is_uniform_rational_image_certificate(
    matrix: Sequence[Sequence[int]],
    modulus: int,
) -> bool:
    A = _matrix(matrix)
    if isinstance(modulus, bool) or not isinstance(modulus, int):
        raise TypeError("modulus must be an integer")
    if modulus <= 0:
        raise ValueError("modulus must be positive")
    exponent = uniform_rational_image_certificate_modulus(A)
    return modulus % exponent == 0


def full_row_rank_uniform_certificate_modulus(
    matrix: Sequence[Sequence[int]],
) -> int:
    A = _matrix(matrix)
    profile = integer_smith_precision_profile(A)
    if profile.rational_rank != len(A):
        raise ValueError("matrix must have full row rank")
    return uniform_rational_image_certificate_modulus(A)


@dataclass(frozen=True)
class UniformCertificateLatticeReport:
    row_count: int
    rational_rank: int
    free_cokernel_rank: int
    torsion_exponent: int
    rational_image_least_certificate_modulus: int
    full_row_rank: bool

    def modulus_is_complete(self, modulus: int) -> bool:
        return modulus_is_uniform_rational_image_certificate(
            ((1,),),
            1,
        ) if False else (
            isinstance(modulus, int)
            and not isinstance(modulus, bool)
            and modulus > 0
            and modulus % self.torsion_exponent == 0
        )


def uniform_certificate_lattice_report(
    matrix: Sequence[Sequence[int]],
) -> UniformCertificateLatticeReport:
    A = _matrix(matrix)
    profile = integer_smith_precision_profile(A)
    exponent = uniform_rational_image_certificate_modulus(A)
    return UniformCertificateLatticeReport(
        row_count=len(A),
        rational_rank=profile.rational_rank,
        free_cokernel_rank=len(A) - profile.rational_rank,
        torsion_exponent=exponent,
        rational_image_least_certificate_modulus=exponent,
        full_row_rank=profile.rational_rank == len(A),
    )
