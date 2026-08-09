"""Finite behavioral quotient of E001 material operator words.

At a fixed amplitude A, an operator word is observable through the finite
function it induces on ``{0,...,A}``.  Distinct syntactic words may induce the
same function and are then exactly interchangeable for any further composition
built from the same deterministic finite operators.

This is an E001 application of future/behavioral quotient reasoning, not a new
general semigroup theorem.
"""

from __future__ import annotations

from dataclasses import dataclass

from .material_program import MaterialOperator, apply_material_word

MaterialWord = tuple[MaterialOperator, ...]
MaterialSignature = tuple[int, ...]


@dataclass(frozen=True)
class MaterialWordBehavior:
    """One ordered word together with its full finite-chain function table."""

    amplitude: int
    word: MaterialWord
    signature: MaterialSignature


def material_word_signature(
    amplitude: int,
    word: MaterialWord | list[MaterialOperator],
) -> MaterialSignature:
    """Return the complete induced function table on ``0..amplitude``."""
    if isinstance(amplitude, bool) or not isinstance(amplitude, int) or amplitude <= 0:
        raise ValueError("amplitude must be a positive integer")
    operators = tuple(word)
    return tuple(
        apply_material_word(sample, amplitude, operators).result
        for sample in range(amplitude + 1)
    )


def material_word_behavior(
    amplitude: int,
    word: MaterialWord | list[MaterialOperator],
) -> MaterialWordBehavior:
    operators = tuple(word)
    return MaterialWordBehavior(
        amplitude=amplitude,
        word=operators,
        signature=material_word_signature(amplitude, operators),
    )


def material_words_equivalent(
    amplitude: int,
    left: MaterialWord | list[MaterialOperator],
    right: MaterialWord | list[MaterialOperator],
) -> bool:
    """Exact extensional equality of two material programs at one finite scale."""
    return material_word_signature(amplitude, left) == material_word_signature(
        amplitude, right
    )


def compose_material_words(
    first: MaterialWord | list[MaterialOperator],
    second: MaterialWord | list[MaterialOperator],
) -> MaterialWord:
    """Return the word for applying ``first`` and then ``second``."""
    return tuple(first) + tuple(second)


def verify_equivalence_congruence(
    amplitude: int,
    left: MaterialWord | list[MaterialOperator],
    right: MaterialWord | list[MaterialOperator],
    context_before: MaterialWord | list[MaterialOperator] = (),
    context_after: MaterialWord | list[MaterialOperator] = (),
) -> bool:
    """Verify that one known extensional equality survives a word context."""
    if not material_words_equivalent(amplitude, left, right):
        raise ValueError("left and right words are not equivalent at this amplitude")
    left_context = compose_material_words(
        compose_material_words(context_before, left), context_after
    )
    right_context = compose_material_words(
        compose_material_words(context_before, right), context_after
    )
    equivalent = material_words_equivalent(
        amplitude, left_context, right_context
    )
    if not equivalent:
        raise AssertionError("extensional material-word equality failed congruence")
    return True
