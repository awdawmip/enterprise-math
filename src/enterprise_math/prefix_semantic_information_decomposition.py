"""Shannon-information decomposition of the prefix semantic quotient ladder.

Assume the literal length-H word is uniform on k^H words.  For any deterministic
quotient Q, conditioned on a semantic class q the literal words are uniform over
that quotient fiber.  Therefore

    H(W) = H(Q) + E[log2 |fiber(Q)|].

Apply this to the exact ladder

    literal -> full timing -> discovery order -> terminal set.

The semantic entropies satisfy

    H_terminal <= H_discovery <= H_timing <= H_literal.

The increments have exact meanings.

### Discovery-order information

For a word using S=s distinct generators, one terminal set contains s! equally
sized discovery-order fibers.  Hence

    H_discovery - H_terminal = E[log2(S!)].

### Duration information

Fix one discovery order with s generators.  A positive duration composition r
has literal fiber

    f(r)=product_i i^(r_i-1).

The induced duration probability is f(r)/Stirling(H,s).  The conditional entropy
of that duration distribution, averaged over S, is exactly

    H_timing - H_discovery.

### Stutter-provenance information

Within one timing class, the remaining literal ambiguity is which already-seen
generator produced each semantic stutter.  Its conditional entropy is

    log2 f(r).

Averaging over timing classes gives

    H_literal - H_timing.

Thus literal action information is partitioned exactly into terminal-set state,
first-discovery order, discovery timing, and stutter-action provenance.

Shannon entropy, Stirling occupancy distributions and deterministic quotient
chain rules are standard prior information theory/combinatorics.  The project
value is the exact semantic-precision information accounting.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import comb, factorial, log2

from .prefix_semantic_fiber_decomposition import (
    discovery_order_literal_fiber_size,
    positive_compositions,
    stirling_second_kind,
    terminal_set_literal_fiber_size,
    timing_fiber_size_from_durations,
)


def _positive(name: str, value: int) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value < 1:
        raise ValueError(f"{name} must be a positive integer")
    return value


def falling_factorial(total: int, selected: int) -> int:
    if not 0 <= selected <= total:
        raise ValueError("selected must lie in 0..total")
    return factorial(total) // factorial(total - selected)


def _entropy_from_equal_fiber_strata(
    total_words: int,
    strata: tuple[tuple[int, int], ...],
) -> float:
    """Entropy when each stratum gives (class_count, common_fiber_size)."""
    entropy = 0.0
    for class_count, fiber_size in strata:
        if class_count <= 0 or fiber_size <= 0:
            continue
        probability = fiber_size / total_words
        entropy += class_count * probability * (log2(total_words) - log2(fiber_size))
    return entropy


def literal_word_entropy_bits(generator_count: int, word_length: int) -> float:
    k = _positive("generator_count", generator_count)
    h = _positive("word_length", word_length)
    return h * log2(k)


def distinct_generator_count_probability(
    generator_count: int,
    word_length: int,
    distinct_generators: int,
) -> float:
    k = _positive("generator_count", generator_count)
    h = _positive("word_length", word_length)
    s = _positive("distinct_generators", distinct_generators)
    if s > min(k, h):
        return 0.0
    count = falling_factorial(k, s) * stirling_second_kind(h, s)
    return count / (k**h)


def terminal_semantic_entropy_bits(generator_count: int, word_length: int) -> float:
    k = _positive("generator_count", generator_count)
    h = _positive("word_length", word_length)
    total = k**h
    strata = tuple(
        (
            comb(k, s),
            terminal_set_literal_fiber_size(h, s),
        )
        for s in range(1, min(k, h) + 1)
    )
    return _entropy_from_equal_fiber_strata(total, strata)


def discovery_semantic_entropy_bits(generator_count: int, word_length: int) -> float:
    k = _positive("generator_count", generator_count)
    h = _positive("word_length", word_length)
    total = k**h
    strata = tuple(
        (
            falling_factorial(k, s),
            discovery_order_literal_fiber_size(h, s),
        )
        for s in range(1, min(k, h) + 1)
    )
    return _entropy_from_equal_fiber_strata(total, strata)


def timing_semantic_entropy_bits(generator_count: int, word_length: int) -> float:
    k = _positive("generator_count", generator_count)
    h = _positive("word_length", word_length)
    total = k**h
    entropy = 0.0
    for s in range(1, min(k, h) + 1):
        order_count = falling_factorial(k, s)
        for durations in positive_compositions(h, s):
            fiber = timing_fiber_size_from_durations(durations)
            probability = fiber / total
            entropy += order_count * probability * (log2(total) - log2(fiber))
    return entropy


def expected_discovery_order_information_bits(generator_count: int, word_length: int) -> float:
    k = _positive("generator_count", generator_count)
    h = _positive("word_length", word_length)
    return sum(
        distinct_generator_count_probability(k, h, s) * log2(factorial(s))
        for s in range(1, min(k, h) + 1)
    )


def duration_entropy_given_distinct_count_bits(word_length: int, distinct_generators: int) -> float:
    h = _positive("word_length", word_length)
    s = _positive("distinct_generators", distinct_generators)
    if s > h:
        raise ValueError("distinct_generators cannot exceed word_length")
    total = stirling_second_kind(h, s)
    if total <= 0:
        return 0.0
    entropy = 0.0
    for durations in positive_compositions(h, s):
        fiber = timing_fiber_size_from_durations(durations)
        probability = fiber / total
        entropy += probability * (log2(total) - log2(fiber))
    return entropy


def expected_duration_information_bits(generator_count: int, word_length: int) -> float:
    k = _positive("generator_count", generator_count)
    h = _positive("word_length", word_length)
    return sum(
        distinct_generator_count_probability(k, h, s)
        * duration_entropy_given_distinct_count_bits(h, s)
        for s in range(1, min(k, h) + 1)
    )


def expected_stutter_provenance_bits(generator_count: int, word_length: int) -> float:
    k = _positive("generator_count", generator_count)
    h = _positive("word_length", word_length)
    total = k**h
    result = 0.0
    for s in range(1, min(k, h) + 1):
        order_count = falling_factorial(k, s)
        for durations in positive_compositions(h, s):
            fiber = timing_fiber_size_from_durations(durations)
            if fiber == 1:
                continue
            probability_mass = order_count * fiber / total
            result += probability_mass * log2(fiber)
    return result


def quotient_conditional_literal_entropy_bits(
    generator_count: int,
    word_length: int,
    level: str,
) -> float:
    literal = literal_word_entropy_bits(generator_count, word_length)
    if level == "terminal":
        semantic = terminal_semantic_entropy_bits(generator_count, word_length)
    elif level == "discovery":
        semantic = discovery_semantic_entropy_bits(generator_count, word_length)
    elif level == "timing":
        semantic = timing_semantic_entropy_bits(generator_count, word_length)
    else:
        raise ValueError("level must be terminal, discovery, or timing")
    return literal - semantic


@dataclass(frozen=True)
class PrefixSemanticInformationReport:
    generator_count: int
    word_length: int
    literal_entropy_bits: float
    terminal_entropy_bits: float
    discovery_entropy_bits: float
    timing_entropy_bits: float
    discovery_order_information_bits: float
    duration_information_bits: float
    stutter_provenance_bits: float

    @property
    def decomposition_sum_bits(self) -> float:
        return (
            self.terminal_entropy_bits
            + self.discovery_order_information_bits
            + self.duration_information_bits
            + self.stutter_provenance_bits
        )

    @property
    def total_semantic_loss_at_terminal_bits(self) -> float:
        return self.literal_entropy_bits - self.terminal_entropy_bits


def prefix_semantic_information_report(
    generator_count: int,
    word_length: int,
) -> PrefixSemanticInformationReport:
    k = _positive("generator_count", generator_count)
    h = _positive("word_length", word_length)
    literal = literal_word_entropy_bits(k, h)
    terminal = terminal_semantic_entropy_bits(k, h)
    discovery = discovery_semantic_entropy_bits(k, h)
    timing = timing_semantic_entropy_bits(k, h)
    order_info = expected_discovery_order_information_bits(k, h)
    duration_info = expected_duration_information_bits(k, h)
    stutter = expected_stutter_provenance_bits(k, h)
    tolerance = 1e-10
    if abs((discovery - terminal) - order_info) > tolerance:
        raise AssertionError("discovery-order entropy increment failed exact expectation law")
    if abs((timing - discovery) - duration_info) > tolerance:
        raise AssertionError("timing entropy increment failed duration-entropy law")
    if abs((literal - timing) - stutter) > tolerance:
        raise AssertionError("literal/timing entropy gap failed stutter-provenance law")
    if abs(literal - (terminal + order_info + duration_info + stutter)) > tolerance:
        raise AssertionError("prefix semantic information decomposition failed chain rule")
    return PrefixSemanticInformationReport(
        generator_count=k,
        word_length=h,
        literal_entropy_bits=literal,
        terminal_entropy_bits=terminal,
        discovery_entropy_bits=discovery,
        timing_entropy_bits=timing,
        discovery_order_information_bits=order_info,
        duration_information_bits=duration_info,
        stutter_provenance_bits=stutter,
    )
