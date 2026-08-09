"""Integer grade coherence for deterministic continuation-type composition.

Let `star(a,b)` be an associative continuation-type join and let gamma(a,b) be
the integer grade shift produced by one binary join.  Pairwise grade data can
generate an arbitrary-dimensional grade without parenthesization ambiguity
exactly when

    gamma(a,b) + gamma(star(a,b),c)
  = gamma(b,c) + gamma(a,star(b,c))

for every triple.  The difference is an exact three-body grade compatibility
defect.

Base-B carry is a canonical causal example.  Residue types join by addition mod
B and the local grade shift floor((a+b)/B) is coherent because the represented
integer total is always

    residue + B * accumulated_carry.

Traditional cocycle/coboundary terminology, when used, is a mathematical shadow
of this bracket-independence requirement rather than the ontology.
"""

from __future__ import annotations

from typing import Hashable

ContinuationType = Hashable
TypeOperation = dict[tuple[ContinuationType, ContinuationType], ContinuationType]
GradeShift = dict[tuple[ContinuationType, ContinuationType], int]


def _validate(
    types: tuple[ContinuationType, ...],
    operation: TypeOperation,
    grade_shift: GradeShift,
) -> None:
    if not isinstance(types, tuple) or not types or len(set(types)) != len(types):
        raise ValueError("types must be a non-empty tuple of unique labels")
    expected = {(left, right) for left in types for right in types}
    if set(operation) != expected or set(grade_shift) != expected:
        raise ValueError("operation and grade_shift must define every ordered type pair")
    if not set(operation.values()) <= set(types):
        raise ValueError("operation outputs must be declared types")
    if any(
        isinstance(value, bool) or not isinstance(value, int)
        for value in grade_shift.values()
    ):
        raise ValueError("grade shifts must be integers")


def operation_is_associative(
    types: tuple[ContinuationType, ...],
    operation: TypeOperation,
) -> bool:
    expected = {(left, right) for left in types for right in types}
    if set(operation) != expected:
        raise ValueError("operation must define every ordered type pair")
    for first in types:
        for second in types:
            for third in types:
                if operation[(operation[(first, second)], third)] != operation[
                    (first, operation[(second, third)])
                ]:
                    return False
    return True


def grade_associativity_defect(
    types: tuple[ContinuationType, ...],
    operation: TypeOperation,
    grade_shift: GradeShift,
) -> dict[tuple[ContinuationType, ContinuationType, ContinuationType], int]:
    """Signed left-bracket minus right-bracket grade defect for each triple."""
    _validate(types, operation, grade_shift)
    defects = {}
    for first in types:
        for second in types:
            for third in types:
                left = (
                    grade_shift[(first, second)]
                    + grade_shift[(operation[(first, second)], third)]
                )
                right = (
                    grade_shift[(second, third)]
                    + grade_shift[(first, operation[(second, third)])]
                )
                if left != right:
                    defects[(first, second, third)] = left - right
    return defects


def grade_shift_is_coherent(
    types: tuple[ContinuationType, ...],
    operation: TypeOperation,
    grade_shift: GradeShift,
) -> bool:
    return operation_is_associative(types, operation) and not grade_associativity_defect(
        types, operation, grade_shift
    )


def regrade_pair_shift(
    types: tuple[ContinuationType, ...],
    operation: TypeOperation,
    grade_shift: GradeShift,
    type_baseline: dict[ContinuationType, int],
) -> GradeShift:
    """Change type-dependent grade baselines without changing coherence defect.

    If stored grade is replaced by `grade + h(type)`, the pair shift becomes

        gamma'(a,b)=gamma(a,b)+h(a*b)-h(a)-h(b).
    """
    _validate(types, operation, grade_shift)
    if set(type_baseline) != set(types):
        raise ValueError("type_baseline must define every type")
    if any(
        isinstance(value, bool) or not isinstance(value, int)
        for value in type_baseline.values()
    ):
        raise ValueError("type baselines must be integers")
    return {
        (left, right): (
            grade_shift[(left, right)]
            + type_baseline[operation[(left, right)]]
            - type_baseline[left]
            - type_baseline[right]
        )
        for left in types
        for right in types
    }


def base_carry_law(base: int) -> tuple[tuple[int, ...], TypeOperation, GradeShift]:
    """Residue join and local carry grade for ordinary base-B integer addition."""
    if isinstance(base, bool) or not isinstance(base, int) or base < 2:
        raise ValueError("base must be an integer at least two")
    types = tuple(range(base))
    operation = {
        (left, right): (left + right) % base
        for left in types
        for right in types
    }
    grade_shift = {
        (left, right): (left + right) // base
        for left in types
        for right in types
    }
    return types, operation, grade_shift


def fold_residues_and_carry(values: tuple[int, ...], base: int) -> tuple[int, int]:
    """Left-fold base-B residues into `(residue, accumulated_carry)`.

    Inputs are base-B residue digits.  The represented integer sum is exactly
    `residue + base*carry`.
    """
    types, operation, grade_shift = base_carry_law(base)
    if not isinstance(values, tuple) or not values:
        raise ValueError("values must be a non-empty tuple")
    if any(value not in types for value in values):
        raise ValueError("every value must be a valid residue")
    residue = values[0]
    carry = 0
    for value in values[1:]:
        carry += grade_shift[(residue, value)]
        residue = operation[(residue, value)]
    return residue, carry
