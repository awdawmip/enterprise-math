"""Local-global reachability for integer affine targets.

For an integer homomorphism ``A: Z^n -> Z^m`` and target ``b``, modular
solvability is the cokernel condition

    A x == b (mod M)    iff    [b] in M coker(A).

Because a finitely generated abelian group ``G`` satisfies

    intersection_(M>=1) M G = {0},

one obtains the exact local-global theorem

    A x = b over Z
      iff
    A x == b (mod M) is solvable for every positive M,

and equivalently it is enough to test every prime power.

A finite modular family cannot certify this in general: all of its equality
precision collapses to one lcm ceiling.  A finite certificate becomes possible
once an independent bound excludes arbitrarily deep free-cokernel lifts.

Let ``Q`` be any integer row family spanning the rational left nullspace of A,
so ``Q A=0`` and

    Q b = 0    iff    b in im_Q(A).

Let ``E`` be the exponent of the torsion subgroup of ``coker(A)`` (the largest
nonzero Smith invariant factor, or 1 when there is no torsion).  If an admissible
target family satisfies

    ||Q b||_infinity <= B,

then every modulus D with

    D > B,    E | D

is an exact finite local-global certificate on that family:

    A x = b over Z
      iff
    A x == b (mod D) is solvable.

Indeed modular solvability forces ``Qb`` to be divisible by D; the bound then
forces ``Qb=0``, removing the free cokernel obstruction.  The target class is
then torsion, and ``E|D`` makes ``D`` annihilate that torsion, so membership in
``D coker(A)`` forces the class itself to vanish.

For one fixed target, the exact data provide the bound ``B=||Qb||_infinity``.
For a whole target box ``|b_i|<=H``, the uniform bound

    B <= H * max_q ||q||_1

produces one modulus certifying every target in the box.

This does not contradict the finite-modular no-go results: the modulus is chosen
using an independent exact/bounded lift constraint.  Without such a bound, no
fixed finite D can exclude a free cokernel coordinate that is an unknown multiple
of D.

Smith normal form, rational nullspaces, finitely generated abelian groups, CRT
and linear congruences are standard prior mathematics.  This module only packages
the exact A2/P023 finite-precision certification boundary.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import gcd, lcm
from typing import Sequence

from .integer_affine_fiber_diagnostic import (
    integrally_reachable,
    modularly_reachable,
)
from .integer_future_smith_precision import integer_smith_precision_profile


Matrix = tuple[tuple[int, ...], ...]
Vector = tuple[int, ...]


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


def _target(values: Sequence[int], row_count: int) -> Vector:
    target = tuple(values)
    if len(target) != row_count:
        raise ValueError("target must have one entry per matrix row")
    for value in target:
        if isinstance(value, bool) or not isinstance(value, int):
            raise TypeError("target entries must be integers")
    return target


def _lcm_many(values: Sequence[int]) -> int:
    result = 1
    for value in values:
        result = lcm(result, value)
    return result


def _primitive_integer_vector(values: Sequence[Fraction]) -> Vector:
    denominators = tuple(value.denominator for value in values)
    common_denominator = _lcm_many(denominators)
    integers = [int(value * common_denominator) for value in values]
    common = 0
    for value in integers:
        common = gcd(common, abs(value))
    if common:
        integers = [value // common for value in integers]
    first_nonzero = next((value for value in integers if value), 0)
    if first_nonzero < 0:
        integers = [-value for value in integers]
    return tuple(integers)


def integer_left_nullspace_rows(matrix: Sequence[Sequence[int]]) -> Matrix:
    """Return integer rows spanning ``{q in Q^m : q A=0}`` over Q.

    The rows are individually primitive but are not claimed to be a canonical
    integral lattice basis.  Rational spanning is exactly what the finite
    certificate theorem needs.
    """
    A = _matrix(matrix)
    row_count = len(A)
    column_count = len(A[0])

    # Solve A^T q = 0 by exact RREF.  The equation matrix has ``column_count``
    # rows and ``row_count`` unknown coordinates.
    work = [
        [Fraction(A[row][column]) for row in range(row_count)]
        for column in range(column_count)
    ]
    pivot_columns: list[int] = []
    pivot_row = 0
    for column in range(row_count):
        pivot = next(
            (
                row
                for row in range(pivot_row, len(work))
                if work[row][column] != 0
            ),
            None,
        )
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        pivot_value = work[pivot_row][column]
        work[pivot_row] = [value / pivot_value for value in work[pivot_row]]
        for row in range(len(work)):
            if row == pivot_row:
                continue
            factor = work[row][column]
            if factor == 0:
                continue
            work[row] = [
                left - factor * right
                for left, right in zip(work[row], work[pivot_row], strict=True)
            ]
        pivot_columns.append(column)
        pivot_row += 1
        if pivot_row == len(work):
            break

    free_columns = tuple(
        column for column in range(row_count) if column not in set(pivot_columns)
    )
    basis = []
    for free in free_columns:
        vector = [Fraction(0) for _ in range(row_count)]
        vector[free] = Fraction(1)
        for row, pivot_column in enumerate(pivot_columns):
            vector[pivot_column] = -work[row][free]
        primitive = _primitive_integer_vector(vector)
        if not any(primitive):
            raise AssertionError("left-nullspace basis produced zero vector")
        basis.append(primitive)

    # Mechanical verification of the annihilator property.
    for row in basis:
        for column in range(column_count):
            if sum(row[index] * A[index][column] for index in range(row_count)) != 0:
                raise AssertionError("left-nullspace row failed to annihilate matrix")
    return tuple(basis)


def left_nullspace_target_values(
    matrix: Sequence[Sequence[int]],
    target: Sequence[int],
) -> Vector:
    A = _matrix(matrix)
    b = _target(target, len(A))
    return tuple(
        sum(coefficient * value for coefficient, value in zip(row, b, strict=True))
        for row in integer_left_nullspace_rows(A)
    )


def cokernel_torsion_exponent(matrix: Sequence[Sequence[int]]) -> int:
    """Exponent of the torsion subgroup of coker(A); 1 when torsion-free."""
    profile = integer_smith_precision_profile(_matrix(matrix))
    return profile.smith_invariant_factors[-1] if profile.smith_invariant_factors else 1


def _certificate_modulus(torsion_exponent: int, free_bound: int) -> int:
    if torsion_exponent <= 0:
        raise ValueError("torsion exponent must be positive")
    if free_bound < 0:
        raise ValueError("free bound must be nonnegative")
    result = lcm(torsion_exponent, free_bound + 1)
    if result <= free_bound or result % torsion_exponent != 0:
        raise AssertionError("finite local-global modulus lost certificate conditions")
    return result


def target_specific_certificate_modulus(
    matrix: Sequence[Sequence[int]],
    target: Sequence[int],
) -> int:
    """One finite modulus whose solvability is equivalent to exact reachability."""
    A = _matrix(matrix)
    b = _target(target, len(A))
    values = left_nullspace_target_values(A, b)
    free_bound = max((abs(value) for value in values), default=0)
    return _certificate_modulus(cokernel_torsion_exponent(A), free_bound)


def bounded_target_certificate_modulus(
    matrix: Sequence[Sequence[int]],
    target_abs_bound: int,
) -> int:
    """One modulus certifying every target with ``|b_i|<=target_abs_bound``."""
    A = _matrix(matrix)
    if isinstance(target_abs_bound, bool) or not isinstance(target_abs_bound, int):
        raise TypeError("target_abs_bound must be an integer")
    if target_abs_bound < 0:
        raise ValueError("target_abs_bound must be nonnegative")
    left_rows = integer_left_nullspace_rows(A)
    max_l1 = max((sum(abs(value) for value in row) for row in left_rows), default=0)
    free_bound = target_abs_bound * max_l1
    return _certificate_modulus(cokernel_torsion_exponent(A), free_bound)


def prime_power_components(modulus: int) -> tuple[int, ...]:
    if isinstance(modulus, bool) or not isinstance(modulus, int):
        raise TypeError("modulus must be an integer")
    if modulus <= 0:
        raise ValueError("modulus must be positive")
    if modulus == 1:
        return ()
    remaining = modulus
    prime = 2
    components = []
    while prime * prime <= remaining:
        if remaining % prime:
            prime = 3 if prime == 2 else prime + 2
            continue
        power = 1
        while remaining % prime == 0:
            remaining //= prime
            power *= prime
        components.append(power)
        prime = 3 if prime == 2 else prime + 2
    if remaining > 1:
        components.append(remaining)
    if _lcm_many(tuple(components)) != modulus:
        raise AssertionError("prime-power components failed CRT reconstruction")
    return tuple(components)


@dataclass(frozen=True)
class AffineFiniteLocalGlobalReport:
    certificate_modulus: int
    prime_power_certificate_moduli: tuple[int, ...]
    exact_reachable: bool
    certificate_modulus_solvable: bool
    prime_power_family_solvable: bool
    left_nullspace_rows: Matrix
    left_nullspace_target_values: Vector
    free_obstruction_bound: int
    torsion_exponent: int

    @property
    def certificate_matches_exact(self) -> bool:
        return self.exact_reachable == self.certificate_modulus_solvable


def affine_finite_local_global_report(
    matrix: Sequence[Sequence[int]],
    target: Sequence[int],
) -> AffineFiniteLocalGlobalReport:
    A = _matrix(matrix)
    b = _target(target, len(A))
    left_rows = integer_left_nullspace_rows(A)
    values = left_nullspace_target_values(A, b)
    free_bound = max((abs(value) for value in values), default=0)
    torsion_exponent = cokernel_torsion_exponent(A)
    modulus = _certificate_modulus(torsion_exponent, free_bound)
    components = prime_power_components(modulus)
    exact = integrally_reachable(A, b)
    mod_solvable = modularly_reachable(A, b, modulus)
    component_solvable = all(
        modularly_reachable(A, b, component) for component in components
    )
    if mod_solvable != component_solvable:
        raise AssertionError("CRT prime-power family disagreed with certificate modulus")
    if exact != mod_solvable:
        raise AssertionError("finite local-global certificate disagreed with exact reachability")
    return AffineFiniteLocalGlobalReport(
        certificate_modulus=modulus,
        prime_power_certificate_moduli=components,
        exact_reachable=exact,
        certificate_modulus_solvable=mod_solvable,
        prime_power_family_solvable=component_solvable,
        left_nullspace_rows=left_rows,
        left_nullspace_target_values=values,
        free_obstruction_bound=free_bound,
        torsion_exponent=torsion_exponent,
    )


def local_global_countermodulus(
    matrix: Sequence[Sequence[int]],
    target: Sequence[int],
) -> int | None:
    """Return a finite modulus detecting exact unreachability, else None."""
    report = affine_finite_local_global_report(matrix, target)
    return None if report.exact_reachable else report.certificate_modulus


def local_global_prime_power_counterexample(
    matrix: Sequence[Sequence[int]],
    target: Sequence[int],
) -> int | None:
    """Return one prime power at which an unreachable target already fails."""
    report = affine_finite_local_global_report(matrix, target)
    if report.exact_reachable:
        return None
    counterexample = next(
        (
            modulus
            for modulus in report.prime_power_certificate_moduli
            if not modularly_reachable(matrix, target, modulus)
        ),
        None,
    )
    if counterexample is None:
        raise AssertionError("unreachable target had no prime-power local obstruction")
    return counterexample
