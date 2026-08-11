"""Exact prefix-observable word semantics for commuting idempotent OR actions.

Terminal transformation semantics for the k-bit OR family collapses a word to
one final mask: the set of generators that occur.  If the declared future
language observes the state after **every prefix**, that quotient is too coarse.

For a word w=a_1...a_H define cumulative masks

    U_t = mask(a_1) OR ... OR mask(a_t).

The exact prefix-observable normal form is the sequence

    tau(w)=(U_1,...,U_H).

For any initial state x the observed prefix-state sequence is

    (x OR U_1,...,x OR U_H).

Hence tau is sufficient for every initial state, and it is minimal/extensional:
starting from x=0 recovers tau itself.

Composition is still formulaic.  If left trace has final mask F, then

    tau(uv)=tau(u) ++ (F OR V_1,...,F OR V_|v|)

where `(V_i)=tau(v)`.

Unlike the terminal effect monoid, the prefix-trace operation algebra is infinite
for unbounded word length even when k=1: `a, a^2, ...` have one terminal effect
but traces of different lengths.

For exact word length H>=1, the number of distinct prefix traces is

    sum_{s=1}^{min(k,H)} P(k,s) * C(H-1,s-1),

where s is the number of distinct generators first introduced, P(k,s) chooses
their ordered identities, and C(H-1,s-1) chooses their remaining first-appearance
positions after the mandatory first discovery at position1.

The number of terminal masks at exact length H is only

    sum_{s=1}^{min(k,H)} C(k,s).

Thus prefix observability can restore large amounts of order/timing semantics
that terminal operation quotienting intentionally erases.

Prefix traces, semilattice actions and cumulative scans are standard prior
mathematics/CS.  The project value is the exact future-language boundary for
semantic word normalization.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import comb, factorial
from typing import Sequence

from .formulaic_idempotent_word_normal_form import word_mask_normal_form


def _generator_count(value: int) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value < 1:
        raise ValueError("generator_count must be a positive integer")
    return value


def _validate_word(word: Sequence[int], generator_count: int) -> tuple[int, ...]:
    k = _generator_count(generator_count)
    values = tuple(word)
    for generator in values:
        if isinstance(generator, bool) or not isinstance(generator, int) or not 0 <= generator < k:
            raise ValueError("word contains generator outside declared range")
    return values


def prefix_mask_trace(word: Sequence[int], generator_count: int) -> tuple[int, ...]:
    values = _validate_word(word, generator_count)
    current = 0
    result = []
    for generator in values:
        current |= 1 << generator
        result.append(current)
    return tuple(result)


def terminal_mask_from_prefix_trace(trace: Sequence[int], generator_count: int) -> int:
    k = _generator_count(generator_count)
    values = tuple(trace)
    if not values:
        return 0
    limit = 1 << k
    previous = 0
    for mask in values:
        if isinstance(mask, bool) or not isinstance(mask, int) or not 0 <= mask < limit:
            raise ValueError("trace mask outside semantic state space")
        if previous & ~mask:
            raise ValueError("prefix trace must be monotone under OR inclusion")
        previous = mask
    return values[-1]


def prefix_state_trace(
    initial_state: int,
    word: Sequence[int],
    generator_count: int,
) -> tuple[int, ...]:
    k = _generator_count(generator_count)
    limit = 1 << k
    if isinstance(initial_state, bool) or not isinstance(initial_state, int) or not 0 <= initial_state < limit:
        raise ValueError("initial_state outside k-bit state space")
    return tuple(initial_state | mask for mask in prefix_mask_trace(word, k))


def compose_prefix_mask_traces(
    left_trace: Sequence[int],
    right_trace: Sequence[int],
    generator_count: int,
) -> tuple[int, ...]:
    k = _generator_count(generator_count)
    left = tuple(left_trace)
    right = tuple(right_trace)
    left_final = terminal_mask_from_prefix_trace(left, k)
    terminal_mask_from_prefix_trace(right, k)
    return left + tuple(left_final | mask for mask in right)


def prefix_trace_composition_matches_words(
    left_word: Sequence[int],
    right_word: Sequence[int],
    generator_count: int,
) -> bool:
    k = _generator_count(generator_count)
    left = prefix_mask_trace(left_word, k)
    right = prefix_mask_trace(right_word, k)
    composed = compose_prefix_mask_traces(left, right, k)
    direct = prefix_mask_trace((*tuple(left_word), *tuple(right_word)), k)
    if composed != direct:
        raise AssertionError("prefix-trace composition disagreed with word concatenation")
    return True


def terminal_effect_matches_prefix_trace(
    word: Sequence[int],
    generator_count: int,
) -> bool:
    k = _generator_count(generator_count)
    final_from_trace = terminal_mask_from_prefix_trace(prefix_mask_trace(word, k), k)
    final_direct = word_mask_normal_form(word, k)
    if final_from_trace != final_direct:
        raise AssertionError("prefix trace final mask disagreed with terminal normal form")
    return True


def falling_factorial(total: int, selected: int) -> int:
    if not 0 <= selected <= total:
        raise ValueError("selected must lie in 0..total")
    return factorial(total) // factorial(total - selected)


def prefix_trace_count_exact_length(generator_count: int, word_length: int) -> int:
    k = _generator_count(generator_count)
    if isinstance(word_length, bool) or not isinstance(word_length, int) or word_length < 0:
        raise ValueError("word_length must be nonnegative")
    if word_length == 0:
        return 1
    return sum(
        falling_factorial(k, distinct) * comb(word_length - 1, distinct - 1)
        for distinct in range(1, min(k, word_length) + 1)
    )


def terminal_effect_count_exact_length(generator_count: int, word_length: int) -> int:
    k = _generator_count(generator_count)
    if isinstance(word_length, bool) or not isinstance(word_length, int) or word_length < 0:
        raise ValueError("word_length must be nonnegative")
    if word_length == 0:
        return 1
    return sum(comb(k, distinct) for distinct in range(1, min(k, word_length) + 1))


def full_support_prefix_trace_count(generator_count: int, word_length: int) -> int:
    k = _generator_count(generator_count)
    if isinstance(word_length, bool) or not isinstance(word_length, int) or word_length < 0:
        raise ValueError("word_length must be nonnegative")
    if word_length < k:
        return 0
    return factorial(k) * comb(word_length - 1, k - 1)


@dataclass(frozen=True)
class PrefixObservableWordCountReport:
    generator_count: int
    word_length: int
    literal_word_count: int
    terminal_effect_count: int
    prefix_trace_count: int
    full_support_prefix_trace_count: int

    @property
    def prefix_to_terminal_ratio(self) -> float:
        return self.prefix_trace_count / self.terminal_effect_count


def prefix_observable_word_count_report(
    generator_count: int,
    word_length: int,
) -> PrefixObservableWordCountReport:
    k = _generator_count(generator_count)
    if isinstance(word_length, bool) or not isinstance(word_length, int) or word_length < 0:
        raise ValueError("word_length must be nonnegative")
    literal = 1 if word_length == 0 else k**word_length
    return PrefixObservableWordCountReport(
        generator_count=k,
        word_length=word_length,
        literal_word_count=literal,
        terminal_effect_count=terminal_effect_count_exact_length(k, word_length),
        prefix_trace_count=prefix_trace_count_exact_length(k, word_length),
        full_support_prefix_trace_count=full_support_prefix_trace_count(k, word_length),
    )
