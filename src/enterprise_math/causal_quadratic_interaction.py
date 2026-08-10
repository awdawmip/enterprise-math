"""Quadratic geometry as an exact 2-body LEGO response.

Let every primitive move carry the same unit self-grade L and let B(u,v) be an
integer pair grade that has already been justified as a shadow of the declared
causal pair language.  For a finite primitive-move word W define

    Q(W) = |W| L + 2 sum_{i<j} B(w_i,w_j).

This is not an approximation: it is the exact order-two LEGO interaction
response.  Concatenating two words A,B gives

    Q(A+B) = Q(A)+Q(B)+2 Cross(A,B).

Thus a Pythagorean-style additivity theorem is exactly the zero cross-interaction
regime.  No angle or inner product is primitive in this construction; if B is
rendered as a traditional inner-product shadow then the familiar quadratic law
is recovered afterwards.
"""

from __future__ import annotations

from typing import Callable, Hashable

Primitive = Hashable
PairGrade = Callable[[Primitive, Primitive], int]


def quadratic_interaction_response(
    word: tuple[Primitive, ...],
    unit_grade: int,
    pair_grade: PairGrade,
) -> int:
    if isinstance(unit_grade, bool) or not isinstance(unit_grade, int):
        raise ValueError("unit_grade must be an integer")
    total = len(word) * unit_grade
    for index, left in enumerate(word):
        for right in word[index + 1 :]:
            total += 2 * pair_grade(left, right)
    return total


def cross_pair_interaction(
    left_word: tuple[Primitive, ...],
    right_word: tuple[Primitive, ...],
    pair_grade: PairGrade,
) -> int:
    return sum(pair_grade(left, right) for left in left_word for right in right_word)


def merge_quadratic_identity(
    left_word: tuple[Primitive, ...],
    right_word: tuple[Primitive, ...],
    unit_grade: int,
    pair_grade: PairGrade,
) -> bool:
    left = quadratic_interaction_response(left_word, unit_grade, pair_grade)
    right = quadratic_interaction_response(right_word, unit_grade, pair_grade)
    merged = quadratic_interaction_response(left_word + right_word, unit_grade, pair_grade)
    return merged == left + right + 2 * cross_pair_interaction(left_word, right_word, pair_grade)


def pythagorean_shadow_holds(
    left_word: tuple[Primitive, ...],
    right_word: tuple[Primitive, ...],
    unit_grade: int,
    pair_grade: PairGrade,
) -> bool:
    return (
        cross_pair_interaction(left_word, right_word, pair_grade) == 0
        and quadratic_interaction_response(left_word + right_word, unit_grade, pair_grade)
        == quadratic_interaction_response(left_word, unit_grade, pair_grade)
        + quadratic_interaction_response(right_word, unit_grade, pair_grade)
    )
