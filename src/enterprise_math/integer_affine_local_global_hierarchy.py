"""Structural hierarchy for finite local-global affine reachability certificates.

The generic local-global theorem for ``A x=b`` needs all modular precisions when
no extra information is available.  This module records the exact conditions
under which that infinite family collapses to a finite one.

Let ``G=coker(A)`` and let ``E=exp(Tor(G))`` (largest nonzero Smith factor, or
1 when the torsion subgroup is trivial).

### Rational-image certificate

If ``b`` is already known to lie in ``im_Q(A)``, then its cokernel class is
pure torsion.  Since ``E Tor(G)=0``,

    A x=b over Z
      iff
    A x == b (mod E) is solvable.

When A has full row rank, every target is rationally reachable, so the **same
single modulus E certifies every integer target**.  Equivalently, the finite CRT
family consisting of the prime-power components of E is complete.

### Bounded free-cokernel certificate

If A is rank-deficient but admissible targets satisfy a known bound
``||Qb||_infinity<=B`` for an integer rational-left-nullspace family Q, then any
multiple of E strictly greater than B certifies exact reachability.  The smallest
positive modulus satisfying those two theorem conditions is

    E * (floor(B/E)+1).

For a box ``|b_i|<=H``, one may take

    B=H * max_q ||q||_1.

### No-bound boundary

If a free cokernel direction is allowed with unbounded target lifts, no fixed
finite modulus family is uniformly complete: its lcm D is defeated by shifting a
target by D along that free direction.  Thus finite certification is controlled
by a genuine trichotomy:

* finite cokernel / rational-image promise -> torsion exponent certificate;
* free cokernel + independent height bound -> bounded certificate;
* free cokernel + no bound -> finite-modular no-go.

All group-theoretic ingredients are standard.  The project value is the precise
condition under which a finite precision ceiling becomes an exact decision
procedure rather than only evidence.
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
    integer_left_nullspace_rows,
    left_nullspace_target_values,
    prime_power_components,
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


def smallest_multiple_above(divisor: int, bound: int) -> int:
    """Smallest positive multiple of divisor strictly greater than bound."""
    if isinstance(divisor, bool) or not isinstance(divisor, int):
        raise TypeError("divisor must be an integer")
    if isinstance(bound, bool) or not isinstance(bound, int):
        raise TypeError("bound must be an integer")
    if divisor <= 0:
        raise ValueError("divisor must be positive")
    if bound < 0:
        raise ValueError("bound must be nonnegative")
    result = divisor * (bound // divisor + 1)
    if result <= bound or result % divisor:
        raise AssertionError("smallest-multiple certificate arithmetic failed")
    return result


def rational_image_certificate_modulus(matrix: Sequence[Sequence[int]]) -> int:
    """Single complete modulus once free cokernel obstruction is excluded."""
    return cokernel_torsion_exponent(_matrix(matrix))


def rational_image_certificate_holds(
    matrix: Sequence[Sequence[int]],
    target: Sequence[int],
) -> bool:
    """Verify exact reachability from rational reachability plus mod-E solvability."""
    A = _matrix(matrix)
    if not rationally_reachable(A, target):
        raise ValueError("target must already be known rationally reachable")
    modulus = rational_image_certificate_modulus(A)
    modular = modularly_reachable(A, target, modulus)
    exact = integrally_reachable(A, target)
    if modular != exact:
        raise AssertionError("torsion-exponent certificate disagreed with exact reachability")
    return modular


def full_row_rank_certificate_modulus(matrix: Sequence[Sequence[int]]) -> int:
    """Uniform all-target certificate modulus for a full-row-rank map."""
    A = _matrix(matrix)
    rank = integer_smith_precision_profile(A).rational_rank
    if rank != len(A):
        raise ValueError("matrix must have full row rank")
    return cokernel_torsion_exponent(A)


def bounded_box_certificate_modulus(
    matrix: Sequence[Sequence[int]],
    target_abs_bound: int,
) -> int:
    """Smallest modulus satisfying the theorem conditions for one target box."""
    A = _matrix(matrix)
    if isinstance(target_abs_bound, bool) or not isinstance(target_abs_bound, int):
        raise TypeError("target_abs_bound must be an integer")
    if target_abs_bound < 0:
        raise ValueError("target_abs_bound must be nonnegative")
    left_rows = integer_left_nullspace_rows(A)
    max_l1 = max((sum(abs(value) for value in row) for row in left_rows), default=0)
    free_bound = target_abs_bound * max_l1
    return smallest_multiple_above(cokernel_torsion_exponent(A), free_bound)


def bounded_box_certificate_holds(
    matrix: Sequence[Sequence[int]],
    target: Sequence[int],
    target_abs_bound: int,
) -> bool:
    A = _matrix(matrix)
    target_values = tuple(target)
    if len(target_values) != len(A):
        raise ValueError("target must have one entry per matrix row")
    if any(abs(value) > target_abs_bound for value in target_values):
        raise ValueError("target lies outside declared absolute-value bound")
    modulus = bounded_box_certificate_modulus(A, target_abs_bound)
    modular = modularly_reachable(A, target_values, modulus)
    exact = integrally_reachable(A, target_values)
    if modular != exact:
        raise AssertionError("bounded-box certificate disagreed with exact reachability")
    return modular


@dataclass(frozen=True)
class LocalGlobalCertificationHierarchy:
    row_count: int
    rational_rank: int
    free_cokernel_rank: int
    torsion_exponent: int
    full_row_rank: bool
    full_row_rank_certificate_modulus: int | None
    full_row_rank_prime_power_family: tuple[int, ...] | None


def local_global_certification_hierarchy(
    matrix: Sequence[Sequence[int]],
) -> LocalGlobalCertificationHierarchy:
    A = _matrix(matrix)
    profile = integer_smith_precision_profile(A)
    row_count = len(A)
    free_rank = row_count - profile.rational_rank
    exponent = cokernel_torsion_exponent(A)
    full = free_rank == 0
    modulus = exponent if full else None
    components = prime_power_components(exponent) if full else None
    return LocalGlobalCertificationHierarchy(
        row_count=row_count,
        rational_rank=profile.rational_rank,
        free_cokernel_rank=free_rank,
        torsion_exponent=exponent,
        full_row_rank=full,
        full_row_rank_certificate_modulus=modulus,
        full_row_rank_prime_power_family=components,
    )


def left_nullspace_bound_for_target(
    matrix: Sequence[Sequence[int]],
    target: Sequence[int],
) -> int:
    """Actual free-obstruction height in the deterministic chosen Q chart."""
    values = left_nullspace_target_values(matrix, target)
    return max((abs(value) for value in values), default=0)
