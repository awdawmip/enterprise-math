"""Exact event-driven repair of a two-sided Barlow coordination history.

Whole-shell coordination history reconstructs at each radius the unordered pair
of one-sided absolute prefix drifts. To recover the ordered, signed two-sided
microscopic stacking window, two event types need bits:

1. every departure of one absolute channel from zero starts a new sign
   excursion and needs one orientation bit;
2. every split of an equal unordered pair {d,d} into {d-1,d+1} needs one bit
   saying which labelled side took the larger successor.

If E is the total zero-departure count and B the diagonal-split count, the exact
microscopic fiber size is 2^(E+B).  For every nonempty horizon N the repair
count lies sharply between 2 and N+1.
"""

from __future__ import annotations

from itertools import product
from math import comb

from .p022_barlow_excursion_repair import (
    AbsoluteHistory,
    StackingWord,
    absolute_prefix_history,
    reconstruct_word_from_excursion_orientations,
    total_orientation_repair_bit_load,
)

UnorderedPair = tuple[int, int]
PairHistory = tuple[UnorderedPair, ...]


def _normalize_pair(left: int, right: int) -> UnorderedPair:
    return (left, right) if left <= right else (right, left)


def _require_pair_history(history: PairHistory) -> None:
    if not isinstance(history, tuple):
        raise ValueError("pair history must be a tuple")
    previous = (0, 0)
    for pair in history:
        if (
            not isinstance(pair, tuple)
            or len(pair) != 2
            or pair[0] < 0
            or pair[1] < 0
            or pair[0] > pair[1]
        ):
            raise ValueError("pair history entries must be sorted non-negative pairs")
        left, right = previous
        a, b = pair
        legal = (
            abs(a - left) == 1 and abs(b - right) == 1
        ) or (
            abs(b - left) == 1 and abs(a - right) == 1
        )
        if not legal:
            raise ValueError("pair history has no legal two-channel ±1 transition")
        previous = pair


def unordered_absolute_pair_history(
    left_word: StackingWord, right_word: StackingWord
) -> PairHistory:
    if len(left_word) != len(right_word):
        raise ValueError("two-sided words must have equal length")
    left = absolute_prefix_history(left_word)
    right = absolute_prefix_history(right_word)
    return tuple(_normalize_pair(a, b) for a, b in zip(left, right, strict=True))


def total_zero_departure_events(history: PairHistory) -> int:
    _require_pair_history(history)
    previous = (0, 0)
    total = 0
    for current in history:
        total += int(previous[0] == 0) + int(previous[1] == 0)
        previous = current
    return total


def diagonal_split_count(history: PairHistory) -> int:
    _require_pair_history(history)
    previous = (0, 0)
    total = 0
    for current in history:
        if previous[0] == previous[1] and current[0] != current[1]:
            total += 1
        previous = current
    return total


def two_sided_repair_bit_count(history: PairHistory) -> int:
    return total_zero_departure_events(history) + diagonal_split_count(history)


def two_sided_microscopic_fiber_size(history: PairHistory) -> int:
    return 2 ** two_sided_repair_bit_count(history)


def minimum_two_sided_repair_bits(length: int) -> int:
    """Sharp lower bound: 0 for empty history, otherwise two initial signs."""
    if isinstance(length, bool) or not isinstance(length, int) or length < 0:
        raise ValueError("length must be non-negative")
    return 0 if length == 0 else 2


def maximum_two_sided_repair_bits(length: int) -> int:
    """Sharp upper bound ``N+1`` for nonempty horizons.

    A one-step repair cost can be two only when the previous unordered pair is
    (0,0). Every later return to (0,0) is preceded by a (1,1)->(0,0) step whose
    repair cost is zero, so each later excess +1 is paired with a preceding -1
    relative to the baseline one bit per step. The initial 0->(1,1) contributes
    the sole uncompensated extra bit. The alternating history
    (1,1),(0,2),(1,1),(0,2),... attains the bound.
    """
    if isinstance(length, bool) or not isinstance(length, int) or length < 0:
        raise ValueError("length must be non-negative")
    return 0 if length == 0 else length + 1


