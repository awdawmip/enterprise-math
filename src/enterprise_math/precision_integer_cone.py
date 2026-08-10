"""Integer-cone separation certificates for fractionless R004 constraints.

A finite rational mixture of deterministic atoms can be denominator-cleared to
non-negative integer multiplicities.  Therefore a linear functional that is
non-positive on every integer generator but positive on a target is already an
exact impossibility certificate; no normalized probability coordinate is
required.

This is elementary linear/convex/semigroup mathematics.  R004 uses it as a
common integer interface for its Bell and future finite-constraint work.
"""
from __future__ import annotations

from collections.abc import Sequence

from enterprise_math.precision_count_defect import (
    binary_correlation_numerator,
    r004_bell_target_count_tables,
)
from enterprise_math.precision_locality_obstruction import local_response_tables

IntegerWord = tuple[int, ...]


def integer_dot(functional: Sequence[int], state: Sequence[int]) -> int:
    coefficients = tuple(functional)
    values = tuple(state)
    if not coefficients or len(coefficients) != len(values):
        raise ValueError("functional and state must have the same nonzero width")
    if any(isinstance(value, bool) or not isinstance(value, int) for value in coefficients + values):
        raise ValueError("integer cone words require integers")
    return sum(coefficient * value for coefficient, value in zip(coefficients, values))


def cone_separation_certificate_holds(
    generators: Sequence[Sequence[int]],
    target: Sequence[int],
    functional: Sequence[int],
) -> bool:
    """Check h(g)<=0 for every generator and h(target)>0."""
    atoms = tuple(tuple(generator) for generator in generators)
    if not atoms:
        raise ValueError("at least one generator is required")
    target_word = tuple(target)
    coefficients = tuple(functional)
    width = len(target_word)
    if width == 0 or len(coefficients) != width or any(len(atom) != width for atom in atoms):
        raise ValueError("all cone words must have common nonzero width")
    return (
        all(integer_dot(coefficients, atom) <= 0 for atom in atoms)
        and integer_dot(coefficients, target_word) > 0
    )


def generator_combination(
    generators: Sequence[Sequence[int]], weights: Sequence[int]
) -> IntegerWord:
    """Non-negative integer combination of fixed-width generators."""
    atoms = tuple(tuple(generator) for generator in generators)
    row = tuple(weights)
    if not atoms or len(atoms) != len(row):
        raise ValueError("one weight is required per nonempty generator family")
    width = len(atoms[0])
    if width == 0 or any(len(atom) != width for atom in atoms):
        raise ValueError("generators must have common nonzero width")
    if any(isinstance(weight, bool) or not isinstance(weight, int) or weight < 0 for weight in row):
        raise ValueError("generator weights must be non-negative integers")
    return tuple(
        sum(weight * atom[index] for weight, atom in zip(row, atoms))
        for index in range(width)
    )


def functional_nonpositive_on_cone(
    generators: Sequence[Sequence[int]],
    weights: Sequence[int],
    functional: Sequence[int],
) -> bool:
    """Executable monoid consequence of a generatorwise linear inequality."""
    atoms = tuple(tuple(generator) for generator in generators)
    if not all(integer_dot(functional, atom) <= 0 for atom in atoms):
        return False
    combined = generator_combination(atoms, weights)
    return integer_dot(functional, combined) <= 0


def r004_local_bell_generators() -> tuple[IntegerWord, ...]:
    """Five-coordinate local deterministic correlation/count atoms."""
    output: list[IntegerWord] = []
    for a0, a1, b0, b1 in local_response_tables():
        output.append((a0 * b0, a0 * b1, a1 * b0, a1 * b1, 1))
    return tuple(output)


def r004_bell_target_word() -> IntegerWord:
    tables = r004_bell_target_count_tables()
    numerators = []
    totals = set()
    for setting in ((0, 0), (0, 1), (1, 0), (1, 1)):
        numerator, total = binary_correlation_numerator(tables[setting])
        numerators.append(numerator)
        totals.add(total)
    if len(totals) != 1:
        raise AssertionError("R004 target uses one common setting mass")
    return (*numerators, next(iter(totals)))


def r004_bell_separating_functional() -> IntegerWord:
    """One CHSH orientation as a pure integer dual word."""
    return (-1, -1, -1, 1, -2)


def r004_bell_integer_certificate_defect() -> int:
    generators = r004_local_bell_generators()
    target = r004_bell_target_word()
    functional = r004_bell_separating_functional()
    if not cone_separation_certificate_holds(generators, target, functional):
        raise AssertionError("declared CHSH integer certificate must separate the target")
    return integer_dot(functional, target)
