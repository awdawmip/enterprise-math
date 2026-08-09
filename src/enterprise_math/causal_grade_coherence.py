"""Integer grade coherence for deterministic continuation-type composition.

A binary continuation-type join may carry an integer pair grade shift gamma.
Its three-body rebracketing defect is

    D3(a,b,c) = gamma(a,b) + gamma(a*b,c)
              - gamma(b,c) - gamma(a,b*c).

D3=0 is exact bracket-independent pair-grade coherence.  When D3 is nonzero it
can be read as the integer correction needed to transport between the two
three-body bracketings.  Because D3 is derived from one pair-grade assignment,
it automatically satisfies a four-body pentagon identity: the two finite paths
of rebracketing a four-block product have the same total correction.

An independently supplied three-body correction that violates this pentagon is
not sufficient to make four-block composition path-independent and therefore
requires additional higher compatibility data.

Base-B carry is a canonical D3=0 example.  Traditional cocycle/coboundary and
associator terminology is a mathematical shadow of these finite causal
rebracketing requirements rather than the ontology.
"""

from __future__ import annotations

from typing import Hashable

ContinuationType = Hashable
TypeOperation = dict[tuple[ContinuationType, ContinuationType], ContinuationType]
GradeShift = dict[tuple[ContinuationType, ContinuationType], int]
AssociatorGrade = dict[tuple[ContinuationType, ContinuationType, ContinuationType], int]


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
) -> AssociatorGrade:
    """Signed left-bracket minus right-bracket grade defect for each nonzero triple."""
    _validate(types, operation, grade_shift)
    defects: AssociatorGrade = {}
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


def derived_associator_grade(
    types: tuple[ContinuationType, ...],
    operation: TypeOperation,
    grade_shift: GradeShift,
) -> AssociatorGrade:
    """Total D3 table, including zero entries, derived from one pair-grade law."""
    _validate(types, operation, grade_shift)
    sparse = grade_associativity_defect(types, operation, grade_shift)
    return {
        (a, b, c): sparse.get((a, b, c), 0)
        for a in types
        for b in types
        for c in types
    }


def grade_shift_is_coherent(
    types: tuple[ContinuationType, ...],
    operation: TypeOperation,
    grade_shift: GradeShift,
) -> bool:
    return operation_is_associative(types, operation) and not grade_associativity_defect(
        types, operation, grade_shift
    )


def pentagon_defect(
    types: tuple[ContinuationType, ...],
    operation: TypeOperation,
    associator: AssociatorGrade,
) -> dict[tuple[ContinuationType, ContinuationType, ContinuationType, ContinuationType], int]:
    """Four-body path defect of a declared integer three-body rebracketing correction.

    For associative `*`, path independence between the two standard routes from
    `(((a*b)*c)*d)` to `a*(b*(c*d))` requires

        A(a,b,c) + A(a,b*c,d) + A(b,c,d)
      = A(a*b,c,d) + A(a,b,c*d).

    Nonzero results mean ternary correction data is still insufficient.
    """
    if not operation_is_associative(types, operation):
        raise ValueError("pentagon grade comparison requires associative type join")
    expected = {(a, b, c) for a in types for b in types for c in types}
    if set(associator) != expected:
        raise ValueError("associator must define every ordered type triple")
    if any(
        isinstance(value, bool) or not isinstance(value, int)
        for value in associator.values()
    ):
        raise ValueError("associator grades must be integers")

    result = {}
    for a in types:
        for b in types:
            for c in types:
                for d in types:
                    left_path = (
                        associator[(a, b, c)]
                        + associator[(a, operation[(b, c)], d)]
                        + associator[(b, c, d)]
                    )
                    right_path = (
                        associator[(operation[(a, b)], c, d)]
                        + associator[(a, b, operation[(c, d)])]
                    )
                    if left_path != right_path:
                        result[(a, b, c, d)] = left_path - right_path
    return result


def derived_associator_satisfies_pentagon(
    types: tuple[ContinuationType, ...],
    operation: TypeOperation,
    grade_shift: GradeShift,
) -> bool:
    if not operation_is_associative(types, operation):
        return False
    associator = derived_associator_grade(types, operation, grade_shift)
    return not pentagon_defect(types, operation, associator)


def regrade_pair_shift(
    types: tuple[ContinuationType, ...],
    operation: TypeOperation,
    grade_shift: GradeShift,
    type_baseline: dict[ContinuationType, int],
) -> GradeShift:
    """Change type-dependent grade baselines without changing D3."""
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