def ordered_absolute_history_realizations(history: PairHistory) -> tuple[
    tuple[AbsoluteHistory, AbsoluteHistory], ...
]:
    _require_pair_history(history)
    split_total = diagonal_split_count(history)
    realizations = set()

    for choices in product((0, 1), repeat=split_total):
        choice_index = 0
        previous_left = 0
        previous_right = 0
        left_history = []
        right_history = []

        for pair in history:
            a, b = pair
            candidates = []
            for current_left, current_right in ((a, b), (b, a)):
                if (
                    abs(current_left - previous_left) == 1
                    and abs(current_right - previous_right) == 1
                ):
                    candidates.append((current_left, current_right))
            candidates = list(dict.fromkeys(candidates))
            if len(candidates) == 1:
                current_left, current_right = candidates[0]
            elif len(candidates) == 2:
                current_left, current_right = candidates[choices[choice_index]]
                choice_index += 1
            else:
                raise AssertionError("legal pair history must have one or two labelled successors")

            left_history.append(current_left)
            right_history.append(current_right)
            previous_left = current_left
            previous_right = current_right

        if choice_index != split_total:
            raise AssertionError("every split bit must be consumed exactly once")
        realizations.add((tuple(left_history), tuple(right_history)))

    expected = 2 ** split_total
    if len(realizations) != expected:
        raise AssertionError("ordered absolute realization count must be 2^B")
    return tuple(sorted(realizations))


def microscopic_word_pair_realizations(history: PairHistory) -> tuple[
    tuple[StackingWord, StackingWord], ...
]:
    output = set()
    for left_history, right_history in ordered_absolute_history_realizations(history):
        from .p022_barlow_excursion_repair import excursion_count

        left_e = excursion_count(left_history)
        right_e = excursion_count(right_history)
        for left_orientation in product((-1, 1), repeat=left_e):
            left_word = reconstruct_word_from_excursion_orientations(
                left_history, tuple(left_orientation)
            )
            for right_orientation in product((-1, 1), repeat=right_e):
                right_word = reconstruct_word_from_excursion_orientations(
                    right_history, tuple(right_orientation)
                )
                output.add((left_word, right_word))

    expected = two_sided_microscopic_fiber_size(history)
    if len(output) != expected:
        raise AssertionError("full two-sided repair must produce exactly 2^(E+B) words")
    return tuple(sorted(output))


def total_diagonal_split_bit_load(length: int) -> int:
    """Total B-event load over all ``4^N`` ordered microscopic word pairs.

    At prefix time t>=1, a split can occur only when the two signed walks have
    equal nonzero absolute magnitude. The number of ordered length-t prefix
    pairs with equal nonzero absolute magnitude is

        2*C(2t,t) - 2*1_(t even)*C(t,t/2)^2.

    Exactly two of the four next step pairs split the absolute magnitudes. The
    suffix is arbitrary. This yields the finite integer sum below.
    """
    if isinstance(length, bool) or not isinstance(length, int) or length < 0:
        raise ValueError("length must be non-negative")
    total = 0
    for time in range(1, length):
        zero_overlap = comb(time, time // 2) ** 2 if time % 2 == 0 else 0
        total += (
            comb(2 * time, time) - zero_overlap
        ) * (4 ** (length - time))
    return total


def total_two_sided_repair_bit_load(length: int) -> int:
    """Total ``E+B`` over all ordered microscopic two-sided windows."""
    if isinstance(length, bool) or not isinstance(length, int) or length < 0:
        raise ValueError("length must be non-negative")
    # Each one-sided word's excursion count is repeated against 2^N choices on
    # the other side, and there are two labelled sides.
    excursion_load = (2 ** (length + 1)) * total_orientation_repair_bit_load(length)
    return excursion_load + total_diagonal_split_bit_load(length)
