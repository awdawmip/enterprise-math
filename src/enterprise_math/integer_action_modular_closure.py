"""Exact modular future-action closure via full-rank integer preimage lattices.

For integer future row lattice ``L_h`` and modulus ``M``, the row module seen
modulo M is represented without residue-state enumeration by

    K_h = L_h + M Z^n.

``K_h`` is a full-rank finite-index lattice in ``Z^n`` from horizon zero.  Its
quotient ``K_h / M Z^n`` is exactly the modular row module.

The action closure is

    K_(h+1) = K_h + sum_a K_h A_a.

Because every action matrix is integer, ``M Z^n`` is action-invariant.  A row
Hermite basis therefore gives an exact online compiler.

The finite index

    I_h = [Z^n : K_h]

has two simultaneous meanings under the standard nondegenerate pairing on
``(Z/MZ)^n``:

* ``I_h`` is the number of modular state residues invisible to all current
  future rows (kernel size);
* ``M^n / I_h`` is the number of observable modular future phases / size of the
  modular row module.

Every strict closure step enlarges ``K_h`` and hence decreases ``I_h`` to a
proper divisor.  Therefore final modular closure is attained after at most
``Omega(I_0)`` strict refinements.  For prime M this reduces to the ordinary
finite-field hidden-dimension budget; prime powers retain several p-adic layers.

Hermite normal form, finite-index lattices and finite abelian duality are standard
prior mathematics.  The project value is the exact modular P023 action-language
compiler and arithmetic stop bound.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence

from .integer_action_language_observability import prime_factor_multiplicity
from .integer_action_module_closure import (
    action_module_closure_step,
    integer_row_hermite_basis,
)
from .integer_future_smith_precision import integer_smith_precision_profile


Matrix = tuple[tuple[int, ...], ...]


def _rows(values: Sequence[Sequence[int]]) -> Matrix:
    rows = tuple(tuple(row) for row in values)
    if not rows:
        raise ValueError("observation rows must be nonempty")
    width = len(rows[0])
    if width == 0 or any(len(row) != width for row in rows):
        raise ValueError("observation rows must have one common positive width")
    for row in rows:
        for value in row:
            if isinstance(value, bool) or not isinstance(value, int):
                raise TypeError("observation entries must be integers")
    return rows


def _modulus(value: int) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError("modulus must be an integer")
    if value <= 0:
        raise ValueError("modulus must be positive")
    return value


def modulus_identity_rows(dimension: int, modulus: int) -> Matrix:
    if isinstance(dimension, bool) or not isinstance(dimension, int) or dimension <= 0:
        raise ValueError("dimension must be a positive integer")
    mod = _modulus(modulus)
    return tuple(
        tuple(mod if row == column else 0 for column in range(dimension))
        for row in range(dimension)
    )


def modular_preimage_lattice_basis(
    observation_rows: Sequence[Sequence[int]],
    modulus: int,
) -> Matrix:
    rows = _rows(observation_rows)
    mod = _modulus(modulus)
    dimension = len(rows[0])
    return integer_row_hermite_basis(
        rows + modulus_identity_rows(dimension, mod)
    )


def full_rank_lattice_index(basis_rows: Sequence[Sequence[int]]) -> int:
    basis = _rows(basis_rows)
    dimension = len(basis[0])
    profile = integer_smith_precision_profile(basis)
    if profile.rational_rank != dimension:
        raise ValueError("lattice basis must have full state rank")
    return profile.maximal_nonzero_determinantal_divisor


@dataclass(frozen=True)
class ModularActionClosureStep:
    horizon: int
    preimage_basis: Matrix
    state_kernel_size: int
    observable_phase_count: int


@dataclass(frozen=True)
class ModularActionClosureReport:
    modulus: int
    state_dimension: int
    initial_kernel_size: int
    arithmetic_refinement_budget: int
    exact_stabilization_horizon: int
    final_state_kernel_size: int
    final_observable_phase_count: int
    final_preimage_basis: Matrix
    steps: tuple[ModularActionClosureStep, ...]

    @property
    def modularly_injective(self) -> bool:
        return self.final_state_kernel_size == 1


def modular_action_closure_report(
    action_matrices: Sequence[Sequence[Sequence[int]]],
    observation_rows: Sequence[Sequence[int]],
    modulus: int,
) -> ModularActionClosureReport:
    rows = _rows(observation_rows)
    mod = _modulus(modulus)
    actions = tuple(tuple(tuple(row) for row in matrix) for matrix in action_matrices)
    if not actions:
        raise ValueError("at least one action matrix is required")
    dimension = len(rows[0])
    for action in actions:
        if len(action) != dimension or any(len(row) != dimension for row in action):
            raise ValueError("every action must be square on the state dimension")
        for row in action:
            for value in row:
                if isinstance(value, bool) or not isinstance(value, int):
                    raise TypeError("action entries must be integers")

    current = modular_preimage_lattice_basis(rows, mod)
    initial_index = full_rank_lattice_index(current)
    budget = prime_factor_multiplicity(initial_index)
    torus_size = mod ** dimension
    steps: list[ModularActionClosureStep] = []

    def record(horizon: int, basis: Matrix) -> int:
        index = full_rank_lattice_index(basis)
        if torus_size % index != 0:
            raise AssertionError("modular preimage index did not divide state torus")
        steps.append(
            ModularActionClosureStep(
                horizon=horizon,
                preimage_basis=basis,
                state_kernel_size=index,
                observable_phase_count=torus_size // index,
            )
        )
        return index

    current_index = record(0, current)
    horizon = 0
    strict_refinements = 0
    while True:
        nxt = action_module_closure_step(current, actions)
        next_index = full_rank_lattice_index(nxt)
        record(horizon + 1, nxt)

        if nxt == current:
            if strict_refinements > budget:
                raise AssertionError("modular closure exceeded arithmetic refinement budget")
            return ModularActionClosureReport(
                modulus=mod,
                state_dimension=dimension,
                initial_kernel_size=initial_index,
                arithmetic_refinement_budget=budget,
                exact_stabilization_horizon=horizon,
                final_state_kernel_size=current_index,
                final_observable_phase_count=torus_size // current_index,
                final_preimage_basis=current,
                steps=tuple(steps),
            )

        strict_refinements += 1
        if current_index % next_index != 0 or next_index >= current_index:
            raise AssertionError("strict modular lattice refinement did not lower index by division")
        if strict_refinements > budget:
            raise AssertionError("modular closure exceeded prime-factor index bound")
        horizon += 1
        current = nxt
        current_index = next_index
