"""Minimal orientation repair for one-sided absolute Barlow drift history.

A stacking word sigma_1,...,sigma_N in {−1,+1} generates signed prefix drift
``delta_k`` and absolute history ``d_k=|delta_k|``.  The absolute history is a
nonnegative nearest-neighbor walk. Its lost sign is not one independent bit per
layer: sign remains fixed throughout each nonzero excursion and becomes free
again only when the path leaves zero.

If the absolute history has e excursions, its microscopic fiber has exactly
2^e words. One orientation sign per excursion reconstructs the word exactly.
The number of absolute histories with e excursions also has a closed binomial
formula, giving the complete P011 fiber/collision spectrum of this quotient.
"""

from __future__ import annotations

from math import comb

StackingWord = tuple[int, ...]
AbsoluteHistory = tuple[int, ...]
FiberProfile = tuple[tuple[int, int], ...]


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


def _require_natural(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a non-negative integer")


def _require_positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


def signed_prefix_history(word: StackingWord) -> tuple[int, ...]:
    _require_word(word)
    total = 0
    output = []
    for sign in word:
        total += sign
        output.append(total)
    return tuple(output)


def absolute_prefix_history(word: StackingWord) -> AbsoluteHistory:
    return tuple(abs(value) for value in signed_prefix_history(word))


def excursion_count(history: AbsoluteHistory) -> int:
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
    return 2 ** excursion_count(history)


def reconstruct_word_from_excursion_orientations(
    history: AbsoluteHistory, orientations: tuple[int, ...]
) -> StackingWord:
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
    _require_natural("length", length)
    return comb(length, length // 2)


def maximum_excursion_count(length: int) -> int:
    _require_natural("length", length)
    return (length + 1) // 2


def maximum_orientation_fiber_size(length: int) -> int:
    return 2 ** maximum_excursion_count(length)


def absolute_history_count_with_excursions(length: int, excursions: int) -> int:
    """Number A_(N,e) of absolute histories with exactly e excursions."""
    _require_natural("length", length)
    _require_natural("excursions", excursions)
    if length == 0:
        return 1 if excursions == 0 else 0
    if excursions == 0 or excursions > maximum_excursion_count(length):
        return 0
    if length % 2:
        half = (length - 1) // 2
        return comb(2 * half + 1 - excursions, half + 1 - excursions)
    half = length // 2
    return 2 * comb(2 * half - excursions - 1, half - excursions)


def excursion_count_spectrum(length: int) -> tuple[tuple[int, int], ...]:
    _require_natural("length", length)
    if length == 0:
        return ((0, 1),)
    return tuple(
        (excursions, absolute_history_count_with_excursions(length, excursions))
        for excursions in range(1, maximum_excursion_count(length) + 1)
    )


def absolute_history_fiber_profile(length: int) -> FiberProfile:
    _require_natural("length", length)
    if length == 0:
        return ((1, 1),)
    return tuple(
        (2 ** excursions, count)
        for excursions, count in excursion_count_spectrum(length)
        if count
    )


def absolute_history_collision_count(length: int, order: int) -> int:
    _require_natural("length", length)
    _require_positive("order", order)
    return sum(
        history_count * comb(fiber_size, order)
        for fiber_size, history_count in absolute_history_fiber_profile(length)
        if fiber_size >= order
    )


def absolute_history_collision_polynomial_coefficients(length: int) -> tuple[int, ...]:
    maximum = maximum_orientation_fiber_size(length)
    return tuple(
        absolute_history_collision_count(length, order)
        for order in range(1, maximum + 1)
    )


def total_orientation_repair_bit_load(length: int) -> int:
    """Total excursion-orientation bits over all 2^N microscopic words.

    A new repair bit is required at step k exactly when the signed prefix before
    that step is zero.  Only even prefix lengths 2j can be zero.  Counting the
    balanced prefix and arbitrary suffix gives

        R_N = sum_{j=0}^{floor((N-1)/2)} C(2j,j) 2^(N-2j).

    Using ``sum_{j=0}^m C(2j,j)/4^j = (2m+1)C(2m,m)/4^m`` gives the exact
    integer closed form below.
    """
    _require_natural("length", length)
    if length == 0:
        return 0
    half_index = (length - 1) // 2
    return (
        2 ** (length - 2 * half_index)
        * (2 * half_index + 1)
        * comb(2 * half_index, half_index)
    )


def average_orientation_repair_load_fraction(length: int) -> tuple[int, int]:
    """Exact rational average ``R_N/2^N`` reduced only by powers of two."""
    _require_natural("length", length)
    if length == 0:
        return 0, 1
    numerator = total_orientation_repair_bit_load(length)
    denominator = 2 ** length
    while numerator % 2 == 0 and denominator % 2 == 0:
        numerator //= 2
        denominator //= 2
    return numerator, denominator
