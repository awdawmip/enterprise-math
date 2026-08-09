"""Exact event-driven repair of a two-sided Barlow coordination history.

Whole-shell coordination history reconstructs at each radius the unordered pair
of one-sided absolute prefix drifts.  To recover the ordered, signed two-sided
microscopic stacking window, two independent event types need bits:

1. every departure of one absolute channel from zero starts a new sign
   excursion and needs one orientation bit;
2. every split of an equal unordered pair {d,d} into {d-1,d+1} needs one bit
   saying which labelled side took the larger successor.

If E is the total zero-departure count and B the diagonal-split count, the exact
microscopic fiber size is 2^(E+B).
"""

from __future__ import annotations

from itertools import product

from .p022_barlow_excursion_repair import (
    AbsoluteHistory,
    StackingWord,
    absolute_prefix_history,
    reconstruct_word_from_excursion_orientations,
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
        # A legal ordered realization changes each component by one; test that
        # at least one matching between previous and current has this property.
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
    """Unordered absolute two-channel history of two equal-length words."""
    if len(left_word) != len(right_word):
        raise ValueError("two-sided words must have equal length")
    left = absolute_prefix_history(left_word)
    right = absolute_prefix_history(right_word)
    return tuple(_normalize_pair(a, b) for a, b in zip(left, right, strict=True))


def total_zero_departure_events(history: PairHistory) -> int:
    """Total one-sided excursion starts, computable without side labels."""
    _require_pair_history(history)
    previous = (0, 0)
    total = 0
    for current in history:
        total += int(previous[0] == 0) + int(previous[1] == 0)
        previous = current
    return total


def diagonal_split_count(history: PairHistory) -> int:
    """Number of equal-pair states that split into unequal successors."""
    _require_pair_history(history)
    previous = (0, 0)
    total = 0
    for current in history:
        if previous[0] == previous[1] and current[0] != current[1]:
            total += 1
        previous = current
    return total


def two_sided_repair_bit_count(history: PairHistory) -> int:
    """Minimal event-bit count E+B for exact ordered signed reconstruction."""
    return total_zero_departure_events(history) + diagonal_split_count(history)


def two_sided_microscopic_fiber_size(history: PairHistory) -> int:
    """Exact number of ordered signed word pairs mapping to one pair history."""
    return 2 ** two_sided_repair_bit_count(history)


def ordered_absolute_history_realizations(history: PairHistory) -> tuple[
    tuple[AbsoluteHistory, AbsoluteHistory], ...
]:
    """Enumerate ordered absolute-channel histories using one bit per split.

    This is an executable reconstruction oracle.  The theorem-level count is
    ``2^B``; enumeration is used only for finite regression and exact repair.
    """
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
                # A genuine ambiguity can occur only when the previous pair is
                # equal and the current pair is split.
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
    """Enumerate all ordered signed microscopic two-sided word pairs."""
    output = set()
    for left_history, right_history in ordered_absolute_history_realizations(history):
        # For one fixed labelled absolute realization, each excursion gets one
        # independent sign.  Generate the exact orientation words by trying the
        # required number of signs for each side.
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
