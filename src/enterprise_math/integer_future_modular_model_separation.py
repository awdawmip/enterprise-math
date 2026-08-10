"""Modular precision region separating two integer observation maps.

Let two integer observation matrices have the same shape and define their
difference matrix ``Delta=O_left-O_right``.  Let

    g = gcd(all entries of Delta),

with ``g=0`` exactly when the matrices are identical.

For any positive modulus M,

    O_left == O_right (mod M) entrywise
      iff M divides g.

Because equality of the matrices modulo M is equivalent to equality of their
modular outputs for **every** state, the complete modular indistinguishability
region is the principal divisor down-set

    { M>0 : M | g }.

If ``g>0``, the first prime-power precision that distinguishes the maps along the
p-adic ladder is

    p^(v_p(g)+1).

Equivalently the first distinguishing exponent is ``v_p(g)+1``.  If ``g=0``, no
modular precision can distinguish the identical maps.

This turns model separation into an exact object in the modular divisibility
precision lattice.  The free-versus-deep-torsion no-go is the special case whose
difference content is the chosen finite torsion depth D.

GCD content and modular congruence are standard prior arithmetic.  The project
value is the precision-region interpretation.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import gcd
from typing import Sequence

from .integer_future_modular_precision import modular_observation_signature
from .integer_future_padic_precision import p_adic_valuation


Matrix = tuple[tuple[int, ...], ...]
Vector = tuple[int, ...]


def _matrix(values: Sequence[Sequence[int]], *, name: str) -> Matrix:
    rows = tuple(tuple(row) for row in values)
    if not rows:
        raise ValueError(f"{name} must contain at least one row")
    width = len(rows[0])
    if width == 0 or any(len(row) != width for row in rows):
        raise ValueError(f"{name} rows must have one common positive width")
    for row in rows:
        for value in row:
            if isinstance(value, bool) or not isinstance(value, int):
                raise TypeError(f"{name} entries must be integers")
    return rows


def observation_difference_matrix(
    left: Sequence[Sequence[int]],
    right: Sequence[Sequence[int]],
) -> Matrix:
    left_matrix = _matrix(left, name="left")
    right_matrix = _matrix(right, name="right")
    if len(left_matrix) != len(right_matrix) or len(left_matrix[0]) != len(right_matrix[0]):
        raise ValueError("observation matrices must have the same shape")
    return tuple(
        tuple(a - b for a, b in zip(left_row, right_row, strict=True))
        for left_row, right_row in zip(left_matrix, right_matrix, strict=True)
    )


def integer_matrix_content(matrix: Sequence[Sequence[int]]) -> int:
    values = _matrix(matrix, name="matrix")
    content = 0
    for row in values:
        for value in row:
            content = gcd(content, abs(value))
    return content


def observation_model_difference_content(
    left: Sequence[Sequence[int]],
    right: Sequence[Sequence[int]],
) -> int:
    return integer_matrix_content(observation_difference_matrix(left, right))


def models_indistinguishable_modulus(
    left: Sequence[Sequence[int]],
    right: Sequence[Sequence[int]],
    modulus: int,
) -> bool:
    if isinstance(modulus, bool) or not isinstance(modulus, int):
        raise TypeError("modulus must be an integer")
    if modulus <= 0:
        raise ValueError("modulus must be positive")
    content = observation_model_difference_content(left, right)
    return content == 0 or content % modulus == 0


def first_distinguishing_prime_power_exponent(
    left: Sequence[Sequence[int]],
    right: Sequence[Sequence[int]],
    prime: int,
) -> int | None:
    content = observation_model_difference_content(left, right)
    if content == 0:
        # Still validate the requested prime.
        p_adic_valuation(1, prime)
        return None
    return p_adic_valuation(content, prime) + 1


def first_distinguishing_prime_power_modulus(
    left: Sequence[Sequence[int]],
    right: Sequence[Sequence[int]],
    prime: int,
) -> int | None:
    exponent = first_distinguishing_prime_power_exponent(left, right, prime)
    if exponent is None:
        return None
    return prime ** exponent


def modular_separating_state_witness(
    left: Sequence[Sequence[int]],
    right: Sequence[Sequence[int]],
    modulus: int,
) -> Vector | None:
    """Return one unit-coordinate state separating the maps modulo M, if any."""
    left_matrix = _matrix(left, name="left")
    right_matrix = _matrix(right, name="right")
    if len(left_matrix) != len(right_matrix) or len(left_matrix[0]) != len(right_matrix[0]):
        raise ValueError("observation matrices must have the same shape")
    if isinstance(modulus, bool) or not isinstance(modulus, int):
        raise TypeError("modulus must be an integer")
    if modulus <= 0:
        raise ValueError("modulus must be positive")
    dimension = len(left_matrix[0])
    for column in range(dimension):
        state = tuple(int(index == column) for index in range(dimension))
        if modular_observation_signature(left_matrix, state, modulus) != modular_observation_signature(right_matrix, state, modulus):
            return state
    return None


@dataclass(frozen=True)
class ModularModelSeparationReport:
    difference_content: int
    identical_over_integers: bool
    tested_moduli: tuple[int, ...]
    indistinguishable_tested_moduli: tuple[int, ...]
    distinguishing_tested_moduli: tuple[int, ...]

    @property
    def all_tested_moduli_indistinguishable(self) -> bool:
        return not self.distinguishing_tested_moduli


def modular_model_separation_report(
    left: Sequence[Sequence[int]],
    right: Sequence[Sequence[int]],
    tested_moduli: Sequence[int],
) -> ModularModelSeparationReport:
    moduli = tuple(tested_moduli)
    if not moduli:
        raise ValueError("tested_moduli must be nonempty")
    indistinguishable = []
    distinguishing = []
    for modulus in moduli:
        if models_indistinguishable_modulus(left, right, modulus):
            indistinguishable.append(modulus)
            if modular_separating_state_witness(left, right, modulus) is not None:
                raise AssertionError("indistinguishable modulus had a separating state")
        else:
            distinguishing.append(modulus)
            if modular_separating_state_witness(left, right, modulus) is None:
                raise AssertionError("distinguishing modulus lacked a unit-state witness")
    content = observation_model_difference_content(left, right)
    return ModularModelSeparationReport(
        difference_content=content,
        identical_over_integers=(content == 0),
        tested_moduli=moduli,
        indistinguishable_tested_moduli=tuple(indistinguishable),
        distinguishing_tested_moduli=tuple(distinguishing),
    )
