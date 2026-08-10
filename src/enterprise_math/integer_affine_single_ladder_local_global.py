"""A single modular precision ladder can be complete for exact affine IMAGE.

Let ``G=coker(A)`` have free rank f and torsion exponent

    E = product_p p^a_p.

Choose a positive ladder base R.  The infinite nested family

    R, R^2, R^3, ...

is uniformly complete for exact reachability of every target iff

* every prime dividing E also divides R; and
* when f>0, R>1.

Equivalently ``rad(E) | R`` plus a nontrivial base for any free cokernel.

The proof separates the exact-sequence layers.  On the free part, divisibility by
all powers R^e forces an integer vector to vanish when R>1.  On each p-primary
torsion part, ``v_p(R^e)`` tends to infinity whenever p|R, eventually reaching
the finite exponent depth a_p.

Thus one cofinal arithmetic precision chain is enough; the full modulus lattice
is not required.  A convenient canonical base is:

* E itself when E>1;
* 2 when E=1 and the cokernel has a free part;
* 1 when the cokernel is trivial (no modular test is needed at all).

With base E>1, every torsion IMAGE obstruction fails already at the first level.
Any later first failure can therefore be attributed to a free cokernel component.
This supplies a clean operational split between finite torsion depth and unbounded
free precision.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence

from .integer_affine_fiber_diagnostic import integrally_reachable, modularly_reachable
from .integer_affine_local_global import cokernel_torsion_exponent
from .integer_future_smith_precision import integer_smith_precision_profile


INFINITE = "INFINITE"
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


def integer_radical(value: int) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError("value must be an integer")
    if value <= 0:
        raise ValueError("value must be positive")
    remaining = value
    prime = 2
    result = 1
    while prime * prime <= remaining:
        if remaining % prime:
            prime = 3 if prime == 2 else prime + 2
            continue
        result *= prime
        while remaining % prime == 0:
            remaining //= prime
        prime = 3 if prime == 2 else prime + 2
    if remaining > 1:
        result *= remaining
    return result


def free_cokernel_rank(matrix: Sequence[Sequence[int]]) -> int:
    A = _matrix(matrix)
    profile = integer_smith_precision_profile(A)
    return len(A) - profile.rational_rank


def ladder_base_is_uniformly_complete(
    matrix: Sequence[Sequence[int]],
    base: int,
) -> bool:
    A = _matrix(matrix)
    if isinstance(base, bool) or not isinstance(base, int):
        raise TypeError("base must be an integer")
    if base <= 0:
        raise ValueError("base must be positive")
    exponent = cokernel_torsion_exponent(A)
    free_rank = free_cokernel_rank(A)
    return (
        base % integer_radical(exponent) == 0
        and (free_rank == 0 or base > 1)
    )


def canonical_complete_ladder_base(matrix: Sequence[Sequence[int]]) -> int:
    A = _matrix(matrix)
    exponent = cokernel_torsion_exponent(A)
    free_rank = free_cokernel_rank(A)
    if exponent > 1:
        base = exponent
    elif free_rank > 0:
        base = 2
    else:
        base = 1
    if not ladder_base_is_uniformly_complete(A, base):
        raise AssertionError("canonical local-global ladder base was incomplete")
    return base


def ladder_modulus(base: int, exponent: int) -> int:
    if isinstance(base, bool) or not isinstance(base, int):
        raise TypeError("base must be an integer")
    if isinstance(exponent, bool) or not isinstance(exponent, int):
        raise TypeError("exponent must be an integer")
    if base <= 0:
        raise ValueError("base must be positive")
    if exponent <= 0:
        raise ValueError("exponent must be positive")
    return base ** exponent


@dataclass(frozen=True)
class AffineSingleLadderSpectrum:
    base: int
    observed_max_exponent: int
    moduli: tuple[int, ...]
    solvable_flags: tuple[bool, ...]
    first_unsolvable_exponent: int | None
    exact_reachable: bool
    exact_height: int | str | None

    @property
    def no_failure_observed(self) -> bool:
        return self.first_unsolvable_exponent is None


def finite_single_ladder_spectrum(
    matrix: Sequence[Sequence[int]],
    target: Sequence[int],
    max_exponent: int,
    *,
    base: int | None = None,
    resolve_exact_height: bool = False,
) -> AffineSingleLadderSpectrum:
    A = _matrix(matrix)
    if isinstance(max_exponent, bool) or not isinstance(max_exponent, int):
        raise TypeError("max_exponent must be an integer")
    if max_exponent <= 0:
        raise ValueError("max_exponent must be positive")
    chosen = canonical_complete_ladder_base(A) if base is None else base
    if not ladder_base_is_uniformly_complete(A, chosen):
        raise ValueError("declared ladder base is not uniformly complete for this cokernel")

    moduli = tuple(ladder_modulus(chosen, level) for level in range(1, max_exponent + 1))
    flags = tuple(modularly_reachable(A, target, modulus) for modulus in moduli)
    saw_false = False
    for flag in flags:
        if saw_false and flag:
            raise AssertionError("nested ladder solvability resurrected at finer precision")
        if not flag:
            saw_false = True
    first_failure = next(
        (index + 1 for index, flag in enumerate(flags) if not flag),
        None,
    )
    exact = integrally_reachable(A, target)

    exact_height: int | str | None = None
    if resolve_exact_height:
        if exact:
            exact_height = INFINITE
        elif chosen == 1:
            raise AssertionError("trivial complete ladder cannot contain unreachable targets")
        else:
            level = 1
            while modularly_reachable(A, target, ladder_modulus(chosen, level)):
                level += 1
            exact_height = level - 1

    if exact and first_failure is not None:
        raise AssertionError("exactly reachable target failed a modular ladder level")
    if exact_height != INFINITE and exact_height is not None:
        if first_failure is not None and exact_height != first_failure - 1:
            raise AssertionError("finite ladder disagreed with resolved exact height")
        if first_failure is None and exact_height < max_exponent:
            raise AssertionError("finite ladder missed a resolved failure")

    return AffineSingleLadderSpectrum(
        base=chosen,
        observed_max_exponent=max_exponent,
        moduli=moduli,
        solvable_flags=flags,
        first_unsolvable_exponent=first_failure,
        exact_reachable=exact,
        exact_height=exact_height,
    )
