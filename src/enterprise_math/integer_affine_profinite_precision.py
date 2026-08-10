"""Profinite precision topology of integer affine IMAGE membership.

Let

    L = im_Z(A) <= Z^m.

At modulus M, affine reachability sees the congruence thickening

    L_M = L + M Z^m.

The exact local-global theorem is the closure identity

    L = intersection_(M>=1) L_M.

Equivalently every finitely generated subgroup of ``Z^m`` is closed in the
congruence/profinite topology.

Finite uniform certification is a stronger topological property.  One modulus M
already decides exact membership for every target iff

    L_M=L,

or equivalently ``M Z^m <= L``.  Such an M exists iff L has finite index in the
ambient lattice, iff ``rank_Q(A)=m``.  In profinite language:

* every integer image lattice is closed;
* it is open (hence clopen) iff it has full ambient rank;
* in the open case the least congruence modulus is the exponent of ``Z^m/L``,
  i.e. the largest Smith invariant factor E.

If A is rank-deficient, L is closed but not open: every target outside L is
separated by some finite modulus, yet no one finite modulus works uniformly for
all targets.

The rational-image promise replaces the ambient lattice by the saturation

    S = span_Q(L) cap Z^m.

Inside S, L has finite index and is therefore open in the induced profinite
precision.  The same torsion exponent E is the least uniform certificate scale
there.  This is the topological form of the IMAGE/FIBER local-global hierarchy.

Profinite topology, subgroup separability and lattice index are standard prior
mathematics.  The project value is the precision interpretation: finite exact
certifiability is openness, while asymptotic modular identifiability is closure.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence

from .integer_affine_fiber_diagnostic import (
    integrally_reachable,
    modularly_reachable,
    rationally_reachable,
)
from .integer_affine_local_global import (
    cokernel_torsion_exponent,
    local_global_countermodulus,
)
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


def image_is_profinite_open(matrix: Sequence[Sequence[int]]) -> bool:
    A = _matrix(matrix)
    return integer_smith_precision_profile(A).rational_rank == len(A)


def image_is_profinite_closed(matrix: Sequence[Sequence[int]]) -> bool:
    """All finitely generated integer image lattices are congruence-closed."""
    _matrix(matrix)
    return True


def least_uniform_open_modulus(matrix: Sequence[Sequence[int]]) -> int | None:
    A = _matrix(matrix)
    return cokernel_torsion_exponent(A) if image_is_profinite_open(A) else None


def finite_modulus_decides_all_target_membership(
    matrix: Sequence[Sequence[int]],
    modulus: int,
) -> bool:
    """Whether ``L + M Z^m = L`` for the image lattice L."""
    A = _matrix(matrix)
    if isinstance(modulus, bool) or not isinstance(modulus, int):
        raise TypeError("modulus must be an integer")
    if modulus <= 0:
        raise ValueError("modulus must be positive")
    if not image_is_profinite_open(A):
        return False
    exponent = cokernel_torsion_exponent(A)
    return modulus % exponent == 0


def target_separation_modulus(
    matrix: Sequence[Sequence[int]],
    target: Sequence[int],
) -> int | None:
    """Finite congruence neighborhood separating an unreachable target from L."""
    A = _matrix(matrix)
    if integrally_reachable(A, target):
        return None
    modulus = local_global_countermodulus(A, target)
    if modulus is None:
        raise AssertionError("closed image lattice lost finite separation modulus")
    if modularly_reachable(A, target, modulus):
        raise AssertionError("declared separation modulus did not separate target")
    return modulus


def rational_image_subspace_has_finite_certificate(
    matrix: Sequence[Sequence[int]],
    target: Sequence[int],
) -> bool:
    """Exact membership on the saturation is decided by the torsion exponent."""
    A = _matrix(matrix)
    if not rationally_reachable(A, target):
        raise ValueError("target must lie in the rational image/saturation")
    exponent = cokernel_torsion_exponent(A)
    modular = modularly_reachable(A, target, exponent)
    exact = integrally_reachable(A, target)
    if modular != exact:
        raise AssertionError("saturated-subspace open certificate failed")
    return modular


@dataclass(frozen=True)
class ProfiniteImagePrecisionReport:
    ambient_rank: int
    image_rational_rank: int
    free_cokernel_rank: int
    profinitely_closed: bool
    profinitely_open: bool
    least_uniform_modulus: int | None
    torsion_exponent: int

    @property
    def clopen(self) -> bool:
        return self.profinitely_closed and self.profinitely_open


def profinite_image_precision_report(
    matrix: Sequence[Sequence[int]],
) -> ProfiniteImagePrecisionReport:
    A = _matrix(matrix)
    profile = integer_smith_precision_profile(A)
    ambient = len(A)
    image_rank = profile.rational_rank
    open_ = image_rank == ambient
    exponent = cokernel_torsion_exponent(A)
    return ProfiniteImagePrecisionReport(
        ambient_rank=ambient,
        image_rational_rank=image_rank,
        free_cokernel_rank=ambient - image_rank,
        profinitely_closed=True,
        profinitely_open=open_,
        least_uniform_modulus=exponent if open_ else None,
        torsion_exponent=exponent,
    )
