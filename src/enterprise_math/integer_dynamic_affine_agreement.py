"""Exact and modular agreement states for total-affine dynamic models.

The dynamic affine difference compiler returns a Z-row module in homogeneous
coordinates.  Write one HNF basis as rows

    (a_i, c_i),

where ``a_i`` contains coefficients of the original state x and ``c_i`` is the
constant homogeneous coordinate.  The two affine models agree on x for every
future action word exactly when

    A x = -c.

This exposes two distinct diagnostic layers.

### IMAGE / COKERNEL

First ask whether ``-c`` belongs to the integer column image of A (exact case),
or to

    im_Z(A) + M Z^r

for modulus M.  If not, there are no agreement states.

### FIBER

If the equation is solvable, all solutions form an affine coset of ``ker A``
(exact) or ``ker(A mod M)`` (modular).  Hence the modular number of agreeing
states is exactly the Smith kernel size of A modulo M.

So image solvability and kernel multiplicity must not be conflated.  The scalar
pair ``2x+1=0 mod4`` (no solution) versus ``2x+2=0 mod4`` (two solutions) is the
sharp smallest example.

Integer lattice membership, affine congruences and Smith kernels are standard
prior mathematics.  The project value is the exact cross-layer diagnostic on a
dynamic-model agreement problem.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence

from .integer_action_module_closure import integer_row_hermite_basis
from .integer_dynamic_affine_model_separation import (
    dynamic_affine_difference_module_basis,
)
from .integer_future_modular_precision import modular_smith_precision_report
from .integer_future_smith_precision import integer_smith_precision_profile


Matrix = tuple[tuple[int, ...], ...]
Vector = tuple[int, ...]


def split_affine_difference_basis(
    augmented_basis: Sequence[Sequence[int]],
) -> tuple[Matrix, Vector]:
    rows = tuple(tuple(row) for row in augmented_basis)
    if not rows:
        return (), ()
    width = len(rows[0])
    if width < 2 or any(len(row) != width for row in rows):
        raise ValueError("augmented affine rows must share width at least two")
    for row in rows:
        for value in row:
            if isinstance(value, bool) or not isinstance(value, int):
                raise TypeError("augmented affine entries must be integers")
    return (
        tuple(row[:-1] for row in rows),
        tuple(row[-1] for row in rows),
    )


def column_image_generators_as_rows(linear_rows: Sequence[Sequence[int]]) -> Matrix:
    rows = tuple(tuple(row) for row in linear_rows)
    if not rows:
        return ()
    width = len(rows[0])
    if width == 0 or any(len(row) != width for row in rows):
        raise ValueError("linear rows must share positive width")
    return tuple(
        tuple(rows[row][column] for row in range(len(rows)))
        for column in range(width)
    )


def vector_in_integer_row_lattice(
    generators: Sequence[Sequence[int]],
    target: Sequence[int],
) -> bool:
    rows = tuple(tuple(row) for row in generators)
    vector = tuple(target)
    if not vector:
        raise ValueError("target vector must be nonempty")
    for value in vector:
        if isinstance(value, bool) or not isinstance(value, int):
            raise TypeError("target entries must be integers")
    if not rows:
        return all(value == 0 for value in vector)
    if any(len(row) != len(vector) for row in rows):
        raise ValueError("lattice generators must match target dimension")
    basis = integer_row_hermite_basis(rows)
    extended = integer_row_hermite_basis(rows + (vector,))
    return basis == extended


def affine_equation_integer_solvable(
    linear_rows: Sequence[Sequence[int]],
    constants: Sequence[int],
) -> bool:
    rows = tuple(tuple(row) for row in linear_rows)
    shift = tuple(constants)
    if len(rows) != len(shift):
        raise ValueError("one constant is required per affine equation")
    if not rows:
        return not shift
    target = tuple(-value for value in shift)
    return vector_in_integer_row_lattice(
        column_image_generators_as_rows(rows),
        target,
    )


def affine_equation_modular_solvable(
    linear_rows: Sequence[Sequence[int]],
    constants: Sequence[int],
    modulus: int,
) -> bool:
    rows = tuple(tuple(row) for row in linear_rows)
    shift = tuple(constants)
    if len(rows) != len(shift):
        raise ValueError("one constant is required per affine equation")
    if isinstance(modulus, bool) or not isinstance(modulus, int):
        raise TypeError("modulus must be an integer")
    if modulus <= 0:
        raise ValueError("modulus must be positive")
    if not rows:
        return not shift
    row_count = len(rows)
    target = tuple(-value for value in shift)
    generators = column_image_generators_as_rows(rows) + tuple(
        tuple(modulus if row == column else 0 for column in range(row_count))
        for row in range(row_count)
    )
    return vector_in_integer_row_lattice(generators, target)


@dataclass(frozen=True)
class DynamicAffineExactAgreementReport:
    state_dimension: int
    solvable: bool
    agreement_free_rank: int | None
    linear_smith_factors: tuple[int, ...]
    augmented_difference_basis: Matrix


@dataclass(frozen=True)
class DynamicAffineModularAgreementReport:
    modulus: int
    state_dimension: int
    solvable: bool
    agreement_state_count: int
    total_state_count: int
    linear_smith_factors: tuple[int, ...]

    @property
    def all_states_agree(self) -> bool:
        return self.agreement_state_count == self.total_state_count


def dynamic_affine_exact_agreement_report(
    left_actions,
    left_observation_rows,
    left_observation_offset,
    right_actions,
    right_observation_rows,
    right_observation_offset,
) -> DynamicAffineExactAgreementReport:
    basis = dynamic_affine_difference_module_basis(
        left_actions,
        left_observation_rows,
        left_observation_offset,
        right_actions,
        right_observation_rows,
        right_observation_offset,
    )
    # Original state dimension is augmented width minus one.  If the difference
    # module is zero, infer it from the observation rows instead.
    if basis:
        state_dimension = len(basis[0]) - 1
    else:
        observation_rows = tuple(tuple(row) for row in left_observation_rows)
        if not observation_rows:
            raise ValueError("left observation rows must be nonempty")
        state_dimension = len(observation_rows[0])
        return DynamicAffineExactAgreementReport(
            state_dimension=state_dimension,
            solvable=True,
            agreement_free_rank=state_dimension,
            linear_smith_factors=(),
            augmented_difference_basis=(),
        )

    linear, constants = split_affine_difference_basis(basis)
    solvable = affine_equation_integer_solvable(linear, constants)
    profile = integer_smith_precision_profile(linear) if linear else None
    return DynamicAffineExactAgreementReport(
        state_dimension=state_dimension,
        solvable=solvable,
        agreement_free_rank=(
            profile.hidden_free_rank if solvable and profile is not None else None
        ),
        linear_smith_factors=(
            profile.smith_invariant_factors if profile is not None else ()
        ),
        augmented_difference_basis=basis,
    )


def dynamic_affine_modular_agreement_report(
    left_actions,
    left_observation_rows,
    left_observation_offset,
    right_actions,
    right_observation_rows,
    right_observation_offset,
    modulus: int,
) -> DynamicAffineModularAgreementReport:
    exact = dynamic_affine_exact_agreement_report(
        left_actions,
        left_observation_rows,
        left_observation_offset,
        right_actions,
        right_observation_rows,
        right_observation_offset,
    )
    if isinstance(modulus, bool) or not isinstance(modulus, int):
        raise TypeError("modulus must be an integer")
    if modulus <= 0:
        raise ValueError("modulus must be positive")
    total = modulus ** exact.state_dimension
    if not exact.augmented_difference_basis:
        return DynamicAffineModularAgreementReport(
            modulus=modulus,
            state_dimension=exact.state_dimension,
            solvable=True,
            agreement_state_count=total,
            total_state_count=total,
            linear_smith_factors=(),
        )
    linear, constants = split_affine_difference_basis(exact.augmented_difference_basis)
    solvable = affine_equation_modular_solvable(linear, constants, modulus)
    if not solvable:
        return DynamicAffineModularAgreementReport(
            modulus=modulus,
            state_dimension=exact.state_dimension,
            solvable=False,
            agreement_state_count=0,
            total_state_count=total,
            linear_smith_factors=exact.linear_smith_factors,
        )
    modular = modular_smith_precision_report(linear, modulus)
    return DynamicAffineModularAgreementReport(
        modulus=modulus,
        state_dimension=exact.state_dimension,
        solvable=True,
        agreement_state_count=modular.kernel_size,
        total_state_count=total,
        linear_smith_factors=exact.linear_smith_factors,
    )
