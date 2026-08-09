"""Exact fiber/collision structure of selected-layer Barlow precision.

A length-N stacking prefix is a word in {−1,+1}^N.  If the future language
observes only prefix imbalances at selected layers, the word decomposes into
independent ±1 segments.  Fiber cardinalities are products of binomial
coefficients, and the total equal-observation pair count factors into central
binomial coefficients.

This is a concrete P022 specialization of the P011 finite fiber/collision
spectrum and the P023/P024 task-relative quotient principle.
"""

from __future__ import annotations

from math import comb

StackingWord = tuple[int, ...]


def _require_length(length: int) -> None:
    if isinstance(length, bool) or not isinstance(length, int) or length < 0:
        raise ValueError("length must be a non-negative integer")


def _require_word(word: StackingWord) -> None:
    if not isinstance(word, tuple):
        raise ValueError("word must be a tuple")
    if any(sign not in (-1, 1) for sign in word):
        raise ValueError("word entries must be -1 or +1")


def _require_selected_layers(length: int, selected_layers: tuple[int, ...]) -> None:
    _require_length(length)
    if not isinstance(selected_layers, tuple):
        raise ValueError("selected_layers must be a tuple")
    if any(
        isinstance(layer, bool)
        or not isinstance(layer, int)
        or layer <= 0
        or layer > length
        for layer in selected_layers
    ):
        raise ValueError("selected layers must lie in 1..length")
    if tuple(sorted(set(selected_layers))) != selected_layers:
        raise ValueError("selected layers must be strictly increasing")


def stacking_word_imbalance(word: StackingWord) -> int:
    _require_word(word)
    return sum(word)


def imbalance_fiber_size(length: int, imbalance: int) -> int:
    """Number of ±1 words of one length having one prescribed net imbalance."""
    _require_length(length)
    if isinstance(imbalance, bool) or not isinstance(imbalance, int):
        raise ValueError("imbalance must be an integer")
    if abs(imbalance) > length or (length + imbalance) % 2:
        return 0
    plus_count = (length + imbalance) // 2
    return comb(length, plus_count)


def imbalance_fiber_spectrum(length: int) -> tuple[tuple[int, int], ...]:
    """Return ``(imbalance, fiber_size)`` for the final-layer quotient."""
    _require_length(length)
    return tuple(
        (imbalance, imbalance_fiber_size(length, imbalance))
        for imbalance in range(-length, length + 1, 2)
    )


def selected_layer_observation(
    word: StackingWord, selected_layers: tuple[int, ...]
) -> tuple[int, ...]:
    """Prefix imbalance vector at the declared queried layers."""
    _require_word(word)
    _require_selected_layers(len(word), selected_layers)
    output = []
    running = 0
    selected = set(selected_layers)
    for index, sign in enumerate(word, start=1):
        running += sign
        if index in selected:
            output.append(running)
    return tuple(output)


def selected_segment_lengths(
    length: int, selected_layers: tuple[int, ...]
) -> tuple[tuple[int, ...], int]:
    """Return constrained segment lengths and the final unobserved tail length."""
    _require_selected_layers(length, selected_layers)
    if not selected_layers:
        return (), length
    previous = 0
    segments = []
    for layer in selected_layers:
        segments.append(layer - previous)
        previous = layer
    return tuple(segments), length - previous


def selected_observation_image_size(
    length: int, selected_layers: tuple[int, ...]
) -> int:
    """Number of represented prefix-imbalance trajectories.

    A segment of length ell has exactly ell+1 possible net imbalances. Segment
    increments are independent, while the unobserved tail contributes no new
    observation coordinate.
    """
    segments, _ = selected_segment_lengths(length, selected_layers)
    result = 1
    for segment in segments:
        result *= segment + 1
    return result


def selected_observation_fiber_size(
    length: int,
    selected_layers: tuple[int, ...],
    observed_imbalances: tuple[int, ...],
) -> int:
    """Exact microscopic word count in one selected-layer observation fiber."""
    segments, tail = selected_segment_lengths(length, selected_layers)
    if not isinstance(observed_imbalances, tuple) or len(observed_imbalances) != len(
        selected_layers
    ):
        raise ValueError("observed_imbalances must match selected_layers")

    previous_imbalance = 0
    result = 1
    for segment, current_imbalance in zip(
        segments, observed_imbalances, strict=True
    ):
        if isinstance(current_imbalance, bool) or not isinstance(current_imbalance, int):
            raise ValueError("observed imbalances must be integers")
        increment = current_imbalance - previous_imbalance
        segment_fiber = imbalance_fiber_size(segment, increment)
        if segment_fiber == 0:
            return 0
        result *= segment_fiber
        previous_imbalance = current_imbalance
    return result * (2 ** tail)


def equal_observation_ordered_pair_count(
    length: int, selected_layers: tuple[int, ...]
) -> int:
    """Number of ordered word pairs sharing the selected-layer observation.

    On a constrained segment of length ell, summing squared binomial fiber
    sizes gives the Vandermonde identity

        sum_k C(ell,k)^2 = C(2ell,ell).

    Segment constraints factor. The final unobserved tail is arbitrary in both
    words and contributes ``4^tail``.
    """
    segments, tail = selected_segment_lengths(length, selected_layers)
    result = 4 ** tail
    for segment in segments:
        result *= comb(2 * segment, segment)
    return result


def collapsed_unordered_word_pair_count(
    length: int, selected_layers: tuple[int, ...]
) -> int:
    """Distinct unordered microscopic word pairs identified by the quotient."""
    ordered_equal = equal_observation_ordered_pair_count(length, selected_layers)
    identical_pairs = 2 ** length
    difference = ordered_equal - identical_pairs
    if difference < 0 or difference % 2:
        raise AssertionError("equal-observation ordered pairs must split into diagonal + reversals")
    return difference // 2


def final_imbalance_collapsed_pair_count(length: int) -> int:
    """Closed final-layer specialization ``(C(2N,N)-2^N)/2``."""
    _require_length(length)
    if length == 0:
        return 0
    return (comb(2 * length, length) - 2 ** length) // 2


def higher_collision_count(length: int, order: int) -> int:
    """P011-style order-k collision count for the final imbalance quotient.

    This is

        sum_delta C(|fiber_delta|, order).
    """
    _require_length(length)
    if isinstance(order, bool) or not isinstance(order, int) or order < 1:
        raise ValueError("order must be a positive integer")
    return sum(
        comb(fiber_size, order)
        for _, fiber_size in imbalance_fiber_spectrum(length)
        if fiber_size >= order
    )
