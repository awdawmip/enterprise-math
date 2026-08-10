"""Modular future precision derived exactly from integer Smith factors.

Let an integer observation matrix ``O : Z^n -> Z^m`` have rational rank ``r``
and nonzero Smith invariant factors

    d_1 | d_2 | ... | d_r.

Reduce both state coordinates and observations modulo a positive integer ``M``.
On the finite state torus ``(Z/MZ)^n`` the induced homomorphism has

    |ker(O mod M)|
      = M^(n-r) * product_i gcd(d_i, M),

    |im(O mod M)|
      = product_i M / gcd(d_i, M).

Each hidden free integer direction contributes ``M`` invisible residues.  Each
Smith coordinate contributes ``gcd(d_i,M)`` kernel residues and therefore
``M/gcd(d_i,M)`` observable phases.

The scalar formula ``M/gcd(M,g)`` from earlier modular history/scheduler examples
is exactly the rank-one case.

Full integer injectivity does not imply modular injectivity: a nonunit Smith
factor can become invisible modulo a divisor.  Conversely a unimodular full-rank
observation (all Smith factors one) is injective modulo every positive M.

Smith normal form and finite abelian groups are standard prior mathematics.  The
project value is the exact bridge from integer future-observability precision to
finite modular phase counts.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import product
from math import gcd, prod
from typing import Sequence

from .integer_future_smith_precision import integer_smith_precision_profile


Matrix = tuple[tuple[int, ...], ...]
Vector = tuple[int, ...]


def _matrix(values: Sequence[Sequence[int]]) -> Matrix:
    rows = tuple(tuple(row) for row in values)
    if not rows:
        raise ValueError("observation matrix must contain at least one row")
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


def modular_observation_signature(
    observation_matrix: Sequence[Sequence[int]],
    state: Sequence[int],
    modulus: int,
) -> Vector:
    matrix = _matrix(observation_matrix)
    mod = _modulus(modulus)
    values = tuple(state)
    if len(values) != len(matrix[0]):
        raise ValueError("state dimension must match observation matrix")
    for value in values:
        if isinstance(value, bool) or not isinstance(value, int):
            raise TypeError("state entries must be integers")
    return tuple(
        sum(coefficient * value for coefficient, value in zip(row, values, strict=True)) % mod
        for row in matrix
    )


@dataclass(frozen=True)
class ModularSmithPrecisionReport:
    modulus: int
    state_dimension: int
    rational_rank: int
    hidden_free_rank: int
    smith_factors: tuple[int, ...]
    smith_kernel_residue_factors: tuple[int, ...]
    smith_observable_phase_factors: tuple[int, ...]
    kernel_size: int
    image_size: int
    state_torus_size: int

    @property
    def modularly_injective(self) -> bool:
        return self.kernel_size == 1

    @property
    def unimodular_integer_full_rank(self) -> bool:
        return (
            self.hidden_free_rank == 0
            and all(factor == 1 for factor in self.smith_factors)
        )


def modular_smith_precision_report(
    observation_matrix: Sequence[Sequence[int]],
    modulus: int,
) -> ModularSmithPrecisionReport:
    matrix = _matrix(observation_matrix)
    mod = _modulus(modulus)
    profile = integer_smith_precision_profile(matrix)
    factors = profile.smith_invariant_factors
    kernel_factors = tuple(gcd(factor, mod) for factor in factors)
    phase_factors = tuple(mod // value for value in kernel_factors)
    kernel_size = (mod ** profile.hidden_free_rank) * prod(kernel_factors)
    image_size = prod(phase_factors)
    torus_size = mod ** len(matrix[0])
    if kernel_size * image_size != torus_size:
        raise AssertionError("Smith modular kernel/image counting identity failed")
    return ModularSmithPrecisionReport(
        modulus=mod,
        state_dimension=len(matrix[0]),
        rational_rank=profile.rational_rank,
        hidden_free_rank=profile.hidden_free_rank,
        smith_factors=factors,
        smith_kernel_residue_factors=kernel_factors,
        smith_observable_phase_factors=phase_factors,
        kernel_size=kernel_size,
        image_size=image_size,
        state_torus_size=torus_size,
    )


def modular_state_partition(
    observation_matrix: Sequence[Sequence[int]],
    modulus: int,
) -> frozenset[frozenset[Vector]]:
    """Explicit finite torus partition for bounded oracle/regression use."""
    matrix = _matrix(observation_matrix)
    mod = _modulus(modulus)
    dimension = len(matrix[0])
    groups: dict[Vector, set[Vector]] = {}
    for state in product(range(mod), repeat=dimension):
        signature = modular_observation_signature(matrix, state, mod)
        groups.setdefault(signature, set()).add(tuple(state))
    return frozenset(frozenset(group) for group in groups.values())


def verify_modular_smith_count_by_enumeration(
    observation_matrix: Sequence[Sequence[int]],
    modulus: int,
) -> bool:
    report = modular_smith_precision_report(observation_matrix, modulus)
    partition = modular_state_partition(observation_matrix, modulus)
    if len(partition) != report.image_size:
        raise AssertionError("enumerated modular image count disagreed with Smith formula")
    block_sizes = {len(block) for block in partition}
    if block_sizes != {report.kernel_size}:
        raise AssertionError("modular homomorphism fibers did not have Smith kernel size")
    return True


def row_extension_modular_precision_refines(
    base_rows: Sequence[Sequence[int]],
    added_rows: Sequence[Sequence[int]],
    modulus: int,
) -> bool:
    base = _matrix(base_rows)
    added = tuple(tuple(row) for row in added_rows)
    if any(len(row) != len(base[0]) for row in added):
        raise ValueError("added rows must match base state dimension")
    extended = base + added
    base_report = modular_smith_precision_report(base, modulus)
    extended_report = modular_smith_precision_report(extended, modulus)
    if base_report.kernel_size % extended_report.kernel_size != 0:
        raise AssertionError("row extension failed modular kernel divisibility")
    if extended_report.image_size % base_report.image_size != 0:
        raise AssertionError("row extension failed modular image divisibility")
    return True
