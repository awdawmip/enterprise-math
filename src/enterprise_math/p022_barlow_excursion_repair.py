"""Minimal orientation repair for one-sided absolute Barlow drift history.

A stacking word sigma_1,...,sigma_N in {−1,+1} generates signed prefix drift
``delta_k`` and absolute history ``d_k=|delta_k|``.  The absolute history is a
nonnegative nearest-neighbor walk.  Its lost sign is not one independent bit
per layer: sign remains fixed throughout each nonzero excursion and becomes
free again only when the path leaves zero.

If the absolute history has e excursions, its microscopic fiber has exactly
2^e words.  One orientation sign per excursion reconstructs the word exactly.
"""

from __future__ import annotations

from math import comb

StackingWord = tuple[int, ...]
AbsoluteHistory = tuple[int, ...]


def _require_word(word: StackingWord) -> None:
    if not isinstance(word, tuple) or any(sign not in (-1, 1) for sign in word):
        raise ValueError("word must be a tuple of -1/+1 signs")


def _require_absolute_history(history: AbsoluteHistory) -> None:
    if not isinstance(history, tuple) or any(
        isinstance(value, bool) or not isinstance(value, int) or value < 0
        for value in history
    ):
        raise ValueError("absolute history must be a tuple of non-negative integers")
    previous = 0
    for current in history:
        if abs(current - previous) != 1:
            raise ValueError("absolute history must move by exactly one per step")
        previous = current


def signed_prefix_history(word: StackingWord) -> tuple[int, ...]:
    _require_word(word)
    total = 0
    output = []
    for sign in word:
        total += sign
        output.append(total)
    return tuple(output)


def absolute_prefix_history(word: StackingWord) -> AbsoluteHistory:
    """Return ``(|delta_1|,...,|delta_N|)``."""
    return tuple(abs(value) for value in signed_prefix_history(word))


def excursion_count(history: AbsoluteHistory) -> int:
    """Number of departures ``0 -> 1`` in the absolute drift path."""
    _require_absolute_history(history)
    previous = 0
    count = 0
    for current in history:
        if previous == 0:
            if current != 1:
                raise AssertionError("a legal departure from zero must reach one")
            count += 1
        previous = current
    return count


def orientation_fiber_size(history: AbsoluteHistory) -> int:
    """Number of microscopic ±1 words represented by one absolute history."""
    return 2 ** excursion_count(history)


def reconstruct_word_from_excursion_orientations(
    history: AbsoluteHistory, orientations: tuple[int, ...]
) -> StackingWord:
    """Recover the unique stacking word for one orientation sign per excursion."""
    _require_absolute_history(history)
    expected = excursion_count(history)
    if (
        not isinstance(orientations, tuple)
        or len(orientations) != expected
        or any(sign not in (-1, 1) for sign in orientations)
    ):
        raise ValueError("orientations must supply one -1/+1 sign per excursion")

    previous_absolute = 0
    previous_signed = 0
    active_orientation = 0
    orientation_index = 0
    word = []

    for current_absolute in history:
        if previous_absolute == 0:
            active_orientation = orientations[orientation_index]
            orientation_index += 1
        current_signed = active_orientation * current_absolute if current_absolute else 0
        step = current_signed - previous_signed
        if step not in (-1, 1):
            raise AssertionError("excursion orientation must reconstruct a ±1 step")
        word.append(step)
        previous_absolute = current_absolute
        previous_signed = current_signed
        if current_absolute == 0:
            active_orientation = 0

    return tuple(word)


def absolute_history_image_size(length: int) -> int:
    """Number of legal one-sided absolute histories of length ``length``.

    These are nonnegative ±1 prefixes (Dyck prefixes).  The classical reflection
    count is ``C(length,floor(length/2))``.
    """
    if isinstance(length, bool) or not isinstance(length, int) or length < 0:
        raise ValueError("length must be non-negative")
    return comb(length, length // 2)


def maximum_excursion_count(length: int) -> int:
    """Largest possible number of independent orientation decisions."""
    if isinstance(length, bool) or not isinstance(length, int) or length < 0:
        raise ValueError("length must be non-negative")
    return (length + 1) // 2


def maximum_orientation_fiber_size(length: int) -> int:
    return 2 ** maximum_excursion_count(length)
