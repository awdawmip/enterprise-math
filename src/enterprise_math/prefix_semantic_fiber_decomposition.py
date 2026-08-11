"""Exact fibers of literal words under terminal/discovery/timing quotients.

Fix k generators and exact word length H.  Let s be the number of distinct
generators used by one word.

### Terminal set

For one fixed s-element terminal generator set, literal words in the fiber are
all surjections from H positions onto those s labels:

    fiber_terminal(H,s) = s! * S(H,s),

where S(H,s) is a Stirling number of the second kind.

### Discovery order

Fix one ordered first-appearance list `(g_1,...,g_s)`.  Relabeling each block of
positions by the order of its first occurrence gives the standard restricted-
growth-string bijection with set partitions into s blocks.  Hence

    fiber_discovery(H,s) = S(H,s).

### Full timing / run-length form

Fix one exact phase form with first-appearance order `(g_i)` and positive phase
durations `(r_i)`, sum r_i=H.  In phase i the first action must be the new
generator g_i.  Each remaining stutter position in that phase can use any of the
i already-seen generators without changing the prefix state.  Therefore

    fiber_timing(r_1,...,r_s) = product_i i^(r_i-1).

These timing fibers are highly nonuniform.  For fixed H,s their minimum is1
(all extra stutters placed in phase1) and maximum is s^(H-s) (all extra stutters
placed in the last phase).

Summing the timing fibers over all positive compositions of H into s parts gives
S(H,s), recovering the discovery-order fiber.  Multiplying by s! recovers the
terminal-set fiber.  Summing over terminal sets recovers k^H literal words.

Stirling numbers, surjections, restricted-growth strings and positive
compositions are standard prior combinatorics.  The Enterprise Math value is the
exact semantic-dedup fiber accounting across the Stage131 observation ladder.
"""

from __future__ import annotations

from functools import lru_cache
from itertools import combinations
from math import factorial
from typing import Iterable, Sequence

from .prefix_run_length_normal_form import PrefixRun


def _positive(name: str, value: int) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value < 1:
        raise ValueError(f"{name} must be a positive integer")
    return value


@lru_cache(maxsize=None)
def stirling_second_kind(total: int, blocks: int) -> int:
    if isinstance(total, bool) or not isinstance(total, int) or total < 0:
        raise ValueError("total must be a nonnegative integer")
    if isinstance(blocks, bool) or not isinstance(blocks, int) or blocks < 0:
        raise ValueError("blocks must be a nonnegative integer")
    if total == 0:
        return int(blocks == 0)
    if blocks == 0 or blocks > total:
        return 0
    if blocks == 1 or blocks == total:
        return 1
    return (
        blocks * stirling_second_kind(total - 1, blocks)
        + stirling_second_kind(total - 1, blocks - 1)
    )


def terminal_set_literal_fiber_size(word_length: int, distinct_generators: int) -> int:
    h = _positive("word_length", word_length)
    s = _positive("distinct_generators", distinct_generators)
    if s > h:
        return 0
    return factorial(s) * stirling_second_kind(h, s)


def discovery_order_literal_fiber_size(word_length: int, distinct_generators: int) -> int:
    h = _positive("word_length", word_length)
    s = _positive("distinct_generators", distinct_generators)
    if s > h:
        return 0
    return stirling_second_kind(h, s)


def timing_form_literal_fiber_size(
    phases: Sequence[PrefixRun],
    generator_count: int,
) -> int:
    k = _positive("generator_count", generator_count)
    values = tuple(phases)
    if not values:
        return 1
    seen = set()
    result = 1
    for index, phase in enumerate(values, start=1):
        if not isinstance(phase, PrefixRun):
            raise TypeError("phases must contain PrefixRun values")
        if (
            isinstance(phase.generator, bool)
            or not isinstance(phase.generator, int)
            or not 0 <= phase.generator < k
        ):
            raise ValueError("phase generator outside declared range")
        if phase.generator in seen:
            raise ValueError("phase generators must be distinct")
        seen.add(phase.generator)
        if (
            isinstance(phase.run_length, bool)
            or not isinstance(phase.run_length, int)
            or phase.run_length < 1
        ):
            raise ValueError("phase run length must be positive")
        result *= index ** (phase.run_length - 1)
    return result


def timing_fiber_minimum(word_length: int, distinct_generators: int) -> int:
    h = _positive("word_length", word_length)
    s = _positive("distinct_generators", distinct_generators)
    if s > h:
        raise ValueError("distinct_generators cannot exceed word_length")
    return 1


def timing_fiber_maximum(word_length: int, distinct_generators: int) -> int:
    h = _positive("word_length", word_length)
    s = _positive("distinct_generators", distinct_generators)
    if s > h:
        raise ValueError("distinct_generators cannot exceed word_length")
    return s ** (h - s)


def positive_compositions(total: int, parts: int) -> tuple[tuple[int, ...], ...]:
    h = _positive("total", total)
    s = _positive("parts", parts)
    if s > h:
        return ()
    if s == 1:
        return ((h,),)
    result = []
    for cuts in combinations(range(1, h), s - 1):
        boundaries = (0, *cuts, h)
        result.append(
            tuple(
                boundaries[index + 1] - boundaries[index]
                for index in range(s)
            )
        )
    return tuple(result)


def timing_fiber_size_from_durations(durations: Sequence[int]) -> int:
    values = tuple(durations)
    if not values:
        return 1
    result = 1
    for index, duration in enumerate(values, start=1):
        if isinstance(duration, bool) or not isinstance(duration, int) or duration < 1:
            raise ValueError("durations must be positive integers")
        result *= index ** (duration - 1)
    return result


def timing_fibers_sum_to_discovery_fiber(word_length: int, distinct_generators: int) -> bool:
    h = _positive("word_length", word_length)
    s = _positive("distinct_generators", distinct_generators)
    if s > h:
        raise ValueError("distinct_generators cannot exceed word_length")
    total = sum(
        timing_fiber_size_from_durations(composition)
        for composition in positive_compositions(h, s)
    )
    expected = discovery_order_literal_fiber_size(h, s)
    if total != expected:
        raise AssertionError("timing fibers failed to sum to discovery-order fiber")
    return True


def terminal_fiber_equals_order_factor(
    word_length: int,
    distinct_generators: int,
) -> bool:
    h = _positive("word_length", word_length)
    s = _positive("distinct_generators", distinct_generators)
    if s > h:
        raise ValueError("distinct_generators cannot exceed word_length")
    if terminal_set_literal_fiber_size(h, s) != (
        factorial(s) * discovery_order_literal_fiber_size(h, s)
    ):
        raise AssertionError("terminal fiber failed s!-times discovery law")
    return True


def literal_word_count_from_terminal_fibers(generator_count: int, word_length: int) -> int:
    k = _positive("generator_count", generator_count)
    h = _positive("word_length", word_length)
    total = 0
    from math import comb

    for s in range(1, min(k, h) + 1):
        total += comb(k, s) * terminal_set_literal_fiber_size(h, s)
    return total


def literal_word_count_from_discovery_fibers(generator_count: int, word_length: int) -> int:
    k = _positive("generator_count", generator_count)
    h = _positive("word_length", word_length)
    total = 0
    for s in range(1, min(k, h) + 1):
        ordered = factorial(k) // factorial(k - s)
        total += ordered * discovery_order_literal_fiber_size(h, s)
    return total
